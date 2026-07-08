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

    st.markdown("### 📄 Prompt")
    st.code(
        current["prompt"],
        language="text"
    )

    st.markdown("### ⭐ Score")
    st.metric(
         "Score",
         current["score"]
         )
    
    st.markdown("### 🧪 Generated Test Cases")
    for case in current["result"]:
        st.write(
            f"✅ {case.category}"
            )