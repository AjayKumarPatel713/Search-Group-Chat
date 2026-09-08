from src.parser import parse_chat
import pandas as pd


def get_context(df, index, minutes=30):

    target_time = df.loc[index, "datetime"]

    start_time = target_time - pd.Timedelta(minutes=minutes)
    end_time = target_time + pd.Timedelta(minutes=minutes)

    context = df[
        (df["datetime"] >= start_time) &
        (df["datetime"] <= end_time)
    ].copy()

    return context


if __name__ == "__main__":

    df = parse_chat("data/chat.txt")

    # Example: message containing "chalo Manali fix hai"
    matches = df[
        df["message"].str.contains(
            "chalo Manali fix hai",
            case=False,
            na=False
        )
    ]

    if len(matches) > 0:

        index = matches.index[0]

        context = get_context(
            df,
            index,
            minutes=30
        )

        print("\nConversation Context:\n")

        print(
            context[
                ["datetime", "sender", "message"]
            ].to_string(index=False)
        )