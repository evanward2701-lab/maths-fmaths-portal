# AS1AlgebraicMethodsProofMermaid-006

**Asset ID:** `AS1AlgebraicMethodsProofMermaid-006`  
**Source:** Teacher transcript harder proof by exhaustion example: cube numbers are a multiple of `9`, one more, or one less.  
**Related lesson section:** Worked Example 8.  
**Purpose:** Show why exhaustion does not always mean even/odd, and why modulo-3 cases are chosen for cube-number questions.

```mermaid
flowchart TD
    A["Claim:<br/>Every cube number is a multiple of 9,<br/>one more than a multiple of 9,<br/>or one less than a multiple of 9"] --> B["Even and odd split gives powers of 2<br/>Not useful for multiples of 9"]
    B --> C["Use three exhaustive cases"]
    C --> D["Case 1:<br/>integer = 3n"]
    D --> D1["(3n)^3 = 27n^3"]
    D1 --> D2["= 9(3n^3)"]
    D2 --> D3["Multiple of 9"]
    C --> E["Case 2:<br/>integer = 3n + 1"]
    E --> E1["(3n + 1)^3"]
    E1 --> E2["= 27n^3 + 27n^2 + 9n + 1"]
    E2 --> E3["= 9(3n^3 + 3n^2 + n) + 1"]
    E3 --> E4["One more than a multiple of 9"]
    C --> F["Case 3:<br/>integer = 3n - 1"]
    F --> F1["(3n - 1)^3"]
    F1 --> F2["= 27n^3 - 27n^2 + 9n - 1"]
    F2 --> F3["= 9(3n^3 - 3n^2 + n) - 1"]
    F3 --> F4["One less than a multiple of 9"]
    D3 --> G["All cases covered"]
    E4 --> G
    F4 --> G
    G --> H["Therefore the statement is true"]
```
