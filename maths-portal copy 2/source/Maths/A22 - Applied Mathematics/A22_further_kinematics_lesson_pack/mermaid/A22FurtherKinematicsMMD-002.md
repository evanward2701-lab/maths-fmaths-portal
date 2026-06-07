# A22FurtherKinematicsMMD-002

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | A22FurtherKinematicsMMD-002 |
| Asset type | Mermaid diagram |
| Unit | A22: A2 2 Applied Mathematics |
| Topic | Further Kinematics |
| Topic code | A22-KIN |
| Related LO IDs | A22-KIN-LO002 |
| Related lesson section | Core Theory: Constant acceleration vector SUVAT |
| Source | Chapter 8 Further Kinematics transcript; MechYr2-Chp8-FurtherKinematics.pdf p.5 |
| Purpose | Show vector/scalar SUVAT quantities and the invalid squared-vector warning. |

```mermaid
flowchart TB
    Start["Constant acceleration vector motion"] --> Vectors["Vector quantities"]
    Start --> Scalar["Scalar quantity"]
    Vectors --> R["r: position or displacement vector"]
    Vectors --> U["u: initial velocity vector"]
    Vectors --> V["v: final velocity vector"]
    Vectors --> A["a: acceleration vector"]
    Scalar --> T["t: time"]
    Start --> Good["Valid vector SUVAT forms"]
    Good --> Eq1["v = u + at"]
    Good --> Eq2["r = r0 + ut + 1/2 at^2"]
    Good --> Eq3["r = r0 + vt - 1/2 at^2"]
    Start --> Warning["Exam warning"]
    Warning --> Bad["Do not use v^2 = u^2 + 2as as a vector equation"]
```
