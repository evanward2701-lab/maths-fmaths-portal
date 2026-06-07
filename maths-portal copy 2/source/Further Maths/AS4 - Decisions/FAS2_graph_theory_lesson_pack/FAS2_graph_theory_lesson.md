# 1. Lesson Title and Metadata

```yaml
date_generated: 2026-06-04
course: CCEA GCE Further Mathematics
unit_code: FAS2
unit_name: Further AS 2 Applied Mathematics
applied_section: Section D: Discrete and Decision Mathematics
topic_code: FAS2-GRAPH
topic_name: Graph theory
lesson_title: Graph Theory: Graphs and Networks
topic_slug: graph_theory
topic_pascal: GraphTheory
topic_id: FAS2GraphTheory
lesson_file: FAS2_graph_theory_lesson.md
lo_ids:
  - FAS2-GRAPH-LO001
  - FAS2-GRAPH-LO002
  - FAS2-GRAPH-LO003
  - FAS2-GRAPH-LO004
  - FAS2-GRAPH-LO005
bridge_tags:
  - ordinary_algebra_notation
  - ordinary_table_reasoning
  - ordinary_counting
  - ordinary_modelling_diagrams
  - ordinary_proof_language
topic_tags:
  - graph_theory
  - vertices
  - edges
  - degree
  - subgraph
  - planarity
  - complete_graph
  - complete_bipartite_graph
  - star_graph
  - traversability
  - eulerian_circuit
  - hamiltonian_path
  - weighted_graph
  - digraph
  - tree
  - spanning_tree
```

## Lesson purpose

This lesson teaches the core language and first structural results of **graph theory** for CCEA Further Mathematics. A graph, in this topic, is **not** a coordinate graph with \(x\)- and \(y\)-axes. It is a diagram made from **vertices** and **edges**, used to represent connections.

The uploaded teacher transcript describes this chapter as a “big background section” that prepares students for later decision mathematics topics, especially algorithms on graphs, route inspection, travelling salesperson problems and critical path analysis. The transcript also stresses that graphs and networks are intuitive because they appear in real contexts such as tram networks, roads, villages, hospitals and broadband connections.

---

# 2. Evidence Map

## 2.1 Core Further Mathematics sources

| Source | Role in lesson |
|---|---|
| CCEA GCE Further Mathematics Specification Map | Official authority for `FAS2-GRAPH` topic boundary and LO IDs |
| Further Maths README Module Map | Confirms project unit prefixes, metadata rules and bridge expectations |
| Further Maths Evidence Drop Checklist | Confirms evidence logging, off-spec logging and asset planning requirements |

## 2.2 Lesson-specific evidence sources

| Source | Evidence used |
|---|---|
| Teacher transcript: `transcripts.md` | Introductory teaching language; graph/network definitions; subgraph example; degree example; walk/path/trail/cycle examples; Euler handshaking lemma; tree/spanning tree/complete graph/isomorphic graph explanations; matrix representation; planarity algorithm as off-spec enrichment |
| Lesson PDF: `Decision Maths 1 chapter 2 Graphs and networks (including A2 content Planarity Alg).pdf` | Slide definitions and diagrams for modelling with graphs, subgraphs, degree/valency, traversability definitions, connected graphs, loops, simple graphs, directed graphs, handshaking lemma, special graphs, matrices and planarity |
| Screenshot PDF: `Chapter_2_Graphs_&_Networks_💻_(Decision_1)_screenshots.pdf` | Visual support for diagrams and handwritten annotations; no parsed text available, so only visible preview information and matching transcript/PDF evidence are used |

## 2.3 Key evidence notes

The lesson PDF defines a graph as points called vertices or nodes connected by lines called edges or arcs, and defines a weighted graph/network as one where a number is associated with each edge.

The transcript reinforces the same terminology and explicitly warns that two edges can cross without creating a vertex unless a vertex is marked there.

The screenshot PDF contains many visual pages, but no machine-parsed text was available. Therefore, diagram descriptions in this lesson rely on visible previews plus the transcript/PDF text. No hidden screenshot detail is claimed.

---

# 3. Specification Alignment

| LO ID | Official wording | Lesson coverage | Evidence source | Boundary note | Ordinary Maths bridge |
|---|---|---|---|---|---|
| `FAS2-GRAPH-LO001` | demonstrate understanding of and use the basic concepts of graph theory, including vertex, edge, degree, planarity and subgraph | Definitions of graph, vertex/node, edge/arc, subgraph, degree/valency/order, odd/even vertices, planarity concept | CCEA spec; transcript; lesson PDF | Full planarity algorithm excluded from core | Ordinary diagrams and table reading |
| `FAS2-GRAPH-LO002` | demonstrate understanding of certain basic graphs, including the complete graph on \(n\) vertices \(K_n\), the complete bipartite graph \(K_{m,n}\) and the star on \(n\) vertices \(S_n\) | Complete graph \(K_n\), edge-count formula, complete bipartite graph, star graph | CCEA spec; lesson PDF for \(K_n\); CCEA spec for \(K_{m,n}\), \(S_n\) | Lesson evidence thin for \(K_{m,n}\), \(S_n\) | Counting and double-counting |
| `FAS2-GRAPH-LO003` | demonstrate understanding of and use the traversability of graphs including circuits, Eulerian circuits and Hamiltonian paths, and basic conditions necessary for their existence | Walk, path, trail, cycle, circuit, Eulerian circuit, Hamiltonian path, Hamiltonian cycle as related evidence term, degree conditions | CCEA spec; transcript; lesson PDF | Hamiltonian cycle appears in evidence; Hamiltonian path is official wording | Route descriptions and proof language |
| `FAS2-GRAPH-LO004` | demonstrate understanding of and deal with weighted edges and digraphs | Weighted graphs/networks; digraphs; directed edges; route reading | CCEA spec; transcript; lesson PDF | Matrix representations are enrichment only | Modelling with diagrams and units |
| `FAS2-GRAPH-LO005` | demonstrate understanding of and use the basic concepts associated with trees: root, connectedness, binary tree and spanning tree | Connected graph, tree, rooted tree, binary tree, spanning tree | CCEA spec; transcript/PDF for connectedness, tree and spanning tree | Root and binary tree evidence is specification-led | Tree diagrams, hierarchy diagrams |

---

# 4. Learning Objectives

## 4.1 Core Further Maths objectives

By the end of this lesson, you should be able to:

1. Define a graph using **vertices/nodes** and **edges/arcs**.
2. Distinguish between an ordinary graph and a **weighted graph/network**.
3. Use the terms **vertex set** and **edge set**.
4. Identify and draw a **subgraph**.
5. Find the **degree**, **valency** or **order** of a vertex.
6. Classify vertices as **odd** or **even**.
7. Use Euler’s handshaking lemma:
   \[
   \sum \deg(v)=2|E|.
   \]
8. Explain why the number of odd vertices in an undirected graph must be even.
9. Distinguish between a **walk**, **path**, **trail**, **cycle**, **circuit**, **Eulerian circuit**, **Hamiltonian path** and related Hamiltonian cycle.
10. Recognise and use **connected graphs**, **loops**, **multiple edges**, **simple graphs** and **digraphs**.
11. Recognise and work with \(K_n\), \(K_{m,n}\) and \(S_n\).
12. Understand trees, rooted trees, binary trees and spanning trees.
13. Understand planarity as a basic graph concept.

## 4.2 Bridge objectives

You should be able to connect this topic to ordinary A-Level Maths by:

1. Using familiar table and diagram reading skills.
2. Recognising that a graph here is **not** a coordinate graph.
3. Using counting ideas to avoid double-counting edges.
4. Writing clear mathematical justifications rather than only drawing pictures.

## 4.3 Exam technique objectives

You should learn to:

1. Define graph-theory terms precisely.
2. Label vertices clearly using capital letters.
3. State routes using strings of vertex labels, for example \(ABCDE\).
4. Check whether a line crossing is actually a vertex.
5. Use parity of vertex degrees before trying to draw impossible graphs.
6. Write final conclusions such as “therefore the graph cannot have an Eulerian circuit”.

---

# 5. Explicit Prerequisite Recap

## 5.1 GCSE foundations

You should already be comfortable with:

- counting objects carefully;
- reading diagrams;
- identifying whether a number is odd or even;
- using tables;
- following routes on a map;
- interpreting simple networks, such as roads or transport lines.

## 5.2 Ordinary AS/A2 Mathematics foundations

This topic has **no direct ordinary CCEA A-Level Maths predecessor**. It is one of the places where Further Maths quietly opens a new door in the wall and says, “Graphs are no longer curves. They are connection-machines.”

The useful ordinary Maths background is:

- algebraic notation;
- sets and lists;
- tables;
- counting and double-counting;
- proof language;
- modelling diagrams from mechanics/statistics.

## 5.3 Previous Further Mathematics foundations

This is a foundation topic for later Decision Mathematics. It supports:

- algorithms on graphs;
- shortest path problems;
- minimal spanning trees;
- route inspection;
- travelling salesperson methods;
- critical path analysis.

## 5.4 A-Level Maths Bridge: What You Already Know and What Further Maths Changes

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| Ordinary algebra and functions | A graph usually meant a curve or relation drawn on axes | A graph now means vertices connected by edges | Do not look for \(x\)- and \(y\)-axes |
| Ordinary coordinate geometry | Intersections usually mattered | Edge crossings do not create vertices unless a vertex is marked | A crossing line is not automatically a junction |
| Ordinary statistics/mechanics diagrams | Diagrams model real-world situations | Networks model roads, computers, stations, handshakes and tasks | Weighted graphs are not normally drawn to scale |
| Ordinary counting/probability | Avoid double-counting outcomes | Degrees double-count edges in the handshaking lemma | Edge total is half the degree total |
| Ordinary proof | Explain why a statement follows | Graph theory uses restrictions such as parity and connectedness | A drawing without justification may not earn full marks |

In ordinary A-Level Maths, this idea appeared as diagram interpretation, table reading and structured counting.

In Further Maths, the same idea becomes a new object: a **graph**, made from vertices and edges.

The key upgrade is that the diagram is no longer just a picture. It is a mathematical structure.

The danger is assuming visual features mean more than they do. A line crossing is not a vertex. A weighted graph is not to scale. A graph that looks split into two pieces may still be “one graph”, but it is not connected.

---

# 6. Big Picture Explanation

A **graph** is a way of modelling relationships.

The objects are called **vertices** or **nodes**. The connections between them are called **edges** or **arcs**.

That sounds tiny, but the idea is a mathematical seed crystal. Once you can describe connections, you can model:

- tram stops and tracks;
- towns and roads;
- computers and network cables;
- people and handshakes;
- tasks and dependencies;
- possible routes through a building;
- choices in an algorithm.

The uploaded teacher transcript introduces this chapter as background for later Decision Mathematics. The first concepts are deliberately abstract, but they become useful later for route inspection, travelling salesperson problems, graph algorithms and project planning.

For CCEA FAS2, this lesson is not mainly about lengthy calculations. It is about learning a precise language. Once you can say exactly what a vertex, edge, degree, walk, trail, circuit or tree is, later algorithms become much less foggy.

