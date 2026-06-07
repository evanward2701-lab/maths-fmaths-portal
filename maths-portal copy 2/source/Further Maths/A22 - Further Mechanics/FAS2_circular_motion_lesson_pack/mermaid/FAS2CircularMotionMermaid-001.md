# FAS2CircularMotionMermaid-001

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | `FAS2CircularMotionMermaid-001` |
| Asset type | Mermaid diagram |
| Topic ID | `FAS2CircularMotion` |
| Unit | `FAS2`: Further AS 2 Applied Mathematics |
| Topic codes | `FAS2-CM`, `FAS2-FCM` |
| Related lesson file | `FAS2_circular_motion_lesson.md` |
| Related lesson section | `# 9. Visual Asset Integration` |
| Used placeholder | `[VISUAL PLACEHOLDER: FAS2CircularMotionMermaid-001 | Source: CCEA Further Maths specification boundary + lesson PDF chapter overview + teacher transcript | Insert from mermaid/FAS2CircularMotionMermaid-001.md | Purpose: Show the decision pathway for circular motion problems. The diagram must branch into horizontal circles, vertical circles, constrained vertical circles, unconstrained vertical circles, and projectile motion after leaving the path.]` |
| Source | CCEA Further Maths specification boundary + lesson PDF chapter overview + teacher transcript |
| Purpose | Show the decision pathway for circular motion problems, separating horizontal-circle methods from vertical-circle methods. |

## Creation Notes

This Mermaid diagram supports the main lesson’s method-selection strategy. It preserves the evidence-backed distinction between horizontal circular motion with constant speed, vertical circular motion where speed usually changes, constrained vertical-circle motion, unconstrained vertical-circle motion, and projectile motion after leaving the circular path.

## Mermaid Diagram

```mermaid
flowchart TD
    A["Circular motion problem"] --> B{"Is the motion in a horizontal plane?"}
    A --> C{"Is the motion in a vertical plane?"}

    B -->|Yes| H1["Horizontal circular motion"]
    B -->|No| C

    H1 --> H2["Check units first<br/>m, s, kg, N, rad s^-1"]
    H2 --> H3["Use angular-linear link<br/>v = rω"]
    H3 --> H4["Use radial acceleration<br/>a = rω^2 or a = v^2/r"]
    H4 --> H5["Draw only real forces<br/>T, R, friction, mg"]
    H5 --> H6["Resolve vertically<br/>usually equilibrium"]
    H6 --> H7["Resolve horizontally towards centre<br/>real inward resultant = ma"]
    H7 --> H8{"Which horizontal model?"}

    H8 --> H9["Flat road / rough disc<br/>friction may provide inward force"]
    H8 --> H10["Conical pendulum<br/>vertical balance, horizontal acceleration"]
    H8 --> H11["Banked corner without friction<br/>reaction has inward component"]
    H8 --> H12["Two strings / wire / other model<br/>components provide inward resultant"]

    H9 --> H13["If limiting friction:<br/>F = μR"]
    H10 --> H14["Typical equations:<br/>T cos α = mg<br/>T sin α = mrω^2"]
    H11 --> H15["Typical equations:<br/>R cos α = mg<br/>R sin α = mv^2/r"]
    H12 --> H16["Build simultaneous equations<br/>from vertical and radial directions"]

    C -->|Yes| V1["Vertical circular motion"]
    C -->|No| X1["Check whether another mechanics model is needed"]

    V1 --> V2["Speed usually changes<br/>bottom fastest, top slowest"]
    V2 --> V3["Choose G.P.E. zero level<br/>lowest point or centre"]
    V3 --> V4["Use energy to relate speeds<br/>K.E. + G.P.E. conserved when only gravity does work"]
    V4 --> V5["Use radial acceleration<br/>a = v^2/r"]
    V5 --> V6["Resolve forces towards centre<br/>real inward resultant = mv^2/r"]
    V6 --> V7{"Is the particle constrained to the circle?"}

    V7 -->|Yes| K1["Constrained circular path"]
    K1 --> K2["Examples:<br/>rigid rod<br/>bead on circular wire"]
    K2 --> K3["Particle cannot leave the circle"]
    K3 --> K4["For full circle:<br/>check speed at the top"]
    K4 --> K5["Rod may be in tension or thrust<br/>wire reaction may change direction"]

    V7 -->|No| U1["Unconstrained circular path"]
    U1 --> U2["Examples:<br/>string<br/>outside of smooth sphere"]
    U2 --> U3{"Which contact force controls the path?"}
    U3 -->|String| U4["String must stay taut<br/>T ≥ 0"]
    U3 -->|Surface| U5["Surface contact requires<br/>R ≥ 0"]

    U4 --> U6{"Does T become zero?"}
    U5 --> U7{"Does R become zero?"}

    U6 -->|No| U8["Continue circular motion<br/>use energy + radial F = ma"]
    U7 -->|No| U8

    U6 -->|Yes| P1["String goes slack"]
    U7 -->|Yes| P2["Particle loses contact"]

    P1 --> P3["Circular model ends"]
    P2 --> P3
    P3 --> P4["Particle moves freely under gravity"]
    P4 --> P5["Use projectile motion<br/>initial velocity is tangent to circle at leaving point"]
    P5 --> P6["Remember:<br/>horizontal velocity may remain non-zero at highest point"]

    H13 --> Z["Final answer<br/>include units and direction where needed"]
    H14 --> Z
    H15 --> Z
    H16 --> Z
    K5 --> Z
    U8 --> Z
    P6 --> Z

    Z --> W["Exam warning:<br/>do not add centripetal force as a separate force"]
```

## Accessibility Description

This flowchart begins with a circular motion problem and splits the problem into horizontal-plane and vertical-plane cases. It ends with a warning that “centripetal force” must not be added as a separate force.
