# A22FurtherKinematicsMMD-003

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | A22FurtherKinematicsMMD-003 |
| Asset type | Mermaid diagram |
| Unit | A22: A2 2 Applied Mathematics |
| Topic | Further Kinematics |
| Topic code | A22-KIN |
| Related LO IDs | A22-KIN-LO002 |
| Related lesson section | Worked Example: Velocity vector, speed and bearing |
| Source | Chapter 8 Further Kinematics transcript; MechYr2-Chp8-FurtherKinematics.pdf p.5 |
| Purpose | Show how a velocity vector gives speed by magnitude and direction by bearing. |

```mermaid
flowchart TB
    V["Velocity vector<br/>v = (3, 10)"] --> Components["Components"]
    Components --> East["i-component = 3<br/>3 units east"]
    Components --> North["j-component = 10<br/>10 units north"]
    V --> Speed["Speed"]
    Speed --> Mag["|v| = sqrt(3^2 + 10^2)"]
    Mag --> SpeedAns["|v| = sqrt(109) = 10.4 ms^-1"]
    V --> Bearing["Bearing"]
    Bearing --> Tan["tan(theta) = 3/10"]
    Tan --> Theta["theta = 16.7 degrees"]
    Theta --> BearingAns["Bearing = 017 degrees"]
```
