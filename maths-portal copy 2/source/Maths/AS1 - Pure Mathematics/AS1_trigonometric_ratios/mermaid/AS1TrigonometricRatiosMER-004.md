# AS1TrigonometricRatiosMER-004

Source: P1-Chp9-TrigonometricRatios.pdf pp.13-18  
Related section: Sine Rule and Ambiguous Case  
Purpose: Workflow for sine rule, including the second possible angle.

```mermaid
flowchart TD
    A[Sine rule problem] --> B[Mark opposite angle-side pairs]
    B --> C{Missing side or angle?}
    C -->|Side| D[Use a / sin A = b / sin B]
    C -->|Angle| E[Use sin A / a = sin B / b]
    E --> F[Use inverse sine]
    F --> G{Could angle be obtuse?}
    G -->|No| H[Use calculator angle]
    G -->|Yes| I[Use 180 degrees - calculator angle]
    H --> J[Check triangle angle sum]
    I --> J
```
