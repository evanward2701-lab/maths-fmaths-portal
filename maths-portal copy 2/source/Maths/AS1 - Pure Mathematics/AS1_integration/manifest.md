# Manifest - AS1 Integration Lesson Pack

## Topic Identity

| Field | Value |
|---|---|
| Course | CCEA GCE Mathematics |
| Unit code | AS1 |
| Unit name | AS 1 Pure Mathematics |
| Topic code | AS1-INT |
| Topic name | Integration |
| Topic slug | integration |
| Topic Pascal | Integration |
| Topic ID | AS1Integration |
| Main lesson file | AS1_integration_lesson.md |
| Output folder | AS1_integration |
| Generation status | Complete; files physically written and zipped |

## Learning Outcomes

| LO ID | Official learning outcome | Coverage status |
|---|---|---|
| AS1-INT-LO001 | demonstrate understanding of and use indefinite integration as the reverse of differentiation | Covered |
| AS1-INT-LO002 | integrate \(x^n\) excluding \(n=-1\), and related sums, differences and constant multiples | Covered |
| AS1-INT-LO003 | evaluate definite integrals | Covered |
| AS1-INT-LO004 | use a definite integral to find the area defined by a curve and either axis | Covered |

## Phase Status

| Phase | Name | Status |
|---|---|---|
| Phase 0 | Evidence Intake and Plan | Complete |
| Phase 1 | Main Lesson Markdown | Complete |
| Phase 2 | Mermaid Diagrams | Complete |
| Phase 3 | SVG Assets | Complete |
| Phase 4 | TikZ Assets | Complete |
| Phase 5 | Interactive Widgets | Complete |
| Phase 6 | Manifest, Source Reference and Packaging | Complete |

## Asset Register

### Mermaid Assets

| Asset ID | File | Purpose | Status |
|---|---|---|---|
| AS1IntegrationMER-001 | mermaid/AS1IntegrationMER-001.md | Reverse differentiation/integration flowchart | Written |

### SVG Assets

| Asset ID | File | Purpose | Status |
|---|---|---|---|
| AS1IntegrationSVG-001 | svg/AS1IntegrationSVG-001.svg | Positive area under \(y=f(x)\) | Written |
| AS1IntegrationSVG-002 | svg/AS1IntegrationSVG-002.svg | Definite integral evaluation layout | Written |
| AS1IntegrationSVG-003 | svg/AS1IntegrationSVG-003.svg | Area between \(y=20-x-x^2\) and \(x\)-axis | Written |
| AS1IntegrationSVG-004 | svg/AS1IntegrationSVG-004.svg | Signed area and total area | Written |
| AS1IntegrationSVG-005 | svg/AS1IntegrationSVG-005.svg | Line-curve triangle subtraction | Written |
| AS1IntegrationSVG-006 | svg/AS1IntegrationSVG-006.svg | Area function and thin strip explanation | Written |

### TikZ Assets

| Asset ID | File | Companion SVG | Purpose | Status |
|---|---|---|---|---|
| AS1IntegrationTIKZ-001 | tikz/AS1IntegrationTIKZ-001.tex | AS1IntegrationSVG-001 | Positive area under curve | Written |
| AS1IntegrationTIKZ-002 | tikz/AS1IntegrationTIKZ-002.tex | AS1IntegrationSVG-002 | Definite integral layout | Written |
| AS1IntegrationTIKZ-003 | tikz/AS1IntegrationTIKZ-003.tex | AS1IntegrationSVG-003 | \(y=20-x-x^2\) finite area | Written |
| AS1IntegrationTIKZ-004 | tikz/AS1IntegrationTIKZ-004.tex | AS1IntegrationSVG-004 | Signed area | Written |
| AS1IntegrationTIKZ-005 | tikz/AS1IntegrationTIKZ-005.tex | AS1IntegrationSVG-005 | Line-curve triangle subtraction | Written |
| AS1IntegrationTIKZ-006 | tikz/AS1IntegrationTIKZ-006.tex | AS1IntegrationSVG-006 | Area function explanation | Written |

### Widget Assets

| Asset ID | File | Purpose | Status |
|---|---|---|---|
| AS1IntegrationWID-001 | widgets/AS1IntegrationWID-001.html | AS1 power-rule integration checker | Written |
| AS1IntegrationWID-002 | widgets/AS1IntegrationWID-002.html | Signed-area explorer | Written |

## Syllabus Boundary Summary

### Core AS1 Content Included

- Integration as reverse differentiation.
- Indefinite integration with \(+c\).
- Integration of \(x^n\), where \(n\ne -1\).
- Rational powers of \(x\).
- Negative powers of \(x\), excluding \(x^{-1}\).
- Sums, differences and constant multiples.
- Finding \(f(x)\) given \(f'(x)\).
- Finding the constant of integration using a point on a curve.
- Definite integrals.
- Upper limit minus lower limit.
- No \(+c\) in definite integration.
- Area under a curve and the \(x\)-axis.
- Signed area versus total area.
- Area using definite integration with triangle/trapezium support where appropriate.

### Excluded or Marked as Boundary Risk

| Item | Status | Reason |
|---|---|---|
| \(\int \frac1x\,dx\) | Excluded from core | AS1 excludes \(n=-1\); this appears later in A2 integration. |
| Surface areas and volumes | Excluded | Not AS1 Integration core. |
| MAT/STEP extension questions | Excluded from core | Useful enrichment only, not required CCEA AS1 content. |
| Direct area between two curves using top-minus-bottom | Boundary risk | Explicitly belongs to A21 Integration in the CCEA map; AS1-safe line-curve examples use triangle/trapezium support. |
| Advanced integration methods | Excluded | Substitution, parts, partial fractions and related methods are not AS1. |

## Missing Evidence Summary

| Missing or partial item | Impact | Action taken |
|---|---|---|
| Topic-specific README_module_map.md not pasted | Medium | Topic identity inferred from the CCEA specification map and project module map. |
| Topic-specific EVIDENCE_DROP_CHECKLIST.md not pasted | Medium | Generic evidence checklist used. |
| Full textbook pages not supplied | Medium | Exercise page references logged, but unprovided textbook questions not reproduced. |
| Screenshots PDF had limited parsed text | Low to medium | Used as visual support only; no uninspected visual details invented. |

## Final Generation Status

The AS1 Integration lesson pack is complete and physically written to disk. ZIP packaging complete.
