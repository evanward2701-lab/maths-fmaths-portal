# FA22 Graph Theory: Bipartite Matchings and Complete Matchings

## 1. Lesson Title and Metadata

| Field | Value |
|---|---|
| Date generated | 2026-06-04 |
| Course | CCEA GCE Further Mathematics |
| Unit code | `FA22` |
| Unit name | Further A2 2 Applied Mathematics |
| Applied section | Section D: Discrete and Decision Mathematics |
| Topic code | `FA22-GRAPH` |
| Topic name | Graph theory |
| Lesson focus | Bipartite graphs, matchings, complete matchings and Hall’s marriage theorem |
| Topic slug | `graph_theory_bipartite_matchings` |
| Topic Pascal | `GraphTheoryBipartiteMatchings` |
| Topic ID | `FA22GraphTheoryBipartiteMatchings` |
| Lesson file name | `FA22_graph_theory_bipartite_matchings_lesson.md` |
| Core LO IDs | `FA22-GRAPH-LO003`, `FA22-GRAPH-LO004` |
| Bridge tags | `#OrdinaryMathsBridge`, `#Tables`, `#SetNotation`, `#Counting`, `#ProofLanguage`, `#AlgorithmicReasoning` |
| Topic tags | `#FA22`, `#GRAPH`, `#Decision`, `#GraphTheory`, `#BipartiteGraphs`, `#Matching`, `#CompleteMatching`, `#HallsMarriageTheorem`, `#SectionD` |

### Boundary Notice

The uploaded lesson-specific evidence teaches **D2 Allocation Problems**, including weighted cost matrices and the Hungarian algorithm. This is useful mathematical context, but it is **not confirmed as CCEA core content** by the supplied CCEA Further Mathematics specification map.

This lesson therefore teaches the CCEA-safe core:

```text
Bipartite graphs, matchings, complete matchings and Hall’s marriage theorem.
```

The Hungarian algorithm and weighted allocation procedures are logged as optional enrichment only, not as required CCEA content.

---

## 2. Evidence Map

| Evidence source | Evidence role in this lesson | How it is used |
|---|---|---|
| `CCEA_GCE_Further_Mathematics_Specification_Map.md` | Core CCEA authority | Supplies `FA22-GRAPH-LO003` and `FA22-GRAPH-LO004`, the official topic boundary and Section D classification. |
| `Further_Maths_README_module_map.md` | Workflow and metadata authority | Supplies required metadata format, file naming conventions and bridge expectations. |
| `Further_Maths_EVIDENCE_DROP_CHECKLIST.md` | Evidence-control source | Confirms off-spec content must be excluded from the core lesson. |
| `Ordinary_A_Level_Maths_Bridge_Spec_Extracts.md` | Bridge context only | Supplies the idea that Graph theory has no direct ordinary A-Level predecessor and should be bridged using proof, tables, counting and algorithmic reasoning. |
| `Further Maths Portal Build – Knowledge Evidence.txt` | Project workflow source | Confirms phase structure, lesson sections and asset placeholder rules. |
| `transcripts.md` | Lesson-specific transcript | Supplies D2 allocation context, including worker-task cost matrices, one-worker-to-one-task language, Hungarian algorithm steps, dummy entries, maximum allocation, incomplete data and allocation LP formulation. This is used only for boundary logging and optional enrichment. |
| `Chapter_2_Allocation_Problems_⌨️_(Decision_2)_screenshots.pdf` | Lesson-specific visual evidence | Confirms the screenshot chapter title and visible D2 contents list: Hungarian algorithm, dummy entries, maximum allocation, incomplete data and A2-only linear programming. Used only for boundary logging and optional enrichment planning. |

---

## 3. Specification Alignment

| LO ID | Official CCEA wording | Lesson coverage | Evidence source | Syllabus boundary | Ordinary A-Level Maths bridge |
|---|---|---|---|---|---|
| `FA22-GRAPH-LO003` | demonstrate understanding of and work with bipartite graphs, including matchings and complete matchings | Define bipartite graph, matching and complete matching; represent assignment situations as bipartite graphs; find and justify matchings by inspection and reasoning. | CCEA Further Mathematics specification map | Core. Weighted cost optimisation is excluded unless separately specified by CCEA. | Tables, set notation, mappings and counting. |
| `FA22-GRAPH-LO004` | demonstrate understanding of and use Hall’s marriage theorem | State Hall’s theorem; define \(N(S)\); test subsets \(S\); prove whether a complete matching exists; interpret failure of Hall’s condition. | CCEA Further Mathematics specification map | Core. The theorem checks existence of complete matchings, not minimum-cost allocation. | Proof language, subset notation, counting inequalities. |

### Neighbouring CCEA Content Not Covered Here

| LO ID | Reason not included |
|---|---|
| `FA22-GRAPH-LO001` | Vertex and edge colouring are part of FA22 Graph theory but not this lesson focus. |
| `FA22-GRAPH-LO002` | Cutsets and max-flow min-cut theorem are part of FA22 Graph theory but not this lesson focus. |
| `FA22-ALGGRAPH-LO003` | Simplex algorithm and tableau for two-variable linear programming is a separate FA22 Algorithms on graphs topic. The uploaded D2 allocation LP is not the same as CCEA two-variable simplex tableau. |

---

## 4. Learning Objectives

### Core Further Maths Objectives

By the end of this lesson, you should be able to:

1. Define a bipartite graph.
2. Identify the two disjoint vertex sets in a bipartite graph.
3. Explain why every edge in a bipartite graph must join a vertex in one set to a vertex in the other set.
4. Define a matching.
5. Decide whether a given set of edges is a matching.
6. Define a complete matching from one vertex set to another.
7. Construct a complete matching where one exists.
8. State Hall’s marriage theorem using correct set notation.
9. For a subset \(S\), find its neighbourhood \(N(S)\).
10. Test Hall’s condition:
   \[
   |N(S)|\ge |S|
   \]
   for relevant subsets.
11. Use Hall’s theorem to prove that a complete matching exists.
12. Use Hall’s theorem to prove that a complete matching does not exist.

### Bridge Objectives

You should be able to connect this lesson to ordinary A-Level Maths by:

1. Reading information from tables and converting it into mathematical structure.
2. Using set notation correctly.
3. Counting elements in a set.
4. Writing a short proof using a condition and a conclusion.
5. Recognising the difference between a numerical cost table and an adjacency table.

### Exam Technique Objectives

You should be able to:

1. Label the two parts of a bipartite graph clearly.
2. Avoid using the same vertex twice in a matching.
3. Show enough subset-neighbourhood checks for Hall’s theorem.
4. State clearly whether the matching is complete.
5. Avoid importing the Hungarian algorithm into a CCEA graph theory question unless the question explicitly asks for it.

---

## 5. Explicit Prerequisite Recap

### GCSE Foundations

You need:

- Counting objects in a set.
- Reading tables.
- Drawing simple diagrams.
- Understanding that an edge or line can represent a relationship between two objects.
- Interpreting “possible” and “not possible” links.

### Ordinary AS/A2 Mathematics Foundations

You need:

- Set notation:
  \[
  A=\{a,b,c\}
  \]
- The number of elements in a set:
  \[
  |A|=3
  \]
