# A21TrigonometricFunctionsMermaid-005

**Asset ID:** `A21TrigonometricFunctionsMermaid-005`  
**Source:** Chapter 6 notation warnings; CCEA A21-TRIG-LO002  
**Related lesson section:** Key Definitions and Notation  
**Purpose:** Prevent the notation trap: confusing inverse trig notation with reciprocal trig notation.

```mermaid
flowchart TD
    A["See a trig expression"] --> B{"Does it use superscript -1?<br/>Example: cos⁻¹x"}
    B -- "Yes" --> C["Inverse trig function"]
    C --> D["cos⁻¹x = arccos x"]
    D --> E["Meaning:<br/>the angle whose cosine is x"]
    B -- "No" --> F{"Does it use sec, cosec or cot?"}
    F -- "sec x" --> G["sec x = 1/cos x"]
    F -- "cosec x" --> H["cosec x = 1/sin x"]
    F -- "cot x" --> I["cot x = 1/tan x = cos x/sin x"]
    F -- "No" --> J["Use ordinary sin, cos or tan rules"]
    E --> K["Warning:<br/>cos⁻¹x does not mean 1/cos x"]
    G --> L["Reciprocal trig function"]
    H --> L
    I --> L
```
