# Mermaid Asset: FA22CentreOfMassMermaid-001

| Field | Value |
|---|---|
| Asset ID | FA22CentreOfMassMermaid-001 |
| Source | CCEA `FA22-COM` specification boundary + uploaded lesson evidence |
| Related lesson section | Section 9.1 Visual Placeholder: Concept Flow |
| Used placeholder | `[VISUAL PLACEHOLDER: FA22CentreOfMassMermaid-001 | Source: CCEA FA22-COM specification boundary + uploaded lesson evidence | Insert from mermaid/FA22CentreOfMassMermaid-001.md | Purpose: Show the whole lesson flow from the centre-of-mass model to particles, laminae, composites, frameworks and suspended laminae.]` |
| Purpose | Show the whole lesson flow from the physical model to the repeated centre-of-mass calculation methods. |

```mermaid
flowchart TD
    A["Real body<br/>Many particles of matter"] --> B["Each particle has its own weight<br/>mᵢg acting vertically downward"]
    B --> C["Centre-of-mass model"]
    C --> D["Replace many weights by one resultant weight<br/>acting through G"]
    D --> E["Use moments / weighted averages"]
    E --> F["Particles on a line"]
    F --> F1["∑mᵢxᵢ = x̄∑mᵢ"]
    E --> G["Particles in a plane"]
    G --> G1["∑mᵢrᵢ = r̄∑mᵢ"]
    E --> H["Standard uniform laminae"]
    H --> H1["Use symmetry, triangle rules, sector formulae"]
    E --> I["Composite laminae"]
    I --> I1["Mass ∝ area; holes are negative mass"]
    E --> J["Rods, wires and frameworks"]
    J --> J1["Mass ∝ length; framework means wire/rod here"]
    E --> K["Suspended laminae"]
    K --> K1["G vertically below suspension point; use moments for strings"]
    D --> L["Model limitation: angular acceleration and calculus derivations excluded"]
```
