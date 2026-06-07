# A22NormalDistributionMER-001

## Asset ID
`A22NormalDistributionMER-001`

## Source
CCEA GCE Mathematics Specification Map, `A22-NORMAL-LO003`; Phase 1 lesson sections on distribution choice and binomial-to-normal approximation.

## Related lesson section
`Core Theory Part 6: Binomial-to-Normal Approximation`

## Purpose
Show how to choose between a binomial model, a normal model, a normal approximation to a binomial model, or no simple model.

```mermaid
flowchart TD
    A["Start: read the context carefully"] --> B{"Is the variable a measured continuous quantity?"}
    B -->|Yes| C["Normal model may be appropriate"]
    C --> C1["Check for evidence of approximate symmetry"]
    C1 --> C2["Use X ~ N(mu, sigma^2) if mean and standard deviation are given or can be found"]
    B -->|No| D{"Is the variable a count of successes?"}
    D -->|Yes| E{"Does it satisfy binomial conditions?"}
    E --> E1["Fixed number of trials n"]
    E --> E2["Two outcomes: success or failure"]
    E --> E3["Constant probability p"]
    E --> E4["Independent trials"]
    E1 --> F{"Are all binomial conditions reasonable?"}
    E2 --> F
    E3 --> F
    E4 --> F
    F -->|Yes| G["Use X ~ B(n, p)"]
    G --> H{"Is a normal approximation requested or sensible?"}
    H -->|Yes| I["Approximate by Y ~ N(np, np(1-p))"]
    I --> J["Apply continuity correction before calculating probability"]
    H -->|No| K["Use exact binomial probabilities"]
    F -->|No| L["Do not use binomial without stating limitations"]
    D -->|No| M["No simple binomial or normal model from the given information"]
    C2 --> N["Interpret final probability in context"]
    J --> N
    K --> N
    L --> N
    M --> N
```
