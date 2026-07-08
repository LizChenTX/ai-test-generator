from src.generator.fake_llm import FakeLLM

from src.evaluator.quality_evaluator import QualityEvaluator

from src.service.prompt_mutator import PromptMutator

from src.service.prompt_optimizer import PromptOptimizer

from src.service.experiment_tracker import ExperimentTracker


def print_report(board):

    print("\nPrompt Experiment Report\n")

    for row in board:

        print("=" * 60)

        print(f"Prompt: {row['name']}")

        print(f"Score : {row['score']}")

        print()

        print("Prompt Content")

        print("-" * 60)

        print(row["prompt"])

        print()

        print("Generated Test Cases")

        print("-" * 60)

        for case in row["result"]:

            print(
                f"• {case.category}: {case.description}"
            )

        print()


optimizer = PromptOptimizer(

    PromptMutator(),

    FakeLLM(),

    QualityEvaluator(),

    ExperimentTracker()

)

board = optimizer.optimize(

    "login api"

)

print_report(board)