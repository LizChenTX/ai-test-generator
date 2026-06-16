class PromptPipeline:

    def __init__(
        self,
        builder,
        generator,
        evaluator
    ):

        self.builder = builder

        self.generator = generator

        self.evaluator = evaluator

    def execute(
        self,
        requirement,
        version
    ):

        prompt = self.builder.build(
            requirement,
            version
        )

        result = self.generator.run(
            prompt
        )

        score = self.evaluator.score(
            result
        )

        return {

            "prompt": prompt,

            "result": result,

            "score": score
        }