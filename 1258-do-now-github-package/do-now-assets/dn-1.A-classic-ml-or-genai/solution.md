# Sample / solution

## Why this approach works
Sorting by the verb, not gut feel, is what makes this defensible: predict, detect, assign, and cluster point to classic ML because the output is a number, label, or grouping from historical data, while draft, summarize, answer, and generate point to GenAI because the output is language. When a placement is uncertain, the use case is usually underspecified, which is a finding in itself.

## A complete solution
Take U6, "Answer questions from a fixed approved FAQ without inventing." A complete defense sounds like this: "I place U6 on the boundary. If we use GenAI, it must be grounded, answering only from the approved FAQ with an explicit 'not stated' fallback, because an ungrounded model will invent plausible-sounding policy. But the honest engineering answer is that classic retrieval or rules may be safer here: the FAQ is fixed, the answers are known, and there is an answer key to test against. I would only choose GenAI if residents ask in very varied natural language that a rules matcher keeps missing."

The other seven items sort cleanly: U1, U3, U5, U7 to classic ML; U2, U4, U8 to GenAI.
