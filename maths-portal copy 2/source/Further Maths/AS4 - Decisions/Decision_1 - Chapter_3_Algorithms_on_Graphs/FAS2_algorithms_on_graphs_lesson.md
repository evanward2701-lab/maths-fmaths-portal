# FAS2 Algorithms on Graphs: Prim’s Algorithm, Dijkstra’s Algorithm and Greedy Thinking

## 1. Lesson Title and Metadata

| Field | Entry |
|---|---|
| Date generated | 2026-06-05 |
| Course | CCEA GCE Further Mathematics |
| Unit code | `FAS2` |
| Unit title | Further AS 2 Applied Mathematics |
| Applied section | Section D: Discrete and Decision Mathematics |
| Topic code | `FAS2-ALGGRAPH` |
| Topic name | Algorithms on graphs |
| Lesson focus | Greedy algorithms, Prim’s algorithm and Dijkstra’s algorithm |
| Topic slug | `algorithms_on_graphs` |
| Topic Pascal | `AlgorithmsOnGraphs` |
| Topic ID | `FAS2AlgorithmsOnGraphs` |
| Lesson file | `FAS2_algorithms_on_graphs_lesson.md` |
| Core LO IDs | `FAS2-ALGGRAPH-LO001`, `FAS2-ALGGRAPH-LO003`, `FAS2-ALGGRAPH-LO005` |
| Official LO IDs logged as missing evidence | `FAS2-ALGGRAPH-LO002`, `FAS2-ALGGRAPH-LO004` |
| Bridge tags | `#NoDirectOrdinaryMathsPredecessor`, `#Optimisation`, `#Tables`, `#Inequalities`, `#AlgorithmicReasoning` |
| Topic tags | `#FAS2`, `#ALGGRAPH`, `#Decision`, `#Algorithms`, `#Prim`, `#Dijkstra`, `#GreedyAlgorithm`, `#MinimalSpanningTree`, `#ShortestPath`, `#SectionD` |

This lesson teaches the CCEA Further Mathematics FAS2 Algorithms on Graphs content that is supported by the supplied lesson evidence and confirmed by the supplied CCEA Further Mathematics specification boundary.

The core of the lesson is:

- what an algorithm is;
- what a greedy algorithm is;
- how Prim’s algorithm finds a minimal spanning tree for a connected weighted graph;
- how Dijkstra’s algorithm finds a shortest path.

Kruskal’s algorithm and Floyd’s algorithm appear in the supplied evidence, but they are not treated as required CCEA core content because they are not named in the supplied CCEA FAS2 Algorithms on Graphs learning outcomes used for this lesson.

## 2. Evidence Map

| Source | Type | Used for | Authority level | Notes |
|---|---|---|---|---|
| `CCEA_GCE_Further_Mathematics_Specification_Map.md` | Project source/specification map | Topic identity, LO IDs, wording, syllabus boundary | Highest | Identified `FAS2-ALGGRAPH`. |
| `Further_Maths_README_module_map.md` | Project source/module map | Metadata conventions and file structure | High | Confirms Further Maths prefixes and bridge separation. |
| `Further_Maths_EVIDENCE_DROP_CHECKLIST.md` | Project source/checklist | Evidence intake and asset planning | High | Used for logs and placeholders. |
| `Ordinary_A_Level_Maths_Bridge_Spec_Extracts.md` | Bridge source | Ordinary A-Level Maths bridge | Bridge only | Confirms no direct ordinary A-Level predecessor. |
| `Decision Maths 1 Chapter 3 Algorithms on Graphs (including Floyd A2 content).pdf` | Lesson PDF/slide evidence | Definitions, Prim, Dijkstra, matrix method, boundary risks | Evidence-backed where on CCEA spec | Cross-board/third-party style evidence, controlled by CCEA boundary. |
| `transcripts.md` | Teacher transcript | Explanations, warnings, examples, exam technique | Evidence-backed where on CCEA spec | Speech-recognition distortions corrected where mathematically clear. |
| `Chapter_3_Algorithms_on_Graphs_💻_(Decision_1)_screenshots.pdf` | Screenshot PDF | Visual layout and diagram evidence | Partial visual evidence | No text parsed automatically; only visible/readable details used. |

### Evidence limitations

The screenshot PDF could not be text-parsed automatically. It contains rendered images, and the visible preview shows slides and worked networks, but this lesson does not claim that every page of the 150-page screenshot PDF has been manually inspected. Visual descriptions preserve only visible/readable details available through preview and parsed companion sources.

The transcript contains automatic speech-recognition distortions. For example, “crysal”, “Crystal”, or “croll” refer to Kruskal, and “Dyas” refers to Dijkstra. The lesson corrects mathematical names while preserving the intended method.

## 3. Specification Alignment

| LO ID | Official wording | Lesson coverage | Evidence source | Boundary note | Ordinary A-Level bridge |
|---|---|---|---|---|---|
| `FAS2-ALGGRAPH-LO001` | demonstrate understanding of the definition of an algorithm, including the term greedy algorithm | Defines algorithm, greedy algorithm, repeated rule-based decision, allowed move, rejected move, final output. | Transcript and lesson PDF explain greedy selection and graph algorithms. | Core. | Ordinary Maths contributes comparison, inequalities, tables and step-by-step notation. |
| `FAS2-ALGGRAPH-LO002` | solve problems involving critical path analysis, including a precedence table for an activity network, event times and float times, and an algorithm for finding the critical path | Not taught here due missing lesson-specific evidence. | D1 overview lists Critical Path Analysis separately. | Missing evidence. | Needs a separate evidence-backed section. |
| `FAS2-ALGGRAPH-LO003` | recall and use Prim's algorithm to find a minimal spanning tree for a connected weighted graph | Teaches Prim’s algorithm on weighted graphs and from distance matrices. | Slide evidence and transcript. | Core. Matrix method included as representation technique. | Ordinary optimisation and table-reading skills extend to graph algorithms. |
| `FAS2-ALGGRAPH-LO004` | recall binary trees and traverse them using breadth first search and depth first search | Not taught here due missing lesson-specific evidence. | No supplied binary tree/BFS/DFS evidence. | Missing evidence. | Needs a separate evidence-backed section. |
| `FAS2-ALGGRAPH-LO005` | recall and use Dijkstra's algorithm to find a shortest path | Teaches final labels, working values, smallest-label choice and traceback. | PDF/transcript Dijkstra evidence. | Core. | Ordinary arithmetic, inequalities and table discipline. |

