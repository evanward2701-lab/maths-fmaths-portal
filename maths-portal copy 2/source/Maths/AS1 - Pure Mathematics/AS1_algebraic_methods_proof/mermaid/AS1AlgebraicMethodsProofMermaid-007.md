# AS1AlgebraicMethodsProofMermaid-007

**Asset ID:** `AS1AlgebraicMethodsProofMermaid-007`  
**Source:** Teacher transcript warning on not starting with the conclusion, using the `3,4,5` right-triangle proof.  
**Related lesson section:** Worked Example 5; Common Mistakes and Exam Traps.  
**Purpose:** Show the correct proof flow for consecutive integer sides of a right-angled triangle.

```mermaid
flowchart TD
    A["Claim:<br/>If three consecutive integers are sides of a right-angled triangle,<br/>they must be 3, 4 and 5"] --> B["Do not start by checking 3^2 + 4^2 = 5^2"]
    B --> C["Let the side lengths be<br/>x, x + 1, x + 2"]
    C --> D["The hypotenuse is the longest side:<br/>x + 2"]
    D --> E["Use Pythagoras:<br/>x^2 + (x + 1)^2 = (x + 2)^2"]
    E --> F["Expand:<br/>2x^2 + 2x + 1 = x^2 + 4x + 4"]
    F --> G["Rearrange:<br/>x^2 - 2x - 3 = 0"]
    G --> H["Factorise:<br/>(x - 3)(x + 1) = 0"]
    H --> I["x = 3 or x = -1"]
    I --> J["Reject x = -1<br/>Side lengths cannot be negative"]
    J --> K["Therefore x = 3"]
    K --> L["Side lengths are<br/>3, 4, 5"]
```
