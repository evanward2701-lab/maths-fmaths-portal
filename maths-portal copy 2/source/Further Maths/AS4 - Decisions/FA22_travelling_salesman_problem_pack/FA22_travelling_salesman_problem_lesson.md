# The Travelling Salesman Problem and the Nearest Neighbour Algorithm

```yaml
date_generated: 2026-06-05
course: CCEA GCE Further Mathematics
unit_code: FA22
unit_name: Further A2 2 Applied Mathematics
applied_section: "Section D: Discrete and Decision Mathematics"
topic_code: FA22-ALGGRAPH
topic_name: "Algorithms on graphs: Travelling Salesman Problem and nearest neighbour algorithm"
topic_slug: travelling_salesman_problem
topic_pascal: TravellingSalesmanProblem
topic_id: FA22TravellingSalesmanProblem
lesson_file: FA22_travelling_salesman_problem_lesson.md
core_lo_ids:
  - FA22-ALGGRAPH-LO001
related_prerequisite_further_maths_lo_ids:
  - FAS2-GRAPH-LO003
  - FAS2-GRAPH-LO005
  - FAS2-ALGGRAPH-LO003
  - FAS2-ALGGRAPH-LO005
bridge_tags:
  - tables
  - counting
  - inequalities
  - optimisation
  - algorithmic_reasoning
topic_tags:
  - FA22
  - ALGGRAPH
  - Decision
  - GraphTheory
  - HamiltonianCycle
  - NearestNeighbourAlgorithm
  - TravellingSalesmanProblem
```

## 1. Lesson Title and Metadata

**Course:** CCEA GCE Further Mathematics  
**Unit:** FA22, Further A2 2 Applied Mathematics  
**Applied section:** Section D, Discrete and Decision Mathematics  
**Topic code:** FA22-ALGGRAPH  
**Topic ID:** FA22TravellingSalesmanProblem  
**Lesson file:** `FA22_travelling_salesman_problem_lesson.md`  
**Core LO ID:** FA22-ALGGRAPH-LO001  
**Core official wording:** recall and use the nearest neighbour algorithm to construct a Hamiltonian cycle.

### Student-facing summary

The travelling salesman problem asks for a shortest route that visits all required places and returns to the start. In CCEA FA22, the essential algorithmic skill is to **recall and use the nearest neighbour algorithm to construct a Hamiltonian cycle**.

That means we are not trying to solve every possible TSP by brute force. Instead, we use a clear greedy algorithm:

1. start at a specified vertex;
2. go to the nearest unvisited vertex;
3. repeat until every vertex has been visited;
4. return to the starting vertex;
5. state the Hamiltonian cycle and its total length.

The main exam danger is that the nearest neighbour algorithm feels obvious, so students rush it. The marks live in the small details: crossing off visited vertices, not returning home too early, writing the route, and adding the correct table entries.

## 2. Evidence Map

| Source | Evidence used | Lesson role |
|---|---|---|
| CCEA Further Mathematics specification map | FA22-ALGGRAPH-LO001 | Core syllabus authority |
| Uploaded teacher transcript | TSP versus route inspection; classical/practical TSP; tour/Hamiltonian cycle; nearest neighbour explanation; exam warnings | Main lesson explanation evidence |
| Uploaded slide PDF | Definitions, bounds diagram, least-distance matrix, NNA algorithm, MST/RMST context | Slide-backed terminology and visual placeholders |
| Uploaded screenshot PDF | Visual confirmations of diagrams, tables and annotations | Visual plan only |
| Ordinary A-Level Maths bridge extracts | Table reading, inequalities, counting, optimisation language, algorithmic reasoning | Bridge context only |
| Cross-board Decision 1 content | MST/RMST bounds, Pearson exercise references, route inspection comparison | Boundary-controlled context/enrichment |

**Evidence limitation note.** The screenshot PDF contains visual pages but no parsed text. Visual evidence from it is used only where the visible rendered page details are readable. No hidden or uninspected screenshot detail is claimed. The slide PDF and transcript are cross-board Decision 1 materials. They are useful, but they do **not** override the CCEA FA22 specification boundary.

## 3. Specification Alignment

