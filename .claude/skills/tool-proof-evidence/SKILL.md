---
name: tool-proof-evidence
description: How to prove a change to this tool actually works before calling it done - the evidence that fits each kind of change, real clicks in the UI instead of handler calls, proving the output the tool really produced, new checks shown failing first, and the Not exercised line. Extends the general afl-proof-evidence ideas and art-qa-critic. Use it when finishing any feature or fix, writing a PR's Evidence section, adding a test, or about to say something works or looks right.
---

# Proof before "done"

"It works" is not evidence; what the tool produced is. The usual false passes: a test that calls
an endpoint while the page's button is broken, a check run only on input that already passed,
a render of the wrong file, a QA step that never saw a bad input.

## Pick evidence that fits the change

| Change | Evidence that counts |
|---|---|
| Pure Python | unit tests, each new check shown failing on a known-bad input first |
| External tool script (Blender, Godot, ComfyUI) | the `-m blender` / `-m gpu` test on a tiny fixture; numbers before/after |
| Output file (model, image, export) | open it in the consuming program (e.g. headless Godot import) with no errors |
| Generated art | five views untextured and textured, anatomy count, `art-qa-critic` + `ai-slop-art` |
| Motion | a short clip, checked by the motion critic |
| UI flow | a real click at the control's position (browser automation), then the result on screen |

## A look is the director's

Validators and green tests never approve a look. The lead's own check first (2x crops), then
the director from labelled images (a clip for motion).

## Write it down

**Evidence:** tests with counts, fixture, seed, capture or clip by path. **Not exercised:** what
you did not cover. After two similar failed fixes, change the evidence before another fix.

## Learnings

Proven findings for this project live in `references/learnings.md`; general ones go to the
general skill's log.
