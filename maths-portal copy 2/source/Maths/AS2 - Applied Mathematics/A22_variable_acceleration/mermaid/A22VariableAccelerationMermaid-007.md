# A22VariableAccelerationMermaid-007

**Asset ID:** `A22VariableAccelerationMermaid-007`  
**Source:** Lesson PDF pages 3, 8 and 9; transcript warnings on greatest speed and graph reasoning.  
**Related lesson section:** Worked Example 2; Worked Example 7; Exam Technique Notes  
**Purpose:** Provide a decision path for greatest-speed questions, especially when velocity is negative.

```mermaid
flowchart TD
    Start["Greatest speed in interval a <= t <= b"]
    Remember["Speed = |velocity|"]
    Endpoints["Evaluate v(a) and v(b)"]
    Stationary["Find stationary points of v(t)<br/>solve dv/dt = 0"]
    Filter["Keep only stationary times inside the interval"]
    Eval["Evaluate v(t) at all candidate times"]
    AbsValues["Convert each value to speed using |v|"]
    Compare["Choose the largest speed"]
    Units["State answer with units m s^-1"]

    Start --> Remember --> Endpoints --> Stationary --> Filter --> Eval --> AbsValues --> Compare --> Units
```
