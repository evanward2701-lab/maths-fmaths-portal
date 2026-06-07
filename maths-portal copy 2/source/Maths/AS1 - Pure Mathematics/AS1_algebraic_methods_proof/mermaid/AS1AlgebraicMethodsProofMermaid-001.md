# AS1AlgebraicMethodsProofMermaid-001

**Asset ID:** `AS1AlgebraicMethodsProofMermaid-001`  
**Source:** Teacher transcript, proof overview and method definitions.  
**Related lesson section:** Big Picture Explanation; Core Theory; Exam Technique.  
**Purpose:** Show how to choose between proof by deduction, proof by exhaustion and disproof by counterexample. Proof by contradiction is shown as A2/future context only.

```mermaid
flowchart TD
    A["Start with the question wording"] --> B{"Does it ask you to prove a statement is true?"}
    B -->|Yes| C{"Can direct algebra reach the required form?"}
    C -->|Yes| D["Use proof by deduction<br/>Start from known facts<br/>Work to the conclusion"]
    C -->|No| E{"Can the values be split into all possible cases?"}
    E -->|Yes| F["Use proof by exhaustion<br/>Prove every case<br/>Then write a final conclusion"]
    E -->|No| G["Look for another valid proof route<br/>Do not assume the conclusion"]
    B -->|No| H{"Does it ask you to disprove or prove false?"}
    H -->|Yes| I["Use disproof by counterexample<br/>Find one legal value that breaks the claim"]
    H -->|No| J["Read the wording again<br/>Identify whether it is always, sometimes or never true"]
    K["Proof by contradiction"]:::future
    K --> L["A2/future context only<br/>Not treated as AS1 core here"]:::future
    classDef future fill:#eeeeee,stroke:#777777,color:#333333,stroke-dasharray: 5 5;
```
