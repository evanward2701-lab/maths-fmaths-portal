# A21BinomialExpansionMermaid-003

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | A21BinomialExpansionMermaid-003 |
| Unit | A21 |
| Topic code | A21-SS |
| Topic ID | A21BinomialExpansion |
| Source | CCEA specification map + Chapter 4 Binomial Expansion transcript + reveal-block PDF |
| Related lesson section | Validity Decision Flow |
| Purpose | Show how to decide the validity condition for an infinite binomial expansion. |

## Mermaid Code

```mermaid
flowchart TD
    A["Expression to expand"] --> B{"Is it in the form (1 + u)^n?"}
    B -- "Yes" --> C["Identify u"]
    C --> D["Require |u| < 1"]
    D --> E["Solve the inequality"]
    E --> F["State final range clearly"]
    B -- "No" --> G{"Is it in the form (a + bx)^n?"}
    G -- "Yes" --> H["Factor out a"]
    H --> I["(a + bx)^n = a^n(1 + bx/a)^n"]
    I --> J["Small part is bx/a"]
    J --> K["Require |bx/a| < 1"]
    K --> F
    G -- "No" --> L["Rewrite first, or use partial fractions if rational"]
    L --> C
    F --> M["Check endpoints are excluded"]
    M --> N["No equality signs in validity interval"]
```
