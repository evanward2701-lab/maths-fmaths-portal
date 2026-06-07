# A22VariableAccelerationMermaid-001

**Asset ID:** `A22VariableAccelerationMermaid-001`  
**Source:** CCEA A22-KIN-LO001; lesson PDF pages on differentiation and integration.  
**Related lesson section:** Core Theory 8.2 and 8.3  
**Purpose:** Show the “differentiate down, integrate up” chain between displacement, velocity and acceleration.

```mermaid
flowchart TD
    S["Displacement<br/>s(t) or x(t)<br/>units: m"]
    V["Velocity<br/>v(t)<br/>units: m s^-1"]
    A["Acceleration<br/>a(t)<br/>units: m s^-2"]

    S -->|"differentiate with respect to t<br/>v = ds/dt"| V
    V -->|"differentiate with respect to t<br/>a = dv/dt"| A

    A -->|"integrate with respect to t<br/>v = ∫a dt"| V
    V -->|"integrate with respect to t<br/>s = ∫v dt"| S

    S -.->|"differentiate twice<br/>a = d^2s/dt^2"| A
```
