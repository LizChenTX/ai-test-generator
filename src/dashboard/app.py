import streamlit as st
import matplotlib.pyplot as plt

from src.service.prompt_optimizer import PromptOptimizer
from src.generator.fake_llm import FakeLLM
from src.evaluator.quality_evaluator import QualityEvaluator
from src.service.prompt_mutator import PromptMutator
from src.service.experiment_tracker import ExperimentTracker

from src.dashboard.components import render_title
from src.dashboard.metrics import render_metrics
from src.dashboard.leaderboard import render_leaderboard
from src.dashboard.prompt_viewer import render_prompt_viewer


render_title()

# -----------------------------
# Siderbar
# -----------------------------
st.sidebar.header(
    "⚙️ Experiment Settings"
)
requirement = st.sidebar.text_area(
    "Requirement",
    value="login api",
    height=120
)
st.sidebar.caption(
    "Example: login api, payment api, shopping cart"
)

# -----------------------------
# Session State
# -----------------------------
if "results" not in st.session_state:
    st.session_state["results"] = []


# -----------------------------
# Run Experiment
# -----------------------------
if st.sidebar.button("Run Experiment"):

    if not requirement.strip():
        st.warning(
            "Please enter a requirement."
        )
    else:
        optimizer = PromptOptimizer(
            PromptMutator(),
            FakeLLM(),
            QualityEvaluator(),
            ExperimentTracker()
            )

    st.session_state["results"] = optimizer.optimize(
        requirement
    )


# -----------------------------
# Dashboard
# -----------------------------
results = st.session_state["results"]

if results:

    render_metrics(results)

    render_leaderboard(results)

    render_prompt_viewer(results)

    scores = [r["score"] for r in results]

    prompts = [r["name"] for r in results]

    fig, ax = plt.subplots()

    ax.bar(prompts, scores)

    ax.set_ylabel("Score")

    ax.set_title("Prompt Performance")

    st.pyplot(fig)