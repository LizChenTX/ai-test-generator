from src.generator.prompt_builder import (
    PromptBuilder
)

from src.generator.fake_llm import (
    FakeLLM
)

from src.evaluator.test_case_evaluator import (
    TestCaseEvaluator
)

def test_prompt_ab():

    builder = PromptBuilder()

    llm = FakeLLM()

    evaluator = TestCaseEvaluator()

    prompt_a = builder.build(
        "login",
        "A"
    )

    result_a = llm.run(
        prompt_a
    )

    score_a = evaluator.score(
        result_a
    )

    prompt_b = builder.build(
        "login",
        "B"
    )

    result_b = llm.run(
        prompt_b
    )

    score_b = evaluator.score(
        result_b
    )

    assert score_b > score_a