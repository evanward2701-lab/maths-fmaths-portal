# A21TrigonometricFunctionsMermaid-006

**Asset ID:** `A21TrigonometricFunctionsMermaid-006`  
**Source:** Chapter 6 reciprocal graph explanation; CCEA A21-TRIG-LO003  
**Related lesson section:** Core Theory → Graphs of reciprocal trig functions  
**Purpose:** Show how zeros, small values and $\pm1$ values of the original trig graph control the reciprocal graph.

```mermaid
flowchart TD
    A["Start with original graph:<br/>y = sin x, cos x or tan x"] --> B["Reciprocal graph uses y = 1/f(x)"]
    B --> C{"What is f(x)?"}
    C -- "f(x) = 1" --> D["1/f(x) = 1<br/>Point stays at y = 1"]
    C -- "f(x) = -1" --> E["1/f(x) = -1<br/>Point stays at y = -1"]
    C -- "0 < f(x) < 1" --> F["Reciprocal is positive and larger than 1"]
    C -- "-1 < f(x) < 0" --> G["Reciprocal is negative and less than -1"]
    C -- "f(x) = 0" --> H["1/f(x) is undefined<br/>Vertical asymptote"]
    D --> I["Sketch reciprocal branches"]
    E --> I
    F --> I
    G --> I
    H --> I
    I --> J["State domain restrictions and range"]
```
