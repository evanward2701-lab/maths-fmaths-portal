# AS1AlgebraicMethodsProofMermaid-004

**Asset ID:** `AS1AlgebraicMethodsProofMermaid-004`  
**Source:** Teacher transcript proof by exhaustion example `n^2+n` even for all integers.  
**Related lesson section:** Worked Example 6; Core Theory.  
**Purpose:** Show that proof by exhaustion must cover every possible case.

```mermaid
flowchart TD
    A["Claim:<br/>n^2 + n is even for all integers n"] --> B["Every integer is either even or odd"]
    B --> C["Case 1:<br/>n is even"]
    C --> C1["Let n = 2k"]
    C1 --> C2["n^2 + n = (2k)^2 + 2k"]
    C2 --> C3["= 4k^2 + 2k"]
    C3 --> C4["= 2(2k^2 + k)"]
    C4 --> C5["Even"]
    B --> D["Case 2:<br/>n is odd"]
    D --> D1["Let n = 2k + 1"]
    D1 --> D2["n^2 + n = (2k + 1)^2 + (2k + 1)"]
    D2 --> D3["= 4k^2 + 6k + 2"]
    D3 --> D4["= 2(2k^2 + 3k + 1)"]
    D4 --> D5["Even"]
    C5 --> E["Both possible cases work"]
    D5 --> E
    E --> F["Therefore n^2 + n is even for all integers n"]
```
