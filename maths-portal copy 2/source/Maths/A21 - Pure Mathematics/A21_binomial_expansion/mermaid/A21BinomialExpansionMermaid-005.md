# A21BinomialExpansionMermaid-005

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | A21BinomialExpansionMermaid-005 |
| Unit | A21 |
| Topic code | A21-SS |
| Topic ID | A21BinomialExpansion |
| Source | CCEA specification map + Chapter 4 Binomial Expansion transcript + reveal-block PDF |
| Related lesson section | Combining Expansions |
| Purpose | Show how to multiply two binomial expansions and keep only the required powers of x. |

## Mermaid Code

```mermaid
flowchart TD
    A["Start with a quotient or product"] --> B["Rewrite as product of binomial factors"]
    B --> C["Example: ((1 + x)/(1 - x))^(1/2)"]
    C --> D["= (1 + x)^(1/2)(1 - x)^(-1/2)"]
    D --> E["Decide highest power needed"]
    E --> F["If working to x^2, expand each factor to x^2"]
    F --> G["Multiply the truncated expansions"]
    G --> H{"Product term power?"}
    H -- "x^0, x^1 or x^2" --> I["Keep the term"]
    H -- "x^3 or higher" --> J["Ignore for this approximation"]
    I --> K["Collect like powers"]
    J --> K
    K --> L["State final expansion"]
    L --> M["Combine validity conditions"]
    M --> N["Use the stricter range"]
```
