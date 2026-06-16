import pytest

from src.generator.prompt_generator import (
    PromptGenerator
)

@pytest.mark.parametrize(
    "version,expected",
    [

        (
            "A",
            1
        ),

        (
            "B",
            3
        )
    ]
)

def test_prompt_versions(
    version,
    expected
):

    generator = PromptGenerator()

    result = generator.generate(
        "login api",
        version
    )

    assert len(
        result
    ) == expected