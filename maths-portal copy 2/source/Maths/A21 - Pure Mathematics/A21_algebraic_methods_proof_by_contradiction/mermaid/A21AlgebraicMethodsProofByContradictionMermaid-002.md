# Asset ID: A21AlgebraicMethodsProofByContradictionMermaid-002

## Source
- Dr Frost/Pearson-style negation slide.
- Phase 1 Key Definitions and Notation.
- Teacher transcript discussion of assuming the negation.

## Related Lesson Section
Key Definitions and Notation

## Purpose
Help students choose the correct negation before beginning a contradiction proof.

## Mermaid Diagram

```mermaid
flowchart TD
    A["Statement type"] --> B{"Which form?"}
    B --> C["There is no object<br/>with property P"]
    C --> C1["Negation:<br/>There exists an object<br/>with property P"]
    B --> D["There exists an object<br/>with property P"]
    D --> D1["Negation:<br/>There is no object<br/>with property P"]
    B --> E["All objects have<br/>property P"]
    E --> E1["Negation:<br/>At least one object<br/>does not have property P"]
    B --> F["There are infinitely many<br/>objects of a type"]
    F --> F1["Negation:<br/>There are finitely many<br/>objects of that type"]
    B --> G["If A, then B"]
    G --> G1["Negation:<br/>A is true and B is false"]
    C1 --> H["Use this as the<br/>contradiction assumption"]
    D1 --> H
    E1 --> H
    F1 --> H
    G1 --> H
```
