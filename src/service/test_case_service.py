class TestCaseService:

    def __init__(self, generator):
        self.generator = generator

    def generate_test_cases(self, requirement: str):

        return self.generator.generate(requirement)