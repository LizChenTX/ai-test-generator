class PromptPipeline:

    def __init__(
        self,
        builder,
        generator,
        evaluator,
        telemetry
    ):

        self.builder = builder

        self.generator = generator

        self.evaluator = evaluator

        self.telemetry = telemetry

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

        metrics = self.telemetry.track(

            prompt,

            result

        )

        score = self.evaluator.score(

            result

        )

        return {

            "score": score,

            "metrics": metrics,

            "result": result
        }