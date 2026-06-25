class LLMJudge:

    WEIGHT = {

        "functional": 2,

        "negative": 2,

        "boundary": 3,

        "edge": 1

    }

    def score(
        self,
        results
    ):

        score = 0

        for r in results:

            score += (

                self.WEIGHT

                .get(

                    r.category,

                    0

                )

            )

        return score