| LO ID | Official wording | Lesson coverage | Evidence source | Boundary note | Ordinary A-Level bridge |
|---|---|---|---|---|---|
| **FA22-ALGGRAPH-LO001** | recall and use the nearest neighbour algorithm to construct a Hamiltonian cycle | Full coverage: algorithm statement, route construction, table use, repeated starting vertices, total length, exam wording | CCEA spec map; uploaded transcript; uploaded slide PDF | Core CCEA content | Uses table reading, inequalities, systematic arithmetic and optimisation language |
| FAS2-GRAPH-LO003 | Hamiltonian paths/cycles and traversability concepts | Used as prerequisite language only | CCEA spec map; uploaded TSP definitions | Not current FA22 core LO | No direct ordinary A-Level graph theory predecessor |
| FAS2-GRAPH-LO005 | Trees and spanning trees | Used only to explain why MST content appears in the evidence | CCEA spec map; uploaded slides | Not core for this FA22 lesson | Links to structured methods and connected diagrams |
| FAS2-ALGGRAPH-LO003 | Prim’s algorithm for minimal spanning trees | Optional contextual note for upper bounds | CCEA spec map; uploaded evidence | Not taught as core here | Algorithmic step discipline |
| FAS2-ALGGRAPH-LO005 | Dijkstra’s shortest path algorithm | Mentioned as a possible way to generate least-distance tables | CCEA spec map; uploaded evidence | Not taught as core here | Table and path comparison reasoning |

## 4. Learning Objectives

### Core Further Maths objectives

By the end of this lesson, you should be able to:

1. define a Hamiltonian cycle in the context of a weighted graph or distance table;
2. explain why the travelling salesman problem is about visiting vertices, not necessarily every edge;
3. apply the nearest neighbour algorithm from a specified starting vertex;
4. construct the resulting Hamiltonian cycle;
5. calculate the total length of the Hamiltonian cycle;
6. compare two nearest-neighbour routes and choose the better upper bound when asked.

### Bridge objectives

You should be able to connect this topic to ordinary Maths habits:

1. read a two-way table accurately;
2. compare numerical quantities using inequalities;
3. use factorial counting to understand why brute force becomes unrealistic;
4. keep an ordered method record rather than doing mental jumps.

### Exam technique objectives

You should be able to:

1. write the route clearly, for example \(A\to D\to E\to C\to F\to B\to A\);
2. show the route length as a sum of selected edge weights;
3. avoid revisiting a vertex before all vertices have been visited;
4. return to the start only at the final step;
5. state that nearest neighbour gives a Hamiltonian cycle, but not necessarily the optimal Hamiltonian cycle.

## 5. Explicit Prerequisite Recap

### GCSE foundations

You should already be comfortable with adding positive numbers accurately, comparing numbers, reading rows and columns in a table, understanding an ordered route, and using inequalities such as \(<,>,\leq,\geq\).

### Ordinary AS/A2 Mathematics foundations

Ordinary A-Level Maths does not normally teach graph algorithms as a central topic, so the bridge is more about transferable habits than direct content. You should already have met structured table work, exact arithmetic, sequences of decisions in multi-step problems, inequalities, optimisation language and factorial notation such as \(n!\).

### Previous Further Mathematics foundations

This lesson leans on earlier discrete and decision ideas:

- a **graph** has vertices and edges;
- a **weighted graph** has numbers attached to edges;
- a **network** can represent roads, flights, towns, classrooms or delivery points;
- a **cycle** begins and ends at the same vertex;
- a **Hamiltonian cycle** visits every vertex exactly once before returning to the start;
- Prim’s and Dijkstra’s algorithms may appear in surrounding questions, but they are not the core of this lesson.

### A-Level Maths Bridge: What You Already Know and What Further Maths Changes

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| Algebra and arithmetic fluency | Keep exact totals and avoid premature rounding | Route lengths are sums of edge weights from a table or graph | One arithmetic slip can change the chosen “nearest” vertex |
| Tables and data interpretation | Read entries by matching row and column | A distance matrix gives the weights between vertices | In symmetric tables, \(AB=BA\), but you must still read the correct entry |
| Inequalities | Decide which of two numbers is smaller/larger | The nearest neighbour algorithm repeatedly chooses the smallest valid entry | The smallest entry overall is not always allowed; it must be from the current vertex to an unvisited vertex |
| Counting with factorials | \(n!\) counts arrangements | The number of possible Hamiltonian cycles grows very quickly | Do not try to list every route unless the network is tiny |
| Optimisation language | A minimum is the smallest possible value under conditions | TSP seeks a shortest Hamiltonian cycle | NNA gives a route, but not necessarily the optimal route |
| Structured method writing | Showing ordered steps in a calculation | Algorithms must be recorded as ordered vertex choices and route lengths | Marks can be lost for giving only the final number without the route |

