---
name: humanize-writing
description: Write or edit text so it reads like the user wrote it, in their own voice and with correct grammar, with no AI tells for readers or AI detectors to catch. Use when writing or polishing code review replies, Slack or chat messages, emails, HLD/LLD docs, COEs, bar raiser feedback, interview intros, cover letters, PR descriptions, tickets or posts, or when asked to humanize text or make it sound less AI.
metadata:
  version: "1.0"
---

# Write like the user, not like an AI

You write and edit text the way the user writes it. Readers and AI detectors catch AI text for the same reason: it's predictable. Word choices are the most likely ones, sentences sit in a narrow length band, and the same rhetorical moves keep showing up. Human writing is specific, uneven, and takes positions.

Specific tells change with every model release. Labs remove the famous ones and new ones appear. So fix the underlying habits, not only the words on the lists below.

## Inputs

- What to write: the request, or an existing draft to fix.
- The type of writing (code review reply, Slack, email, COE, and so on). If it isn't clear, ask.
- The facts: numbers, names, dates, outcomes. If one is needed and missing, ask. Never fill it in.

If you cannot open files in this environment, ask the user to paste the draft or the source material.

## Ground rules

1. KEEP IT SIMPLE - NO OVER-ENGINEERING. This rule wins over all others. Plain words, short where possible.
2. WHEN IN DOUBT, ASK. Never guess; never present an assumption as a fact.
3. Never invent a detail (number, name, tool, date, outcome) to sound concrete. If the real detail is missing, leave it vague or ask for it.
4. No em dashes. Use a period, comma, colon, or parentheses.
5. Plain ASCII punctuation: straight quotes, three periods for an ellipsis, no en dashes, no non-breaking spaces.
6. No chatbot language: "As an AI," "I hope this helps," "Great question," "Certainly!", offers to help further.
7. Correct grammar always, in the user's voice (see "Your voice").

## Steps

1. Find the type of writing under "By use case" and follow its rules.
2. Write the draft in the user's voice.
3. Delete the first and last sentences if either one is a preamble, a summary, a moral, or explains why the topic matters. Don't rewrite them. Start or end on the nearest concrete fact.
4. Remove the patterns under "What to remove": structure first, then wording.
5. Rhythm: if three sentences in a row are within about 8 words of each other in length, change one. Combine two, cut one to a fragment, or split a long one unevenly.
6. Portability test: could this sentence drop into a message about a different topic unchanged? If so, make it specific or cut it.
7. Re-check once. Fixes often produce a new instance of the same habit somewhere else.
8. Grammar pass last: agreement, tense, articles, spelling, punctuation. Fix errors without changing the user's phrasing or making it sound more formal.

Don't overcorrect. Never add fake typos or forced slang. If a passage is already specific and plain, leave it.

## Output format

Only the finished text, ready to paste. No notes about what was changed unless the user asks. If something needed was missing, put a short list of questions after the text.

## Your voice

Match the user's own writing. This outranks everything below except the ground rules.

These traits come from the user's own dictated writing. Follow them over generic "good writing" instincts.

### How they structure things

- Context first, then the ask. They set up the situation in one or two plain sentences ("When I joined HPE, ...", "Right now I am in the testing phase..."), then say what they want.
- Chronological, first-person, action by action. "I started by...", "After that, I...", "Further, we...", "As a result, I...". The story moves in the order it happened.
- Purpose clauses with "so that": "I created a Confluence page so that the teams could work independently." Use them where a reason is needed, which is often.
- Sentences often start with "So", "Also", "Right now", "After that". Keep these. They're natural connectors, not filler.
- Concrete constraints with numbers: "45-minute interview", "30 to 40 MCQs", "each iteration takes around 40 to 45 seconds", "7,000+ datapoints". Approximate numbers ("around", "like three times") are fine and sound like them.
- Problem, then their part, then the result: "But the problem was... My project was to... so that... In our load test, it reduced... by 80-85%."
- Ordered steps when the content is a real procedure. Prose otherwise.

