# A21TrigonometricFunctionsMermaid-002

**Asset ID:** `A21TrigonometricFunctionsMermaid-002`  
**Source:** CCEA A21-TRIG-LO008; Chapter 6 proof-method evidence  
**Related lesson section:** Core Theory → Two proof tips for reciprocal trig identities  
**Purpose:** Give students a decision-flow for proving identities involving `sec`, `cosec` and `cot`.

```mermaid
flowchart TD
    A["Read the identity carefully"] --> B{"Is one side messier?"}
    B -- "Yes" --> C["Start with the messier side"]
    B -- "No obvious messy side" --> D["Start with the side containing reciprocal functions or fractions"]
    C --> E["Rewrite sec, cosec and cot using sin and cos"]
    D --> E
    E --> F{"Are algebraic fractions being added or subtracted?"}
    F -- "Yes" --> G["Create a common denominator and combine"]
    F -- "No" --> H["Look for common factors"]
    G --> H
    H --> I["Cancel only common factors,<br/>never across addition or subtraction"]
    I --> J{"Can a trig identity now be used?"}
    J -- "sin²θ + cos²θ = 1" --> K["Replace sin²θ + cos²θ by 1"]
    J -- "1 + tan²θ = sec²θ" --> L["Use sec² identity"]
    J -- "1 + cot²θ = cosec²θ" --> M["Use cosec² identity"]
    J -- "Not yet" --> N["Expand, factorise or recombine carefully"]
    K --> O["Simplify to match the target side"]
    L --> O
    M --> O
    N --> O
    O --> P["Write final line:<br/>LHS ≡ RHS, hence proven"]
```