---

# 7. Key Definitions and Notation

## 7.1 Graph

A **graph** is a collection of points called **vertices** or **nodes**, connected by lines called **edges** or **arcs**.

If the graph is called \(G\), we often write:

\[
G=(V,E),
\]

where:

- \(V\) is the set of vertices;
- \(E\) is the set of edges.

For example, if

\[
V=\{A,B,C,D\},
\]

then \(A,B,C,D\) are vertices.

If

\[
E=\{AB,BC,CD,AD\},
\]

then \(AB,BC,CD,AD\) are edges.

## 7.2 Vertex or node

A **vertex** or **node** is a point in a graph.

The plural of vertex is **vertices**.

## 7.3 Edge or arc

An **edge** or **arc** is a connection between two vertices.

For example, \(AB\) means there is an edge joining \(A\) to \(B\).

## 7.4 Weighted graph or network

A **weighted graph** is a graph where each edge has a number associated with it.

That number is called its **weight**.

A weighted graph is often called a **network**.

The weight might represent:

- distance;
- time;
- cost;
- capacity;
- resistance;
- delay.

The lesson PDF gives a computer network context where edge weights represent ping times in milliseconds, and warns that a weighted graph is not normally drawn to scale.

## 7.5 Subgraph

A **subgraph** of \(G\) is a graph whose vertices belong to \(G\) and whose edges belong to \(G\).

Informally:

\[
\text{subgraph}=\text{part of the original graph}.
\]

## 7.6 Degree, valency or order of a vertex

The **degree**, **valency** or **order** of a vertex is the number of edges incident to it.

If \(v\) is a vertex, its degree is written as:

\[
\deg(v).
\]

If \(\deg(v)\) is even, \(v\) is an **even vertex**.

If \(\deg(v)\) is odd, \(v\) is an **odd vertex**.

## 7.7 Loop

A **loop** is an edge that starts and finishes at the same vertex.

A loop contributes \(2\) to the degree of the vertex, because it meets the vertex twice.

## 7.8 Multiple edges

**Multiple edges** occur when more than one edge joins the same pair of vertices.

## 7.9 Simple graph

A **simple graph** has:

1. no loops;
2. at most one edge between any pair of vertices.

## 7.10 Directed graph or digraph

A **directed graph**, or **digraph**, is a graph where the edges have direction.

A directed edge may allow travel from \(A\) to \(B\), but not from \(B\) to \(A\).

## 7.11 Connected graph

Two vertices are **connected** if there is a path between them.

A graph is **connected** if all its vertices are connected.

## 7.12 Walk

A **walk** is a route through a graph along edges from one vertex to the next.

Vertices and edges may be repeated.

## 7.13 Path

A **path** is a walk in which no vertex is visited more than once.

## 7.14 Trail

A **trail** is a walk in which no edge is visited more than once.

Vertices may be repeated.

## 7.15 Cycle

A **cycle** is a walk in which:

1. the end vertex is the same as the start vertex;
2. no other vertex is visited more than once.

## 7.16 Circuit

A **circuit** is a closed trail.

That means:

1. it starts and ends at the same vertex;
2. no edge is repeated.

## 7.17 Eulerian circuit

An **Eulerian circuit** is a circuit that uses every edge of the graph exactly once.

## 7.18 Hamiltonian path

A **Hamiltonian path** is a path that visits every vertex exactly once.

## 7.19 Hamiltonian cycle

A **Hamiltonian cycle** is a cycle that visits every vertex.

The uploaded evidence uses Hamiltonian cycles frequently. CCEA’s official FAS2 wording names **Hamiltonian paths**, so this lesson treats Hamiltonian cycles as a useful related concept rather than the main syllabus phrase.

## 7.20 Tree

A **tree** is a connected graph with no cycles.

## 7.21 Spanning tree

A **spanning tree** is a subgraph that:

1. includes all the vertices of the original graph;
2. is a tree.

## 7.22 Rooted tree

A **rooted tree** is a tree where one vertex is chosen as the **root**.

The root gives the tree a hierarchy.

## 7.23 Binary tree

A **binary tree** is a rooted tree in which each vertex has at most two children.

## 7.24 Complete graph \(K_n\)

The **complete graph** on \(n\) vertices is written:

\[
K_n.
\]

Every vertex is joined directly to every other vertex by a single edge.

## 7.25 Complete bipartite graph \(K_{m,n}\)

A **complete bipartite graph** \(K_{m,n}\) has two sets of vertices:

\[
A=\{a_1,a_2,\dots,a_m\},
\]

\[
B=\{b_1,b_2,\dots,b_n\}.
\]

Every vertex in \(A\) is connected to every vertex in \(B\).

No vertices inside the same set are connected to each other.

## 7.26 Star graph \(S_n\)

A **star graph** \(S_n\) has one central vertex connected to \(n\) outer vertices.

It looks like a hub with spokes.

## 7.27 Planar graph

A **planar graph** is a graph that can be drawn in a plane so that no two edges meet except at a vertex.

A graph may look non-planar in one drawing but be planar if redrawn.

---

# 8. Core Theory

## 8.1 Graphs are not coordinate graphs

In ordinary A-Level Maths, the word “graph” usually means something like:

\[
y=x^2,\qquad y=\sin x,\qquad y=e^x.
\]

Those graphs live on coordinate axes.

In this topic, a graph is instead a structure made from vertices and edges.

**Bridge Note:** In ordinary A-Level Maths, you used graphs to show numerical relationships. Here, Further Maths uses graphs to show connections.

A graph might show:

- stations connected by tram tracks;
- computers connected by network links;
- people connected by handshakes;
- towns connected by roads.

## 8.2 Vertex set and edge set

Suppose a graph has vertices:

\[
A,\ B,\ C,\ D,\ E,\ F.
\]

Then the **vertex set** is:

\[
V=\{A,B,C,D,E,F\}.
\]

Suppose its edges are:

\[
AB,\ AC,\ AF,\ BC,\ BD,\ CE,\ CE,\ DE.
\]

Then the **edge set** is:

\[
E=\{AB,AC,AF,BC,BD,CE,CE,DE\}.
\]

Notice that \(CE\) appears twice. That means there are **multiple edges** joining \(C\) and \(E\).

A graph with multiple edges is not simple.

**Bridge Note:** In ordinary Maths, a set usually does not repeat elements. In graph theory evidence, an edge list can show repeated edges to represent multiple connections. Treat that carefully. If the exam uses formal set notation, it may describe multiple edges separately or draw them.

## 8.3 Edge crossings do not automatically create vertices

A very important diagram warning:

Two edges may cross in a drawing without creating a vertex.

A vertex is only present if the graph marks one there, usually with a dot or labelled point.

So, if edges \(AC\) and \(BD\) cross visually, that does **not** mean the graph contains a vertex at their crossing.

**Exam trap:** If there is no marked vertex at the crossing, you cannot change route at that crossing.

## 8.4 Weighted graphs and networks

If every edge has a number attached, the graph is **weighted**.

Example:

\[
AB=4,\qquad AC=12,\qquad AD=7.
\]

These numbers might represent distances between towns.

If there is no edge between \(C\) and \(E\), then there is no direct route from \(C\) to \(E\). A traveller may need to go through another vertex, such as:

\[
C\to A\to E.
\]

**Bridge Note:** In ordinary Mechanics or Statistics, numbers in a diagram often have units and meaning. Here, weights may be distances, times or costs. Always say what the weight represents if the context gives it.

The lesson PDF gives ping times measured in milliseconds and explicitly warns:

\[
\text{weighted graph is not normally drawn to scale.}
\]

## 8.5 Degree, valency and order

The degree, valency or order of a vertex is the number of edges incident to it.

If four edges meet at \(A\), then:

\[
\deg(A)=4.
\]

If two edges meet at \(B\), then:

\[
\deg(B)=2.
\]

If one edge meets at \(E\), then:

\[
\deg(E)=1.
\]

A vertex of degree \(1\) is odd.

A vertex of degree \(2\) is even.

A vertex of degree \(3\) is odd.

A vertex of degree \(4\) is even.

## 8.6 Loops and degree

A loop starts and ends at the same vertex.

If a loop is attached to vertex \(A\), it contributes \(2\) to \(\deg(A)\), not \(1\).

Why?

Because the loop meets \(A\) twice:

1. once when it leaves \(A\);
2. once when it returns to \(A\).

So if \(A\) has one ordinary edge and one loop, then:

\[
\deg(A)=1+2=3.
\]

**Exam trap:** Forgetting that a loop counts twice is one of those tiny errors that steals marks wearing socks.

## 8.7 Euler’s handshaking lemma

Euler’s handshaking lemma says:

\[
\sum_{v\in V}\deg(v)=2|E|.
\]

In words:

\[
\text{sum of all vertex degrees}=2\times\text{number of edges}.
\]

### Why is this true?

Every edge has two ends.

Each edge contributes \(1\) to the degree of one endpoint and \(1\) to the degree of the other endpoint.

So each edge contributes \(2\) to the total degree count.

Therefore, if there are \(|E|\) edges:

\[
\sum_{v\in V}\deg(v)=2|E|.
\]

### Consequence: the number of odd vertices is even

Since:

\[
2|E|
\]

is always even, the total degree sum must be even.

Even-degree vertices contribute even numbers to the sum.

Odd-degree vertices contribute odd numbers to the sum.

A sum of odd numbers is even only if there is an even number of odd terms.

Therefore:

\[
\text{the number of odd vertices must be even.}
\]

## 8.8 Handshaking lemma in a handshake context

Imagine each vertex is a person and each edge is a handshake.

If Peter shakes hands with Quentin, that single handshake is counted:

- once in Peter’s degree;
- once in Quentin’s degree.

So the total degree count double-counts handshakes.

If the degree total is \(18\), then:

\[
2|E|=18.
\]

Divide by \(2\):

\[
|E|=9.
\]

So there were:

\[
9
\]

handshakes.

## 8.9 Walks, paths, trails, cycles and circuits

These words are close together, so we need a clean ladder.

### Walk

A walk is any route through a graph along edges.

Vertices may repeat.

Edges may repeat.

Example route:

\[
P\to R\to U\to T\to R\to P\to S.
\]

Written compactly:

\[
PRUTRPS.
\]

### Path

A path is a walk where no vertex is visited more than once.

Example:

\[
P\to Q\to R\to T\to U.
\]

Written compactly:

\[
PQRTU.
\]

### Trail

A trail is a walk where no edge is visited more than once.

Vertices may repeat.

Example:

\[
R\to T\to U\to S.
\]

Written compactly:

\[
RTUS.
\]

### Cycle

A cycle is a path that ends where it started.

Example:

\[
P\to Q\to T\to R\to P.
\]

Written compactly:

\[
PQTRP.
\]

The start and end vertex are the same, and no other vertex is repeated.

### Circuit

A circuit is a closed trail.

That means it starts and ends at the same vertex, and no edge is repeated.

### Eulerian circuit

An Eulerian circuit is a circuit using every edge exactly once.

### Hamiltonian path

A Hamiltonian path visits every vertex exactly once.

