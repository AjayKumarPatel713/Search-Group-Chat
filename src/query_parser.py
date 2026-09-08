import re
from datetime import datetime, timedelta


PARTICIPANTS = [
    "Rahul",
    "Priya",
    "Aman",
    "Neha",
    "Rohit",
    "Ananya",
    "Vikash",
    "Sneha"
]


def parse_query(query, reference_date=None):

    result = {
        "original_query": query,
        "sender": None,
        "start_date": None,
        "end_date": None,
        "search_query": query
    }

    # ==========================================
    # REFERENCE DATE
    # ==========================================

    now = reference_date if reference_date else datetime.now()

    # ==========================================
    # DETECT SENDER
    # ==========================================

    for person in PARTICIPANTS:

        if re.search(
            rf"\b{person}\b",
            query,
            re.IGNORECASE
        ):

            result["sender"] = person

            result["search_query"] = re.sub(
                rf"\b{person}\b",
                "",
                result["search_query"],
                flags=re.IGNORECASE
            )

            break

    # ==========================================
    # TEMPORAL QUERY
    # ==========================================

    query_lower = query.lower()

    # ------------------------------------------
    # TODAY
    # ------------------------------------------

    if "today" in query_lower:

        start_date = now.replace(
            hour=0,
            minute=0,
            second=0,
            microsecond=0
        )

        end_date = now.replace(
            hour=23,
            minute=59,
            second=59,
            microsecond=999999
        )

        result["start_date"] = start_date
        result["end_date"] = end_date

        result["search_query"] = re.sub(
            r"\btoday\b",
            "",
            result["search_query"],
            flags=re.IGNORECASE
        )

    # ------------------------------------------
    # YESTERDAY
    # ------------------------------------------

    elif "yesterday" in query_lower:

        yesterday = now - timedelta(days=1)

        start_date = yesterday.replace(
            hour=0,
            minute=0,
            second=0,
            microsecond=0
        )

        end_date = yesterday.replace(
            hour=23,
            minute=59,
            second=59,
            microsecond=999999
        )

        result["start_date"] = start_date
        result["end_date"] = end_date

        result["search_query"] = re.sub(
            r"\byesterday\b",
            "",
            result["search_query"],
            flags=re.IGNORECASE
        )

    # ------------------------------------------
    # THIS WEEK
    # ------------------------------------------

    elif "this week" in query_lower:

        start_date = (
            now - timedelta(days=now.weekday())
        ).replace(
            hour=0,
            minute=0,
            second=0,
            microsecond=0
        )

        end_date = now.replace(
            hour=23,
            minute=59,
            second=59,
            microsecond=999999
        )

        result["start_date"] = start_date
        result["end_date"] = end_date

        result["search_query"] = re.sub(
            r"\bthis week\b",
            "",
            result["search_query"],
            flags=re.IGNORECASE
        )

    # ------------------------------------------
    # LAST WEEK
    # ------------------------------------------

    elif "last week" in query_lower:

        start_of_this_week = (
            now - timedelta(days=now.weekday())
        ).replace(
            hour=0,
            minute=0,
            second=0,
            microsecond=0
        )

        start_date = start_of_this_week - timedelta(days=7)

        end_date = start_of_this_week - timedelta(
            seconds=1
        )

        result["start_date"] = start_date
        result["end_date"] = end_date

        result["search_query"] = re.sub(
            r"\blast week\b",
            "",
            result["search_query"],
            flags=re.IGNORECASE
        )

    # ------------------------------------------
    # THIS MONTH
    # ------------------------------------------

    elif "this month" in query_lower:

        start_date = now.replace(
            day=1,
            hour=0,
            minute=0,
            second=0,
            microsecond=0
        )

        end_date = now.replace(
            hour=23,
            minute=59,
            second=59,
            microsecond=999999
        )

        result["start_date"] = start_date
        result["end_date"] = end_date

        result["search_query"] = re.sub(
            r"\bthis month\b",
            "",
            result["search_query"],
            flags=re.IGNORECASE
        )

    # ------------------------------------------
    # LAST MONTH
    # ------------------------------------------

    elif "last month" in query_lower:

        first_day_this_month = now.replace(
            day=1,
            hour=0,
            minute=0,
            second=0,
            microsecond=0
        )

        end_date = first_day_this_month - timedelta(
            seconds=1
        )

        start_date = end_date.replace(
            day=1,
            hour=0,
            minute=0,
            second=0,
            microsecond=0
        )

        result["start_date"] = start_date
        result["end_date"] = end_date

        result["search_query"] = re.sub(
            r"\blast month\b",
            "",
            result["search_query"],
            flags=re.IGNORECASE
        )

    # ==========================================
    # CLEAN SEARCH QUERY
    # ==========================================

    result["search_query"] = re.sub(
        r"\s+",
        " ",
        result["search_query"]
    ).strip()

    result["search_query"] = re.sub(
        r"\s+([?.!,])",
        r"\1",
        result["search_query"]
    )

    # ==========================================
    # IMPORTANT
    # ==========================================

    return result


# ==========================================
# TEST
# ==========================================

if __name__ == "__main__":

    queries = [
        "What did Priya say about the budget?",
        "What did we discuss today?",
        "What did we discuss yesterday?",
        "What did we discuss this week?",
        "What did we discuss last week?",
        "What did we discuss this month?",
        "What did we discuss last month?"
    ]

    reference_date = datetime(2026, 6, 30, 23, 28)

    for query in queries:

        print("\nQuery:", query)

        parsed = parse_query(
            query,
            reference_date=reference_date
        )

        print(parsed)