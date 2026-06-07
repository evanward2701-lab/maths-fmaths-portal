# A21BinomialExpansionMermaid-006

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | A21BinomialExpansionMermaid-006 |
| Unit | A21 |
| Topic code | A21-SS |
| Topic ID | A21BinomialExpansion |
| Source | CCEA specification map + Chapter 4 Binomial Expansion transcript + reveal-block PDF |
| Related lesson section | Partial Fractions Workflow |
| Purpose | Show the workflow from rational expression to partial fractions to separate binomial expansions. |

## Mermaid Code

```mermaid
flowchart TD
    A["Start with rational expression"] --> B["Check if direct binomial expansion is possible"]
    B -- "Not directly" --> C["Decompose into partial fractions"]
    C --> D["Find constants A, B, C as needed"]
    D --> E["Rewrite each fraction in binomial form"]
    E --> F["Examples: (1 + x)^(-1), (1 - x/2)^(-1)"]
    F --> G["Expand each part separately"]
    G --> H["Apply outside multipliers"]
    H --> I["Add or subtract expansions term by term"]
    I --> J["Collect constant, x, x^2, x^3 terms"]
    J --> K["State cubic or required approximation"]
    K --> L["Find validity for each separate expansion"]
    L --> M["Use the overlap of all valid ranges"]
    M --> N["State final range"]
```
