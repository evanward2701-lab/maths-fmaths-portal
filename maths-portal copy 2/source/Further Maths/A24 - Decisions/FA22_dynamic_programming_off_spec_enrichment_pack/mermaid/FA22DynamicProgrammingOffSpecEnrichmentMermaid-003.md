# Mermaid Asset: FA22DynamicProgrammingOffSpecEnrichmentMermaid-003

```mermaid
flowchart LR
    A[Whole optimal route S-A-E-I-T] --> B[Subroute E-I-T is optimal]
    B --> C[V(E) can be reused]
    C --> D[A uses AE + V(E)]
    D --> E[S uses SA + V(A)]
    F[If a subroute were not optimal] --> G[Replace it with a better subroute]
    G --> H[Whole route improves]
    H --> I[Contradiction]
    I --> C
```
