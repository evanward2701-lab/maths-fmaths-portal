# Manifest – FAS2 Product-Moment Correlation Coefficient Lesson Pack

## Topic identity

| Field | Value |
|---|---|
| Course | CCEA GCE Further Mathematics |
| Unit code | `FAS2` |
| Unit title | Further AS 2 Applied Mathematics |
| Applied section | Section C: Statistics |
| Topic code | `FAS2-BIV` |
| Topic area | Bivariate distributions |
| Topic slug | `product_moment_correlation_coefficient` |
| Topic Pascal | `ProductMomentCorrelationCoefficient` |
| Topic ID | `FAS2ProductMomentCorrelationCoefficient` |
| Lesson file | `FAS2_product_moment_correlation_coefficient_lesson.md` |
| Core LO IDs | `FAS2-BIV-LO001` |
| Generation status | Complete |

## Learning outcome coverage

| LO ID | Official wording | Status |
|---|---|---|
| `FAS2-BIV-LO001` | calculate the product-moment correlation coefficient and understand its use, interpretation and limitations | Covered in lesson file, worked examples, practice, visual plan and widgets. |

## Phase statuses

| Phase | Status |
|---|---|
| Phase 0 – Evidence Intake and Build Plan | Completed in chat; distilled into lesson, manifest and source reference. |
| Phase 1 – Main Lesson Markdown | Written to `FAS2_product_moment_correlation_coefficient_lesson.md`. |
| Phase 2 – Mermaid Assets | Written to `mermaid/`. |
| Phase 3 – SVG Assets | Written to `svg/`. |
| Phase 4 – TikZ Assets | Written to `tikz/`. |
| Phase 5 – Widgets | Written to `widgets/`. |
| Phase 6 – Manifest, Source Reference and Packaging | Completed. |

## Asset manifest

| Asset ID | Type | Relative path | Source | Status |
|---|---|---|---|---|
| `FAS2ProductMomentCorrelationCoefficientMermaid-001` | Mermaid | `mermaid/FAS2ProductMomentCorrelationCoefficientMermaid-001.md` | CCEA FAS2-BIV-LO001 + transcript PMCC method | Written |
| `FAS2ProductMomentCorrelationCoefficientSVG-001` | SVG | `svg/FAS2ProductMomentCorrelationCoefficientSVG-001.svg` | Chapter 2 correlation screenshots + transcript visual explanation | Written |
| `FAS2ProductMomentCorrelationCoefficientSVG-002` | SVG | `svg/FAS2ProductMomentCorrelationCoefficientSVG-002.svg` | PMCC formula evidence from transcript and formula booklet reference | Written |
| `FAS2ProductMomentCorrelationCoefficientBridgeSVG-001` | SVG | `svg/FAS2ProductMomentCorrelationCoefficientBridgeSVG-001.svg` | Ordinary A-Level Maths bridge + Further Maths specification | Written |
| `FAS2ProductMomentCorrelationCoefficientTikZ-001` | TikZ | `tikz/FAS2ProductMomentCorrelationCoefficientTikZ-001.tex` | Transcript warning that `r` does not measure steepness | Written |
| `FAS2ProductMomentCorrelationCoefficientTikZ-002` | TikZ | `tikz/FAS2ProductMomentCorrelationCoefficientTikZ-002.tex` | AI-proposed teaching enhancement based on PMCC limitations | Written |
| `FAS2ProductMomentCorrelationCoefficientWidget-001` | HTML widget | `widgets/FAS2ProductMomentCorrelationCoefficientWidget-001.html` | AI-proposed teaching enhancement based on lesson evidence | Written |
| `FAS2ProductMomentCorrelationCoefficientWidget-002` | HTML widget | `widgets/FAS2ProductMomentCorrelationCoefficientWidget-002.html` | AI-proposed teaching enhancement based on transcript warnings | Written |

## Output layout

```text
FAS2_product_moment_correlation_coefficient_lesson.md
manifest.md
source_reference.md
mermaid/FAS2ProductMomentCorrelationCoefficientMermaid-001.md
svg/FAS2ProductMomentCorrelationCoefficientSVG-001.svg
svg/FAS2ProductMomentCorrelationCoefficientSVG-002.svg
svg/FAS2ProductMomentCorrelationCoefficientBridgeSVG-001.svg
tikz/FAS2ProductMomentCorrelationCoefficientTikZ-001.tex
tikz/FAS2ProductMomentCorrelationCoefficientTikZ-002.tex
widgets/FAS2ProductMomentCorrelationCoefficientWidget-001.html
widgets/FAS2ProductMomentCorrelationCoefficientWidget-002.html
```

## Verification status

| Check | Status |
|---|---|
| Every lesson placeholder has a matching asset file | Passed |
| Every asset file has the correct ID | Passed |
| Every SVG file is valid XML in structure | Passed |
| Every widget file has a valid HTML structure | Passed |
| No old five-single-Markdown-file references remain | Passed |
| LO IDs are preserved exactly | Passed |
| Ordinary A-Level Maths bridge content is labelled as bridge context only | Passed |
| Off-spec content excluded from core | Passed |

## Unresolved issues

- The screenshot PDF had no parsed text; visual claims are limited to visible/readable details.
- Some transcript numerical content was garbled; inconsistent numerical examples were flagged in the lesson rather than silently repaired.
- Spearman’s rank, tied ranks, non-parametric tests and correlation hypothesis testing remain enrichment/boundary-risk unless official CCEA evidence is supplied.
