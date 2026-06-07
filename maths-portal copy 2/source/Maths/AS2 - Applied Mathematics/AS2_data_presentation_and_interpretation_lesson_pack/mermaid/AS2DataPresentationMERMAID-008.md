# AS2DataPresentationMERMAID-008

**Asset ID:** AS2DataPresentationMERMAID-008  
**Source:** Width and height of histogram bars evidence  
**Related lesson section:** Worked Examples 15 and 16  
**Purpose:** Show the method for finding the drawn width and drawn height of a histogram bar from a known bar.

```mermaid
flowchart TD
    A[Known histogram bar] --> B[Record drawn width and drawn height]
    B --> C[Calculate known drawn area]
    C --> D[Match known drawn width to known class width]
    D --> E[Find scale from class width to drawn width]
    E --> F[Use scale to find new drawn width]
    C --> G[Match known drawn area to known frequency]
    G --> H[Find area-frequency scale]
    H --> I[Use new frequency to find required drawn area]
    F --> J[Use area = width times height]
    I --> J
    J --> K[New height = required drawn area / new drawn width]
    K --> L[State width and height clearly with units]
```
