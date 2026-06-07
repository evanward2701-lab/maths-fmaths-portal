# Asset ID: A21AlgebraicMethodsProofByContradictionMermaid-004

## Source
- Teacher transcript worked example: given rational \(a\) and irrational \(b\), prove \(a-b\) is irrational.
- Phase 1 Worked Example 4.

## Related Lesson Section
Worked Example 4

## Purpose
Show the strategy for rational/irrational contradiction proofs.

## Mermaid Diagram

```mermaid
flowchart TD
    A["Claim:<br/>a rational, b irrational<br/>implies a - b irrational"] --> B["Assume for contradiction:<br/>a rational, b irrational,<br/>a - b rational"]
    B --> C["a = c/d<br/>c,d integers, d not 0"]
    B --> D["a - b = e/f<br/>e,f integers, f not 0"]
    C --> E["Rearrange to make b the subject"]
    D --> E
    E --> F["b = a - e/f"]
    F --> G["b = c/d - e/f"]
    G --> H["b = (cf - de)/(df)"]
    H --> I["So b is rational"]
    I --> J["Contradiction:<br/>b was assumed irrational"]
    J --> K["Therefore a - b is irrational"]
```
