# A21IntegrationMermaid-002

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | A21IntegrationMermaid-002 |
| Asset type | Mermaid flowchart |
| Lesson | A21 Integration |
| Related section | Separable Differential Equations |
| Source | CCEA A21-INT-LO006/LO007 |
| Purpose | Show separable differential-equation workflow. |

```mermaid
flowchart TD
    A["Differential equation"] --> B{"Can variables separate?"}
    B -- No --> X["Do not force the method"]
    B -- Yes --> C["Move y/V terms to one side"]
    C --> D["Move x/t terms to other side"]
    D --> E["Write differentials clearly"]
    E --> F["Integrate both sides"]
    F --> G{"Logarithm appears?"}
    G -- Yes --> H["Use modulus where needed"]
    G -- No --> I["Continue"]
    H --> J["Add constant"]
    I --> J
    J --> K{"Need exponentiation?"}
    K -- Yes --> L["Exponentiate and combine e^C into A"]
    K -- No --> M["Write general solution"]
    L --> M
    M --> N{"Initial condition?"}
    N -- Yes --> O["Substitute values and find constant"]
    N -- No --> P["Leave general solution"]
    O --> Q["Particular solution"]
    Q --> R{"Context?"}
    P --> R
    R -- Yes --> S["Interpret and state limitations"]
    R -- No --> T["Final mathematical answer"]
```
