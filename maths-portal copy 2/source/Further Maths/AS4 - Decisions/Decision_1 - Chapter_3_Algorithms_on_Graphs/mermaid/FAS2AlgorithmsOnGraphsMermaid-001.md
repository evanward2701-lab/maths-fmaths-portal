# FAS2AlgorithmsOnGraphsMermaid-001

## Asset Metadata

| Field | Entry |
|---|---|
| Asset ID | `FAS2AlgorithmsOnGraphsMermaid-001` |
| Asset type | Mermaid diagram |
| Related lesson file | `FAS2_algorithms_on_graphs_lesson.md` |
| Related lesson section | Section 9: Visual Asset Integration |
| Used placeholder | `[VISUAL PLACEHOLDER: FAS2AlgorithmsOnGraphsMermaid-001 | Source: CCEA FAS2 Algorithms on Graphs specification + supplied lesson evidence | Insert from mermaid/FAS2AlgorithmsOnGraphsMermaid-001.md | Purpose: Decision flow for choosing Prim’s algorithm or Dijkstra’s algorithm.]` |
| Source | CCEA FAS2 Algorithms on Graphs specification boundary + supplied Decision 1 Algorithms on Graphs evidence |
| Purpose | Help students choose the correct algorithm before calculating. |
| Core CCEA content represented | Algorithm definition, greedy algorithm, Prim’s algorithm, Dijkstra’s algorithm |
| Boundary content flagged | Kruskal’s algorithm, Floyd’s algorithm, Prim’s order/complexity proof |
| Status | Written to file. |

## Creation Notes

This diagram supports the first exam decision in the lesson: use Prim’s algorithm for minimum connector/minimal spanning tree questions, use Dijkstra’s algorithm for shortest-path questions, separate official missing FAS2 content, and keep Kruskal/Floyd/Prim complexity as enrichment only for this evidence-backed lesson.

## Mermaid Code

```mermaid
flowchart TD
    Start([Read the question carefully]) --> Q1{Does it ask for a minimum connector,<br/>minimal spanning tree,<br/>or to connect all vertices?}

    Q1 -- Yes --> Prim[Use Prim's algorithm]
    Prim --> PrimOut[Output:<br/>selected edges forming a tree<br/>+ total weight]
    PrimOut --> PrimChecks{Check MST conditions}
    PrimChecks --> P1[Every vertex included]
    PrimChecks --> P2[No cycles]
    PrimChecks --> P3[Total weight stated]

    Q1 -- No --> Q2{Does it ask for the shortest path<br/>or shortest route between<br/>specified vertices?}

    Q2 -- Yes --> Dijkstra[Use Dijkstra's algorithm]
    Dijkstra --> DijkstraOut[Output:<br/>final labels<br/>+ traceback route<br/>+ shortest distance]
    DijkstraOut --> D1[Start label is 0]
    DijkstraOut --> D2[Smallest working value becomes final]
    DijkstraOut --> D3[Trace back using label differences]

    Q2 -- No --> Q3{Is it another official FAS2<br/>Algorithms on Graphs item?}

    Q3 -- Critical path analysis --> Missing1[Official FAS2 content,<br/>but missing lesson-specific evidence here.<br/>Build separate evidence-backed lesson.]
    Q3 -- Binary tree traversal --> Missing2[Official FAS2 content,<br/>but missing lesson-specific evidence here.<br/>Build separate evidence-backed lesson.]
    Q3 -- No or unclear --> Boundary[Do not force Prim or Dijkstra.<br/>Check the specification boundary.]

    Start --> GreedyNote[Greedy algorithm idea:<br/>choose the best available legal option<br/>at each step]
    GreedyNote --> Legal[Key word: available.<br/>Smallest number on the page<br/>may not be legal.]

    Boundary --> OffSpec{Supplied evidence mentions<br/>Kruskal, Floyd or Prim complexity?}
    OffSpec -- Kruskal --> Enrich1[Optional enrichment only<br/>in this evidence-backed lesson.<br/>Not named in supplied CCEA FAS2 LO wording.]
    OffSpec -- Floyd --> Enrich2[Optional enrichment only.<br/>Supplied evidence labels Floyd as A2 content,<br/>but supplied CCEA boundary here does not require it.]
    OffSpec -- Prim order/complexity --> Enrich3[Optional enrichment only.<br/>Not required by supplied FAS2 LO wording.]
```

## Accessibility Description

This flowchart begins with reading the question carefully. It checks whether the task is a minimum connector/minimal spanning tree problem, in which case Prim’s algorithm is used, or a shortest-route problem, in which case Dijkstra’s algorithm is used. It also marks critical path analysis and binary tree traversal as official FAS2 content requiring separate evidence, and Kruskal/Floyd/Prim complexity as enrichment only for this lesson.

## Student-Facing Caption

Use this diagram before calculating. The first mark-saving move is choosing the correct algorithm: **Prim connects everything**, while **Dijkstra finds a shortest route**.
