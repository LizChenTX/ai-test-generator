from abc import ABC, abstractmethod
from src.models import TestCase


class BaseLLM(ABC):

    @abstractmethod
    def run(self, prompt: str) -> list[TestCase]:
        pass