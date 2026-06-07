# AS1AlgebraicMethodsProofMermaid-005

**Asset ID:** `AS1AlgebraicMethodsProofMermaid-005`  
**Source:** Teacher transcript disproof by counterexample section.  
**Related lesson section:** Worked Examples 9 to 11; Exam Technique.  
**Purpose:** Show the logic of disproof by counterexample.

```mermaid
flowchart TD
    A["Universal statement:<br/>For every allowed value, the claim is true"] --> B["To disprove it, search for one allowed value"]
    B --> C{"Does the value satisfy the conditions?"}
    C -->|No| D["Not a valid counterexample<br/>Try another value"]
    C -->|Yes| E{"Does it make the conclusion false?"}
    E -->|No| F["This value does not disprove it<br/>Try another value"]
    E -->|Yes| G["Valid counterexample found"]
    G --> H["Write the substitution clearly"]
    H --> I["Show why the conclusion fails"]
    I --> J["Therefore the statement is false"]
```
