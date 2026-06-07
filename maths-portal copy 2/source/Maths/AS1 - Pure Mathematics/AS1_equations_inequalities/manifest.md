# Manifest: AS1 Equations and Inequalities

## Topic Identity

| Field | Value |
|---|---|
| Course | CCEA GCE Mathematics |
| Unit code | AS1 |
| Unit name | AS 1 Pure Mathematics |
| Topic code | AS1-AF |
| Official topic area | Algebra and functions |
| Topic name | Equations and Inequalities |
| Topic slug | equations_inequalities |
| Topic Pascal | EquationsInequalities |
| Topic ID | AS1EquationsInequalities |
| Main lesson file | AS1_equations_inequalities_lesson.md |
| Generated in chat | Yes |
| Files written to disk | Yes |
| Package status | Written and zipped |

## Learning Outcome IDs

### Core LO IDs

| LO ID | Status | Coverage |
|---|---|---|
| AS1-AF-LO004 | Covered | Discriminant used to determine two, one or no real intersections. |
| AS1-AF-LO007 | Covered | Simultaneous equations in two variables by elimination and substitution, including one linear and one quadratic equation. |
| AS1-AF-LO009 | Covered | Linear and quadratic inequalities in one variable, graphical interpretation, brackets and fractional/reducible inequalities. |
| AS1-AF-LO014 | Covered | Algebraic solutions interpreted graphically. |
| AS1-AF-LO015 | Covered | Intersection points of graphs used to solve equations. |

### Supporting LO IDs

| LO ID | Status | Coverage |
|---|---|---|
| AS1-AF-LO003 | Supporting | Quadratic functions and graphs used in intersection and inequality reasoning. |
| AS1-AF-LO006 | Supporting | Quadratic solving used after substitution and when solving inequalities. |
| AS1-AF-LO012 | Supporting | Sketching simple curves used for inequality and intersection interpretation. |

### Logged gap

| LO ID | Status | Reason |
|---|---|---|
| AS1-AF-LO008 | Not covered | The supplied lesson evidence did not include solving simultaneous equations in three variables. |

## Phase Status

| Phase | Name | Status | Output |
|---|---|---|---|
| Phase 0 | Evidence Intake and Plan | Complete | Evidence summary, metadata, LO mapping, boundary log |
| Phase 1 | Main Lesson Markdown | Complete | `AS1_equations_inequalities_lesson.md` |
| Phase 2 | Mermaid Diagrams | Complete | 5 Mermaid files |
| Phase 3 | SVG Assets | Complete | 6 SVG files |
| Phase 4 | TikZ Assets | Complete | 2 TikZ files |
| Phase 5 | Widgets | Complete | 3 HTML widgets |
| Phase 6 | Manifest, Source Reference and Packaging | Complete | `manifest.md`, `source_reference.md`, ZIP package |

## Intended Folder Structure

```text
AS1_equations_inequalities/
  AS1_equations_inequalities_lesson.md
  manifest.md
  source_reference.md
  mermaid/
    AS1EquationsInequalitiesMermaid-001.md
    AS1EquationsInequalitiesMermaid-002.md
    AS1EquationsInequalitiesMermaid-003.md
    AS1EquationsInequalitiesMermaid-004.md
    AS1EquationsInequalitiesMermaid-005.md
  svg/
    AS1EquationsInequalitiesSVG-001.svg
    AS1EquationsInequalitiesSVG-002.svg
    AS1EquationsInequalitiesSVG-003.svg
    AS1EquationsInequalitiesSVG-004.svg
    AS1EquationsInequalitiesSVG-005.svg
    AS1EquationsInequalitiesSVG-006.svg
  tikz/
    AS1EquationsInequalitiesTikZ-001.tex
    AS1EquationsInequalitiesTikZ-002.tex
  widgets/
    AS1EquationsInequalitiesWidget-001.html
    AS1EquationsInequalitiesWidget-002.html
    AS1EquationsInequalitiesWidget-003.html
```

## Asset Register

### Mermaid assets

