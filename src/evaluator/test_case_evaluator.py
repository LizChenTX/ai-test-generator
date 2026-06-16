class TestCaseEvaluator:

    def score(
        self,
        results
    ):

        categories = set()

        for case in results:

            categories.add(
                case.category
            )

        return len(
            categories
        )