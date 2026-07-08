import streamlit as st


def render_prompt_viewer(results):

    if not results:
        return

    st.subheader("📝 Prompt Detail")

    names = [

        r["name"]

        for r in results

    ]

    selected = st.selectbox(

        "Choose Prompt",

        names

    )

    current = next(

        r

        for r in results

        if r["name"] == selected

    )

    st.code(

        current["prompt"],

        language="text"

    )