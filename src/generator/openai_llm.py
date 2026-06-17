from src.generator.base_llm import BaseLLM


class OpenAILLM(BaseLLM):

    def run(self, prompt: str):

        raise NotImplementedError(
            "Enable when API key is available"
        )