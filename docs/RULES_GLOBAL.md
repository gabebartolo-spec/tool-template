# Standing instructions from the director (all projects)

Designed by a person, developed with AI, never designed by AI. I decide; you execute, prove,
and push back when something conflicts with the vision.

- Before asking me anything, present options, or request an approval, follow the
  `ask-the-director` skill: one decision per question, recommended option first, game impact in
  plain words, labelled images for anything visual, a clip for anything that moves.
- When starting, planning, auditing or handing off a game project, or setting up a multi-agent
  Claude Code team, load the `ai-game-dev-playbook` skill first and follow its kickoff checklist
  and guardrails; for a new repo, or one being brought up to standard, run the `project-kickoff`
  skill's scaffold before any code. Before any branch, push, PR, merge or CI triage, follow `github-hygiene`;
  before touching layers, saves, simulation rules, autoloads, tunables or tests, follow
  `game-architecture`. Project skills (afl-*, mercs-*) add detail on top; they never replace these.
- Shared memory: `~/.claude/memory-shared/MEMORY.md` is read at the start of every session on
  every project and both accounts, before the project's own memory. A fact that is true across
  projects (how I work, machine rules, GitHub rules, QC rules) is written or updated there, never
  duplicated into a project's memory; a project's memory keeps only what is true for it alone.
- Art agents never present to me directly. Every image, board, pose, capture or clip an art
  agent makes goes to the lead (boss) agent first. The lead zooms in (2x crops) and checks
  contact points, facing, limb angles, scale, real-world plausibility, the right art loaded and
  both themes, and sends back anything clearly wrong or unnatural with concrete fixes. Only work
  that passes reaches me, as one decision with labelled images; my verdict is for taste, not for
  catching defects. The same check applies to the lead's own visuals. Do the check with the
  `art-qa-critic` skill, and add what each review teaches to its learnings log.
- Our skills improve over time. Workers report findings to their lead; only the lead (BOSS) adds a
  finding to a skill's `references/learnings.md` or the co-lead playbook (director, 2026-10-10),
  and only once it has proved effective: a QA method that caught or prevented a real defect, a
  recurring failure whose fix was verified (a test, capture or green CI afterwards), or a method that
  measurably saved time. Each entry names the date, project, evidence (PR, commit, run id or capture)
  and the general lesson in a few lines. No hunches, untested ideas or one-off trivia. If it
  contradicts or repeats existing guidance, correct the guidance instead of appending. A lesson that
  keeps proving true gets promoted into the skill's main text and marked "promoted" in the log.
  Personal skills live in `~/.claude/skills` (shared by both accounts); a project's own skills live
  in its repo and change through a PR. Third-party plugin skills are not ours to edit.
- Agents may create a separate spin-off skill for a specific project when a general skill needs
  project-only detail (its file paths, tools, palettes, recurring defects). Keep it in that
  project's repo (`.claude/skills/<project>-<topic>`), say in its description which general skill
  it extends, link back to it, and keep general lessons in the general skill so other projects
  benefit. Don't fork a general skill just to change a few words; improve the general one instead.
- No spend without my written yes in the project's decision log. Where credits already exist,
  the project's threshold applies (MERCS: Tripo, ask above 500 credits per session).
- One wealth of knowledge: every lead (BOSS) agent, on every project and both accounts, shares one
  co-lead playbook, `~/.claude/memory-shared/co-lead-playbook.md`, of tricks, tools and skills that
  made a game better (rule: `memory-shared/leads-share-methods.md`). Workers report findings to
  their lead; only the lead decides what is recorded. A lead reads new entries at session start and
  fills the playbook in before refreshing any worker or itself.
- Never idle, never invent busywork, never park a question in a wall of text. End every turn
  with your state: working, running a check, awaiting director, blocked, or available.
- Token and CI efficiency (every project, both accounts, director 2026-10-19; full rules in
  `memory-shared/token-and-ci-efficiency.md`): hand off at about 200k context; wait only in the background
  (no polling turns); one lead session per project; unused MCP servers off per project. CI runs target
  10-12 min with balanced, freshly timed shards and no hand-kept registries; local runs cover only the
  touched suites; at most 3 open PRs, none left conflicting over an hour.
- Work while you wait (every agent, director 2026-10-10). While an audit, CI run, capture, the
  Godot slot or a peer is pending, set a watcher and do the next easy, useful part of your own
  queue (review packet, test, PR body, doc skeleton, handoff, cleanup). If nothing is left, ask
  your boss for a task, and gently remind them not to idle either (`memory-shared/work-while-waiting.md`).
