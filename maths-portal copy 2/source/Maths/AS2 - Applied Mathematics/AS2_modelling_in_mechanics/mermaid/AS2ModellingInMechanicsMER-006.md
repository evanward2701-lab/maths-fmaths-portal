# AS2ModellingInMechanicsMER-006

## Asset metadata

- asset_id: AS2ModellingInMechanicsMER-006
- lesson_id: AS2ModellingInMechanics
- related_placeholder: AS2ModellingInMechanicsSVG-006
- source: MechYr1-Chp8-Introduction.pdf, page 4; transcript modelling assumptions section
- related lesson section: Core Theory, Modelling Assumptions
- purpose: Link each modelling assumption to its meaning and calculation consequence.

```mermaid
flowchart TD
    A["Modelling assumptions"] --> P["Particle"]
    A --> S["Smooth surface"]
    A --> R["Rough surface"]
    A --> L["Light or smooth pulley"]
    A --> I["Inextensible string"]
    A --> Rod["Rod"]
    A --> Peg["Peg or support"]
    P --> P1["Dimensions negligible"]
    P1 --> P2["Mass concentrated at a single point"]
    P2 --> P3["Rotational effects and air resistance can be ignored"]
    S --> S1["No friction"]
    R --> R1["Friction present"]
    L --> L1["No friction and pulley has no mass"]
    L1 --> L2["Tension same either side of pulley"]
    I --> I1["String does not stretch"]
    I1 --> I2["Connected objects have same acceleration"]
    Rod --> Rod1["One dimension negligible"]
    Rod1 --> Rod2["Mass concentrated along a line and rigid"]
    Peg --> Peg1["Dimensionless and fixed support"]
    Peg1 --> Peg2["Can be rough or smooth depending on question"]
```
