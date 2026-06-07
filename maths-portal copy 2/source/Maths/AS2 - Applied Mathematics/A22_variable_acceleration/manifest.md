# manifest.md

## Lesson Pack Manifest

### Topic Identity

| Field | Value |
|---|---|
| Course | CCEA GCE Mathematics |
| Unit code | A22 |
| Unit name | A2 2 Applied Mathematics |
| Applied section | Mechanics |
| Topic code | A22-KIN |
| Topic name | Kinematics |
| Lesson title | Variable Acceleration |
| topic_slug | variable_acceleration |
| topic_pascal | VariableAcceleration |
| topic_id | A22VariableAcceleration |
| lesson_file | A22_variable_acceleration_lesson.md |
| Core LO IDs | A22-KIN-LO001 |
| Related LO IDs excluded from core | A22-KIN-LO002, A22-KIN-LO003, A22-KIN-LO004 |

---

## Specification Alignment

| LO ID | Status | Coverage |
|---|---|---|
| A22-KIN-LO001 | Covered | Straight-line calculus kinematics: \(v=\frac{ds}{dt}\), \(a=\frac{dv}{dt}=\frac{d^2s}{dt^2}\), \(s=\int v\,dt\), \(v=\int a\,dt\). |
| A22-KIN-LO002 | Excluded | Two-dimensional vector calculus kinematics belongs in a separate lesson. |
| A22-KIN-LO003 | Excluded | Motion under gravity in two dimensions belongs in a separate lesson. |
| A22-KIN-LO004 | Excluded | Projectile motion belongs in a separate lesson. |

---

## Phase Status

| Phase | Status | Output |
|---|---|---|
| Phase 0 | Complete | Evidence intake, metadata, boundaries, missing evidence and off-spec logs. |
| Phase 1 | Complete | Main lesson Markdown. |
| Phase 2 | Complete | Mermaid diagrams. |
| Phase 3 | Complete | SVG assets. |
| Phase 4 | Complete | TikZ assets. |
| Phase 5 | Complete | Interactive widgets. |
| Phase 6 | Complete | Manifest, source reference and packaging. |
| File writing | Complete | Files written into `/mnt/data/A22_variable_acceleration/`. |
| Packaging | Complete | ZIP package created. |

---

## Folder Structure

```text
A22_variable_acceleration/
  A22_variable_acceleration_lesson.md
  manifest.md
  source_reference.md
  mermaid/
    A22VariableAccelerationMermaid-001.md
    A22VariableAccelerationMermaid-002.md
    A22VariableAccelerationMermaid-003.md
    A22VariableAccelerationMermaid-004.md
    A22VariableAccelerationMermaid-005.md
    A22VariableAccelerationMermaid-006.md
    A22VariableAccelerationMermaid-007.md
  svg/
    A22VariableAccelerationSVG-001.svg
    A22VariableAccelerationSVG-002.svg
    A22VariableAccelerationSVG-003.svg
    A22VariableAccelerationSVG-004.svg
    A22VariableAccelerationSVG-005.svg
  tikz/
    A22VariableAccelerationTikZ-001.tex
    A22VariableAccelerationTikZ-002.tex
    A22VariableAccelerationTikZ-003.tex
    A22VariableAccelerationTikZ-004.tex
    A22VariableAccelerationTikZ-005.tex
    A22VariableAccelerationTikZ-006.tex
  widgets/
    A22VariableAccelerationWidget-001.html
    A22VariableAccelerationWidget-002.html
    A22VariableAccelerationWidget-003.html
```

---

## Asset Manifest

### Main Lesson File

| File | Status | Purpose |
|---|---|---|
| `A22_variable_acceleration_lesson.md` | Complete | Full Markdown lesson for A22 Variable Acceleration. |

### Mermaid Assets

