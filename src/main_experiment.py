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

experiment = PromptExperiment(

    PromptBuilder(),

    FakeLLM(),

    LLMJudge()

)

result = experiment.compare(

    "login"

)

pprint(
    result
)