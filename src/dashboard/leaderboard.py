import pandas as pd
import streamlit as st


def render_leaderboard(results):

    rows = []

    previous_score = None
    current_rank = 0

    medals = {
        1: "🥇",
        2: "🥈",
        3: "🥉"
    }

    for index, r in enumerate(results):

        if r["score"] != previous_score:
            current_rank = index + 1
            previous_score = r["score"]

        rank = medals.get(current_rank, str(current_rank))

        rows.append(
            {
                "Rank": rank,
                "Prompt": r["name"],
                "Score": r["score"],
            }
        )

    df = pd.DataFrame(rows)

    st.subheader("🏆 Leaderboard")

    st.dataframe(
        df,
        use_container_width=True,
    )