### Boundary-control statement

This lesson is not a general Decision 1 lesson. It is a CCEA Further Mathematics lesson. Therefore:

- Prim’s algorithm is core because CCEA names it in `FAS2-ALGGRAPH-LO003`.
- Dijkstra’s algorithm is core because CCEA names it in `FAS2-ALGGRAPH-LO005`.
- Greedy algorithm language is core because CCEA names it in `FAS2-ALGGRAPH-LO001`.
- Kruskal’s algorithm is not treated as required core content because it is not named in the supplied CCEA FAS2 LO wording.
- Floyd’s algorithm is not treated as required core content because it is not named in the supplied CCEA FAS2 or FA22 Algorithms on Graphs LO wording.
- Critical path analysis and binary tree traversals are official FAS2 content, but this evidence drop does not provide enough lesson-specific evidence to build them faithfully here.

## 4. Learning Objectives

### 4.1 Core Further Maths objectives

By the end of this lesson, you should be able to:

1. Define an algorithm as a finite, repeatable set of instructions for solving a problem.
2. Explain what makes an algorithm greedy: at each step it takes the best available allowed option according to a local rule.
3. Recognise when a problem asks for a minimal spanning tree or minimum connector.
4. Use Prim’s algorithm to find a minimal spanning tree for a connected weighted graph.
5. Use a distance matrix representation to apply Prim’s algorithm when the matrix represents a connected weighted graph.
6. Recognise when a problem asks for a shortest path between two specified vertices.
7. Use Dijkstra’s algorithm to find a shortest path.
8. Trace back through final labels in Dijkstra’s algorithm to state the actual route, not only the length.

### 4.2 Bridge objectives

You should be able to connect this lesson to ordinary A-Level Maths habits by:

1. Comparing numerical values accurately.
2. Using inequality language such as “smaller than”, “least available” and “minimum”.
3. Keeping tables, rows, columns and labels aligned.
4. Showing a sequence of decisions clearly.
5. Interpreting a final numerical answer in context.

### 4.3 Exam technique objectives

You should be able to:

1. Decide whether the question wants a minimum connector or a shortest route.
2. Write selected arcs/edges in a clear order.
3. Avoid selecting the smallest number on the page when it is not an allowed move.
4. Record final labels and working labels cleanly for Dijkstra’s algorithm.
5. For Dijkstra, trace back by checking that
   \[
   \text{final label at later vertex}-\text{final label at earlier vertex}=\text{weight of connecting arc}.
   \]
6. State both the route and the length when the question asks for both.
7. Avoid relying only on highlighting, because scanned exam scripts may not preserve it clearly.

## 5. Explicit Prerequisite Recap

### 5.1 GCSE foundations

You should already be comfortable with:

- adding several numbers accurately;
- comparing numbers;
- choosing the smallest value from a list;
- reading a table;
- using letters to label objects;
- following a sequence of instructions.

This lesson is not algebra-heavy. Its danger is stranger: one wrong tick, one missed edge, one row-column slip, and the whole algorithm wanders into the bushes.

### 5.2 Ordinary AS/A2 Mathematics foundations

There is no direct ordinary CCEA A-Level Mathematics predecessor for graph algorithms. However, ordinary Maths gives useful habits.

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| Ordinary algebra and inequalities | Compare values and choose smaller/larger quantities. | Algorithms repeatedly choose the smallest allowed value. | “Smallest” is not enough; it must be an allowed edge or label. |
| Ordinary optimisation language | Understand minimum and maximum in context. | Prim finds a minimum connector; Dijkstra finds a shortest route. | Minimum connector and shortest route solve different problems. |
| Ordinary table work | Read rows, columns and headings accurately. | Prim’s matrix method and Dijkstra labels rely on table discipline. | A row/column mismatch can corrupt the algorithm. |
| Ordinary problem-solving layout | Show steps clearly and justify conclusions. | Further Maths requires a visible algorithmic trail. | Do not jump from graph to answer without showing the sequence of choices. |

### 5.3 Previous Further Mathematics foundations

This lesson assumes you have already met basic graph/network language from FAS2 Graph theory, especially:

- vertex;
- edge or arc;
- weighted graph;
- connected graph;
- walk;
- path;
- tree;
- cycle;
- subgraph;
- spanning tree.

### 5.4 A-Level Maths Bridge: What You Already Know and What Further Maths Changes

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| Ordinary CCEA A-Level Maths bridge extracts | No direct ordinary A-Level topic predecessor for algorithms on graphs. | Further Maths introduces discrete networks and formal algorithms. | Do not confuse graph theory graphs with coordinate graphs. |
| AS/A2 algebraic comparison skills | Compare numerical quantities and choose smaller values. | Prim and Dijkstra use repeated “smallest allowed” selections. | A value can be numerically smallest but algorithmically illegal. |
| AS/A2 table skills | Read tables systematically. | Distance matrices and label boxes become part of the method. | Unlabelled or misaligned working eats marks quietly. |
| Ordinary optimisation language | Interpret minimum values in context. | Minimum spanning tree and shortest path become distinct optimisation problems. | “Minimum” does not always mean “shortest route”. |

In ordinary A-Level Maths, this idea appeared as comparing values, organising tables and solving optimisation-style problems.

In Further Maths, the same idea becomes a rule-driven process on a discrete structure called a graph or network.

The key upgrade is that you are not just calculating a number. You are following an algorithm whose steps must be visible, reproducible and legal.

The danger is treating every algorithm as “pick the smallest number”. The real rule is “pick the smallest number that the algorithm currently allows”.

## 6. Big Picture Explanation

A graph in this topic is a network of points and connections. The points are called vertices. The connections are called edges or arcs. If a number is written on an edge, the graph is weighted.

The weight might represent:

- distance;
- time;
- cost;
- cable length;
- risk;
- delay.

### 6.1 Two different problems

#### Problem A: Connect everything as cheaply as possible

