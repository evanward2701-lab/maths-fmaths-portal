# 1. Lesson Title and Metadata

## Lesson Title

Eulerian Traversability and Boundary-Controlled Route Inspection

## Metadata

| Field | Value |
|---|---|
| Date generated | 2026-06-05 |
| Course | CCEA GCE Further Mathematics |
| Unit | FAS2: Further AS 2 Applied Mathematics |
| Applied section | Section D: Discrete and Decision Mathematics |
| Primary topic code | FAS2-GRAPH |
| Supporting topic code | FAS2-ALGGRAPH |
| Topic name | Graph theory: Eulerian traversability and boundary-controlled route inspection |
| Topic slug | eulerian_traversability_and_route_inspection |
| Topic Pascal | EulerianTraversabilityAndRouteInspection |
| Topic ID | FAS2EulerianTraversabilityAndRouteInspection |
| Lesson file name | FAS2_eulerian_traversability_and_route_inspection_lesson.md |
| Core LO IDs | FAS2-GRAPH-LO001, FAS2-GRAPH-LO002, FAS2-GRAPH-LO003, FAS2-GRAPH-LO004, FAS2-GRAPH-LO005 |
| Supporting LO IDs | FAS2-ALGGRAPH-LO005 |
| Bridge tags | Ordinary Maths bridge, diagram interpretation, algebraic counting, proof and justification |
| Topic tags | Graph theory, Eulerian circuit, semi-Eulerian trail, traversability, weighted network, route inspection enrichment |

## Boundary Statement

The official CCEA core for this pack is graph theory and traversability: vertices, edges or arcs, degree, connectedness, circuits, Eulerian circuits, Hamiltonian paths, basic existence conditions and weighted edges. The uploaded lesson evidence is a Decision 1 route inspection chapter. The supplied CCEA Further Mathematics specification map does not explicitly name the Route Inspection Algorithm or Chinese Postman Problem as a CCEA learning outcome. Therefore Eulerian and semi-Eulerian graph theory is core, weighted graph interpretation is core, and route inspection is included as evidence-backed enrichment/application unless further CCEA evidence is supplied.

# 2. Evidence Map

| Evidence source | Use | Boundary status |
|---|---|---|
| CCEA_GCE_Further_Mathematics_Specification_Map.md | Unit, topic code, LO IDs, official syllabus boundary | Highest authority |
| Further_Maths_README_module_map.md | Metadata, workflow, phase structure | Project workflow |
| Further_Maths_EVIDENCE_DROP_CHECKLIST.md | Missing evidence and off-spec logging | Project workflow |
| Ordinary_A_Level_Maths_Bridge_Spec_Extracts.md | Ordinary Maths bridge | Bridge only |
| CCEA_GCE_Mathematics_Specification_Map.md | Ordinary Maths bridge context | Bridge only |
| Decision Maths 1 chapter 4 Route Inspection PDF | Eulerian/semi-Eulerian evidence, route inspection examples | Cross-board/third-party, boundary controlled |
| transcripts.md | Teacher explanations and warnings | Cross-board/third-party, boundary controlled |
| Chapter_4_Route_Inspection screenshots PDF | Visual slide evidence | Partially inspectable only |

# 3. Specification Alignment

| LO ID | Official wording | Lesson coverage | Boundary |
|---|---|---|---|
| FAS2-GRAPH-LO001 | demonstrate understanding of and use the basic concepts of graph theory, including vertex, edge, degree, planarity and subgraph | Vertices, edges/arcs, nodes, degree, connected graph, graph reduction | Core |
| FAS2-GRAPH-LO002 | demonstrate understanding of certain basic graphs, including the complete graph on \(n\) vertices \(K_n\), the complete bipartite graph \(K_{m,n}\) and the star on \(n\) vertices \(S_n\) | \(K_n\) classification for Eulerian/semi-Eulerian status | Core where used |
| FAS2-GRAPH-LO003 | demonstrate understanding of and use the traversability of graphs including circuits, Eulerian circuits and Hamiltonian paths, and basic conditions necessary for their existence | Eulerian circuits, semi-Eulerian trails, degree parity, connectedness | Main core |
| FAS2-GRAPH-LO004 | demonstrate understanding of and deal with weighted edges and digraphs | Weighted networks and edge weights | Weighted edges core; route inspection enrichment |
| FAS2-GRAPH-LO005 | demonstrate understanding of and use the basic concepts associated with trees: root, connectedness, binary tree and spanning tree | Connectedness and tree distinction | Supporting only |
| FAS2-ALGGRAPH-LO005 | recall and use Dijkstra's algorithm to find a shortest path | Shortest path subskill for route inspection enrichment | Supporting only |

