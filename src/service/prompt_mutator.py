class PromptMutator:

    TEMPLATES = [

"""
Generate tests.

Requirement:
{r}
""",

"""
You are QA.

Generate:

functional
negative

Requirement:
{r}
""",

"""
You are principal QA.

Generate:

functional
negative
boundary

Requirement:
{r}
""",

"""
Think step by step.

Generate tests.

Requirement:
{r}
"""

    ]

    def mutate(
        self,
        requirement
    ):

        prompts = []

        for p in self.TEMPLATES:

            prompts.append(

                p.format(
                    r=requirement
                )

            )

        return prompts