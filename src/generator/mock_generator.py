from src.models import (
    TestCase
)

from src.generator.base_generator import (
    BaseGenerator
)


class MockGenerator(
    BaseGenerator
):

    def run(
        self,
        prompt
    ):

        return [

            TestCase(
                "mock",
                "always same"
            )
        ]