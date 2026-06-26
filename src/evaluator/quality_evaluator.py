class QualityEvaluator:

    def score(
        self,
        results
    ):

        categories = set()

        score = 0

        for r in results:

            categories.add(
                r.category
            )

        coverage = len(
            categories
        )

        duplication = (

            len(results)

            -

            coverage

        )

        score += (

            coverage

            * 2

        )

        score -= duplication

        return score