- Basic inequality language:
  \[
  |N(S)|\ge |S|
  \]
- Function or mapping language, especially the idea that one input can be paired with one output.
- Table-reading skills.

### Previous Further Mathematics Foundations

Useful but not absolutely required:

- FAS2 Graph theory language: vertex, edge, path, graph.
- General Decision Mathematics habit: define the objects before applying the rule.
- Basic proof language: “For this subset”, “therefore”, “hence”, “so no complete matching exists”.

### A-Level Maths Bridge: What You Already Know and What Further Maths Changes

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| AS1 Algebra and Functions | You used tables, mappings and function notation to connect inputs and outputs. | A bipartite matching pairs objects from one set with objects from another set, but with graph-theoretic restrictions. | Do not assume every pairing is allowed. Only edges in the graph can be used. |
| AS1 / A21 proof language | You learned to justify algebraic statements using clear logical steps. | Hall’s theorem requires a condition to be checked for subsets \(S\), then a conclusion about complete matching. | A diagram that “looks possible” is not proof unless the required matching or Hall condition is shown. |
| AS2 / A22 table interpretation | You read information from tables and interpreted what entries mean. | A table may become an adjacency table for a bipartite graph. | A cost matrix is not automatically an adjacency matrix. In this CCEA lesson, edges mean “allowed”, not “has numerical cost”. |
| Counting and set notation | You counted elements and used finite sets. | Hall’s condition compares \(|S|\) with \(|N(S)|\). | Missing one subset can invalidate the theorem check. |
| Algorithmic reasoning | You followed ordered procedures in numerical methods, statistics and applied topics. | Further Decision Mathematics often uses precise graph conditions and algorithms. | The Hungarian algorithm is from the uploaded D2 evidence, but it is not CCEA core for this lesson. |

In ordinary A-Level Maths, this idea appeared as tables, mappings, counting and proof.  
In Further Maths, the same idea becomes a graph structure: one set of objects is connected to another set by edges.  
The key upgrade is that the question is no longer just “can I pair these objects?” but “can I choose edges so that every required vertex is matched exactly once?”  
The danger is that weighted allocation methods, especially the Hungarian algorithm, are tempting because they also assign workers to tasks. For CCEA FA22 Graph theory, the core question is about **existence of matchings**, not minimum-cost optimisation.

---

## 6. Big Picture Explanation

A bipartite matching problem is about controlled pairing.

Imagine two separate islands of objects:

\[
U=\{\text{workers}\}
\]

and

\[
W=\{\text{tasks}\}.
\]

An edge joins a worker to a task only when that worker is allowed to do that task. The graph is bipartite because the two types of objects stay on opposite sides. Edges go across the water. No edges are allowed inside the worker island, and no edges are allowed inside the task island.

A **matching** chooses some of the edges, but it must obey one strict rule:

```text
No vertex may be used more than once.
```

So if worker \(A\) is matched to task \(1\), worker \(A\) cannot also be matched to task \(2\), and task \(1\) cannot also be matched to worker \(B\).

A **complete matching** from \(U\) to \(W\) matches every vertex in \(U\). In worker-task language, every worker in the required set gets one task, and no two workers get the same task.

Hall’s marriage theorem is the great bouncer at the door. It checks whether a complete matching is possible before we waste time trying to construct one.

For every subset \(S\) of \(U\), look at all vertices in \(W\) connected to at least one vertex in \(S\). This set is called the neighbourhood of \(S\), written:

\[
N(S).
\]

Hall’s condition is:

\[
|N(S)|\ge |S|
\]

for every subset \(S\subseteq U\).

This says:

```text
Every group of k vertices in U must collectively have access to at least k possible partners in W.
```

If three workers can collectively only do two tasks, then no complete matching can exist. The graph has a bottleneck, a tiny doorway trying to swallow a parade.

---

## 7. Key Definitions and Notation

### Graph

A **graph** is a set of vertices joined by edges.

We usually write:

\[
G=(V,E)
\]

where:

- \(V\) is the set of vertices;
- \(E\) is the set of edges.

Because this lesson uses two vertex sets, we will avoid using \(V\) for both “all vertices” and “right-hand vertex set” when possible. We will usually write the two parts as:

\[
U \quad \text{and} \quad W.
\]

### Bipartite Graph

A **bipartite graph** is a graph whose vertices can be split into two disjoint sets, say \(U\) and \(W\), so that every edge joins a vertex in \(U\) to a vertex in \(W\).

This means:

\[
U\cap W=\varnothing.
\]

There are no edges joining two vertices both in \(U\), and no edges joining two vertices both in \(W\).

### Edge Notation

If \(u\in U\) and \(w\in W\), the edge joining them may be written:

\[
uw
\]

or

\[
(u,w).
\]

In a worker-task interpretation, \((A,2)\) means:

```text
Worker A can be paired with task 2.
```

### Matching

A **matching** is a set of edges in which no two edges share a vertex.

For example, suppose:

\[
U=\{A,B,C\},\qquad W=\{1,2,3\}.
\]

The edge set

\[
M=\{(A,1),(B,3)\}
\]

is a matching if both edges exist in the graph, because:

- \(A\) is used once;
- \(B\) is used once;
- task \(1\) is used once;
- task \(3\) is used once.

The edge set

\[
\{(A,1),(A,2)\}
\]

is **not** a matching, because vertex \(A\) is used twice.

The edge set

\[
\{(A,1),(B,1)\}
\]

is **not** a matching, because vertex \(1\) is used twice.

### Complete Matching

A **complete matching from \(U\) to \(W\)** is a matching in which every vertex in \(U\) is matched to a distinct vertex in \(W\).

If:

\[
|U|=|W|
\]

then a complete matching from \(U\) to \(W\) matches every vertex in both sets. Some textbooks call this a **perfect matching**, but the CCEA wording supplied for this lesson is “complete matching”, so we will use that language.

### Neighbourhood of a Set

Let \(S\subseteq U\).

The **neighbourhood** of \(S\), written \(N(S)\), is the set of vertices in \(W\) that are adjacent to at least one vertex in \(S\).

In symbols:

\[
N(S)=\{w\in W:\text{ there is an edge from some }s\in S\text{ to }w\}.
\]

### Hall’s Marriage Theorem

For a bipartite graph with parts \(U\) and \(W\), there is a complete matching from \(U\) to \(W\) if and only if:

\[
|N(S)|\ge |S|
\]

for every subset:

\[
S\subseteq U.
\]

This is Hall’s condition.

### Important Notation Warning

The symbol:

\[
|S|
\]

means “the number of elements in \(S\)”.

It does **not** mean absolute value in this graph theory context.

So if:

\[
S=\{A,B,C\},
\]

then:

\[
|S|=3.
\]

---

## 8. Core Theory

### 8.1 From a Table to a Bipartite Graph

Suppose three workers \(A,B,C\) can do some of three tasks \(1,2,3\). The information might be given in a table.

| Worker | Task 1 | Task 2 | Task 3 |
|---|---:|---:|---:|
| \(A\) | yes | yes | no |
| \(B\) | yes | no | no |
| \(C\) | no | yes | yes |

This is not a weighted cost matrix. It does not tell us times or costs. It only tells us whether an edge exists.

We form two vertex sets:

\[
U=\{A,B,C\}
\]