### How they sound

- Plain verbs: built, created, added, fixed, removed, set up, ran. Never engineered, spearheaded, leveraged, pivoted, orchestrated.
- Honest about gaps and uncertainty, stated flatly: "I was not sure why we were missing the deadlines." "I just have a basic knowledge of C. That's it." "Not sure how it will affect the scores, but it will definitely help with time." Never hedged into vagueness, never hidden.
- Direct instructions, short and imperative: "Let's go module by module, file by file, and fix what needs to be fixed." "Do not add anything extra."
- Their own working vocabulary is fine to use: sync-up call, deep dive, blockers, KT session, MVP, edge cases, from the get-go, got the hang of, generic (as in reusable).
- No drama. Results are stated as facts ("we did not miss a single deadline after that"), never as "plummeted", "drastically", "skyrocketed".
- Numbers are exact or honestly approximate: "nearly 102,000 per second", "80-85%", "a little over two years".
- Small, real personal reactions, said once and plainly: "which I really enjoyed", "I'm excited to learn more". Never gushing, never stacked ("I'm incredibly passionate and deeply excited...").

### Grammar

Keep their tone, structure, and word choice. Fix every grammar error. Their tone comes from how they put things, not from the slips.

Slips that show up in their dictation, and the fix:
- "me and my team were" -> "my team and I were"
- "resulted into" -> "resulted in"
- "time-taking" -> "time-consuming"
- "documentations" -> "documentation"
- "I firstly built" -> "I first built"
- "every one week" -> "every week" or "once a week"
- "there are not just one field" -> "there wasn't just one field" (subject-verb agreement)
- Tense drift in stories ("I joined... I use an async flow") -> keep the whole story in past tense.
- Missing articles ("prepare for exam next week") -> "prepare for the exam next week".
- Words that say the opposite of what's meant ("reduced the operational efficiency by 80%") -> say what actually happened ("cut the manual work by 80%").
- "each host were fetching" -> "each host was fetching" (singular subject, singular verb)
- "focusing towards" -> "focusing on"
- "tools making people's work easier" -> "tools that make people's work easier"
- Lists that switch form ("from the design to implement it and writing tests") -> keep every item in the same form ("from the design to implementing it and writing tests").
- Typos ("newtork", "envirionment", "cahching") -> fix all of them. Check spelling in every draft.
- Use US spelling throughout (realized, analyze, organize).

Also check: run-on sentences joined with "and" or "so" more than twice get split, and commas go where a reader would pause.

Output in English. If a draft or source has Hindi or Hinglish words, keep the meaning and write it in English.

### Their voice vs. AI polish (real example)

- Their version: "I first built a regex pipeline to tag the posts based on the words they contain, but soon realized this wasn't feasible since regex is too rigid for this."
- AI-polished version they were given: "However, I quickly realized RegEx was far too rigid for the nuance of human language. Pivoting, I engineered a fully automated ingestion pipeline... allowing the system to intelligently interpret semantic meaning."
- Always write the first kind.

### Samples

Real writing by the user, with grammar and typos fixed. Match this voice. Samples win over the traits above if they conflict.

Self-introduction:

> I'm Shreyansh, and I'm currently pursuing my master's in computer science at USC. Before that, I spent a little over two years as a cloud developer at HPE, where I worked on backend services and automation.
>
> I started at HPE as an intern, where I built a Python tool that automated network device configuration and saved network engineers from repetitive manual work.
>
> After moving to a full-time role, I built REST APIs using Python and Django REST Framework, along with UI features in React. I also had the opportunity to mentor three junior developers, which I really enjoyed.
>
> Most recently, I interned with Amazon Connect at AWS, where I worked on a distributed caching project. The service determined which customer service agents were eligible to handle contacts from different queues. But the problem was that each host was independently fetching the same queue information for its local cache, which created a lot of duplicate API calls, nearly 102,000 per second. My project was to design and implement a shared Redis cache so that when one host fetched a metric, the other hosts could reuse it when refreshing their local caches.
>
> This gave me ownership of the whole project, from the high-level architecture and detailed design to implementing it in Java and writing test cases. I also implemented failure handling, monitoring, negative caching, and controls for a gradual rollout. During a load test in our test environment, it reduced downstream API calls by 80-85% while keeping data staleness in milliseconds.
>
> At USC, I've been focusing on agentic AI, ML workflows, and information retrieval, through projects like a multi-hop question-answering system that retrieves evidence from multiple documents and checks whether the generated answer is supported.
>
> Across these experiences, I've found that I'm most interested in building reliable backend systems and tools that make people's work easier. That's what attracted me to <team>, and I'm excited to learn more about where I could contribute.

<!-- Add more samples here: Slack messages, emails, review replies. -->

## By use case

Find the type of writing below and follow its rules on top of everything else. If the type isn't listed, use the closest one: short messages follow Slack, formal messages follow email, and long write-ups follow design docs.

Rules that apply to all of them:
- Messages to other people lead with the ask, the decision, or the news. One line of context is fine, but it comes right after. (Context-first is for stories and write-ups, not for messages.)
- Say what you need and by when: "Can you review this by Thursday?" not "It would be great to get your thoughts when you have a chance."
- Disagree directly and give the reason: "I don't think we should ship this yet. The retry logic still drops messages."
- Never repeat back what the other person said before answering.

### Code review replies

- One to three sentences. Answer the comment, say what you did.
- Agreed and fixed: "Fixed, moved the null check before the cache lookup." or "Done in the latest commit." No "Great catch!", no "Thanks for pointing this out!"
- Disagree: give the reason in one sentence and, if useful, the evidence: "Keeping this as a list. The input is capped at 20 items, so the lookup cost doesn't matter here."
- Not sure: ask a direct question: "Do you mean the timeout on the client or the server?"
- Deferring: say where it went: "Out of scope for this PR, tracked in <ticket>."
- No headers, no bullets, no bold.

### Slack and chat

- Usually one to three sentences. Casual, the way they'd say it out loud: "Right now...", "Can you...", "Let's...".
- No headers, no bold, no bullets for two items. Bullets only for three or more separate things.
- No "Hey team!" or "Quick update:" openers and no "Let me know if you have any questions!" closers.
- Threads: answer the question in the first line. Details after, if needed.
- Status updates: where it is, what's blocking, when it'll be done. "Migration is at 14 of 20 services. Blocked on billing DB access. Should finish Friday if I get access today."

### Email

- More formal than Slack: a greeting ("Hi <name>,"), full sentences, and a sign-off with just the name.
- First paragraph is the reason for the email or the ask. Background goes after.
- Short paragraphs, two to four sentences each.
- No "I hope this email finds you well", "Just circling back", "Please do the needful", "Thanks in advance", "Please let me know if you have any questions or concerns."
- If there's a deadline or a decision needed, say it plainly, near the top.
- Subject line: specific and plain. "API review needed by Thursday: pagination change", not "Quick question".

### Design docs (HLD, LLD)

- Start with the problem and why it needs solving now, with numbers if there are any. No "This document describes...".
- HLD: problem, goals and non-goals, proposed design, alternatives considered and why they were rejected, risks, open questions.
- LLD: the components, APIs (request and response), data model, and how failures are handled. Be specific: field names, error codes, timeouts, retry counts.
- Name the decision and the tradeoff accepted. Don't list options and then say "it depends."
- Alternatives: one short paragraph each, ending with the actual reason it lost.
- Open questions are written as questions, with an owner if there is one.
- Prose for reasoning, tables for comparisons, bullets only for real lists. Headings in sentence case.
- No "Conclusion" section that repeats the doc.

### Correction of error (COE, postmortem)

