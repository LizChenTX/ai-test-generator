import random

from src.models import TestCase
from src.generator.base_llm import BaseLLM


class FakeLLM(BaseLLM):

    def run(self, prompt):

        categories = []

        categories.append(
            "functional"
        )

        if "negative" in prompt:

            categories.append(
                "negative"
            )

        if "boundary" in prompt:

            categories.append(
                "boundary"
            )

        # 模拟LLM波动

        if random.random() > 0.6:

            categories.append(
                "edge"
            )

        return [

            TestCase(
                c,
                f"{c} scenario"
            )

            for c in categories
        ]