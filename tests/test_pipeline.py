from src.generator.prompt_builder import (
    PromptBuilder
)

from src.generator.fake_llm import (
    FakeLLM
)

from src.evaluator.test_case_evaluator import (
    TestCaseEvaluator
)

from src.service.pipeline import (
    PromptPipeline
)


def test_pipeline():

    pipeline = PromptPipeline(

        PromptBuilder(),

        FakeLLM(),

        TestCaseEvaluator()

    )

    output = pipeline.execute(

        "login",

        "B"

    )

    assert output[
        "score"
    ] == 3