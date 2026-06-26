# AI Test Generator

A lightweight prompt experimentation and evaluation platform for automated test generation.

This project was built to explore how AI systems can generate and evaluate software test cases through prompt engineering, experimentation, and scoring pipelines.

---

## Overview

This project simulates an AI workflow:

Requirement

↓

Prompt Generation

↓

LLM Layer (Mock)

↓

Evaluation

↓

Experiment Tracking

↓

Optimization

The current implementation does not require paid API usage and runs locally.

---

## Features

### Prompt Engineering

* Prompt Builder
* Prompt Mutation
* Prompt Comparison

### LLM Abstraction

* Fake LLM implementation
* Provider decoupling

### Evaluation

* Quality-based scoring
* Coverage evaluation

### Experiment Platform

* Experiment tracker
* Leaderboard
* Prompt optimization

---

## Architecture

```text
Requirement
↓

PromptMutator

↓

FakeLLM

↓

QualityEvaluator

↓

ExperimentTracker

↓

PromptOptimizer
```

---

## Run

Create virtual environment:

```bash
python -m venv .venv
```

Activate:

```bash
source .venv/bin/activate
```

Install:

```bash
pip install -r requirements.txt
```

Run:

```bash
python -m src.main_optimizer
```

---

## Example Output

```text
Experiment 1

Prompt:
Generate tests

Score: 2

Experiment 2

Prompt:
You are QA

Score: 4
```

---

## Roadmap

v1 Mock Prompt Evaluation

v2 Prompt Optimization

v3 Experiment Tracking

v4 OpenAI Integration (planned)

v5 Retrieval-Augmented Generation (planned)

---

## Author

Built as an AI Engineering transition project.
