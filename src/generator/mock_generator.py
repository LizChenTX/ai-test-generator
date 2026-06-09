from src.models import TestCase

class MockGenerator:

    def generate(self, requirement: str):

        return [
            TestCase(
                category="functional",
                description="Valid login"
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