# 4. Learning Objectives

## Core Further Maths Objectives

By the end of the core CCEA part of this lesson, the student should be able to define graph, vertex, edge, arc, degree and connectedness; find the degree of each vertex; use parity to decide whether a connected graph is Eulerian, semi-Eulerian or neither; explain why an Eulerian circuit requires every vertex to have even degree; explain why a semi-Eulerian trail has exactly two odd vertices; use the Handshake Lemma
\[
\sum_{v\in V}\deg(v)=2|E|;
\]
classify complete graphs \(K_n\); and interpret weighted edges.

## Boundary-Controlled Route Inspection Objectives

The student should understand route inspection as finding the shortest closed route that traverses every edge at least once, recognise the cases \(0\), \(2\), and \(4\) odd vertices, and keep this method labelled as evidence-backed enrichment/application rather than confirmed CCEA core from the supplied LO map.

# 5. Explicit Prerequisite Recap

## GCSE Foundations

Counting, adding labelled values, interpreting diagrams, distinguishing points from lines, following a route through a diagram, and recognising even and odd numbers.

## Ordinary AS/A2 Mathematics Foundations

Solving simple algebraic equations, reading diagrams accurately, justifying conclusions, listing cases systematically and interpreting results in context.

### A-Level Maths Bridge: What You Already Know and What Further Maths Changes

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| AS1 Algebra and Functions | Manipulating expressions and solving equations | Degree expressions can be added and equated to \(2|E|\) | Solving for \(n\) is not enough; interpret degree parity. |
| AS1/A21 proof and reasoning | Justifying a result with a chain of statements | Eulerian conditions must be explained, not guessed from a drawing | “It looks possible” is not proof. |
| Diagram interpretation | Reading labels and diagram features | A graph is an abstract network of vertices and edges | The visual layout can lie politely; adjacency tells the truth. |
| Counting skills | Listing possibilities systematically | Pairings of odd vertices must be complete and non-repeated | Missing one pairing can lose the optimum. |
| Ordinary modelling | Translating words into maths | Roads, bridges, paths and inspections become weighted networks | Real-world context does not override graph-theoretic requirements. |

In ordinary A-Level Maths, this idea appeared as careful diagram reading, algebraic counting and proof-style explanation. In Further Maths, the same idea becomes an abstract network: points are vertices, connections are edges, and the shape of the drawing is less important than which vertices are joined. The key upgrade is that a route problem becomes a structure problem. The danger is trying to trace by eye before proving whether tracing is possible.

# 6. Big Picture Explanation

Route and traversability questions ask whether a route can travel along every required connection without wasting movement. Euler’s Seven Bridges problem reduced a messy map to a graph: land masses became vertices and bridges became edges. Once the problem was stripped to its structure, the issue was degree parity. For a closed route, every time you enter a vertex you must leave it, so entries and exits come in pairs. Pairs give even degree. For an open route using every edge exactly once, the start vertex has one unpaired exit and the end vertex has one unpaired entry, so exactly two vertices have odd degree.

Route inspection adds weights. If the graph is already Eulerian, no repeats are needed. If it is not Eulerian, some edges must be repeated, and the question becomes: which repeated paths add the least extra weight?

# 7. Key Definitions and Notation