This is a minimal spanning tree problem. You want:

- every vertex included;
- no cycles;
- the total weight as small as possible.

This is the job of Prim’s algorithm in the CCEA FAS2 boundary.

#### Problem B: Get from one place to another as quickly as possible

This is a shortest path problem. You want:

- a start vertex;
- a target vertex;
- the route of least total weight between them.

This is the job of Dijkstra’s algorithm.

### 6.2 The algorithmic mindset

An algorithm is a finite, clear, repeatable set of instructions. For this topic, the central exam habit is:

\[
\text{Choose}\rightarrow\text{Record}\rightarrow\text{Check legality}\rightarrow\text{Repeat}.
\]

### 6.3 Why greedy algorithms appear

A greedy algorithm makes a locally best choice at each step. For example:

- Prim’s algorithm chooses the least-weight edge that connects the growing tree to a new vertex.
- Dijkstra’s algorithm chooses the currently smallest working label and makes it final.

The greedy idea is not “pick any tiny number”. It is “pick the best available legal move”.

## 7. Key Definitions and Notation

### 7.1 Graph and network language

A graph \(G\) is a mathematical structure made from:

- a set of vertices, usually labelled \(A,B,C,\ldots\);
- a set of edges or arcs joining pairs of vertices.

A network is usually a graph with weights on its edges.

If edge \(AB\) has weight \(7\), write:

\[
w(AB)=7.
\]

### 7.2 Walk, path and connectedness

A walk is a route through a graph along edges from one vertex to the next.

A path is a walk in which no vertex is visited more than once.

Two vertices are connected if there is a path between them.

A graph is connected if all its vertices are connected.

### 7.3 Tree, subgraph and spanning tree

A tree is a connected graph with no cycles.

A cycle is a closed route that returns to its starting vertex without immediately retracing an edge.

A subgraph of \(G\) is a graph whose vertices and edges belong to \(G\).

A spanning tree is a subgraph that:

1. includes all the vertices of the original graph;
2. is a tree.

So:

\[
\text{spanning tree}=\text{all vertices included}+\text{connected with no cycles}.
\]

### 7.4 Minimal spanning tree

A minimal spanning tree, often called an MST, is a spanning tree such that the total length or weight of its arcs/edges is as small as possible. It is sometimes called a minimum connector.

For a spanning tree \(T\), its total weight is:

\[
W(T)=\sum_{e\in T}w(e).
\]

A minimal spanning tree is a spanning tree \(T_{\min}\) such that:

\[
W(T_{\min})\leq W(T)
\]

for every spanning tree \(T\) of the graph.

### 7.5 Algorithm

An algorithm is a finite sequence of clear instructions that can be followed to solve a problem. In this lesson, an algorithm must tell you:

- where to start;
- what values to compare;
- what to record;
- what to reject or ignore;
- when to stop;
- how to interpret the result.

### 7.6 Greedy algorithm

A greedy algorithm chooses the best available option at each step according to a local rule. In this lesson:

- “best” usually means least weight or smallest current value;
- “available” is crucial.

### 7.7 Prim’s algorithm notation

Let:

\[
G=(V,E),
\]

where \(V\) is the set of vertices, \(E\) is the set of edges, and \(w(e)\) is the weight of edge \(e\).

At any stage, let \(T\) be the current tree. The next edge must:

1. have one endpoint already in \(T\);
2. have one endpoint not yet in \(T\);
3. have the smallest possible weight among such edges.

### 7.8 Dijkstra’s algorithm notation

Let:

- \(S\) be the start vertex;
- \(T\) be the target vertex;
- \(X\) be the vertex that has just received a final label;
- \(Y\) be a vertex directly connected to \(X\);
- \(d(X)\) be the final label at \(X\);
- \(w(XY)\) be the weight of edge \(XY\).

The working value at \(Y\) through \(X\) is:

\[
d(X)+w(XY).
\]

If \(Y\) already has a working value, replace it only if the new value is smaller.

## 8. Core Theory

### 8.1 What makes an algorithm valid?

An algorithm must be:

1. finite: it stops after a finite number of steps;
2. clear: each step is unambiguous;
3. repeatable: another person can follow it and check it;
4. correct for its purpose: it solves the problem it claims to solve.

For graph algorithms, a correct solution usually includes:

- a sequence of selected vertices or edges;
- any rejected edges where the algorithm requires rejection;
- a final route or tree;
- a total weight, distance, cost or time.

**Bridge Note:** In ordinary A-Level Maths, you often solved a problem by choosing a method and calculating. Here, Further Maths extends that by making the method itself part of the answer. The examiner wants the breadcrumb trail, not just the sandwich at the end.

### 8.2 Greedy algorithms

A greedy algorithm makes the best available local choice at each step.

For Prim’s algorithm, the next edge is available only if it joins:

\[
\text{a vertex already in the tree}
\]

to

\[
\text{a vertex not yet in the tree}.
\]

For Dijkstra’s algorithm, the next final label is the smallest current working value among vertices that do not yet have final labels.

### 8.3 Minimal spanning trees

A minimal spanning tree solves:

> How can we connect every vertex in the network using the smallest total weight?

It must:

1. include every vertex;
2. be connected;
3. have no cycles.

If the original graph has \(n\) vertices, any spanning tree has:

\[
n-1
\]

edges.

### 8.4 Prim’s algorithm: purpose and method

Prim’s algorithm finds a minimal spanning tree for a connected weighted graph.

Steps:

1. Choose any vertex to start the tree.
2. Select an arc of least weight that joins a vertex already in the tree to a vertex not yet in the tree.
3. If there is a choice of arcs of equal weight, choose either valid edge.
4. Repeat until all vertices are connected.

Important warning: after each new vertex is added, inspect all edges from the whole current tree to new vertices, not just edges from the last vertex added.

### 8.5 Why Prim’s algorithm never creates a cycle

At every stage, Prim’s algorithm adds an edge from the current tree to a vertex not yet in the tree. A cycle would require both endpoints already to be connected inside the tree. Since Prim’s algorithm forbids that, it cannot create a cycle.

### 8.6 Equal weights in Prim’s algorithm