and

\[
W=\{1,2,3\}.
\]

Now convert each “yes” into an edge:

- \(A\) can do task \(1\), so include \((A,1)\).
- \(A\) can do task \(2\), so include \((A,2)\).
- \(B\) can do task \(1\), so include \((B,1)\).
- \(C\) can do task \(2\), so include \((C,2)\).
- \(C\) can do task \(3\), so include \((C,3)\).

So the edge set is:

\[
E=\{(A,1),(A,2),(B,1),(C,2),(C,3)\}.
\]

**Bridge Note:** In ordinary A-Level Maths, a table usually gives values to calculate with. Here, Further Maths changes the table into structure: the entries tell us which edges exist.

### 8.2 Checking Whether a Set of Edges Is a Matching

Using the graph above:

\[
E=\{(A,1),(A,2),(B,1),(C,2),(C,3)\}.
\]

Consider:

\[
M_1=\{(A,2),(B,1),(C,3)\}.
\]

Check the left-hand vertices:

\[
A,\ B,\ C.
\]

Each appears exactly once.

Check the right-hand vertices:

\[
2,\ 1,\ 3.
\]

Each appears exactly once.

Therefore:

\[
M_1=\{(A,2),(B,1),(C,3)\}
\]

is a matching.

Since every vertex in \(U=\{A,B,C\}\) is matched, it is also a complete matching from \(U\) to \(W\).

Now consider:

\[
M_2=\{(A,1),(B,1),(C,3)\}.
\]

The right-hand vertex \(1\) appears in two edges:

\[
(A,1)\quad\text{and}\quad(B,1).
\]

So task \(1\) is used twice.

Therefore:

\[
M_2
\]

is **not** a matching.

**Bridge Note:** In ordinary A-Level Maths, repeated values in a table might not be a problem. In a matching, repeated vertices are fatal. One vertex twice means the matching breaks.

### 8.3 What Complete Matching Really Means

A complete matching from \(U\) to \(W\) does not simply mean “there are enough edges overall”.

It means:

```text
Every vertex in U gets exactly one partner in W, and no vertex in W is used more than once.
```

For example:

\[
U=\{A,B,C\},\qquad W=\{1,2,3\}.
\]

If:

\[
M=\{(A,2),(B,1),(C,3)\},
\]

then every element of \(U\) is matched:

\[
A\mapsto 2,\qquad B\mapsto 1,\qquad C\mapsto 3.
\]

So \(M\) is complete from \(U\) to \(W\).

But:

\[
M=\{(A,2),(B,1)\}
\]

is not complete from \(U\) to \(W\), because \(C\) is unmatched.

Even though this is a valid matching, it is not a complete matching.

**Bridge Note:** In ordinary A-Level Maths, a partial answer might still earn method marks. In graph matching, “matching” and “complete matching” are different targets. The word complete is doing heavy lifting.

### 8.4 Why Hall’s Theorem Is Needed

Sometimes a complete matching is easy to see by inspection.

But sometimes a graph becomes too tangled to test by guesswork. Hall’s theorem gives a precise condition.

Let the two vertex sets be:

\[
U=\{A,B,C\}
\]

and

\[
W=\{1,2,3\}.
\]

Suppose the edges are:

\[
E=\{(A,1),(A,2),(B,1),(C,2),(C,3)\}.
\]

To use Hall’s theorem, we must check subsets \(S\subseteq U\).

The subsets of \(U\) are:

\[
\varnothing,\{A\},\{B\},\{C\},\{A,B\},\{A,C\},\{B,C\},\{A,B,C\}.
\]

Usually the empty set is harmless because:

\[
N(\varnothing)=\varnothing
\]

and:

\[
|N(\varnothing)|=0=|\varnothing|.
\]

For \(S=\{A\}\),

\[
N(\{A\})=\{1,2\},\qquad |N(S)|=2\ge 1=|S|.
\]

For \(S=\{B\}\),

\[
N(\{B\})=\{1\},\qquad |N(S)|=1\ge 1=|S|.
\]

For \(S=\{C\}\),

\[
N(\{C\})=\{2,3\},\qquad |N(S)|=2\ge 1=|S|.
\]

For \(S=\{A,B\}\),

\[
N(\{A,B\})=\{1,2\},\qquad |N(S)|=2\ge 2=|S|.
\]

For \(S=\{A,C\}\),

\[
N(\{A,C\})=\{1,2,3\},\qquad |N(S)|=3\ge 2=|S|.
\]

For \(S=\{B,C\}\),

\[
N(\{B,C\})=\{1,2,3\},\qquad |N(S)|=3\ge 2=|S|.
\]

For \(S=\{A,B,C\}\),

\[
N(S)=\{1,2,3\},\qquad |N(S)|=3\ge 3=|S|.
\]

Since:

\[
|N(S)|\ge |S|
\]

for every subset \(S\subseteq U\), Hall’s theorem tells us that a complete matching from \(U\) to \(W\) exists.

One such complete matching is:

\[
\{(A,2),(B,1),(C,3)\}.
\]

**Bridge Note:** In ordinary A-Level Maths, proof often means showing a statement follows from algebra. Here, the proof is combinatorial: every possible group of left-hand vertices must have enough available right-hand neighbours.

### 8.5 How Hall’s Theorem Detects Failure

Let:

\[
U=\{A,B,C\},\qquad W=\{1,2,3\}.
\]

Suppose the edge set is:

\[
E=\{(A,1),(B,1),(C,2),(C,3)\}.
\]

Take the subset:

\[
S=\{A,B\}.
\]

The neighbours of \(A\) are:

\[
\{1\}.
\]

The neighbours of \(B\) are:

\[
\{1\}.
\]

So the combined neighbourhood is still only:

\[
N(\{A,B\})=\{1\}.
\]

Now count:

\[
|S|=2
\]

but:

\[
|N(S)|=1.
\]

So:

\[
|N(S)|<|S|
\]

because:

\[
1<2.
\]

Hall’s condition fails.

Therefore, by Hall’s theorem, there is no complete matching from \(U\) to \(W\).

The interpretation is simple:

```text
A and B are two vertices fighting over only one possible partner.
```

No matter what happens with \(C\), both \(A\) and \(B\) cannot be matched distinctly.

**Bridge Note:** In ordinary A-Level Maths, a counterexample can disprove a claim. Here, one subset \(S\) with \(|N(S)|<|S|\) disproves the existence of a complete matching.

### 8.6 The Difference Between CCEA Matching and the Uploaded D2 Allocation Evidence

The uploaded D2 transcript describes a weighted allocation chapter. It uses a cost matrix where each entry is a time or cost, and it teaches the Hungarian algorithm to minimise or maximise a total. That transcript explicitly describes one worker doing one task and an \(n\times n\) cost matrix.

In CCEA FA22 Graph theory, the supplied official LO wording does not ask for the Hungarian algorithm. It asks for bipartite graphs, matchings, complete matchings and Hall’s marriage theorem.

| CCEA FA22 matching | Uploaded D2 weighted allocation |
|---|---|
| Edge means “this pairing is allowed”. | Matrix entry gives a time, cost or profit. |
| Main question: does a complete matching exist? | Main question: which complete allocation minimises or maximises a total? |
| Core theorem: Hall’s marriage theorem. | Core method: Hungarian algorithm. |
| CCEA core in this lesson. | Optional enrichment only. |

