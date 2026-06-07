# AS1VectorsMermaid-003

## Asset ID
AS1VectorsMermaid-003

## Source
P1-Chp11-Vectors.pdf, Vector Basics slide on subtraction, zero vector and scalars.

## Related lesson section
Core Theory: Vector subtraction; Scalar multiplication; Parallel vectors.

## Purpose
Show the logic chain connecting vector subtraction, negation, scalar multiplication and parallel-vector proof.

```mermaid
flowchart TD
    A["Vector subtraction"] --> B["a - b = a + (-b)"]
    B --> C["-b has same magnitude as b<br/>but opposite direction"]
    D["Zero vector"] --> E["PQ + QP = 0"]
    E --> F["No net movement"]
    G["Scalar multiplication"] --> H["lambda a scales vector a"]
    H --> I["Positive scalar:<br/>same direction"]
    H --> J["Negative scalar:<br/>opposite direction"]
    H --> K["Magnitude changes unless scalar = 1"]
    L["Parallel-vector test"] --> M["Can one vector be written as a scalar multiple of the other?"]
    M -->|"Yes"| N["Vectors are parallel"]
    M -->|"No"| O["Need another method or not parallel"]
```