In ordinary A-Level Maths, this idea appeared as choosing, comparing and organising numbers carefully. In Further Maths, the same idea becomes an algorithm on a graph. The key upgrade is that every choice changes the next row of the table you are allowed to use. The danger is treating “nearest” as “smallest number anywhere in the table” rather than “smallest available distance from the vertex I am currently at.”

## 6. Big Picture Explanation

The travelling salesman problem is a routing problem. A person, vehicle or process must visit a list of places and return to the start while keeping the total route length as small as possible.

The uploaded evidence contrasts this with route inspection:

- route inspection is interested in travelling along **every edge**;
- the travelling salesman problem is interested in visiting **every vertex**.

So if a graph represents streets, route inspection is a postman walking every street. If a graph represents delivery locations, TSP is a courier visiting every delivery point.

### Classical and practical TSP

**Classical TSP:** each vertex is visited **exactly once** before returning to the start. This is directly linked to a Hamiltonian cycle.

**Practical TSP:** each vertex is visited **at least once** before returning to the start. This allows repeated vertices. In CCEA FA22 nearest-neighbour questions, the algorithm constructs a Hamiltonian cycle, so you should think in the classical sense unless the question explicitly says otherwise.

### Why not just test every route?

For a complete undirected network with \(n\) vertices, if reversed cycles are the same and the starting point is fixed, the number of distinct Hamiltonian cycles is

\[
\frac{(n-1)!}{2}.
\]

For \(20\) cities:

\[
\frac{19!}{2}=60\,822\,550\,204\,416\,000.
\]

That is over \(60\) quadrillion possible cycles. This is why the course uses algorithms and bounds rather than brute force.

## 7. Key Definitions and Notation

A **vertex** is a point in a graph. An **edge** is a connection between two vertices. A **weighted edge** is an edge with a number attached, representing distance, time, cost or length.

A **walk** in a network is a finite sequence of edges such that the end vertex of one edge is the start vertex of the next.

A **tour** is a walk which visits every vertex and returns to its starting vertex.

A **Hamiltonian cycle** is a tour which visits every vertex exactly once before returning to the start.

For example, in a graph with vertices \(A,B,C,D,E\), the route

\[
A\to B\to D\to C\to E\to A
\]

is Hamiltonian if all vertices are visited exactly once before returning to \(A\).

The **Travelling Salesman Problem** involves finding a tour of minimum total weight. In this lesson, the CCEA core method is:

\[
\text{use nearest neighbour to construct a Hamiltonian cycle.}
\]

A **distance matrix** is a table giving distances between pairs of vertices. For a non-directional network, the matrix is symmetric:

\[
AB=BA.
\]

An **upper bound** for the TSP is the length of a valid route that visits all vertices and returns to the start. The nearest neighbour algorithm produces a Hamiltonian cycle, so its length is an upper bound.

## 8. Core Theory

### 8.1 Boundary control

The uploaded Decision 1 evidence teaches a full travelling salesman chapter. The CCEA FA22 core learning outcome identified for this lesson is narrower:

\[
\boxed{\text{Recall and use the nearest neighbour algorithm to construct a Hamiltonian cycle.}}
\]

The wider TSP ideas are used as context, prerequisite support or optional enrichment.

### 8.2 TSP as a vertex problem

The travelling salesman problem is concerned with visiting vertices. The edges represent travel links, but TSP does **not** ask you to travel every edge.

| Problem type | Main target | Route requirement |
|---|---|---|
| Route inspection | Edges | Travel along every edge |
| Travelling salesman | Vertices | Visit every vertex and return to the start |

### 8.3 Tours and Hamiltonian cycles

A **tour** is a walk that visits every vertex and returns to the starting vertex.

A **Hamiltonian cycle** is a tour that visits every vertex exactly once before returning to the starting vertex.

For FA22-ALGGRAPH-LO001, the nearest neighbour algorithm must construct a Hamiltonian cycle. The route should therefore look like:

\[
\text{start}\to \text{new vertex}\to \text{new vertex}\to \cdots \to \text{last new vertex}\to \text{start}.
\]

The start appears twice in the written route only because it appears at the beginning and at the end.

### 8.4 Least-distance tables

The nearest neighbour algorithm is usually applied to a complete distance table. A complete distance table gives a distance between every pair of vertices.

\[
\begin{array}{c|cccc}
 & A & B & C & D\\
\hline
A & - & 7 & 4 & 10\\
B & 7 & - & 5 & 8\\
C & 4 & 5 & - & 6\\
D & 10 & 8 & 6 & -
\end{array}
\]

The dash means “do not travel from a vertex to itself”. If the network is non-directional, the table is symmetric.

