# AS1DifferentiationMERMAID-005

## Asset Metadata

- Asset ID: `AS1DifferentiationMERMAID-005`
- Asset type: Mermaid flowchart
- Source: Chapter 12 Differentiation PDF pp.21–23
- Related lesson section: Core Theory 14–16
- Purpose: Compare the method for finding tangents and normals to curves.
- Status: Final

```mermaid
flowchart TD
    A["Question asks for tangent or normal"] --> B["Differentiate curve"]
    B --> C["Find tangent gradient m_t at given x"]
    C --> D["Find point on curve"]
    D --> E["Substitute x into original function to get y"]
    E --> F["Point is (x1, y1)"]
    F --> G{"Tangent or normal?"}
    G --> H["Tangent"]
    H --> I["Use m = m_t"]
    I --> J["Equation: y - y1 = m(x - x1)"]
    G --> K["Normal"]
    K --> L["Use negative reciprocal"]
    L --> M["m_n = -1 / m_t"]
    M --> N["Equation: y - y1 = m_n(x - x1)"]
    J --> O["Final line equation"]
    N --> O
    O --> P["Exam check: did the question ask for tangent or normal?"]
```
