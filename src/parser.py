import re
import pandas as pd


# ==========================================
# WHATSAPP MESSAGE PATTERN
# ==========================================

MESSAGE_PATTERN = re.compile(
    r"^(\d{2}/\d{2}/\d{4}),\s*(\d{2}:\d{2})\s*-\s*([^:]+):\s*(.*)$"
)


# ==========================================
# PARSE CHAT
# ==========================================

def parse_chat(file_path):

    messages = []

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        for line in file:

            line = line.strip()

            if not line:
                continue

            match = MESSAGE_PATTERN.match(line)

            if not match:
                continue

            date, time, sender, message = match.groups()

            datetime_value = pd.to_datetime(
                f"{date} {time}",
                format="%d/%m/%Y %H:%M"
            )

            messages.append({
                "datetime": datetime_value,
                "sender": sender.strip(),
                "message": message.strip()
            })

    return pd.DataFrame(messages)


# ==========================================
# TEST
# ==========================================

if __name__ == "__main__":

    file_path = "data/chat.txt"

    df = parse_chat(file_path)

    print(
        "Total parsed messages:",
        len(df)
    )

    print(
        "\nFirst 5 messages:\n"
    )

    print(
        df.head()
    )

    print(
        "\nColumns:"
    )

    print(
        df.columns.tolist()
    )