### 8.5 Triangle inequality and shortcuts

The triangle inequality says:

\[
\text{longest side} \leq \text{sum of the two shorter sides}.
\]

Suppose the direct edge \(BC\) has weight \(27\), but

\[
BA=11,\qquad AC=13.
\]

Then

\[
BA+AC=11+13=24.
\]

Since

\[
24<27,
\]

the route \(B\to A\to C\) is shorter than the direct edge \(B\to C\). The least-distance table should use \(BC=24\), not \(27\).

**Bridge Note:** In ordinary A-Level Maths, inequalities were used to compare sizes. Here, the comparison decides which route is genuinely shortest.

### 8.6 Brute force route count

If a complete undirected network has \(n\) vertices, then the number of distinct Hamiltonian cycles is

\[
\frac{(n-1)!}{2}.
\]

For \(20\) vertices:

\[
\frac{19!}{2}=60\,822\,550\,204\,416\,000.
\]

This is the mathematical reason for using algorithms and bounds rather than trying every route.

### 8.7 Upper bounds

If nearest neighbour produces a route of length \(L\), then

\[
\text{optimal route length}\leq L.
\]

For CCEA nearest neighbour work:

\[
\boxed{\text{Nearest neighbour gives an upper bound, not necessarily the optimum.}}
\]

### 8.8 The nearest neighbour algorithm

The nearest neighbour algorithm is greedy. At each step, choose:

\[
\boxed{\text{the nearest vertex that has not yet been visited.}}
\]

For a specified starting vertex:

1. Start at the specified vertex.
2. From the current vertex, choose the nearest vertex that has **not** yet been visited.
3. Move to that vertex.
4. Repeat until every vertex has been visited.
5. Return directly to the starting vertex.
6. Write down the Hamiltonian cycle.
7. Add the selected edge weights to find the total length.

If the route generated is

\[
A\to D\to C\to B\to E\to A,
\]

then the route length is

\[
AD+DC+CB+BE+EA.
\]

### 8.9 All starting vertices

If a question asks you to apply nearest neighbour starting from each vertex, record every Hamiltonian cycle and every length, then choose the smallest generated length as the best nearest-neighbour upper bound.

This does not automatically prove it is the true optimum. It proves there is a Hamiltonian cycle of that length.

### 8.10 Current row discipline

If the current vertex is \(C\), look along row \(C\), but only choose from vertices not yet visited.

Example: route so far:

\[
A\to D\to C.
\]

Visited vertices are \(A,D,C\). If row \(C\) gives

\[
CB=6,\qquad CE=10,
\]

then choose \(B\), because \(6<10\). You may not choose \(D\), even if \(CD\) is smaller, because \(D\) has already been visited.

**Bridge Note:** In ordinary table work, you could often just pick the smallest number in a row. Here, the table has a memory. Previously visited vertices are closed doors.

### 8.11 Ties

If two unvisited vertices are equally near, state the tie clearly. For example:

\[
EC=EF=12.
\]

If no tie-breaking rule is supplied, either route may be valid, but if asked for the best upper bound, try both tied branches and compare.

### 8.12 Nearest neighbour versus Prim’s algorithm

| Feature | Nearest neighbour | Prim’s algorithm |
|---|---|---|
| Purpose | Construct a Hamiltonian cycle | Construct a minimum spanning tree |
| Shape produced | Cycle returning to start | Tree with no cycle |
| Next choice comes from | Most recently chosen vertex | Any vertex already in the growing tree |
| FA22 role here | Core LO | Prerequisite/context only |

Nearest neighbour thinks like a traveller. Prim thinks like a tree-builder.

### 8.13 Full method template

Start at \(A\). From \(A\), the nearest unvisited vertex is \(D\), so choose \(A\to D\). From \(D\), choose the nearest unvisited vertex. Continue until all vertices have been visited, then return to \(A\). State:

\[
\boxed{A\to D\to C\to B\to E\to A}
\]

and compute:

\[
AD+DC+CB+BE+EA.
\]

## 9. Visual Asset Integration

[VISUAL PLACEHOLDER: FA22TravellingSalesmanProblemMermaid-001 | Source: CCEA FA22-ALGGRAPH-LO001 + uploaded nearest-neighbour slide evidence | Insert from mermaid/FA22TravellingSalesmanProblemMermaid-001.md | Purpose: Show the nearest neighbour algorithm as a decision flow from starting vertex to final Hamiltonian cycle.]