This is a small-looking difference with exam-sized teeth. A CCEA Hall’s theorem question does not need row reduction, column reduction or augmenting by \(e\). A D2 Hungarian algorithm question does, but that is not the CCEA core lesson here.

---

## 9. Visual Asset Integration

The visuals below are placeholders only. They point to the split asset files generated for later phases.

[VISUAL PLACEHOLDER: FA22GraphTheoryBipartiteMatchingsMermaid-001 | Source: CCEA FA22-GRAPH-LO003 and FA22-GRAPH-LO004 | Insert from mermaid/FA22GraphTheoryBipartiteMatchingsMermaid-001.md | Purpose: Show the logical flow from bipartite graph to matching to complete matching to Hall’s marriage theorem.]

[VISUAL PLACEHOLDER: FA22GraphTheoryBipartiteMatchingsSVG-001 | Source: CCEA FA22-GRAPH-LO003 | Insert from svg/FA22GraphTheoryBipartiteMatchingsSVG-001.svg | Purpose: Show a bipartite graph with workers on the left, tasks on the right, allowed edges, and one highlighted complete matching.]

[VISUAL PLACEHOLDER: FA22GraphTheoryBipartiteMatchingsSVG-002 | Source: CCEA FA22-GRAPH-LO004 | Insert from svg/FA22GraphTheoryBipartiteMatchingsSVG-002.svg | Purpose: Visualise a subset S, its neighbourhood N(S), and the inequality |N(S)| ≥ |S|.]

[VISUAL PLACEHOLDER: FA22GraphTheoryBipartiteMatchingsBridgeSVG-001 | Source: Ordinary A-Level Maths bridge + Further Maths specification | Insert from svg/FA22GraphTheoryBipartiteMatchingsBridgeSVG-001.svg | Purpose: Compare prior ordinary Maths table-reading with the Further Maths graph representation.]

[VISUAL PLACEHOLDER: FA22GraphTheoryBipartiteMatchingsTikZ-001 | Source: CCEA FA22-GRAPH-LO003 | Insert from tikz/FA22GraphTheoryBipartiteMatchingsTikZ-001.tex | Purpose: Provide a precise mathematical diagram of a bipartite graph and complete matching for printable notes.]

[VISUAL PLACEHOLDER: FA22GraphTheoryBipartiteMatchingsTikZ-002 | Source: CCEA FA22-GRAPH-LO004 | Insert from tikz/FA22GraphTheoryBipartiteMatchingsTikZ-002.tex | Purpose: Provide a precise subset-neighbourhood diagram for Hall’s marriage theorem.]

---

## 10. Interactive Learning Widgets

[INTERACTIVE PLACEHOLDER: FA22GraphTheoryBipartiteMatchingsWidget-001 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FA22GraphTheoryBipartiteMatchingsWidget-001.html | Purpose: Let the student choose edges in a bipartite graph and test whether the chosen edges form a matching or complete matching.]

This widget lets the student choose allowed edges, select a proposed matching, and receive feedback on repeated vertices, missing vertices and complete matching status.

[INTERACTIVE PLACEHOLDER: FA22GraphTheoryBipartiteMatchingsWidget-002 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FA22GraphTheoryBipartiteMatchingsWidget-002.html | Purpose: Let the student select a subset S and calculate N(S), |S| and |N(S)| dynamically.]

This widget lets the student select a subset \(S\subseteq U\), displays \(N(S)\), and checks whether \(|N(S)|\ge |S|\).

---
## 11. Worked Examples

The worked examples below are generated to match the CCEA FA22 Graph theory boundary. They are not past-paper questions and are not textbook questions.

### Worked Example 1: Identify a Matching

#### Question

Let:

\[
U=\{A,B,C,D\}
\]

and:

\[
W=\{1,2,3,4\}.
\]

Suppose a bipartite graph has edge set:

\[
E=\{(A,1),(A,3),(B,2),(C,2),(C,4),(D,3)\}.
\]

Decide whether each of the following is a matching.

\[
M_1=\{(A,1),(B,2),(C,4)\}
\]

\[
M_2=\{(A,3),(D,3)\}
\]

\[
M_3=\{(A,1),(B,2),(C,4),(D,3)\}
\]

#### Solution

A matching is a set of edges in which no two edges share a vertex.

For:

\[
M_1=\{(A,1),(B,2),(C,4)\},
\]

the left-hand vertices are:

\[
A,\ B,\ C,
\]

with no repeat, and the right-hand vertices are:

\[
1,\ 2,\ 4,
\]

with no repeat. Every edge in \(M_1\) is in \(E\), so \(M_1\) is a matching. It is not complete from \(U\) to \(W\), because \(D\in U\) is unmatched.

For:

\[
M_2=\{(A,3),(D,3)\},
\]

the right-hand vertex \(3\) is repeated. Therefore \(M_2\) is not a matching.

For:

\[
M_3=\{(A,1),(B,2),(C,4),(D,3)\},
\]

the left-hand vertices are:

\[
A,\ B,\ C,\ D,
\]

with no repeat, and the right-hand vertices are:

\[
1,\ 2,\ 4,\ 3,
\]

with no repeat. Every edge in \(M_3\) is in \(E\). Therefore \(M_3\) is a matching. Since every vertex in \(U\) is matched, it is a complete matching from \(U\) to \(W\).

#### Final exam-style answer

\[
M_1 \text{ is a matching, but not complete.}
\]

\[
M_2 \text{ is not a matching, since vertex }3\text{ is used twice.}
\]

\[
M_3 \text{ is a complete matching from }U\text{ to }W.
\]

#### Teaching note

Do not just count the number of edges. A set of four edges is not automatically a complete matching. You must check repeated vertices.

---

### Worked Example 2: Use Hall’s Theorem to Prove a Complete Matching Exists

#### Question

Let:

\[
U=\{A,B,C\}
\]

and:

\[
W=\{1,2,3\}.
\]

The edge set of a bipartite graph is:

\[
E=\{(A,1),(A,2),(B,1),(B,3),(C,2),(C,3)\}.
\]

Use Hall’s marriage theorem to show that a complete matching from \(U\) to \(W\) exists.

#### Solution

Hall’s marriage theorem says that a complete matching from \(U\) to \(W\) exists if and only if:

\[
|N(S)|\ge |S|
\]

for every subset:

\[
S\subseteq U.
\]

Here:

\[
U=\{A,B,C\}.
\]

The non-empty subsets of \(U\) are:

\[
\{A\},\{B\},\{C\},\{A,B\},\{A,C\},\{B,C\},\{A,B,C\}.
\]

For:

\[
S=\{A\},
\]

the edges from \(A\) are:

\[
(A,1),(A,2),
\]

so:

\[
N(\{A\})=\{1,2\}.
\]

Therefore:

\[
|N(\{A\})|=2\ge 1=|\{A\}|.
\]

For:

\[
S=\{B\},
\]

the edges from \(B\) are:

\[
(B,1),(B,3),
\]

so:

\[
N(\{B\})=\{1,3\}.
\]

Therefore:

\[
|N(\{B\})|=2\ge 1=|\{B\}|.
\]

For:

