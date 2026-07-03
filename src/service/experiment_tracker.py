class ExperimentTracker:

    def __init__(self):

        self.history = []

    def save(

        self,

        prompt,

        score

    ):

        self.history.append(

            {

                "name": prompt["name"],

                "prompt": prompt["prompt"],

                "score": score

            }

        )

    def leaderboard(self):

        return sorted(

            self.history,

            key=lambda x: x["score"],

            reverse=True

        )