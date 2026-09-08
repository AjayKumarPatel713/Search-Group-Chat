from sentence_transformers import SentenceTransformer, util
from src.parser import parse_chat


# 1. Load the embedding model
model = SentenceTransformer(
    "paraphrase-multilingual-MiniLM-L12-v2"
)


# 2. Load chat data
df = parse_chat("data/chat.txt")


# 3. Create embeddings for all messages
message_embeddings = model.encode(
    df["message"].tolist(),
    convert_to_tensor=True,
    show_progress_bar=True
)


def semantic_search(query, top_k=10):
    """
    Search messages based on semantic meaning.
    """

    # 4. Convert user query into embedding
    query_embedding = model.encode(
        query,
        convert_to_tensor=True
    )

    # 5. Calculate similarity between query and all messages
    similarities = util.cos_sim(
        query_embedding,
        message_embeddings
    )[0]

    # 6. Get top matching message indexes
    top_results = similarities.argsort(
        descending=True
    )[:top_k]

    # 7. Create result dataframe
    results = df.iloc[
        top_results.cpu().numpy()
    ].copy()

    # 8. Add similarity score
    results["similarity"] = similarities[
        top_results
    ].cpu().numpy()

    return results


# Test
if __name__ == "__main__":

    query = "When did we decide on the trip?"

    results = semantic_search(
        query,
        top_k=10
    )

    print("\nQuery:", query)

    print("\nTop Results:\n")

    print(
        results[
            ["datetime", "sender", "message", "similarity"]
        ].to_string(index=False)
    )