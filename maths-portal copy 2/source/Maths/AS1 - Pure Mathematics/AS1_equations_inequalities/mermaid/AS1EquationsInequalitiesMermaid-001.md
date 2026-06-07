# AS1EquationsInequalitiesMermaid-001

## Asset ID
AS1EquationsInequalitiesMermaid-001

## Source
- CCEA GCE Mathematics Specification Map: AS1 Algebra and functions
- P1 Chapter 3: Equations and Inequalities PDF
- Chapter 3 Equations & Inequalities teacher transcript

## Related lesson section
Core Theory: Method Choice for Equations and Inequalities

## Purpose
Show the student which method to choose: elimination, substitution, discriminant, sketching or set-builder notation.

## Mermaid code

```mermaid
flowchart TD
    A["Start: What type of task is this?"] --> B{"Two equations<br/>in two variables?"}
    B -->|Yes| C{"Are both equations linear?"}
    C -->|Yes| D["Use elimination if coefficients can be matched"]
    C -->|No| E["Use substitution<br/>Make x or y the subject in the simpler equation"]
    E --> F["Substitute into the other equation"]
    F --> G["Solve the resulting equation"]
    G --> H["Substitute back to find the matching variable"]
    H --> I["Write answers as ordered pairs (x,y)"]
    B -->|No| J{"Graph intersection question?"}
    J -->|Yes| K["Equate or substitute equations"]
    K --> L["Rearrange to one equation"]
    L --> M{"Need number of intersections?"}
    M -->|Yes| N["Use discriminant b² - 4ac"]
    N --> O{"Sign of discriminant"}
    O -->|> 0| P["Two distinct real intersections"]
    O -->|= 0| Q["Exactly one repeated/tangent intersection"]
    O -->|< 0| R["No real intersections"]
    M -->|No| S["Solve equation and substitute for coordinates"]
    J -->|No| T{"Inequality in one variable?"}
    T -->|Linear| U["Solve like an equation<br/>Reverse sign if multiplying/dividing by negative"]
    T -->|Quadratic| V["Get 0 on one side"]
    V --> W["Factorise or solve roots"]
    W --> X["Sketch sign regions"]
    X --> Y["Choose above/below axis and include/exclude endpoints"]
    T -->|Fractional reducible| Z["Avoid multiplying by x directly<br/>Use safe transformation such as multiplying by x² where valid"]
    Z --> V
    U --> AA["Write solution set"]
    Y --> AA
    S --> AA
    I --> AA
```
