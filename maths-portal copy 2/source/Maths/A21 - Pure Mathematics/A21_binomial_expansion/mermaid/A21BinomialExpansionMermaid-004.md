# A21BinomialExpansionMermaid-004

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | A21BinomialExpansionMermaid-004 |
| Unit | A21 |
| Topic code | A21-SS |
| Topic ID | A21BinomialExpansion |
| Source | CCEA specification map + Chapter 4 Binomial Expansion transcript + reveal-block PDF |
| Related lesson section | Constant Not One Workflow |
| Purpose | Show the method for rewriting expressions such as (4 + x)^(1/2). |

## Mermaid Code

```mermaid
flowchart TD
    A["Start: (a + bx)^n"] --> B["Factor out a from the bracket"]
    B --> C["a + bx = a(1 + bx/a)"]
    C --> D["Raise both factors to power n"]
    D --> E["(a + bx)^n = a^n(1 + bx/a)^n"]
    E --> F["Expand (1 + bx/a)^n"]
    F --> G["Multiply every term by a^n"]
    G --> H["State validity: |bx/a| < 1"]
    I["Example"] --> J["(4 + x)^(1/2)"]
    J --> K["= 4^(1/2)(1 + x/4)^(1/2)"]
    K --> L["= 2(1 + x/4)^(1/2)"]
    L --> M["Valid when |x/4| < 1"]
    M --> N["So |x| < 4"]
```
