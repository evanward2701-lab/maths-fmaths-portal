# AS2ModellingInMechanicsMER-009

## Asset metadata

- asset_id: AS2ModellingInMechanicsMER-009
- lesson_id: AS2ModellingInMechanics
- related_placeholder: teaching enhancement
- source: MechYr1-Chp8-Introduction.pdf, page 9; transcript modelling with vectors section
- related lesson section: Worked Example 7
- purpose: Show the difference between resultant displacement and total distance travelled.

```mermaid
flowchart TD
    A["Journey from A to B to C"] --> B["Displacement AB = 6i + 4j"]
    A --> C["Displacement BC = 5i - 12j"]
    B --> D["Resultant displacement AC"]
    C --> D
    D --> E["AC = AB + BC"]
    E --> F["AC = 11i - 8j"]
    F --> G["Magnitude of AC = sqrt(11^2 + 8^2)"]
    G --> H["Final displacement magnitude = 13.6 m"]
    B --> I["Distance AB = magnitude of AB"]
    C --> J["Distance BC = magnitude of BC"]
    I --> K["Total distance = |AB| + |BC|"]
    J --> K
    K --> L["Total distance = 7.21 + 13 = 20.21 m"]
```
