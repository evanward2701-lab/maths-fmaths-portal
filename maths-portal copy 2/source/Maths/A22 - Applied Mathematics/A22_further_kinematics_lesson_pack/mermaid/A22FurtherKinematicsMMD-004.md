# A22FurtherKinematicsMMD-004

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | A22FurtherKinematicsMMD-004 |
| Asset type | Mermaid diagram |
| Unit | A22: A2 2 Applied Mathematics |
| Topic | Further Kinematics |
| Topic code | A22-KIN |
| Related LO IDs | A22-KIN-LO003, A22-KIN-LO004 |
| Related lesson section | Core Theory: Projectiles using vectors |
| Source | Chapter 8 Further Kinematics transcript; MechYr2-Chp8-FurtherKinematics.pdf p.9 |
| Purpose | Show the modelling flow for projectile motion using vector SUVAT under gravity. |

```mermaid
flowchart TB
    Context["Projectile under gravity"] --> Inputs["Set up vectors"]
    Inputs --> R0["Initial position<br/>r0 = (0, 20)"]
    Inputs --> U["Initial velocity<br/>u = (5, 8)"]
    Inputs --> A["Acceleration due to gravity<br/>a = (0, -9.8)"]
    R0 --> Formula["r = r0 + ut + 1/2 at^2"]
    U --> Formula
    A --> Formula
    Formula --> R["r = (5t, 20 + 8t - 4.9t^2)"]
    R --> Ground["Ground impact condition"]
    Ground --> Jzero["Set vertical component equal to zero"]
    Jzero --> Quad["20 + 8t - 4.9t^2 = 0"]
```
