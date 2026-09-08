# 🔎 Search a Group Chat Properly

A simple and explainable **group chat search system** that allows users to search thousands of chat messages using natural-language queries.

The system combines **keyword-based search, semantic search, query understanding, and conversation context** to retrieve relevant messages from a large group chat.

---

## 📌 Project Overview

Searching through a large group chat manually can be difficult, especially when the chat contains:

* Thousands of messages
* Multiple participants
* Hinglish / code-mixed language
* Typos and informal language
* Very short replies like "yes", "done", "same"
* Forwarded messages
* Conversations spread across multiple messages
* Important decisions hidden inside long conversations

This project attempts to solve that problem by allowing users to search the chat using natural-language questions.

For example:

```text
Who suggested Manali as the destination?
```

Instead of manually scanning the entire chat, the system retrieves the relevant message:

```text
Aman: Manali kaisa rahega?
```

---

# 🎯 Problem Statement

Build a search system capable of retrieving relevant messages from a large synthetic group chat containing:

* 4,000+ messages
* 8 participants
* 6 months of conversation
* Informal Hinglish/code-mixed text
* Typos
* Forwarded messages
* Short contextual replies
* Multiple decision-making conversations

The system is evaluated using **40 test queries**, including semantic queries where the query and the correct message may have little or no exact word overlap.

---

# ✨ Features

## 1. Chat Parsing

The system parses the raw chat file and converts it into a structured format containing:

* Date
* Time
* Sender
* Message
* Datetime

Example:

```text
12/04/2026, 10:30 - Aman: Manali kaisa rahega?
```

is converted into structured data.

---

## 2. Keyword Search

The system uses traditional keyword matching to find messages containing important words from the user's query.

This works well when the query contains words that are directly present in the message.

Example:

```text
Which backend framework was selected?
```

can match:

```text
Aman: backend FastAPI
```

---

## 3. Semantic Search

The system also uses semantic similarity to find messages that are conceptually related to the query.

This helps when the exact words in the query are different from the words used in the chat.

For example:

```text
What was the maximum spending limit?
```

can be related to:

```text
Rohit: around 1500 per person max
```

even though the words are not exactly the same.

---

## 4. Query Understanding

The system performs basic query processing to identify useful information such as:

* Participant names
* Temporal expressions
* Search terms

Examples:

```text
Priya said what about the hotel?
```

```text
What happened last week?
```

This helps narrow down the search space.

---

## 5. Conversation Context

A single message is sometimes not enough to understand the meaning.

For example:

```text
Question:
Which place was finally selected?

Message:
Neha: Ring Road wala venue final karte hain
```

The system also displays nearby messages so that the user can understand the surrounding conversation.

This is especially useful for short replies such as:

```text
yes
done
same
perfect
okay
reject
```

---

## 6. Streamlit Interface

A simple Streamlit web interface is provided for interacting with the search system.

The user can:

1. Enter a natural-language query
2. Run the search
3. View the top results
4. See sender and timestamp
5. Read surrounding conversation context

---

# 🏗️ System Architecture

```text
                USER QUERY
                     │
                     ▼
            Query Understanding
                     │
                     ▼
              Candidate Search
                /          \
               /            \
              ▼              ▼
        Keyword Search   Semantic Search
               \            /
                \          /
                 ▼        ▼
                   Ranking
                     │
                     ▼
                Top 5 Results
                     │
                     ▼
             Conversation Context
                     │
                     ▼
                Streamlit UI
```

---

# 📂 Project Structure

```text
Search-Group-Chat/
│
├── .gitignore
├── PROJECT_STATUS.md
├── README.md
├── app.py
├── evaluate.py
├── generate_corpus.py
├── requirements.txt
├── test_queries.json
│
├── data/
│   └── chat.txt
│
└── src/
    ├── context.py
    ├── hybrid_search.py
    ├── parser.py
    ├── query_parser.py
    ├── search.py
    └── semantic_search.py
```

---

# 📊 Dataset

The project uses a synthetic group chat generated specifically for this project.

The dataset contains:

* **4146 total messages**
* **8 participants**
* Approximately **6 months of conversation**
* Normal casual messages
* Forwarded messages
* Decision-oriented conversations

The chat was generated using a fixed random seed so that the dataset remains reproducible.

---

# 👥 Participants

The synthetic group contains 8 participants:

