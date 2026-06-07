# A22VariableAccelerationMermaid-004

**Asset ID:** `A22VariableAccelerationMermaid-004`  
**Source:** Lesson PDF maxima/minima page and transcript discussion.  
**Related lesson section:** Core Theory 8.6; Common Mistakes 12  
**Purpose:** Show how maximum/minimum displacement and velocity connect to \(v=0\) and \(a=0\), while warning that endpoints still matter.

```mermaid
flowchart TD
    Start["Maximum or minimum question"]
    Quantity{"Which quantity is being maximised?"}

    Disp["Displacement s(t)"]
    Vel["Velocity v(t)"]
    Speed["Speed |v(t)|"]

    DS["Set ds/dt = 0"]
    V0["Since ds/dt = v,<br/>solve v(t)=0"]
    DV["Set dv/dt = 0"]
    A0["Since dv/dt = a,<br/>solve a(t)=0"]

    Candidates["Build candidate list:<br/>stationary times + endpoints"]
    CompareS["Compare s values"]
    CompareV["Compare v values"]
    CompareAbs["Compare |v| values"]

    Answer["Choose valid answer in interval<br/>with correct units"]

    Start --> Quantity
    Quantity --> Disp --> DS --> V0 --> Candidates --> CompareS --> Answer
    Quantity --> Vel --> DV --> A0 --> Candidates --> CompareV --> Answer
    Quantity --> Speed --> Candidates --> CompareAbs --> Answer
```