If there is a choice of equal-weight available arcs, either may be chosen. There may be more than one valid minimal spanning tree.

### 8.7 Prim’s algorithm from a distance matrix

A distance matrix might look like:

\[
\begin{array}{c|cccc}
 & A & B & C & D\\
\hline
A & - & 8 & 10 & -\\
B & 8 & - & 23 & 14\\
C & 10 & 23 & - & 7\\
D & - & 14 & 7 & -
\end{array}
\]

Matrix method:

1. Choose any vertex to start the tree.
2. Delete/cross the row in the matrix for the chosen vertex.
3. Number the column in the matrix for the chosen vertex.
4. Ring the lowest undeleted entry in the numbered columns.
5. The ringed entry becomes the next arc to be added to the tree.
6. Repeat until all rows are deleted.

If a column is numbered, that vertex has already been added to the tree. If a row is not deleted, that vertex has not yet been added. So choosing the smallest undeleted entry in the numbered columns means choosing the least edge from the current tree to a new vertex.

### 8.8 Dijkstra’s algorithm: purpose and method

Dijkstra’s algorithm finds the shortest path from a start vertex to a target vertex.

It does not find a minimal spanning tree.

It solves:

\[
\text{Shortest route from }S\text{ to }T.
\]

Labels:

- a working value is provisional and can be replaced;
- a final label is permanent and is not revisited.

Method:

1. Label the start vertex \(S\) with final label \(0\).
2. If \(X\) has just received its final label, update every directly connected non-final vertex \(Y\) using
   \[
   d(X)+w(XY).
   \]
3. If \(Y\) already has a working value, keep the smaller value.
4. Choose the smallest working value and make it final.
5. Repeat until the target vertex has a final label.
6. Trace back to find the route.

Traceback rule:

\[
d(B)-d(A)=w(AB).
\]

If this is true, then edge \(AB\) can lie immediately before \(B\) on a shortest route.

### 8.9 Prim versus Dijkstra

| Feature | Prim’s algorithm | Dijkstra’s algorithm |
|---|---|---|
| Main purpose | Find a minimal spanning tree | Find a shortest path |
| Output | Tree connecting all vertices | Route from a start vertex to a target vertex |
| Uses every vertex? | Yes | Not necessarily |
| Greedy choice | Least allowed edge from tree to new vertex | Smallest current working label |
| Stops when | All vertices are connected | Target vertex receives final label |
| Typical final answer | Selected edges and total weight | Route and shortest distance |

## 9. Visual Asset Integration

Diagram evidence is partially unclear here. The description below preserves the visible/readable details only. No uninspected visual detail is claimed.

[VISUAL PLACEHOLDER: FAS2AlgorithmsOnGraphsBridgeSVG-001 | Source: Ordinary A-Level Maths bridge + CCEA Further Mathematics specification | Insert from svg/FAS2AlgorithmsOnGraphsBridgeSVG-001.svg | Purpose: Compare prior ordinary Maths method with Further Maths extension.]

[VISUAL PLACEHOLDER: FAS2AlgorithmsOnGraphsMermaid-001 | Source: CCEA FAS2 Algorithms on Graphs specification + supplied lesson evidence | Insert from mermaid/FAS2AlgorithmsOnGraphsMermaid-001.md | Purpose: Decision flow for choosing Prim’s algorithm or Dijkstra’s algorithm.]

[VISUAL PLACEHOLDER: FAS2AlgorithmsOnGraphsSVG-001 | Source: Supplied PDF minimum spanning tree and Prim’s algorithm evidence | Insert from svg/FAS2AlgorithmsOnGraphsSVG-001.svg | Purpose: Show how a connected weighted graph is reduced to a minimal spanning tree.]

[VISUAL PLACEHOLDER: FAS2AlgorithmsOnGraphsTikZ-001 | Source: Supplied PDF/transcript Prim’s algorithm worked example | Insert from tikz/FAS2AlgorithmsOnGraphsTikZ-001.tex | Purpose: Create a precise mathematical diagram for the Prim’s algorithm worked example.]

[VISUAL PLACEHOLDER: FAS2AlgorithmsOnGraphsSVG-002 | Source: Supplied PDF Prim’s algorithm matrix method | Insert from svg/FAS2AlgorithmsOnGraphsSVG-002.svg | Purpose: Show how crossed rows, numbered columns and circled lowest entries implement Prim’s algorithm from a distance matrix.]

[VISUAL PLACEHOLDER: FAS2AlgorithmsOnGraphsTikZ-002 | Source: Supplied PDF Dijkstra’s algorithm notation and worked example | Insert from tikz/FAS2AlgorithmsOnGraphsTikZ-002.tex | Purpose: Show Dijkstra’s label-box structure with vertex name, order of labelling, final label and working values.]

[VISUAL PLACEHOLDER: FAS2AlgorithmsOnGraphsSVG-003 | Source: Supplied PDF Dijkstra traceback instruction | Insert from svg/FAS2AlgorithmsOnGraphsSVG-003.svg | Purpose: Show how the shortest path is recovered by subtracting edge weights from final labels.]

[VISUAL PLACEHOLDER: FAS2AlgorithmsOnGraphsSVG-004 | Source: CCEA FAS2 specification boundary + supplied lesson evidence | Insert from svg/FAS2AlgorithmsOnGraphsSVG-004.svg | Purpose: Separate core CCEA content from supplied but excluded enrichment.]

## 10. Interactive Learning Widgets

[INTERACTIVE PLACEHOLDER: FAS2AlgorithmsOnGraphsWidget-001 | Source: AI-proposed teaching enhancement based on Prim’s algorithm lesson evidence | Insert from widgets/FAS2AlgorithmsOnGraphsWidget-001.html | Purpose: Help the student practise selecting the next valid Prim edge.]

Student inputs: choose a starting vertex, click an available edge, build a tree step by step, reset the graph and request a hint. It checks choosing an edge between two already-tree vertices, choosing an edge outside the tree, choosing a larger valid edge while a smaller valid edge exists, stopping early and including a cycle.

[INTERACTIVE PLACEHOLDER: FAS2AlgorithmsOnGraphsWidget-002 | Source: AI-proposed teaching enhancement based on Prim’s matrix evidence | Insert from widgets/FAS2AlgorithmsOnGraphsWidget-002.html | Purpose: Train row-crossing, column-numbering and lowest-valid-entry selection for Prim’s algorithm from a distance matrix.]

