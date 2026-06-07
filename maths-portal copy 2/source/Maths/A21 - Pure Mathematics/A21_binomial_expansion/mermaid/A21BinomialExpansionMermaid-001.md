# A21BinomialExpansionMermaid-001

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | A21BinomialExpansionMermaid-001 |
| Unit | A21 |
| Topic code | A21-SS |
| Topic ID | A21BinomialExpansion |
| Source | CCEA specification map + Chapter 4 Binomial Expansion transcript + reveal-block PDF |
| Related lesson section | Finite to Infinite Binomial Expansion |
| Purpose | Show the conceptual shift from AS finite binomial expansion to A2 infinite rational-power expansion. |

## Mermaid Code

```mermaid
flowchart TD
    A["AS binomial expansion"] --> B["Power n is a positive integer"]
    B --> C["Expansion eventually stops"]
    C --> D["Example: (1 + x)^5"]
    D --> E["1 + 5x + 10x^2 + 10x^3 + 5x^4 + x^5"]
    A --> F["A2 binomial expansion"]
    F --> G["Power n can be rational"]
    G --> H["n may be negative or fractional"]
    H --> I["Expansion usually continues forever"]
    I --> J["Example: (1 + x)^(-1)"]
    J --> K["1 - x + x^2 - x^3 + ..."]
    K --> L["Need a validity condition"]
    L --> M["Usually require |small part| < 1"]
```
