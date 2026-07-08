import matplotlib.pyplot as plt
import streamlit as st


def render_chart(results):

    scores = [
        r["score"]
        for r in results
    ]

    prompts = [
        r["name"]
        for r in results
    ]

    fig, ax = plt.subplots()

    bars = ax.bar(
        prompts,
        scores
    )

    ax.set_ylabel(
        "Score"
    )

    ax.set_title(
        "Prompt Performance"
    )

    ax.bar_label(
        bars
    )

    st.pyplot(fig)