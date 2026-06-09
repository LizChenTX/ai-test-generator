from generator.mock_generator import MockGenerator
from service.test_case_service import TestCaseService

generator = MockGenerator()
service = TestCaseService(generator)

result = service.generate_test_cases("Login API")

for r in result:
    print(r)