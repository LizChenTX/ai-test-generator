from src.generator.base_llm import BaseLLM
from src.models import TestCase


class MockGenerator(BaseLLM):

    def run(self, prompt: str):

        return [
            TestCase("mock", "fixed output")
        ]