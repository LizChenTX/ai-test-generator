import streamlit as st


def render_metrics(results):

    if not results:
        return

    total = len(results)

    best_score = max(
        r["score"]
        for r in results
    )

    avg = round(

        sum(
            r["score"]
            for r in results
        ) / total,

        2

    )

    winners = [

        r["name"]

        for r in results

        if r["score"] == best_score

    ]

    if len(winners) == 1:

        winner = winners[0]

    else:

        winner = f"{len(winners)} prompts"

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Experiments",
        total
    )

    col2.metric(
        "Best Score",
        best_score
    )

    col3.metric(
        "Average Score",
        avg
    )

    col4.metric(
        "Winner",
        winner
    )