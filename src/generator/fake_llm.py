from src.models import (
    TestCase
)

from src.generator.base_generator import (
    BaseGenerator
)


class FakeLLM(
    BaseGenerator
):

    def run(
        self,
        prompt
    ):

        if "boundary" in prompt:

            return [

                TestCase(
                    "functional",
                    "valid login"
                ),

                TestCase(
                    "negative",
                    "wrong password"
                ),

                TestCase(
                    "boundary",
                    "empty username"
                )
            ]

        return [

            TestCase(
                "functional",
                "valid login"
            )
        ]