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

        return self.tracker.leaderboard()