A graph is \(G=(V,E)\), where \(V\) is the set of vertices and \(E\) is the set of edges. A vertex or node is a point in the graph. An edge or arc is a connection between two vertices. If an edge joins \(A\) and \(B\), write \(AB\in E\). The degree of a vertex \(v\), written \(\deg(v)\), is the number of edges incident with it. A loop contributes \(2\) to the degree.

A graph is connected if every vertex can be reached from every other vertex by travelling along edges. A walk is a sequence of connected vertices and edges. A trail is a walk in which no edge is repeated. A circuit is a closed trail. An Eulerian circuit is a circuit that uses every edge exactly once. A connected graph is Eulerian iff every vertex has even degree. A connected graph is semi-Eulerian iff exactly two vertices have odd degree.

The Handshake Lemma is:
\[
\sum_{v\in V}\deg(v)=2|E|.
\]
Therefore the total degree is even and the number of odd-degree vertices is even.

A complete graph \(K_n\) has \(n\) vertices, with every vertex joined to every other vertex. Every vertex has degree \(n-1\). A weighted edge is an edge with a number attached, representing distance, time, cost or another quantity. The total weight \(W\) is the sum of all edge weights.

# 8. Core Theory

## 8.1 The Königsberg Bridge Problem

The question “Can one cross every bridge exactly once and return to the start?” becomes “Does the graph have an Eulerian circuit?” Since a closed route must enter and leave each vertex in pairs, every vertex must have even degree. In the Königsberg graph, the four land-mass vertices are odd, so no Eulerian circuit exists.

## 8.2 Why an Eulerian Circuit Needs Even Degrees

Suppose a route starts at vertex \(A\), travels along every edge exactly once, and returns to \(A\). Pick a vertex \(v\). Each time the route arrives at \(v\), it must later leave \(v\). Since the route is closed, even the starting vertex has its first departure paired with the final return. Hence the incident edges at \(v\) occur as enter/leave pairs:
\[
(\text{enter},\text{leave}),\quad (\text{enter},\text{leave}),\ldots
\]
so \(\deg(v)=2k\) for some integer \(k\ge 0\). Therefore \(\deg(v)\) is even.

**Bridge Note:** In ordinary Maths, proof often follows algebraic implication. Here the proof is structural: a route pattern forces even degree.

## 8.3 Eulerian Graph Theorem

\[
G\text{ is Eulerian}\iff G\text{ is connected and }\deg(v)\text{ is even for all }v\in V.
\]

Exam-style conclusion:
\[
\text{The graph is connected and all vertices have even degree, so it is Eulerian.}
\]

Connectedness is essential. A disconnected graph may have all even degrees but still cannot be traversed in a single route.

## 8.4 Semi-Eulerian Graphs

A semi-Eulerian trail uses every edge exactly once but starts and ends at different vertices. If the start vertex is \(S\), then its first leave is unpaired, so \(\deg(S)=1+2k\), odd. If the end vertex is \(T\), its final enter is unpaired, so \(\deg(T)=2m+1\), odd. Every other vertex has enter/leave pairs and even degree. Thus:
\[
G\text{ is semi-Eulerian}\iff G\text{ is connected and exactly two vertices have odd degree.}
\]

## 8.5 Classification Algorithm

1. Check connectedness. If disconnected, classify as neither for whole-graph traversability.
2. Count every vertex degree.
3. Count odd-degree vertices.
4. Use:

| Number of odd vertices | Classification |
|---:|---|
| 0 | Eulerian |
| 2 | Semi-Eulerian |
| 4,6,8,\ldots | Neither |
| 1,3,5,\ldots | Recount; impossible for a graph |

## 8.6 Handshake Lemma Example

A connected graph has 4 nodes and 8 edges. The degrees are
\[
2n-2,\quad n-1,\quad n-1,\quad n.
\]
Since there are 8 edges,
\[
(2n-2)+(n-1)+(n-1)+n=16.
\]
Collect like terms:
\[
5n-4=16.
\]
Add 4:
\[
5n=20.
\]
Divide by 5:
\[
n=4.
\]
Substitute:
\[
2n-2=6,\quad n-1=3,\quad n-1=3,\quad n=4.
\]
So the degrees are
\[
6,3,3,4.
\]
There are exactly two odd-degree vertices. Since the graph is connected, it is semi-Eulerian.