### Hamiltonian cycle

A Hamiltonian cycle visits every vertex and returns to the start.

## 8.10 Traversability conditions

For CCEA FAS2, you need basic conditions connected to traversability.

### Eulerian circuit condition

For a connected undirected graph to have an Eulerian circuit, every vertex must have even degree.

So if a graph has an Eulerian circuit, then:

\[
\deg(v)\text{ is even for every vertex }v.
\]

### Eulerian trail condition

A connected undirected graph has an Eulerian trail but not an Eulerian circuit when exactly two vertices have odd degree.

The trail starts at one odd vertex and ends at the other odd vertex.

### More than two odd vertices

If a connected graph has more than two odd vertices, it cannot have an Eulerian trail using every edge exactly once.

### Hamiltonian path warning

Hamiltonian paths are about visiting **vertices**, not edges.

Eulerian circuits are about using **edges**, not vertices.

| Concept | Must include every… | May repeat vertices? | May repeat edges? |
|---|---:|---:|---:|
| Eulerian circuit | Edge | Yes, if needed | No |
| Hamiltonian path | Vertex | No | Usually no, because repeated edge would force repeated vertices in a simple path |

## 8.11 Connected graphs

Two vertices are connected if there is a path between them.

A graph is connected if every pair of vertices is connected.

A graph can be one graph even if it is drawn as two separated pieces, but it is not a connected graph.

## 8.12 Simple graphs, loops and multiple edges

A simple graph has:

\[
\text{no loops}
\]

and

\[
\text{at most one edge connecting any pair of vertices.}
\]

If a graph has a loop, it is not simple.

If a graph has two or more edges between the same pair of vertices, it is not simple.

## 8.13 Directed graphs and digraphs

In a directed graph, edges have arrows.

If there is a directed edge:

\[
A\to B,
\]

you can travel from \(A\) to \(B\), but not necessarily from \(B\) to \(A\).

Directed graphs are also called **digraphs**.

## 8.14 Complete graphs \(K_n\)

A complete graph \(K_n\) has \(n\) vertices, and every vertex is connected to every other vertex by a single edge.

### Edge count in \(K_n\)

Each of the \(n\) vertices connects to:

\[
n-1
\]

other vertices.

So the total degree sum is:

\[
n(n-1).
\]

But every edge has been counted twice.

Therefore, the number of edges is:

\[
\frac{n(n-1)}{2}.
\]

So:

\[
|E(K_n)|=\frac{n(n-1)}{2}.
\]

### Example: \(K_{10}\)

For \(K_{10}\):

\[
|E(K_{10})|=\frac{10(10-1)}{2}.
\]

\[
|E(K_{10})|=\frac{10\cdot9}{2}.
\]

\[
|E(K_{10})|=\frac{90}{2}.
\]

\[
|E(K_{10})|=45.
\]

## 8.15 Complete bipartite graphs \(K_{m,n}\)

A complete bipartite graph \(K_{m,n}\) has two vertex groups.

Let:

\[
A=\{a_1,a_2,\ldots,a_m\}
\]

and

\[
B=\{b_1,b_2,\ldots,b_n\}.
\]

Every vertex in \(A\) is joined to every vertex in \(B\).

No vertices in \(A\) are joined to each other.

No vertices in \(B\) are joined to each other.

### Number of edges in \(K_{m,n}\)

Each of the \(m\) vertices in \(A\) connects to \(n\) vertices in \(B\).

So:

\[
|E(K_{m,n})|=mn.
\]

### Example: \(K_{3,4}\)

There are:

\[
3
\]

vertices in the first set and:

\[
4
\]

vertices in the second set.

So:

\[
|E(K_{3,4})|=3\cdot4.
\]

\[
|E(K_{3,4})|=12.
\]

**Evidence note:** \(K_{m,n}\) is required by the CCEA specification but was not developed in the uploaded lesson PDF/transcript. This section is therefore specification-led rather than teacher-transcript-led.

## 8.16 Star graphs \(S_n\)

A star graph \(S_n\) has one central vertex joined to \(n\) outer vertices.

So it has:

\[
n+1
\]

vertices in total if the notation means \(n\) outer vertices.

The central vertex has degree:

\[
n.
\]

Each outer vertex has degree:

\[
1.
\]

### Edge count in \(S_n\)

There is one edge from the centre to each outer vertex.

So:

\[
|E(S_n)|=n.
\]

**Evidence note:** \(S_n\) is required by the CCEA specification but was not developed in the uploaded lesson PDF/transcript. This section is therefore specification-led.

## 8.17 Trees

A tree is a connected graph with no cycles.

So a graph is a tree if:

1. every vertex is connected to the rest of the graph;
2. there is no cycle.

If a graph has a triangle, square or any closed loop of edges, it is not a tree.

If a graph is split into two separate pieces, it is not a tree because it is not connected.

## 8.18 Spanning trees

A spanning tree is a subgraph that:

1. contains all the vertices of the original graph;
2. is connected;
3. has no cycles.

If the original graph is \(G\), a spanning tree uses every vertex of \(G\), but only enough edges to keep the graph connected without forming a cycle.

### Key fact

If a tree has \(n\) vertices, then it has:

\[
n-1
\]

edges.

So if a spanning tree contains all \(n\) vertices of a graph, it must have:

\[
n-1
\]

edges.

This is useful later in minimal spanning tree algorithms.

## 8.19 Rooted trees and binary trees

A rooted tree has one chosen vertex called the **root**.

From the root, the tree can be read as a hierarchy.

A binary tree is a rooted tree where each vertex has at most two children.

These concepts are part of `FAS2-GRAPH-LO005`, but the uploaded lesson evidence mostly develops ordinary trees and spanning trees rather than rooted or binary trees. So this lesson gives the required definitions and keeps depth controlled.

## 8.20 Planarity as a core concept

A graph is planar if it can be drawn in the plane so that no two edges meet except at a vertex.

This means:

- edge crossings are not allowed unless the crossing point is a vertex;
- a graph may be planar even if the first drawing looks crossed;
- the question is whether the graph **can be redrawn** without edge crossings.

### CCEA boundary note

For this FAS2 lesson, the **definition and basic concept of planarity** are core because `FAS2-GRAPH-LO001` includes planarity.

The full inside/outside **planarity algorithm** from the uploaded evidence is not taught as core CCEA FAS2 content in this lesson. It is logged later under optional enrichment.

---

# 9. Visual Asset Integration

[VISUAL PLACEHOLDER: FAS2GraphTheoryMermaid-001 | Source: CCEA FAS2-GRAPH specification + uploaded lesson evidence | Insert from mermaid/FAS2GraphTheoryMermaid-001.md | Purpose: Show how the graph theory vocabulary branches from graph, network, traversability, special graphs and trees. Description: A concept map linking graph \(G=(V,E)\), vertices, edges, degree, subgraph, weighted graph, digraph, walks/paths/trails/cycles, Eulerian circuit, Hamiltonian path, \(K_n\), \(K_{m,n}\), \(S_n\), tree and spanning tree.]

[VISUAL PLACEHOLDER: FAS2GraphTheorySVG-001 | Source: Uploaded lesson PDF and transcript | Insert from svg/FAS2GraphTheorySVG-001.svg | Purpose: Introduce a graph as vertices connected by edges. Description: A labelled graph with vertices \(A,B,C,D,E\), weighted edges such as \(AB=4\), \(AC=12\), \(AD=7\), and a visible crossing of two edges labelled “not a vertex unless marked”.]

[VISUAL PLACEHOLDER: FAS2GraphTheorySVG-002 | Source: Uploaded lesson PDF and transcript | Insert from svg/FAS2GraphTheorySVG-002.svg | Purpose: Teach degree/valency/order and odd/even vertices. Description: A graph with each vertex labelled by its degree, including examples of degree \(1,2,3,4\), and a small table classifying vertices as odd or even.]

[VISUAL PLACEHOLDER: FAS2GraphTheorySVG-003 | Source: Uploaded lesson PDF and transcript | Insert from svg/FAS2GraphTheorySVG-003.svg | Purpose: Compare walk, path, trail, cycle, circuit, Eulerian circuit and Hamiltonian path. Description: A shared graph with coloured route overlays and a comparison table showing whether vertices or edges may repeat.]

[VISUAL PLACEHOLDER: FAS2GraphTheorySVG-004 | Source: CCEA specification + uploaded lesson evidence | Insert from svg/FAS2GraphTheorySVG-004.svg | Purpose: Compare required special graph families. Description: Side-by-side diagrams of \(K_5\), \(K_{3,2}\) and \(S_5\), with vertex/edge counts.]

[VISUAL PLACEHOLDER: FAS2GraphTheorySVG-005 | Source: CCEA specification + uploaded lesson evidence | Insert from svg/FAS2GraphTheorySVG-005.svg | Purpose: Explain tree, non-tree, rooted tree, binary tree and spanning tree. Description: A connected acyclic tree, a graph rejected because it contains a cycle, a graph rejected because it is not connected, a rooted tree with root marked, and a spanning tree extracted from a larger graph.]

[VISUAL PLACEHOLDER: FAS2GraphTheoryBridgeSVG-001 | Source: Ordinary A-Level Maths bridge + CCEA FAS2 Graph Theory specification | Insert from svg/FAS2GraphTheoryBridgeSVG-001.svg | Purpose: Compare prior ordinary Maths meaning of graph with Further Maths graph theory meaning. Description: Left panel shows coordinate axes and \(y=f(x)\); right panel shows graph \(G=(V,E)\) with vertices and edges. Warning banner: “No axes needed. Crossings are not automatically vertices.”]

[VISUAL PLACEHOLDER: FAS2GraphTheoryTikZ-001 | Source: Uploaded transcript subgraph example | Insert from tikz/FAS2GraphTheoryTikZ-001.tex | Purpose: Provide precise exam-style weighted graph diagram for subgraph examples. Description: Vertices \(A,B,C,D,E\), weighted edges including \(AB=4\), \(BD=6\), \(AC=12\), \(AD=7\), \(CD=10\), \(AE=14\), with one crossing explicitly not marked as a vertex.]

[VISUAL PLACEHOLDER: FAS2GraphTheoryTikZ-002 | Source: Uploaded lesson PDF and CCEA FAS2-GRAPH traversability boundary | Insert from tikz/FAS2GraphTheoryTikZ-002.tex | Purpose: Show Eulerian degree conditions. Description: Three graphs labelled “0 odd vertices: Eulerian circuit possible”, “2 odd vertices: Eulerian trail possible”, “4 odd vertices: no Eulerian trail/circuit using every edge exactly once”.]

---

# 10. Interactive Learning Widgets

[INTERACTIVE PLACEHOLDER: FAS2GraphTheoryWidget-001 | Source: AI-proposed teaching enhancement based on CCEA FAS2-GRAPH and uploaded handshaking lemma evidence | Insert from widgets/FAS2GraphTheoryWidget-001.html | Purpose: Reinforce degree counting and Euler’s handshaking lemma.]

Student inputs:

- number of vertices;
- degree of each vertex.

Widget displays:

