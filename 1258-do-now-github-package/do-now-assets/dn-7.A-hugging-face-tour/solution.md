# Sample / solution

## Why this approach works
The three-fact extraction works because task, license, and limitations are the procurement questions in disguise: what is this model for, may we legally use it, and where will it break. A model card answers all three on a single page, which is why five minutes of reading beats five months of rework; an agency that adopts a model with the wrong license or the wrong domain discovers it at audit time, not at download time. The weak instinct is to judge by name, download count, or star rating: popularity says nothing about fitness for a government purpose, and a widely downloaded model can still be English-only, trained on movie reviews, or restricted to non-commercial use. Requiring one stated limitation in every post is the discipline that matters most, because every model has limits and a learner who cannot find one has not read the card.

## A complete solution
Working the README's default example, the model page for `distilbert-base-uncased-finetuned-sst-2-english` yields the three facts in under five minutes. The pipeline tag at the top reads text classification, specifically binary sentiment analysis, positive versus negative. The license tag on the right rail reads Apache 2.0, which permits government reuse, modification, and redistribution with attribution, so the procurement question has a clean answer. The limitations are stated on the card: the model was fine-tuned on SST-2, a dataset of English movie-review sentences, so it expects short English text, inherits the biases of that training data, and has never seen government language like case notes or service requests.

Posted in Zoom chat in the capture template, the artifact is one line:

`model: distilbert-base-uncased-finetuned-sst-2-english, limit: trained on English movie-review sentences, so it is not tuned to agency language and inherits its training data's biases`

Scanning peers' posts completes the exercise: shortlist any model whose license permits agency use and whose domain matches yours, and reject one with a one-word reason, license, language, or domain, for example rejecting a non-commercial-licensed summarizer with the single word "license."
