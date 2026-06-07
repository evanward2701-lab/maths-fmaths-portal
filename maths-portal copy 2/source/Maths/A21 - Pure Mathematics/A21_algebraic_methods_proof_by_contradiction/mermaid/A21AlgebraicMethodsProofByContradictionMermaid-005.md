# Asset ID: A21AlgebraicMethodsProofByContradictionMermaid-005

## Source
- Teacher transcript worked example: prove \(\sqrt2\) is irrational.
- Dr Frost/Pearson-style slide proof.

## Related Lesson Section
Worked Example 5

## Purpose
Show the contradiction chain in the standard proof that \(\sqrt2\) is irrational.

## Mermaid Diagram

```mermaid
flowchart TD
    A["Claim:<br/>sqrt(2) is irrational"] --> B["Assume for contradiction:<br/>sqrt(2) is rational"]
    B --> C["sqrt(2) = a/b<br/>in simplest form"]
    C --> D["2 = a^2 / b^2"]
    D --> E["2b^2 = a^2"]
    E --> F["a^2 is even"]
    F --> G["a is even"]
    G --> H["let a = 2k"]
    H --> I["2b^2 = (2k)^2"]
    I --> J["2b^2 = 4k^2"]
    J --> K["b^2 = 2k^2"]
    K --> L["b^2 is even"]
    L --> M["b is even"]
    M --> N["a and b are both even"]
    N --> O["Contradiction:<br/>a/b was in simplest form"]
    O --> P["Therefore sqrt(2) is irrational"]
```