- total degree sum;
- whether the total is even;
- implied number of edges if possible:
  \[
  |E|=\frac{\sum\deg(v)}{2};
  \]
- number of odd vertices;
- warning if an odd number of odd vertices appears.

Error checks:

- non-integer degrees;
- negative degrees;
- odd degree sum;
- odd number of odd vertices.

[INTERACTIVE PLACEHOLDER: FAS2GraphTheoryWidget-002 | Source: AI-proposed teaching enhancement based on uploaded walk/path/trail/cycle evidence | Insert from widgets/FAS2GraphTheoryWidget-002.html | Purpose: Help students classify a route as a walk, path, trail, cycle, circuit, Eulerian circuit or Hamiltonian path.]

Student inputs:

- graph edge list;
- route as capital letters, for example `PQTRP`.

Widget displays:

- whether each consecutive pair is an edge;
- repeated vertices;
- repeated edges;
- classification table.

Error checks:

- route uses missing vertex;
- route uses non-existing edge;
- repeated vertex invalidates path;
- repeated edge invalidates trail.

[INTERACTIVE PLACEHOLDER: FAS2GraphTheoryWidget-003 | Source: AI-proposed teaching enhancement based on CCEA tree and spanning tree requirements | Insert from widgets/FAS2GraphTheoryWidget-003.html | Purpose: Let students build/check a spanning tree.]

Student inputs:

- original vertex list;
- original edge list;
- chosen subgraph edge list.

Widget displays:

- whether all original vertices are included;
- whether the chosen subgraph is connected;
- whether it contains a cycle;
- whether it is a spanning tree;
- expected edge count \(n-1\).

Error checks:

- chosen edge not in original graph;
- missing vertex;
- cycle detected;
- disconnected chosen subgraph.

---

# 11. Worked Examples

## Worked Example 1: Identify vertices, edges and whether the graph is weighted

**Evidence source:** Uploaded lesson PDF and teacher transcript.

**On-spec status:** Core `FAS2-GRAPH-LO001`, `FAS2-GRAPH-LO004`

### Question

A graph has vertices

\[
A,\ B,\ C,\ D,\ E
\]

and edges

\[
AB,\ AC,\ AD,\ BD,\ CD,\ AE.
\]

Some edges have weights:

\[
AB=4,\quad AC=12,\quad AD=7,\quad BD=6,\quad CD=10,\quad AE=14.
\]

1. Write down the vertex set.
2. Write down the edge set.
3. State whether the graph is weighted.
4. State whether \(C\) is directly connected to \(E\).

### Solution

The vertices are:

\[
A,\ B,\ C,\ D,\ E.
\]

So the vertex set is:

\[
V=\{A,B,C,D,E\}.
\]

The edges are:

\[
AB,\ AC,\ AD,\ BD,\ CD,\ AE.
\]

So the edge set is:

\[
E=\{AB,AC,AD,BD,CD,AE\}.
\]

Each edge has a number associated with it:

\[
AB=4,\quad AC=12,\quad AD=7,\quad BD=6,\quad CD=10,\quad AE=14.
\]

Therefore, the graph is a **weighted graph**.

A weighted graph may also be called a **network**.

To decide whether \(C\) is directly connected to \(E\), look for the edge \(CE\) in the edge set.

\[
E=\{AB,AC,AD,BD,CD,AE\}.
\]

There is no edge \(CE\).

Therefore, \(C\) is **not directly connected** to \(E\).

### Final exam-style answer

\[
V=\{A,B,C,D,E\}
\]

\[
E=\{AB,AC,AD,BD,CD,AE\}
\]

The graph is weighted, so it is a network.

There is no direct edge \(CE\), so \(C\) is not directly connected to \(E\).

### Teaching note

A missing edge is information. It means “there is no direct connection”, not “we forgot to draw it”. In networks, silence has teeth.

## Worked Example 2: Draw a subgraph with four vertices and three edges

**Evidence source:** Teacher transcript.

**On-spec status:** Core `FAS2-GRAPH-LO001`

### Question

A weighted graph has vertices:

\[
A,\ B,\ C,\ D,\ E
\]

and includes the weighted edges:

\[
AB=4,\quad AC=12,\quad AD=7,\quad BD=6,\quad CD=10,\quad AE=14.
\]

Draw or describe a subgraph containing:

- four vertices;
- three edges.

### Solution

A subgraph must use only vertices and edges from the original graph.

Choose the four vertices:

\[
A,\ B,\ C,\ D.
\]

These all belong to the original graph, so they are allowed.

Now choose three edges from the original graph that join these vertices.

For example:

\[
AB,\quad BD,\quad AC.
\]

Check each edge belongs to the original graph:

\[
AB=4
\]

belongs to the original graph.

\[
BD=6
\]

belongs to the original graph.

\[
AC=12
\]

belongs to the original graph.

So the subgraph has:

\[
V_{\text{sub}}=\{A,B,C,D\}
\]

and

\[
E_{\text{sub}}=\{AB,BD,AC\}.
\]

The weights are preserved:

\[
AB=4,\quad BD=6,\quad AC=12.
\]

### Final exam-style answer

One possible subgraph is:

\[
V_{\text{sub}}=\{A,B,C,D\},
\]

\[
E_{\text{sub}}=\{AB,BD,AC\},
\]

with weights:

\[
AB=4,\quad BD=6,\quad AC=12.
\]

### Teaching note

There are many possible answers. A subgraph is not unique. The only rule is that every chosen vertex and every chosen edge must already belong to the original graph.

## Worked Example 3: Find degrees and classify vertices as odd or even

**Evidence source:** Teacher transcript and lesson PDF.

**On-spec status:** Core `FAS2-GRAPH-LO001`, support for `FAS2-GRAPH-LO003`

### Question

A graph has vertices

\[
A,\ B,\ C,\ D,\ E
\]

and edges

\[
AB,\ AC,\ AD,\ AE,\ BD,\ CD.
\]

Find the degree of each vertex and state whether each vertex is odd or even.

### Solution

The degree of a vertex is the number of edges incident to it.

### Vertex \(A\)

The edges incident to \(A\) are:

\[
AB,\ AC,\ AD,\ AE.
\]

There are \(4\) edges.

\[
\deg(A)=4.
\]

Since \(4\) is even, \(A\) is an even vertex.

### Vertex \(B\)

The edges incident to \(B\) are:

\[
AB,\ BD.
\]

There are \(2\) edges.

\[
\deg(B)=2.
\]

Since \(2\) is even, \(B\) is an even vertex.

### Vertex \(C\)

The edges incident to \(C\) are:

\[
AC,\ CD.
\]

There are \(2\) edges.

\[
\deg(C)=2.
\]

Since \(2\) is even, \(C\) is an even vertex.

### Vertex \(D\)

The edges incident to \(D\) are:

\[
AD,\ BD,\ CD.
\]

There are \(3\) edges.

\[
\deg(D)=3.
\]

Since \(3\) is odd, \(D\) is an odd vertex.

### Vertex \(E\)

The edge incident to \(E\) is:

\[
AE.
\]

There is \(1\) edge.

\[
\deg(E)=1.
\]

Since \(1\) is odd, \(E\) is an odd vertex.

### Final exam-style answer

| Vertex | Incident edges | Degree | Odd/even |
|---|---|---:|---|
| \(A\) | \(AB,AC,AD,AE\) | \(4\) | even |
| \(B\) | \(AB,BD\) | \(2\) | even |
| \(C\) | \(AC,CD\) | \(2\) | even |
| \(D\) | \(AD,BD,CD\) | \(3\) | odd |
| \(E\) | \(AE\) | \(1\) | odd |

### Teaching note

Degree is not about edge weights. A weight of \(12\) still counts as one edge. The number on the edge is cargo, not a second road.

## Worked Example 4: Use route terminology

**Evidence source:** Teacher transcript.

**On-spec status:** Core `FAS2-GRAPH-LO003`

### Question

In a graph with vertices

\[
P,\ Q,\ R,\ S,\ T,\ U,
\]

classify the following routes:

1. \(PRUTRPS\)
2. \(PQRTU\)
3. \(PQTRP\)
4. \(PQRTUSP\)

Use the terms walk, path, cycle and Hamiltonian cycle where appropriate.

### Solution

A route is written using capital letters.

For example:

\[
PRUTRPS
\]

means:

\[
P\to R\to U\to T\to R\to P\to S.
\]

### Route 1: \(PRUTRPS\)

This route repeats vertices.

The vertex \(R\) appears twice:

\[
P\to R\to U\to T\to R\to P\to S.
\]

The vertex \(P\) also appears twice.

So it is not a path.

It is still a route through the graph.

Therefore:

\[
PRUTRPS
\]

is a **walk**.

### Route 2: \(PQRTU\)

This route is:

\[
P\to Q\to R\to T\to U.
\]

The vertices are:

\[
P,\ Q,\ R,\ T,\ U.
\]

No vertex is repeated.

Therefore:

\[
PQRTU
\]

is a **path**.

Every path is also a walk, but “path” is the more precise description.

### Route 3: \(PQTRP\)

This route is:

\[
P\to Q\to T\to R\to P.
\]

The route starts at \(P\) and ends at \(P\).

The internal vertices are:

\[
Q,\ T,\ R.
\]

No internal vertex is repeated.

Therefore:

\[
PQTRP
\]

is a **cycle**.

### Route 4: \(PQRTUSP\)

This route is:

\[
P\to Q\to R\to T\to U\to S\to P.
\]

It starts and ends at \(P\).

It includes all six vertices:

\[
P,\ Q,\ R,\ S,\ T,\ U.
\]

No vertex is repeated except the start/end vertex \(P\).

Therefore:

\[
PQRTUSP
\]

is a **Hamiltonian cycle**.

### Final exam-style answer

| Route | Classification |
|---|---|
| \(PRUTRPS\) | walk |
| \(PQRTU\) | path |
| \(PQTRP\) | cycle |
| \(PQRTUSP\) | Hamiltonian cycle |

### Teaching note

The definitions form a little staircase:

\[
\text{walk}\to\text{path}\to\text{cycle}\to\text{Hamiltonian cycle}.
\]

Each step adds a restriction.

## Worked Example 5: Euler’s handshaking lemma in context

**Evidence source:** Teacher transcript.

**On-spec status:** Core support for `FAS2-GRAPH-LO001` and `FAS2-GRAPH-LO003`

### Question

Peter, Quentin, Rory, Shahan, Tahmina and Usman attend a networking event. Each edge in a graph represents a handshake.

The degrees of the vertices are:

\[
\deg(P)=3,\quad \deg(Q)=3,\quad \deg(R)=4,\quad \deg(S)=2,\quad \deg(T)=3,\quad \deg(U)=3.
\]

1. Find the total degree.
2. Find the number of edges.
3. Explain what the number of edges represents.
4. Explain why the degree total is double the edge total.

### Solution

### Part 1: Total degree

Add the degrees:

\[
3+3+4+2+3+3.
\]

Work left to right:

\[
3+3=6.
\]

\[
6+4=10.
\]

\[
10+2=12.
\]

\[
12+3=15.
\]

\[
15+3=18.
\]

So the total degree is:

