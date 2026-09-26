#!/usr/bin/env python3
"""Build 1258-DoNow-Master-Guide-Standalone_custom.html from the enriched standalone guide.

Adds a 'Targeted students' block to each activity: 0-3 students from the class
Google Sheet (Main tab) whose stated interests/verbs match the activity, plus a
short paragraph on how the activity helps them. Does NOT modify the original guide.
"""
import re, pathlib

ROOT = pathlib.Path(__file__).parent
SRC = ROOT / "1258-Workbook-Standalone.html"
OUT = ROOT / "1258-Workbook-Standalone_custom.html"

# anchor -> (student names, how this activity helps them)
TARGET = {
 "activity-0-1": (["Vijayalakshmi", "Joe C", "Vikas Vaid"],
    "All three rated their Python and ML exposure at 0, so this healthcheck removes the first barrier to the course: proving the environment works before content begins. For Joe, who is mid-implementation on a basic project, a working lab VM also doubles as a safe sandbox for his own experiments."),
 "activity-0-2": (["Vijayalakshmi", "Natalie Sherwood", "Rob H."],
    "These three all listed summarize/explain/recommend-style verbs but rated their GenAI skill at 0-1, so an honest baseline card plus a Bloom home level is exactly their starting point: Natalie's list/compare/summarize/explain verbs sit mostly at L1-L2 (Remember/Understand), Rob's summarize/compare/explain/recommend spread from L2 up to L5, and Vijayalakshmi's extract/summarize/recommend/generate span the full ladder. Seeing their own verbs land on the ladder is the moment the framework becomes personal."),
 "activity-0-3": (["Jerri", "Vikas Vaid", "Lynn Ibrus"],
    "Jerri works in Public Safety and Lynn in Finance, two verticals where the wrong paste can become an incident; Vikas in IT Support fields these questions from colleagues. The Approved/Caution/No sort gives all three a two-question test they can apply before anything leaves their browser."),
 "activity-1-a": (["Tyler Moule", "Lynn Ibrus", "Tyler Bested"],
    "Tyler M. rated ML at 2, the highest in the class, and Lynn does financial data analytics and modelling, which is classic ML territory. Sorting U1-U8 lets them confirm their instincts while Tyler Bested practices the compare/diagnose verbs he listed."),
 "activity-1-b": (["John Cayton", "Rob H.", "Natalie Sherwood"],
    "John is making government data available for citizens, so audience switching is his daily job. Rob and Natalie both listed explain among their verbs; this drill turns that habit into a repeatable CIO-versus-citizen technique."),
 "activity-1-c": (["Tyler Moule", "Jerri", "Joe C"],
    "Jerri is considering chatbots, and this decision (prompt an existing model versus train your own) is the first fork in that project. Tyler M.'s ML background and Joe's basic implementation work make the volume/labels/repeatability test immediately usable for both."),
 "activity-1-d": (["Tyler Bested", "Jerri", "Vijayalakshmi"],
    "Tyler Bested and Jerri are the two students with Python at 1, so a zero-setup browser demo of entity and sentiment analysis shows them what an ML API returns before they ever write code. Vijayalakshmi listed extract as a verb; NER is extraction in its purest form."),
 "activity-2-a": (["Rob H.", "John Cayton", "Natalie Sherwood"],
    "Rob and Natalie recommend and explain for a living, which means their credibility rides on sourced claims. John is preparing citizen-facing data, where an unverified statistic can end up in a press release; the SUPPORTED-with-URL habit protects all three."),
 "activity-2-b": (["Tyler Bested", "Lynn Ibrus", "Fabrice Simo"],
    "Lynn's classify/infer verbs and Tyler's diagnose verb are exactly the patterns hiding in E1-E8. Fabrice listed compare and recommend, so naming the pattern behind each scenario builds the vocabulary he needs to scope AI ideas in his own team."),
 "activity-2-c": (["John Cayton", "Joe C", "Vijayalakshmi"],
    "John is literally in the stage of making datasets available for citizens, so the ask-then-verify loop is his workflow with a safety catch. Joe and Vijayalakshmi both listed extract as a core verb; verifying before trusting an AI-suggested URL is the cheapest extraction insurance there is."),
 "activity-2-d": (["John Cayton", "Lynn Ibrus", "Jerri"],
    "John needs citizen-ready datasets, Lynn needs financial data series, and Jerri needs public-safety reference data for chatbot grounding. Leaving class with one personally vetted bookmark gives each of them a starting asset rather than a generic list."),
 "activity-3-a": (["Natalie Sherwood", "Rob H.", "Vikas Vaid"],
    "Summarize is a top-listed verb for all three. Rewriting one paragraph for a named reader converts that habit into a controlled prompt technique they can reuse for status reports, ticket notes, and citizen updates the same afternoon."),
 "activity-3-b": (["Joe C", "Fabrice Simo", "Tyler Bested"],
    "Joe is documenting a basic implementation, and a process flow is the diagram his stakeholders will ask for. Fabrice and Tyler Bested both compare options for a living; turning text into a diagram is how you make a process comparable at a glance."),
 "activity-3-c": (["Jerri", "Lynn Ibrus", "Vikas Vaid"],
    "Public-safety case text, financial records, and IT support logs are exactly the C2/C5/C6-style stickies on this board. These three get a personal paste/no-paste rulebook tuned to the data classes they actually touch."),
 "activity-3-d": (["Vikas Vaid", "Vijayalakshmi", "Rob H."],
    "Vikas and Vijayalakshmi sit in IT, where shadow AI shows up as tickets and odd network traffic first. Rob's compare verb fits the inventory format; together they leave with a blame-free register template their organizations can adopt."),
 "activity-4-a": (["Vikas Vaid", "Natalie Sherwood", "Vijayalakshmi"],
    "All three are GenAI level 1 and listed extract/summarize as verbs. Few-shot examples are the single biggest quality jump available to a beginner, and this drill gives them the before/after evidence on a task shape they recognize."),
 "activity-4-b": (["Tyler Moule", "Joe C", "Fabrice Simo"],
    "Tyler M. listed generate and recommend, and Joe and Fabrice both generate content in their work. Assigning the model a role plus an output contract turns those generation requests from one-line wishes into repeatable instructions."),
 "activity-4-c": (["Lynn Ibrus", "Vijayalakshmi", "Natalie Sherwood"],
    "Lynn models financial data, so specifying columns and shapes is home turf; Vijayalakshmi's extract verb and Natalie's list verb both depend on structured output. Asking for the shape up front is the skill that makes AI output paste-ready."),
 "activity-4-d": (["Jerri", "Vikas Vaid", "Rob H."],
    "Jerri's chatbot idea lives or dies on grounded answers, and Vikas in IT Support needs assistants that say 'not stated' instead of inventing fixes. Rob's summarize habit gains the discipline of answering only from the source."),
 "activity-5-a": (["Jerri", "Lynn Ibrus", "Vikas Vaid"],
    "Jerri's public-safety context, Lynn's financial models, and Vikas's support systems each face a different top risk on this grid. Ranking R1-R8 forces each of them to name which failure their own organization would fund first, which is the argument they will need back at work."),
 "activity-5-b": (["Vikas Vaid", "Vijayalakshmi", "Jerri"],
    "Both IT students and the public-safety student handle incidents where the question 'was it confidentiality, integrity, or availability?' decides who responds. Mapping F1-F8 to the triad gives them a shared vocabulary with their security teams."),
 "activity-5-c": (["John Cayton", "Tyler Moule", "Jerri"],
    "John's citizen-data project is exactly the kind of use case OMB-style screening exists for, and Tyler M.'s guidance role means he will answer this question for others. Jerri's chatbot concept gets an early read on whether it would count as high-impact before any build starts."),
 "activity-5-d": (["Jerri", "Vikas Vaid", "Vijayalakshmi"],
    "If Jerri deploys a chatbot, A1-A6 are the first six messages it will receive. Vikas and Vijayalakshmi in IT will be asked 'is our assistant safe?'; red-teaming mentally teaches them what a real attack looks like before one arrives."),
 "activity-5-x": (["Tyler Moule", "John Cayton", "Jerri"],
    "Tyler M. is working on guidance areas for AI use, which is this activity at organizational scale. John's citizen-data project and Jerri's chatbot both need responsible-AI practices mapped to lifecycle stages with named owners, not a policy PDF nobody reads."),
 "activity-6-a": (["Lynn Ibrus", "John Cayton", "Tyler Bested"],
    "Lynn's financial models fail silently on dirty inputs, and John's citizen datasets will be judged on quality dimensions exactly like these ten rows. Tyler Bested's diagnose verb gets a workout spotting the seeded flaws."),
 "activity-6-b": (["Tyler Bested", "Jerri", "John Cayton"],
    "The two Python-capable students, Tyler Bested and Jerri, can take a proposed schema straight into code, while John's data-availability project needs exactly this artifact: field names, types, and justifications that survive an open-data review."),
 "activity-6-c": (["Lynn Ibrus", "Tyler Bested", "Fabrice Simo"],
    "Lynn's in-year/out-year financial modelling is the class's most natural synthetic-data candidate, since real ledgers can't be shared. Tyler Bested and Fabrice practice the compare verb by separating real, synthetic, and neither on the board."),
 "activity-6-d": (["Lynn Ibrus", "Vijayalakshmi", "Vikas Vaid"],
    "Lynn cleans financial data routinely, and Vijayalakshmi's and Vikas's extract/summarize work stalls on messy inputs. Writing the cleaning rules as an explicit prompt with a JSON contract turns an ad-hoc chore into a reusable asset."),
 "activity-7-a": (["Tyler Bested", "Jerri", "Tyler Moule"],
    "Tyler Bested and Jerri have the Python background to actually pull a model card's model down after class, and Tyler M. (ML level 2) can read licenses and limitations with a practitioner's eye. The tour shows all three where vetted models live."),
 "activity-7-b": (["Lynn Ibrus", "Tyler Bested", "Joe C"],
    "Lynn in Finance is the person who will be asked what agency-scale AI costs, and the token-multiplication chain is her defensible answer. Tyler Bested listed calculate as a verb, and Joe's basic implementation needs a cost story before it needs more features."),
 "activity-7-c": (["Tyler Bested", "Jerri", "Joe C"],
    "Tyler Bested and Jerri (Python 1) already think in versioned artifacts, and Joe is mid-implementation where an unversioned prompt edit is a real risk. The minimum header gives all three a change-management habit that scales from one prompt to a service."),
 "activity-7-d": (["Jerri", "Vikas Vaid", "Tyler Moule"],
    "Jerri's chatbot plan is a RAG plan, and this activity names the six ways it will fail before users do. Vikas needs to triage 'the assistant gave a wrong answer' tickets by layer, and Tyler M.'s guidance work needs this vocabulary to advise teams honestly."),
 "activity-8-a": (["Tyler Bested", "Lynn Ibrus", "Tyler Moule"],
    "Tyler Bested's diagnose/calculate verbs and Lynn's infer verb map directly onto choosing the metric that catches each failure. Tyler M., at ML level 2, gets to pressure-test his intuition that accuracy alone never catches the failures that matter."),
 "activity-8-b": (["Joe C", "Jerri", "John Cayton"],
    "Joe's basic implementation, Jerri's chatbot idea, and John's citizen-data release are all pilots-in-waiting. Scoring the five readiness items shows each of them the single lowest gap to close before their project can be called production."),
 "activity-8-c": (["Lynn Ibrus", "Natalie Sherwood", "Rob H."],
    "Lynn reads financial dashboards, and Natalie and Rob both listed compare as a verb. The critique drill sharpens the exact instinct they need: spotting a truncated axis or an undefined denominator before it reaches a decision-maker."),
 "activity-8-d": (["Rob H.", "Natalie Sherwood", "John Cayton"],
    "Rob and Natalie recommend and explain publicly, so a wrong 'current comment period' answer lands on their desk. John's citizen-facing data work makes the ask-then-verify habit with an authoritative URL a daily professional safeguard."),
 "activity-9-a": (["Vijayalakshmi", "Natalie Sherwood", "Vikas Vaid"],
    "All three started at GenAI level 0-1 with summarize/extract verbs, so their P0 baseline has the most room to grow. Rewriting it with role, audience, source limits, and format shows them the gap between their day-one prompt and a production-shaped one."),
 "activity-9-b": (["Joe C", "Jerri", "John Cayton"],
    "Joe has an implementation underway, Jerri has a chatbot concept, and John has a citizen-data goal; this activity converts each into a use case with a named user and a measurable result, the sentence their sponsors will ask for first."),
 "activity-9-c": (["Jerri", "Lynn Ibrus", "Tyler Moule"],
    "Jerri's public-safety chatbot needs a guardrail named before it needs a feature, Lynn's financial outputs need a review control, and Tyler M.'s guidance work means writing guardrails others will follow. The risk/guardrail/owner triple is the format that survives an audit."),
 "activity-9-d": (["John Cayton", "Joe C", "Tyler Moule"],
    "John listed execute among his verbs and his citizen-data project needs exactly this roster: sponsor, data owner, security, legal, ops, and a real user. Joe's implementation and Tyler M.'s guidance role both stall without the missing role named."),
 "activity-b-x": (["Jerri", "Vikas Vaid", "Natalie Sherwood"],
    "A public-safety chatbot will receive hostile or distressed language, and Jerri needs a moderation rubric before launch. Vikas in IT Support and Natalie with her explain verb benefit from scoring borderline phrases consistently rather than by gut feel."),
}

