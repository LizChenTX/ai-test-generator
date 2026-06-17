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

from src.service.telemetry import (
    Telemetry
)


def test_metrics():

    pipeline = PromptPipeline(

        PromptBuilder(),

        FakeLLM(),

        TestCaseEvaluator(),

        Telemetry()

    )

    result = pipeline.execute(

        "login api",

        "B"

    )

    assert (

        result[
            "metrics"
        ].tokens

        >

        0

    )

    assert (

        result[
            "metrics"
        ].latency_ms

        >

        0

    )