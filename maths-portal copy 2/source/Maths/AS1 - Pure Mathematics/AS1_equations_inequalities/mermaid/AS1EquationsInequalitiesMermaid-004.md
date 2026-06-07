# AS1EquationsInequalitiesMermaid-004

## Asset ID
AS1EquationsInequalitiesMermaid-004

## Source
- CCEA AS1-AF-LO009: linear and quadratic inequalities in one variable
- P1 Chapter 3 PDF: recap of linear inequalities and solving quadratic inequalities
- Chapter 3 transcript: emphasis on sketching and reasoning

## Related lesson section
Core Theory: Linear and Quadratic Inequalities

## Purpose
Give a repeatable workflow for solving inequalities without losing signs and endpoints.

## Mermaid code

```mermaid
flowchart TD
    A["Start with inequality"] --> B{"Linear or quadratic?"}
    B -->|Linear| C["Expand brackets if needed"]
    C --> D["Collect x terms on one side"]
    D --> E{"Multiply/divide by negative?"}
    E -->|Yes| F["Reverse inequality sign"]
    E -->|No| G["Keep inequality sign"]
    F --> H["Write solution set"]
    G --> H
    B -->|Quadratic| I["Get 0 on one side"]
    I --> J["Factorise or solve roots"]
    J --> K["Mark roots on number line or sketch parabola"]
    K --> L{"Inequality asks for positive or negative?"}
    L -->|> 0 or ≥ 0| M["Choose where graph is above or on x-axis"]
    L -->|< 0 or ≤ 0| N["Choose where graph is below or on x-axis"]
    M --> O{"Strict inequality?"}
    N --> O
    O -->|Yes: < or >| P["Do not include endpoints"]
    O -->|No: ≤ or ≥| Q["Include endpoints"]
    P --> H
    Q --> H
```
