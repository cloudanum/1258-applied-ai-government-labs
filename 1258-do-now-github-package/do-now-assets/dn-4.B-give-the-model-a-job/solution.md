# Sample / solution

## Why this approach works
A role line decides what the model notices before it writes a word: a records officer scans for exemptions and deadlines, a communications director scans for what a resident would misread and what a reporter would quote. The contract half makes the answer reviewable; you can say an answer is wrong only if you first said what right looks like.

## A complete solution
For the records task: `Task: Summarize a public-records request | Role: You are a government records officer | Output must look like: issues identified, exemptions to check, and a draft response in 5 bullets`. For the chatbot task: `Task: Review a chatbot answer | Role: You are a cautious communications director | Output must look like: factual risk, tone risk, and a revised answer`.

The chatbot review is the one worth defending, because the role choice is the tricky part. "You are an AI expert" flags how the model failed, but the person who owns the failure in government is the communications director, whose job is to ask what happens when this answer gets screenshotted. The contract forces the review into three fields I can act on: factual risk is anything the answer asserts that we cannot source, tone risk is anything dismissive, speculative, or blaming the resident, and the revised answer is the version I could publish today. Both prompts fit the `Task | Role | Output must look like` template exactly, and a colleague could run either tomorrow and get a comparable result.
