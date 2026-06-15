from src.generator.mock_generator import MockGenerator
from src.service.test_case_service import TestCaseService

def test_login_requirement():

    service = TestCaseService(
        MockGenerator()
    )

    result = service.generate_test_cases(
        "login api"
    )

    assert len(result) == 3