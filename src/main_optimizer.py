from src.generator.fake_llm import (
    FakeLLM
)

from src.evaluator.quality_evaluator import (
    QualityEvaluator
)

from src.service.prompt_mutator import (
    PromptMutator
)

from src.service.prompt_optimizer import (
    PromptOptimizer
)

from src.service.experiment_tracker import (
    ExperimentTracker
)


optimizer = PromptOptimizer(

    PromptMutator(),

    FakeLLM(),

    QualityEvaluator(),

    ExperimentTracker()

)

optimizer.optimize(

    "login api"

)