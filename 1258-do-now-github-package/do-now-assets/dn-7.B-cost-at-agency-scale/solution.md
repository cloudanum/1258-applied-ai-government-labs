# Sample / solution

## Why this approach works
At agency scale, cost is pure multiplication, users × requests/day × tokens × working days, so only the full chain produces a defensible number, never a per-request price. The driver worth naming is model choice: every volume lever moves the bill linearly, while per-token prices across model tiers differ by an order of magnitude.

## A complete solution
The chain: 12,000 staff × 2 requests/day = 24,000 requests/day. Tokens/day = 24,000 × 1,600 = 38.4M. Monthly tokens = 38.4M × 22 ≈ 845M, split into 633.6M input and 211.2M output. At a mid-tier price of $0.40 per million input and $1.60 per million output: (633.6 × $0.40) + (211.2 × $1.60) ≈ $253 + $338 ≈ $590 per month. The same workload on a frontier card of $2.50 in / $10.00 out lands near $3,700 per month. Output tokens are a quarter of the volume but roughly 57% of the mid-tier bill, and swapping model tiers moves the total about 6x with no change in usage.

Testing the levers one at a time: doubling requests per user doubles the bill, doubling tokens per request doubles the bill, and routing half of all requests to a model at one-tenth the price cuts the bill about 45% while touching only the model-choice assumption. A complete post reads: "biggest cost driver: model choice because at 845M tokens/month (12,000 users × 2 requests × 1,600 tokens × 22 days) every volume lever moves the bill only linearly, while per-token prices across model tiers differ by 10x or more; routing half our 24,000 daily requests to a small model at one-tenth the price cuts the monthly bill about 45% with no reduction in service."

If a colleague posts "biggest cost driver: users," the reconciliation is one question: could request volume plausibly double? If usage is capped by policy, volume levers are bounded and model tier remains the only lever with an order-of-magnitude swing.
