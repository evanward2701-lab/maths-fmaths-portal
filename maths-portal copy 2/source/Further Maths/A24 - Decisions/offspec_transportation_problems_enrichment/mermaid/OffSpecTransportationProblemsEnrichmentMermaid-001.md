# Mermaid Asset: OffSpecTransportationProblemsEnrichmentMermaid-001

| Field | Value |
|---|---|
| Asset ID | `OffSpecTransportationProblemsEnrichmentMermaid-001` |
| Asset type | Mermaid flowchart |
| Lesson file | `offspec_transportation_problems_enrichment_lesson.md` |
| Related lesson section | Section 9.9 Linear Programming Formulation Map; Section 11 Worked Example 8 |
| Source | Teacher transcript: Transportation Problems 8, Linear programming |
| CCEA status | Off-spec enrichment only |
| Purpose | Show how a transportation table becomes a linear programming formulation. |

```mermaid
flowchart TD
    A["Transportation table"] --> B["Sources / suppliers"]
    A --> C["Destinations / demand points"]
    A --> D["Route costs<br/>c_ij = cost per unit from i to j"]
    A --> E["Supply totals<br/>s_i"]
    A --> F["Demand totals<br/>d_j"]
    B --> G["Decision variables<br/>x_ij = units transported from i to j"]
    C --> G
    D --> H["Objective function<br/>Minimise P = sum c_ij x_ij"]
    G --> H
    E --> I["Supply constraints<br/>sum_j x_ij <= s_i<br/>or = s_i in balanced exact allocation"]
    G --> I
    F --> J["Demand constraints<br/>sum_i x_ij >= d_j<br/>or = d_j when exactly met"]
    G --> J
    G --> K["Non-negativity<br/>x_ij >= 0"]
    H --> L["Complete LP model"]
    I --> L
    J --> L
    K --> L
    M["Off-spec enrichment note<br/>Not a CCEA-core transportation topic"] -.-> L
```

## Accessibility Description

A vertical flowchart starts with the transportation table. It branches into sources, destinations, route costs, supply totals and demand totals. Sources and destinations define route variables. Route costs and variables create the objective function. Supply totals create supply constraints. Demand totals create demand constraints. Non-negativity constraints apply to every variable. These combine into the LP model.