\[
S=\{C\},
\]

the edges from \(C\) are:

\[
(C,2),(C,3),
\]

so:

\[
N(\{C\})=\{2,3\}.
\]

Therefore:

\[
|N(\{C\})|=2\ge 1=|\{C\}|.
\]

For:

\[
S=\{A,B\},
\]

we combine the neighbours of \(A\) and \(B\):

\[
N(\{A,B\})=\{1,2,3\}.
\]

Therefore:

\[
|N(\{A,B\})|=3\ge 2=|\{A,B\}|.
\]

For:

\[
S=\{A,C\},
\]

we combine the neighbours of \(A\) and \(C\):

\[
N(\{A,C\})=\{1,2,3\}.
\]

Therefore:

\[
|N(\{A,C\})|=3\ge 2=|\{A,C\}|.
\]

For:

\[
S=\{B,C\},
\]

we combine the neighbours of \(B\) and \(C\):

\[
N(\{B,C\})=\{1,2,3\}.
\]

Therefore:

\[
|N(\{B,C\})|=3\ge 2=|\{B,C\}|.
\]

For:

\[
S=\{A,B,C\},
\]

all three right-hand vertices are adjacent to at least one vertex in \(S\). Therefore:

\[
N(\{A,B,C\})=\{1,2,3\}.
\]

So:

\[
|N(\{A,B,C\})|=3=|\{A,B,C\}|.
\]

Since:

\[
|N(S)|\ge |S|
\]

for every subset \(S\subseteq U\), Hall’s theorem tells us that a complete matching exists.

One complete matching is:

\[
\{(A,2),(B,1),(C,3)\}.
\]

Check:

\[
A\to 2,\qquad B\to 1,\qquad C\to 3.
\]

No vertex is used twice.

#### Final exam-style answer

For every subset \(S\subseteq U\), the neighbourhood \(N(S)\) satisfies:

\[
|N(S)|\ge |S|.
\]

Therefore, by Hall’s marriage theorem, a complete matching from \(U\) to \(W\) exists.

For example:

\[
\{(A,2),(B,1),(C,3)\}
\]

is a complete matching.

---

### Worked Example 3: Use Hall’s Theorem to Prove No Complete Matching Exists

#### Question

Let:

\[
U=\{A,B,C,D\}
\]

and:

\[
W=\{1,2,3,4\}.
\]

Suppose the edges are:

\[
E=\{(A,1),(B,1),(C,2),(C,3),(D,3),(D,4)\}.
\]

Use Hall’s marriage theorem to prove that no complete matching from \(U\) to \(W\) exists.

#### Solution

Hall’s marriage theorem says that a complete matching from \(U\) to \(W\) exists if and only if:

\[
|N(S)|\ge |S|
\]

for every subset:

\[
S\subseteq U.
\]

To prove that no complete matching exists, it is enough to find one subset \(S\) for which:

\[
|N(S)|<|S|.
\]

Consider:

\[
S=\{A,B\}.
\]

The edges involving \(A\) and \(B\) are:

\[
(A,1)
\]

and:

\[
(B,1).
\]

So both \(A\) and \(B\) are only adjacent to vertex \(1\).

Therefore:

\[
N(\{A,B\})=\{1\}.
\]

Now count:

\[
|\{A,B\}|=2
\]

and:

\[
|N(\{A,B\})|=|\{1\}|=1.
\]

So:

\[
|N(\{A,B\})|=1<2=|\{A,B\}|.
\]

Therefore Hall’s condition fails.

Hence there is no complete matching from \(U\) to \(W\).

#### Final exam-style answer

Take:

\[
S=\{A,B\}.
\]

Then:

\[
N(S)=\{1\}.
\]

So:

\[
|N(S)|=1<2=|S|.
\]

Hall’s condition fails, so no complete matching exists.

---

### Worked Example 4: Construct a Complete Matching by Reasoning

#### Question

A bipartite graph has:

\[
U=\{A,B,C,D\}
\]

and:

\[
W=\{1,2,3,4\}.
\]

The edge set is:

\[
E=\{(A,1),(A,2),(B,2),(C,2),(C,3),(D,3),(D,4)\}.
\]

Find a complete matching from \(U\) to \(W\), or explain why none exists.

#### Solution

We need to match every vertex in \(U\):

\[
A,\ B,\ C,\ D.
\]

Vertex \(B\) is adjacent only to \(2\), since the only edge involving \(B\) is:

\[
(B,2).
\]

So if a complete matching exists, we must use:

\[
(B,2).
\]

Now vertex \(2\) is used, so no other chosen edge may use vertex \(2\).

The available edges left are:

\[
(A,1),\quad (C,3),\quad (D,3),\quad (D,4).
\]

Notice that \(A\) now cannot use \((A,2)\), because \(2\) is already used by \(B\). So \(A\) must use:

\[
(A,1).
\]

Now \(1\) and \(2\) are used.

For \(C\), the available edge is:

\[
(C,3).
\]

So choose:

\[
(C,3).
\]

Now \(3\) is used.

For \(D\), the edge \((D,3)\) is no longer available because \(3\) is used by \(C\), so choose:

\[
(D,4).
\]

Therefore a complete matching is:

\[
M=\{(A,1),(B,2),(C,3),(D,4)\}.
\]

Check that every vertex in \(U\) is used once:

\[
A,\ B,\ C,\ D.
\]

Check that every selected vertex in \(W\) is used once:

\[
1,\ 2,\ 3,\ 4.
\]

No repeats occur.

Therefore:

\[
M=\{(A,1),(B,2),(C,3),(D,4)\}
\]

is a complete matching.

---

## 12. Common Mistakes and Exam Traps

### 12.1 Confusing Weighted Allocation with Bipartite Matching

The uploaded transcript uses a cost matrix, row reduction, column reduction and matrix augmentation to solve weighted allocation problems. It says the goal is to allocate workers to tasks efficiently by time or cost, using an \(n\times n\) cost matrix and the Hungarian algorithm.

That is **not** the CCEA core method for this lesson.

For this lesson:

- Edges mean “allowed”.
- The question is about whether a matching exists.
- Hall’s theorem checks complete matching existence.
- There is no minimising total cost unless the question explicitly introduces such a method.

### 12.2 Treating Every Edge Set as a Matching

A set of edges is not automatically a matching.

You must check:

```text
No two selected edges share a vertex.
```

For example:

\[
\{(A,1),(B,1)\}
\]

is not a matching because vertex \(1\) is used twice.

### 12.3 Forgetting What “Complete” Refers To

A complete matching from \(U\) to \(W\) means every vertex in \(U\) is matched.

It does not always mean every vertex in \(W\) is matched, unless:

\[
|U|=|W|.
\]

### 12.4 Checking Hall’s Theorem on Only Singletons

Checking only:

\[
\{A\},\{B\},\{C\}
\]

is not enough.

Hall’s theorem says every subset:

\[
S\subseteq U
\]

must satisfy:

\[
|N(S)|\ge |S|.
\]

The failure may happen in a larger subset such as:

\[
S=\{A,B\}.
\]

### 12.5 Misreading \(N(S)\)

The set \(N(S)\) is the set of all neighbours of at least one vertex in \(S\).

It is not:

- the number of edges from \(S\);
- the set \(S\) itself;
- the set of unmatched vertices;
- the set of all vertices in the graph.

If:

\[
S=\{A,B\}
\]

and:

\[
A\to 1,2,\qquad B\to 2,3,
\]

then:

\[
N(S)=\{1,2,3\}.
\]

Notice that \(2\) is written once, not twice.

### 12.6 Counting Edges Instead of Counting Neighbours

Hall’s theorem compares:

\[
|N(S)|
\]

with:

\[
|S|.
\]

It does not compare the number of edges leaving \(S\) with \(|S|\).

Example:

\[
A\to 1,\qquad B\to 1.
\]

There are two edges from \(S=\{A,B\}\), but:

\[
N(S)=\{1\}.
\]

So:

\[
|N(S)|=1.
\]

### 12.7 Direction of Complete Matching

A complete matching from \(U\) to \(W\) checks all vertices in \(U\).

If the question asks for a complete matching from \(W\) to \(U\), then the subsets in Hall’s theorem must be taken from \(W\), not \(U\).

Read the direction. Tiny wording, giant hinge.

### 12.8 Old Table Habits Becoming Risky

In ordinary A-Level Maths, tables often invite arithmetic.

In this lesson, a table may encode edges. So:

- “yes” means an edge exists;
- blank or “no” means no edge exists;
- numbers are not automatically costs;
- a cost matrix belongs to a different, off-spec weighted allocation method unless CCEA explicitly asks.

---

## 13. Practice Questions

The following questions are AI-generated, on-spec practice questions. They are not past-paper or textbook questions.

### Practice Question 1: Matching or Not?

Let:

\[
U=\{A,B,C\}
\]

and:

\[
W=\{1,2,3\}.
\]

The edge set is:

\[
E=\{(A,1),(A,2),(B,2),(C,2),(C,3)\}.
\]

Decide whether each set is a matching.

(a)
\[
M_1=\{(A,1),(B,2)\}
\]

(b)
\[
M_2=\{(A,2),(B,2)\}
\]

(c)
\[
M_3=\{(A,1),(B,2),(C,3)\}
\]

### Practice Question 2: Find a Complete Matching

Let:

\[
U=\{P,Q,R,S\}
\]

and:

\[
W=\{a,b,c,d\}.
\]

The edge set is:

\[
E=\{(P,a),(P,b),(Q,b),(R,c),(R,d),(S,d)\}.
\]

Find a complete matching from \(U\) to \(W\), or explain why none exists.

### Practice Question 3: Hall’s Theorem, Successful Case

Let:

\[
U=\{A,B,C\}
\]

and:

\[
W=\{x,y,z\}.
\]

The edge set is:

\[
E=\{(A,x),(A,y),(B,x),(B,z),(C,y),(C,z)\}.
\]

Use Hall’s theorem to show that a complete matching exists.

### Practice Question 4: Hall’s Theorem, Failure Case

Let:

\[
U=\{A,B,C,D\}
\]

and:

\[
W=\{1,2,3,4\}.
\]

The edge set is:

\[
E=\{(A,1),(B,1),(C,2),(C,3),(D,3),(D,4)\}.
\]

Use Hall’s theorem to prove that no complete matching from \(U\) to \(W\) exists.

### Practice Question 5: Table to Bipartite Graph

The table shows which workers can do which jobs.

| Worker | Job 1 | Job 2 | Job 3 | Job 4 |
|---|---:|---:|---:|---:|
| \(A\) | yes | no | yes | no |
| \(B\) | yes | yes | no | no |
| \(C\) | no | yes | no | yes |
| \(D\) | no | no | yes | yes |

(a) Write down the two vertex sets \(U\) and \(W\).  
(b) Write down the edge set \(E\).  
(c) Find a complete matching from \(U\) to \(W\).

---

## 14. Worked Solutions

### Solution to Practice Question 1

We have:

\[
U=\{A,B,C\},\qquad W=\{1,2,3\}
\]

and:

\[
E=\{(A,1),(A,2),(B,2),(C,2),(C,3)\}.
\]

For (a):

\[
M_1=\{(A,1),(B,2)\}.
\]

Both edges exist, and no vertex is repeated, so \(M_1\) is a matching.

For (b):

\[
M_2=\{(A,2),(B,2)\}.
\]

Both edges use vertex \(2\in W\), so \(M_2\) is not a matching.

For (c):

\[
M_3=\{(A,1),(B,2),(C,3)\}.
\]

Every edge exists, and no vertex is repeated. Every vertex in \(U\) is matched, so \(M_3\) is a complete matching from \(U\) to \(W\).

### Solution to Practice Question 2

We have:

\[
U=\{P,Q,R,S\},\qquad W=\{a,b,c,d\}
\]

and:

\[
E=\{(P,a),(P,b),(Q,b),(R,c),(R,d),(S,d)\}.
\]

Vertex \(Q\) is adjacent only to \(b\), so any complete matching must include:

\[
(Q,b).
\]

Vertex \(S\) is adjacent only to \(d\), so any complete matching must include:

\[
(S,d).
\]

Now \(b\) and \(d\) are used.

Vertex \(R\) is adjacent to \(c,d\), but \(d\) is already used by \(S\), so \(R\) must use:

\[
(R,c).
\]

Vertex \(P\) is adjacent to \(a,b\), but \(b\) is already used by \(Q\), so \(P\) must use:

\[
(P,a).
\]

Therefore a complete matching is:

\[
M=\{(P,a),(Q,b),(R,c),(S,d)\}.
\]

### Solution to Practice Question 3

Hall’s theorem says a complete matching from \(U\) to \(W\) exists if and only if:

\[
|N(S)|\ge |S|
\]

for every subset \(S\subseteq U\).

Here:

\[
U=\{A,B,C\},\qquad W=\{x,y,z\}.
\]

The non-empty subsets of \(U\) are:

\[
\{A\},\{B\},\{C\},\{A,B\},\{A,C\},\{B,C\},\{A,B,C\}.
\]

For the singletons:

\[
N(\{A\})=\{x,y\},\qquad |N(\{A\})|=2\ge 1=|\{A\}|.
\]

\[
N(\{B\})=\{x,z\},\qquad |N(\{B\})|=2\ge 1=|\{B\}|.
\]

\[
N(\{C\})=\{y,z\},\qquad |N(\{C\})|=2\ge 1=|\{C\}|.
\]

For the pairs:

\[
N(\{A,B\})=\{x,y,z\},\qquad |N(\{A,B\})|=3\ge 2=|\{A,B\}|.
\]

\[
N(\{A,C\})=\{x,y,z\},\qquad |N(\{A,C\})|=3\ge 2=|\{A,C\}|.
\]

\[
N(\{B,C\})=\{x,y,z\},\qquad |N(\{B,C\})|=3\ge 2=|\{B,C\}|.
\]

For the whole set:

\[
N(\{A,B,C\})=\{x,y,z\},\qquad |N(\{A,B,C\})|=3=|\{A,B,C\}|.
\]

Since Hall’s condition holds for every subset \(S\subseteq U\), a complete matching exists.

One complete matching is:

\[
\{(A,y),(B,x),(C,z)\}.
\]

### Solution to Practice Question 4

Let:

\[
S=\{A,B\}.
\]

The neighbours of \(A\) are:

\[
\{1\}.
\]

The neighbours of \(B\) are:

\[
\{1\}.
\]

Therefore:

\[
N(S)=N(\{A,B\})=\{1\}.
\]

Now:

\[
|S|=|\{A,B\}|=2
\]

and:

\[
|N(S)|=|\{1\}|=1.
\]

So:

\[
|N(S)|=1<2=|S|.
\]

Hall’s condition fails.

Therefore, by Hall’s marriage theorem, no complete matching from \(U\) to \(W\) exists.

### Solution to Practice Question 5

The worker set is:

\[
U=\{A,B,C,D\}.
\]

The job set is:

\[
W=\{1,2,3,4\}.
\]

Write an edge for each “yes”. From the table:

\[
E=\{(A,1),(A,3),(B,1),(B,2),(C,2),(C,4),(D,3),(D,4)\}.
\]

One possible complete matching is:

\[
M=\{(A,3),(B,1),(C,2),(D,4)\}.
\]

Check the left-hand vertices:

\[
A,\ B,\ C,\ D.
\]

Each appears once.

Check the right-hand vertices:

\[
3,\ 1,\ 2,\ 4.
\]

Each appears once.

Therefore \(M\) is a complete matching from \(U\) to \(W\).

---

## 15. Exam Technique Notes

### 15.1 Start by Naming the Two Sets

Always begin by identifying the two parts of the bipartite graph.

For example:

\[
U=\{A,B,C,D\},\qquad W=\{1,2,3,4\}.
\]

This prevents a lot of fog later.

### 15.2 State What an Edge Means

Write one clear sentence:

```text
The edge (A,2) means that A can be matched with 2.
```

For worker-task questions:

```text
The edge (A,2) means worker A can do task 2.
```

This matters because in the uploaded D2 allocation evidence, entries are times or costs rather than simple allowed/not allowed edges.

### 15.3 For a Matching, Check Repeated Vertices

A clean checking sentence:

```text
No vertex occurs in more than one selected edge, so this is a matching.
```

Or:

```text
Vertex 2 occurs in two selected edges, so this is not a matching.
```

### 15.4 For a Complete Matching, Say Which Side Is Complete

Use:

```text
Every vertex in U is matched exactly once, so this is a complete matching from U to W.
```

Do not merely say:

```text
It is complete.
```

That is too floaty. Pin the direction down.

### 15.5 For Hall’s Theorem, Define \(N(S)\)

Write:

\[
N(S)=\{\text{vertices in }W\text{ adjacent to at least one vertex in }S\}.
\]

Then show counts.

For a successful case:

\[
S=\{A,B\},\qquad N(S)=\{1,2,3\}.
\]

\[
|S|=2,\qquad |N(S)|=3.
\]

\[
3\ge 2.
\]

### 15.6 For Failure, One Subset Is Enough

A perfect disproof layout:

\[
S=\{A,B\}.
\]

\[
N(S)=\{1\}.
\]

\[
|N(S)|=1<2=|S|.
\]

Therefore Hall’s condition fails, so no complete matching exists.

### 15.7 Do Not Use the Hungarian Algorithm Unless Asked

The uploaded transcript gives detailed Hungarian algorithm steps: row reduction, column reduction, covering zeros, finding the smallest uncovered element \(e\), augmenting the matrix, and repeating until zeros can be covered in \(n\) lines.

Those steps are not part of this CCEA FA22 Graph theory matching lesson.

For this lesson, the exam-method compass points to:

- bipartite graph;
- matching;
- complete matching;
- Hall’s theorem;
- subset neighbourhoods.

### 15.8 Use Diagrams, But Do Not Let Them Replace Proof

A diagram is brilliant for seeing the matching.

But for Hall’s theorem, write the set notation.

A good answer is not just a drawing. It is a drawing plus:

\[
S=\{A,B\},\qquad N(S)=\{1\},\qquad |N(S)|<|S|.
\]

The symbols are the exam’s passport stamp.

---

## 16. Syllabus Gap Check

### 16.1 LO Coverage Table

| LO ID | Covered? | Evidence coverage | Lesson sections |
|---|---:|---|---|
| `FA22-GRAPH-LO003` | Yes | Definitions of bipartite graph, matching and complete matching; worked examples; practice questions; visual placeholders. | Sections 6, 7, 8, 9, 11, 12, 13, 14, 15 |
| `FA22-GRAPH-LO004` | Yes | Hall’s theorem definition, successful proof, failed condition proof, neighbourhood notation, practice questions and solutions. | Sections 7, 8, 9, 10, 11, 12, 13, 14, 15 |

### 16.2 Evidence Coverage Table

| Evidence item | Covered in core lesson? | Notes |
|---|---:|---|
| CCEA FA22 Graph theory matching LO | Yes | Main authority for this lesson. |
| CCEA Hall’s marriage theorem LO | Yes | Main theorem taught. |
| Uploaded D2 allocation transcript | No, not as core | Used for off-spec boundary logging only. The transcript teaches weighted cost matrices and the Hungarian algorithm. |
| Screenshot PDF for D2 allocation chapter | No, not as core | Used only to confirm visual chapter context and off-spec enrichment status. |
| Ordinary A-Level bridge evidence | Yes, bridge only | Used to explain prior skills: tables, sets, counting and proof. |

### 16.3 Bridge Coverage Table

| Bridge idea | Included? | Where |
|---|---:|---|
| Tables to structure | Yes | Sections 5, 6, 8, 9, 15 |
| Set notation | Yes | Sections 5, 7, 8, 11, 14 |
| Counting elements | Yes | Hall’s theorem sections |
| Proof and counterexample logic | Yes | Worked Examples 2 and 3 |
| Difference between adjacency and cost matrices | Yes | Sections 8, 12, 15, 16 |

### 16.4 Off-Spec Content Found but Excluded

| Off-spec or boundary-risk content | Source | Why excluded from core |
|---|---|---|
| Hungarian algorithm | Uploaded transcript and screenshot PDF | Not confirmed by supplied CCEA Further Mathematics specification map for `FA22-GRAPH-LO003` or `FA22-GRAPH-LO004`. |
| Row reduction and column reduction | Uploaded transcript | Hungarian algorithm procedure, not Hall’s theorem or bipartite matching. |
| Cover zeros with minimum horizontal and vertical lines | Uploaded transcript | Weighted assignment optimisation, not CCEA core matching existence. |
| Augment matrix by \(e\) | Uploaded transcript | Hungarian algorithm procedure. |
| Dummy row or dummy column | Uploaded transcript | Weighted allocation adjustment, not CCEA core matching. |
| Maximum profit conversion using largest value minus entry | Uploaded transcript | Weighted allocation optimisation, not CCEA core matching. |
| Incomplete data handled by large artificial costs | Uploaded transcript | Weighted allocation technique, not CCEA core matching. |
| 0-1 allocation linear programming with \(x_{ij}\) | Uploaded transcript | Related to allocation modelling, but not the same as CCEA FA22 Graph theory matchings. |

### 16.5 Optional Enrichment Not Required by CCEA

The following could become a separate enrichment lesson, but must not be labelled as required CCEA FA22 Graph theory content:

