# Manifest

## Topic Identity

| Field | Value |
|---|---|
| Unit code | `FAS2` |
| Unit name | Further AS 2 Applied Mathematics |
| Applied section | Section A: Mechanics 1 plus Section B: Mechanics 2 |
| Topic code | `FAS2-CM`, `FAS2-FCM` |
| Topic name | Circular motion and Further circular motion |
| Topic slug | `circular_motion` |
| Topic Pascal | `CircularMotion` |
| Topic ID | `FAS2CircularMotion` |
| Lesson file | `FAS2_circular_motion_lesson.md` |
| LO IDs | `FAS2-CM-LO001`, `FAS2-CM-LO002`, `FAS2-CM-LO003`, `FAS2-FCM-LO001` |
| Generation status | Complete |

## Phase Statuses

| Phase | Status |
|---|---|
| Phase 0 – Evidence Intake and Plan | Complete in chat |
| Phase 1 – Main Lesson Markdown | Written to `FAS2_circular_motion_lesson.md` |
| Phase 2 – Mermaid Diagrams | Written to `mermaid/` |
| Phase 3 – SVG Assets | Written to `svg/` |
| Phase 4 – TikZ Assets | Written to `tikz/` |
| Phase 5 – Widgets | Written to `widgets/` |
| Phase 6 – Manifest, Source Reference and Packaging | Complete |

## Output Layout

```text
FAS2_circular_motion_lesson.md
manifest.md
source_reference.md
mermaid/
svg/
tikz/
widgets/
```

## Asset Manifest

| Asset ID | Relative path | Status |
|---|---|---|
| `FAS2CircularMotionMermaid-001` | `mermaid/FAS2CircularMotionMermaid-001.md` | Written |
| `FAS2CircularMotionSVG-001` | `svg/FAS2CircularMotionSVG-001.svg` | Written |
| `FAS2CircularMotionSVG-002` | `svg/FAS2CircularMotionSVG-002.svg` | Written |
| `FAS2CircularMotionSVG-003` | `svg/FAS2CircularMotionSVG-003.svg` | Written |
| `FAS2CircularMotionSVG-004` | `svg/FAS2CircularMotionSVG-004.svg` | Written |
| `FAS2CircularMotionSVG-005` | `svg/FAS2CircularMotionSVG-005.svg` | Written |
| `FAS2CircularMotionSVG-006` | `svg/FAS2CircularMotionSVG-006.svg` | Written |
| `FAS2CircularMotionSVG-007` | `svg/FAS2CircularMotionSVG-007.svg` | Written |
| `FAS2CircularMotionSVG-008` | `svg/FAS2CircularMotionSVG-008.svg` | Written |
| `FAS2CircularMotionBridgeSVG-001` | `svg/FAS2CircularMotionBridgeSVG-001.svg` | Written |
| `FAS2CircularMotionTikZ-001` | `tikz/FAS2CircularMotionTikZ-001.tex` | Written |
| `FAS2CircularMotionTikZ-002` | `tikz/FAS2CircularMotionTikZ-002.tex` | Written |
| `FAS2CircularMotionWidget-001` | `widgets/FAS2CircularMotionWidget-001.html` | Written |
| `FAS2CircularMotionWidget-002` | `widgets/FAS2CircularMotionWidget-002.html` | Written |
| `FAS2CircularMotionWidget-003` | `widgets/FAS2CircularMotionWidget-003.html` | Written |

## Verification Summary

| Check | Result |
|---|---|
| Every lesson placeholder has a matching asset file | Passed |
| Every asset file has the correct ID | Passed |
| Every SVG file parses as XML | Passed |
| Every widget file has a valid HTML document structure | Passed |
| No old five-single-Markdown-file references remain | Passed |
| LO IDs are preserved exactly | Passed |
| Ordinary A-Level Maths bridge content is labelled as bridge context only | Passed |
| Off-spec material is excluded from core or marked as enrichment | Passed |
| Missing evidence is logged honestly | Passed |

## Unresolved Issues

The written files have no unresolved structural issues. Evidence limitations remain recorded in `source_reference.md`.
