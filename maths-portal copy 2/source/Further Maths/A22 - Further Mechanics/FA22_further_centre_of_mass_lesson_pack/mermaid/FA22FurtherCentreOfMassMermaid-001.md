# Mermaid Asset: FA22FurtherCentreOfMassMermaid-001

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | FA22FurtherCentreOfMassMermaid-001 |
| Asset type | Mermaid diagram |
| Unit | FA22: Further A2 2 Applied Mathematics |
| Applied section | Section B: Mechanics 2 |
| Topic code | FA22-FCOM |
| Topic name | Further centre of mass |
| Topic ID | FA22FurtherCentreOfMass |
| Related lesson file | FA22_further_centre_of_mass_lesson.md |
| Related lesson section | # 9. Visual Asset Integration; # 6. Big Picture Explanation; # 8. Core Theory |
| Used placeholder | `[VISUAL PLACEHOLDER: FA22FurtherCentreOfMassMermaid-001 | Source: CCEA FA22-FCOM specification boundary + teacher transcript overview | Insert from mermaid/FA22FurtherCentreOfMassMermaid-001.md | Purpose: Show how the topic grows from ordinary moments and integration into laminae, solids, composite bodies, suspended bodies, sliding and toppling.]` |
| Source | CCEA FA22-FCOM specification boundary + teacher transcript overview |
| Purpose | Show how ordinary A-Level Maths ideas grow into FA22 Further Centre of Mass methods, while marking the key syllabus boundary that banked corners belong elsewhere. |
| Creation status | Generated in Phase 2 |

## Mermaid Code

```mermaid
flowchart TD
    A["Ordinary A-Level Maths foundations"] --> B["A21/A2 Integration<br/>Definite integrals, areas, exact algebra"]
    A --> C["A22 Moments<br/>Moment of force = force × distance"]
    A --> D["A21 Volumes of Revolution<br/>Volume from rotating a curve"]
    A --> E["AS2/A2 Forces and Friction<br/>R, F, μ, limiting equilibrium"]

    B --> F["Further upgrade:<br/>Integrals become sums of mass elements"]
    C --> G["Further upgrade:<br/>Moment of mass = mass × distance<br/>because g cancels"]
    D --> H["Further upgrade:<br/>Thin discs become mass elements"]
    E --> I["Further upgrade:<br/>Rigid-body stability needs geometry, not just forces"]

    F --> J["FA22-FCOM Core Idea<br/>M x̄ = sum of mass moments<br/>M ȳ = sum of mass moments"]
    G --> J
    H --> J
    I --> J

    J --> K["Laminae using calculus<br/>M = ∫ y dx<br/>M x̄ = ∫ xy dx<br/>M ȳ = 1/2 ∫ y² dx"]
    K --> L["Laminae between curves<br/>M = ∫(y₁ - y₂) dx<br/>strip centre height = 1/2(y₁ + y₂)"]
    J --> M["Solids using volumes of revolution<br/>M proportional to ∫ y² dx<br/>M x̄ proportional to ∫ xy² dx"]
    M --> N["Standard solid proofs<br/>solid cone<br/>solid hemisphere"]
    J --> O["Composite bodies<br/>component mass ratios<br/>mass-moment tables<br/>removed pieces as negative mass"]
    O --> P["Non-uniform bodies<br/>include density law inside dm"]
    J --> Q["Suspended bodies<br/>centre of mass lies vertically below suspension point"]
    Q --> R["Use geometry and trigonometry<br/>draw 2D cross-section<br/>label P, G, and vertical"]
    J --> S["Sliding and toppling"]
    S --> T["Sliding test<br/>F ≤ μR<br/>F = μR only at limiting sliding"]
    S --> U["Toppling test<br/>line of action of weight passes through edge at limiting toppling"]
    T --> V["Compare thresholds<br/>slides first, topples first, or simultaneous"]
    U --> V
    W["Boundary warning<br/>Banked corners belong to FA22-FCM,<br/>not FA22-FCOM"]:::warning
    S -. "do not merge topics" .-> W
    classDef warning fill:#FBEFEF,stroke:#C5A059,color:#2C2C2E,stroke-width:2px;
```

## Accessibility Description

This flowchart begins with ordinary A-Level Maths foundations: integration, moments, volumes of revolution, and forces/friction. Each foundation points to a Further Mechanics upgrade. These upgrades combine into the core centre-of-mass equation. From there, the diagram branches into laminae, solids, composite bodies, non-uniform bodies, suspended bodies, and sliding/toppling. A warning box states that banked corners belong to `FA22-FCM`, not `FA22-FCOM`.