\[
18.
\]

### Part 2: Number of edges

Euler’s handshaking lemma says:

\[
\sum_{v\in V}\deg(v)=2|E|.
\]

Here:

\[
\sum_{v\in V}\deg(v)=18.
\]

So:

\[
18=2|E|.
\]

Divide both sides by \(2\):

\[
|E|=9.
\]

So there are:

\[
9
\]

edges.

### Part 3: Meaning of the edges

Each edge represents a handshake.

So \(9\) edges means:

\[
9
\]

handshakes took place.

### Part 4: Why degree total is double edge total

Each handshake involves two people.

So each handshake contributes:

\[
1
\]

to one person’s degree and:

\[
1
\]

to the other person’s degree.

Therefore, each handshake contributes:

\[
2
\]

to the total degree.

So the total degree double-counts the number of handshakes.

### Final exam-style answer

\[
3+3+4+2+3+3=18.
\]

\[
18=2|E|.
\]

\[
|E|=9.
\]

There are \(9\) edges, representing \(9\) handshakes.

The degree total is double the edge total because each handshake is counted once for each of the two people involved.

### Teaching note

This is why the result is called the handshaking lemma. One handshake, two people, two degree contributions.

## Worked Example 6: Find \(x\) from degrees and edges

**Evidence source:** Teacher transcript.

**On-spec status:** Core support for `FAS2-GRAPH-LO001` and `FAS2-GRAPH-LO003`

### Question

A graph has five nodes and eight edges.

The valencies of the nodes are:

\[
x,\quad x-1,\quad x+1,\quad 2x-1,\quad x-1.
\]

Find \(x\).

### Solution

Valency means degree.

Euler’s handshaking lemma says:

\[
\sum_{v\in V}\deg(v)=2|E|.
\]

The graph has \(8\) edges, so:

\[
2|E|=2\times 8.
\]

\[
2|E|=16.
\]

Now add the given valencies:

\[
x+(x-1)+(x+1)+(2x-1)+(x-1)=16.
\]

Collect the \(x\)-terms:

\[
x+x+x+2x+x=6x.
\]

Collect the constants:

\[
-1+1-1-1.
\]

First:

\[
-1+1=0.
\]

Then:

\[
0-1-1=-2.
\]

So the left-hand side becomes:

\[
6x-2.
\]

Therefore:

\[
6x-2=16.
\]

Add \(2\) to both sides:

\[
6x=18.
\]

Divide both sides by \(6\):

\[
x=3.
\]

### Final exam-style answer

\[
x+(x-1)+(x+1)+(2x-1)+(x-1)=2(8)
\]

\[
6x-2=16
\]

\[
6x=18
\]

\[
x=3.
\]

### Teaching note

Do not start drawing the graph first. Use the degree total first. The handshaking lemma is the key, like the little brass key in an old desk drawer.

## Worked Example 7: Interpret \(x=3\) as actual degrees

**Evidence source:** Same transcript example as Worked Example 6.

**On-spec status:** Core support for `FAS2-GRAPH-LO001`

### Question

Using:

\[
x=3,
\]

find the actual valencies:

\[
x,\quad x-1,\quad x+1,\quad 2x-1,\quad x-1.
\]

### Solution

Substitute:

\[
x=3.
\]

First valency:

\[
x=3.
\]

Second valency:

\[
x-1=3-1.
\]

\[
x-1=2.
\]

Third valency:

\[
x+1=3+1.
\]

\[
x+1=4.
\]

Fourth valency:

\[
2x-1=2(3)-1.
\]

\[
2x-1=6-1.
\]

\[
2x-1=5.
\]

Fifth valency:

\[
x-1=3-1.
\]

\[
x-1=2.
\]

So the degrees are:

\[
3,\quad 2,\quad 4,\quad 5,\quad 2.
\]

### Check with handshaking lemma

Add the degrees:

\[
3+2+4+5+2.
\]

\[
3+2=5.
\]

\[
5+4=9.
\]

\[
9+5=14.
\]

\[
14+2=16.
\]

The graph has \(8\) edges, so:

\[
2|E|=2(8)=16.
\]

The check works.

### Final exam-style answer

\[
3,\ 2,\ 4,\ 5,\ 2.
\]

These degrees total:

\[
16=2(8),
\]

so they are consistent with a graph having \(8\) edges.

### Teaching note

A degree of \(5\) in a graph with five vertices is possible only if loops or multiple edges may be used, because a simple graph on five vertices has maximum degree \(4\). This is why you must watch whether the graph is required to be simple.

## Worked Example 8: Complete graph edge count

**Evidence source:** Teacher transcript and lesson PDF.

**On-spec status:** Core `FAS2-GRAPH-LO002`

### Question

Find the number of edges in \(K_8\).

### Solution

In \(K_8\), there are:

\[
8
\]

vertices.

Each vertex is connected to every other vertex.

So each vertex has degree:

\[
8-1=7.
\]

The sum of degrees is therefore:

\[
8\times7=56.
\]

By Euler’s handshaking lemma:

\[
\sum_{v\in V}\deg(v)=2|E|.
\]

So:

\[
56=2|E|.
\]

Divide by \(2\):

\[
|E|=28.
\]

### Alternative formula method

For \(K_n\):

\[
|E(K_n)|=\frac{n(n-1)}2.
\]

For \(K_8\):

\[
|E(K_8)|=\frac{8(8-1)}2.
\]

\[
|E(K_8)|=\frac{8\cdot7}{2}.
\]

\[
|E(K_8)|=\frac{56}{2}.
\]

\[
|E(K_8)|=28.
\]

### Final exam-style answer

\[
K_8 \text{ has } 28 \text{ edges.}
\]

### Teaching note

The division by \(2\) is not optional. Counting “each vertex has \(7\) edges” counts every edge twice.

## Worked Example 9: Complete bipartite graph edge count

**Evidence source:** CCEA specification requirement for \(K_{m,n}\). Lesson-specific evidence does not develop this graph family, so this is specification-led.

**On-spec status:** Core `FAS2-GRAPH-LO002`

### Question

Find the number of edges in \(K_{3,5}\).

### Solution

The graph \(K_{3,5}\) has two sets of vertices.

One set contains:

\[
3
\]

vertices.

The other set contains:

\[
5
\]

vertices.

In a complete bipartite graph, every vertex in the first set connects to every vertex in the second set.

So the number of edges is:

\[
3\times5.
\]

\[
3\times5=15.
\]

### Final exam-style answer

\[
K_{3,5}\text{ has }15\text{ edges.}
\]

### Teaching note

Do not connect vertices inside the same part. Bipartite means the graph has two shores, and edges only cross the river.

## Worked Example 10: Star graph degrees

**Evidence source:** CCEA specification requirement for \(S_n\). Lesson-specific evidence does not develop this graph family, so this is specification-led.

**On-spec status:** Core `FAS2-GRAPH-LO002`

### Question

For the star graph \(S_6\), find:

1. the number of edges;
2. the degree of the central vertex;
3. the degree of each outer vertex.

### Solution

The star graph \(S_6\) has one central vertex connected to \(6\) outer vertices.

Each outer vertex is joined directly to the centre.

There are:

\[
6
\]

edges.

The central vertex is incident to all \(6\) edges.

So the degree of the central vertex is:

\[
6.
\]

Each outer vertex has only one edge, joining it to the centre.

So each outer vertex has degree:

\[
1.
\]

### Final exam-style answer

\[
|E(S_6)|=6.
\]

The central vertex has degree:

\[
6.
\]

Each outer vertex has degree:

\[
1.
\]

### Check with handshaking lemma

There is one central vertex of degree \(6\), and \(6\) outer vertices each of degree \(1\).

So the total degree is:

\[
6+6(1).
\]

\[
6+6=12.
\]

The number of edges is \(6\), so:

\[
2|E|=2(6)=12.
\]

The check works.

## Worked Example 11: Identify a tree and a spanning tree

**Evidence source:** Teacher transcript.

**On-spec status:** Core `FAS2-GRAPH-LO005`

### Question

A graph \(G\) has vertices:

\[
A,\ B,\ C,\ D,\ E.
\]

A subgraph \(T\) has edges:

\[
AB,\ AC,\ CD,\ CE.
\]

1. Does \(T\) contain all the vertices of \(G\)?
2. If \(T\) is connected and has no cycles, what type of graph is \(T\)?
3. Is \(T\) a spanning tree of \(G\)?

### Solution

### Part 1

The vertices appearing in \(T\) are:

\[
A,\ B,\ C,\ D,\ E.
\]

These are all the vertices of \(G\).

So \(T\) contains all vertices of \(G\).

### Part 2

The question states that \(T\) is connected and has no cycles.

A connected graph with no cycles is a tree.

So \(T\) is a **tree**.

### Part 3

A spanning tree is a subgraph that:

1. is a tree;
2. contains all vertices of the original graph.

We have shown:

\[
T\text{ contains all vertices of }G.
\]

The question tells us:

\[
T\text{ is connected and has no cycles.}
\]

Therefore:

\[
T\text{ is a tree.}
\]

So:

\[
T\text{ is a spanning tree of }G.
\]

### Final exam-style answer

\(T\) contains all vertices of \(G\). Since \(T\) is connected and has no cycles, \(T\) is a tree. Therefore \(T\) is a spanning tree of \(G\).

### Teaching note

For spanning trees, “spanning” means every vertex is included. It does not mean every edge is included. In fact, including too many edges often creates cycles.

## Worked Example 12: Planarity concept only

**Evidence source:** Uploaded PDF and transcript.

**On-spec status:** Core for basic planarity concept under `FAS2-GRAPH-LO001`; full planarity algorithm excluded from core.

### Question

A graph is drawn with two edges crossing. Explain why this does not automatically prove that the graph is non-planar.

### Solution

A planar graph is a graph that can be drawn so that no two edges meet except at a vertex.

The key phrase is:

\[
\text{can be drawn}.
\]

A graph might have crossings in one drawing but be redrawable without crossings.

Therefore, a crossed drawing does not automatically prove the graph is non-planar.

To prove non-planarity, more argument is needed.

### Final exam-style answer

A crossed drawing does not prove the graph is non-planar, because planarity depends on whether the graph can be redrawn so that edges meet only at vertices.

### Boundary note

The full planarity algorithm from the uploaded lesson is not taught as core CCEA FAS2 content here. It is logged as optional enrichment.

---

# 12. Common Mistakes and Exam Traps

## 12.1 Treating graph theory graphs as coordinate graphs

Wrong idea:

\[
\text{graph}=\text{something with }x\text{- and }y\text{-axes}.
\]

Correct idea:

\[
\text{graph}=\text{vertices connected by edges}.
\]

In this topic, a graph can model stations, people, computers or roads. Axes are not required.

## 12.2 Thinking a crossing is a vertex

A crossing is only a vertex if there is a marked point or label there.

If two edges cross without a vertex, you cannot “turn” at that crossing.

## 12.3 Confusing weights with number of edges

An edge with weight \(14\) is still one edge.

So if \(AE=14\), then edge \(AE\) contributes:

\[
1
\]

to \(\deg(A)\) and:

