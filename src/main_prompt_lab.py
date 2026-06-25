from pprint import pprint

from src.generator.prompt_builder import (
    PromptBuilder
)

from src.generator.fake_llm import (
    FakeLLM
)

from src.evaluator.llm_judge import (
    LLMJudge
)

from src.service.prompt_experiment import (
    PromptExperiment
)

exp = PromptExperiment(

    PromptBuilder(),

    FakeLLM(),

    LLMJudge()

)

result = exp.compare(

    "login api",

    runs=20

)

pprint(
    result
)