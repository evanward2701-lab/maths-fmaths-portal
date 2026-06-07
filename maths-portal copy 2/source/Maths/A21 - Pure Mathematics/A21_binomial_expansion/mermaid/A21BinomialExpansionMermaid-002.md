# A21BinomialExpansionMermaid-002

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | A21BinomialExpansionMermaid-002 |
| Unit | A21 |
| Topic code | A21-SS |
| Topic ID | A21BinomialExpansion |
| Source | CCEA specification map + Chapter 4 Binomial Expansion transcript + reveal-block PDF |
| Related lesson section | Coefficient Pattern |
| Purpose | Show the coefficient-building pattern used for rational, negative and fractional powers. |

## Mermaid Code

```mermaid
flowchart LR
    A["Start with (1 + u)^n"] --> B["First term: 1"]
    B --> C["Second term: n u"]
    C --> D["Third term: n(n - 1)/2! times u^2"]
    D --> E["Fourth term: n(n - 1)(n - 2)/3! times u^3"]
    E --> F["Fifth term: n(n - 1)(n - 2)(n - 3)/4! times u^4"]
    F --> G["Continue the pattern"]
    H["Key habit"] --> I["Each new numerator factor subtracts one more"]
    H --> J["Denominator uses matching factorial"]
    H --> K["Power of u increases each time"]
```