## 8.7 Complete Graphs \(K_n\)

In \(K_n\), every vertex has degree \(n-1\). If \(n=2k+1\), then \(n-1=2k\), even, so \(K_{2k+1}\) is Eulerian. \(K_2\) has two vertices of degree 1, so it is semi-Eulerian. For even \(n>2\), all \(n\) vertices are odd, so the graph is neither.

| Graph | Degree | Classification |
|---|---:|---|
| \(K_1\) | 0 | Eulerian |
| \(K_2\) | 1 | Semi-Eulerian |
| \(K_3\) | 2 | Eulerian |
| \(K_4\) | 3 | Neither |
| \(K_5\) | 4 | Eulerian |
| \(K_6\) | 5 | Neither |
| \(K_{2n+1}\) | \(2n\) | Eulerian |

## 8.8 Weighted Networks and Route Inspection Enrichment

Let \(W\) be the total weight of the network. Route inspection asks for the shortest closed route traversing every edge at least once. This is evidence-backed enrichment/application, not confirmed CCEA core from the supplied LO map.

If all vertices are even:
\[
\text{shortest closed inspection length}=W.
\]

If exactly two odd vertices \(A,B\):
\[
\text{shortest closed inspection length}=W+d(A,B),
\]
where \(d(A,B)\) is the shortest path length between them.

If four odd vertices \(A,B,C,D\):
\[
\text{length}=W+\min\{d(A,B)+d(C,D),d(A,C)+d(B,D),d(A,D)+d(B,C)\}.
\]

More than four odd vertices is excluded from core unless CCEA evidence confirms it.

# 9. Visual Asset Integration

[VISUAL PLACEHOLDER: FAS2EulerianTraversabilityAndRouteInspectionMermaid-001 | Source: CCEA graph traversability boundary + supplied Eulerian/semi-Eulerian evidence | Insert from mermaid/FAS2EulerianTraversabilityAndRouteInspectionMermaid-001.md | Purpose: Decision tree for classifying a connected graph as Eulerian, semi-Eulerian or neither.]

[VISUAL PLACEHOLDER: FAS2EulerianTraversabilityAndRouteInspectionMermaid-002 | Source: CCEA Further Maths specification boundary + supplied route inspection evidence | Insert from mermaid/FAS2EulerianTraversabilityAndRouteInspectionMermaid-002.md | Purpose: Separate CCEA core graph theory from route inspection enrichment.]

[VISUAL PLACEHOLDER: FAS2EulerianTraversabilityAndRouteInspectionMermaid-003 | Source: Supplied route inspection PDF and transcript | Insert from mermaid/FAS2EulerianTraversabilityAndRouteInspectionMermaid-003.md | Purpose: Route inspection method map for 0, 2 and 4 odd vertices.]

[VISUAL PLACEHOLDER: FAS2EulerianTraversabilityAndRouteInspectionSVG-001 | Source: Seven Bridges of Königsberg PDF slide + teacher transcript | Insert from svg/FAS2EulerianTraversabilityAndRouteInspectionSVG-001.svg | Purpose: Show map-to-graph abstraction from land masses and bridges.]

[VISUAL PLACEHOLDER: FAS2EulerianTraversabilityAndRouteInspectionSVG-002 | Source: Teacher transcript arrow explanation + screenshot annotations | Insert from svg/FAS2EulerianTraversabilityAndRouteInspectionSVG-002.svg | Purpose: Explain why entering and leaving a vertex gives even degree.]

[VISUAL PLACEHOLDER: FAS2EulerianTraversabilityAndRouteInspectionSVG-003 | Source: Supplied Eulerian/semi-Eulerian graph evidence | Insert from svg/FAS2EulerianTraversabilityAndRouteInspectionSVG-003.svg | Purpose: Compare Eulerian, semi-Eulerian and neither using vertex parity.]

