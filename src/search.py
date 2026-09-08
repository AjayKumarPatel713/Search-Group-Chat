import re
import numpy as np

from src.parser import parse_chat
from src.query_parser import parse_query

from sentence_transformers import SentenceTransformer, util


# ==========================================
# LOAD MODEL
# ==========================================

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# ==========================================
# STOPWORDS
# ==========================================

STOPWORDS = {
    "what", "where", "when", "who", "why",
    "how", "did", "does", "do", "the",
    "a", "an", "is", "was", "were",
    "they", "we", "he", "she", "it",
    "for", "to", "of", "on", "in",
    "about", "and", "or", "as",
    "will", "would", "could",
    "can", "their", "there",
    "finally", "decide", "decided",
    "group", "say", "said",
    "tell", "me", "please",
    "be", "at"
}


# ==========================================
# GENERIC / NOISY MESSAGES
# ==========================================

GENERIC_MESSAGES = {
    "done",
    "done 👍",
    "okay",
    "ok",
    "ok 👍",
    "perfect",
    "agree",
    "nice",
    "same",
    "yes",
    "haan",
    "haan done",
    "lets build",
    "sounds good",
    "we need to finalize this"
}


# ==========================================
# IMPORTANT DECISION WORDS
# ==========================================

DECISION_WORDS = {
    "final",
    "finalized",
    "confirm",
    "confirmed",
    "fix",
    "fixed",
    "selected",
    "choose",
    "chosen",
    "decision",
    "decide",
    "lock",
    "locked",
    "done"
}


# ==========================================
# TOKENIZE
# ==========================================

def tokenize(text):

    words = re.findall(
        r"[a-zA-Z0-9]+",
        str(text).lower()
    )

    return [
        word
        for word in words
        if word not in STOPWORDS
    ]


# ==========================================
# KEYWORD SCORE
# ==========================================

def keyword_score(query, message):

    query_words = tokenize(query)
    message_lower = str(message).lower()

    if not query_words:
        return 0.0

    matched = 0

    for word in query_words:

        if word in message_lower:
            matched += 1

    return matched / len(query_words)


# ==========================================
# EXACT PHRASE SCORE
# ==========================================

def phrase_score(query, message):

    query_words = tokenize(query)

    message_lower = str(message).lower()

    if len(query_words) < 2:
        return 0.0

    # Check small phrases from query
    for size in [4, 3, 2]:

        if len(query_words) >= size:

            for i in range(
                len(query_words) - size + 1
            ):

                phrase = " ".join(
                    query_words[i:i + size]
                )

                if phrase in message_lower:
                    return 1.0

    return 0.0


# ==========================================
# DECISION SCORE
# ==========================================

def decision_score(message):

    text = str(message).lower()

    score = 0.0

    for word in DECISION_WORDS:

        if word in text:
            score += 0.15

    return min(score, 0.45)


# ==========================================
# GENERIC MESSAGE PENALTY
# ==========================================

def generic_penalty(message):

    text = str(message).strip().lower()

    if text in GENERIC_MESSAGES:
        return 0.35

    # Very short generic messages
    if len(text.split()) <= 2:

        if text in {
            "done",
            "okay",
            "ok",
            "perfect",
            "agree",
            "same",
            "yes",
            "haan"
        }:
            return 0.30

    return 0.0


# ==========================================
# SEARCH CHAT
# ==========================================

def search_chat(
    df,
    query,
    top_k=5
):

    if df.empty:
        return df

    # ==========================================
    # QUERY PARSING
    # ==========================================

    parsed = parse_query(
        query,
        reference_date=df["datetime"].max()
    )

    search_query = parsed["search_query"]

    # ==========================================
    # FILTER DATA
    # ==========================================

    filtered_df = df.copy()

    # ------------------------------------------
    # SENDER FILTER
    # ------------------------------------------

    if parsed["sender"]:

        filtered_df = filtered_df[
            filtered_df["sender"].str.lower()
            ==
            parsed["sender"].lower()
        ]

    # ------------------------------------------
    # DATE FILTER
    # ------------------------------------------

    if parsed["start_date"] is not None:

        filtered_df = filtered_df[
            filtered_df["datetime"]
            >=
            parsed["start_date"]
        ]

    if parsed["end_date"] is not None:

        filtered_df = filtered_df[
            filtered_df["datetime"]
            <=
            parsed["end_date"]
        ]

    # ==========================================
    # EMPTY RESULT
    # ==========================================

    if filtered_df.empty:
        return filtered_df

    # ==========================================
    # SEMANTIC SEARCH
    # ==========================================

    messages = (
        filtered_df["message"]
        .fillna("")
        .astype(str)
        .tolist()
    )

    query_embedding = model.encode(
        search_query,
        convert_to_tensor=True
    )

    message_embeddings = model.encode(
        messages,
        convert_to_tensor=True
    )

    semantic_scores = util.cos_sim(
        query_embedding,
        message_embeddings
    )[0].cpu().numpy()

    # ==========================================
    # CALCULATE FINAL SCORE
    # ==========================================

    final_scores = []

    for i, message in enumerate(messages):

        semantic = float(
            semantic_scores[i]
        )

        keyword = keyword_score(
            search_query,
            message
        )

        phrase = phrase_score(
            search_query,
            message
        )

        decision = decision_score(
            message
        )

        penalty = generic_penalty(
            message
        )

        # --------------------------------------
        # FINAL RANKING
        # --------------------------------------

        score = (
            semantic * 0.45
            +
            keyword * 0.40
            +
            phrase * 0.30
            +
            decision
            -
            penalty
        )

        final_scores.append(score)

    # ==========================================
    # ADD SCORES
    # ==========================================

    result_df = filtered_df.copy()

    result_df["semantic_score"] = semantic_scores

    result_df["final_score"] = final_scores

    # ==========================================
    # SORT
    # ==========================================

    result_df = result_df.sort_values(
        by="final_score",
        ascending=False
    )

    # ==========================================
    # TOP K
    # ==========================================

    return result_df.head(top_k)


# ==========================================
# TEST
# ==========================================

if __name__ == "__main__":

    df = parse_chat(
        "data/chat.txt"
    )

    print(
        "Total messages:",
        len(df)
    )

    print(
        "Earliest message:",
        df["datetime"].min()
    )

    print(
        "Latest message:",
        df["datetime"].max()
    )

    # ======================================
    # TEST QUERIES
    # ======================================

    queries = [

        "Where did the group decide to go for the trip?",

        "What technology stack did the group choose?",

        "Which database was finally chosen?",

        "Which venue did the group finally select?",

        "What time was the venue available?",

        "Who suggested Manali as the destination?"

    ]

    for query in queries:

        print("\n================================")
        print("QUERY:", query)
        print("================================")

        results = search_chat(
            df,
            query,
            top_k=5
        )

        for _, row in results.iterrows():

            print(
                f"{row['datetime']} | "
                f"{row['sender']} | "
                f"{row['message']} | "
                f"score={row['final_score']:.3f}"
            )