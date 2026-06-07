# AS2StatisticalDistributionsMermaid-003

**Asset ID:** AS2StatisticalDistributionsMermaid-003  
**Source:** Transcript explanation linking combinations, binomial coefficients and repeated trials  
**Related lesson section:** Core Theory 8.5, Worked Example 3, Worked Example 5  
**Purpose:** Show how the binomial formula comes from tree/path counting.

```mermaid
flowchart TD
    A["n repeated trials"] --> B["Each trial has success probability p"]
    A --> C["Each trial has failure probability 1 - p"]
    B --> D["Want exactly r successes"]
    C --> E["Then there are n - r failures"]
    D --> F["Probability of successes: p^r"]
    E --> G["Probability of failures: (1-p)^(n-r)"]
    F --> H["One specific order"]
    G --> H
    H --> I["Probability for one order: p^r(1-p)^(n-r)"]
    D --> J["Count how many orders give r successes"]
    J --> K["Use nCr"]
    K --> L["Number of orders = nCr"]
    I --> M["Multiply one-order probability by number of orders"]
    L --> M
    M --> N["P(X = r) = nCr p^r(1-p)^(n-r)"]
```
