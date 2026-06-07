# FA22FlowsInNetworksMermaid-001

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | `FA22FlowsInNetworksMermaid-001` |
| Unit | `FA22` |
| Topic code | `FA22-GRAPH` |
| Topic ID | `FA22FlowsInNetworks` |
| Lesson file | `FA22_flows_in_networks_lesson.md` |
| Related lesson sections | Section 8 Core Theory; Section 9 Visual Asset Integration; Section 11 Worked Examples; Section 15 Exam Technique Notes |
| Used placeholder | `[VISUAL PLACEHOLDER: FA22FlowsInNetworksMermaid-001 | Source: CCEA FA22-GRAPH-LO002 + uploaded transcript | Insert from mermaid/FA22FlowsInNetworksMermaid-001.md | Purpose: Show the complete decision route from reading a capacitated directed network to proving maximality using the maximum flow-minimum cut theorem.]` |
| Source | CCEA `FA22-GRAPH-LO002` + uploaded transcript `Chapter 3: Flows in Networks 1` |
| Purpose | Show the complete workflow for solving a flows-in-networks problem. |
| Creation notes | Lesson-navigation diagram, not a replacement for a precise network diagram. |

## Mermaid Diagram

```mermaid
flowchart TD
    A["Start: capacitated directed network"] --> B["Identify source and sink"]
    B --> C["Read each directed arc"]
    C --> D["Record capacity c(e)"]
    C --> E["Record current flow f(e), if supplied"]
    D --> F["Feasibility check"]
    E --> F
    F --> F1{"For every arc, is 0 ≤ f(e) ≤ c(e)?"}
    F1 -- "No" --> F2["Flow is not feasible: repair or reject"]
    F1 -- "Yes" --> G["Conservation check"]
    G --> G1{"At every internal vertex, is flow in = flow out?"}
    G1 -- "No" --> G2["Use conservation equations to find missing values"]
    G2 --> G
    G1 -- "Yes" --> H["Find value of the flow"]
    H --> H1["Flow value = total flow out of source"]
    H --> H2["Also = total flow into sink"]
    H1 --> I["Candidate flow value F"]
    H2 --> I
    I --> J{"Need to improve the flow?"}
    J -- "No, only checking" --> M["Choose a cut or cutset"]
    J -- "Yes" --> K["Use labelling procedure"]
    K --> K1["Forward label = spare capacity = c(e) - f(e)"]
    K --> K2["Backward label = current flow = f(e)"]
    K1 --> K3["Check paired labels add to capacity"]
    K2 --> K3
    K3 --> L{"Is there an augmenting route from source to sink using positive labels?"}
    L -- "Yes" --> L1["Augment by the smallest label on that route"]
    L1 --> L2["Update labels and current flows"]
    L2 --> H
    L -- "No" --> M["Choose a cut or cutset"]
    M --> M1["Separate vertices into source-side set and sink-side set"]
    M1 --> M2["Count arcs crossing from source side to sink side"]
    M2 --> M3["Use capacities, not current flows"]
    M3 --> M4["Cut capacity C"]
    M4 --> N{"Does F = C?"}
    N -- "Yes" --> O["By the max-flow min-cut theorem, the flow is maximal"]
    N -- "No" --> P["Maximality not proven: improve flow or find a smaller cut"]
    O --> Q["Final answer: state maximum flow and supporting cut"]
    P --> J
    R["Special theorem-proof shortcut"] --> R1["Minimum cut may use saturated arcs away from source"]
    R --> R2["It may also use empty arcs towards source"]
    R1 --> M
    R2 --> M

    classDef start fill:#FFFFF0,stroke:#C5A059,color:#2C2C2E,stroke-width:2px;
    classDef process fill:#FAF9F6,stroke:#E5E5EA,color:#2C2C2E,stroke-width:1.5px;
    classDef decision fill:#FBEFEF,stroke:#C5A059,color:#2C2C2E,stroke-width:1.5px;
    classDef theorem fill:#FFF8DC,stroke:#D4AF37,color:#2C2C2E,stroke-width:2px;
    class A start;
    class B,C,D,E,F,G,H,I,K,K1,K2,K3,L1,L2,M,M1,M2,M3,M4,Q,R1,R2 process;
    class F1,G1,J,L,N decision;
    class O theorem;
```
