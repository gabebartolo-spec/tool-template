# New Tool: working rules for every Claude Code session

Python 3.12 tool. WHAT IT DRIVES: fill in at kickoff (e.g. headless Blender, Godot export
checks, local generators). Read this file, then your handoff (`agent-handoffs/<role>.md`), then
the design (`docs/superpowers/specs/<date>-<topic>-design.md`, the source of truth for what the
tool is), then `docs/STATUS.md` "Assigned items". The general rules every project shares live in
`~/.claude/CLAUDE.md` and the skills it names (`ask-the-director`, `ai-game-dev-playbook`,
`github-hygiene`, `game-architecture`, `art-qa-critic`, `ai-slop-art`); this file holds only
what is true for this tool.

## Always loaded

Claude Code imports these core documents in full at every session start (the `@` lines below),
so they are part of this file: read them as rules, never skim or skip them.

@docs/ROADMAP.md
@docs/STATUS.md
At kickoff, add the design spec here as an import line too (`@docs/superpowers/specs/<date>-<topic>-design.md`).

## Philosophy (permanent)

**Designed by a person, developed with AI, never designed by AI.** The director supplies vision,
taste and final judgement. Agents supply execution, evidence and honest pushback.

- **PILLAR: write one sentence every feature must serve, with the director, at kickoff.** A
  feature that does not serve it is cut, even if it works.
- **A roadmap item is context, not authorisation.** Start only what `docs/STATUS.md` lists as
  assigned. When an assigned task is done: stop, report with evidence, recommend the next step, wait.
- **Simplest viable option first.** Fewer screens, fewer settings, fewer files.
- **Challenge the director** when a request conflicts with the design or these rules. One
  paragraph, a better option, then do what the director decides.
- **Ask, don't ponder.** His calls are asked at once, the `ask-the-director` way, with labelled
  images for anything visual and a clip for anything that moves.

## Hard rules

1. **No spend** without the director's written yes in `docs/DECISIONS.md`.
2. **Licences.** Every model, library or asset allows commercial use and is listed in
   `docs/LICENCES.md` before use. Non-commercial or research-only is banned.
3. **Nothing private in git.** No keys, tokens, personal paths or model weights. Machine paths
   live in the gitignored `config.local.toml` (template: `config.example.toml`).
4. **Never modify installs other tools own** (e.g. the Stability Matrix ComfyUI). What this tool
   needs goes in its own env (`.venv/`, gitignored).
5. **Proof before "done".** A change is done when its evidence is in the PR body.
6. **Change method after two failed fixes.** Gather different evidence and rethink.

## Machine rules (shared PC, one 12 GB GPU)

- One GPU job at a time (ComfyUI, Blender bakes/renders, local models). Never slow down, defer or
  pause work for what the director is doing on the PC; just never pop up a window or steal focus.
- Blender always `blender -b` (never a window). Godot only headless, isolated `APPDATA=<scratch>`.
  Never kill a process by image name; kill your own PID.
- Worktrees: `git worktree add -b claude/<topic> ../new-tool-wt/<topic> origin/main`. Remove the
  worktree when the PR merges. More than four live is a violation.
- Only the lead edits `docs/STATUS.md` and `docs/DECISIONS.md`, in a docs-only board PR after
  each merge; every other PR states its board and log changes in its body.
- Stage files by name, never `git add -A`; never `git stash`.

## Tests and CI

`python -m pytest` (unit), `python -m pytest -m blender` / `-m gpu` (local only), `ruff check .`.
CI (`tests.yml`, job `test`) runs ruff and the unit suite; no GPU in CI. Keep CI under 10
minutes. See the `tool-tests` skill.

## Sessions and context

- Fresh session at every task boundary; write `agent-handoffs/<role>.md` first (120-line cap,
  rewritten, never appended). Hand off at about 200k context; wait in the background only.
- End every turn with your state: working, running a check, awaiting director, blocked, available.

## Skills

Project skills live in `.claude/skills/tool-*` and extend the general ones; each has a
`references/learnings.md` with the evidence bar from `~/.claude/CLAUDE.md`. General lessons go
to the general skill's log so every project benefits.
