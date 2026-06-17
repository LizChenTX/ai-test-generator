from dataclasses import dataclass

@dataclass
class Metrics:

    tokens: int

    latency_ms: int

    cost_usd: float