Student inputs: choose a matrix entry, follow crossed rows and numbered columns, record selected arcs. It checks unnumbered columns, crossed rows, dashes and non-minimal valid entries.

[INTERACTIVE PLACEHOLDER: FAS2AlgorithmsOnGraphsWidget-003 | Source: AI-proposed teaching enhancement based on Dijkstra label-box evidence | Insert from widgets/FAS2AlgorithmsOnGraphsWidget-003.html | Purpose: Help the student complete Dijkstra’s algorithm using working values and final labels.]

Student inputs: choose the next final label, inspect working values and reveal traceback. It checks wrong final-label choices, revisiting final vertices and traceback logic.

[INTERACTIVE PLACEHOLDER: FAS2AlgorithmsOnGraphsWidget-004 | Source: AI-proposed teaching enhancement based on CCEA FAS2 boundary | Insert from widgets/FAS2AlgorithmsOnGraphsWidget-004.html | Purpose: Train students to choose Prim or Dijkstra from question wording.]

Student inputs: sort prompts into Prim, Dijkstra, missing official content, or optional enrichment/excluded core.

## 11. Worked Examples

### Worked Example 1: Prim’s algorithm on a small weighted graph

Use Prim’s algorithm, starting at \(A\), to find a minimal spanning tree for the weighted graph with vertices \(A,B,C,D,E\) and weighted edges:

\[
DE=4,\quad AE=5,\quad BC=5,\quad AD=6,\quad BD=6,\quad AB=7,\quad CD=8.
\]

Start at \(A\). The current tree contains:

\[
\{A\}.
\]

Available edges from \(A\):

\[
AE=5,\quad AD=6,\quad AB=7.
\]

Choose:

\[
AE=5.
\]

Current tree:

\[
\{A,E\}.
\]

Available edges from \(\{A,E\}\) to new vertices:

\[
ED=4,\quad AD=6,\quad AB=7.
\]

Choose:

\[
ED=4.
\]

Current tree:

\[
\{A,E,D\}.
\]

Available edges to vertices not yet in the tree:

\[
DB=6,\quad AB=7,\quad DC=8.
\]

The edge \(AD=6\) is not allowed because both \(A\) and \(D\) are already in the tree; adding it would create a cycle.

Choose:

\[
DB=6.
\]

Current tree:

\[
\{A,E,D,B\}.
\]

The only vertex not yet in the tree is \(C\). Available edges to \(C\):

\[
BC=5,\quad DC=8.
\]

Choose:

\[
BC=5.
\]

All vertices are included, so stop.

Selected edges:

\[
AE,\quad ED,\quad DB,\quad BC.
\]

Total weight:

\[
W=5+4+6+5=20.
\]

Final answer:

\[
\boxed{AE,\ ED,\ DB,\ BC}\quad\text{with total weight}\quad\boxed{20}.
\]

### Worked Example 2: Prim’s algorithm from a distance matrix

Use Prim’s algorithm, starting at \(A\), for:

\[
\begin{array}{c|cccc}
 & A & B & C & D\\
\hline
A & - & 8 & 10 & -\\
B & 8 & - & 23 & 14\\
C & 10 & 23 & - & 7\\
D & - & 14 & 7 & -
\end{array}
\]

Start at \(A\). Cross row \(A\), number column \(A\). In column \(A\), the lowest valid entry is \(8\), giving:

\[
AB=8.
\]

Add \(B\). Cross row \(B\), number column \(B\). Now look in numbered columns \(A,B\) and uncrossed rows \(C,D\):

\[
\begin{array}{c|cc}
 & A & B\\
\hline
C & 10 & 23\\
D & - & 14
\end{array}
\]

Choose:

\[
AC=10.
\]

Add \(C\). Cross row \(C\), number column \(C\). Now only row \(D\) remains:

\[
\begin{array}{c|ccc}
 & A & B & C\\
\hline
D & - & 14 & 7
\end{array}
\]

Choose:

\[
CD=7.
\]

Selected arcs:

\[
AB,\quad AC,\quad CD.
\]

Total weight:

\[
W=8+10+7=25.
\]

Final answer:

\[
\boxed{AB,\ AC,\ CD}\quad\text{with total weight}\quad\boxed{25}.
\]

### Worked Example 3: Dijkstra’s algorithm

Use Dijkstra’s algorithm to find the shortest path from \(S\) to \(T\) with edges:

\[
SB=3,\quad SC=8,\quad SD=12,
\]
\[
BE=2,\quad BC=4,
\]
\[
CE=3,\quad CD=3,\quad CF=9,\quad CT=12,
\]
\[
DF=5,\quad ET=14,\quad FT=3.
\]

Start:

\[
d(S)=0.
\]

From \(S\):

\[
B:3,\quad C:8,\quad D:12.
\]

Smallest is \(B=3\), so:

\[
d(B)=3.
\]

From \(B\):

\[
E:3+2=5,
\]
\[
C:3+4=7.
\]

Replace \(C:8\) with \(C:7\). Smallest is \(E=5\), so:

\[
d(E)=5.
\]

From \(E\):

\[
C:5+3=8
\]

but \(C=7\) is smaller, so keep \(C=7\). Also:

\[
T:5+14=19.
\]

Smallest is \(C=7\), so:

\[
d(C)=7.
\]

From \(C\):

\[
D:7+3=10,
\]
	replacing \(D:12\),

\[
F:7+9=16,
\]

\[
T:7+12=19.
\]

Smallest is \(D=10\), so:

\[
d(D)=10.
\]

From \(D\):

\[
F:10+5=15,
\]

replacing \(F:16\). Smallest is \(F=15\), so:

\[
d(F)=15.
\]

From \(F\):

\[
T:15+3=18,
\]

replacing \(T:19\). So:

\[
d(T)=18.
\]

Stop.

Final labels:

| Vertex | Order | Final label |
|---|---:|---:|
| \(S\) | 1 | 0 |
| \(B\) | 2 | 3 |
| \(E\) | 3 | 5 |
| \(C\) | 4 | 7 |
| \(D\) | 5 | 10 |
| \(F\) | 6 | 15 |
| \(T\) | 7 | 18 |