[VISUAL PLACEHOLDER: FAS2EulerianTraversabilityAndRouteInspectionBridgeSVG-001 | Source: Ordinary A-Level Maths bridge + Further Maths graph specification | Insert from svg/FAS2EulerianTraversabilityAndRouteInspectionBridgeSVG-001.svg | Purpose: Compare ordinary diagram interpretation with Further Maths graph abstraction.]

[VISUAL PLACEHOLDER: FAS2EulerianTraversabilityAndRouteInspectionSVG-004 | Source: Route inspection PDF | Insert from svg/FAS2EulerianTraversabilityAndRouteInspectionSVG-004.svg | Purpose: Show route inspection as total weight plus repeated shortest paths.]

[VISUAL PLACEHOLDER: FAS2EulerianTraversabilityAndRouteInspectionTikZ-001 | Source: Eulerian and semi-Eulerian graph evidence | Insert from tikz/FAS2EulerianTraversabilityAndRouteInspectionTikZ-001.tex | Purpose: Precise graph examples with degree labels.]

[VISUAL PLACEHOLDER: FAS2EulerianTraversabilityAndRouteInspectionTikZ-002 | Source: Greendale all-even route inspection example from PDF | Insert from tikz/FAS2EulerianTraversabilityAndRouteInspectionTikZ-002.tex | Purpose: Weighted all-even network showing shortest closed route equals total weight.]

[VISUAL PLACEHOLDER: FAS2EulerianTraversabilityAndRouteInspectionTikZ-003 | Source: Four odd vertices route inspection PDF example | Insert from tikz/FAS2EulerianTraversabilityAndRouteInspectionTikZ-003.tex | Purpose: Show pairings of four odd vertices and choosing the least extra length.]

[VISUAL PLACEHOLDER: FAS2EulerianTraversabilityAndRouteInspectionTikZ-004 | Source: Complete graph \(K_n\) test-your-understanding slide | Insert from tikz/FAS2EulerianTraversabilityAndRouteInspectionTikZ-004.tex | Purpose: Show \(K_1,K_2,K_3,K_4,K_5,K_6\) classification.]

# 10. Interactive Learning Widgets

[INTERACTIVE PLACEHOLDER: FAS2EulerianTraversabilityAndRouteInspectionWidget-001 | Source: AI-proposed teaching enhancement based on CCEA graph traversability evidence | Insert from widgets/FAS2EulerianTraversabilityAndRouteInspectionWidget-001.html | Purpose: Classify a graph from vertex degrees and connectedness.]

[INTERACTIVE PLACEHOLDER: FAS2EulerianTraversabilityAndRouteInspectionWidget-002 | Source: AI-proposed teaching enhancement based on \(K_n\) evidence and CCEA graph theory | Insert from widgets/FAS2EulerianTraversabilityAndRouteInspectionWidget-002.html | Purpose: Classify \(K_n\) as Eulerian, semi-Eulerian or neither.]

[INTERACTIVE PLACEHOLDER: FAS2EulerianTraversabilityAndRouteInspectionWidget-003 | Source: AI-proposed teaching enhancement based on supplied route inspection evidence | Insert from widgets/FAS2EulerianTraversabilityAndRouteInspectionWidget-003.html | Purpose: Calculate route inspection length for 0, 2 or 4 odd vertices.]

[INTERACTIVE PLACEHOLDER: FAS2EulerianTraversabilityAndRouteInspectionWidget-004 | Source: AI-proposed teaching enhancement based on transcript arrow explanation | Insert from widgets/FAS2EulerianTraversabilityAndRouteInspectionWidget-004.html | Purpose: Build intuition for why Eulerian circuits require even degree.]

# 11. Worked Examples

## Worked Example 1: Seven Bridges of Königsberg

