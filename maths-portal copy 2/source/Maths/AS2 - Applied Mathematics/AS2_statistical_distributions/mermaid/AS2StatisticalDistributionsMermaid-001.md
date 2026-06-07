# AS2StatisticalDistributionsMermaid-001

**Asset ID:** AS2StatisticalDistributionsMermaid-001  
**Source:** CCEA AS2-DIST specification map + DrFrostMaths Chapter 6 overview  
**Related lesson section:** Big Picture Explanation, Core Theory  
**Purpose:** Show the learning route from random variables to binomial probabilities and cumulative probabilities.

```mermaid
flowchart TD
    A["Start: statistical distributions"] --> B["Random variable X"]
    B --> C["Possible outcomes x"]
    C --> D["Assign each outcome a probability P(X = x)"]
    D --> E["Discrete probability distribution"]
    E --> F{"How is the distribution represented?"}
    F --> G["Table form"]
    F --> H["Function form p(x)"]
    F --> I["Graphical form"]
    E --> J["Special example: discrete uniform distribution"]
    J --> K["All outcomes have equal probability"]
    E --> L["Main AS2 model: binomial distribution"]
    L --> M["Check binomial conditions"]
    M --> N["Write X ~ B(n, p)"]
    N --> O["Exact probability: P(X = r)"]
    O --> P["Use binomial formula"]
    P --> Q["P(X = r) = nCr p^r (1-p)^(n-r)"]
    N --> R["Cumulative probability"]
    R --> S["Use P(X <= r), complements, tables or calculator"]
    S --> T["Interpret probability in context"]
```