Trace back:

\[
18-3=15=d(F),
\]
\[
15-5=10=d(D),
\]
\[
10-3=7=d(C),
\]
\[
7-4=3=d(B),
\]
\[
3-3=0=d(S).
\]

Therefore:

\[
\boxed{S\to B\to C\to D\to F\to T}
\]

with shortest length:

\[
\boxed{18}.
\]

### Worked Example 4: Dijkstra with two shortest routes

If Dijkstra gives:

\[
d(T)=37,
\]

and traceback allows:

\[
S\to A\to D\to G\to T
\]

and

\[
S\to B\to E\to G\to T,
\]

then there are two shortest routes, both with shortest time:

\[
\boxed{37\text{ minutes}}.
\]

## 12. Common Mistakes and Exam Traps

### 12.1 Using the wrong algorithm

| Question wording | Correct response |
|---|---|
| “Find a minimal spanning tree” | Use Prim’s algorithm |
| “Find a minimum connector” | Use Prim’s algorithm |
| “Connect all vertices with minimum total weight” | Use Prim’s algorithm |
| “Find the shortest path from \(S\) to \(T\)” | Use Dijkstra’s algorithm |
| “Find the shortest route between two specified vertices” | Use Dijkstra’s algorithm |

### 12.2 Choosing the smallest number anywhere

A greedy algorithm does not mean:

\[
\text{Choose the smallest number on the page.}
\]

It means:

\[
\text{Choose the smallest allowed number at this stage.}
\]

### 12.3 Only checking the last vertex added in Prim

If the current tree contains \(\{A,C,D\}\), check edges from \(A\), \(C\) and \(D\) to vertices not yet in the tree. Do not only check edges from \(D\).

### 12.4 Creating a cycle in an MST

If selected edges are \(AB\) and \(BC\), adding \(AC\) creates:

\[
A\to B\to C\to A.
\]

That is a cycle, so it is not a tree.

### 12.5 Stopping Prim too early

A spanning tree on \(n\) vertices must have \(n-1\) edges. If a graph has \(7\) vertices, the spanning tree must have \(6\) edges.

### 12.6 Thinking there is only one possible MST

Equal-weight choices may lead to different-looking minimal spanning trees with the same total weight.

### 12.7 Not writing selected edges clearly

Good evidence:

\[
AC(30),\ CD(22),\ DE(18),\ BD(24),\ EG(26),\ FG(21),\ GH(33).
\]

Poor evidence:

```text
I highlighted it.
```

### 12.8 Matrix Prim from wrong rows or columns

Only entries in numbered columns and uncrossed rows are eligible.

### 12.9 Treating Dijkstra working values as final labels

A working value can be replaced. A final label cannot.

### 12.10 Forgetting traceback in Dijkstra

The final label gives distance, not the route. Trace back using:

\[
d(B)-d(A)=w(AB).
\]

### 12.11 Ignoring multiple shortest routes

If more than one predecessor satisfies the traceback rule, there may be more than one shortest route.

### 12.12 Importing Kruskal or Floyd into core

Kruskal and Floyd appear in the supplied evidence, but they are enrichment only for this evidence-backed CCEA FAS2 lesson.

## 13. Practice Questions

These are generated on-spec practice questions, not past-paper or textbook questions.

### Question 1: Algorithm choice

For each question, state whether you should use Prim’s algorithm, Dijkstra’s algorithm, or neither for this lesson.

1. Find a minimum connector for a network of towns.
2. Find the shortest route from \(A\) to \(H\).
3. Find a minimal spanning tree.
4. Find a route from \(S\) to \(T\) with least total time.
5. Apply Floyd’s algorithm.
6. Traverse a binary tree using breadth first search.
7. Find the minimum total cable length needed to connect every building.
8. Find a shortest path from \(P\) to \(Q\).

### Question 2: Definitions

Define: vertex, edge, weighted graph, path, tree, spanning tree, minimal spanning tree, greedy algorithm.

### Question 3: Tree edge count

A connected weighted graph has \(9\) vertices. How many edges will any spanning tree have? Explain why a connected graph with \(9\) vertices and \(9\) selected edges cannot be a tree.

### Question 4: Ordinary Maths comparison habit

A student says: “I chose edge \(CD=4\) first because it is the smallest number in the matrix.” Explain why this may be invalid when using Prim’s algorithm from a matrix starting at \(A\).

### Question 5: Tables and careful notation

A distance matrix has row \(B\) crossed out but column \(B\) not numbered. Explain what has gone wrong.

### Question 6: Prim’s algorithm on a graph

Use Prim’s algorithm, starting at \(A\), to find a minimal spanning tree for vertices \(A,B,C,D,E,F\) and edges:

\[
AB=4,\ AC=7,\ BC=2,\ BD=5,\ CD=6,\ CE=3,\ DE=4,\ DF=8,\ EF=5.
\]

### Question 7: Prim’s algorithm from a distance matrix

Use Prim’s algorithm, starting at \(A\), for:

\[
\begin{array}{c|ccccc}
 & A & B & C & D & E\\
\hline
A & - & 6 & 2 & - & -\\
B & 6 & - & 5 & 4 & -\\
C & 2 & 5 & - & 7 & 3\\
D & - & 4 & 7 & - & 1\\
E & - & - & 3 & 1 & -
\end{array}
\]

### Question 8: Dijkstra’s algorithm

Use Dijkstra’s algorithm to find the shortest path from \(S\) to \(T\):

\[
SA=4,\ SB=2,\ AB=1,\ AC=5,\ BC=8,\ BD=10,\ CD=2,\ CE=6,\ DE=3,\ DT=7,\ ET=1.
\]

### Question 9: Prim with equal choices

Use Prim’s algorithm, starting at \(A\), for:

\[
AB=3,\ AC=3,\ BC=4,\ BD=2,\ CD=2,\ DE=5,\ CE=5.
\]

Find two different minimal spanning trees and explain why both can be valid.

### Question 10: Dijkstra with two shortest routes

Use Dijkstra’s algorithm from \(S\) to \(T\):

