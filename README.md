# New Tool (from gabebartolo-spec/tool-template)

A Python 3.12 tool starter with every project rule already in place: `CLAUDE.md`, CI (ruff +
pytest, doc caps, secret scan), PR template, status board, decision log, licence register,
handoffs and the project skills under `.claude/skills/`.

## Kickoff checklist (the first session does this, then deletes this section)

GitHub does not fill in names, so a new repo made with **Use this template** starts generic:

1. Rename: `New Tool` / `new-tool` everywhere (`grep -rn "New Tool\|new-tool" .`), the package
   `src/app` if you want, and the `tool-` skill prefix if you want a project slug.
2. Brainstorm with the director (superpowers `brainstorming` skill), write the design to
   `docs/superpowers/specs/`, and fill the `PILLAR:` and `WHAT IT DRIVES:` lines in `CLAUDE.md`.
3. Load the `project-kickoff` skill and do its section 3: branch protection (`test`,
   `doc-caps`, `gitleaks` required), the deliberately broken gate PRs (a failing test, a ruff
   error, a planted `TOOL_TEST_SECRET_` + 16 characters), the licence register.
4. The first item in `docs/STATUS.md` is assigned by the director.

## Rules

- Project rules: `CLAUDE.md` and `.claude/skills/tool-*`.
- Rules for every project: `~/.claude/CLAUDE.md` and the skills it names (live source; backed up
  to the private `gabebartolo-spec/claude-kit`). `docs/RULES_GLOBAL.md` is a snapshot of it from
  when this template was last updated; if they differ, `~/.claude` wins.

## Dev setup

```bash
python -m venv .venv
.venv/Scripts/pip install -e ".[dev]"
cp config.example.toml config.local.toml   # then edit paths
.venv/Scripts/python -m pytest
```
