# Search a Group Chat Properly

A semantic and keyword-based search system for finding relevant messages from large, messy group-chat conversations.

The project is designed to handle realistic group-chat data containing Hinglish/code-mixed messages, typos, short replies, forwarded messages, participant names, and decision-related conversations.

---

## 📌 Project Overview

Searching a large group chat using simple keyword matching is often difficult.

For example, a user may ask:

> "Where did the group decide to go for the trip?"

But the actual message in the chat may be:

> "chalo Manali fix hai"

The words in the query and the actual message may have little or no direct overlap.

This project combines **keyword search and semantic search** to retrieve relevant messages from a large group-chat dataset.

The system also displays the surrounding conversation context so that the user can understand why a particular message was retrieved.

---

## 🎯 Problem Statement

Build a system that can search a large group chat and retrieve relevant messages for natural-language queries.

The dataset contains:

* 4,000+ messages
* 8 participants
* 6 months of conversation
* Hinglish / code-mixed text
* Typos and informal language
* Short replies
* Forwarded messages
* Multiple decision-making conversations

The system was evaluated using **40 manually created test queries**.

---

## ✨ Features

### 1. Chat Parsing

The system reads chat messages from a `.txt` file and extracts:

* Date
* Time
* Sender
* Message

Example:

```text
15/02/2026, 21:08 - Rahul: chalo Manali fix hai
```

is converted into structured data.

---

### 2. Keyword Search

The system searches for important words from the user's query inside the chat messages.

This helps when the query contains words that directly occur in the conversation.

---

### 3. Semantic Search

The system also uses semantic similarity to find messages that are conceptually related to the query, even when exact words are different.

For example:

```text
Query:
Who suggested Manali as the destination?

Relevant message:
Manali kaisa rahega?
```

---

### 4. Query Understanding

The system can identify useful information from a query such as:

* Participant name
* Temporal expressions
* Search terms

Supported temporal expressions include:

```text
today
yesterday
this week
last week
this month
last month
```

---

### 5. Conversation Context

For each retrieved result, the application displays surrounding messages.

Example:

```text
Sneha: budget kitna hai?
Rohit: around 1500 per person max
Vikash: restaurant me ho jayega
```

This makes the search result easier to understand.

---

### 6. Streamlit Interface

The project provides a simple Streamlit web interface where users can enter a natural-language query and view the retrieved messages with their conversation context.

---

## 🏗️ System Architecture

```text
                 Group Chat (.txt)
                        |
                        v
                 Chat Parser
                        |
                        v
              Structured Messages
                        |
                        v
                 User Query
                        |
                        v
               Query Understanding
                        |
                        v
              Candidate Retrieval
                 /           \
                /             \
       Keyword Search     Semantic Search
                \             /
                 \           /
                  v         v
                     Ranking
                        |
                        v
                   Top Results
                        |
                        v
              Conversation Context
                        |
                        v
                  Streamlit UI
```

---

## 📂 Project Structure

```text
Search-Group-Chat/
│
├── data/
│   └── chat.txt
│
├── src/
│   ├── parser.py
│   ├── search.py
│   ├── semantic_search.py
│   ├── query_parser.py
│   └── context.py
│
├── app.py
├── generate_corpus.py
├── evaluate.py
├── test_queries.json
├── requirements.txt
├── PROJECT_STATUS.md
└── .gitignore
```

---

## 📊 Dataset

The synthetic dataset contains:

| Property           |               Value |
| ------------------ | ------------------: |
| Total messages     |               4,146 |
| Participants       |                   8 |
| Time period        | January – June 2026 |
| Normal messages    |               4,000 |
| Forwarded messages |                  30 |
| Decision threads   |                   3 |

### Participants

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

## 🧵 Decision Threads

The dataset contains three major decision-making conversations.

### 1. Manali Trip

The group discusses:

* Destination
* Budget
* Travel method
* Dates
* Hotel
* Activities
* Final confirmation

Final decision:

```text
chalo Manali fix hai
```

---

### 2. Project Technology Stack

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

### 3. Farewell Venue

The group discusses:

* Restaurant vs banquet
* Budget
* Parking
* Location
* Food
* Music
* Cake
* Timing

Final decision:

```text
Ring Road wala venue final karte hain
```

---

## 🔎 Example Queries

The system can answer queries such as:

```text
Who suggested Manali as the destination?

Which backend framework was selected?

What stack was confirmed for the prototype?

Which venue did the group finally select?

What was the maximum budget per person?

Did the chosen venue have parking?

What food options were available?

What did Priya say about the hotel budget?
```

---

## 📈 Evaluation

The system was evaluated using **40 manually created queries**.

The queries cover different types of searches including:

* Semantic queries
* Participant-specific queries
* Decision-related queries
* Temporal queries
* Budget-related queries
* Technology-related queries
* Venue-related queries

A query is considered correct when the expected relevant message appears in the **Top-5 retrieved results**.

### Final Evaluation

```text
Total Queries: 40
Correct: 16
Wrong: 24
Accuracy: 40.00%
```

### Top-5 Retrieval Accuracy

**40.00%**

---

## ⚠️ Current Limitations

The current system is intentionally kept simple and explainable.

The main limitation is **conversation-level context**.

For example:

```text
Vikash: toh final stack confirm?
Rahul: Python + FastAPI + Streamlit + SQLite
```

If the query asks:

```text
What was the final technology stack?
```

the system may sometimes retrieve the question message instead of the following answer.

Similarly, very short replies such as:

```text
yes
done
nahi
then reject
```

can be difficult to retrieve correctly without deeper conversation understanding.

---

## 🚀 Future Improvements

Possible improvements include:

* Conversation-level retrieval
* Better handling of short replies
* Answer-aware ranking
* Improved query intent detection
* Better temporal reasoning
* Entity-aware retrieval
* Retrieval of multiple related messages
* Reranking using a stronger language model
* Better evaluation dataset with more diverse queries

---

## 🛠️ Technologies Used

* Python
* Pandas
* Streamlit
* Regular Expressions
* Sentence Transformers
* Semantic Search
* Keyword Search
* JSON

---

## ⚙️ Installation

Clone the repository:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Move into the project directory:

```bash
cd Search-Group-Chat
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will open in the browser.

Enter a natural-language query and the system will return the most relevant messages along with conversation context.

---

## 🧪 Running Evaluation

To run the 40-query evaluation:

```bash
python evaluate.py
```

The script reports:

* Total queries
* Correct results
* Wrong results
* Final Top-5 accuracy

---

## 💡 Design Philosophy

The primary goal of this project was not to build an overly complicated search engine.

Instead, the focus was on building a system that is:

* Simple
* Explainable
* Easy to test
* Easy to extend
* Suitable for real-world group-chat search

The current version provides a baseline that can be improved with more advanced conversation-level retrieval techniques.

---

## 📌 Project Status

**Current Status: Working Prototype**

Completed:

* [x] Synthetic chat corpus generation
* [x] Chat parser
* [x] Keyword search
* [x] Semantic search
* [x] Query understanding
* [x] Conversation context display
* [x] Streamlit interface
* [x] 40-query evaluation
* [x] Final evaluation

Current Top-5 Accuracy:

**40.00%**

---

## 👨‍💻 Author

**Ajay Kumar Patel**

This project was developed as a practical information-retrieval and semantic-search project focused on searching large group-chat conversations.