| Asset ID | File | Purpose |
|---|---|---|
| AS1EquationsInequalitiesMermaid-001 | mermaid/AS1EquationsInequalitiesMermaid-001.md | Method-choice flowchart for equations and inequalities. |
| AS1EquationsInequalitiesMermaid-002 | mermaid/AS1EquationsInequalitiesMermaid-002.md | Classifies possible solution-set sizes. |
| AS1EquationsInequalitiesMermaid-003 | mermaid/AS1EquationsInequalitiesMermaid-003.md | Shows discriminant cases for graph intersections. |
| AS1EquationsInequalitiesMermaid-004 | mermaid/AS1EquationsInequalitiesMermaid-004.md | Workflow for linear and quadratic inequalities. |
| AS1EquationsInequalitiesMermaid-005 | mermaid/AS1EquationsInequalitiesMermaid-005.md | Safe workflow for fractional inequality \(\frac6x>2\). |

### SVG assets

| Asset ID | File | Purpose |
|---|---|---|
| AS1EquationsInequalitiesSVG-001 | svg/AS1EquationsInequalitiesSVG-001.svg | Solution set types. |
| AS1EquationsInequalitiesSVG-002 | svg/AS1EquationsInequalitiesSVG-002.svg | Simultaneous equations as graph intersections. |
| AS1EquationsInequalitiesSVG-003 | svg/AS1EquationsInequalitiesSVG-003.svg | Discriminant cases: two, one or no intersections. |
| AS1EquationsInequalitiesSVG-004 | svg/AS1EquationsInequalitiesSVG-004.svg | Sign regions for \(y=(x+5)(x-3)\). |
| AS1EquationsInequalitiesSVG-005 | svg/AS1EquationsInequalitiesSVG-005.svg | Safe fractional inequality method and sign chart. |
| AS1EquationsInequalitiesSVG-006 | svg/AS1EquationsInequalitiesSVG-006.svg | Optional enrichment: two-variable inequality region. |

### TikZ assets

| Asset ID | File | Purpose |
|---|---|---|
| AS1EquationsInequalitiesTikZ-001 | tikz/AS1EquationsInequalitiesTikZ-001.tex | Clean exam-style line-parabola intersection graph. |
| AS1EquationsInequalitiesTikZ-002 | tikz/AS1EquationsInequalitiesTikZ-002.tex | Clean quadratic inequality graph and number-line solution diagram. |

### Widget assets

| Asset ID | File | Purpose |
|---|---|---|
| AS1EquationsInequalitiesWidget-001 | widgets/AS1EquationsInequalitiesWidget-001.html | Discriminant explorer for \(ax^2+bx+c=0\). |
| AS1EquationsInequalitiesWidget-002 | widgets/AS1EquationsInequalitiesWidget-002.html | Quadratic inequality interval explorer. |
| AS1EquationsInequalitiesWidget-003 | widgets/AS1EquationsInequalitiesWidget-003.html | Set-builder notation translator. |

## Placeholder Consistency Check

All Phase 1 placeholders now have matching drafted files in the package.

## Syllabus Boundary Summary

### Included as core

- Solution sets and set-builder notation.
- Simultaneous equations in two variables by elimination.
- Simultaneous equations in two variables by substitution.
- One linear and one quadratic simultaneous system.
- Graph intersections as solutions.
- Discriminant use for two, one or no intersections.
- Linear inequalities in one variable.
- Quadratic inequalities in one variable.
- Inequalities with brackets.
- Fractional inequalities only where reducible to linear or quadratic inequalities.
- Graphical interpretation of inequalities.

### Excluded from core or marked optional

| Item | Decision |
|---|---|
| STEP 2010 Q1 extension | Excluded from core. Optional enrichment only. |
| MAT 2012 1G extension | Excluded from core. Optional enrichment only. |
| Edexcel C1 exercise references | Not used as core CCEA practice. |
| Two-variable inequality regions | Optional enrichment only. |
| Full rational inequality theory | Excluded. Only reducible forms are treated. |
| Simultaneous equations in three variables | Logged gap due missing lesson evidence. |

## Generation Status

Status: Complete. Files written and zipped.
