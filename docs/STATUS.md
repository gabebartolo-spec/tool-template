# Status board

Cap: 150 lines. Edited only by the lead, in a board PR after each merge, from the merged PR's
"Board and log" section. History rolls to `docs/archive/status_<month>.md`.

## Phase
Current phase: **0 — Foundations** (gate: CI green on main and proven to reject a failing test,
a lint error and a planted secret). Gate signer: the lead.

## Agents

| Agent | State | Item | Branch / PR | Since |
|-------|-------|------|-------------|-------|
| Lead | available | kickoff checklist (README) | — | YYYY-MM-DD |

States: working · running a check · awaiting director · blocked · available.

## Assigned items (in order; an item starts only when it is listed here)

### Phase 0
1. Lead: the README kickoff checklist.
2. Lead: prove the gate with throwaway PRs (failing test, ruff error, planted
   `TOOL_TEST_SECRET_` + 16 characters), each closed unmerged after it goes red. Record run ids
   in `docs/audits/kickoff_gate.md`.
