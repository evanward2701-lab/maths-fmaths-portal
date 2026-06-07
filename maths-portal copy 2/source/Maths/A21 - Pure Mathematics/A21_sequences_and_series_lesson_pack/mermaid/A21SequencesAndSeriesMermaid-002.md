# A21SequencesAndSeriesMermaid-002

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | A21SequencesAndSeriesMermaid-002 |
| Unit code | A21 |
| Topic code | A21-SS |
| Related lesson section | Modelling with sequences and series |
| Purpose | Modelling decision tree. |

```mermaid
flowchart TD
    A[Start: modelling question] --> B[Identify what changes]
    B --> C{How does it change?}
    C -->|Fixed amount| D[Arithmetic model]
    D --> D1[u_n = a + (n - 1)d]
    D --> D2[S_n = n/2(2a + (n - 1)d)]
    C -->|Fixed percentage| E[Geometric model]
    E --> E1[Increase p%: r = 1 + p/100]
    E --> E2[Decrease p%: r = 1 - p/100]
    E --> E3[u_n = ar^(n - 1)]
    E --> E4[S_n = a(1 - r^n)/(1 - r)]
    C -->|Uses previous term| F[Recurrence model]
    F --> F1[Generate terms and look for cycles]
    D1 --> G[Interpret in context]
    D2 --> G
    E3 --> G
    E4 --> G
    F1 --> G
    G --> H[State limitation if asked]
```
