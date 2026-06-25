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


def test_prompt_ab():

    experiment = PromptExperiment(

        PromptBuilder(),

        FakeLLM(),

        LLMJudge()

    )

    result = experiment.compare(

        "login"

    )
    print(result)

    assert (

        result[
            "winner"
        ]

        ==

        "B"

    )