```text
Rahul
Priya
Aman
Neha
Rohit
Ananya
Vikash
Sneha
```

---

# 🧵 Decision Threads

The dataset contains three important decision-making threads.

## 1. Manali Trip

The group discusses:

* Destination
* Budget
* Travel dates
* Hotel
* Transportation
* Activities

Final decision:

```text
Manali
11 April night departure
14 April return
```

---

## 2. Project Technology Stack

The group discusses:

* Python
* React
* Streamlit
* FastAPI
* SQLite
* PostgreSQL
* Docker

Final stack:

```text
Python + FastAPI + Streamlit + SQLite
```

---

## 3. Farewell Venue

The group discusses:

* Restaurant vs banquet
* Budget
* Parking
* Food
* Location
* Music
* Timing

Final decision:

```text
Ring Road venue
```

---

# 💬 Example Queries

The system can answer queries such as:

```text
Who suggested Manali as the destination?

Which backend framework was selected?

What stack was confirmed for the prototype?

Which venue did the group finally select?

What was the maximum budget per person?

When would the group return?

What food options were available?
```

---

# 🚀 Quick Start Demo

After starting the application, try these queries:

### Query 1

```text
Who suggested Manali as the destination?
```

Expected relevant message:

```text
Aman: Manali kaisa rahega?
```

### Query 2

```text
Which backend framework was selected?
```

Expected relevant message:

```text
Vikash: backend FastAPI kar sakte hain
```

### Query 3

```text
Which venue did the group finally select?
```

Expected relevant message:

```text
Neha: Ring Road wala venue final karte hain
```

### Query 4

```text
What was the maximum budget per person?
```

Expected relevant message:

```text
Rohit: around 1500 per person max
```

---

# ⚙️ How to Run the Project

Follow the steps below to run the project locally.

## 1. Clone the Repository

```bash
git clone https://github.com/AjayKumarPatel713/Search-Group-Chat.git
```

Move into the project directory:

```bash
cd Search-Group-Chat
```

---

## 2. Create a Virtual Environment

For Windows:

```bash
python -m venv venv
```

---

## 3. Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

After activation, the terminal should show something similar to:

```text
(venv) PS C:\...\Search-Group-Chat>
```

---

## 4. Install Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

---

## 5. Run the Streamlit Application

Start the application using:

```bash
streamlit run app.py
```

Streamlit will start the local web server and provide a browser URL.

Usually it will be available at:

```text
http://localhost:8501
```

Open the URL in your browser if it does not open automatically.

---

## 6. Search the Group Chat

Enter a natural-language query in the Streamlit interface.

For example:

```text
Who suggested Manali as the destination?
```

Other example queries:

```text
Which backend framework was selected?

Which venue did the group finally select?

What was the maximum budget per person?
```

The application will display:

* Search results
* Sender
* Timestamp
* Relevant message
* Conversation context

---

## 7. Run the Evaluation

The project contains 40 test queries in:

```text
test_queries.json
```

Run the evaluation using:

```bash
python evaluate.py
```

The script checks whether the expected message appears within the top 5 retrieved results.

Example output:

```text
================================
FINAL EVALUATION
================================
Total Queries: 40
Correct: 16
Wrong: 24
Accuracy: 40.00%
```

---

## 8. Generate the Dataset

If you want to regenerate the synthetic chat dataset, run:

```bash
python generate_corpus.py
```

The generated chat will be stored in:

```text
data/chat.txt
```

---

# 📈 Evaluation

The project contains **40 test queries** stored in:

```text
test_queries.json
```

Each test case contains:

* User query
* Expected relevant message

The evaluation checks whether the expected message appears within the **top 5 retrieved results**.

Run:

```bash
python evaluate.py
```

Current evaluation:

```text
Total Queries: 40
Correct: 16
Wrong: 24
Top-5 Accuracy: 40.00%
```

---

# 📌 Evaluation Method

For every query:

1. The query is sent to the search system.
2. The system retrieves the top 5 messages.
3. The expected message is compared with the retrieved messages.
4. If the expected message appears in the top 5, the query is counted as correct.

Formula:

```text
Accuracy =
Correct Queries / Total Queries × 100
```

Current result:

```text
16 / 40 × 100 = 40%
```

---

# ⚠️ Current Limitations

The current system is intentionally kept relatively simple and explainable.

Some limitations include:

### 1. Short Replies

Messages such as:

