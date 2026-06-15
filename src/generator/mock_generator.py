from src.models import TestCase

class MockGenerator:

    def generate(self, requirement: str):

        requirement = requirement.lower()

        if "login" in requirement:

            return [

                TestCase(
                    category="functional",
                    description="Valid username and password"
                ),

                TestCase(
                    category="negative",
                    description="Invalid password"
                ),

                TestCase(
                    category="boundary",
                    description="Empty username"
                )
            ]

        return [
            TestCase(
                category="functional",
                description="Generic happy path"
            )
        ]