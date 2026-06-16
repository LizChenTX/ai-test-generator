from src.models import TestCase

class PromptGenerator:

    def build_prompt(
        self,
        requirement,
        version="A"
    ):

        if version == "A":

            return f"""
Generate test cases.

{requirement}
"""

        if version == "B":

            return f"""
You are senior QA.

Generate:

1 functional
1 negative
1 boundary

Requirement:

{requirement}
"""

    def generate(
        self,
        requirement,
        version="A"
    ):

        prompt = self.build_prompt(
            requirement,
            version
        )

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
                "login"
            )
        ]