# AS1DifferentiationMERMAID-009

## Asset Metadata

- Asset ID: `AS1DifferentiationMERMAID-009`
- Asset type: Mermaid flowchart
- Source: CCEA AS1-DIFF boundary + A21 differentiation boundary comparison
- Related lesson section: Syllabus Gap Check; Off-Spec Content Found but Excluded
- Purpose: Make the AS1 boundary explicit by separating allowed AS1 methods from later A2 methods.
- Status: Final

```mermaid
flowchart TD
    A["Differentiation method needed"] --> B{"Can expression be rewritten as sums/differences of ax^n?"}
    B --> C["Yes"]
    C --> D["AS1 core method"]
    D --> E["Use power rule"]
    E --> F["Differentiate rational powers, constants, sums and differences"]
    B --> G["No"]
    G --> H{"Would it need product, quotient or chain rule?"}
    H --> I["Yes"]
    I --> J["Not AS1 core for this lesson"]
    J --> K["Log as off-spec or future A2 content"]
    H --> L{"Can algebra avoid the advanced rule?"}
    L --> M["Yes"]
    M --> N["Rewrite first, then use AS1 method"]
    L --> O["No"]
    O --> P["Do not include as required core content"]
    K --> Q["Keep lesson aligned to CCEA AS1-DIFF"]
    P --> Q
    F --> Q
    N --> Q
```
