---
asset_id: FAS2RecurrenceRelationshipsMermaid-001
asset_type: Mermaid
unit_code: FAS2
topic_code: FAS2-REC
topic_name: Recurrence relationships
topic_slug: recurrence_relationships
topic_pascal: RecurrenceRelationships
topic_id: FAS2RecurrenceRelationships
lesson_file: FAS2_recurrence_relationships_lesson.md
related_lesson_section: "Section 9.1 Recurrence route map"
source: "CCEA Further Mathematics specification map + teacher transcript evidence"
purpose: "Show the route from recurrence model to closed form, including generation, verification, first-order solving and second-order solving."
status: "Generated in Phase 2"
---

# FAS2RecurrenceRelationshipsMermaid-001

```mermaid
flowchart TD
    A["Recurrence relationships<br/>FAS2-REC"] --> B["Core model structure"]
    B --> C["Recurrence relation<br/>plus initial condition(s)"]
    C --> D["Define variables<br/>u_n, n, units/context"]
    C --> E["Generate terms recursively"]
    C --> F["Verify a proposed closed form"]
    C --> G["Solve for a closed form"]
    C --> H["Interpret or criticise model"]

    E --> E1["Example route:<br/>u_{n+1}=u_n+3, u_0=3"]
    E1 --> E2["u_1=3+3=6"]
    E2 --> E3["u_2=6+3=9"]
    E3 --> E4["Sequence begins:<br/>3, 6, 9, ..."]

    F --> F1["Write u_{n-1}<br/>or u_{n-2} if needed"]
    F1 --> F2["Substitute into recurrence"]
    F2 --> F3["Simplify"]
    F3 --> F4["Show result equals given u_n"]

    G --> I{"Classify recurrence"}
    I --> J["First-order homogeneous<br/>u_n = a u_{n-1}"]
    J --> J1["u_n = C a^n"]
    J1 --> J2["Use initial condition<br/>to find C"]

    I --> K["First-order non-homogeneous<br/>u_n = a u_{n-1}+g(n)"]
    K --> K1{"Is a = 1?"}
    K1 -->|Yes| K2["u_n = u_0 + Σ g(r)<br/>from r=1 to n"]
    K1 -->|No| K3["Complementary function C a^n<br/>plus particular solution"]
    K3 --> K4["Use initial condition"]

    I --> L["Second-order homogeneous<br/>u_n = a u_{n-1}+b u_{n-2}"]
    L --> L1["Auxiliary equation<br/>r^2 - ar - b = 0"]
    L1 --> L2{"Root type"}
    L2 -->|Distinct roots α, β| L3["u_n = A α^n + B β^n"]
    L2 -->|Repeated root α| L4["u_n = (A + Bn) α^n"]
    L2 -->|Complex roots| L5["u_n = R^n(A cos nθ + B sin nθ)"]

    L --> M["Fibonacci-type relation<br/>F_n = F_{n-1}+F_{n-2}"]
    M --> M1["r^2-r-1=0"]

    H --> H1["Check assumptions and limitations"]
    H1 --> H2["negative loan balance,<br/>ambiguous timing,<br/>unlimited growth"]

    style A fill:#FAF9F6,stroke:#C5A059,color:#2C2C2E
    style C fill:#FFFFF0,stroke:#D4AF37,color:#2C2C2E
    style G fill:#FBEFEF,stroke:#C5A059,color:#2C2C2E
    style I fill:#FAF9F6,stroke:#D4AF37,color:#2C2C2E
    style L1 fill:#FFFFF0,stroke:#C5A059,color:#2C2C2E
```

## Accessibility description

A top-down flowchart beginning with the core structure recurrence relation plus initial conditions. It branches to generating terms, verifying a closed form, solving first-order relations, solving second-order homogeneous relations, Fibonacci-type relations, and model criticism.
