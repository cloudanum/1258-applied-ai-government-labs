# Do Now 7.B: Cost at Agency Scale 🎯

**Time:** 5 minutes
**Format:** No sandbox or tooling required, this activity is done mentally and captured in Zoom chat (or on the Mural board if the instructor directs).
**Mural:** https://app.mural.co/t/day10626/m/day10626/1790240809044/741969c4e1aa6b09012abf0820591d84b02deda0

## Goal
Estimate the monthly token cost of one GenAI assistant rolled out to 12,000 staff, then decide which single assumption moves the total cost the most. Post your answer as `biggest cost driver: ___ because ___`.

**Assets:** Worked driver table with example inputs and formulas (see `board-items.tsv`); a calculator or spreadsheet is handy but not required.

**🌐 MS Co-pilot Specific Info:** Let Copilot do the arithmetic chain (users × requests × tokens × days), then change one assumption and recompute, sensitivity, not the point estimate, is the skill.

**🧩 Pattern watch:** Design pattern, **Sensitivity analysis**: change one assumption at a time and watch the cost curve. Anti-pattern, **Single point estimate**: one confident number with no range and no driver named.

> ℹ️ **Good to know:** A token, the unit AI models bill by, is roughly three quarters of an English word, so a page of text runs about 500 to 800 tokens. Pricing is quoted per million tokens, which is why small per-call costs turn into budget lines at agency scale. Your multiplication chain is the arithmetic behind every AI invoice. (Source: [IBM Think](https://www.ibm.com/think/topics/tokens))

## Run steps 🪜
1. Read the worked driver table on the board (or in `board-items.tsv`): 12,000 staff, 2 requests per person per day, 1,200 input + 400 output tokens per request.
2. Do the arithmetic chain: requests/day = 12,000 × 2 = 24,000; tokens/day = 24,000 × 1,600 = 38.4M; monthly tokens = 38.4M × 22 ≈ 845M.
3. Convert tokens to dollars using separate input and output prices from the instructor's price card or any public pricing page (output tokens usually cost several times more).
4. Test the levers one at a time: what happens to the bill if requests per user double? If tokens per request double? If half the asks are routed to a smaller, cheaper model?
5. Decide which assumption changes the cost most, and post it in Zoom chat as `biggest cost driver: ___ because ___` with your number attached.
6. Read three other chat posts, find one that names a different driver, and reply with the assumption you would both need to agree on before the debrief.

## Key takeaway 💡
At agency scale, cost is pure multiplication, users × requests/day × tokens × working days, so the cheapest token is the one you never send, and the highest-leverage move is usually routing simple asks to a smaller model.

## Study further 📚
- [Vertex AI generative AI pricing, Google Cloud](https://cloud.google.com/vertex-ai/generative-ai/pricing), real per-token input/output prices to plug into your estimate.
- [What are tokens?, IBM Think](https://www.ibm.com/think/topics/tokens), clear explainer on what a token is and why models bill by it.
- [Plan and manage costs for Azure OpenAI, Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/manage-costs), official guidance on estimating and controlling token spend.

## Common mistake to name ⚠️
Quoting a per-request price without doing the multiplication; require the full chain, users × requests/day × tokens × 22 days, and one named assumption that moves the total most.

## If finished early ⏩
Recompute the monthly bill assuming routing sends half of all requests to a model at one-tenth the price: how much is saved, and which assumption in the chain did you just touch?

**Solution link in master guide:** `#answer-7-b`