\[
1
\]

to \(\deg(E)\).

It does not contribute \(14\) to the degree.

## 12.4 Forgetting that a loop counts twice

A loop contributes:

\[
2
\]

to the degree of its vertex.

Not:

\[
1.
\]

## 12.5 Mixing up path and trail

A path restricts vertices.

A trail restricts edges.

| Term | Restriction |
|---|---|
| Path | no vertex repeated |
| Trail | no edge repeated |

The words are tiny. The mark difference can be large.

## 12.6 Mixing up Eulerian and Hamiltonian ideas

Eulerian language is about **edges**.

Hamiltonian language is about **vertices**.

| Concept | Focus |
|---|---|
| Eulerian circuit | uses every edge exactly once |
| Hamiltonian path | visits every vertex exactly once |

## 12.7 Using a necessary condition as if it is automatically sufficient

For example:

- a graph with all even vertices may have an Eulerian circuit only if it is also connected in the relevant part;
- a graph with even degree sum is not automatically constructible under extra restrictions such as simplicity.

Always check the wording.

## 12.8 Forgetting connectedness for trees

A tree must be:

\[
\text{connected}
\]

and:

\[
\text{acyclic}.
\]

A graph with no cycles but two separate pieces is not a tree.

## 12.9 Confusing spanning tree with subgraph

Every spanning tree is a subgraph.

Not every subgraph is a spanning tree.

A spanning tree must contain every vertex of the original graph.

## 12.10 Miscounting \(K_n\)

For \(K_n\), do not answer:

\[
n(n-1).
\]

That double-counts every edge.

Correct:

\[
|E(K_n)|=\frac{n(n-1)}2.
\]

## 12.11 Misbuilding \(K_{m,n}\)

In \(K_{m,n}\), do not join vertices inside the same group.

Only connect between the two groups.

## 12.12 Over-teaching off-spec planarity algorithm

Planarity as a concept is core.

The full planarity algorithm in the uploaded material is labelled “A Level Only” or “A2 only” in that source, and is not confirmed as CCEA FAS2 core from the supplied boundary. It belongs in enrichment, not the central lesson.

---

# 13. Practice Questions

These are **AI-generated on-spec practice questions**, not past-paper or textbook questions.

## 13.1 Basic fluency questions

### Question 1

A graph has:

\[
V=\{A,B,C,D\}
\]

and

\[
E=\{AB,AC,BD,CD\}.
\]

Find the degree of each vertex.

### Question 2

A graph has vertices \(P,Q,R,S\) and edges:

\[
PQ,\ PR,\ RS,\ SP,\ QS.
\]

Is the route

\[
PQRSP
\]

a walk, path, cycle, or Hamiltonian cycle? Give the most precise description possible.

### Question 3

A graph has \(7\) edges. The degrees of all but one of its vertices are:

\[
3,\ 2,\ 4,\ 1,\ 2.
\]

Find the missing degree.

### Question 4

How many edges are there in \(K_9\)?

### Question 5

How many edges are there in \(K_{4,6}\)?

### Question 6

For the star graph \(S_8\), state:

1. the number of edges;
2. the degree of the central vertex;
3. the degree of each outer vertex.

## 13.2 Bridge questions

### Question 7

Explain why the word “graph” in graph theory does not mean the same thing as a graph of \(y=f(x)\).

### Question 8

A weighted graph is drawn with one edge much shorter than another, but its weight is larger.

Explain why this is not a contradiction.

### Question 9

A student says:

“The two lines cross, so there must be a vertex there.”

Explain the mistake.

## 13.3 Standard exam-style questions

### Question 10

A graph has vertices:

\[
A,\ B,\ C,\ D,\ E,\ F
\]

and edges:

\[
AB,\ AC,\ AD,\ BC,\ CD,\ DE,\ EF.
\]

1. Write down the degree of each vertex.
2. State which vertices are odd.
3. Verify Euler’s handshaking lemma for this graph.
4. State whether the graph could have an Eulerian circuit. Give a reason.

### Question 11

A connected graph has vertices with degrees:

\[
2,\ 2,\ 4,\ 4,\ 6.
\]

1. Find the number of edges.
2. State whether the graph could have an Eulerian circuit.
3. Explain your answer.

### Question 12

A graph has five vertices. The degrees are:

\[
x,\ x+1,\ 2x,\ x-1,\ 4.
\]

The graph has \(9\) edges.

Find \(x\).

### Question 13

A subgraph \(T\) of a graph \(G\) contains all \(7\) vertices of \(G\). The subgraph \(T\) is connected and has no cycles.

1. What type of graph is \(T\)?
2. How many edges does \(T\) have?
3. What extra phrase describes \(T\) in relation to \(G\)?

### Question 14

A graph has vertex set:

\[
V=\{A,B,C,D,E\}
\]

and edge set:

\[
E=\{AB,BC,CD,DE,EA,AC\}.
\]

Classify each route as a walk, path, trail or cycle. Give the most precise valid description.

1. \(ABCDE\)
2. \(ABCDEA\)
3. \(ACDEA\)
4. \(ABCDC\)

## 13.4 Harder synthesis questions

### Question 15

A connected graph has \(8\) vertices and \(11\) edges.

Four of the vertex degrees are:

\[
1,\ 2,\ 3,\ 4.
\]

The other four vertex degrees are all equal to \(k\).

Find \(k\), if possible. Then state whether the graph could have an Eulerian circuit.

### Question 16

A graph has \(n\) vertices and is complete.

It has \(66\) edges.

Find \(n\).

### Question 17

A connected graph has exactly two odd vertices.

A student claims:

“It must have an Eulerian circuit.”

Explain whether the student is correct.

### Question 18

A graph \(G\) has \(6\) vertices. A subgraph \(T\) has all \(6\) vertices and \(5\) edges.

A student says:

“Since \(T\) has \(n-1\) edges, it must be a spanning tree.”

Explain why this reasoning is incomplete.

---

# 14. Worked Solutions

## Solution 1

Given:

\[
V=\{A,B,C,D\}
\]

\[
E=\{AB,AC,BD,CD\}.
\]

Degree of \(A\):

Edges incident to \(A\):

\[
AB,\ AC.
\]

\[
\deg(A)=2.
\]

Degree of \(B\):

Edges incident to \(B\):

\[
AB,\ BD.
\]

\[
\deg(B)=2.
\]

Degree of \(C\):

Edges incident to \(C\):

\[
AC,\ CD.
\]

\[
\deg(C)=2.
\]

Degree of \(D\):

Edges incident to \(D\):

\[
BD,\ CD.
\]

\[
\deg(D)=2.
\]

Final answer:

\[
\deg(A)=2,\quad \deg(B)=2,\quad \deg(C)=2,\quad \deg(D)=2.
\]

## Solution 2

The route is:

\[
PQRSP.
\]

This means:

\[
P\to Q\to R\to S\to P.
\]

It starts at \(P\) and ends at \(P\).

The internal vertices are:

\[
Q,\ R,\ S.
\]

No internal vertex is repeated.

It visits all four vertices:

\[
P,\ Q,\ R,\ S.
\]

Therefore, it is a cycle that includes every vertex.

Final answer:

\[
PQRSP
\]

is a Hamiltonian cycle.

## Solution 3

A graph has \(7\) edges.

By Euler’s handshaking lemma:

\[
\sum \deg(v)=2|E|.
\]

\[
\sum \deg(v)=2(7).
\]

\[
\sum \deg(v)=14.
\]

Known degrees:

\[
3,\ 2,\ 4,\ 1,\ 2.
\]

Add them:

\[
3+2+4+1+2.
\]

\[
3+2=5.
\]

\[
5+4=9.
\]

\[
9+1=10.
\]

\[
10+2=12.
\]

Let the missing degree be \(d\).

\[
12+d=14.
\]

Subtract \(12\):

\[
d=2.
\]

Final answer:

\[
2.
\]

## Solution 4

For \(K_9\):

\[
|E(K_n)|=\frac{n(n-1)}2.
\]

So:

\[
|E(K_9)|=\frac{9(9-1)}2.
\]

\[
|E(K_9)|=\frac{9\cdot8}{2}.
\]

\[
|E(K_9)|=\frac{72}{2}.
\]

\[
|E(K_9)|=36.
\]

Final answer:

\[
36.
\]

## Solution 5

For \(K_{4,6}\):

\[
|E(K_{m,n})|=mn.
\]

Here:

\[
m=4,\quad n=6.
\]

So:

\[
|E(K_{4,6})|=4\cdot6.
\]

\[
|E(K_{4,6})|=24.
\]

Final answer:

\[
24.
\]

## Solution 6

For \(S_8\), there is one central vertex connected to \(8\) outer vertices.

Number of edges:

\[
8.
\]

Degree of central vertex:

\[
8.
\]

Degree of each outer vertex:

\[
1.
\]

Final answer:

\[
|E(S_8)|=8.
\]

Central vertex degree:

\[
8.
\]

Each outer vertex degree:

\[
1.
\]

## Solution 7

In ordinary coordinate geometry, a graph usually means a curve or relation drawn on axes, such as:

\[
y=f(x).
\]

In graph theory, a graph is a collection of vertices connected by edges.

So a graph-theory graph does not need:

- an \(x\)-axis;
- a \(y\)-axis;
- coordinates;
- a function rule.

It models connections, not necessarily numerical input-output relationships.

## Solution 8

A weighted graph is not normally drawn to scale.

The drawn length of an edge is just part of the diagram layout.

The weight is the number written on the edge.

So an edge may be drawn short but have a large weight, or drawn long but have a small weight.

The weight is the mathematical information.

## Solution 9

The student has assumed that a visual crossing automatically creates a vertex.

This is not true.

A vertex must be marked, usually by a dot or a label.

If two edges cross but there is no marked vertex, then the route cannot change direction at that crossing.

Final answer:

The crossing is not a vertex unless the graph marks it as one.

## Solution 10

Given:

\[
V=\{A,B,C,D,E,F\}
\]

\[
E=\{AB,AC,AD,BC,CD,DE,EF\}.
\]

### Part 1: Degrees

For \(A\):

\[
AB,\ AC,\ AD.
\]

\[
\deg(A)=3.
\]

For \(B\):

\[
AB,\ BC.
\]

\[
\deg(B)=2.
\]

For \(C\):

\[
AC,\ BC,\ CD.
\]

\[
\deg(C)=3.
\]

For \(D\):

\[
AD,\ CD,\ DE.
\]

\[
\deg(D)=3.
\]

For \(E\):

\[
DE,\ EF.
\]

\[
\deg(E)=2.
\]

For \(F\):

\[
EF.
\]

\[
\deg(F)=1.
\]

So:

\[
\deg(A)=3,\quad \deg(B)=2,\quad \deg(C)=3,
\]

\[
\deg(D)=3,\quad \deg(E)=2,\quad \deg(F)=1.
\]

### Part 2: Odd vertices

Odd degrees:

\[
3,\ 3,\ 3,\ 1.
\]

So the odd vertices are:

\[
A,\ C,\ D,\ F.
\]

### Part 3: Verify Euler’s handshaking lemma

