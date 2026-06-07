# Mermaid Asset: FA22CentreOfMassBridgeMermaid-001

| Field | Value |
|---|---|
| Asset ID | FA22CentreOfMassBridgeMermaid-001 |
| Source | Ordinary A-Level Maths bridge + Further Maths specification |
| Related lesson section | Section 9.2 Visual Placeholder: Ordinary Maths Bridge Map |
| Used placeholder | `[VISUAL PLACEHOLDER: FA22CentreOfMassBridgeMermaid-001 | Source: Ordinary A-Level Maths bridge + Further Maths specification | Insert from mermaid/FA22CentreOfMassBridgeMermaid-001.md | Purpose: Compare prior ordinary Maths method with Further Maths extension.]` |
| Purpose | Compare ordinary A-Level Mechanics and Vectors with Further Maths centre-of-mass methods. |

```mermaid
flowchart LR
    subgraph Ordinary["Ordinary A-Level Maths bridge context only"]
        A1["Weight W = mg"]
        A2["Moments = force × perpendicular distance"]
        A3["Static equilibrium"]
        A4["Position vectors"]
        A5["Coordinate geometry and trigonometry"]
    end
    subgraph Further["FA22 Centre of Mass"]
        B1["Replace many weights by one resultant through G"]
        B2["∑mᵢxᵢ = x̄∑mᵢ"]
        B3["∑mᵢrᵢ = r̄∑mᵢ"]
        B4["Area/length as mass ratio"]
        B5["G vertically below pivot"]
        B6["Two-string moments"]
    end
    subgraph Risks["Warnings"]
        C1["No ordinary average unless justified"]
        C2["Keep negative coordinates"]
        C3["Lamina ≠ wire/framework"]
        C4["Radians for arc/sector formulae"]
        C5["Holes are negative mass"]
        C6["No calculus / variable density in FA22-COM core"]
    end
    A1 --> B1
    A2 --> B1
    A4 --> B3
    A3 --> B5
    A2 --> B6
    B2 --> C1
    B2 --> C2
    B4 --> C3
    B4 --> C4
    B4 --> C5
    B4 --> C6
```
