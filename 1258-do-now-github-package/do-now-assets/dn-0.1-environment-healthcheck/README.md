# Do Now 0.1: Environment Healthcheck 🎯

**Time:** 5 minutes
**Format:** No sandbox or tooling required, you are simply confirming your course VM works, and the result is captured in Zoom chat (or on the Mural board if the instructor points you there).
**Mural:** https://app.mural.co/t/day10626/m/day10626/1790240780402/ea3b0b9154d58175acaa271842c2a9ec6e8081cc

## Goal
By the end of this five-minute warm-up you will have launched your CloudShare lab, opened JupyterLab in the Viewer, and posted a clear `PASS` or `BLOCKER: <what failed>` status in Zoom chat. The artifact you produce is small but important: one visible line in the capture channel that either confirms your environment is ready or names exactly what failed. The underlying habit is treating environment readiness as a first-class task, every lab in this course depends on this VM, and a vague "it doesn't work" helps no one. You are also practicing the professional skill of reporting a technical status in a structured, actionable way before real work begins.

## Why it matters
If the environment fails at minute five, you have the whole session to fix it; if it fails silently at minute forty, you lose the lab. Making the check visible in chat also lets the instructor and TAs spot patterns, one blocked learner is a support ticket, ten is a platform problem.

**Assets:** CloudShare VM, course page.

## Run steps 🪜
1. From the course page, launch your CloudShare lab and wait for the VM to finish provisioning.
2. Open the Viewer tab and bring up JupyterLab, confirm the file browser and launcher actually render, not just a blank page.
3. Open one notebook (for example `lab_0.1_healthcheck.ipynb`) and run the first cell to confirm the kernel starts.
4. If a check fails, note exactly what you saw, error text, stuck spinner, or blank page, instead of just "broken".
5. Post your status in Zoom chat using the capture template: `PASS` if everything worked, or `BLOCKER: <what failed>` if it did not, in-room and remote learners both post, so the instructor gets one clean status list.
6. If you posted BLOCKER, add one detail, which step failed and the exact message, so a TA can triage without a follow-up question.
7. Watch the chat for the instructor's all-clear before moving on; a PASS on your machine plus a room full of BLOCKERs still means wait.

## Key takeaway 💡
A healthcheck is only useful when its result is visible and specific: `PASS` or `BLOCKER: <what failed>` beats silence or "it doesn't work" every time.

## Study further 📚
- [JupyterLab Documentation, Project Jupyter](https://jupyterlab.readthedocs.io/en/stable/), official reference for the interface you just opened.
- [Project Jupyter Documentation Hub](https://docs.jupyter.org/en/latest/), starting point for notebooks, kernels, and the Jupyter ecosystem.
- [Python 3 Documentation, Python.org](https://docs.python.org/3/), official documentation for the language your lab notebooks run on.

## Common mistake to name ⚠️
Posting "it works" with no evidence, or a vague BLOCKER with no error text. The exercise *is* the status message; a PASS nobody can trust, or a BLOCKER nobody can triage, just moves the delay later in the session.

## If finished early ⏩
Run the remaining healthcheck cells and treat the network check as informational, then reply in chat to one BLOCKER post with a suggestion if you have seen that failure before.

**Solution link in master guide:** `#answer-0-1`
