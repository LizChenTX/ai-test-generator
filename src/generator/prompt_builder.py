class PromptBuilder:

    def build(
        self,
        requirement,
        version
    ):

        if version == "A":

            return f"""
Generate test cases.

Requirement:

{requirement}
"""

        if version == "B":

            return f"""
You are senior QA.

Generate:

- functional
- negative
- boundary

Requirement:

{requirement}
"""