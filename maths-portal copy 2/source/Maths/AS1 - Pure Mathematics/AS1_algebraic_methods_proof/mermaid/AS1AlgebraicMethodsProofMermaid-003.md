# AS1AlgebraicMethodsProofMermaid-003

**Asset ID:** `AS1AlgebraicMethodsProofMermaid-003`  
**Source:** Teacher transcript worked example: product of two odd numbers is odd.  
**Related lesson section:** Worked Example 1.  
**Purpose:** Show the proof-by-deduction algebra chain for proving the product of two odd numbers is odd.

```mermaid
flowchart TD
    A["Claim:<br/>The product of two odd numbers is odd"] --> B["Let the odd numbers be<br/>2m + 1 and 2n + 1<br/>where m and n are integers"]
    B --> C["Multiply:<br/>(2m + 1)(2n + 1)"]
    C --> D["Expand:<br/>4mn + 2m + 2n + 1"]
    D --> E["Factor the even part:<br/>2(2mn + m + n) + 1"]
    E --> F["2mn + m + n is an integer"]
    F --> G["Expression has form<br/>2(integer) + 1"]
    G --> H["Therefore the product is odd"]
```
