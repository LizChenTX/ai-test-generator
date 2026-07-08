import streamlit as st


def render_prompt_viewer(results):

    if not results:
        return

    st.subheader("📝 Prompt Detail")

    with st.container(border=True):

        selected_index = st.selectbox(
            "Choose Prompt",
            range(len(results)),
            format_func=lambda i: results[i]["name"]
            )

        current = results[selected_index]

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