# Asset ID: A21AlgebraicMethodsProofByContradictionMermaid-006

## Source
- Teacher transcript and slide evidence for Euclid's proof that there are infinitely many prime numbers.
- Phase 1 Worked Example 6.

## Related Lesson Section
Worked Example 6

## Purpose
Show how assuming a finite list of all primes leads to \(N=p_1p_2\cdots p_n+1\), which cannot be divisible by any prime in the list.

## Mermaid Diagram

```mermaid
flowchart TD
    A["Claim:<br/>There are infinitely many primes"] --> B["Assume for contradiction:<br/>There are finitely many primes"]
    B --> C["List all primes:<br/>p1, p2, ..., pn"]
    C --> D["Construct:<br/>N = p1 p2 ... pn + 1"]
    D --> E["Choose any listed prime pi"]
    E --> F["pi divides the product<br/>p1 p2 ... pn"]
    F --> G["N = pi times M + 1"]
    G --> H["Remainder is 1"]
    H --> I["N is not divisible<br/>by any listed prime"]
    I --> J{"What is N?"}
    J --> K["N is prime"]
    J --> L["N is composite"]
    K --> M["New prime not in the list"]
    L --> N["Prime factor not in the list"]
    M --> O["Contradiction"]
    N --> O
    O --> P["Therefore infinitely many primes"]
```
