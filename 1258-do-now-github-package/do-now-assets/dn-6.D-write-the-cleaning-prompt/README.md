# Do Now 6.D: Write the Cleaning Prompt 🎯

**Time:** 5 minutes
**Format:** No sandbox or tooling required, this activity is done mentally and captured in Zoom chat (in-person learners can post their prompt as a Mural comment on the board).
**Mural:** https://app.mural.co/t/day10626/m/day10626/1790240807054/1d814f71975cf6050dbac5e3980a4b2baf02bd83

## Goal
By the end of this five-minute writing sprint you will have drafted one complete cleaning prompt you could hand to an LLM to fix the dirty 311 rows from activity 6.A, with explicit normalization rules and a required output shape. Your artifact is the prompt itself, posted in chat, containing a rules section (ISO dates, dedup by request ID) and an output contract (JSON with keys `rows`, `flags`, `removed_duplicate_ids`). The instinct this builds: an LLM cleans data exactly as well as the contract you write for it, vague instructions produce confident, unverifiable output, while explicit rules plus a fixed schema make the result checkable by both humans and code.

## Why it matters
A cleaning prompt is a contract: the more precisely you specify rules and output shape, the more verifiable the model's work becomes. Writing one in chat, where peers can poke holes in it, builds the habit of treating LLM output as something to be checked against a spec, not trusted on its face.

**Assets:** Dirty rows from 6.A and the rule prompts (see `board-items.tsv`).

**🌐 MS Co-pilot Specific Info:** Your cleaning prompt can run in Copilot over small, non-sensitive samples; for real agency data the same prompt belongs in an approved pipeline, not a browser chat.

## Run steps 🪜
1. Look back at the dirty rows from 6.A, mixed date formats (`01/03/26`, `2026-13-03`), duplicate request ID `311-10485`, inconsistent wards and statuses, and decide exactly what "clean" means for each column.
2. Write your normalization rules as imperative prompt lines, e.g. `Convert created_date to ISO YYYY-MM-DD; flag impossible dates.`
3. Add a deduplication rule, e.g. `If request_id repeats, keep the most complete row and list removed rows.`
4. Specify the output shape explicitly: `Return JSON with keys: rows, flags, removed_duplicate_ids.`, never leave the format to the model's imagination.
5. Post your complete cleaning prompt in Zoom chat (or as a Mural comment if you are in person), keeping the rules section and the output-shape section clearly separated.
6. Read one other learner's prompt and reply with the first thing that would go wrong if you actually ran it, an ambiguous rule, a missing key, or no instruction for rows that cannot be fixed.

## Key takeaway 💡
An LLM cleans data exactly as well as the contract you write for it, explicit rules plus a required output schema turn a vague "clean this" into verifiable, reviewable results.

## Study further 📚
- [What is prompt engineering?, IBM Think](https://www.ibm.com/think/topics/prompt-engineering), fundamentals of writing instructions that LLMs follow reliably.
- [Introduction to prompt design, Google Cloud](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/introduction-prompt-design), Google's guide to clear, structured, unambiguous prompts.
- [Working with missing data, pandas documentation](https://pandas.pydata.org/docs/user_guide/missing_data.html), the canonical reference for the cleaning operations your prompt is describing.

## Common mistake to name ⚠️
Writing instructions with no output contract. "Clean this data" returns confident prose; require a rules section and an explicit output schema, named keys, types, and what to do with failures, so the result can be validated programmatically.

## If finished early ⏩
Add a refusal or flagging rule to your prompt: what should the model do when a row cannot be cleaned unambiguously, guess, drop, or flag for human review?

## ⭐ Bonus (optional)
Rewrite the same cleaning rules as a request for a Python/pandas script instead of cleaned JSON. Post both versions and note which one you would trust more in production, and why.

**Solution link in master guide:** `#answer-6-d`
