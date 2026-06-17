class PromptPipeline:

    def __init__(self, builder, llm, evaluator, telemetry):

        self.builder = builder
        self.llm = llm
        self.evaluator = evaluator
        self.telemetry = telemetry

    def execute(self, requirement, version):

        prompt = self.builder.build(requirement, version)

        result = self.llm.run(prompt)

        metrics = self.telemetry.track(prompt, result)

        score = self.evaluator.score(result)

        return {
            "prompt": prompt,
            "result": result,
            "metrics": metrics,
            "score": score
        }