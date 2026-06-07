# Mermaid Asset: FA22DynamicProgrammingOffSpecEnrichmentMermaid-002

```mermaid
flowchart TD
    A[Read the wording] --> B{What is optimised?}
    B --> C[Minimum total cost or shortest route]
    C --> C1[w(XY)+V(Y)]
    C1 --> C2[Star smallest total]
    B --> D[Maximum total value or profit]
    D --> D1[w(XY)+V(Y)]
    D1 --> D2[Star largest total]
    B --> E[Maximum single arc as small as possible]
    E --> E1[max(w(XY),V(Y))]
    E1 --> E2[Star smallest maximum: minimax]
    B --> F[Minimum single arc as large as possible]
    F --> F1[min(w(XY),V(Y))]
    F1 --> F2[Star largest minimum: maximin]
```
