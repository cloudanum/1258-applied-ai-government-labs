# Do Now 4.B: Give the Model a Job 🎯

**Time:** 5 minutes
**Format:** No special tooling or environment required, this activity is done mentally and captured in Zoom chat (or as comments on the Mural board if you are in the room).
**Mural:** https://app.mural.co/t/day10626/m/day10626/1790240796050/1508b14d84e6e205e4ceef79f89a0161439aacc5

## Goal
By the end of this five-minute warm-up you will have picked one government task sticky (J1–J4) and written a two-part prompt for it: a role, "You are a ___", plus an output contract, "the output must look like ___." Working from patterns like "summarize a public-records request" (role: government records officer; contract: issues, exemptions to check, and a draft response in 5 bullets) and "review a chatbot answer" (role: cautious communications director; contract: factual risk, tone risk, revised answer), you will see how much of a model's behavior can be set before it writes a single word. The artifact you produce is one complete role-plus-contract prompt, posted in chat; the instinct you build is that assigning a job selects the expertise, vocabulary, and caution level the answer will arrive with.

## Why it matters
A role line is the fastest way to move a model from generic to government-grade: it changes what the model notices, what it flags as risky, and whom it imagines reading. Assigning a role before asking for output is a core AI-at-work habit; doing it in chat makes the reasoning visible and easy to correct.

**Assets:** Task stickies J1–J4 (see `board-items.tsv`).

**🌐 MS Co-pilot Specific Info:** Copilot honors role + contract prompts: “You are a government records officer. Return … in 5 bullets” works verbatim in the browser chat, try your final version there after the exercise.

**🧩 Pattern watch:** Design pattern, **Persona plus output contract**: a named role and a stated shape make outputs reviewable. Anti-pattern, **Prompt and pray**: no role, no shape, no way to say what 'wrong' means.

## Run steps 🪜
1. Read the task stickies J1–J4 on the Mural board or the instructor's screen, and pick the one closest to your real work.
2. Ask who in government would do this task best, that is your role. Write it as `You are a ___` (for a records-request task: `You are a government records officer`).
3. Decide what a finished answer must contain. For a records summary that is issues, exemptions to check, and a draft response in 5 bullets; for a chatbot review it is factual risk, tone risk, and a revised answer.
4. Post your full prompt to Zoom chat as one structured message: `Task: ___ | Role: You are a ___ | Output must look like: ___`.
5. Compare roles in chat: find one classmate whose different role would produce a different answer, and reply saying what would change.
6. If the instructor is capturing on Mural, copy your role-plus-contract onto a sticky beside your chosen task so the board collects the room's templates.

## Key takeaway 💡
"You are a ___" tells the model which expertise, vocabulary, and caution level to bring before it writes a single word, but the role only pays off when you pair it with a contract for what the output must look like.

## Study further 📚
- [System message guidance, Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/system-message), how the system message frames the model's role, tone, and boundaries.
- [System instructions, Google Cloud](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/system-instructions), setting the model's job before the user prompt in Vertex AI.
- [What is prompt engineering?, IBM Think](https://www.ibm.com/think/topics/prompt-engineering), the core techniques, including persona and role prompting.

## Common mistake to name ⚠️
Writing "You are an expert" and stopping there, a role without an output contract produces confident rambling, so require the named fields (issues, exemptions, draft) that make the answer usable.

## If finished early ⏩
Write two different roles for the same task, say, a records officer and a skeptical journalist, and post both in chat with one line on how the role alone changes what gets flagged.

## ⭐ Bonus (optional)
Take a recurring task from your own agency and write the role-plus-contract prompt you would actually reuse; post it in chat as a candidate team template, and note whom the role must satisfy (auditor, director, resident).

**Solution link in master guide:** `#answer-4-b`