The problem asks whether one can cross all seven bridges exactly once and return to the start. Model land masses as vertices and bridges as edges. The required route is an Eulerian circuit. In a circuit, every vertex must have even degree. In the Königsberg graph, all four vertices are odd. Therefore no Eulerian circuit exists.

\[
\boxed{\text{No. The graph has odd-degree vertices, so it cannot have an Eulerian circuit.}}
\]

## Worked Example 2: Degree Expressions

A connected graph has 4 nodes and 8 edges. The degrees are
\[
2n-2,\ n-1,\ n-1,\ n.
\]
By the Handshake Lemma:
\[
(2n-2)+(n-1)+(n-1)+n=16.
\]
\[
5n-4=16,
\]
\[
5n=20,
\]
\[
n=4.
\]
Therefore the degrees are:
\[
6,3,3,4.
\]
There are exactly two odd vertices, so the graph is semi-Eulerian because it is connected.

## Worked Example 3: Complete Graphs

For \(K_n\), \(\deg(v)=n-1\). Thus \(K_7\) has degree \(6\), Eulerian; \(K_8\) has eight odd vertices, neither; \(K_2\) has exactly two odd vertices, semi-Eulerian; \(K_{11}\) has degree \(10\), Eulerian.

## Worked Example 4: Simple Connected Graph with Four Vertices

Minimum edges for a connected graph on four vertices:
\[
4-1=3.
\]
Maximum edges for a simple graph on four vertices:
\[
\frac{4(4-1)}{2}=6.
\]
The division by 2 is required because each undirected edge is counted twice by \(4\times 3\).

## Worked Example 5: Constructing an Eulerian Graph

To draw an Eulerian graph with five nodes and seven arcs, the total degree must be
\[
2\times 7=14.
\]
A suitable even degree sequence is:
\[
4,4,2,2,2.
\]
Construct a connected graph with vertices \(A,B,C,D,E\) and edges
\[
AB,AC,AD,AE,BC,BD,BE.
\]
Then \(A\) and \(B\) have degree \(4\), and \(C,D,E\) each have degree \(2\). Hence the graph is connected and Eulerian.

## Worked Example 6: Route Inspection, All Even

If all vertices are even, the graph is Eulerian. The shortest closed route equals the total weight. In the Greendale evidence example, the total is \(104\) minutes, so
\[
\boxed{104\text{ minutes}}.
\]

## Worked Example 7: Route Inspection, Two Odd Vertices

If \(W=57\) and the shortest path between the two odd vertices has length \(3\), then a closed route has length:
\[
57+3=60.
\]
If the route may start at one odd vertex and finish at the other, the length is simply \(57\).

## Worked Example 8: Two Odd Vertices with Indirect Path

If \(W=103\) and the shortest path from \(E\) to \(F\) is \(EBACF\) of length \(8\), then
\[
103+8=111.
\]
The repeated edges are the edges on \(EBACF\), not merely “\(EF\)”.

## Worked Example 9: Four Odd Vertices

Odd vertices: \(A,C,D,G\). Pairings:
\[
AD+CG=7+4=11,
\]
\[
AC+DG=9+9=18,
\]
\[
AG+DC=13+7=20.
\]
Least extra length is \(11\). If \(W=72\), then:
\[
72+11=83.
\]

# 12. Common Mistakes and Exam Traps

- Forgetting connectedness.
- Counting vertices instead of degrees.
- Treating a crossing as a vertex when no vertex is marked.
- Counting an odd number of odd vertices and not recounting.
- Confusing Eulerian with semi-Eulerian.
- Saying “two odd vertices” without saying “connected”.
- Assuming the physical map shape matters more than adjacency.
- Confusing edge, path, trail, circuit and route.
- In route inspection, forgetting to add total weight \(W\).
- Naming only the endpoint pair rather than the actual repeated edges.
- Missing one of the three pairings for four odd vertices.
- Treating route inspection or more than four odd vertices as confirmed CCEA core without official CCEA evidence.

# 13. Practice Questions

