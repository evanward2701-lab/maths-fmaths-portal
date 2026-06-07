# AS1VectorsMermaid-007

## Asset ID
AS1VectorsMermaid-007

## Source
P1-Chp11-Vectors.pdf, Position Vectors slides.

## Related lesson section
Core Theory: Position vectors and vector differences; Worked Examples 9 and 10.

## Purpose
Show how position vectors from the origin lead to the vector difference formula AB = OB - OA.

```mermaid
flowchart TD
    A["Point A has coordinates (x1, y1)"] --> B["Position vector OA = (x1, y1)"]
    C["Point B has coordinates (x2, y2)"] --> D["Position vector OB = (x2, y2)"]
    B --> E["Vector from A to B"]
    D --> E
    E --> F["AB = OB - OA"]
    F --> G["AB = (x2, y2) - (x1, y1)"]
    G --> H["AB = (x2 - x1, y2 - y1)"]
    H --> I["Distance AB = |AB|"]
    I --> J["AB distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)"]
```
