import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Prompt Optimizer",
    page_icon="🤖",
    layout="wide"
)

from src.service.prompt_optimizer import PromptOptimizer
from src.generator.fake_llm import FakeLLM
from src.evaluator.quality_evaluator import QualityEvaluator
from src.service.prompt_mutator import PromptMutator
from src.service.experiment_tracker import ExperimentTracker

from src.dashboard.components import render_title
from src.dashboard.metrics import render_metrics
from src.dashboard.leaderboard import render_leaderboard
from src.dashboard.prompt_viewer import render_prompt_viewer
from src.dashboard.chart import render_chart

render_title()

# -----------------------------
# Session State
# -----------------------------
if "results" not in st.session_state:
    st.session_state["results"] = []

if "history" not in st.session_state:
    st.session_state["history"] = []

if "requirement" not in st.session_state:
    st.session_state["requirement"] = ""

# -----------------------------
# Siderbar
# -----------------------------
st.sidebar.header("⚙️ Experiment Settings")
requirement = st.sidebar.text_area(
    "Requirement",
    key="requirement",
    height=120
)
st.sidebar.caption(
    "Example: login api, payment api, shopping cart"
)

# -----------------------------
# Run Experiment
# -----------------------------
if st.sidebar.button("Run Experiment"):
    if not requirement.strip():
        st.warning("Please enter a requirement.")
    else:
        optimizer = PromptOptimizer(
            PromptMutator(),
            FakeLLM(),
            QualityEvaluator(),
            ExperimentTracker()
        )
        results = optimizer.optimize(requirement)
        st.session_state["results"] = results
        st.session_state["history"].append(
            {
                "requirement": requirement,
                "results": results
            }
        )

# -----------------------------
# History
# -----------------------------
st.sidebar.divider()
st.sidebar.subheader("📖 Run History")
for item in st.session_state["history"]:
    st.sidebar.write(
        item["requirement"]
    )

# -----------------------------
# Dashboard
# -----------------------------
results = st.session_state["results"]

if results:
    render_metrics(results)

    col1, col2 = st.columns(2)

    with col1:
        render_chart(results)

    with col2:
        render_leaderboard(results)

    render_prompt_viewer(results)