Sum of degrees:

\[
3+2+3+3+2+1.
\]

\[
3+2=5.
\]

\[
5+3=8.
\]

\[
8+3=11.
\]

\[
11+2=13.
\]

\[
13+1=14.
\]

There are \(7\) edges.

\[
2|E|=2(7).
\]

\[
2|E|=14.
\]

So:

\[
\sum\deg(v)=2|E|.
\]

Euler’s handshaking lemma is verified.

### Part 4: Eulerian circuit

For an Eulerian circuit in a connected graph, every vertex must have even degree.

This graph has odd vertices:

\[
A,\ C,\ D,\ F.
\]

Therefore, it cannot have an Eulerian circuit.

Final answer:

No, the graph cannot have an Eulerian circuit because it has odd vertices.

## Solution 11

Degrees:

\[
2,\ 2,\ 4,\ 4,\ 6.
\]

### Part 1: Number of edges

Sum of degrees:

\[
2+2+4+4+6.
\]

\[
2+2=4.
\]

\[
4+4=8.
\]

\[
8+4=12.
\]

\[
12+6=18.
\]

Euler’s handshaking lemma:

\[
\sum\deg(v)=2|E|.
\]

So:

\[
18=2|E|.
\]

Divide by \(2\):

\[
|E|=9.
\]

### Part 2: Eulerian circuit

All degrees are even:

\[
2,\ 2,\ 4,\ 4,\ 6.
\]

The question says the graph is connected.

So the graph could have an Eulerian circuit.

Final answer:

\[
|E|=9.
\]

The graph could have an Eulerian circuit because it is connected and all vertices have even degree.

## Solution 12

Degrees:

\[
x,\ x+1,\ 2x,\ x-1,\ 4.
\]

The graph has \(9\) edges.

Euler’s handshaking lemma:

\[
\sum\deg(v)=2|E|.
\]

\[
x+(x+1)+2x+(x-1)+4=2(9).
\]

Simplify the left-hand side.

Collect \(x\)-terms:

\[
x+x+2x+x=5x.
\]

Collect constants:

\[
1-1+4=4.
\]

So:

\[
5x+4=18.
\]

Subtract \(4\):

\[
5x=14.
\]

Divide by \(5\):

\[
x=\frac{14}{5}.
\]

But degrees must be whole numbers.

So no such graph can exist with these degree expressions and \(9\) edges.

Final answer:

\[
x=\frac{14}{5},
\]

which is not an integer, so the graph is not constructible under these conditions.

## Solution 13

A subgraph \(T\) contains all \(7\) vertices of \(G\).

It is connected and has no cycles.

### Part 1

A connected graph with no cycles is a tree.

So:

\[
T
\]

is a tree.

### Part 2

A tree with \(n\) vertices has \(n-1\) edges.

Here:

\[
n=7.
\]

So:

\[
n-1=7-1.
\]

\[
n-1=6.
\]

So \(T\) has:

\[
6
\]

edges.

### Part 3

Since \(T\) is a tree and contains all vertices of \(G\), it is a spanning tree of \(G\).

Final answer:

\(T\) is a tree, it has \(6\) edges, and it is a spanning tree of \(G\).

## Solution 14

Given:

\[
V=\{A,B,C,D,E\}
\]

\[
E=\{AB,BC,CD,DE,EA,AC\}.
\]

### Route 1: \(ABCDE\)

\[
A\to B\to C\to D\to E.
\]

Check edges:

\[
AB,\ BC,\ CD,\ DE
\]

all exist.

No vertex is repeated.

So \(ABCDE\) is a path.

### Route 2: \(ABCDEA\)

\[
A\to B\to C\to D\to E\to A.
\]

Check edges:

\[
AB,\ BC,\ CD,\ DE,\ EA
\]

all exist.

The route starts and ends at \(A\).

No other vertex is repeated.

It visits every vertex.

So it is a Hamiltonian cycle.

### Route 3: \(ACDEA\)

\[
A\to C\to D\to E\to A.
\]

Check edges:

\[
AC,\ CD,\ DE,\ EA
\]

all exist.

The route starts and ends at \(A\).

No other vertex is repeated.

It is a cycle.

It does not include vertex \(B\), so it is not Hamiltonian.

### Route 4: \(ABCDC\)

\[
A\to B\to C\to D\to C.
\]

Check edges:

\[
AB,\ BC,\ CD,\ DC
\]

where \(DC\) is the same undirected edge as \(CD\).

The edge \(CD\) is used twice:

\[
C\to D
\]

and:

\[
D\to C.
\]

So it is not a trail.

The vertex \(C\) is repeated, so it is not a path.

It is still a walk.

Final answer:

| Route | Most precise classification |
|---|---|
| \(ABCDE\) | path |
| \(ABCDEA\) | Hamiltonian cycle |
| \(ACDEA\) | cycle |
| \(ABCDC\) | walk |

## Solution 15

The graph has \(8\) vertices and \(11\) edges.

By Euler’s handshaking lemma:

\[
\sum\deg(v)=2|E|.
\]

\[
\sum\deg(v)=2(11).
\]

\[
\sum\deg(v)=22.
\]

Four known degrees are:

\[
1,\ 2,\ 3,\ 4.
\]

Their sum is:

\[
1+2+3+4=10.
\]

The other four degrees are all \(k\), so their total is:

\[
4k.
\]

Therefore:

\[
10+4k=22.
\]

Subtract \(10\):

\[
4k=12.
\]

Divide by \(4\):

\[
k=3.
\]

So the degrees are:

\[
1,\ 2,\ 3,\ 4,\ 3,\ 3,\ 3,\ 3.
\]

Now count odd vertices.

Odd degrees:

\[
1,\ 3,\ 3,\ 3,\ 3,\ 3.
\]

There are \(6\) odd vertices.

For an Eulerian circuit, every vertex must have even degree.

This graph has odd vertices.

Therefore, it cannot have an Eulerian circuit.

Final answer:

\[
k=3.
\]

The graph cannot have an Eulerian circuit because it has odd vertices.

## Solution 16

A complete graph with \(n\) vertices has:

\[
\frac{n(n-1)}2
\]

edges.

Given:

\[
\frac{n(n-1)}2=66.
\]

Multiply both sides by \(2\):

\[
n(n-1)=132.
\]

So:

\[
n^2-n=132.
\]

Bring all terms to one side:

\[
n^2-n-132=0.
\]

Factorise:

\[
n^2-n-132=(n-12)(n+11).
\]

So:

\[
(n-12)(n+11)=0.
\]

Therefore:

\[
n-12=0
\]

or:

\[
n+11=0.
\]

So:

\[
n=12
\]

or:

\[
n=-11.
\]

A graph cannot have a negative number of vertices, so:

\[
n=12.
\]

Final answer:

\[
K_{12}
\]

has \(66\) edges, so:

\[
n=12.
\]

## Solution 17

A connected graph has exactly two odd vertices.

The student claims:

“It must have an Eulerian circuit.”

This is incorrect.

A connected graph has an Eulerian circuit when every vertex has even degree.

If it has exactly two odd vertices, it may have an Eulerian trail that starts at one odd vertex and ends at the other odd vertex.

But it cannot have an Eulerian circuit.

Final answer:

The student is not correct. Exactly two odd vertices allows an Eulerian trail, not an Eulerian circuit.

## Solution 18

The graph \(G\) has \(6\) vertices.

The subgraph \(T\) has all \(6\) vertices and \(5\) edges.

A tree with \(n\) vertices has \(n-1\) edges.

Here:

\[
n=6.
\]

\[
n-1=6-1=5.
\]

So the edge count is consistent with a tree.

However, this does not by itself prove that \(T\) is a tree.

To be a tree, \(T\) must be:

1. connected;
2. have no cycles.

The student has checked only the edge count.

Final answer:

The reasoning is incomplete because \(T\) must also be shown to be connected and acyclic. Having \(n-1\) edges alone is not enough unless the required connectedness or acyclicity condition is also established.

---

# 15. Exam Technique Notes

## 15.1 Define terms exactly

Graph theory is vocabulary-heavy.

For definition marks, use crisp wording:

- A graph consists of vertices connected by edges.
- A weighted graph has a number associated with each edge.
- A path is a walk with no repeated vertices.
- A trail is a walk with no repeated edges.
- A tree is a connected graph with no cycles.

Do not write poetic fog such as “a graph is where points are joined together somehow”. The examiner’s pen enjoys precision.

## 15.2 Use capital letters for routes

Routes should be written as strings of vertex labels:

\[
ABCDE
\]

or with arrows:

\[
A\to B\to C\to D\to E.
\]

If clarity matters, arrows are safer.

## 15.3 State whether vertices or edges repeat

When classifying a route, explicitly check:

- Are all consecutive pairs connected by edges?
- Is any vertex repeated?
- Is any edge repeated?
- Does the route start and finish at the same vertex?
- Does it include every vertex?
- Does it include every edge?

## 15.4 Use handshaking lemma before drawing

If a question gives degrees and edge count, start with:

\[
\sum\deg(v)=2|E|.
\]

This often gives the unknown immediately.

## 15.5 Parity is a quick impossibility test

If the number of odd vertices is odd, the graph is impossible.

If the degree total is odd, the graph is impossible.

Why?

Because:

\[
\sum\deg(v)=2|E|
\]

must be even.

## 15.6 For \(K_n\), divide by \(2\)

Write:

\[
|E(K_n)|=\frac{n(n-1)}2.
\]

The division by \(2\) prevents double-counting.

## 15.7 For \(K_{m,n}\), do not divide by \(2\)

Write:

\[
|E(K_{m,n})|=mn.
\]

Here you are counting connections from one part to the other, and each edge is counted once.

## 15.8 For trees, use the two-part definition

Tree:

\[
\text{connected and no cycles}.
\]

Spanning tree:

\[
\text{tree subgraph containing all original vertices}.
\]

## 15.9 Weighted graph warning

A weighted graph is not normally drawn to scale. Use the weights, not the visual lengths. The uploaded lesson PDF makes this warning explicitly in the modelling-with-graphs section.

## 15.10 Planarity boundary

For this CCEA FAS2 lesson:

Core:

\[
\text{definition and recognition of planarity}.
\]

Not core unless later CCEA evidence confirms it:

\[
\text{full planarity algorithm}.
\]

---

# 16. Syllabus Gap Check

## 16.1 LO coverage table

| LO ID | Coverage in lesson | Coverage status |
|---|---|---|
| `FAS2-GRAPH-LO001` | Vertex, edge, degree, planarity, subgraph | Covered |
| `FAS2-GRAPH-LO002` | \(K_n\), \(K_{m,n}\), \(S_n\) | Covered, but \(K_{m,n}\) and \(S_n\) are specification-led due to thin lesson evidence |
| `FAS2-GRAPH-LO003` | Walk, path, trail, cycle, circuit, Eulerian circuit, Hamiltonian path, conditions using degree parity | Covered |
| `FAS2-GRAPH-LO004` | Weighted graphs/networks and digraphs | Covered |
| `FAS2-GRAPH-LO005` | Tree, connectedness, root, binary tree, spanning tree | Covered, but rooted/binary tree are specification-led due to thin lesson evidence |

