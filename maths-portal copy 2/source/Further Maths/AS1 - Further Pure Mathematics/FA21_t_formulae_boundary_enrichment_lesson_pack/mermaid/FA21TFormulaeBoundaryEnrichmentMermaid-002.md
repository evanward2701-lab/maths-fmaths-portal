# FA21TFormulaeBoundaryEnrichmentMermaid-002

## Asset metadata

| Field | Value |
|---|---|
| Asset ID | `FA21TFormulaeBoundaryEnrichmentMermaid-002` |
| Asset type | Mermaid flowchart |
| Topic ID | `FA21TFormulaeBoundaryEnrichment` |
| Related lesson file | `FA21_t_formulae_boundary_enrichment_lesson.md` |
| Related lesson section | Section 9: Visual Asset Integration |
| Source | Supplied FP1 t-formulae PDF and teacher transcript |
| CCEA status | Not confirmed CCEA core; enrichment only |
| Purpose | Show the complete method for solving trigonometric equations using t-formulae. |

```mermaid
flowchart TD
    Start["Start with a trig equation<br/>for example: 2 sin θ - 3 cos θ = 1"] --> Boundary["Boundary note:<br/>t-formulae are enrichment here,<br/>not confirmed CCEA core"]
    Boundary --> ChooseAngle["Identify the angle ladder<br/>θ / 2 → θ<br/>or θ → 2θ<br/>or x → 2x"]
    ChooseAngle --> Substitution{"Which doubled angle is needed?"}
    Substitution -->|Need θ from θ / 2| LetHalf["Let t = tan(θ / 2)"]
    Substitution -->|Need 2θ from θ| LetTheta["Let t = tan θ"]
    Substitution -->|Need 2x from x| LetX["Let t = tan x"]
    LetHalf --> FormulaTheta["Use:<br/>sin θ = 2t / (1 + t^2)<br/>cos θ = (1 - t^2) / (1 + t^2)<br/>tan θ = 2t / (1 - t^2)"]
    LetTheta --> Formula2Theta["Use:<br/>sin 2θ = 2t / (1 + t^2)<br/>cos 2θ = (1 - t^2) / (1 + t^2)<br/>tan 2θ = 2t / (1 - t^2)"]
    LetX --> Formula2X["Use:<br/>sin 2x = 2t / (1 + t^2)<br/>cos 2x = (1 - t^2) / (1 + t^2)<br/>tan 2x = 2t / (1 - t^2)"]
    FormulaTheta --> Algebra["Substitute into the equation<br/>and collect terms in t"]
    Formula2Theta --> Algebra
    Formula2X --> Algebra
    Algebra --> DenomCheck["Before clearing denominators,<br/>record restrictions:<br/>1 + t^2 ≠ 0 for real t<br/>1 - t^2 ≠ 0 means t ≠ ±1<br/>2t ≠ 0 means t ≠ 0"]
    DenomCheck --> Clear["Clear denominators carefully"]
    Clear --> Poly["Obtain an algebraic equation<br/>often quadratic or quartic in t"]
    Poly --> SolveT["Solve for t<br/>factorise or use quadratic formula"]
    SolveT --> Reject["Reject impossible or excluded t-values"]
    Reject --> Undo["Undo the substitution"]
    Undo --> HalfCase{"Was t = tan(θ / 2) used?"}
    HalfCase -->|Yes| HalfRange["Convert original range:<br/>0 ≤ θ ≤ 2π<br/>becomes<br/>0 ≤ θ / 2 ≤ π"]
    HalfCase -->|No| DirectRange["Use the range for the actual angle<br/>for example θ or x"]
    HalfRange --> SolveHalf["Solve tan(θ / 2) = t<br/>inside the half-angle range"]
    SolveHalf --> Double["Double the half-angle solutions<br/>to get θ"]
    DirectRange --> SolveDirect["Solve tan(angle) = t<br/>inside the given range"]
    Double --> FinalCheck["Check final answers in original equation<br/>and original range"]
    SolveDirect --> FinalCheck
    FinalCheck --> Answer["Write final answers<br/>in the original variable"]
```
