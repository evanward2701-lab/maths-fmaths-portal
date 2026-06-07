---
asset_id: FA22TravellingSalesmanProblemMermaid-001
asset_type: mermaid
topic_id: FA22TravellingSalesmanProblem
unit_code: FA22
topic_code: FA22-ALGGRAPH
lesson_file: FA22_travelling_salesman_problem_lesson.md
related_lesson_section: "# 9. Visual Asset Integration"
used_placeholder: "[VISUAL PLACEHOLDER: FA22TravellingSalesmanProblemMermaid-001 | Source: CCEA FA22-ALGGRAPH-LO001 + uploaded nearest-neighbour slide evidence | Insert from mermaid/FA22TravellingSalesmanProblemMermaid-001.md | Purpose: Show the nearest neighbour algorithm as a decision flow from starting vertex to final Hamiltonian cycle.]"
source:
  - CCEA FA22-ALGGRAPH-LO001
  - Uploaded transcript evidence: Chapter 5, Travelling Salesman Problem, nearest neighbour algorithm section
purpose: "Show the nearest neighbour algorithm as a decision flow from starting vertex to final Hamiltonian cycle."
---

# FA22TravellingSalesmanProblemMermaid-001

```mermaid
flowchart TD
    A["Start nearest neighbour algorithm"] --> B{"Has the question specified<br/>a starting vertex?"}
    B -- "Yes" --> C["Use the specified starting vertex"]
    B -- "No, and all starts are requested" --> C2["Choose the first starting vertex<br/>from the list of vertices"]
    C --> D["Set current vertex = start"]
    C2 --> D
    D --> E["Mark the start vertex as visited"]
    E --> F["Write route so far:<br/>start"]
    F --> G{"Have all vertices<br/>been visited?"}
    G -- "No" --> H["Inspect distances from<br/>the current vertex only"]
    H --> I["Ignore:<br/>• the diagonal dash<br/>• already visited vertices"]
    I --> J{"Is there a unique nearest<br/>unvisited vertex?"}
    J -- "Yes" --> K["Choose the nearest<br/>unvisited vertex"]
    J -- "No, tie" --> T["State the tie clearly<br/>and follow the given tie rule,<br/>or choose one route consistently"]
    T --> K
    K --> L["Add the chosen vertex<br/>to the route"]
    L --> M["Add the chosen edge weight<br/>to the running total"]
    M --> N["Mark the chosen vertex<br/>as visited"]
    N --> O["Set current vertex<br/>= chosen vertex"]
    O --> G
    G -- "Yes" --> P["Return directly to<br/>the starting vertex"]
    P --> Q["Add the final return edge<br/>to the route length"]
    Q --> R["State the Hamiltonian cycle"]
    R --> S["State the total length<br/>as an upper bound"]
    S --> U{"Were all starting vertices<br/>required?"}
    U -- "No" --> V["Finish"]
    U -- "Yes" --> W{"Have all starting vertices<br/>been used?"}
    W -- "No" --> X["Repeat the algorithm<br/>from the next starting vertex"]
    X --> D
    W -- "Yes" --> Y["Compare all route lengths"]
    Y --> Z["Select the smallest route length<br/>as the best nearest-neighbour upper bound"]
    Z --> V
```

Student warning: nearest neighbour chooses the nearest unvisited vertex from the current vertex only. It does not choose the smallest unused edge in the whole table, and it is not Prim’s algorithm.