## 16.2 Evidence coverage table

| Evidence item | Covered in lesson? | Notes |
|---|---:|---|
| Graph definition | Yes | Core definition used |
| Weighted graph/network | Yes | Includes warning not drawn to scale |
| Subgraph | Yes | Worked example included |
| Degree/valency/order | Yes | Worked examples included |
| Odd/even vertices | Yes | Linked to handshaking lemma |
| Route notation | Yes | Capital-letter routes used |
| Walk/path/trail/cycle | Yes | Definitions and examples included |
| Eulerian circuit | Yes | Defined and linked to conditions |
| Hamiltonian cycle | Yes | Included as evidence-related support |
| Hamiltonian path | Yes | Included as official CCEA wording |
| Connected graph | Yes | Covered |
| Loop | Yes | Includes degree contribution of \(2\) |
| Simple graph | Yes | Covered |
| Directed graph/digraph | Yes | Covered |
| Euler handshaking lemma | Yes | Fully developed |
| Tree/spanning tree | Yes | Covered |
| Complete graph \(K_n\) | Yes | Formula derived |
| Complete bipartite \(K_{m,n}\) | Yes | Specification-led |
| Star \(S_n\) | Yes | Specification-led |
| Isomorphic graphs | Not core | Logged as enrichment |
| Matrix representation | Not core | Logged as enrichment |
| Full planarity algorithm | Not core | Excluded from core |

## 16.3 Bridge coverage table

| Bridge idea | Included? | Where |
|---|---:|---|
| Ordinary graph as curve vs Further graph as network | Yes | Sections 5, 6, 8 |
| Counting and double-counting | Yes | Handshaking lemma |
| Diagrams and modelling | Yes | Weighted graphs, networks, connectedness |
| Proof and explanation | Yes | Eulerian conditions, impossibility checks |
| Table reading | Yes | Degree tables and classification tables |

## 16.4 Off-Spec Content Found but Excluded

### Full planarity algorithm

The uploaded PDF includes a planarity algorithm requiring a Hamiltonian cycle, drawing vertices as a polygon, labelling edges inside/outside and checking crossing constraints. The PDF explicitly labels this section “A Level Only”, and the transcript also describes it as A2-only in that source.

This lesson includes only the core FAS2 concept of planarity:

\[
\text{can the graph be drawn so edges meet only at vertices?}
\]

The full algorithm is excluded from core teaching.

### Matrix representation of graphs

The uploaded lesson develops adjacency and distance matrices. The transcript describes an adjacency matrix as showing the number of edges joining corresponding vertices and notes how loops and directed graphs affect entries.

However, matrix representation is not named in the supplied `FAS2-GRAPH` LO wording, so it is not taught as core content here.

### Isomorphic graphs

The uploaded transcript develops isomorphic graphs as graphs showing the same information in different forms.

This is not named in the supplied `FAS2-GRAPH` LO wording, so it is treated as optional enrichment only.

## 16.5 Optional Enrichment Not Required by CCEA

The following can be placed in extension panels if desired:

1. adjacency matrices;
2. distance matrices;
3. isomorphic graph checking;
4. full planarity algorithm;
5. proof of tree edge count \(n-1\);
6. non-planarity of \(K_5\) and \(K_{3,3}\), if later confirmed by the intended route.

## 16.6 Weak evidence warnings

| Area | Warning |
|---|---|
| \(K_{m,n}\) | Required by CCEA, but not developed in uploaded lesson-specific evidence |
| \(S_n\) | Required by CCEA, but not developed in uploaded lesson-specific evidence |
| Rooted tree | Required by CCEA, but not developed in uploaded lesson-specific evidence |
| Binary tree | Required by CCEA, but not developed in uploaded lesson-specific evidence |
| Screenshot PDF | Visuals available only through preview; no parsed text available |

## 16.7 Missing Evidence Log

| Missing evidence | Impact |
|---|---|
| Official CCEA worked examples for Graph Theory | Generated examples are on-spec but not past-paper labelled |
| Mark schemes for CCEA graph theory questions | Exam technique is general and evidence-led, not mark-scheme-specific |
| Full lesson-specific examples for \(K_{m,n}\), \(S_n\), rooted tree, binary tree | Covered from specification boundary, but extra examples are AI-proposed |
| Fully inspectable screenshot text | No hidden visual details claimed |

---

# 17. Recommended Enhancements Not in the Evidence

These are AI-proposed enhancements. They are not claimed as evidence-backed diagrams or official examples.

## 17.1 Diagrams

1. **Graph theory dictionary wall**
   - A single visual glossary showing vertex, edge, loop, multiple edge, weighted edge, directed edge and crossing non-vertex.

2. **Walk/path/trail/cycle route overlay**
   - Same graph, four route overlays.
   - Each overlay uses a checklist:
     - repeated vertex?
     - repeated edge?
     - closed?
     - all vertices?

3. **Eulerian vs Hamiltonian split diagram**
   - Left panel: “Eulerian thinks about edges.”
   - Right panel: “Hamiltonian thinks about vertices.”

4. **Special graph family cards**
   - \(K_n\), \(K_{m,n}\), \(S_n\).
   - Each card includes:
     - diagram;
     - degree pattern;
     - edge count;
     - common mistake.

5. **Tree decision flowchart**
   - Is it connected?
   - Does it contain a cycle?
   - Does it contain all original vertices?
   - Therefore: not tree, tree, or spanning tree.

## 17.2 Animations

1. **Handshaking lemma animation**
   - Each edge lights up at both endpoints.
   - Counter shows degree total increasing by \(2\) per edge.

2. **Spanning tree builder**
   - Student deletes edges from a connected graph until no cycles remain.

3. **Planarity redraw demonstration**
   - Shows a graph with crossings being redrawn without crossings.
   - Carefully labelled as planarity concept, not full algorithm.

## 17.3 Widgets

1. **Degree checker**
   - Already planned as `FAS2GraphTheoryWidget-001`.

2. **Route classifier**
   - Already planned as `FAS2GraphTheoryWidget-002`.

3. **Spanning tree checker**
   - Already planned as `FAS2GraphTheoryWidget-003`.

## 17.4 Extra examples

1. Constructing a graph from a degree sequence.
2. Detecting impossible degree sequences.
3. Comparing \(K_5\) and \(K_{2,3}\).
4. Finding all odd vertices and predicting possible Eulerian traversability.
5. Identifying a spanning tree from a larger weighted network.

---

# 18. Supplementary Sources Used

## 18.1 Project Sources used

- CCEA GCE Further Mathematics Specification Map.
- Further Maths README Module Map.
- Further Maths Evidence Drop Checklist.
- Ordinary A-Level Maths Bridge Spec Extracts.

## 18.2 Lesson-specific evidence used

- `transcripts.md`, containing teacher transcript for “Chapter 2: Graphs & Networks”.
- `Decision Maths 1 chapter 2 Graphs and networks (including A2 content Planarity Alg).pdf`.
- `Chapter_2_Graphs_&_Networks_💻_(Decision_1)_screenshots.pdf`.

## 18.3 Ordinary A-Level Maths bridge sources

Ordinary A-Level Maths bridge material was used only to explain prior skills:

- diagram interpretation;
- algebraic notation;
- proof language;
- counting and double-counting;
- table reading.

It was not used to override the Further Mathematics specification.

## 18.4 Cross-board and third-party source notes

The uploaded lesson PDF references Pearson Decision 1 exercises and uses “Decision 1” language. These references are treated as lesson evidence and not as CCEA authority.

## 18.5 Evidence limitations

The screenshot PDF could not be parsed as text. Only visible preview details and matching transcript/PDF content were used.

The uploaded material contains A2-only planarity algorithm content. This is excluded from the core FAS2 lesson.

## 18.6 Final evidence boundary statement

The core lesson follows CCEA `FAS2-GRAPH` boundaries. Where uploaded lesson evidence contains additional material not confirmed by the CCEA FAS2 topic boundary, it has been logged as optional enrichment or excluded from core teaching.

---

# 19. Final Student Checklist

## 19.1 Prerequisite confidence checklist

Before moving on, check that you can:

- [ ] count carefully without skipping objects;
- [ ] identify odd and even numbers;
- [ ] read a labelled diagram;
- [ ] write a list using set notation;
- [ ] explain a conclusion in a full sentence;
- [ ] avoid assuming diagrams are drawn to scale.

## 19.2 Further Maths method checklist

You should now be able to:

- [ ] define a graph using vertices and edges;
- [ ] explain the difference between vertices/nodes and edges/arcs;
- [ ] identify a weighted graph or network;
- [ ] write a vertex set;
- [ ] write an edge set;
- [ ] identify a subgraph;
- [ ] calculate the degree/valency/order of each vertex;
- [ ] classify vertices as odd or even;
- [ ] use Euler’s handshaking lemma:
  \[
  \sum\deg(v)=2|E|;
  \]
- [ ] explain why the number of odd vertices is even;
- [ ] classify walks, paths, trails, cycles and circuits;
- [ ] distinguish Eulerian circuits from Hamiltonian paths;
- [ ] recognise connected graphs;
- [ ] recognise loops and multiple edges;
- [ ] recognise simple graphs;
- [ ] recognise directed graphs or digraphs;
- [ ] calculate the number of edges in \(K_n\);
- [ ] calculate the number of edges in \(K_{m,n}\);
- [ ] describe a star graph \(S_n\);
- [ ] recognise trees and spanning trees;
- [ ] define rooted trees and binary trees at the required basic level;
- [ ] explain planarity as a redrawable no-crossing property.

## 19.3 Exam technique checklist

In an exam, remember to:

- [ ] use the exact definitions;
- [ ] write routes with capital letters;
- [ ] check repeated vertices and repeated edges separately;
- [ ] remember that loops count twice for degree;
- [ ] remember that edge weights do not affect degree;
- [ ] use handshaking lemma before trying to draw a graph;
- [ ] divide by \(2\) for \(K_n\);
- [ ] not divide by \(2\) for \(K_{m,n}\);
- [ ] check connectedness before claiming a tree or Eulerian circuit;
- [ ] explain why a graph cannot have an Eulerian circuit if odd vertices exist;
- [ ] avoid treating a crossing as a vertex;
- [ ] keep full planarity algorithm material separate from core FAS2 unless specifically required.

## 19.4 Bridge checklist

You should be clear that:

- [ ] ordinary coordinate graphs are different from graph-theory graphs;
- [ ] graph theory is about connections;
- [ ] diagram layout is not the same as mathematical structure;
- [ ] double-counting is the heart of Euler’s handshaking lemma;
- [ ] old table-reading and proof skills still matter.

## 19.5 Visual understanding checklist

You should be able to look at a graph and identify:

- [ ] vertices;
- [ ] edges;
- [ ] weights;
- [ ] loops;
- [ ] multiple edges;
- [ ] directed edges;
- [ ] crossings that are not vertices;
- [ ] odd and even vertices;
- [ ] connected and disconnected parts;
- [ ] cycles;
- [ ] possible trees;
- [ ] possible spanning trees.
