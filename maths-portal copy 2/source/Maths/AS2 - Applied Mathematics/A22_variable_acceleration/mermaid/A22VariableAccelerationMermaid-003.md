# A22VariableAccelerationMermaid-003

**Asset ID:** `A22VariableAccelerationMermaid-003`  
**Source:** Lesson PDF page 3 and transcript introduction.  
**Related lesson section:** Big Picture Explanation and Core Theory 8.1  
**Purpose:** Compare constant acceleration modelling with variable acceleration modelling.

```mermaid
flowchart LR
    Old["Earlier kinematics<br/>constant acceleration"]
    OldGraph["Velocity-time graph<br/>straight-line sections"]
    OldTools["SUVAT formulae<br/>usually appropriate"]

    New["Variable acceleration"]
    NewFunction["s, v or a given as a function of time<br/>for example v = 1/2 t^3"]
    NewGraph["Velocity-time graph may be curved"]
    NewTools["Use calculus<br/>differentiate or integrate"]

    Old --> OldGraph --> OldTools
    New --> NewFunction --> NewGraph --> NewTools

    OldGraph -. "sudden changes can be unrealistic" .-> NewGraph
```
