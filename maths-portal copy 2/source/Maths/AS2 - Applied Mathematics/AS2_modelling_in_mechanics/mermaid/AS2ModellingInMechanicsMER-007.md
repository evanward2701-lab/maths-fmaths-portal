# AS2ModellingInMechanicsMER-007

## Asset metadata

- asset_id: AS2ModellingInMechanicsMER-007
- lesson_id: AS2ModellingInMechanics
- related_placeholder: AS2ModellingInMechanicsSVG-007
- source: MechYr1-Chp8-Introduction.pdf, pages 7 to 8; transcript scalar-to-vector examples
- related lesson section: Worked Examples
- purpose: Show the process for converting magnitude and direction into vector components.

```mermaid
flowchart TD
    A["Magnitude and angle given"] --> B["Draw a right-angled component triangle"]
    B --> C["Identify side adjacent to angle"]
    B --> D["Identify side opposite angle"]
    C --> C1["Adjacent component = magnitude cos theta"]
    D --> D1["Opposite component = magnitude sin theta"]
    C1 --> E["Decide signs"]
    D1 --> E
    E --> E1["Right is positive"]
    E --> E2["Up is positive"]
    E --> E3["Left is negative"]
    E --> E4["Down is negative"]
    E1 --> F["Write vector form"]
    E2 --> F
    E3 --> F
    E4 --> F
    F --> G["Column vector or i, j form"]
```
