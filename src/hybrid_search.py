from sentence_transformers import SentenceTransformer, util
from src.parser import parse_chat
import numpy as np


# Load embedding model
model = SentenceTransformer(
    "paraphrase-multilingual-MiniLM-L12-v2"
)


# Load chat data
df = parse_chat("data/chat.txt")


# Create embeddings for all messages
message_embeddings = model.encode(
    df["message"].tolist(),
    convert_to_tensor=True,
    show_progress_bar=True
)


def hybrid_search(query, top_k=10):

    # -----------------------------
    # 1. Semantic score
    # -----------------------------

    query_embedding = model.encode(
        query,
        convert_to_tensor=True
    )

    semantic_scores = util.cos_sim(
        query_embedding,
        message_embeddings
    )[0]


    # -----------------------------
    # 2. Keyword score
    # -----------------------------

    query_words = query.lower().split()

    keyword_scores = []

    for message in df["message"]:

        message_lower = message.lower()

        score = 0

        for word in query_words:

            if word in message_lower:
                score += 1

        keyword_scores.append(score)


    # -----------------------------
    # 3. Normalize keyword score
    # -----------------------------

    max_keyword = max(keyword_scores)

    if max_keyword > 0:

        keyword_scores = [
            score / max_keyword
            for score in keyword_scores
        ]

    else:

        keyword_scores = [
            0
            for score in keyword_scores
        ]

    keyword_scores = np.array(keyword_scores)


    # -----------------------------
    # 4. Combine scores
    # -----------------------------

    final_scores = (
        0.7 * semantic_scores.cpu().numpy()
        +
        0.3 * keyword_scores
    )


    # -----------------------------
    # 5. Get top results
    # -----------------------------

    top_indexes = np.argsort(final_scores)[::-1][:top_k].copy()


    results = df.iloc[
        top_indexes
    ].copy()


    results["semantic_score"] = semantic_scores[
        top_indexes
    ].cpu().numpy()

    results["keyword_score"] = [
        keyword_scores[i]
        for i in top_indexes
    ]

    results["final_score"] = [
        final_scores[i]
        for i in top_indexes
    ]


    return results


# -----------------------------
# Test
# -----------------------------

if __name__ == "__main__":

    query = "When did we decide on the trip?"

    results = hybrid_search(
        query,
        top_k=10
    )

    print("\nQuery:", query)

    print("\nHybrid Search Results:\n")

    print(
        results[
            [
                "datetime",
                "sender",
                "message",
                "semantic_score",
                "keyword_score",
                "final_score"
            ]
        ].to_string(index=False)
    )