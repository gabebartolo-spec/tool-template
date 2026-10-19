---
name: tool-tests
description: How to run, add and debug this tool's tests and CI - pytest markers (unit, blender, gpu), fixtures, mocking external programs and generators, headless runs that never steal focus or clash with other agents, and keeping CI under 10 minutes. Extends the general game-architecture skill (test shape) with this repo's Python layout. Use it whenever you run or add a test, touch tests.yml, or see a failure that might not be your change's fault.
---

# Tests

- **Unit** (`python -m pytest`): pure Python. Default run; CI runs exactly this plus `ruff check .`.
- **Blender** (`python -m pytest -m blender`): headless `blender -b --python ...` on tiny fixtures
  in `tests/fixtures/`. Local only; the path comes from `config.local.toml`.
- **GPU** (`python -m pytest -m gpu`): real generation. Local only, one at a time, never while the
  director is in a fullscreen game.

Rules
- Every check that guards a quality gate gets a known-bad fixture that makes it fail.
- External programs and generators sit behind one interface; unit tests use a fake.
- Seeds are pinned and written in the test; a flaky test is a seed to pin, not a rerun.
- Headless Godot runs use `--headless` and `APPDATA=<scratch>`; kill by PID only.
- CI target: under 10 minutes. Long or GPU work never goes in CI.

## Learnings

Proven findings live in `references/learnings.md`.
