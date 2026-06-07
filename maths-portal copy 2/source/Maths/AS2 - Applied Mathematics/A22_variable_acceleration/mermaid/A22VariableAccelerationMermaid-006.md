# A22VariableAccelerationMermaid-006

**Asset ID:** `A22VariableAccelerationMermaid-006`  
**Source:** Lesson PDF page 15; transcript derivation of constant acceleration formulae using integration.  
**Related lesson section:** Core Theory 8.8; Worked Example 11  
**Purpose:** Show how \(v=u+at\) and \(s=ut+\frac12at^2\) are derived by integration when acceleration is constant.

```mermaid
flowchart TD
    Given["Given constant acceleration a<br/>initial velocity u<br/>initial displacement 0"]
    
    Step1["Start with acceleration"]
    IntA["Integrate a with respect to t"]
    VExpr["v = at + C"]
    UseU["At t = 0, v = u"]
    CEqualsU["C = u"]
    VFormula["v = u + at"]

    Step2["Now use v = ds/dt"]
    IntV["Integrate v = u + at"]
    SExpr["s = ut + 1/2 at^2 + C"]
    UseS0["At t = 0, s = 0"]
    CEquals0["C = 0"]
    SFormula["s = ut + 1/2 at^2"]

    Given --> Step1 --> IntA --> VExpr --> UseU --> CEqualsU --> VFormula
    VFormula --> Step2 --> IntV --> SExpr --> UseS0 --> CEquals0 --> SFormula
```