if __name__ == '__main__':
    doc = SRC.read_text()
    doc = doc.replace("<b>Workbook, Standalone Board Edition</b>", "<b>Workbook, Standalone Board Edition (Custom: student-interest targeting)</b>")
    doc = doc.replace("<div class=\"notice\">",
        "<div class=\"notice\"><b>Custom edition:</b> each activity lists up to three students whose stated interests "
        "(from the class intake sheet) match it best, with a short note on why the activity matters for them. "
        "Use it to cold-call with purpose or to pair students deliberately. ", 1)

    count, missing = 0, []
    for anchor, (names, para) in TARGET.items():
        tag = f"<a id='{anchor}'></a>"
        i = doc.find(tag)
        if i == -1:
            missing.append(anchor); continue
        start = doc.rfind("<section class='activity'>", 0, i)
        end = doc.find("</section>", i) + len("</section>")
        sec = doc[start:end]
        block = (f"<p><span class='label'>👥 Targeted students:</span> <b>{', '.join(names)}</b></p>"
                 f"<p class='small'>{para}</p>")
        marker = "<p><span class='label'>💡 Key takeaway:</span>"
        if marker not in sec:
            missing.append(anchor + " (no takeaway marker)"); continue
        sec = sec.replace(marker, block + marker, 1)
        doc = doc[:start] + sec + doc[end:]
        count += 1

    OUT.write_text(doc)
    print(f"custom guide written: {count}/41 activities targeted")
    for m in missing: print("MISSING:", m)
