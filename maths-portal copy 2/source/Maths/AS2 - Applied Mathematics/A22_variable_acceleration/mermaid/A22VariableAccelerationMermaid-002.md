# A22VariableAccelerationMermaid-002

**Asset ID:** `A22VariableAccelerationMermaid-002`  
**Source:** CCEA A22-KIN-LO001; transcript explanation that displacement, velocity or acceleration can be given as functions of time.  
**Related lesson section:** Exam Technique Notes 13.2  
**Purpose:** Help students decide whether to differentiate, integrate, substitute, or solve an equation.

```mermaid
flowchart TD
    Start["Question gives a function of time"]
    GivenS["Given displacement<br/>s(t) or x(t)"]
    GivenV["Given velocity<br/>v(t)"]
    GivenA["Given acceleration<br/>a(t)"]

    WantS["Need displacement<br/>s or x"]
    WantV["Need velocity<br/>v"]
    WantA["Need acceleration<br/>a"]

    Diff1["Differentiate once"]
    Diff2["Differentiate twice"]
    Int1["Integrate once<br/>include + C if indefinite"]
    Int2["Integrate twice<br/>use conditions each time"]
    Sub["Substitute the given time"]
    SolveRest["If at rest, solve v(t)=0"]

    Start --> GivenS
    Start --> GivenV
    Start --> GivenA

    GivenS --> WantV --> Diff1
    GivenS --> WantA --> Diff2
    GivenV --> WantA --> Diff1
    GivenV --> WantS --> Int1
    GivenA --> WantV --> Int1
    GivenA --> WantS --> Int2

    Diff1 --> Sub
    Diff2 --> Sub
    Int1 --> Sub
    Int2 --> Sub

    GivenV --> SolveRest
    GivenS -->|"first find v = ds/dt"| SolveRest
```
