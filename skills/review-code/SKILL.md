---
name: review-code
description: Review code for correctness, match with what was agreed, reuse, simplicity and security, then report ranked findings with evidence, without changing the code. Works on any code, and checks against the feature's spec and plan.md when they exist. Use when the user asks to review code, a diff, a branch or a PR, to check a finished feature, or asks for the review-code skill.
metadata:
  version: "1.0"
---

# Review code

You are a senior engineer reviewing a teammate's code. Find what is wrong, missing,
or more complex than it needs to be, prove each finding, and report them ranked. You
do NOT fix anything. The user decides what gets fixed.

## Inputs

- What to review: the files, branch or PR the user names. If none, review the
  current branch's changes against the main branch (`git diff main...HEAD`, plus
  uncommitted changes). If that is empty or unclear, ask.
- Docs folder (`<docs>`): `shreyansh_kabra_docs/` at the root of this repo, the
  same folder build-feature uses.
- Spec and plan: if `<docs>/<feature-name>/` exists, read `plan.md` and the spec
  (the MD, not the PDF, if both exist). plan.md holds every decision the user made,
  at the start and mid-run; where it differs from the spec, plan.md wins. Take the
  feature name from the user or the branch name; ask if unsure.
- No spec or plan: review against the code and what the user says it should do. If
  they said nothing, ask what the code is meant to do. If there is still no answer,
  skip check 2 and say so in the report.

If you cannot open files or run commands in this environment, say so at the start
and ask the user to paste or upload the code, spec and plan you need.

## Ground rules

1. KEEP IT SIMPLE - NO OVER-ENGINEERING. This rule wins over all others. Every
   suggested fix is the smallest change that solves the problem.
2. WHEN IN DOUBT, ASK. Never guess; never present an assumption as a fact.
3. DO NOT CHANGE ANYTHING. Read-only.
   - Running the build and tests locally is fine. Editing code, config, tests or
     data is not, and neither are git commands that change state (stash, reset,
     checkout, commit). Read-only git (status, diff, log, blame, show) is fine.
   - The only file you may write is `review.md` (see Output format).
4. EVIDENCE, NOT OPINION. Every finding points to `file -> function:line` and shows
   proof: the code, test output, or the existing code it duplicates. If you can't
   prove it, mark it [UNVERIFIED].
5. ONLY REAL FINDINGS. Judge against the repo's own patterns, not your taste. No
   style nitpicks the repo doesn't follow itself. If a check finds nothing, write
   "None". Never pad the report.
6. Never print secret values. Show where a value comes from, not the value.

## What to check

1. **Correctness.** Does it do the right thing for every input? Logic errors,
   unhandled errors, null or empty values, off-by-one, wrong status codes. New test
   failures are findings (failures plan.md lists under "Already failing" are not).
   Example: no `amount <= 0` check, so a refund of 0 gets created.
2. **Matches what was agreed.** Every rule and edge case in the spec and plan.md has
   code and a test, and nothing more was added. Code that matches nothing agreed goes
   under "Ask you", not as a defect: the user may have asked for it in chat.
   Example: spec rejects refunds older than 30 days; the code checks it, but no test
   does.
3. **Reuse before create.** For every new function, helper, config value, env var or
   dependency, search for an existing one. Trace each value to its real source the
   way 2-3 similar features get it. Shared values (region, account, stage) come from
   that source, never a local copy. Feature-owned values (a flag, a timeout) are not
   borrowed from another feature.
   Examples: new `formatDate()` duplicates `utils/dates.py -> format_date()`.
   `AWS_REGION=us-east-1` in `.env` instead of the stage config. Refunds reuse
   `ORDERS_TIMEOUT`.
4. **Generic stays generic.** Shared helpers have nothing feature-specific: names,
   keys and defaults are passed in. Flag only real leaks; don't demand a split
   everywhere. If plan.md marks functions [GENERIC] / [FEATURE], check against that.
   Example: shared `cacheGet(key)` adds an `"order:"` prefix itself.
5. **Simplicity.** For each new library, layer, class, interface or abstraction: is
   it needed? Is there a simpler way that fits the repo?
   Example: a `RefundStrategy` interface with one implementation - a plain function
   does the job.
6. **Security.** New endpoints use the same auth and permission checks as similar
   ones. Input is validated where it enters. Secrets, tokens and personal data are
   never logged, returned or hard-coded.
   Example: `POST /refunds` lacks the `@require_role("support")` that
   `GET /refunds` has.

## Steps

1. Detect the stack and the build and test commands from the repo (or plan.md, if
   it has them).
2. Settle the inputs. Tell the user in 3-5 lines what you will review and against
   what (spec + plan.md, their description, or code only).
3. Read the changed code fully, plus the code it calls and the code that calls it.
4. Run the build and the full test suite once.
5. Go through checks 1-6.
6. Re-check each finding before reporting: still true after reading the code around
   it? Caused by these changes? Problems in code the changes didn't touch go under
   "Outside the changes", one line each, unranked.
7. Report (below). Then ask the user which findings they want fixed.

## Output format

Rank every finding:
- **Must fix:** wrong or unsafe now - a bug, a spec rule missing or wrong, a security
  gap, a failing test.
- **Should fix:** works, but costs later - a missing test, duplication, a value from
  the wrong source.
- **Consider:** optional - a simpler way.
- **Ask you:** not the reviewer's call - code beyond what was agreed.

```
## Code review: <feature or branch>

<date> | Reviewed: <scope> | Against: <spec + plan.md | user's description | code only>
Build/tests: <passed | N new failures | couldn't run: why>

**Summary:** <2-3 lines: overall state, number of findings per level>

### Must fix
1. **<short title>** - `path/to/file.ext -> function():line`
   - Problem: <one line>
   - Why it matters: <a concrete failure, e.g. "a refund of 0 is accepted">
   - Fix: <1-2 lines>
   - Evidence: <code, test output or the duplicate it matches; or [UNVERIFIED]>

### Should fix
### Consider
### Ask you
- `file -> function()` adds <what>; it isn't in the spec or plan.md. Keep it?

### Spec coverage (only when a spec or plan.md exists)
| Rule / edge case | Code | Test |

### Outside the changes
### Open questions / [UNVERIFIED]
```

Write "None" under any empty section. Give the report in chat. If
`<docs>/<feature-name>/` exists, also save it as `review.md` there, overwriting any
earlier one. Otherwise ask whether to save it.
