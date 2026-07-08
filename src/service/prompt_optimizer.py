from pprint import pprint

class PromptOptimizer:

    def __init__(

        self,

        mutator,

        llm,

        judge,

        tracker

    ):

        self.mutator = mutator

        self.llm = llm

        self.judge = judge

        self.tracker = tracker

    def optimize(

        self,

        requirement

    ):

        prompts = self.mutator.mutate(
            requirement
        )

        experiment = 1

        for p in prompts:

            result = self.llm.run(
                p["prompt"]
            )

            score = self.judge.score(
                result
            )

            self.tracker.save(
                p,
                result,
                score
            )

            print()
            print("=" * 50)

            print(
                f"Experiment {experiment} - {p['name']}"
            )

            print()

            print("PROMPT")
            print()

            print(
                p["prompt"].strip()
            )

            print()

            print("RESULT")
            print()

            for r in result:

                print(
                    f"- {r.category}"
                )

            print()

            print(
                f"SCORE: {score}"
            )

            print("=" * 50)

            experiment += 1

        board = self.tracker.leaderboard()

        print()

        print("#" * 50)

        print("FINAL LEADERBOARD")

        print()

        for i, row in enumerate(
            board,
            start=1
        ):

            print(
                f"{i}. score={row['score']}"
            )

        print()

        print(
            f"WINNER SCORE = {board[0]['score']}"
        )

        print("#" * 50)

        pprint(board)

        return board
    