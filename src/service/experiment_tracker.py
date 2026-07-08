class ExperimentTracker:

    def __init__(self):

        self.history = []

    def save(

        self,

        prompt,

        result,

        score

    ):

        self.history.append(

            {

                "name": prompt["name"],

                "prompt": prompt["prompt"],

                "result": result,

                "score": score

            }

        )

    def leaderboard(self):

        return sorted(

            self.history,

            key=lambda x: x["score"],

            reverse=True

        )