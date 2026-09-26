# Sample / solution

## Why this approach works
Prompt vs. train is a resource question, not a prestige question: prompting wins when the context fits in the request and the task is occasional, while training earns its keep only when sustained volume, a label source, and a repeatable definition of correct all line up. Importance is not scale.

## A complete solution
T6 is the stickiest call. A full defense sounds like this: "I place T6 in Train. The modern instinct is to prompt a general vision model with 'is this stop sign damaged?', and that is exactly how I would pilot it. But the deciding factors are fleet-wide volume and consistency: thousands of photos a day need the same definition of 'damaged' applied the same way every time, with an error rate the roads division can audit. A prompted general model drifts on borderline cases and gives you no stable answer key to test against; a trained vision classifier gives you a repeatable, auditable decision."

The rest of the board sorts on the scale signal: T1, T3, T5 to Prompt (the needed context fits in the request); T2, T4, T6 to Train (nightly volume over 2 million requests, weekly confirmed-fraud labels, fleet-wide photo classification). Posted remotely: `T1-Prompt, T2-Train, T3-Prompt, T4-Train, T5-Prompt, T6-Train`. If you cannot name a Train sticky's label source, owner, and retraining cadence, argue it back down to Prompt.
