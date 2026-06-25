class PromptPipeline:

    def __init__(self, builder, llm_type, evaluator, telemetry):

        self.builder = builder

        self.llm_type = llm_type

        self.evaluator = evaluator

        self.telemetry = telemetry

    def _get_llm(self):

        return self.llm_type

    def execute(self, requirement, version):

        prompt = self.builder.build(requirement, version)

        llm = self._get_llm()

        result = llm.run(prompt)

        metrics = self.telemetry.track(prompt, result)

        score = self.evaluator.score(result)

        return {
            "prompt": prompt,
            "result": result,
            "metrics": metrics,
            "score": score
        }