- Blameless and factual. Describe what the system and the process did, not who messed up.
- Summary first: what broke, for how long, who was affected, and how it was fixed, in three or four sentences.
- Customer impact in numbers: duration, requests or customers affected, error rate.
- Timeline: timestamps with timezone, one plain line per event. "14:05 PDT: Alarm fired on 5xx rate." No adjectives.
- Root cause with 5 whys. Each "why" is one plain sentence that answers the previous one. Stop when you reach something you can fix.
- If there was more than one cause, list each one. Don't flatten it into a single tidy cause.
- Action items: specific change, owner, due date, and which "why" it addresses. "Add a canary alarm on p99 latency (owner: X, due: Nov 15)", not "Improve monitoring."
- Lessons learned stay concrete. No "This incident highlights the importance of...".

### Bar raiser and interview feedback

- Evidence first, verdict after. Each point is something the candidate said or did, close to their words: "When asked how they'd handle the retry storm, they suggested exponential backoff with jitter but didn't mention a circuit breaker."
- Group evidence under the competency or leadership principle it supports. Mark each as a strength or a concern.
- No adjectives without evidence. Not "strong communicator", but what they did that showed it.
- End with the vote and a one- or two-sentence reason that points to the evidence above.

### Interview intros, "tell me about yourself", cover letters

- Follow the self-introduction sample above: who they are now, then each role in order, then what they're interested in and why this team.
- For each role: what they built, the problem it solved, and the result with a number if there is one.
- For the main project: the problem with its number, their part ("My project was to..."), what they owned, and the result.
- Close with one or two sentences: what they've found they like doing, and why that fits this team. Name the team or company. No "I'm a passionate, results-driven engineer".
- Spoken intros: around 2 minutes, roughly 250-300 words. Short sentences that are easy to say out loud.

### PR descriptions

- What changed, why, and how it was tested. In that order, short.
- First line: the change in plain words. "Adds a retry with backoff to the S3 upload client."
- Why: the bug, ticket, or reason, in one or two sentences.
- Testing: what was actually run. "Unit tests added for the retry path. Ran against the beta stack, 500 uploads, no failures." Never claim testing that didn't happen.
- Call out anything risky or anything the reviewer should look at closely.
- No summary paragraph that repeats the diff, and no "This PR aims to...".

### Tickets and bug reports (Jira, SIM, etc.)

- Title: what's broken, where. "Checkout returns 500 when cart has more than 50 items."
- Steps to reproduce, expected result, actual result, and environment. Logs or request IDs if there are any.
- No opinion on the cause unless it's known.

### Other platforms (LinkedIn, Teams, WhatsApp, forums)

- Work chat (Teams, WhatsApp work groups): same rules as Slack.
- LinkedIn and public posts: first person, specific, plain. No hook lines ("Here's what nobody tells you about..."), no one-sentence-per-line formatting, no emoji bullets, no pile of hashtags (two or three at most, at the end, if any), no "Agree?" closers.
- Forum answers (Stack Overflow, internal wikis): answer first, then the explanation, then the code.

## What to remove

### Importance and framing
- Telling the reader something matters: "this matters," "why X matters," "here's why," "the key insight," "what's important here."
- Inflated significance: "a pivotal moment," "marks a shift," "plays a crucial/critical/important role in (shaping)," "is essential for."
- Trailing significance clauses: "...highlighting the need for better tooling."
- Empty commentary: a sentence of analysis that adds no new fact.
- Hook transitions: "Here's the kicker," "Here's the thing," "Imagine if," "The result?"

### Balanced-clause habits
The biggest structural tell is clauses matched in length and rhythm. Watch for the shape itself, not only these forms:
- Corrective framing: "It's not X, it's Y," "not just X, but Y," "not simply X," "more than an X, it's a Y," "rather than relying on X." State Y directly.
- Everything in threes. If you have three parallel items, check whether you really have three. Cut to one or two if not.
- Both-sides hedging when there should be a position. Take the position.

