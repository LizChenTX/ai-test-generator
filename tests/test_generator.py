import pytest

from src.generator.mock_generator import MockGenerator
from src.service.test_case_service import (
    TestCaseService
)

@pytest.fixture
def service():

    return TestCaseService(
        MockGenerator()
    )

@pytest.mark.parametrize(
    "requirement,expected",
    [

        (
            "login api",
            3
        ),

        (
            "payment api",
            1
        )
    ]
)

def test_generate(
    service,
    requirement,
    expected
):

    result = service.generate_test_cases(
        requirement
    )

    assert len(result) == expected