\[
SA=2,\ SB=2,\ AC=3,\ BC=3,\ CT=4,\ AD=5,\ BD=5,\ DT=2.
\]

Find all shortest routes.

## 14. Worked Solutions

### Solution 1

1. Prim’s algorithm.
2. Dijkstra’s algorithm.
3. Prim’s algorithm.
4. Dijkstra’s algorithm.
5. Neither for this core lesson; Floyd is enrichment only.
6. Neither in this evidence-backed lesson; binary tree traversal needs separate evidence.
7. Prim’s algorithm.
8. Dijkstra’s algorithm.

### Solution 2

A vertex is a node. An edge is a connection between two vertices. A weighted graph has numerical weights on edges. A path is a walk in which no vertex is visited more than once. A tree is a connected graph with no cycles. A spanning tree includes all vertices and is a tree. A minimal spanning tree is a spanning tree with minimum total edge weight. A greedy algorithm chooses the best available legal option at each step.

### Solution 3

A spanning tree on \(n\) vertices has \(n-1\) edges. For \(9\) vertices:

\[
9-1=8.
\]

A connected graph with \(9\) vertices and \(9\) selected edges has one edge too many and contains a cycle, so it cannot be a tree.

### Solution 4

The smallest number in the whole matrix may not be a legal Prim move. Starting at \(A\), the first edge must connect \(A\) to a new vertex. If \(CD=4\) connects two vertices not yet in the current tree, it is invalid.

### Solution 5

Crossing row \(B\) says \(B\) has been added. Numbering column \(B\) makes edges from \(B\) available for future steps. If row \(B\) is crossed but column \(B\) is not numbered, the method is inconsistent and may miss valid edges.

### Solution 6

Start at \(A\).

Available from \(A\): \(AB=4, AC=7\). Choose \(AB=4\).

Current tree \(\{A,B\}\). Available: \(AC=7, BC=2, BD=5\). Choose \(BC=2\).

Current tree \(\{A,B,C\}\). Available: \(BD=5, CD=6, CE=3\). Choose \(CE=3\).

Current tree \(\{A,B,C,E\}\). Available: \(BD=5, CD=6, DE=4, EF=5\). Choose \(DE=4\).

Current tree \(\{A,B,C,D,E\}\). Available to \(F\): \(DF=8, EF=5\). Choose \(EF=5\).

Selected edges:

\[
AB,\ BC,\ CE,\ DE,\ EF.
\]

Total:

\[
W=4+2+3+4+5=18.
\]

### Solution 7

Start at \(A\). Choose \(AC=2\). Add \(C\). From columns \(A,C\), choose \(CE=3\). Add \(E\). From columns \(A,C,E\), choose \(DE=1\). Add \(D\). From columns \(A,C,D,E\), choose \(BD=4\). Add \(B\).

Selected edges:

\[
AC,\ CE,\ DE,\ BD.
\]

Total:

\[
W=2+3+1+4=10.
\]

### Solution 8

Start \(d(S)=0\). From \(S\): \(A=4, B=2\). Finalise \(B=2\).

From \(B\): \(A=2+1=3\), replacing \(A=4\); \(C=2+8=10\); \(D=2+10=12\). Finalise \(A=3\).

From \(A\): \(C=3+5=8\), replacing \(C=10\). Finalise \(C=8\).

From \(C\): \(D=8+2=10\), replacing \(D=12\); \(E=8+6=14\). Finalise \(D=10\).

From \(D\): \(E=10+3=13\), replacing \(E=14\); \(T=10+7=17\). Finalise \(E=13\).

From \(E\): \(T=13+1=14\), replacing \(T=17\). Finalise \(T=14\).

Final labels:

| Vertex | Order | Final label |
|---|---:|---:|
| \(S\) | 1 | 0 |
| \(B\) | 2 | 2 |
| \(A\) | 3 | 3 |
| \(C\) | 4 | 8 |
| \(D\) | 5 | 10 |
| \(E\) | 6 | 13 |
| \(T\) | 7 | 14 |

Traceback:

\[
14-1=13=d(E),
\]
\[
13-3=10=d(D),
\]
\[
10-2=8=d(C),
\]
\[
8-5=3=d(A),
\]
\[
3-1=2=d(B),
\]
\[
2-2=0=d(S).
\]

Shortest route:

\[
\boxed{S\to B\to A\to C\to D\to E\to T}
\]

with length:

\[
\boxed{14}.
\]

### Solution 9

One MST: choose \(AB=3\), then \(BD=2\), then \(CD=2\), then \(DE=5\). Total:

\[
3+2+2+5=12.
\]

Another MST: choose \(AC=3\), then \(CD=2\), then \(DB=2\), then \(CE=5\). Total:

\[
3+2+2+5=12.
\]

Both are valid because they include every vertex, have no cycles, and have the same minimum total weight.

### Solution 10

Start \(d(S)=0\). \(A=2\), \(B=2\). Finalise both in either order.

From \(A\): \(C=5\), \(D=7\). From \(B\): \(C=5\), \(D=7\). Finalise \(C=5\), then \(D=7\). From \(C\): \(T=9\). From \(D\): \(T=9\). Finalise \(T=9\).

Shortest distance:

\[
\boxed{9}.
\]

Traceback gives:

\[
S\to A\to C\to T,
\]
\[
S\to B\to C\to T,
\]
\[
S\to A\to D\to T,
\]
\[
S\to B\to D\to T.
\]

All have total length \(9\).

## 15. Exam Technique Notes

1. Use Prim when the question asks for a minimal spanning tree, minimum connector, or connecting all vertices.
2. Use Dijkstra when the question asks for a shortest path or route between specified vertices.
3. In Prim, show starting vertex, edges added in order, final tree and total weight.
4. In matrix Prim, show crossed rows, numbered columns and selected entries.
5. In Dijkstra, show final label \(0\) at the start, working values, final labels, order of finalising and traceback.
6. For traceback use:
   \[
   d(B)-d(A)=w(AB).
   \]
7. Keep integer weights exact.
8. Include units where the context gives them.
9. Equal weights may lead to more than one valid MST or shortest route.
10. Keep Kruskal and Floyd outside the required core for this evidence-backed CCEA FAS2 lesson unless future CCEA evidence confirms otherwise.