1. Weighted allocation problems.
2. Cost matrices.
3. Hungarian algorithm.
4. Dummy entries.
5. Maximum profit allocation.
6. Incomplete data by artificial large costs.
7. 0-1 allocation linear programming.

Suggested enrichment title:

```text
Optional Enrichment: Weighted Allocation Problems and the Hungarian Algorithm
```

Boundary label:

```text
This enrichment is conceptually related to matchings but is not required by the supplied CCEA FA22 Graph theory learning outcomes.
```

### 16.6 Weak Evidence Warnings

| Warning | Meaning |
|---|---|
| No CCEA-specific teacher transcript was supplied for bipartite matchings or Hall’s theorem. | Core examples were generated from the CCEA LO boundary, not transcribed from teacher notes. |
| The screenshot PDF is image-based and no parseable text was extracted. | Visual details from later PDF pages were not claimed unless visible in the supplied rendered snippets. |
| The lesson-specific transcript teaches D2 weighted allocation, not CCEA Hall’s theorem. | It was used only to prevent accidental off-spec import. |
| No official CCEA past-paper matching question was supplied. | Practice questions are generated and labelled as such. |

### 16.7 Missing Evidence Log

| Missing evidence | Impact | Resolution |
|---|---|---|
| CCEA classroom notes or transcript for `FA22-GRAPH-LO003` | No teacher-specific worked matching example can be preserved. | Generated examples are clearly labelled. |
| CCEA classroom notes or transcript for `FA22-GRAPH-LO004` | No teacher-specific Hall’s theorem wording can be preserved. | Formal theorem wording is provided using standard mathematical notation. |
| CCEA textbook extract for this exact topic | No textbook diagrams or examples can be transcribed. | AI-proposed visuals are marked as proposed. |
| Official CCEA past-paper question | No question is labelled as past-paper. | Generated exam-style questions are supplied. |

---

## 17. Recommended Enhancements Not in the Evidence

These are proposed enhancements, not evidence-backed content.

### Diagrams

1. A bipartite graph diagram with two clearly separated vertex sets.
2. A matching overlay where selected edges are highlighted.
3. A non-matching diagram showing a repeated vertex.
4. A Hall’s theorem bottleneck diagram where two left vertices share one neighbour.
5. A table-to-graph conversion visual.

### Animations

1. Animate selecting edges one by one and rejecting choices that reuse a vertex.
2. Animate \(S\) expanding and \(N(S)\) updating.
3. Animate a Hall failure when:
   \[
   |N(S)|<|S|.
   \]

### Widgets

1. Matching validator.
2. Complete matching checker.
3. Hall condition subset checker.
4. Table-to-edge-list converter.

### Extra Examples

1. A graph with more right-hand vertices than left-hand vertices.
2. A graph where a complete matching from \(U\) to \(W\) exists but not from \(W\) to \(U\).
3. A proof where checking only singleton subsets would be misleading.
4. A bridge example comparing:
   \[
   \text{cost matrix}
   \]
   with:
   \[
   \text{adjacency table}.
   \]

---

## 18. Supplementary Sources Used

### Project Sources Used

- `CCEA_GCE_Further_Mathematics_Specification_Map.md`
- `Further_Maths_README_module_map.md`
- `Further_Maths_EVIDENCE_DROP_CHECKLIST.md`
- `Ordinary_A_Level_Maths_Bridge_Spec_Extracts.md`
- `Further Maths Portal Build – Knowledge Evidence.txt`

### Lesson-Specific Evidence Used

- `transcripts.md`
- `Chapter_2_Allocation_Problems_⌨️_(Decision_2)_screenshots.pdf`

The transcript evidence confirms the supplied lesson-specific material teaches allocation problems using cost matrices, the Hungarian algorithm, dummy entries, maximum allocation, incomplete data and A2-only linear programming.

### Ordinary A-Level Maths Bridge Sources Used

Ordinary A-Level Mathematics sources were used only as bridge context. They do not override the Further Mathematics specification.

Bridge skills used:

- reading tables;
- using set notation;
- counting elements;
- interpreting mappings;
- writing proof statements;
- distinguishing numerical values from relationships.

### Cross-Board Sources Used

No external web or cross-board source was used.

The supplied D2 transcript appears to be a Decision 2 allocation resource, but because the supplied CCEA Further Mathematics specification boundary does not confirm the Hungarian algorithm as core for `FA22-GRAPH-LO003` or `FA22-GRAPH-LO004`, it has been treated as off-spec enrichment only.

### Evidence Limitations

1. The screenshot PDF was image-based and no full parseable text was available.
2. No CCEA-specific Hall’s theorem transcript was supplied.
3. No CCEA textbook extract was supplied for the exact core topic.
4. No official CCEA past-paper question was supplied.
5. All worked examples and practice questions in this lesson are generated and on-spec, not official past-paper material.

---

## 19. Final Student Checklist

### Prerequisite Confidence Checklist

- [ ] I can read a table and identify allowed relationships.
- [ ] I know that \(|S|\) means the number of elements in \(S\).
- [ ] I can list subsets of a small set such as \(\{A,B,C\}\).
- [ ] I can use set notation such as \(S=\{A,B\}\).
- [ ] I can compare two numbers using \(\ge\) and \(<\).

### Further Maths Method Checklist

- [ ] I can define a bipartite graph.
- [ ] I can identify the two vertex sets in a bipartite graph.
- [ ] I can explain why edges only go between the two sets.
- [ ] I can define a matching.
- [ ] I can decide whether a set of edges is a matching.
- [ ] I can define a complete matching.
- [ ] I can construct a complete matching where one exists.
- [ ] I can define \(N(S)\).
- [ ] I can calculate \(N(S)\) for a given subset \(S\).
- [ ] I can state Hall’s marriage theorem.
- [ ] I can use Hall’s theorem to prove a complete matching exists.
- [ ] I can use Hall’s theorem to prove a complete matching does not exist.

### Exam Technique Checklist

- [ ] I label the two parts of the bipartite graph clearly.
- [ ] I check that selected edges really exist.
- [ ] I check that no selected edge shares a vertex with another selected edge.
- [ ] I state whether the matching is complete from \(U\) to \(W\).
- [ ] I do not confuse number of edges with number of neighbours.
- [ ] I show the subset \(S\), the neighbourhood \(N(S)\), and both counts:
  \[
  |S|,\quad |N(S)|.
  \]
- [ ] For a Hall failure, I give one subset \(S\) where:
  \[
  |N(S)|<|S|.
  \]
- [ ] I avoid using the Hungarian algorithm in this CCEA matching lesson unless explicitly asked.

### Bridge Checklist

- [ ] I understand that a table of “yes/no” entries can represent edges.
- [ ] I understand that a table of times or costs is a different structure.
- [ ] I understand that CCEA matching questions focus on allowed pairings and existence.
- [ ] I understand that weighted allocation and the Hungarian algorithm are optional enrichment here, not core CCEA FA22 Graph theory.

### Diagram/Visual Understanding Checklist

- [ ] I can draw \(U\) on one side and \(W\) on the other.
- [ ] I can draw an edge only when the pairing is allowed.
- [ ] I can highlight a matching without using a vertex twice.
- [ ] I can shade a subset \(S\) and its neighbourhood \(N(S)\).
- [ ] I can explain a Hall bottleneck visually and symbolically.
