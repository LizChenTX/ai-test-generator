from src.generator.mock_generator import MockGenerator
from src.service.test_case_service import TestCaseService

generator = MockGenerator()

service = TestCaseService(
    generator
)

requirement = """
Login API

POST /login

username
password
"""

result = service.generate_test_cases(
    requirement
)

for tc in result:

    print(
        f"[{tc.category}] "
        f"{tc.description}"
    )