# Agent Skills

My skills for AI coding agents. Each skill is one folder with one `SKILL.md`, in the
open Agent Skills format, so it works in Claude Code, Codex, Gemini CLI, Copilot and
other agents that support skills. For tools that don't, paste the `SKILL.md` contents
as the first message.

## Skills

| Skill | What it does | Version |
| --- | --- | --- |
| [build-feature](skills/build-feature/SKILL.md) | Understand, plan, build and explain a feature from a spec, simply | 1.0 |
| [humanize-writing](skills/humanize-writing/SKILL.md) | Write messages, docs and replies in my voice, with correct grammar and no AI tells | 1.1 |
| [debug-issue](skills/debug-issue/SKILL.md) | Find and prove the root cause of a bug in any stack and recommend the fix, without changing the code | 1.0 |
| [review-code](skills/review-code/SKILL.md) | Review any code against its spec and plan for bugs, scope, reuse, simplicity and security, and report ranked findings without changing it | 1.0 |

## Install

Copy a skill's folder (e.g. `skills/build-feature/`) into your agent's skills folder:

| Tool | One repo | All repos |
| --- | --- | --- |
| Most agents (shared convention) | `.agents/skills/` | - |
| Claude Code | `.claude/skills/` | `~/.claude/skills/` |
| Codex | `.agents/skills/` or `.codex/skills/` | `~/.codex/skills/` |
| Gemini CLI | `.agents/skills/` or `.gemini/skills/` | `~/.gemini/skills/` |
| GitHub Copilot | `.agents/skills/` or `.github/skills/` | `~/.copilot/skills/` |

## Conventions for new skills

1. **Name:** `verb-noun`, lowercase, words joined by hyphens, under 64 characters.
   Examples: `build-feature`, `review-code`, `fix-bug`, `write-tests`.
2. **Folder name = `name` in the frontmatter.** `skills/review-code/SKILL.md` has
   `name: review-code`.
3. **Frontmatter has only `name`, `description` and `metadata.version`.** Other
   fields aren't supported by every agent.
4. **Description:** one sentence on what it does, then "Use when ..." so agents know
   when to load it. Under ~500 characters.
5. **Body:** follow `template/SKILL.md` - Inputs, Ground rules, Steps, Output format.
   Every skill keeps the two shared rules: keep it simple, and ask when in doubt.
6. **One `SKILL.md` per skill.** Add extra files only if the skill really needs them.
7. **Versions:** bump `metadata.version` on any change (1.0 -> 1.1; 2.0 if the way
   you use it changes), and update the table above.
