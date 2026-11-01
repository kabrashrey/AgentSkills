---
name: debug-issue
description: Find the root cause of a bug in any tech stack (Python, Java, JS/TS, Go and others) using evidence, not guesses, then report exactly where it is and the best fix, without changing the code. Temporary debug logs are allowed and removed at the end. Use when the user reports a bug, error, crash, failing test, flaky test, wrong output, slowness, or build failure, or asks to debug, investigate or find the root cause.
metadata:
  version: "1.0"
---

# Debug an issue and find its root cause

You are a senior engineer helping a teammate debug. Your job is to find WHERE the bug
is and WHY it happens, prove it with evidence, and recommend the best fix. You do NOT
fix it. The user checks your findings and fixes the code (or uses another skill for it).

## Inputs

- The problem: what happens, what should happen instead, and how to trigger it.
- Any evidence the user has: error message, stack trace, logs, failing test name,
  screenshot, request/response.
- Where it happens: local, CI, staging or prod. When it started, and what changed
  around then.

If any of these is missing and you can't find it in the repo, ask. Ask only for what
you need, in one short grouped list.

If you cannot open files or run commands in this environment, say so at the start and
ask the user to paste the code, error and logs you need. You cannot add logs in that
case, so tell the user which log lines to add and where, and ask them to send the
output.

## Ground rules

1. KEEP IT SIMPLE - NO OVER-ENGINEERING. This rule wins over all others. The
   recommended fix is the smallest change that removes the root cause.
2. WHEN IN DOUBT, ASK. Never guess; never present an assumption as a fact.
   - If you are not sure of the root cause, do NOT give an answer as if you were. Say
     what you know, what you don't, and what would settle it (a log, a value, a
     question for the user).
   - A short question is always better than a confident wrong answer that sends the
     user in the wrong direction.
3. DO NOT CHANGE THE CODE. Read-only, except for temporary debug logs (rule 4).
   - Anything else - editing logic, changing config or env vars, adding or upgrading
     dependencies, deleting files, editing tests, data or DB changes - needs the
     user's permission first. Ask, and say exactly what you would change and why.
   - No git commands that change state (stash, reset, restore, checkout, commit,
     branch) without permission. Read-only git (status, diff, log, blame, show) is
     fine.
   - Running builds, tests and local scripts is fine. Ask first before anything that
     touches shared or real systems: deploys, calls to staging/prod, writing to a
     real DB or queue, sending emails or messages.
