import time

from src.models_metrics import (
    Metrics
)


class Telemetry:

    def track(
        self,
        prompt,
        result
    ):

        tokens = len(
            prompt.split()
        )

        latency = (
            tokens * 10
        )

        cost = (
            tokens
            *
            0.00001
        )

        return Metrics(

            tokens,

            latency,

            round(
                cost,
                5
            )
        )