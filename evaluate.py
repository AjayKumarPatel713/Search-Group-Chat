import json

from src.parser import parse_chat
from src.search import search_chat


# ==========================================
# LOAD DATA
# ==========================================

df = parse_chat("data/chat.txt")


# ==========================================
# LOAD TEST QUERIES
# ==========================================

with open(
    "test_queries.json",
    "r",
    encoding="utf-8"
) as file:

    test_queries = json.load(file)


# ==========================================
# EVALUATION
# ==========================================

correct = 0
total = len(test_queries)


for i, test in enumerate(test_queries, start=1):

    query = test["query"]
    expected = test["expected_message"]

    results = search_chat(
        df,
        query,
        top_k=5
    )

    retrieved_messages = (
        results["message"]
        .tolist()
        if len(results) > 0
        else []
    )

    hit = expected in retrieved_messages

    if hit:
        correct += 1

    print("\n--------------------------------")
    print("Query:", query)
    print("Expected:", expected)
    print("Retrieved:")

    for message in retrieved_messages:
        print(" -", message)

    print("Result:", "PASS" if hit else "FAIL")


# ==========================================
# FINAL RESULT
# ==========================================

accuracy = (
    correct / total * 100
    if total > 0
    else 0
)

print("\n================================")
print("FINAL EVALUATION")
print("================================")

print("Total Queries:", total)
print("Correct:", correct)
print("Wrong:", total - correct)

print(
    f"Accuracy: {accuracy:.2f}%"
)