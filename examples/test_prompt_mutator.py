from src.service.prompt_mutator import PromptMutator

mutator = PromptMutator()

prompts = mutator.mutate("login api")

for p in prompts:
    print("=" * 40)
    print("NAME :", p["name"])
    print()
    print(p["prompt"])