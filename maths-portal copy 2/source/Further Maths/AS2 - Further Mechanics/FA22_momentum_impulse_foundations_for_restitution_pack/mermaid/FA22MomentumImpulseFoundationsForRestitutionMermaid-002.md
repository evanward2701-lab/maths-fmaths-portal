# Mermaid Asset: FA22MomentumImpulseFoundationsForRestitutionMermaid-002

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | `FA22MomentumImpulseFoundationsForRestitutionMermaid-002` |
| Asset type | Mermaid diagram |
| Topic ID | `FA22MomentumImpulseFoundationsForRestitution` |
| Lesson file | `FA22_momentum_impulse_foundations_for_restitution_lesson.md` |
| Related lesson section | Section 9: Visual Asset Integration |
| Used placeholder | `[VISUAL PLACEHOLDER: FA22MomentumImpulseFoundationsForRestitutionMermaid-002 | Source: FM1-Chp1-Momentum.pdf and transcripts.md | Insert from mermaid/FA22MomentumImpulseFoundationsForRestitutionMermaid-002.md | Purpose: Help students choose between \(I=m(v-u)\), \(I=Ft\), and PCLM. Description: The flowchart should begin with “What is asked?” and branch to impulse from velocity change, force-time impulse, conservation of momentum, or vector component method.]` |
| Source | `FM1-Chp1-Momentum.pdf` and `transcripts.md` |
| Purpose | Help students choose the correct method: \(P=mv\), \(I=m(v-u)\), \(I=Ft\), \(Ft=m(v-u)\), PCLM, or vector impulse. |
| Boundary note | This is a bridge/prerequisite method selector for FA22 Restitution readiness. |

## Mermaid Code

```mermaid
flowchart TD
    A["What is the question asking?"] --> B{"Single object<br/>or collision system?"}

    B --> C["Single object"]
    B --> D["Collision system"]

    C --> E{"What information is given?"}
    E --> F["mass and velocity"]
    E --> G["mass, initial velocity,<br/>final velocity"]
    E --> H["force and time"]
    E --> I["force, time, mass,<br/>initial and final velocity"]
    E --> J["vector velocities<br/>using i and j"]

    F --> F1["Use momentum<br/>P = mv"]
    G --> G1["Use impulse<br/>I = m(v - u)"]
    H --> H1["Use force-time impulse<br/>I = Ft"]
    I --> I1["Use impulse-momentum link<br/>Ft = m(v - u)"]
    J --> J1["Use vector impulse<br/>I = m(v - u)<br/>component by component"]

    D --> K{"Is the system isolated<br/>during the impact?"}
    K --> L["Yes"]
    K --> M["No or unclear"]

    L --> N["Use PCLM<br/>m1u1 + m2u2 = m1v1 + m2v2"]
    N --> O{"How many unknown<br/>final velocities?"}
    O --> P["One unknown"]
    O --> Q["Two unknowns"]

    P --> R["PCLM can solve it"]
    Q --> S["PCLM gives one equation only<br/>FA22 Restitution needs another equation"]

    M --> T["Check modelling assumptions<br/>external force may prevent<br/>momentum conservation"]

    U["Always first:<br/>choose a positive direction"] -.-> G1
    U -.-> I1
    U -.-> N

    V["Warning:<br/>speed is magnitude,<br/>velocity needs direction"] -.-> G1
    V -.-> J1

    W["Warning:<br/>if magnitude is asked,<br/>give a positive size"] -.-> G1
    W -.-> J1

    X["Boundary note:<br/>Newton's law of restitution<br/>is not included in this foundation evidence"] -.-> S

    classDef question fill:#FAF9F6,stroke:#E5E5EA,color:#2C2C2E;
    classDef method fill:#FFFFF0,stroke:#D4AF37,color:#2C2C2E;
    classDef warning fill:#FFF7E6,stroke:#C5A059,color:#2C2C2E,stroke-dasharray: 5 3;
    classDef further fill:#FBEFEF,stroke:#C5A059,color:#2C2C2E;

    class A,B,E,K,O question;
    class F1,G1,H1,I1,J1,N,R method;
    class U,V,W,T,X warning;
    class S further;
```
