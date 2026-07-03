import pandas as pd
import streamlit as st

def render_leaderboard(results):
    rows = []

    medals = ["🥇", "🥈", "🥉"]

    for i, r in enumerate(results):
        if i < 3:
            rank = medals[i]
        else:
            rank = str(i + 1)

        rows.append(
            {
                "Rank": rank,
                "Prompt": r["name"],
                "Score": r["score"],
                }
        )

    df = pd.DataFrame(rows)

    st.subheader("🏆 Leaderboard")
    st.dataframe(df, use_container_width=True)