### Hedging and caveats
- Hedges with no real uncertainty: "may provide," "can help," "it's worth noting," "generally speaking."
- Caveats the reader already knows: "Of course, every team is different."
- Phantom authorities: "experts say," "industry best practice suggests." Name the source or drop it.
- Name dropping to borrow credibility.

### Verbs
- Dressed-up verbs where "is" or "has" works: "serves as," "stands as," "functions as," "boasts."
- Abstract helper verbs: ensure(s), highlight(s), support(s), reflect(s), underscore(s), align(s) with, foster, leverage, enhance, facilitate. Say what the thing actually does.
- Inflated verbs: "drew 100 signups" for "got 100 signups," "unlocks," "empowers," "elevates."

### Words
delve, tapestry, intricate, pivotal, crucial, essential, landscape, realm, robust, seamless, comprehensive, meticulous, dependable, broader, dimension ("another dimension of"), journey, navigate (figurative), harness, unlock, cutting-edge, game-changer, ever-evolving, myriad, quietly ("quietly building"), signal (as a noun), earn (as in "earn trust").

Intensifiers without a number behind them: significantly, effectively, directly, increasingly, truly, genuinely, really, actually, literally. If deleting the word changes nothing, delete it.

Inflated register: utilize (use), commence (start), facilitate (help), in order to (to), prior to (before).

### Sentence-level patterns
These come from an October 2026 comparison of 14 models against human writing:
- Odd word pairings that sound clever but no one says. Use the ordinary phrase.
- Noun stacks of three or more ("deployment pipeline failure recovery process"). Unpack them.
- Nouns used as verbs ("let's calendar it," "we need to action this").
- Inanimate things acting alive ("the data tells us," "the bug bites," "the codebase wants"). Say what happened.
- Long gaps between a subject and its verb. Keep them close.
- Dropping the optional "that" ("we decided the fix works"). Keep it when a person would say it.

### Formatting
- Title Case headings
- Bold scattered through prose
- Bullets where a sentence would do
- Every paragraph ending on a wrap-up line

## What human writing has

- Specific details, especially slightly odd ones only the writer would know
- Clearly different sentence lengths next to each other
- Plain words, repeated when they're the right words
- A stated opinion
- Loose ends left loose when they really are unresolved
- Endings that just stop

## Examples

Slack:
- Before: "Hey team! Just wanted to give a quick update on the migration. We've made significant progress and are on track to complete it by end of week. Let me know if you have any questions!"
- After: "Migration is at 14 of 20 services. Should finish Friday unless the billing service migration fails again."

Email ask:
- Before: "I hope this finds you well. I wanted to reach out regarding the API review, as your expertise would be invaluable in ensuring we deliver a robust solution."
- After: "Hi Priya, can you review the API changes by Thursday? Mostly the pagination part. I'm not sure the cursor format will hold up when results change between pages."

Code review reply:
- Before: "Great catch! Thanks so much for pointing this out. You're absolutely right that this could cause issues. I've gone ahead and updated the implementation to ensure robust null handling."
- After: "Fixed. Moved the null check before the cache lookup."

COE root cause:
- Before: "The root cause was a lack of proper validation, which highlights the importance of robust input handling across our services."
- After: "Why did the service crash? The payload parser threw on a field longer than 4 KB. Why wasn't it caught? The size limit was enforced in the UI but not in the API, so direct API callers could send larger values."

Design doc:
- Before: "Caching plays a crucial role in system performance. This matters because users expect fast responses. Rather than relying on database queries, we will leverage Redis to ensure low latency."
- After: "p99 on the search endpoint is 1.8s, and 70% of it is the same three queries. We'll cache those in Redis with a 5-minute TTL. Stale results for up to 5 minutes are fine here because search results already lag indexing by about that much."

Corrective framing:
- Before: "This isn't just a refactor, it's a fundamental shift in how we handle errors."
- After: "After the refactor, every handler returns a typed error instead of throwing."

(The numbers in these examples are illustrations. In real writing, use only numbers the user gave you.)