```text
yes
done
same
perfect
okay
```

are difficult to retrieve correctly without deeper conversation understanding.

### 2. Context Dependency

Some answers depend heavily on previous messages.

For example:

```text
Question:
Did everyone agree?

Message:
Rohit: haan done
```

The word "done" alone does not contain enough information.

### 3. Semantic Search Limitations

Semantic similarity can sometimes retrieve messages that are conceptually related but not the exact answer.

### 4. Informal Language

Hinglish, spelling mistakes and informal chat language make search more difficult.

Examples:

```text
krna
karna
kro
karo
scene kya hai
budget ka kya
```

These expressions can have similar meanings but different text representations.

---

# 🔮 Future Improvements

The system can be improved further using:

* Better embedding models
* More advanced reranking
* Conversation-level retrieval
* Better handling of short replies
* Entity extraction
* Named Entity Recognition
* Temporal reasoning
* Question-answer aware retrieval
* Better multilingual / Hinglish embeddings
* Learning-to-rank approaches
* LLM-based answer generation
* RAG-based conversational search

A future version could retrieve an entire conversation thread instead of treating every message independently.

---

# 🧠 Design Philosophy

The main goal of this project is not only retrieval accuracy but also **simplicity and explainability**.

The implementation intentionally combines understandable techniques:

```text
Query Understanding
        +
Keyword Search
        +
Semantic Search
        +
Ranking
        +
Conversation Context
```

This makes the system easier to understand, debug and explain during an interview.

---

# 🛠️ Technologies Used

* Python
* Pandas
* Regular Expressions
* Sentence Transformers / Embeddings
* Scikit-learn
* Streamlit
* JSON

---

# 📁 Important Files

### `app.py`

Streamlit frontend and user interface.

### `src/parser.py`

Parses the raw chat file into structured data.

### `src/search.py`

Main search logic.

### `src/query_parser.py`

Performs basic query understanding such as participant and time extraction.

### `src/semantic_search.py`

Handles semantic similarity based retrieval.

### `src/context.py`

Provides surrounding conversation context.

### `evaluate.py`

Evaluates the system against the 40 test queries.

### `test_queries.json`

Contains the evaluation queries and expected answers.

### `generate_corpus.py`

Generates the synthetic group chat dataset.

---

# 🔄 Example Search Flow

Suppose the user enters:

```text
What was the maximum budget per person?
```

The system performs:

```text
User Query
    ↓
Query Processing
    ↓
Keyword + Semantic Search
    ↓
Message Ranking
    ↓
Top 5 Results
    ↓
Conversation Context
```

A relevant result can be:

```text
Rohit
around 1500 per person max
```

The interface also provides surrounding messages to help understand the decision.

---

# 📌 Project Status

```text
Status: Completed Baseline
```

Current baseline:

```text
Dataset: 4146 messages
Participants: 8
Evaluation Queries: 40
Top-5 Accuracy: 40%
UI: Streamlit
Repository: Public GitHub
```

The current version focuses on having a **working, understandable and demonstrable search system** rather than maximizing retrieval accuracy at the cost of implementation complexity.

---

# 🎥 Demo

The project can be demonstrated through the Streamlit interface by:

1. Opening the application
2. Entering natural-language queries
3. Viewing retrieved messages
4. Inspecting conversation context
5. Testing different decision-related questions

Recommended demo queries:

```text
Who suggested Manali as the destination?

Which backend framework was selected?

Which venue did the group finally select?

What was the maximum budget per person?
```

---

# 💡 Key Learning

This project demonstrates practical concepts related to:

* Information Retrieval
* Keyword Search
* Semantic Search
* Embeddings
* Query Understanding
* Ranking
* Context Retrieval
* Natural Language Search
* Evaluation of Search Systems
* Building a search interface with Streamlit

---

# 👨‍💻 Author

**Ajay Kumar Patel**

GitHub:

https://github.com/AjayKumarPatel713

Project Repository:

https://github.com/AjayKumarPatel713/Search-Group-Chat

---

# ⭐ Conclusion

**Search a Group Chat Properly** demonstrates how a large and messy group conversation can be converted into a searchable system.

The project combines traditional keyword retrieval with semantic search and conversation context to provide more useful results than simple text matching.

The current implementation achieves a **40% Top-5 accuracy** on 40 evaluation queries while keeping the system relatively simple and explainable.