[VISUAL PLACEHOLDER: FA22TravellingSalesmanProblemSVG-001 | Source: Uploaded slide definitions + transcript terminology | Insert from svg/FA22TravellingSalesmanProblemSVG-001.svg | Purpose: Distinguish a walk, a tour and a Hamiltonian cycle using the same small graph.]

[VISUAL PLACEHOLDER: FA22TravellingSalesmanProblemSVG-002 | Source: Uploaded “Matrix for a complete network of least distances” slide | Insert from svg/FA22TravellingSalesmanProblemSVG-002.svg | Purpose: Show why a non-directional least-distance matrix is symmetric and how the same value appears as \(AB\) and \(BA\).]

[VISUAL PLACEHOLDER: FA22TravellingSalesmanProblemSVG-003 | Source: Uploaded nearest-neighbour algorithm evidence | Insert from svg/FA22TravellingSalesmanProblemSVG-003.svg | Purpose: Demonstrate choosing the nearest unvisited vertex from the current row of a distance table.]

[VISUAL PLACEHOLDER: FA22TravellingSalesmanProblemBridgeSVG-001 | Source: Ordinary A-Level Maths bridge + Further Maths specification | Insert from svg/FA22TravellingSalesmanProblemBridgeSVG-001.svg | Purpose: Compare prior ordinary Maths method with Further Maths extension.]

[VISUAL PLACEHOLDER: FA22TravellingSalesmanProblemTikZ-001 | Source: AI-proposed teaching enhancement based on uploaded NNA evidence | Insert from tikz/FA22TravellingSalesmanProblemTikZ-001.tex | Purpose: Provide a clean weighted complete graph matching the main generated nearest-neighbour worked example.]

## 10. Interactive Learning Widgets

[INTERACTIVE PLACEHOLDER: FA22TravellingSalesmanProblemWidget-001 | Source: AI-proposed teaching enhancement based on CCEA FA22-ALGGRAPH-LO001 and uploaded nearest-neighbour evidence | Insert from widgets/FA22TravellingSalesmanProblemWidget-001.html | Purpose: Let the student step through the nearest neighbour algorithm from a chosen starting vertex.]

The widget allows the student to choose a start vertex, see the current row of a distance table, click the nearest unvisited vertex, receive instant feedback, watch the Hamiltonian cycle build, and see the final route length.

[INTERACTIVE PLACEHOLDER: FA22TravellingSalesmanProblemWidget-002 | Source: AI-proposed teaching enhancement based on common nearest-neighbour mistakes | Insert from widgets/FA22TravellingSalesmanProblemWidget-002.html | Purpose: Check whether a typed route is a valid Hamiltonian cycle and calculate its length.]

The student inputs a route such as \(A,D,C,B,E,A\). The widget checks whether the route starts and ends at the same vertex, whether every vertex is included, whether any vertex is repeated before the final return, which edge weights are used, and the final total length.

## 11. Worked Examples

### Worked Example 1: Completing a table of least distances from a visible network

**Evidence source:** Uploaded screenshot/slide/transcript evidence from the TSP table-of-least-distances recap.  
**On-spec status:** Supporting prerequisite/context for nearest neighbour.

The visible network has vertices \(A,B,C,D,E\) and edges:

\[
AC=13,\quad AB=11,\quad CB=27,\quad CE=18,\quad ED=14,\quad DB=8.
\]

Complete the least-distance table.

Because the network is non-directional, \(AB=BA\), \(AC=CA\), and so on.

\(A\) to \(B\):

\[
AB=11.
\]

\(A\) to \(C\):

\[
AC=13.
\]

\(A\) to \(D\): compare

\[
A\to B\to D=11+8=19
\]

and

\[
A\to C\to E\to D=13+18+14=45.
\]

Since \(19<45\),

\[
AD=19.
\]

\(A\) to \(E\): compare

\[
A\to C\to E=13+18=31
\]

and

\[
A\to B\to D\to E=11+8+14=33.
\]

Since \(31<33\),

\[
AE=31.
\]

\(B\) to \(C\): the direct edge is \(BC=27\), but

\[
B\to A\to C=11+13=24.
\]

Since \(24<27\),

\[
BC=24.
\]

\(B\) to \(D\):

\[
BD=8.
\]

\(B\) to \(E\):

\[
B\to D\to E=8+14=22.
\]

So \(BE=22\).

\(C\) to \(D\):

\[
C\to E\to D=18+14=32.
\]

Also,

\[
C\to A\to B\to D=13+11+8=32.
\]

So \(CD=32\).

\(C\) to \(E\): \(CE=18\).  
\(D\) to \(E\): \(DE=14\).

Completed table:

