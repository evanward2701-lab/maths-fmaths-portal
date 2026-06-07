# AS2DataPresentationMERMAID-007

**Asset ID:** AS2DataPresentationMERMAID-007  
**Source:** Histogram gaps evidence  
**Related lesson section:** Core Theory, Gaps and True Class Widths  
**Purpose:** Show how rounded classes and gaps affect true class boundaries and histogram widths.

```mermaid
flowchart TD
    A[Class intervals shown with gaps] --> B{Are values rounded?}
    B -->|Yes| C[Convert to true class boundaries]
    B -->|No| D[Use stated class boundaries]
    C --> E[Example: 1 to 2 becomes 0.5 to 2.5]
    E --> F[Class width = upper true boundary - lower true boundary]
    D --> F
    F --> G[Use class width for histogram bar width]
    G --> H[Use area proportional to frequency]
    H --> I[Find missing frequency or bar height]
    I --> J[Check adjacent true intervals meet with no artificial gaps]
```
