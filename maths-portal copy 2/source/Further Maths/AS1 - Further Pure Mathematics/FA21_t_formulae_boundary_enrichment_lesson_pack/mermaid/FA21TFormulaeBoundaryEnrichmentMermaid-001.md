# FA21TFormulaeBoundaryEnrichmentMermaid-001

## Asset metadata

| Field | Value |
|---|---|
| Asset ID | `FA21TFormulaeBoundaryEnrichmentMermaid-001` |
| Asset type | Mermaid flowchart |
| Topic ID | `FA21TFormulaeBoundaryEnrichment` |
| Related lesson file | `FA21_t_formulae_boundary_enrichment_lesson.md` |
| Related lesson section | Section 9: Visual Asset Integration |
| Source | Supplied FP1 t-formulae PDF, screenshot derivation pages, teacher transcript |
| CCEA status | Not confirmed CCEA core; enrichment only |
| Purpose | Show how ordinary double-angle trigonometry grows into the t-formulae. |

```mermaid
flowchart TD
    Start["Ordinary A-Level trig bridge<br/>Tangent double-angle formula"] --> TDA["tan 2A = 2 tan A / (1 - tan^2 A)"]
    TDA --> HalfAngle["Set A = θ / 2<br/>so 2A = θ"]
    HalfAngle --> Substitute["Define t = tan(θ / 2)"]
    Substitute --> TanFormula["tan θ = 2t / (1 - t^2)"]
    TanFormula --> TriangleInterpretation["Read tan θ as opposite / adjacent"]
    TriangleInterpretation --> OppAdj["opposite = 2t<br/>adjacent = 1 - t^2"]
    OppAdj --> Pythagoras["Use Pythagoras:<br/>h^2 = (2t)^2 + (1 - t^2)^2"]
    Pythagoras --> Expand["h^2 = 4t^2 + 1 - 2t^2 + t^4"]
    Expand --> Square["h^2 = t^4 + 2t^2 + 1<br/>= (1 + t^2)^2"]
    Square --> Hypotenuse["h = 1 + t^2<br/>for real t"]
    Hypotenuse --> SineFormula["sin θ = opposite / hypotenuse<br/>sin θ = 2t / (1 + t^2)"]
    Hypotenuse --> CosFormula["cos θ = adjacent / hypotenuse<br/>cos θ = (1 - t^2) / (1 + t^2)"]
    TanFormula --> FormulaBox["The t-formulae:<br/>sin θ = 2t / (1 + t^2)<br/>cos θ = (1 - t^2) / (1 + t^2)<br/>tan θ = 2t / (1 - t^2)"]
    SineFormula --> FormulaBox
    CosFormula --> FormulaBox
    FormulaBox --> Boundary["Boundary note:<br/>optional enrichment, not confirmed CCEA core"]
```
