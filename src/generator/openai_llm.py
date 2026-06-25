from src.generator.base_llm import BaseLLM
from src.models import TestCase


class OpenAILLM(BaseLLM):

    def run(self, prompt: str):

        return [
            TestCase("functional", "login works"),
            TestCase("negative", "invalid password"),
            TestCase("boundary", "empty input")
        ]