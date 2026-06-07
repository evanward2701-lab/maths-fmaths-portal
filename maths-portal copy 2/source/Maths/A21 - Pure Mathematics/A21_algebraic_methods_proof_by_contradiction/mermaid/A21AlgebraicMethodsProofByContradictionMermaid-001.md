# Asset ID: A21AlgebraicMethodsProofByContradictionMermaid-001

## Source
- CCEA GCE Mathematics specification map: overarching proof and reasoning theme.
- Teacher transcript: proof by contradiction method.
- Dr Frost/Pearson-style lesson PDF: proof-by-contradiction structure.

## Related Lesson Section
Core Theory

## Purpose
Show the central proof-by-contradiction logic loop: assume the negation, derive a contradiction, reject the assumption, and conclude the original statement.

## Mermaid Diagram

```mermaid
flowchart TD
    A["Original statement S<br/>We want to prove S is true"] --> B["Assume for contradiction<br/>not S is true"]
    B --> C["Use valid mathematics<br/>inside the assumption"]
    C --> D{"Does the assumption<br/>force an impossibility?"}
    D -- "Yes" --> E["Contradiction found"]
    E --> F["Therefore not S is false"]
    F --> G["Therefore S is true"]
    D -- "No" --> H["Proof incomplete<br/>More reasoning needed"]
    H --> C
```
