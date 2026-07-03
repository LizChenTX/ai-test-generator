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

render_title()


if st.button("Run Experiment"):

    optimizer = PromptOptimizer(
        PromptMutator(),
        FakeLLM(),
        QualityEvaluator(),
        ExperimentTracker()
    )

    results = optimizer.optimize("login api")
    render_metrics(results)

    render_leaderboard(results)

    scores = [r["score"] for r in results]

    prompts = [f"Prompt {i}" for i in range(len(scores))]

    fig, ax = plt.subplots()

    ax.bar(prompts, scores)

    ax.set_ylabel("Score")

    ax.set_title("Prompt Performance")

    st.pyplot(fig)