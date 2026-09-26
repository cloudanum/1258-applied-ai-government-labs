# Sample / solution

## Why this approach works
The triad is the shared vocabulary between AI teams and security teams: once a failure maps to a leg, existing controls, owners, and incident processes apply. Sorting by what happened, was something exposed, changed, or unavailable, keeps quiet Integrity failures like a silently changed benefit amount from going unnoticed just because breaches make the headlines.

## A complete solution
Full placement: Confidentiality gets F1 (citizen addresses emailed to the wrong list), F4 (training data on a contractor's personal laptop), and F8 (another person's medical detail in a records response), each one something exposed. Integrity gets F2 (benefit amount silently changed after a bad update), F5 (prompt injection rewriting the assistant's instructions), and F7 (source data edited so future reports are wrong), each one something changed. Availability gets F3 (chatbot down during an emergency declaration) and F6 (flood takes out the only hosting region). Chat post: `C: F1, F4, F8 | I: F2, F5, F7 | A: F3, F6 | spans two: F5`.

F5 is the placement to defend. The wrong instinct is Confidentiality because injections are associated with leaks; the correct call is Integrity, because the injection changes the assistant's instructions, and changed instructions are corrupted configuration, no different in kind from F2's changed benefit amount. It becomes Confidentiality the moment the hijacked instructions make the assistant leak records, which is why one incident can need two owners. One-sentence defense on the board: "F5 is Integrity because the injected text changes what the system is instructed to do; it only becomes Confidentiality if the changed instructions then expose records."