\[
\begin{array}{c|ccccc}
 & A & B & C & D & E\\
\hline
A & - & 11 & 13 & 19 & 31\\
B & 11 & - & 24 & 8 & 22\\
C & 13 & 24 & - & 32 & 18\\
D & 19 & 8 & 32 & - & 14\\
E & 31 & 22 & 18 & 14 & -
\end{array}
\]

The trap is \(BC\). The diagram shows \(BC=27\), but the least distance is \(24\).

### Worked Example 2: Nearest neighbour from a specified starting vertex

Use the nearest neighbour algorithm, starting at \(A\), for:

\[
\begin{array}{c|ccccc}
 & A & B & C & D & E\\
\hline
A & - & 9 & 7 & 5 & 8\\
B & 9 & - & 6 & 4 & 3\\
C & 7 & 6 & - & 2 & 10\\
D & 5 & 4 & 2 & - & 11\\
E & 8 & 3 & 10 & 11 & -
\end{array}
\]

Start at \(A\). From row \(A\):

\[
AB=9,\quad AC=7,\quad AD=5,\quad AE=8.
\]

Nearest is \(D\), so choose \(A\to D\).

Now from \(D\), ignoring visited \(A\):

\[
DB=4,\quad DC=2,\quad DE=11.
\]

Nearest is \(C\), so choose \(D\to C\).

Now from \(C\), ignoring \(A,D\):

\[
CB=6,\quad CE=10.
\]

Nearest is \(B\), so choose \(C\to B\).

Only \(E\) remains, so choose \(B\to E\). Then return \(E\to A\).

The Hamiltonian cycle is

\[
A\to D\to C\to B\to E\to A.
\]

The length is

\[
AD+DC+CB+BE+EA=5+2+6+3+8=24.
\]

Final answer:

\[
\boxed{A\to D\to C\to B\to E\to A,\quad \text{upper bound}=24.}
\]

### Worked Example 3: Nearest neighbour from two specified starts

The table below represents shortest distances between six locations \(A,B,C,D,E,F\):

\[
\begin{array}{c|rrrrrr}
 & A & B & C & D & E & F\\
\hline
A & - & 135 & 180 & 70 & 95 & 225\\
B & 135 & - & 215 & 125 & 205 & 240\\
C & 180 & 215 & - & 150 & 165 & 155\\
D & 70 & 125 & 150 & - & 100 & 195\\
E & 95 & 205 & 165 & 100 & - & 215\\
F & 225 & 240 & 155 & 195 & 215 & -
\end{array}
\]

Starting at \(A\):

\[
A\to D\to E\to C\to F\to B\to A.
\]

Length:

\[
AD+DE+EC+CF+FB+BA=70+100+165+155+240+135=865.
\]

Starting at \(B\):

\[
B\to D\to A\to E\to C\to F\to B.
\]

Length:

\[
BD+DA+AE+EC+CF+FB=125+70+95+165+155+240=850.
\]

Since

\[
850<865,
\]

the better upper bound is

\[
\boxed{850}.
\]

### Worked Example 4: A tie in nearest neighbour

Two possible nearest-neighbour cycles beginning at \(E\) are:

\[
E\to C\to D\to F\to A\to B\to E
\]

and

\[
E\to F\to A\to B\to D\to C\to E.
\]

For cycle 1:

\[
EC+CD+DF+FA+AB+BE=12+4+13+11+12+24=76.
\]

For cycle 2:

\[
EF+FA+AB+BD+DC+CE=12+11+12+8+4+12=59.
\]

Since \(59<76\), cycle 2 gives the better upper bound:

\[
\boxed{E\to F\to A\to B\to D\to C\to E,\quad \text{upper bound}=59.}
\]

## 12. Common Mistakes and Exam Traps

1. **Choosing the nearest vertex overall, not the nearest from the current vertex.** Nearest neighbour is local to the current vertex.
2. **Forgetting “unvisited”.** A small edge to an already visited vertex is not allowed.
3. **Returning to the start too early.** Return only after all vertices have been visited.
4. **Omitting the final return edge.** Without the final edge, you have a path, not a cycle.
5. **Repeating a vertex before all vertices have been visited.** This is not a Hamiltonian cycle.
6. **Mixing up nearest neighbour and Prim’s algorithm.** Nearest neighbour follows the current vertex; Prim grows a tree from any selected vertex.
7. **Thinking nearest neighbour proves optimality.** It gives an upper bound, not necessarily the shortest route.
8. **Adding the wrong table entries.** Add only the edges in the stated route.
9. **Ignoring ties.** State ties and follow the question’s tie rule or compare branches when required.

