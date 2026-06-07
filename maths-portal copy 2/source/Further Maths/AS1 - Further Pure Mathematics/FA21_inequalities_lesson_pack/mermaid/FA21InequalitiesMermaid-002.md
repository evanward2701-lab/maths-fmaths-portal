# FA21InequalitiesMermaid-002

## Asset Metadata

| Field | Entry |
|---|---|
| Asset ID | FA21InequalitiesMermaid-002 |
| Asset type | Mermaid flowchart |
| Lesson file | FA21_inequalities_lesson.md |
| Related lesson section | Section 9.1 Mermaid assets; Section 8.7 Graphical inequalities; Section 11 Worked Examples 5–6 |
| Used placeholder | `[VISUAL PLACEHOLDER: FA21InequalitiesMermaid-002 | Source: FP1 inequalities transcript + PDF enrichment evidence | Insert from mermaid/FA21InequalitiesMermaid-002.md | Purpose: Flowchart for graphical inequalities: sketch both graphs, find asymptotes, find intersections, compare vertical order, write intervals.]` |
| Source | FP1 inequalities transcript + PDF enrichment evidence |
| Boundary status | Internal portal enrichment, not official CCEA Further Mathematics specification content |
| Purpose | Show how to solve graphical inequalities using sketches, intersections, asymptotes and vertical order. |

## Mermaid Code

```mermaid
flowchart TD
    A["Start with an inequality comparing two functions"] --> B["Name the two graphs: y = f(x), y = g(x)"]
    B --> C["Sketch the easier graph first"]
    C --> D["Analyse the harder graph"]
    D --> E["Find values causing division by zero"]
    E --> F["Mark vertical asymptotes and excluded x-values"]
    D --> G["Find large-x and small-x behaviour"]
    G --> H["Mark horizontal or oblique behaviour if relevant"]
    F --> I["Find intersections by solving f(x) = g(x)"]
    H --> I
    I --> J["Place intersections and asymptotes in order on x-axis"]
    J --> K["Use sketch to compare vertical order"]
    K --> L{"Does the question ask f(x) less than g(x)?"}
    L -->|Yes| M["Choose intervals where graph f is below graph g"]
    L -->|No| N{"Does it ask f(x) greater than g(x)?"}
    N -->|Yes| O["Choose intervals where graph f is above graph g"]
    N -->|No| P["Check weak inequality: less/equal or greater/equal"]
    M --> Q["Exclude vertical asymptotes and undefined values"]
    O --> Q
    P --> Q
    Q --> R{"Are intersection endpoints included?"}
    R -->|Strict inequality| S["Do not include intersection endpoints"]
    R -->|Weak inequality| T["Include intersection endpoints if defined"]
    S --> U["Write final intervals using OR or union"]
    T --> U
    U --> V["Final graphical solution"]
```
