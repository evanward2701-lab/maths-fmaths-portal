# Mermaid Asset: FA22FurtherKinematicsMermaid-001

## Asset metadata

| Field | Value |
|---|---|
| Asset ID | `FA22FurtherKinematicsMermaid-001` |
| Asset type | Mermaid diagram |
| Topic ID | `FA22FurtherKinematics` |
| Unit | `FA22`: Further A2 2 Applied Mathematics |
| Topic code | `FA22-FKIN` |
| Related lesson file | `FA22_further_kinematics_lesson.md` |
| Related lesson section | `# 9. Visual Asset Integration`, `# 8. Core Theory` |
| Used placeholder | `[VISUAL PLACEHOLDER: FA22FurtherKinematicsMermaid-001 | Source: CCEA FA22-FKIN boundary + transcript summary slide | Insert from mermaid/FA22FurtherKinematicsMermaid-001.md | Purpose: Show how to choose the correct kinematics equation depending on whether the given function involves \(t\), \(x\), or \(v\).]` |
| Source | CCEA FA22-FKIN boundary + transcript summary of functions of time, displacement and velocity |
| Purpose | Show how to choose the correct kinematics relation depending on whether the given quantity is a function of \(t\), \(x\), or \(v\). |

## Creation notes

This decision tree supports `FA22-FKIN-LO002`.

It separates the three major straight-line variable acceleration cases:

1. Functions of time:
   \[
   a=f(t),\qquad v=f(t)
   \]
2. Functions of displacement:
   \[
   v=f(x),\qquad a=f(x)
   \]
3. Functions of velocity:
   \[
   a=f(v)
   \]

The key exam decision is not “which formula do I remember?” but:

```text
What is given, and what am I trying to find?
```

For distance and displacement questions involving \(a=f(v)\), the route is usually:

\[
a=v\frac{dv}{dx}.
\]

For velocity and time questions involving \(a=f(v)\), the route is usually:

\[
a=\frac{dv}{dt}.
\]

## Mermaid code

```mermaid
flowchart TD
    A["Start: identify the variable in the given motion quantity"] --> B{"What is the quantity given as a function of?"}

    B --> C["Function of time<br/>Examples: a = f(t), v = f(t)"]
    B --> D["Function of displacement<br/>Examples: v = f(x), a = f(x)"]
    B --> E["Function of velocity<br/>Example: a = f(v)"]
    B --> F["3D vector function<br/>Examples: r(t), v(t), a(t)"]

    C --> C1{"What do you need?"}
    C1 --> C2["Need acceleration from velocity<br/>Use a = dv/dt"]
    C1 --> C3["Need velocity from acceleration<br/>Use v = ∫ a dt + C"]
    C1 --> C4["Need displacement from velocity<br/>Use x = ∫ v dt + C"]
    C1 --> C5["Need distance travelled<br/>Split at v = 0 and add magnitudes"]

    D --> D1{"Which quantity is given?"}
    D1 --> D2["Given v = f(x)<br/>Use dx/dt = f(x)"]
    D2 --> D3["Separate variables<br/>dx / f(x) = dt"]
    D1 --> D4["Given a = f(x)<br/>Use a = v dv/dx"]
    D4 --> D5["Equivalent form<br/>d/dx(1/2 v²) = f(x)"]
    D5 --> D6["Integrate with respect to x<br/>1/2 v² = ∫ f(x) dx + C"]

    E --> E1{"What do you need?"}
    E1 --> E2["Need velocity or time<br/>Use a = dv/dt"]
    E2 --> E3["Separate variables<br/>dv / f(v) = dt"]
    E1 --> E4["Need displacement or distance<br/>Use a = v dv/dx"]
    E4 --> E5["Separate variables<br/>v dv / f(v) = dx"]

    F --> F1["Use componentwise calculus"]
    F1 --> F2["r(t) = x(t)i + y(t)j + z(t)k"]
    F2 --> F3["v(t) = dr/dt"]
    F3 --> F4["a(t) = dv/dt = d²r/dt²"]
    F4 --> F5["When integrating, add vector constants"]

    C2 --> G["Use initial conditions and units"]
    C3 --> G
    C4 --> G
    C5 --> G
    D3 --> G
    D6 --> G
    E3 --> G
    E5 --> G
    F5 --> G

    G --> H["Final check:<br/>distance or displacement?<br/>exact or decimal?<br/>scalar or vector?"]
```
