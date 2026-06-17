from pprint import pprint

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


pipeline = PromptPipeline(

    PromptBuilder(),

    FakeLLM(),

    TestCaseEvaluator(),

    Telemetry()

)

output = pipeline.execute(

    "login",

    "B"

)

pprint(
    output
)