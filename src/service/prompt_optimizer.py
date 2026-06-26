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

        prompts = (

            self.mutator.mutate(
                requirement
            )

        )

        experiment = 1

        for p in prompts:

            result = (

                self.llm.run(
                    p
                )

            )

            score = (

                self.judge.score(
                    result
                )

            )

            self.tracker.save(

                p,

                score

            )

            print()

            print(
                "=" * 50
            )

            print(
                f"Experiment {experiment}"
            )

            print()

            print(
                "PROMPT"
            )

            print()

            print(
                p.strip()
            )

            print()

            print(
                "RESULT"
            )

            print()

            for r in result:

                print(
                    f"- {r.category}"
                )

            print()

            print(
                f"SCORE: {score}"
            )

            print(
                "=" * 50
            )

            experiment += 1

        board = (

            self.tracker
            .leaderboard()

        )

        print()

        print(
            "#" * 50
        )

        print(
            "FINAL LEADERBOARD"
        )

        print()

        for i, row in enumerate(
            board,
            start=1
        ):

            print(

                f"{i}. "

                f"score={row['score']}"

            )

        print()

        print(
            f"WINNER SCORE = {board[0]['score']}"
        )

        print(
            "#" * 50
        )

        return board