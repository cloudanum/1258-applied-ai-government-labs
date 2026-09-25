# Do Now 1.D: Try the Google NLP API 🎯

**Time:** 5 minutes
**Format:** No sandbox or tooling required, you only need a browser for the public demo page; observations are captured in Zoom chat (or on the Mural board if you are in the room).
**Mural:** https://app.mural.co/t/day10626/m/day10626/1790240786066/9b138b3dc8eb259be5ecf9efb2745bf9ae88df5c

## Goal
By the end of this five-minute warm-up you will have run real text through Google's hosted Natural Language demo and seen what a managed ML service extracts, entities, sentiment, categories, and moderation flags, without training anything yourself. The artifact you produce is one structured observation in chat: the detection that surprised you and why. The instinct you are building is that a large class of "AI projects" are really API calls to pre-trained managed services, and knowing what these services see in unstructured text, and what they get wrong, is a prerequisite for every buy-vs-build decision. Surprise is the point: the gap between what you expected the model to notice and what it actually noticed is where judgment forms.

## Why it matters
Before an agency trains anything, it should know what a managed service already does with its text, entities, sentiment, syntax, moderation, because buying that capability is often faster, cheaper, and easier to oversee. Doing it in chat makes the surprises visible and comparable: twenty learners pasting different texts produce an instant, crowdsourced map of the service's strengths and blind spots.

**Assets:** Public demo at https://cloud.google.com/natural-language/ (see `board-items.tsv`).

## Run steps 🪜
1. Open https://cloud.google.com/natural-language/ in any browser and scroll to the live demo, no account or setup needed.
2. Run the sample text first and look at all the result tabs: entities, sentiment, syntax, and categories/moderation.
3. Now paste a short paragraph of government-flavored text you invent, a public press release snippet or a made-up citizen complaint, never real case data or personal information.
4. Compare what the service detected with what you expected: which entities did it find or miss, and did the sentiment score match your own reading?
5. Post one observation in Zoom chat using the capture template: `Surprised me: entities/sentiment/moderation/categories because ___`, one detection, one reason.
6. Read the chat and find one observation that contradicts yours; reply with the type of text you used, since managed services behave differently across genres.
7. Keep one mental note for later modules: this API is the "buy" option you will compare against train-your-own in the NER lab.

## Key takeaway 💡
A managed NLP API turns unstructured text into entities, sentiment, categories, and moderation flags with zero training, knowing what it sees (and misses) is the baseline for every buy-vs-build decision an agency makes on language data.

## Study further 📚
- [Cloud Natural Language API, Google Cloud](https://cloud.google.com/natural-language/), the managed service you just tried, with its full feature list.
- [Analyzing entities, Google Cloud](https://cloud.google.com/natural-language/docs/analyzing-entities), how entity extraction works and what the API returns.
- [Analyzing sentiment, Google Cloud](https://cloud.google.com/natural-language/docs/analyzing-sentiment), how sentiment scores and magnitudes are computed.

## Common mistake to name ⚠️
Pasting real citizen data into a public demo "to see what happens", the demo is a third-party service, so invent your text. The second mistake is reporting scores with no surprise attached, which skips the judgment the exercise is building.

## If finished early ⏩
Run the same text twice with one word changed, a neutral word swapped for a charged one, and report in chat how much the sentiment or moderation output moved.

## ⭐ Bonus (optional)
Find one sentence where the API's entity or sentiment detection is flatly wrong, post the sentence type (not any sensitive content) with your verdict in chat, and name the class of government text, legal, medical, casework, where that error would matter most.

**Solution link in master guide:** `#answer-1-d`
