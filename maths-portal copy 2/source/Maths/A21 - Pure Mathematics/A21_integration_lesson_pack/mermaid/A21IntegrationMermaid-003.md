# A21IntegrationMermaid-003

## Asset Metadata

| Field | Value |
|---|---|
| Asset ID | A21IntegrationMermaid-003 |
| Asset type | Mermaid flowchart |
| Lesson | A21 Integration |
| Related section | Evidence Map and Syllabus Boundary |
| Source | Specification map, module map, checklist, lesson evidence |
| Purpose | Show evidence filtering through CCEA boundaries. |

```mermaid
flowchart TD
    A["Evidence sources"] --> B["CCEA specification"]
    A --> C["Module map/checklist"]
    A --> D["Transcript and slides"]
    A --> E["Screenshots"]
    A --> F["Cross-board cheat sheet"]
    B --> G["Authority for LO IDs and boundary"]
    C --> H["Metadata and file conventions"]
    D --> I["Explanations and examples"]
    E --> J["Visual support only"]
    F --> K["Supplementary only"]
    G --> L{"Matches A21 Integration?"}
    H --> L
    I --> L
    J --> L
    K --> L
    L -- Yes --> M["Core lesson content"]
    L -- Unclear --> N["Boundary-risk log"]
    L -- No --> O["Exclude from core"]
    N --> P["Parametric integration and trapezium rule restricted"]
    O --> Q["Further Maths comments excluded"]
```