| File | Status | Purpose |
|---|---|---|
| `mermaid/A22VariableAccelerationMermaid-001.md` | Complete | \(s\), \(v\), \(a\) differentiation/integration chain. |
| `mermaid/A22VariableAccelerationMermaid-002.md` | Complete | Method-choice flowchart for given \(s(t)\), \(v(t)\), or \(a(t)\). |
| `mermaid/A22VariableAccelerationMermaid-003.md` | Complete | Constant acceleration versus variable acceleration. |
| `mermaid/A22VariableAccelerationMermaid-004.md` | Complete | Maxima/minima decision flowchart. |
| `mermaid/A22VariableAccelerationMermaid-005.md` | Complete | Displacement versus total distance travelled. |
| `mermaid/A22VariableAccelerationMermaid-006.md` | Complete | Derivation of \(v=u+at\) and \(s=ut+\frac12at^2\). |
| `mermaid/A22VariableAccelerationMermaid-007.md` | Complete | Greatest speed method using \(|v|\). |

### SVG Assets

| File | Status | Purpose |
|---|---|---|
| `svg/A22VariableAccelerationSVG-001.svg` | Complete | Constant acceleration pieces versus curved variable-acceleration graph. |
| `svg/A22VariableAccelerationSVG-002.svg` | Complete | Displacement, velocity and acceleration calculus chain. |
| `svg/A22VariableAccelerationSVG-003.svg` | Complete | Yo-yo cubic model and valid interval \(0\leq t\leq3\). |
| `svg/A22VariableAccelerationSVG-004.svg` | Complete | Positive and negative velocity-time areas. |
| `svg/A22VariableAccelerationSVG-005.svg` | Complete | Greatest speed as greatest \(|v|\). |

### TikZ Assets

| File | Status | Purpose |
|---|---|---|
| `tikz/A22VariableAccelerationTikZ-001.tex` | Complete | Calculus chain \(s\to v\to a\). |
| `tikz/A22VariableAccelerationTikZ-002.tex` | Complete | Constant versus variable acceleration graph comparison. |
| `tikz/A22VariableAccelerationTikZ-003.tex` | Complete | Signed velocity-time areas and distance travelled. |
| `tikz/A22VariableAccelerationTikZ-004.tex` | Complete | Greatest speed and \(|v|\). |
| `tikz/A22VariableAccelerationTikZ-005.tex` | Complete | Yo-yo valid interval graph. |
| `tikz/A22VariableAccelerationTikZ-006.tex` | Complete | SUVAT derivation by integration. |

### Widget Assets

| File | Status | Purpose |
|---|---|---|
| `widgets/A22VariableAccelerationWidget-001.html` | Complete | Polynomial calculus chain explorer for \(s(t)\), \(v(t)\), \(a(t)\). |
| `widgets/A22VariableAccelerationWidget-002.html` | Complete | Displacement versus total distance checker for quadratic velocity. |
| `widgets/A22VariableAccelerationWidget-003.html` | Complete | Maxima/minima method decision trainer. |

---

## Missing Evidence Log

| Missing item | Expected use | Impact | Action taken |
|---|---|---|---|
| Pasted CCEA spec extract | Direct pasted confirmation of CCEA topic boundary. | Low | Used pre-loaded CCEA specification map. |
| Topic-specific README extract | Local folder naming and topic metadata confirmation. | Low to medium | Inferred from specification map and project conventions. |
| Topic-specific evidence checklist extract | Confirmation of approved evidence items. | Low | Used project-wide evidence checklist conventions. |
| Original textbook pages | Full Pearson exercise wording. | Medium | Only used examples visible in slide evidence. |
| Fully parseable screenshots PDF text | Full screenshot annotation extraction. | Low | Used as partial visual evidence only. |
| CCEA past-paper questions | CCEA-specific exam practice. | Medium | Created CCEA-style practice without claiming it is a past paper. |

---

## Off-Spec and Boundary-Risk Log

| Evidence item | Risk | Decision |
|---|---|---|
| “Applied Year 1” label in lesson evidence | CCEA places calculus kinematics in A22, not AS2. | Treat as A22 support only. |
| Pearson/Edexcel examples | Cross-board evidence. | Use only when aligned with A22-KIN-LO001. |
| Edexcel M2 labels | Not CCEA exam evidence. | Do not describe as CCEA past paper. |
| Website/registration slide content | Not mathematical syllabus content. | Excluded. |
| Two-dimensional vector kinematics | Related A22 content but not this lesson. | Excluded for a later lesson. |
| Projectiles | Related A22 content but not this lesson. | Excluded for a later lesson. |

---

## Generation Status

All six phases have been drafted and written to files.

Final status: complete and packaged.
