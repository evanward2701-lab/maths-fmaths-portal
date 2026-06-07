# Manifest - FAS1 Conic Sections 1 Lesson Pack

## Topic Identity

| Field | Value |
|---|---|
| `unit_code` | `FAS1` |
| Unit title | Further AS 1 Pure Mathematics |
| `topic_code` | `FAS1-CONICS1` |
| Topic-code status | Assumed internal topic code under user override |
| `topic_name` | Conic Sections 1 |
| `topic_slug` | `conic_sections_1` |
| `topic_pascal` | `ConicSections1` |
| `topic_id` | `FAS1ConicSections1` |
| `lesson_file` | `FAS1_conic_sections_1_lesson.md` |
| Applied section | Pure |
| Official CCEA LO status | No official CCEA LO IDs available in project sources |
| Internal assumed LO IDs | `FAS1-CONICS1-LO001` to `FAS1-CONICS1-LO010` |
| Generation status | Complete |
| Output root | `FAS1_conic_sections_1_lesson_pack/` |

## LO IDs

- `FAS1-CONICS1-LO001`
- `FAS1-CONICS1-LO002`
- `FAS1-CONICS1-LO003`
- `FAS1-CONICS1-LO004`
- `FAS1-CONICS1-LO005`
- `FAS1-CONICS1-LO006`
- `FAS1-CONICS1-LO007`
- `FAS1-CONICS1-LO008`
- `FAS1-CONICS1-LO009`
- `FAS1-CONICS1-LO010`

## Phase Statuses

| Phase | Status |
|---|---|
| Phase 0 - Evidence Intake and Build Plan | Complete in chat |
| Phase 1 - Main Lesson Markdown | Complete and written |
| Phase 2 - Mermaid Assets | Complete and written |
| Phase 3 - SVG Assets | Complete and written |
| Phase 4 - TikZ Assets | Complete and written |
| Phase 5 - Interactive Widgets | Complete and written |
| Phase 6 - Manifest, Source Reference and Packaging | Complete and written |

## Output Layout

```text
FAS1_conic_sections_1_lesson_pack/
├── FAS1_conic_sections_1_lesson.md
├── manifest.md
├── source_reference.md
├── mermaid/
├── svg/
├── tikz/
└── widgets/
```

## Asset Manifest

| Asset ID | Type | Relative path | Status |
|---|---|---|---|
| `FAS1ConicSections1Mermaid-001` | Mermaid | `mermaid/FAS1ConicSections1Mermaid-001.md` | Written |
| `FAS1ConicSections1Mermaid-002` | Mermaid | `mermaid/FAS1ConicSections1Mermaid-002.md` | Written |
| `FAS1ConicSections1SVG-001` | SVG | `svg/FAS1ConicSections1SVG-001.svg` | Written |
| `FAS1ConicSections1SVG-002` | SVG | `svg/FAS1ConicSections1SVG-002.svg` | Written |
| `FAS1ConicSections1SVG-003` | SVG | `svg/FAS1ConicSections1SVG-003.svg` | Written |
| `FAS1ConicSections1SVG-004` | SVG | `svg/FAS1ConicSections1SVG-004.svg` | Written |
| `FAS1ConicSections1BridgeSVG-001` | SVG | `svg/FAS1ConicSections1BridgeSVG-001.svg` | Written |
| `FAS1ConicSections1TikZ-001` | TikZ | `tikz/FAS1ConicSections1TikZ-001.tex` | Written |
| `FAS1ConicSections1TikZ-002` | TikZ | `tikz/FAS1ConicSections1TikZ-002.tex` | Written |
| `FAS1ConicSections1TikZ-003` | TikZ | `tikz/FAS1ConicSections1TikZ-003.tex` | Written |
| `FAS1ConicSections1TikZ-004` | TikZ | `tikz/FAS1ConicSections1TikZ-004.tex` | Written |
| `FAS1ConicSections1Widget-001` | HTML widget | `widgets/FAS1ConicSections1Widget-001.html` | Written |
| `FAS1ConicSections1Widget-002` | HTML widget | `widgets/FAS1ConicSections1Widget-002.html` | Written |
| `FAS1ConicSections1Widget-003` | HTML widget | `widgets/FAS1ConicSections1Widget-003.html` | Written |
| `FAS1ConicSections1Widget-004` | HTML widget | `widgets/FAS1ConicSections1Widget-004.html` | Written |
| `FAS1ConicSections1Widget-005` | HTML widget | `widgets/FAS1ConicSections1Widget-005.html` | Written |

## Verification Summary

| Check | Result |
|---|---|
| Every lesson placeholder has a matching asset file | Passed |
| Every asset file has the correct ID | Passed |
| Every SVG parses as XML | Passed |
| Every widget has HTML, head and body structure | Passed |
| No old five-single-Markdown-file references remain | Passed |
| LO IDs are preserved exactly | Passed |
| Ordinary A-Level Maths bridge content is labelled as bridge context only | Passed |
| Off-spec material is excluded from core or marked as preview/enrichment/assumed-extension content | Passed |

## Unresolved Issues

| Issue | Status |
|---|---|
| Official CCEA conics topic code | Unavailable in project sources; internal assumed code used by user instruction |
| Official CCEA conics LO IDs | Unavailable in project sources; internal assumed IDs used by user instruction |
| CCEA conics past-paper wording | Not supplied |
| Full Pearson textbook exercise pages | Not supplied |
| Full searchable screenshot PDF text | Not available; screenshot PDF is image-only |
| Original Desmos activity files | Not supplied |

## Final Quality Check Summary

- Unit prefix and topic identity are consistently recorded as `FAS1`, `FAS1-CONICS1`, `conic_sections_1`, `ConicSections1`, and `FAS1ConicSections1`.
- LO IDs are preserved as the internal assumed IDs `FAS1-CONICS1-LO001` to `FAS1-CONICS1-LO010`.
- On-spec coverage is interpreted under the user override that Conic Sections 1 should be completed as if included.
- Off-spec/preview material such as full ellipse theory, general hyperbola theory and full eccentricity theory is marked as preview/enrichment rather than developed as core Conics 1 method.
- Every placeholder in the lesson points to a matching split asset file.
- Manifest and source reference are written.
