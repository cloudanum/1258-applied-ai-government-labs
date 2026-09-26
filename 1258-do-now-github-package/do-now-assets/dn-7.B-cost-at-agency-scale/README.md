# Do Now 7.B: Cost at Agency Scale 🎯

**Time:** 5 minutes
**Format:** No sandbox or tooling required, this activity is done mentally and captured in Zoom chat (or on the Mural board if the instructor directs).
**Mural:** https://app.mural.co/t/day10626/m/day10626/1790240809044/741969c4e1aa6b09012abf0820591d84b02deda0

## Goal
By the end of this five-minute warm-up you will have estimated what one GenAI assistant costs when it is rolled out to an entire agency: 12,000 staff, two requests per person per day, roughly 1,600 tokens per request (1,200 in, 400 out), across 22 working days a month. You will compute the monthly token volume with back-of-the-envelope math, then decide which single assumption, users, requests per day, tokens per request, or model choice, moves the total cost the most. The artifact you produce is one posted cost driver with its reasoning, in the format `biggest cost driver: ___ because ___`. The instinct being built is multiplication thinking: agency-scale cost is users × requests × tokens × days, so a small per-request change compounds into a serious budget line.

## Why it matters
A demo that costs pennies can become a seven-figure line item at agency scale, and budget owners will ask "what drives this number?" before they approve anything. Estimating token cost from first principles is a core AI-at-work habit; doing it in chat makes the reasoning visible and easy to correct.

**Assets:** Worked driver table with example inputs and formulas (see `board-items.tsv`); a calculator or spreadsheet is handy but not required.

**🌐 MS Co-pilot Specific Info:** Let Copilot do the arithmetic chain (users × requests × tokens × days), then change one assumption and recompute, sensitivity, not the point estimate, is the skill.

## Run steps 🪜
1. Read the worked driver table on the board (or in `board-items.tsv`): 12,000 staff, 2 requests per person per day, 1,200 input + 400 output tokens per request.
2. Do the arithmetic chain: requests/day = 12,000 × 2 = 24,000; tokens/day = 24,000 × 1,600 = 38.4M; monthly tokens = 38.4M × 22 ≈ 845M.
3. Convert tokens to dollars by separating input and output prices (output tokens usually cost several times more than input), use the price card on the instructor's slide or any public pricing page.
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