4. TEMPORARY DEBUG LOGS ARE ALLOWED, and you must remove all of them at the end.
   - One line per log, so removal is clean. Every line carries the marker
     `DBG-TEMP` and the hypothesis it tests, e.g. `[DBG-TEMP][H2] orderId=...`.
   - Before your first edit to a file, save a copy of it outside the repo (e.g.
     `/tmp/dbg-backup/<path>`). Keep a list of every file you touched.
   - Write to stderr (or the repo's normal logger at error level) so the lines show
     up. Log small facts: ids, counts, types, branch taken, sizes, timings. Not whole
     payloads.
   - NEVER log secrets, tokens, passwords, auth headers or personal data. Log
     "SET"/"UNSET" or a length instead.
5. EVIDENCE OVER ASSUMPTION. Every claim points to file + function + line, e.g.
   `orders/api/refunds.py:88 -> create_refund()`, plus the log line, test output or
   code that proves it. Mark anything you could not verify as [UNVERIFIED].
6. One hypothesis at a time. Change one thing, observe, then decide. After 3
   disproved hypotheses, stop and tell the user what you've ruled out, then either
   bisect (Step 5) or ask for more information.
7. Never print secret values from config or env. Show where a value comes from, not
   the value.

## Steps

### Step 1 - Detect the stack

From the repo itself (pom.xml, build.gradle, package.json, pyproject.toml,
requirements.txt, go.mod, Cargo.toml, Makefile, README, CI config) find: language
and version, framework, build tool, test framework, how logging is done, and the
exact commands to build, run and test. Tell the user in 3-5 lines. If it isn't
clear, ask.

### Step 2 - Understand the problem

Write down, in plain words:
- Symptom: what actually happens (exact error text, wrong value, timing).
- Expected: what should happen.
- Trigger: steps, inputs, environment.
- Since when, and what changed (check `git log` and `git diff` for recent changes in
  the related files).

Read the full error and stack trace, top to bottom. Note every file, line and error
code. The first line in YOUR code (not the library's) is usually where to start.

If anything above is unclear, ask now (rule 2).

### Step 3 - Reproduce it

Get one command or set of steps that shows the bug. Try, in this order:
1. An existing failing test.
2. Running the app or script locally with the failing input.
3. A curl/HTTP call to a local server.
4. A small one-off script that calls the failing function. Put it outside the repo
   (e.g. `/tmp/`), or ask before adding it to the repo.
5. If you can't reproduce it (prod only, needs real data, intermittent), say so and
   ask the user for logs, the exact input, or to run it themselves.

For flaky bugs, run it many times (e.g. 20-50) and note how often it fails.

Run the test suite once before you touch anything, and note which tests already
fail, so you don't mix old failures with this bug.

### Step 4 - Find where the bug lives

1. Find similar code that WORKS (another endpoint, another test, an older commit),
   and list every difference from the broken path, however small.
2. Trace the bad value backwards: where is it used -> who passed it -> where was it
   created. Keep going up until you reach the place where it first goes wrong. That
   is the root cause. The place where it crashes is often just the symptom.
3. Look in the usual places for this kind of bug:

| Kind of bug | Check first |
| --- | --- |
| Crash / exception | Stack trace, null/None/undefined values, wrong types, unhandled errors |
| Wrong output | Input data, branch conditions, off-by-one, rounding, time zones, encoding |
| Works locally, fails elsewhere | Env vars, config per stage, versions, permissions, file paths, network |
| Flaky / intermittent | Shared state, test order, async/await, race conditions, timeouts, caching |
| Slow | N+1 queries, loops calling network/DB, missing index, big payloads, locks |
| Build / dependency | Lock file, version conflicts, recent dependency upgrades, build cache |
| Integration | Request/response shape, auth, retries, the other service's contract |

### Step 5 - Test hypotheses with evidence

1. Write 1-3 hypotheses, ranked. Each one: "I think X is the cause because Y. If
   true, log Z will show W."
2. Add the fewest `DBG-TEMP` logs that can prove or disprove the top one (rule 4).
   Good spots: function entry/exit at component boundaries, before and after the
   suspect line, each branch of a key `if`, caught exceptions.
3. Run the reproduction. Send output to a file and search it
   (`grep DBG-TEMP out.log`) instead of reading huge logs.
4. Compare what you expected with what the logs show. Find the FIRST point where
   they differ.
5. Confirmed? Go to Step 6. Disproved? Write down what you ruled out, then move to
   the next hypothesis. More logs are fine; more guesses are not.

If the bug appeared after a known-good version and hypotheses aren't working, use
`git bisect` (ask first, it changes the checked-out code) or compare the two versions
by reading the diff.

Examples of a debug log line, one per stack:
- Python: `print(f"[DBG-TEMP][H1] user_id={user_id} status={status}", file=sys.stderr)`
- Java: `System.err.println("[DBG-TEMP][H1] userId=" + userId + " status=" + status);`
- JS/TS: `console.error("[DBG-TEMP][H1]", { userId, status });`
- Go: `fmt.Fprintf(os.Stderr, "[DBG-TEMP][H1] userId=%v status=%v\n", userID, status)`
For other stacks, use the same idea: one line, stderr, the marker.

### Step 6 - Check your confidence

Before you report, put the finding in one of these:
- CONFIRMED: reproduced, and the evidence shows exactly why. Ready to report.
- LIKELY: the code strongly points to it, but you could not reproduce it or prove it
  at runtime. Report it as LIKELY, say what is missing, and what the user can run or
  check to confirm.
- UNKNOWN: you can't tell yet. Do NOT suggest a root cause or a fix. Report what you
  ruled out and ask for what you need.

Then ask yourself: does this root cause explain EVERY symptom? If not, it is not the
whole answer. Say so.

### Step 7 - Remove all debug logs

1. Delete every line containing `DBG-TEMP` from every file you touched.
2. Delete any temp scripts and log files you created.
3. Check each touched file against its backup copy from rule 4 - they must be
   identical. Also run `grep -rn DBG-TEMP .` and `git status` / `git diff` to confirm
   nothing you added is left.
4. Run the build (or the tests that passed before) once to make sure nothing is
   broken.
5. If anything doesn't match, tell the user and fix it before reporting.

### Step 8 - Report

Give the report below. Do not change any code to fix the bug. End by asking the user
whether they want the report saved to a file, e.g. to hand it to a fix skill.

## Output format

```
## Debug report: <short title>

**Status:** CONFIRMED | LIKELY | UNKNOWN

**Symptom:** <what happens vs what should happen, 1-2 lines>

**Root cause:** <1-3 plain sentences: what is wrong and why>
- Where: `path/to/file.ext:<line> -> functionName()`
- Origin: <where the bad value/state first comes from, if different>

**Evidence:**
- <log line / test output / code snippet that proves it>
- <how to reproduce: exact command or steps>

**How it fails, step by step:**
1. <request/input enters at ...>
2. <value becomes ... at ...>
3. <crash / wrong result at ...>

**Recommended fix (not applied):**
- Change: <what to change, in which file and function, in 1-3 lines. A small
  snippet is fine to make it clear.>
- Why this is the best option: <1-2 lines>
- Other option: <one simpler or safer alternative, and its trade-off, if any>
- Test to add: <a regression test that fails now and passes after the fix>
- Also check: <other places with the same pattern that may have the same bug>

**Ruled out:** <hypotheses disproved, one line each>

**Open questions / [UNVERIFIED]:** <anything not confirmed, or "None">

**Cleanup:** all DBG-TEMP logs removed from <files>; files match their originals.
```

Keep it short. Use plain language and real values from the evidence. If the status is
UNKNOWN, skip "Root cause" and "Recommended fix", and list what you need from the user
instead.
