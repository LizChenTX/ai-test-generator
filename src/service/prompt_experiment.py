class PromptExperiment:

    def __init__(

        self,

        builder,

        llm,

        judge

    ):

        self.builder = builder

        self.llm = llm

        self.judge = judge

    def compare(

        self,

        requirement,

        runs=10

    ):

        versions = [

            "A",

            "B",

            "C",

            "D"

        ]

        scores = {}

        for version in versions:

            total = 0

            for _ in range(

                runs

            ):

                prompt = (

                    self.builder.build(

                        requirement,

                        version

                    )
                )

                result = (

                    self.llm.run(

                        prompt

                    )
                )

                total += (

                    self.judge.score(

                        result

                    )
                )

            scores[
                version
            ] = round(

                total

                /

                runs,

                2

            )

        winner = max(

            scores,

            key=scores.get

        )

        return {

            "scores":

            scores,

            "winner":

            winner

        }