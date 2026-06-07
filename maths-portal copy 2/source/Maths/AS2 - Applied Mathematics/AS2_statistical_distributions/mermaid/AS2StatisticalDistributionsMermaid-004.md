# AS2StatisticalDistributionsMermaid-004

**Asset ID:** AS2StatisticalDistributionsMermaid-004  
**Source:** Slide/transcript evidence on cumulative binomial probability transformations  
**Related lesson section:** Core Theory 8.6, Worked Examples 10-13, Exam Technique Notes  
**Purpose:** Give a clean conversion map for turning probability wording into calculator/table-friendly cumulative form.

```mermaid
flowchart TD
    A["Probability expression"] --> B{"Already P(X <= a)?"}
    B -- "Yes" --> C["Use binomial CD directly"]
    B -- "No" --> D{"Strict less than?"}
    D -- "P(X < a)" --> E["Rewrite as P(X <= a - 1)"]
    D -- "No" --> F{"At least / greater than or equal?"}
    F -- "P(X >= a)" --> G["Rewrite as 1 - P(X <= a - 1)"]
    F -- "No" --> H{"Greater than?"}
    H -- "P(X > a)" --> I["Rewrite as 1 - P(X <= a)"]
    H -- "No" --> J{"Exact value?"}
    J -- "P(X = a)" --> K["Rewrite as P(X <= a) - P(X <= a - 1)"]
    J -- "No" --> L{"Range?"}
    L -- "P(a < X <= b)" --> M["Rewrite as P(X <= b) - P(X <= a)"]
    L -- "P(a <= X <= b)" --> N["Rewrite as P(X <= b) - P(X <= a - 1)"]
    L -- "Other" --> O["Check endpoints carefully before using CD"]
```
