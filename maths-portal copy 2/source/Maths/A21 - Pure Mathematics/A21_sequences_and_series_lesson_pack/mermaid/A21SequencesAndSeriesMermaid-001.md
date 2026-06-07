# A21SequencesAndSeriesMermaid-001

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | A21SequencesAndSeriesMermaid-001 |
| Unit code | A21 |
| Topic code | A21-SS |
| Related lesson section | Exam Technique Summary |
| Purpose | Formula-selection flowchart. |

```mermaid
flowchart TD
    A[Start: read the question] --> B{One term or sum?}
    B -->|One term| C{Arithmetic, geometric or recurrence?}
    C -->|Arithmetic| D[Use u_n = a + (n - 1)d]
    C -->|Geometric| E[Use u_n = ar^(n - 1)]
    C -->|Recurrence| F[Generate terms from the starting value]
    B -->|Finite sum| G{Arithmetic, geometric, sigma or recurrence?}
    G -->|Arithmetic| H[Use S_n = n/2(2a + (n - 1)d) or n/2(a + L)]
    G -->|Geometric| I[Use S_n = a(1 - r^n)/(1 - r)]
    G -->|Sigma| J[Expand, count terms, identify structure]
    G -->|Recurrence| K[Find block, sum block, count leftovers]
    B -->|Sum to infinity| L{Geometric and |r| < 1?}
    L -->|Yes| M[Use S_infinity = a/(1 - r)]
    L -->|No| N[No finite sum to infinity]
```
