# AS1AlgebraicMethodsProofMermaid-008

**Asset ID:** `AS1AlgebraicMethodsProofMermaid-008`  
**Source:** Screenshot PDF pages 1 to 3 show the four proof-type cards; transcript states proof by contradiction is A2/future context.  
**Related lesson section:** Big Picture Explanation; Syllabus Gap Check.  
**Purpose:** Recreate the proof-type overview from the screenshots while clearly marking proof by contradiction as outside AS1 core.

```mermaid
flowchart LR
    A["Chapter 7b:<br/>Algebraic Methods, Proof"] --> B["AS1 Core"]
    A --> C["A2 / Future Context"]
    B --> D["Proof by deduction<br/>Example:<br/>Product of two odd numbers is odd"]
    B --> E["Proof by exhaustion<br/>Example:<br/>n^2 + n is even for all integers n"]
    B --> F["Disproof by counterexample<br/>Example:<br/>n^2 - n + 41 is prime for all integers n"]
    C --> G["Proof by contradiction<br/>Example:<br/>sqrt(2) is irrational"]:::future
    classDef future fill:#eeeeee,stroke:#777777,color:#333333,stroke-dasharray: 5 5;
```
