---
asset_id: FA22FlowsInNetworks2Mermaid-001
asset_type: Mermaid diagram
unit_code: FA22
topic_code: FA22-GRAPH
topic_id: FA22FlowsInNetworks2
topic_slug: flows_in_networks_2
related_lesson_file: FA22_flows_in_networks_2_lesson.md
related_lesson_section: "# 9. Visual Asset Integration"
used_placeholder: "[VISUAL PLACEHOLDER: FA22FlowsInNetworks2Mermaid-001 | Source: CCEA Further Mathematics specification map + transcript playlist overview | Insert from mermaid/FA22FlowsInNetworks2Mermaid-001.md | Purpose: Show how the lesson branches from cutsets and max-flow min-cut into lower capacities, residual arrows, supersources, supersinks and restricted nodes. Description: A flowchart beginning with `FA22-GRAPH-LO002`, then splitting into feasible flows, lower/upper capacities, augmentation, cut values, multiple sources/sinks and restricted nodes.]"
source: "CCEA Further Mathematics specification map + transcript playlist overview"
creation_status: "Generated in Phase 2"
---

# FA22FlowsInNetworks2Mermaid-001

## Purpose

Show how **FA22-GRAPH-LO002** branches from cutsets and the max-flow min-cut theorem into the lesson-specific methods for **Flows in Networks 2**.

## Mermaid code

```mermaid
flowchart TD
    A["FA22-GRAPH-LO002<br/>Cutsets and max-flow min-cut theorem"]
    A --> B["Directed capacitated networks"]
    B --> C["Source S"]
    B --> D["Sink T"]
    B --> E["Arcs carry capacities"]
    E --> F["Upper-only earlier method<br/>0 ≤ f ≤ u"]
    E --> G["Flows in Networks 2 upgrade<br/>l ≤ f ≤ u"]
    G --> H["Lower and upper capacity label<br/>(l, u)"]
    H --> I["Feasible flow condition<br/>l_uv ≤ f_uv ≤ u_uv"]
    I --> J["Node balance<br/>total flow in = total flow out"]
    J --> K["Deduce forced flows"]
    G --> L["Residual network changes"]
    L --> M["Forward residual<br/>u - f"]
    L --> N["Backward residual<br/>f - l"]
    N --> N1["Warning<br/>not simply f unless l = 0"]
    M --> O["Find augmenting route"]
    N --> O
    O --> P["Augment by smallest residual value"]
    P --> Q["Update flow"]
    Q --> R["Actual flow = lower capacity + backward value"]
    A --> U["Cutsets"]
    U --> V["Separate source side from sink side"]
    V --> W["Forward crossing arcs<br/>use upper capacities"]
    V --> X["Backward crossing arcs<br/>use lower capacities and subtract"]
    W --> Y["Cut value<br/>Σ upper forwards - Σ lower backwards"]
    X --> Y
    Y --> Z["Compare with feasible flow"]
    Z --> AA["If feasible flow value = cut value"]
    AA --> AB["By max-flow min-cut theorem<br/>flow is maximum"]
    B --> AC["Multiple sources and/or sinks"]
    AC --> AD["Add supersource S*"]
    AC --> AG["Add supersink T*"]
    B --> AJ["Restricted capacity nodes"]
    AJ --> AL["Create V_in and V_out"]
    AL --> AM["Insert arc V_in → V_out"]
    B --> AO["Blocked node"]
    AO --> AP["Delete the node and incident arcs"]
```