## 13. Practice Questions

### Question 1

A network has vertices \(A,B,C,D\). Decide whether each route is a Hamiltonian cycle.

1. \(A\to B\to C\to D\to A\)
2. \(A\to B\to C\to B\to D\to A\)
3. \(A\to C\to D\to A\)
4. \(B\to D\to A\to C\to B\)

### Question 2

The route \(A\to C\to D\to B\to A\) has edge weights:

\[
AC=6,\quad CD=5,\quad DB=8,\quad BA=7.
\]

Find the route length.

### Question 3

Explain the difference between a tour and a Hamiltonian cycle.

### Question 4

For a complete undirected network with \(7\) vertices, calculate:

\[
\frac{(7-1)!}{2}.
\]

### Question 5

A distance table contains \(AB=20, AC=7, CB=9\). Explain why the least distance from \(A\) to \(B\) should be \(16\), not \(20\), if travel through \(C\) is allowed.

### Question 6

Use the nearest neighbour algorithm, starting at \(A\), for:

\[
\begin{array}{c|ccccc}
 & A & B & C & D & E\\
\hline
A & - & 14 & 9 & 6 & 18\\
B & 14 & - & 7 & 10 & 5\\
C & 9 & 7 & - & 4 & 11\\
D & 6 & 10 & 4 & - & 13\\
E & 18 & 5 & 11 & 13 & -
\end{array}
\]

State the Hamiltonian cycle and upper bound.

### Question 7

Use nearest neighbour, starting at \(C\), for:

\[
\begin{array}{c|cccccc}
 & A & B & C & D & E & F\\
\hline
A & - & 12 & 16 & 20 & 9 & 14\\
B & 12 & - & 10 & 8 & 15 & 11\\
C & 16 & 10 & - & 7 & 18 & 13\\
D & 20 & 8 & 7 & - & 6 & 17\\
E & 9 & 15 & 18 & 6 & - & 5\\
F & 14 & 11 & 13 & 17 & 5 & -
\end{array}
\]

### Question 8

Use nearest neighbour starting at \(A\) and then at \(D\). Choose the better upper bound.

\[
\begin{array}{c|ccccc}
 & A & B & C & D & E\\
\hline
A & - & 8 & 12 & 6 & 10\\
B & 8 & - & 5 & 7 & 9\\
C & 12 & 5 & - & 4 & 11\\
D & 6 & 7 & 4 & - & 3\\
E & 10 & 9 & 11 & 3 & -
\end{array}
\]

### Question 9

In a nearest-neighbour calculation starting from \(E\), the first step has a tie: \(EA=10, EB=10\). Explain what you should do.

### Question 10

A lower bound is \(142\). Nearest neighbour gives cycles of length \(168\) and \(155\). State the best upper bound and an interval for the optimal length, assuming the lower bound is not itself a Hamiltonian cycle.

## 14. Worked Solutions

### Solution 1

1. \(A\to B\to C\to D\to A\): yes.
2. \(A\to B\to C\to B\to D\to A\): no, \(B\) repeats.
3. \(A\to C\to D\to A\): no, \(B\) is missing.
4. \(B\to D\to A\to C\to B\): yes.

### Solution 2

\[
AC+CD+DB+BA=6+5+8+7=26.
\]

### Solution 3

A tour visits every vertex and returns to its starting vertex. A Hamiltonian cycle is a tour which visits every vertex exactly once before returning to the start.

### Solution 4

\[
\frac{(7-1)!}{2}=\frac{6!}{2}=\frac{720}{2}=360.
\]

### Solution 5

\[
AC+CB=7+9=16<20=AB.
\]

So the least distance from \(A\) to \(B\) is \(16\), using \(A\to C\to B\).

### Solution 6

Starting at \(A\):

\[
A\to D\to C\to B\to E\to A.
\]

Length:

\[
AD+DC+CB+BE+EA=6+4+7+5+18=40.
\]

### Solution 7

Starting at \(C\):

\[
C\to D\to E\to F\to B\to A\to C.
\]

Length:

\[
CD+DE+EF+FB+BA+AC=7+6+5+11+12+16=57.
\]

### Solution 8

Starting at \(A\):

\[
A\to D\to E\to B\to C\to A.
\]

Length:

\[
6+3+9+5+12=35.
\]

Starting at \(D\):

\[
D\to E\to B\to C\to A\to D.
\]

Length:

\[
3+9+5+12+6=35.
\]

Both give the same upper bound:

\[
\boxed{35}.
\]

