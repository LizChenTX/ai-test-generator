import streamlit as st


def render_metrics(results):

    if not results:
        return


    total = len(results)

    best = results[0]["score"]

    avg = round(
        sum(r["score"] for r in results)
        / total,
        2
    )

    best_score = max(
    r["score"]
    for r in results
    )

    winners = [
        r["name"]
        for r in results
        if r["score"] == best_score
        ]
    if len(winners) == 1:
        winner = winners[0]
    else:
        winner = "Tie: " + ", ".join(winners)


    st.subheader(
        "📊 Experiment Metrics"
    )


    col1,col2,col3,col4 = st.columns(4)


    col1.metric(
        "Experiments",
        total
    )


    col2.metric(
        "Best Score",
        best
    )


    col3.metric(
        "Average Score",
        avg
    )


    col4.metric(
        "Winner",
        winner
    )