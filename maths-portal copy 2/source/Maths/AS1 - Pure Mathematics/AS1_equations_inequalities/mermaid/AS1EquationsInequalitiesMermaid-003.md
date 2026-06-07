# AS1EquationsInequalitiesMermaid-003

## Asset ID
AS1EquationsInequalitiesMermaid-003

## Source
- CCEA AS1-AF-LO004: discriminant of a quadratic function
- P1 Chapter 3 PDF: simultaneous equations using graphs and discriminant examples
- Chapter 3 transcript: warning that the combined quadratic represents intersection x-values

## Related lesson section
Core Theory: Graph Intersections and the Discriminant

## Purpose
Show how the discriminant controls the number of real roots and therefore the number of graph intersections.

## Mermaid code

```mermaid
flowchart TD
    A["Line and curve intersection problem"] --> B["Substitute or equate equations"]
    B --> C["Rearrange to ax² + bx + c = 0"]
    C --> D["This quadratic gives the x-values of intersections"]
    D --> E["Calculate discriminant Δ = b² - 4ac"]
    E --> F{"What is Δ?"}
    F -->|Δ > 0| G["Two distinct real roots"]
    G --> G1["Two x-values"]
    G1 --> G2["Two points of intersection"]
    F -->|Δ = 0| H["One repeated real root"]
    H --> H1["One x-value"]
    H1 --> H2["Exactly one point of intersection"]
    F -->|Δ < 0| I["No real roots"]
    I --> I1["No real x-values"]
    I1 --> I2["No real points of intersection"]
    D --> J["Do not confuse this combined quadratic with the original curve"]
```
