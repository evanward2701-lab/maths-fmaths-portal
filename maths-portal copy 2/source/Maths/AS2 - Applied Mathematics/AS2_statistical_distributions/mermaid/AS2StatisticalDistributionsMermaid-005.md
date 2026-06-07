# AS2StatisticalDistributionsMermaid-005

**Asset ID:** AS2StatisticalDistributionsMermaid-005  
**Source:** Transcript calculator guidance for binomial probability distribution and cumulative distribution  
**Related lesson section:** Exam Technique Notes  
**Purpose:** Help students choose between exact binomial probability mode and cumulative binomial mode.

```mermaid
flowchart TD
    A["Binomial probability question"] --> B{"What type of probability?"}
    B -- "Exact value P(X = r)" --> C["Use Binomial PD"]
    C --> D["Enter n, p, x = r"]
    D --> E["Calculator gives P(X = r)"]
    B -- "Cumulative P(X <= r)" --> F["Use Binomial CD"]
    F --> G["Enter n, p, x = r"]
    G --> H["Calculator gives P(X <= r)"]
    B -- "Upper tail P(X >= r)" --> I["Use complement first"]
    I --> J["P(X >= r) = 1 - P(X <= r - 1)"]
    J --> F
    B -- "Strict upper tail P(X > r)" --> K["Use complement first"]
    K --> L["P(X > r) = 1 - P(X <= r)"]
    L --> F
    B -- "Range" --> M["Convert to difference of cumulative probabilities"]
    M --> N["Example: P(a < X <= b) = P(X <= b) - P(X <= a)"]
    N --> F
```
