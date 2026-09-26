# Do Now 7.A: Hugging Face Tour 🎯

**Time:** 5 minutes
**Format:** No sandbox or tooling required, just a browser tab open to huggingface.co; the activity is captured in Zoom chat (in-person learners can post as Mural comments on the board).
**Mural:** https://app.mural.co/t/day10626/m/day10626/1790240808058/4bd52685aa90ea52142c9275d286edd9d9b4f383

## Goal
Open one model page on the Hugging Face Hub and extract the three facts that matter for government use: the **task** the model performs, its **license**, and one stated **limitation**. Post your finding as a one-line chat message: `model: <name>, limit: <one limitation>`.

**Assets:** huggingface.co and the capture template (see `board-items.tsv`).

## Run steps 🪜
1. Open huggingface.co and search for a model on a task a government team might use, sentiment analysis, summarization, or named-entity recognition (`distilbert-base-uncased-finetuned-sst-2-english` is a good default).
2. Open the model's page and locate the model card, the README-style section below the header.
3. Find the three facts: the **task** (pipeline tag at the top), the **license** (right rail), and one stated **limitation**, language, domain, bias, or training-data vintage.
4. Ask the procurement question: could your agency legally and appropriately use this model? The license and limitations sections answer it.
5. Post in Zoom chat using the capture template: `model: <name>, limit: <one limitation>`; in person, add the same line as a Mural comment.
6. Scan two other learners' posts and note one model you would shortlist and one you would reject, with a one-word reason: license, language, or domain.

## Key takeaway 💡
A model card is the label on the package: task, license, and limitations tell you what a model is for, whether you may use it, and where it will break, five minutes of reading beats five months of rework.

## Study further 📚
- [Hugging Face Hub documentation, Hugging Face](https://huggingface.co/docs/hub/index), the official guide to models, datasets, and spaces on the Hub.
- [Model Cards, Hugging Face](https://huggingface.co/docs/hub/model-cards), what a model card contains and how to read one critically.
- [Model Cards, Google](https://modelcards.withgoogle.com/about), Google's model-card reports, showing the format applied to real production models.

## Common mistake to name ⚠️
Judging a model by its name or download count; require the license and one stated limitation in every post before it counts as done.

## If finished early ⏩
Find a second model that solves the same task and compare the two licenses, post the pair and name the one your agency could actually use.

## ⭐ Bonus (optional)
Open your model's "Files and versions" and "Community" tabs and note one thing each tells you that the model card does not, actual file formats, download trends, or reported issues.

**Solution link in master guide:** `#answer-7-a`
