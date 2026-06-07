# Asset ID: A21AlgebraicMethodsProofByContradictionMermaid-003

## Source
- Teacher transcript worked example: if n squared is even, then n must be even.
- Dr Frost/Pearson-style slide example.

## Related Lesson Section
Worked Example 2

## Purpose
Show the conditional-statement structure for proving: if \(n^2\) is even, then \(n\) is even.

## Mermaid Diagram

```mermaid
flowchart TD
    A["Claim:<br/>If n squared is even,<br/>then n is even"] --> B["Negation of if A then B:<br/>A is true and B is false"]
    B --> C["Assume for contradiction:<br/>n squared is even<br/>and n is odd"]
    C --> D["Since n is odd,<br/>n = 2k + 1"]
    D --> E["n squared = (2k + 1)^2"]
    E --> F["n squared = 4k^2 + 4k + 1"]
    F --> G["n squared = 2(2k^2 + 2k) + 1"]
    G --> H["Therefore n squared is odd"]
    H --> I["But assumption said<br/>n squared is even"]
    I --> J["Contradiction"]
    J --> K["Therefore if n squared is even,<br/>n must be even"]
```
