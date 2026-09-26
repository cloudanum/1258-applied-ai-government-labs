# Sample / solution

## Why this approach works
The exercise is the status message, not the VM. A bare `PASS` works only because it is the agreed contract: everyone in the room posts the same token, so the instructor can count ready machines at a glance and spot a platform-wide failure in seconds. A `BLOCKER: <what failed>` post earns its keep the same way: naming the step and the exact error text lets a TA triage without a follow-up question, while "it doesn't work" buys a ten-minute round trip of clarifying questions. The deeper habit is treating environment readiness as a first-class task with a visible, checkable result, not a private struggle, because every lab in this course depends on this VM. Posting to one shared channel is what turns one learner's glitch into a pattern the instructor can act on.

## A complete solution
A clean PASS needs no detail beyond the token itself, because the template defines what it means: the VM provisioned, JupyterLab rendered in the Viewer (not a blank page), and the kernel started on the first cell of `lab_0.1_healthcheck.ipynb`.

`PASS`

A good BLOCKER post fills the `<what failed>` slot with the step and the exact message, for example:

`BLOCKER: JupyterLab loads in the Viewer but the kernel will not start, running the first cell of lab_0.1_healthcheck.ipynb hangs on "Connecting to kernel" for over two minutes.`

That single line tells a TA where to look (Viewer is fine, the kernel is the fault) with no follow-up question needed. The weak version, "BLOCKER: notebook broken," gets challenged on exactly the two missing pieces: which step failed, and what you actually saw.
