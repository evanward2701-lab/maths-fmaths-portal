# FAS2CriticalPathAnalysisMermaid-001

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | FAS2CriticalPathAnalysisMermaid-001 |
| Asset type | Mermaid diagram |
| Unit | FAS2: Further AS 2 Applied Mathematics |
| Applied section | Section D: Discrete and Decision Mathematics |
| Topic code | FAS2-ALGGRAPH |
| Topic name | Critical Path Analysis |
| Topic ID | FAS2CriticalPathAnalysis |
| Related lesson file | FAS2_critical_path_analysis_lesson.md |
| Related lesson section | Section 9: Visual Asset Integration |
| Used placeholder | `[VISUAL PLACEHOLDER: FAS2CriticalPathAnalysisMermaid-001 | Source: CCEA FAS2 critical path analysis LO + uploaded CPA slides/transcript | Insert from mermaid/FAS2CriticalPathAnalysisMermaid-001.md | Purpose: Show the overall critical path analysis workflow from project activities to precedence table, activity network, event times, float and critical path.]` |
| Source | CCEA FAS2 critical path analysis LO + uploaded CPA slides/transcript |
| Purpose | Show the overall CPA workflow. |
| Status | Written file. |

```mermaid
flowchart TD
    A["Project to plan"] --> B["Split project into activities A, B, C, ..."]
    B --> C["Identify dependencies"]
    C --> D["Build precedence table"]
    D --> Dwarn["Warning: immediate predecessors only"]
    D --> E["Draw activity-on-arc network"]
    E --> F["Arcs = activities<br/>Nodes = events"]
    F --> G["Add source and sink"]
    G --> H{"Need dummy?"}
    H -- "No" --> I["Add durations"]
    H -- "Yes" --> J["Insert dotted dummy<br/>duration 0"]
    J --> I
    I --> K["Forward pass"]
    K --> Kcalc["Add durations<br/>choose largest incoming"]
    Kcalc --> L["Backward pass"]
    L --> Lcalc["Subtract durations<br/>choose smallest outgoing-back"]
    Lcalc --> M["Calculate float"]
    M --> Mformula["float = L_j - d - E_i"]
    Mformula --> N{"Float = 0?"}
    N -- "Yes" --> O["Critical activity"]
    N -- "No" --> P["Non-critical activity"]
    O --> Q["Trace source to sink"]
    P --> Q
    Q --> R["State critical path"]
    R --> S["State project duration"]
    R --> Rwarn["Check E_i + d = E_j"]
    classDef start fill:#FAF9F6,stroke:#C5A059,color:#2C2C2E,stroke-width:2px;
    classDef process fill:#FFFFF0,stroke:#E5E5EA,color:#2C2C2E,stroke-width:1.5px;
    classDef warning fill:#FBEFEF,stroke:#C5A059,color:#2C2C2E,stroke-width:1.5px;
    class A start;
    class B,C,D,E,F,G,I,K,L,M,Q,R,S process;
    class Dwarn,Kcalc,Lcalc,Mformula,Rwarn warning;
```