1. A graph has edges \(AB,AC,AD,BC,CD,DE\). Find all vertex degrees.
2. A connected graph has degrees \(2,4,4,2,6\). Classify it.
3. A connected graph has degrees \(3,2,4,5,2\). Classify it.
4. A connected graph has degrees \(1,3,3,3,4\). Classify it.
5. Explain why degrees \(1,2,2,4,6\) cannot be a graph degree sequence.
6. A connected graph has 5 vertices and 9 edges with degrees \(n,n+1,2n-1,2n,3n-2\). Find \(n\) and comment.
7. Classify \(K_7,K_8,K_2,K_{11}\).
8. Prove \(K_{2m+1}\) is Eulerian.
9. A simply connected graph has 6 vertices. Find the minimum and maximum number of edges.
10. Construct a connected semi-Eulerian graph with 6 vertices and 7 edges.
11. A connected graph has degrees \(3,2,4,3,5,5\). Classify it and suggest edges to make it semi-Eulerian and Eulerian.
12. Two disconnected triangles each have all degrees even. Explain why the whole graph is not Eulerian.
13. A connected graph has four vertices of degree 2, two vertices of degree 3, and one vertex of degree 4. Find the number of edges and classify.
14. Design a connected Eulerian graph with 6 vertices and 9 edges, allowing loops if necessary.
15. A connected weighted network has all vertices even and edge weights \(6,4,8,7,5,10,3\). Find the shortest closed route length.
16. A network has \(W=86\), two odd vertices \(A,F\), and \(d(A,F)=11\). Find the shortest closed route length.
17. For the same network, find the open route length from \(A\) to \(F\).
18. Four odd vertices \(A,B,C,D\), \(W=120\), with pair distances: \(AB=9,CD=14,AC=11,BD=10,AD=8,BC=16\). Find the closed inspection length.
19. Shortest path \(P\to Q\to R\to T\) has weights \(4,3,5\), and \(W=75\). Find the route length and repeated edges.
20. Explain why \(AB+AC\) is not a valid complete pairing of \(A,B,C,D\).

# 14. Worked Solutions

1. Degrees: \(\deg(A)=3,\deg(B)=2,\deg(C)=3,\deg(D)=3,\deg(E)=1\). Four odd vertices.
2. All degrees even and connected, so Eulerian.
3. Exactly two odd degrees, so semi-Eulerian.
4. Four odd vertices, so neither.
5. Total degree \(1+2+2+4+6=15\), odd, impossible.
6. \(n+(n+1)+(2n-1)+2n+(3n-2)=18\), so \(9n-2=18\), \(n=20/9\). Not an integer, so no such graph exists.
7. \(K_7\): degree 6 Eulerian. \(K_8\): degree 7 with eight odd vertices, neither. \(K_2\): semi-Eulerian. \(K_{11}\): degree 10 Eulerian.
8. In \(K_{2m+1}\), every vertex has degree \((2m+1)-1=2m\), even, and the graph is connected, so Eulerian.
9. Minimum \(6-1=5\). Maximum \(\frac{6\cdot5}{2}=15\). Not \(6\times5\) because edges are double-counted.
10. One answer: vertices \(A,B,C,D,E,F\), edges \(AB,AC,AD,BE,BF,CE,DF\). Degrees \(3,3,2,2,2,2\), connected, exactly two odd vertices.
11. Odd vertices: \(A,D,E,F\), so neither. Add one edge between two odd vertices, e.g. \(AD\), to make semi-Eulerian. Add \(AD\) and \(EF\) to make Eulerian.
12. Each vertex has degree 2, but the graph is disconnected, so no single route traverses the whole graph.
13. Total degree \(4\cdot2+2\cdot3+1\cdot4=18\), so \(|E|=9\). Exactly two odd vertices and connected, so semi-Eulerian.
14. Use a 6-cycle \(AB,BC,CD,DE,EF,FA\), plus loops \(AA,CC,EE\). Loops count twice, so all degrees are even and total edges are 9.
15. Sum weights: \(6+4+8+7+5+10+3=43\).
16. \(86+11=97\).
17. Open route from odd to odd uses each edge once, so \(86\).
18. Pairings: \(AB+CD=23\), \(AC+BD=21\), \(AD+BC=24\). Least \(21\), so \(120+21=141\).
19. Shortest path length \(4+3+5=12\). Route length \(75+12=87\). Repeated edges: \(PQ,QR,RT\).
20. \(AB+AC\) uses \(A\) twice and omits \(D\), so it is not a complete pairing. Every odd vertex must appear exactly once.

