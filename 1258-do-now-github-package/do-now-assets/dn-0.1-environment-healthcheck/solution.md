# Sample / solution

## Why this approach works
The exercise is the status message, not the VM. A shared `PASS` token lets the instructor count ready machines at a glance, and a `BLOCKER: <what failed>` naming the step and exact error lets a TA triage without a follow-up question.

## A complete solution
A clean PASS needs no detail beyond the token itself; the template already says what it means: the VM provisioned, JupyterLab rendered in the Viewer, and the kernel started on the first cell of `lab_0.1_healthcheck.ipynb`.

`PASS`

A good BLOCKER post fills the `<what failed>` slot with the step and the exact message, for example:

`BLOCKER: JupyterLab loads in the Viewer but the kernel will not start, running the first cell of lab_0.1_healthcheck.ipynb hangs on "Connecting to kernel" for over two minutes.`

That line tells a TA where to look (Viewer is fine, the kernel is the fault) with no follow-up question needed.
