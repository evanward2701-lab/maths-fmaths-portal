# AS2StatisticalDistributionsMermaid-002

**Asset ID:** AS2StatisticalDistributionsMermaid-002  
**Source:** Teacher transcript section on binomial distribution conditions  
**Related lesson section:** Core Theory 8.4, Common Mistakes and Exam Traps  
**Purpose:** Give students a decision tree for whether a binomial model is appropriate.

```mermaid
flowchart TD
    A["Context question"] --> B{"Fixed number of trials n?"}
    B -- "No" --> X["Not binomial"]
    B -- "Yes" --> C{"Exactly two outcomes?"}
    C -- "No" --> X
    C -- "Yes" --> D{"Fixed probability of success p?"}
    D -- "No" --> X
    D -- "Yes" --> E{"Independent trials?"}
    E -- "No" --> X
    E -- "Yes" --> F["Binomial model is suitable"]
    F --> G["Define success clearly"]
    G --> H["Let X = number of successes"]
    H --> I["Write X ~ B(n, p)"]
    I --> J["Use binomial formula or calculator"]
```
