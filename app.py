import streamlit as st

from src.parser import parse_chat
from src.search import search_chat
from src.context import get_context


# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Group Chat Search",
    page_icon="🔎",
    layout="wide"
)


# ==========================================
# LOAD CHAT DATA
# ==========================================

@st.cache_data
def load_chat():

    df = parse_chat(
        "data/chat.txt"
    )

    return df


df = load_chat()


# ==========================================
# UI
# ==========================================

st.title("🔎 Search a Group Chat Properly")

st.write(
    "Search your group chat using meaning, "
    "person, or time."
)

st.info(
    "Examples: "
    "When did we decide on the trip? | "
    "What did Priya say about the budget?"
)


# ==========================================
# SEARCH BOX
# ==========================================

query = st.text_input(
    "Enter your question",
    placeholder="e.g. When did we decide on the trip?"
)


search_button = st.button(
    "🔍 Search"
)


# ==========================================
# SEARCH
# ==========================================

if search_button:

    if not query.strip():

        st.warning(
            "Please enter a search query."
        )

    else:

        with st.spinner("Searching chat..."):

            results = search_chat(
                df,
                query,
                top_k=5
            )

        if len(results) == 0:

            st.warning(
                "No matching messages found."
            )

        else:

            st.success(
                f"Found {len(results)} relevant messages."
            )

            for i, (_, result) in enumerate(
                results.iterrows(),
                start=1
            ):

                st.markdown(
                    f"### Result {i}"
                )

                st.write(
                    f"**{result['sender']}**  "
                    f"• {result['datetime']}"
                )

                st.write(
                    result["message"]
                )

                if "similarity" in result:

                    st.caption(
                        f"Semantic similarity: "
                        f"{result['similarity']:.3f} | "
                        f"Final score: "
                        f"{result['final_score']:.3f}"
                    )


                # ==================================
                # CONTEXT
                # ==================================

                with st.expander(
                    "💬 Conversation Context"
                ):

                    context = get_context(
                        df,
                        result.name,
                        minutes=30
                    )

                    for _, message in context.iterrows():

                        if message.name == result.name:

                            st.markdown(
                                f"**➡️ {message['sender']}** "
                                f"• {message['datetime']}"
                            )

                            st.markdown(
                                f"**{message['message']}**"
                            )

                        else:

                            st.write(
                                f"{message['sender']} "
                                f"• {message['datetime']} "
                                f"— {message['message']}"
                            )

                st.divider()