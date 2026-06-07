# A21BinomialExpansionMermaid-007

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | A21BinomialExpansionMermaid-007 |
| Unit | A21 |
| Topic code | A21-SS |
| Topic ID | A21BinomialExpansion |
| Source | CCEA specification map + Chapter 4 Binomial Expansion transcript + reveal-block PDF |
| Related lesson section | Approximation Workflow |
| Purpose | Show how a binomial expansion is used to approximate a surd such as sqrt(2) or sqrt(6). |

## Mermaid Code

```mermaid
flowchart TD
    A["Given expansion"] --> B["Choose or use supplied value of x"]
    B --> C["Substitute x into the original expression"]
    C --> D["Simplify the left-hand side"]
    D --> E{"Does it equal the target surd?"}
    E -- "Yes" --> F["Use right-hand side as approximation"]
    E -- "No" --> G["Rearrange to isolate target surd"]
    F --> H["Substitute x into truncated expansion"]
    G --> H
    H --> I["Simplify exact fractions carefully"]
    I --> J["Obtain p/q or decimal approximation"]
    J --> K["Check validity condition"]
    K --> L{"Is x inside valid range?"}
    L -- "Yes" --> M["Approximation is valid"]
    L -- "No" --> N["Do not use the approximation"]
```