### Solution 9

State the tie clearly:

\[
EA=EB=10.
\]

Choose consistently, or try both routes if asked for the best upper bound. Different tie choices may produce different Hamiltonian cycles.

### Solution 10

The best upper bound is the smaller of \(168\) and \(155\):

\[
\boxed{155}.
\]

Since the lower bound is not itself a Hamiltonian cycle:

\[
\boxed{142<\text{optimal length}\leq155.}
\]

## 15. Exam Technique Notes

- Write the algorithm route, not just the answer.
- Always work from the current vertex.
- Keep a visited list.
- Do not return to the start until the end.
- Include the final return edge in the length.
- If a tie occurs, show it.
- Know the status of your result: NNA gives an upper bound, not automatic optimality.
- Use exact values and include units when supplied.

## 16. Syllabus Gap Check

| LO ID | Official wording | Covered? | Lesson sections |
|---|---|---:|---|
| **FA22-ALGGRAPH-LO001** | recall and use the nearest neighbour algorithm to construct a Hamiltonian cycle | Yes | Sections 3, 4, 7, 8, 11, 13, 14, 15 |
| FAS2-GRAPH-LO003 | Hamiltonian paths/cycles and graph traversability concepts | Prerequisite only | Sections 5, 7 |
| FAS2-GRAPH-LO005 | Trees and spanning trees | Context only | Sections 8, 16, 17 |
| FAS2-ALGGRAPH-LO003 | Prim’s algorithm for MSTs | Context/enrichment only | Sections 8, 12, 16 |
| FAS2-ALGGRAPH-LO005 | Dijkstra’s shortest path algorithm | Context/enrichment only | Sections 8, 16 |

### Off-Spec Content Found but Excluded

- Full MST upper-bound method: included only as context/enrichment, not core FA22-ALGGRAPH-LO001.
- Full RMST lower-bound method: included only as optional enrichment/boundary note.
- Full exact TSP optimisation methods: excluded from core.
- External TSP research examples: motivation only.
- Pearson textbook exercise references: not treated as supplied textbook evidence.

### Optional Enrichment Not Required by CCEA

- Why exact TSP is computationally hard.
- Why \(\frac{(n-1)!}{2}\) counts distinct Hamiltonian cycles.
- MST upper-bound shortcut method.
- RMST lower-bound method.
- Comparing nearest neighbour with advanced optimisation approaches.

## 17. Recommended Enhancements Not in the Evidence

- An algorithm stepper widget.
- A Hamiltonian cycle validator.
- An “NNA versus Prim” comparison card.
- A tie-handling mini-example.
- A least-distance matrix visual.
- An exam route-length highlighter.

## 18. Supplementary Sources Used

- CCEA GCE Further Mathematics Specification Map.
- Further Maths README module map.
- Further Maths Evidence Drop Checklist.
- Further Maths Portal Build Knowledge Evidence.
- Ordinary A-Level Maths Bridge Spec Extracts, bridge context only.
- CCEA GCE Mathematics Specification Map, bridge context only.
- Uploaded `transcripts.md`.
- Uploaded `Decision Maths 1 chapter 5 The Travelling Salesman (A2 content).pdf`.
- Uploaded screenshot PDF, visual planning only.

## 19. Final Student Checklist

### Prerequisite confidence checklist

- [ ] I can identify vertices and edges in a weighted graph.
- [ ] I can read a distance from a table using row and column headings.
- [ ] I can recognise that a non-directional table is symmetric.
- [ ] I can compare distances to find the smallest valid entry.
- [ ] I can add route lengths accurately.

### Further Maths method checklist

- [ ] I can define a tour.
- [ ] I can define a Hamiltonian cycle.
- [ ] I can explain TSP as a vertex-visiting problem.
- [ ] I can start nearest neighbour from a specified vertex.
- [ ] I can choose the nearest unvisited vertex at each step.
- [ ] I can return to the starting vertex at the end.
- [ ] I can write the Hamiltonian cycle clearly.
- [ ] I can calculate the route length and state it as an upper bound.

### Exam technique checklist

- [ ] I show the route, not just the final length.
- [ ] I include the final return edge.
- [ ] I avoid revisiting vertices before the final return.
- [ ] I state ties clearly.
- [ ] I compare upper bounds by choosing the smaller one.
- [ ] I do not claim nearest neighbour proves optimality unless extra evidence is given.

Final mastery loop:

\[
\boxed{\text{current vertex}\to\text{nearest unvisited vertex}\to\text{repeat}\to\text{return to start}\to\text{state route and length}}
\]
