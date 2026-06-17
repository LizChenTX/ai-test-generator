from src.generator.base_llm import BaseLLM
from src.models import TestCase


class FakeLLM(BaseLLM):

    def run(self, prompt: str):

        if "boundary" in prompt:

            return [
                TestCase("functional", "valid login"),
                TestCase("negative", "wrong password"),
                TestCase("boundary", "empty username"),
            ]

        return [
            TestCase("functional", "valid login")
        ]