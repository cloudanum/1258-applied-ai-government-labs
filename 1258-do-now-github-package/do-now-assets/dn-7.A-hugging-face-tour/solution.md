# Sample / solution

## Why this approach works
Task, license, and limitations are the three procurement questions a model card answers on one page: what the model is for, whether you may use it, and where it will break. Requiring one stated limitation in every post is the discipline that proves the card was actually read.

## A complete solution
Working the README's default example, `distilbert-base-uncased-finetuned-sst-2-english` yields the three facts in under five minutes. The pipeline tag reads text classification (binary sentiment, positive versus negative). The license tag reads Apache 2.0, which permits government reuse with attribution. The card states the limitations: fine-tuned on SST-2, a dataset of English movie-review sentences, so it expects short English text, inherits that data's biases, and has never seen government language like case notes or service requests.

Posted in Zoom chat in the capture template:

`model: distilbert-base-uncased-finetuned-sst-2-english, limit: trained on English movie-review sentences, so it is not tuned to agency language and inherits its training data's biases`

Scanning peers' posts: shortlist a model whose license permits agency use and whose domain matches yours, and reject one with a one-word reason, for example a non-commercial-licensed summarizer rejected with the single word "license."
