class PromptMutator:

    TEMPLATES = [

    {
        "name": "Simple",
        "template": """
Generate tests.

Requirement:
{r}
"""
    },

    {
        "name": "QA",
        "template": """
You are QA.

Generate:

functional
negative

Requirement:
{r}
"""
    },

    {
        "name": "Principal QA",
        "template": """
You are principal QA.

Generate:

functional
negative
boundary

Requirement:
{r}
"""
    },

    {
        "name": "Chain of Thought",
        "template": """
Think step by step.

Generate tests.

Requirement:
{r}
"""
    }

]
    def mutate(
        self,
        requirement
    ):

        prompts = []

        for p in self.TEMPLATES:

            prompts.append(

                {
                    "name": p["name"],
                    "prompt": p["template"].format(
                        r=requirement
                    )
                }

            )

        return prompts