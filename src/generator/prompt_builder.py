class PromptBuilder:

    PROMPTS = {

        "A":

"""
Generate tests.

Requirement:
{r}
""",

        "B":

"""
You are QA.

Generate:

functional
negative
boundary

Requirement:
{r}
""",

        "C":

"""
Think step by step.

Generate:

functional
negative
boundary
edge

Requirement:
{r}
""",

        "D":

"""
You are principal QA.

Generate:

functional
negative
boundary
edge

Explain reasoning.

Requirement:
{r}
"""

    }

    def build(

        self,

        requirement,

        version

    ):

        return (

            self

            .PROMPTS

            [

                version

            ]

            .format(

                r=requirement

            )

        )