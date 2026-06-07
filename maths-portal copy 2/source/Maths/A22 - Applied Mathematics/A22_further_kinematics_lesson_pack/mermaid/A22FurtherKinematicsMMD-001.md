# A22FurtherKinematicsMMD-001

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | A22FurtherKinematicsMMD-001 |
| Asset type | Mermaid diagram |
| Unit | A22: A2 2 Applied Mathematics |
| Topic | Further Kinematics |
| Topic code | A22-KIN |
| Related LO IDs | A22-KIN-LO002 |
| Related lesson section | Core Theory: Constant velocity vector motion |
| Source | Chapter 8 Further Kinematics transcript; MechYr2-Chp8-FurtherKinematics.pdf p.3 |
| Purpose | Show how a starting position vector and constant velocity vector combine to form r = r0 + vt. |

```mermaid
flowchart LR
    O["Fixed origin O"] --> R0["Initial position<br/>r0 = (3, 1)"]
    R0 -->|"+ v each second<br/>v = (4, 2)"| R1["After 1 second<br/>r = (7, 3)"]
    R1 -->|"+ v again"| R2["After 2 seconds<br/>r = (11, 5)"]
    R2 --> General["General position<br/>r = r0 + vt<br/>r = (3 + 4t, 1 + 2t)"]
    General --- Note1["Position = starting position + displacement"]
    General --- Note2["Displacement = velocity × time"]
```