## 16. Syllabus Gap Check

| LO ID | Official wording | Coverage in this lesson | Status |
|---|---|---|---|
| `FAS2-ALGGRAPH-LO001` | demonstrate understanding of the definition of an algorithm, including the term greedy algorithm | Algorithm and greedy algorithm defined and used. | Covered |
| `FAS2-ALGGRAPH-LO002` | solve problems involving critical path analysis, including a precedence table for an activity network, event times and float times, and an algorithm for finding the critical path | Not taught due missing lesson-specific evidence. | Missing evidence |
| `FAS2-ALGGRAPH-LO003` | recall and use Prim's algorithm to find a minimal spanning tree for a connected weighted graph | Prim taught on graph and matrix. | Covered |
| `FAS2-ALGGRAPH-LO004` | recall binary trees and traverse them using breadth first search and depth first search | Not taught due missing lesson-specific evidence. | Missing evidence |
| `FAS2-ALGGRAPH-LO005` | recall and use Dijkstra's algorithm to find a shortest path | Dijkstra taught with final labels and traceback. | Covered |

### Off-Spec Content Found but Excluded

#### Kruskal’s algorithm

The supplied lesson evidence gives extensive Kruskal content. However, Kruskal is not named in the supplied CCEA FAS2 Algorithms on Graphs LO wording. It is excluded from required core and may be used only as optional enrichment.

#### Floyd’s algorithm

The supplied evidence includes Floyd’s algorithm and identifies some content as A2. The uploaded PDF title also says it contains Floyd A2 content. Floyd is excluded from required core and may be used as optional enrichment only.

#### Prim’s order/complexity proof

The transcript includes a proof that Prim’s algorithm has cubic order when applied to an \(n\times n\) distance matrix. This is excluded from core because the supplied CCEA FAS2 LO wording does not require it.

### Optional Enrichment Not Required by CCEA

- Kruskal’s algorithm;
- comparison of Kruskal and Prim;
- Floyd’s algorithm;
- Floyd-Warshall/Roy-Warshall historical naming;
- order/complexity of Prim’s algorithm;
- real-world MST applications such as cluster analysis, face tracking and network-cycle avoidance.

### Missing Evidence Log

| Missing evidence | Effect | Required future action |
|---|---|---|
| CCEA-specific worked examples for FAS2 Algorithms on Graphs | Cannot claim CCEA past-paper style beyond broad method. | Add CCEA exam-question evidence or mark schemes. |
| Critical path analysis evidence | `FAS2-ALGGRAPH-LO002` not covered. | Build separate lesson section or chapter. |
| Binary tree BFS/DFS evidence | `FAS2-ALGGRAPH-LO004` not covered. | Build separate lesson section or chapter. |
| Full inspectable screenshot detail for all 150 pages | Some diagrams cannot be preserved fully. | Provide targeted screenshots or searchable slide text. |
| CCEA confirmation of Kruskal or Floyd | Cannot include as required core. | Keep as enrichment unless confirmed by official CCEA source. |

## 17. Recommended Enhancements Not in the Evidence

AI-proposed enhancements:

- algorithm-choice flowchart;
- “allowed edge” spotlight for Prim;
- Dijkstra label-box anatomy;
- traceback subtraction ladder;
- animation of Prim growing a tree;
- animation of Dijkstra expanding certainty;
- “legal or illegal” Prim widget;
- “traceback detective” Dijkstra widget;
- extra examples with disconnected graphs, equal-weight MST choices, and multiple shortest routes.

These are proposed enhancements, not evidence-backed source details.

## 18. Supplementary Sources Used

Project Sources used:

- `CCEA_GCE_Further_Mathematics_Specification_Map.md`;
- `Further_Maths_README_module_map.md`;
- `Further_Maths_EVIDENCE_DROP_CHECKLIST.md`;
- `Ordinary_A_Level_Maths_Bridge_Spec_Extracts.md`;
- `Further Maths Portal Build – Knowledge Evidence.txt`.

Lesson-specific sources used:

- `Decision Maths 1 Chapter 3 Algorithms on Graphs (including Floyd A2 content).pdf`;
- `transcripts.md`;
- `Chapter_3_Algorithms_on_Graphs_💻_(Decision_1)_screenshots.pdf`.

Ordinary A-Level Mathematics sources were used only for bridge context. They do not override Further Mathematics content.

Cross-board or third-party sources were used only where the supplied CCEA Further Mathematics specification boundary confirms the content is relevant.

## 19. Final Student Checklist

### Prerequisite confidence

- [ ] I can recognise vertices and edges/arcs.
- [ ] I can read edge weights accurately.
- [ ] I can explain connected graph, path, tree, cycle and spanning tree.
- [ ] I can add a list of edge weights without slips.
- [ ] I can compare values and identify the smallest valid value.

### Prim’s algorithm

- [ ] I can identify a minimal spanning tree/minimum connector question.
- [ ] I can choose a starting vertex.
- [ ] I can list candidate edges from the current tree to new vertices.
- [ ] I can choose the smallest legal edge.
- [ ] I can avoid cycles.
- [ ] I can include every vertex.
- [ ] I can state selected edges and total weight.

### Prim from a matrix

- [ ] I can cross the row of each added vertex.
- [ ] I can number the column of each added vertex.
- [ ] I can choose only from numbered columns and uncrossed rows.
- [ ] I can translate a matrix entry into an edge.
- [ ] I can calculate the total weight.

### Dijkstra’s algorithm

- [ ] I can identify a shortest-path question.
- [ ] I can put final label \(0\) at the start vertex.
- [ ] I can calculate working values using \(d(X)+w(XY)\).
- [ ] I can replace a working value only when the new value is smaller.
- [ ] I can select the smallest working value as the next final label.
- [ ] I can stop when the destination vertex is final.
- [ ] I can trace back using \(d(B)-d(A)=w(AB)\).
- [ ] I can state the route and shortest distance.

### Final confidence statement

I can identify whether a network problem needs Prim’s algorithm or Dijkstra’s algorithm, carry out the algorithm step by step, show my working clearly, and state the final tree or route with its total weight.