# 15. Exam Technique Notes

Ask first: is the graph connected? Then count odd-degree vertices. Write full reasons: “The graph is connected and all vertices have even degree, so it is Eulerian.” Use “vertices of odd degree” rather than vague “odd vertices” when possible. Check the Handshake Lemma. For \(K_n\), start with \(\deg(v)=n-1\). For route inspection enrichment, calculate \(W\), then add the smallest required repeated path total. If asked for repeated edges, name the actual edges in the shortest path. For four odd vertices, list exactly three complete pairings.

# 16. Syllabus Gap Check

| LO ID | Covered? | Notes |
|---|---|---|
| FAS2-GRAPH-LO001 | Yes | Vertex, edge, degree, connectedness |
| FAS2-GRAPH-LO002 | Yes | Complete graph \(K_n\) classification |
| FAS2-GRAPH-LO003 | Yes | Eulerian circuits, semi-Eulerian trails, traversability |
| FAS2-GRAPH-LO004 | Partly | Weighted edges used; digraphs not developed |
| FAS2-GRAPH-LO005 | Partly | Connectedness and tree comparison only |
| FAS2-ALGGRAPH-LO005 | Partly | Shortest path support only |

## Off-Spec Content Found but Excluded

Route inspection is not treated as official CCEA core because the supplied CCEA LO map does not explicitly name it. More than four odd vertices, six odd vertices, and 15-pairing comparisons are excluded from core and logged as optional enrichment only.

## Missing Evidence Log

Official CCEA route inspection extract, full Pearson textbook pages, CCEA past-paper route inspection questions, official mark schemes and full readable OCR from the screenshot PDF were not supplied.

# 17. Recommended Enhancements Not in the Evidence

AI-proposed enhancements include: map-to-graph abstraction diagram, enter/leave parity diagram, Eulerian classification decision tree, complete graph classifier, four-odd-vertex pairing visual, Eulerian classifier widget, \(K_n\) widget, route inspection enrichment calculator, and pairing checker. These are proposed teaching supports, not additional CCEA authority.

# 18. Supplementary Sources Used

Project sources: CCEA Further Mathematics Specification Map, Further Maths README module map, Evidence Drop Checklist, Ordinary A-Level Maths Bridge Spec Extracts, and CCEA Mathematics Specification Map. Lesson-specific sources: Decision 1 route inspection PDF, transcripts.md, and the screenshot PDF. Ordinary A-Level Maths sources are bridge context only. Cross-board Decision 1 material is used only where compatible with the CCEA graph theory boundary.

# 19. Final Student Checklist

- [ ] I can define graph, vertex, edge, arc and degree.
- [ ] I can explain why a loop counts twice.
- [ ] I can state \(\sum\deg(v)=2|E|\).
- [ ] I can classify connected graphs with 0, 2, or more than 2 odd vertices.
- [ ] I can explain why connectedness matters.
- [ ] I can classify \(K_n\) using \(\deg(v)=n-1\).
- [ ] I can write exam-style reasons using “connected” and “degree”.
- [ ] I can use route inspection formulas as enrichment/application.
- [ ] I can name actual repeated edges, not just endpoint pairs.
- [ ] I can keep off-spec route inspection extensions separate from CCEA core.

Final summary:
\[
\text{routes are controlled by vertex degrees.}
\]
Closed routes need all degrees even. Open Eulerian trails need exactly two odd degrees. Weighted route inspection then asks which edges, if any, must be repeated at least extra cost.
