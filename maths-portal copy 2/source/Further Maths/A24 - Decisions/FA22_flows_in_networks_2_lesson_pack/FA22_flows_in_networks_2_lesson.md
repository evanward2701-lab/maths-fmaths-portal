# 1. Lesson Title and Metadata

```yaml
date_generated: 2026-06-04
course: CCEA GCE Further Mathematics
unit_code: FA22
unit_name: Further A2 2 Applied Mathematics
applied_section: Section D: Discrete and Decision Mathematics
topic_code: FA22-GRAPH
topic_name: Graph theory: Flows in Networks 2
topic_slug: flows_in_networks_2
topic_pascal: FlowsInNetworks2
topic_id: FA22FlowsInNetworks2
lesson_file: FA22_flows_in_networks_2_lesson.md
primary_LO_IDs:
  - FA22-GRAPH-LO002
supporting_prior_Further_Maths_LO_IDs:
  - FAS2-GRAPH-LO001
  - FAS2-GRAPH-LO004
bridge_tags:
  - Ordinary A-Level bridge
  - Set language
  - Proof language
  - Table organisation
  - Algebraic inequalities
  - Algorithmic reasoning
topic_tags:
  - FA22
  - GRAPH
  - Decision Mathematics
  - Graph theory
  - Cutsets
  - Max-flow min-cut theorem
  - Capacitated directed networks
  - Lower and upper capacities
  - Supersources and supersinks
  - Restricted capacity nodes
```

# Graph Theory: Flows in Networks 2

Lower capacities, residual arrows, cut values, supersources, supersinks and restricted nodes in directed capacitated networks.

A flow network is a model for moving something through a directed system. The thing being moved may be water, traffic, data, goods or people. The mathematical task is to respect every capacity condition and every node-balance condition, then prove maximality with a cut.

# 2. Evidence Map

| Source | Used in lesson | Evidence role |
|---|---|---|
| `CCEA_GCE_Further_Mathematics_Specification_Map.md` | Yes | Official authority for `FA22-GRAPH-LO002`: cutsets and max-flow min-cut theorem |
| `Further_Maths_README_module_map.md` | Yes | Metadata, unit-prefix rules, output naming and bridge requirements |
| `Further_Maths_EVIDENCE_DROP_CHECKLIST.md` | Yes | Missing evidence, visual evidence and off-spec logging rules |
| `Ordinary_A_Level_Maths_Bridge_Spec_Extracts.md` | Yes, bridge only | Confirms no direct ordinary A-Level predecessor for graph theory; supports bridge via proof, tables, set language and algorithmic reasoning |
| `transcripts.md` | Yes | Main lesson-specific mathematical content: lower/upper capacities, flow logic, augmentation, cuts, supersources, restricted nodes and exam-question commentary |
| `Chapter_4_Flows_in_Networks_2_⌨️_(Decision_2)_screenshots.pdf` | Yes | Visual evidence for diagrams, annotations and slide structure; PDF is image-only, so only inspected/visible details are claimed |
| Textbook exercise references `D2 Ex4A`, `D2 Ex4B`, `D2 Ex4C` | Indirectly | Used only as labels from transcript evidence; not treated as independent textbook evidence |
| Exam questions mentioned in transcript | Yes, with caution | Used for exam-awareness and method style. Original official papers were not supplied, so no question is labelled as official CCEA past-paper text |

# 3. Specification Alignment

| LO ID | Official wording | Lesson coverage | Evidence source | Syllabus boundary | Ordinary A-Level Maths bridge |
|---|---|---|---|---|---|
| `FA22-GRAPH-LO002` | demonstrate understanding of cutsets and use the max-flow min-cut theorem | Cutsets, cut values, feasible flows, maximum flow proof, saturated cuts, lower/upper capacity adaptations | CCEA specification map; transcript; screenshot PDF | Core lesson authority | No direct ordinary predecessor; use proof, inequalities, tables and modelling habits |
| `FAS2-GRAPH-LO001` | demonstrate understanding of and use the basic concepts of graph theory, including vertex, edge, degree, planarity and subgraph | Recap of vertices/nodes, arcs/edges and graph vocabulary | CCEA specification map | Prior Further Maths prerequisite, not current FA22 LO | Ordinary Maths has diagram-reading and logical condition habits, but not graph theory as a formal topic |
| `FAS2-GRAPH-LO004` | demonstrate understanding of and deal with weighted edges and digraphs | Recap of directed arcs and weighted/capacitated edges | CCEA specification map | Prior Further Maths prerequisite, not current FA22 LO | Ordinary Maths bridge through labelled diagrams, arrows and inequalities |

## Boundary statement

This lesson teaches **Flows in Networks 2** as a lesson-specific chapter inside the official FA22 graph theory area. The official CCEA boundary is `FA22-GRAPH-LO002`, so the core emphasis is:

```text
cutsets + max-flow min-cut theorem
```

Lower capacities, supersources, supersinks and restricted capacity nodes are included because the supplied lesson evidence presents them as A2 flow-network methods. They are taught as applications of cutsets, feasible flow and max-flow/min-cut reasoning, not as invented separate LO IDs.

# 4. Learning Objectives

## 4.1 Core Further Maths objectives

By the end of this lesson, you should be able to:

1. Interpret an arc label \((l,u)\) as a lower capacity \(l\) and upper capacity \(u\).
2. State and use the feasibility condition \(l_{uv}\le f_{uv}\le u_{uv}\).
3. Use flow conservation at a vertex: total flow into the vertex equals total flow out of the vertex.
4. Deduce forced arc flows from lower and upper capacities.
5. Adapt the usual maximum-flow labelling procedure when lower capacities are present.
6. Calculate forward residual capacity \(u_{uv}-f_{uv}\).
7. Calculate backward residual capacity \(f_{uv}-l_{uv}\).
8. Find an augmenting route and update a feasible flow.
9. Calculate cut values when lower capacities are present.
10. Use the max-flow min-cut theorem to prove that a feasible flow is maximal.
11. Add a supersource or supersink to handle multiple sources and/or multiple sinks.
12. Split a restricted-capacity node into an “in” node and an “out” node connected by a capacity arc.
13. Remove a blocked node and its incident arcs from a network when appropriate.
14. Interpret final answers in context, for example litres per second, traffic flow, or capacity through a router.

## 4.2 Bridge objectives

You should connect this lesson to ordinary A-Level Maths habits by treating capacities as inequalities, node balance as simultaneous equation logic, arithmetic as exact bookkeeping, proof language as essential for maximality, and diagrams as data rather than decoration.

## 4.3 Exam technique objectives

You should be able to spot whether a question is asking for a feasible flow, maximum flow, cut value or proof of maximality; use diagram annotations; avoid mixing lower and upper capacities; and state the max-flow min-cut theorem conclusion clearly.

# 5. Explicit Prerequisite Recap

## 5.1 GCSE foundations

You need addition, subtraction, directed-arrow reading, inequalities, simple equation solving, and checking totals.

## 5.2 Ordinary AS/A2 Mathematics foundations

There is no ordinary CCEA A-Level Mathematics topic called “flow networks”. The nearest skills are algebraic inequalities, exact arithmetic, diagram interpretation, table organisation, proof language and modelling language from applied mathematics.

## 5.3 Previous Further Mathematics foundations

This lesson assumes you already know vertex/node, edge/arc, directed graph/digraph, weighted edge, source, sink, path, cut/cutset, capacity and flow. It also assumes you have met the basic maximum-flow method from an earlier flow-network lesson, where capacities had only upper limits and backward residual capacity was simply the current flow because flow could be reduced to zero.

## 5.4 A-Level Maths Bridge: What You Already Know and What Further Maths Changes

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| AS1/A21 algebra | Inequalities, substitution, exact arithmetic and equation solving | A flow \(f_{uv}\) must satisfy \(l_{uv}\le f_{uv}\le u_{uv}\) | A flow that balances one node may violate an arc capacity elsewhere |
| Applied Maths modelling habits | Define variables, draw diagrams, use units and interpret answers | A network models pipes, roads, data routers or transport systems | A final number needs a modelling interpretation and a feasibility check |
| Statistics/table organisation | Read labelled diagrams and organise multiple pieces of information | Flow networks require careful bookkeeping of arcs, cuts and node totals | Missing one cut edge can produce a completely wrong proof |
| Proof language | Use definitions and theorem statements to justify claims | Maximality is justified by the max-flow min-cut theorem | “I found a big flow” is not automatically a maximum flow |
| No direct ordinary graph theory predecessor | Ordinary Maths does not formally teach cutsets or max-flow algorithms | Further Maths introduces discrete structures and algorithmic optimisation | Do not search for a calculus shortcut; the method is diagram logic |

In ordinary A-Level Maths, this idea appeared only indirectly through inequalities, tables, proof and applied modelling. In Further Maths, the same habits become a full discrete optimisation method on a directed network. The key upgrade is that a diagram is no longer decorative: it is the calculation. The danger is that one misread arrow, one missing lower capacity, or one unbalanced node can quietly sink the whole argument.

# 6. Big Picture Explanation

A basic flow problem asks how much can be pushed from a source to a sink. In earlier flow networks, arcs usually had only an upper capacity \(u\), so \(0\le f\le u\). In this lesson, arcs can have both a lower and an upper capacity \((l,u)\), so \(l\le f\le u\). The lower capacity is compulsory: the arc is not allowed to drop below a certain flow. The transcript gives the modelling example of pipes that must maintain water flow in cold weather to stop them freezing.

That one change affects the whole method:

- a backward residual arrow no longer shows how far the flow can fall to zero;
- it shows how far the flow can fall to its lower capacity;
- when calculating a cut value, an arc flowing backwards across the cut cannot be ignored;
- its compulsory lower flow acts like a drain back towards the source side.

This lesson also adds multiple sources and sinks, handled by adding a supersource or supersink; restricted capacity nodes, handled by splitting a node into an “in” and an “out” version; and blocked nodes, handled by deleting the node and its arcs from the network.

# 7. Key Definitions and Notation

## 7.1 Directed network

A **directed network** is a graph in which arcs have directions. If there is an arc from \(A\) to \(B\), write \(AB\) or \(A\to B\).

## 7.2 Vertex or node

A **vertex** or **node** is a point in the network, for example \(A,B,C,D,S,T\).

## 7.3 Arc

An **arc** is a directed connection between two nodes. For example, \(AB\) means the directed arc from \(A\) to \(B\).

## 7.4 Source and sink

A **source** is a node where flow enters the network. A **sink** is a node where flow leaves the network. Common notation uses \(S\) for source and \(T\) for sink.

## 7.5 Flow, lower capacity and upper capacity

For arc \(AB\), write the flow as \(f_{AB}\). The lower capacity is \(l_{AB}\), and the upper capacity is \(u_{AB}\).

The supplied lesson uses labels that look like coordinate pairs:

\[
(l,u).
\]

Here \(l\) is the lower capacity and \(u\) is the upper capacity. For example,

\[
(3,5)
\]

means

\[
3\le f\le 5.
\]

This is not a coordinate pair, even though it looks like one.

## 7.6 Feasible flow

A flow is **feasible** if every arc obeys \(l_{uv}\le f_{uv}\le u_{uv}\) and every intermediate node balances:

\[
\text{total flow in}=\text{total flow out}.
\]

## 7.7 Residual capacities

For an arc \(uv\) with current flow \(f_{uv}\), lower capacity \(l_{uv}\), and upper capacity \(u_{uv}\):

\[
\text{forward residual}=u_{uv}-f_{uv},
\]

\[
\text{backward residual}=f_{uv}-l_{uv}.
\]

This is the key technical change from upper-only flow networks.

## 7.8 Cut value with lower and upper capacities

For a cut:

\[
\text{cut value}
=
\sum(\text{upper capacities of arcs crossing from source side to sink side})
-
\sum(\text{lower capacities of arcs crossing from sink side to source side}).
\]

The second sum is subtracted because compulsory lower flow backwards acts like a drain against the source-to-sink flow.

## 7.9 Max-flow min-cut theorem

The **max-flow min-cut theorem** says:

\[
\text{maximum flow through the network}=\text{minimum cut value}.
\]

If you find a feasible flow of value \(V\) and a cut of value \(V\), then the feasible flow is a maximum flow.

# 8. Core Theory

## 8.1 The upgrade from upper-only capacities to lower-and-upper capacities

In earlier flow networks, an arc capacity \(7\) meant \(0\le f\le 7\). In this lesson, \((2,7)\) means \(2\le f\le 7\). The lower capacity is compulsory.

**Bridge Note:** In ordinary A-Level Maths, an inequality such as \(2\le x\le 7\) was a constraint on a number. Here, Further Maths turns that inequality into a physical or network condition \(2\le f_{uv}\le 7\), and all arcs must also fit together through flow conservation at nodes.

## 8.2 Feasible flow conditions

For every arc \(uv\):

\[
l_{uv}\le f_{uv}\le u_{uv}.
\]

For every intermediate node \(V\):

\[
\sum f_{\text{into }V}=\sum f_{\text{out of }V}.
\]

A flow can fail because an arc breaks its capacity condition or because a node does not balance.

## 8.3 Forced flow by considering one vertex

Consider node \(B\) with arcs

\[
AB:(3,5),\qquad BC:(3,4),\qquad BD:(2,7).
\]

The possible flow into \(B\) is \(3\le f_{AB}\le 5\), so the maximum possible inflow is \(5\). The minimum possible outflow is

\[
3+2=5.
\]

Flow conservation requires

\[
f_{AB}=f_{BC}+f_{BD}.
\]

The maximum possible inflow is exactly the minimum possible outflow:

\[
5=3+2.
\]

Therefore every value is forced:

\[
f_{AB}=5,
\]

\[
f_{BC}=3,
\]

\[
f_{BD}=2.
\]

So

\[
\boxed{AB=5,\quad BC=3,\quad BD=2.}
\]

If \(BC\) were bigger than \(3\), then more than \(5\) would need to leave \(B\). But \(AB\) can supply at most \(5\). The same is true if \(BD\) were bigger than \(2\), or if \(AB\) were less than \(5\).

## 8.4 Flow conservation method at a node

For any node \(V\):

1. List all incoming arcs.
2. List all outgoing arcs.
3. Write the allowed intervals for each arc.
4. Compare maximum possible inflow with minimum possible outflow, or minimum possible inflow with maximum possible outflow.
5. Deduce forced values where equality leaves no freedom.

This method is especially useful when a question says “By considering vertex \(C\)” or “Explain why arcs ... must be at their lower capacities.”

## 8.5 Vertex \(C\), then \(E\), then \(G\)

The transcript’s first full network example asks for flows in \(SC\), \(BC\) and \(CG\). The relevant capacities are:

\[
SC:(2,8),\qquad BC:(4,6),\qquad CG:(3,6).
\]

At \(C\), \(SC\) and \(BC\) flow in, while \(CG\) flows out. Minimum inflow is

\[
2+4=6.
\]

Maximum outflow along \(CG\) is

\[
6.
\]

So

\[
f_{SC}=2,\qquad f_{BC}=4,\qquad f_{CG}=6.
\]

Next, the arcs into \(E\) are

\[
DE:(4,8),\qquad AE:(4,6),\qquad BE:(3,5),
\]

and the arc out is

\[
ET:(7,11).
\]

The maximum outflow through \(ET\) is \(11\). The minimum inflow is

\[
4+4+3=11.
\]

So

\[
DE=4,
\]

\[
AE=4,
\]

\[
BE=3,
\]

and

\[
ET=11.
\]

Finally, since \(CG=6\) and \(BG:(5,9)\), the minimum inflow to \(G\) is

\[
6+5=11.
\]

Since \(GT\) has upper capacity \(11\),

\[
\boxed{GT=11.}
\]

## 8.6 Residual arrows when lower capacities exist

In upper-only flow networks:

\[
\text{backward residual}=f.
\]

With lower capacities, the backward arrow shows how much the current flow can be reduced before it reaches the lower capacity:

\[
\text{backward residual}=f-l.
\]

Examples:

\[
SA:(15,20),\quad f=17:
\]

\[
\text{forward}=20-17=3,
\]

\[
\text{backward}=17-15=2.
\]

\[
AD:(6,12),\quad f=8:
\]

\[
\text{forward}=12-8=4,
\]

\[
\text{backward}=8-6=2.
\]

\[
AE:(4,6),\quad f=4:
\]

\[
\text{forward}=6-4=2,
\]

\[
\text{backward}=4-4=0.
\]

\[
DF:(3,6),\quad f=4:
\]

\[
\text{forward}=6-4=2,
\]

\[
\text{backward}=4-3=1.
\]

## 8.7 Augmenting a flow when lower capacities exist

To augment a flow:

1. Find a route from source to sink through residual arrows.
2. Identify the smallest residual capacity on that route.
3. Increase the flow by that amount along forward arcs.
4. Decrease the flow by that amount along backward arcs.
5. Recalculate residual arrows.
6. Stop when every source-to-sink residual route is blocked.
7. Convert final residual-arrow information back into actual flows.

The transcript’s route is

\[
S\to A\to D\to F\to T.
\]

The residual values are

\[
3,\quad 4,\quad 2,\quad 4.
\]

The augmentation is

\[
\min(3,4,2,4)=2.
\]

If the previous flow value was \(26\), then the new flow value is

\[
26+2=28.
\]

## 8.8 Converting backward residual values back to actual flows

When lower capacities exist, a backward residual value does not directly equal the actual flow. Since

\[
\text{backward residual}=f-l,
\]

then

\[
f=l+\text{backward residual}.
\]

For example, if the lower capacity is \(15\) and the final backward residual value is \(4\), then

\[
f=15+4=19.
\]

## 8.9 Cut values with lower capacities

If a cut divides the vertices into source side \(X\) and sink side \(\overline X\), where \(S\in X\) and \(T\in\overline X\), then

\[
c(X,\overline X)=
\sum_{u\in X, v\in \overline X} u_{uv}
-
\sum_{u\in \overline X, v\in X} l_{uv}.
\]

Example:

\[
12+6+8+7+6-4.
\]

Step by step:

\[
12+6=18,
\]

\[
18+8=26,
\]

\[
26+7=33,
\]

\[
33+6=39,
\]

\[
39-4=35.
\]

So the cut value is

\[
\boxed{35}.
\]

## 8.10 Proving a flow is maximum

To prove a flow is maximum:

1. Find a feasible flow of value \(V\).
2. Find a cut with value \(V\).
3. State that by the max-flow min-cut theorem, the flow is maximal.

If a feasible flow has value \(28\), and a cut has value \(28\), then no larger flow is possible:

\[
\boxed{\text{maximum flow}=28.}
\]

## 8.11 Supersources and supersinks

If a network has multiple sources, create an artificial supersource \(S^*\). If a network has multiple sinks, create an artificial supersink \(T^*\).

For two source nodes \(S_1\) and \(S_2\): if \(S_1\) has outgoing lower capacities \(10\) and \(20\), and upper capacities \(25\) and \(16\), then

\[
S^*S_1:(30,41),
\]

because

\[
10+20=30,
\]

and

\[
25+16=41.
\]

If \(S_2\) has lower capacities \(10\) and \(10\), and upper capacities \(20\) and \(12\), then

\[
S^*S_2:(20,32).
\]

## 8.12 Restricted capacity nodes

If a node \(C\) has restricted capacity \(41\), replace it by two nodes:

\[
C_{\text{in}}
\]

and

\[
C_{\text{out}}.
\]

Connect them by an arc:

\[
C_{\text{in}}\to C_{\text{out}}.
\]

If only an upper restricted capacity is given, use \((0,41)\) in lower/upper notation. All arcs that originally entered \(C\) now enter \(C_{\text{in}}\). All arcs that originally left \(C\) now leave \(C_{\text{out}}\).

If a node \(C\) has restricted capacity \(15\), and no lower capacity is specified, represent the internal arc as

\[
C_{\text{in}}C_{\text{out}}:(0,15).
\]

## 8.13 Restricted capacity node and max-flow proof

If a new restricted node arc has capacity \(30\), and a cut also crosses arcs of capacities \(16\) and \(12\), then

\[
16+30+12=58.
\]

So the maximum flow cannot exceed \(58\). If a feasible flow of \(58\) is also shown, then

\[
\boxed{\text{maximum flow}=58}
\]

by the max-flow min-cut theorem.

## 8.14 Blocked nodes

If a node becomes blocked, no flow can pass through it. Delete the blocked node and every arc linked to that node. Mathematically, a blocked node behaves like a node with capacity \(0\), but deletion is usually cleaner.

## 8.15 Exam-only extension: minimum feasible flow

The transcript includes an exam-question discussion where a flow of \(31\) litres per second is impossible because a lower-capacity cut forces at least \(32\) litres per second. The lower capacities are

\[
10,\quad 2,\quad 5,\quad 5,\quad 6,\quad 4.
\]

Add them:

\[
10+2+5+5+6+4=32.
\]

Since

\[
31<32,
\]

a flow of \(31\) is impossible. This is logged as exam-awareness rather than a separate official LO.

# 9. Visual Asset Integration

Diagram evidence is partially unclear here because the supplied screenshot PDF is image-based, and not all 150 pages have reliable parsed text. The description below preserves the visible/readable details only. No uninspected visual detail is claimed.

[VISUAL PLACEHOLDER: FA22FlowsInNetworks2Mermaid-001 | Source: CCEA Further Mathematics specification map + transcript playlist overview | Insert from mermaid/FA22FlowsInNetworks2Mermaid-001.md | Purpose: Show how the lesson branches from cutsets and max-flow min-cut into lower capacities, residual arrows, supersources, supersinks and restricted nodes. Description: A flowchart beginning with `FA22-GRAPH-LO002`, then splitting into feasible flows, lower/upper capacities, augmentation, cut values, multiple sources/sinks and restricted nodes.]

[VISUAL PLACEHOLDER: FA22FlowsInNetworks2SVG-001 | Source: Screenshot PDF p. 1 and transcript explanation of bracket notation | Insert from svg/FA22FlowsInNetworks2SVG-001.svg | Purpose: Teach that \((l,u)\) means lower capacity and upper capacity, not coordinates. Description: A single directed arc \(A\to B\) labelled \((3,5)\), with annotation \(3\le f_{AB}\le 5\), and a small warning box: “not a coordinate pair”.]

[VISUAL PLACEHOLDER: FA22FlowsInNetworks2TikZ-001 | Source: Screenshot PDF pages 1–3 + transcript video 1 | Insert from tikz/FA22FlowsInNetworks2TikZ-001.tex | Purpose: Preserve the mini-example where considering node \(B\) forces \(AB=5\), \(BC=3\), \(BD=2\). Description: Node \(B\) with incoming arc \(AB:(3,5)\), outgoing arc \(BC:(3,4)\), outgoing arc \(BD:(2,7)\), and side note “maximum in \(=5\), minimum out \(=3+2=5\)”.]

[VISUAL PLACEHOLDER: FA22FlowsInNetworks2TikZ-002 | Source: Screenshot PDF pages 4–24 + transcript video 1 | Insert from tikz/FA22FlowsInNetworks2TikZ-002.tex | Purpose: Preserve the worked network used to deduce \(SC=2\), \(BC=4\), \(CG=6\), then lower capacities at \(DE,AE,BE\), then \(GT=11\). Description: Directed network with nodes \(S,A,B,C,D,E,F,G,T\), capacity pairs visible on all supplied arcs where readable, highlighted vertex \(C\), highlighted arcs into \(E\), and annotation \(GT=11\).]

[VISUAL PLACEHOLDER: FA22FlowsInNetworks2SVG-002 | Source: Screenshot PDF pages 26–35 + transcript video 2 | Insert from svg/FA22FlowsInNetworks2SVG-002.svg | Purpose: Show the adapted residual-arrow rule. Description: A table/arc comparison for \(SA:(15,20), f=17\), \(AD:(6,12), f=8\), \(AE:(4,6), f=4\), \(DF:(3,6), f=4\). Each row shows forward residual \(u-f\) and backward residual \(f-l\).]

[VISUAL PLACEHOLDER: FA22FlowsInNetworks2TikZ-003 | Source: Transcript video 3 | Insert from tikz/FA22FlowsInNetworks2TikZ-003.tex | Purpose: Teach the cut-value formula with backward arcs. Description: A cut separating source-side vertices from sink-side vertices. Forward crossing arcs labelled with upper capacities and a backward crossing arc labelled with lower capacity, with formula \(\sum u_{\text{forward}}-\sum l_{\text{backward}}\).]

[VISUAL PLACEHOLDER: FA22FlowsInNetworks2SVG-003 | Source: Transcript video 4 | Insert from svg/FA22FlowsInNetworks2SVG-003.svg | Purpose: Show how multiple sources and sinks become one source and one sink. Description: Three source nodes \(A,B,C\) connected to artificial supersource \(S^*\), and three sink nodes \(H,F,I\) connected to artificial supersink \(T^*\), with capacities obtained by summing outgoing/incoming capacities.]

[VISUAL PLACEHOLDER: FA22FlowsInNetworks2SVG-004 | Source: Transcript video 5 | Insert from svg/FA22FlowsInNetworks2SVG-004.svg | Purpose: Show how a restricted-capacity node becomes a restricted-capacity arc. Description: A node \(C\) replaced by \(C_{\text{in}}\to C_{\text{out}}\), with capacity \(41\) or \((0,15)\), incoming arcs moved to \(C_{\text{in}}\) and outgoing arcs moved from \(C_{\text{out}}\).]

[VISUAL PLACEHOLDER: FA22FlowsInNetworks2SVG-005 | Source: Transcript video 5 | Insert from svg/FA22FlowsInNetworks2SVG-005.svg | Purpose: Show how a blocked node and all incident arcs are removed. Description: A before/after mini-network where node \(F\) and every arc connected to \(F\) are greyed out and then deleted.]

[VISUAL PLACEHOLDER: FA22FlowsInNetworks2BridgeSVG-001 | Source: Ordinary A-Level Maths bridge + Further Maths specification | Insert from svg/FA22FlowsInNetworks2BridgeSVG-001.svg | Purpose: Compare prior ordinary Maths method with Further Maths extension. Description: Left side: ordinary inequalities, tables and proof. Right side: capacity constraints, network diagrams and max-flow/min-cut proof.]

# 10. Interactive Learning Widgets

[INTERACTIVE PLACEHOLDER: FA22FlowsInNetworks2Widget-001 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FA22FlowsInNetworks2Widget-001.html | Purpose: Let the student practise calculating cut values with lower and upper capacities.]

The student inputs forward-crossing upper capacities and backward-crossing lower capacities. The widget displays \(\sum u_{\text{forward}}-\sum l_{\text{backward}}\) and checks errors such as adding a backward arc instead of subtracting it.

[INTERACTIVE PLACEHOLDER: FA22FlowsInNetworks2Widget-002 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FA22FlowsInNetworks2Widget-002.html | Purpose: Practise calculating forward and backward residual capacities when lower capacities exist.]

The student inputs \(l,f,u\). The widget displays \(u-f\) and \(f-l\). It reinforces that the backward arrow is no longer just the current flow when lower capacity exists.

[INTERACTIVE PLACEHOLDER: FA22FlowsInNetworks2Widget-003 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FA22FlowsInNetworks2Widget-003.html | Purpose: Practise checking whether a node balances and whether each adjacent arc obeys its lower/upper capacity.]

The student inputs incoming and outgoing arc labels \((l,u)\) and proposed current flows. The widget displays \(\sum \text{in}\), \(\sum \text{out}\), and reports whether the node is feasible.

# 11. Worked Examples

## Worked Example 1: forced flows at a single vertex

**Evidence source:** Transcript video 1 and screenshot PDF pages 1–3.

A part of a capacitated directed network has

\[
AB:(3,5),\qquad BC:(3,4),\qquad BD:(2,7),
\]

with directions \(A\to B\), \(B\to C\), \(B\to D\). Deduce the value of the flow in each arc.

At \(B\), the only incoming arc is \(AB\), so

\[
3\le f_{AB}\le 5.
\]

The maximum possible inflow is

\[
5.
\]

The outgoing arcs are \(BC\) and \(BD\). Their lower capacities give minimum outflow

\[
3+2=5.
\]

Flow conservation requires

\[
f_{AB}=f_{BC}+f_{BD}.
\]

Maximum inflow equals minimum outflow, so

\[
f_{AB}=5,
\]

\[
f_{BC}=3,
\]

\[
f_{BD}=2.
\]

Final answer:

\[
\boxed{AB=5,\quad BC=3,\quad BD=2.}
\]

## Worked Example 2: considering vertex \(C\), then \(E\), then \(G\)

The relevant capacities at \(C\) are

\[
SC:(2,8),\qquad BC:(4,6),\qquad CG:(3,6).
\]

Minimum inflow:

\[
2+4=6.
\]

Maximum outflow:

\[
6.
\]

So

\[
\boxed{SC=2,\quad BC=4,\quad CG=6.}
\]

For \(E\):

\[
DE:(4,8),\qquad AE:(4,6),\qquad BE:(3,5),\qquad ET:(7,11).
\]

Maximum flow out of \(E\):

\[
11.
\]

Minimum flow into \(E\):

\[
4+4+3=11.
\]

So

\[
DE=4,
\]

\[
AE=4,
\]

\[
BE=3,
\]

\[
ET=11.
\]

For \(G\), since \(CG=6\) and \(BG\ge 5\), inflow is at least \(11\). Since \(GT\le 11\),

\[
\boxed{GT=11.}
\]

## Worked Example 3: residual capacities

For \(SA:(15,20), f=17\):

\[
20-17=3,
\]

\[
17-15=2.
\]

For \(AD:(6,12), f=8\):

\[
12-8=4,
\]

\[
8-6=2.
\]

For \(AE:(4,6), f=4\):

\[
6-4=2,
\]

\[
4-4=0.
\]

For \(DF:(3,6), f=4\):

\[
6-4=2,
\]

\[
4-3=1.
\]

So

\[
\boxed{\begin{array}{c|c|c}
\text{Arc} & \text{Forward residual} & \text{Backward residual}\\
\hline
SA & 3 & 2\\
AD & 4 & 2\\
AE & 2 & 0\\
DF & 2 & 1
\end{array}}
\]

## Worked Example 4: augmenting a flow

A residual route from \(S\) to \(T\) is

\[
S\to A\to D\to F\to T.
\]

The residual values are

\[
3,\quad 4,\quad 2,\quad 4.
\]

The augmentation is

\[
\min(3,4,2,4)=2.
\]

If the previous flow was \(26\), the new flow is

\[
26+2=28.
\]

So

\[
\boxed{\text{new flow value}=28.}
\]

## Worked Example 5: cut values with lower capacities

Forward upper capacities:

\[
12,\quad 6,\quad 8,\quad 7,\quad 6.
\]

Backward lower capacity:

\[
4.
\]

Cut value:

\[
12+6+8+7+6-4.
\]

Step by step:

\[
12+6=18,
\]

\[
18+8=26,
\]

\[
26+7=33,
\]

\[
33+6=39,
\]

\[
39-4=35.
\]

Final answer:

\[
\boxed{35}.
\]

## Worked Example 6: proving maximum flow with a cut

A feasible flow has value \(28\). A cut crosses arcs with upper capacities

\[
6,\quad 11,\quad 11.
\]

Cut value:

\[
6+11+11=28.
\]

Since the feasible flow value equals the cut value, by the max-flow min-cut theorem,

\[
\boxed{\text{maximum flow}=28.}
\]

## Worked Example 7: supersource with lower/upper capacities

For \(S_1\), lower capacities \(10,20\) and upper capacities \(25,16\) give

\[
10+20=30,
\]

\[
25+16=41.
\]

So

\[
S^*S_1:(30,41).
\]

For \(S_2\), lower capacities \(10,10\) and upper capacities \(20,12\) give

\[
S^*S_2:(20,32).
\]

## Worked Example 8: restricted capacity node

If node \(C\) has restricted capacity \(41\), replace \(C\) by \(C_{\text{in}}\) and \(C_{\text{out}}\), with an arc

\[
C_{\text{in}}\to C_{\text{out}}
\]

of capacity \(41\), or \((0,41)\) in lower/upper notation.

## Worked Example 9: blocked node

If node \(F\) becomes blocked, delete \(F\) and all arcs incident with \(F\).

# 12. Common Mistakes and Exam Traps

1. Treating \((l,u)\) as coordinates instead of a lower/upper capacity pair.
2. Forgetting that \((4,8)\) does not allow \(f=0\); it requires \(4\le f\le 8\).
3. Using the old backward-arrow rule \(\text{backward}=f\) instead of \(f-l\).
4. Forgetting to add backward residual values onto lower capacities when converting back to actual flows.
5. Adding backward cut arcs instead of subtracting lower capacities.
6. Missing a cut edge.
7. Claiming a maximum flow without a matching cut or completed augmentation proof.
8. Not checking node balance after augmentation.
9. Mixing source and sink sides of a cut.
10. Reversing \(V_{\text{in}}\to V_{\text{out}}\) when splitting a restricted node.
11. Omitting units, such as litres per second, when the context supplies them.

# 13. Practice Questions

These are AI-generated practice questions based on the lesson evidence. They are not labelled as past-paper or textbook questions.

1. An arc \(AB\) is labelled \((4,9)\). State the lower capacity, upper capacity and inequality satisfied by \(f_{AB}\).
2. A directed network contains \(AB:(2,6)\), \(BC:(3,5)\), \(BD:(3,8)\), with direction \(A\to B\), \(B\to C\), \(B\to D\). Deduce the flow in each arc.
3. Find forward and backward residual capacities for \(PQ:(5,12), f=9\), \(QR:(2,10), f=2\), and \(RS:(0,7), f=4\).
4. A residual route has values \(5,3,6,4\). The current flow is \(21\). Find the augmentation and new flow.
5. A cut crosses forward arcs with upper capacities \(9,5,8\) and backward arcs with lower capacities \(2,1\). Find the cut value.
6. A feasible flow of value \(34\) is found. A cut has value \(34\). Explain why the flow is maximum.
7. A network has sources \(A\) and \(B\). Arcs leaving \(A\) have lower capacities \(3,5\) and upper capacities \(9,11\). Arcs leaving \(B\) have lower capacities \(4,2\) and upper capacities \(8,7\). Create supersource labels.
8. A network has sink nodes \(X,Y\). Arcs entering \(X\) have lower capacities \(6,1\) and upper capacities \(10,4\). Arcs entering \(Y\) have lower capacities \(5,2,3\) and upper capacities \(9,7,6\). Create supersink labels.
9. Node \(M\) has restricted capacity \(24\). Describe how to replace it.
10. Node \(N\) must carry at least \(6\) and at most \(18\). Represent this as an arc.
11. Node \(K\) becomes blocked. State what happens.
12. A cut crosses forward arcs with upper capacities \(14,6,9,5\) and backward arcs with lower capacities \(3,4\). A feasible flow of \(27\) has been found. Can this cut prove maximality?

# 14. Worked Solutions

## Solution 1

Lower capacity \(4\), upper capacity \(9\), so

\[
\boxed{4\le f_{AB}\le 9.}
\]

## Solution 2

Maximum inflow to \(B\):

\[
6.
\]

Minimum outflow:

\[
3+3=6.
\]

So

\[
\boxed{AB=6,\quad BC=3,\quad BD=3.}
\]

## Solution 3

For \(PQ\):

\[
12-9=3,
\]

\[
9-5=4.
\]

For \(QR\):

\[
10-2=8,
\]

\[
2-2=0.
\]

For \(RS\):

\[
7-4=3,
\]

\[
4-0=4.
\]

So

\[
\boxed{PQ:3,4;\quad QR:8,0;\quad RS:3,4.}
\]

## Solution 4

\[
\min(5,3,6,4)=3.
\]

New flow:

\[
21+3=24.
\]

So augment by \(3\), and the new flow is \(24\).

## Solution 5

\[
9+5+8-2-1=19.
\]

So the cut value is

\[
\boxed{19.}
\]

## Solution 6

A feasible flow has value \(34\), and a cut also has value \(34\). By the max-flow min-cut theorem, no flow can exceed \(34\), and \(34\) can be achieved. Therefore the maximum flow is \(34\).

## Solution 7

For \(A\):

\[
3+5=8,
\]

\[
9+11=20.
\]

So \(S^*A:(8,20)\).

For \(B\):

\[
4+2=6,
\]

\[
8+7=15.
\]

So \(S^*B:(6,15)\).

## Solution 8

For \(X\):

\[
6+1=7,
\]

\[
10+4=14.
\]

So \(XT^*:(7,14)\).

For \(Y\):

\[
5+2+3=10,
\]

\[
9+7+6=22.
\]

So \(YT^*:(10,22)\).

## Solution 9

Replace \(M\) with \(M_{\text{in}}\) and \(M_{\text{out}}\), connected by

\[
M_{\text{in}}\to M_{\text{out}}:(0,24).
\]

Incoming arcs go to \(M_{\text{in}}\), outgoing arcs leave from \(M_{\text{out}}\).

## Solution 10

Use

\[
N_{\text{in}}\to N_{\text{out}}:(6,18).
\]

## Solution 11

Delete \(K\) and all arcs incident with \(K\).

## Solution 12

Cut value:

\[
14+6+9+5-3-4.
\]

Step by step:

\[
14+6=20,
\]

\[
20+9=29,
\]

\[
29+5=34,
\]

\[
34-3=31,
\]

\[
31-4=27.
\]

The cut value is \(27\). Since a feasible flow of \(27\) has been found, this cut proves the flow is maximum by the max-flow min-cut theorem.

# 15. Exam Technique Notes

When asked to deduce flows, look for a vertex where maximum possible inflow equals minimum possible outflow, or minimum possible inflow equals maximum possible outflow.

When asked to explain why an arc is at lower or upper capacity, use a conservation argument rather than just stating the value.

When asked for a maximum flow, use either a completed augmentation procedure or a flow value plus a matching cut value.

For residual arrows with lower capacities:

\[
\text{forward}=u-f,
\]

\[
\text{backward}=f-l.
\]

For cut values:

```text
Forwards use uppers.
Backwards use lowers and subtract.
```

When splitting a restricted node, use \(V_{\text{in}}\to V_{\text{out}}\). When proving a flow cannot exceed a value, use a cut. When the question supplies units, include units in the final answer.

# 16. Syllabus Gap Check

## 16.1 LO coverage table

| LO ID | Coverage status | Evidence coverage | Lesson coverage |
|---|---|---|---|
| `FA22-GRAPH-LO002` | Covered | Cutsets, max-flow min-cut theorem, lower/upper-capacity adaptations, augmentation and proof | Sections 7, 8, 11, 12, 13, 14, 15 |
| `FAS2-GRAPH-LO001` | Bridge/prerequisite only | Basic graph terminology | Sections 5 and 7 |
| `FAS2-GRAPH-LO004` | Bridge/prerequisite only | Directed arcs and weighted/capacitated edges | Sections 5, 7 and 8 |

## 16.2 Evidence coverage table

| Evidence topic | Covered? | Location |
|---|---:|---|
| Lower and upper capacities | Yes | Sections 7, 8, 11 |
| Forced flows by considering a node | Yes | Sections 8 and 11 |
| Example with \(BC=3\), \(BD=2\), \(AB=5\) | Yes | Section 11 |
| Example with \(SC=2\), \(BC=4\), \(CG=6\), \(GT=11\) | Yes | Section 11 |
| Residual arrows adapted for lower capacities | Yes | Sections 8 and 11 |
| Add backward arrow values onto lower capacities | Yes | Sections 8, 11, 12 |
| Cut values with backward lower capacities subtracted | Yes | Sections 8, 11, 14 |
| Max-flow min-cut proof | Yes | Sections 8, 11, 14, 15 |
| Supersources and supersinks | Yes | Sections 8, 11, 14 |
| Restricted capacity nodes | Yes | Sections 8, 11, 14 |
| Blocked nodes | Yes | Sections 8, 11, 14 |
| Exam-question logic | Yes | Sections 12, 15 |
| Exact official exam paper wording | No | Not supplied |

## 16.3 Off-Spec Content Found but Excluded

| Content | Decision | Reason |
|---|---|---|
| Ordinary A-Level unit prefixes in output metadata | Excluded | Further Maths output must use only `FAS1`, `FAS2`, `FA21`, `FA22` |
| Textbook-only references not supplied visually or textually | Excluded as authority | Mentioned only through transcript labels |
| Unseen official past-paper wording | Excluded | Original papers and mark schemes were not supplied |
| Bipartite matching, colouring, travelling-salesperson style algorithms | Excluded | Same broad graph theory family, but not this lesson evidence |

## 16.4 Weak evidence warnings

- The screenshot PDF is image-based, so no reliable full parsed text is available.
- Some screenshot diagrams are small or partially cropped.
- The transcript has speech-to-text imperfections, such as “sync” for “sink” and occasional verbal slips.
- Original CCEA exam papers and mark schemes were not supplied.
- The official project specification map gives broad LO wording, so lesson-specific submethods are included because they are supplied in the lesson evidence and fit the max-flow/min-cut boundary.

# 17. Recommended Enhancements Not in the Evidence

These are AI-proposed enhancements, not evidence-backed content:

- colour-coded cut diagrams;
- before/after residual-network animations;
- node-balance microscope diagrams;
- supersource and supersink template diagrams;
- restricted-node split visuals;
- interactive residual-network explorer;
- automated cut checker;
- additional tiny examples for restricted and blocked nodes.

Formal min-flow theory and linear-programming formulations are excluded from core content unless later supported by official evidence.

# 18. Supplementary Sources Used

Project sources used:

- `CCEA_GCE_Further_Mathematics_Specification_Map.md`
- `Further_Maths_README_module_map.md`
- `Further_Maths_EVIDENCE_DROP_CHECKLIST.md`
- `Ordinary_A_Level_Maths_Bridge_Spec_Extracts.md`

Lesson-specific evidence used:

- `transcripts.md`
- `Chapter_4_Flows_in_Networks_2_⌨️_(Decision_2)_screenshots.pdf`

Ordinary A-Level Mathematics sources were used only as bridge context. They do not override the Further Mathematics specification or lesson-specific flow-network evidence.

No independent cross-board sources were used. Textbook and exam labels such as `D2 Ex4A`, `D2 Ex4B`, `D2 Ex4C` appear in the supplied lesson evidence, but original textbook pages and papers were not supplied. They are therefore treated as source labels, not independent authority.

# 19. Final Student Checklist

## 19.1 Prerequisite confidence checklist

- [ ] I can read directed arrows correctly.
- [ ] I can add and subtract small integers accurately.
- [ ] I can use inequalities such as \(3\le f\le 5\).
- [ ] I can balance totals at a node.
- [ ] I can recognise source and sink nodes.
- [ ] I understand that a cut separates the source side from the sink side.

## 19.2 Further Maths method checklist

- [ ] I can interpret \((l,u)\) as lower and upper capacity.
- [ ] I can check \(l\le f\le u\) for every arc.
- [ ] I can use flow conservation at every intermediate node.
- [ ] I can calculate forward residual capacity \(u-f\).
- [ ] I can calculate backward residual capacity \(f-l\).
- [ ] I can find an augmenting route.
- [ ] I can augment by the smallest residual value on the route.
- [ ] I can convert backward residual values back into actual flows by adding lower capacities.
- [ ] I can calculate cut values using upper capacities forward and lower capacities backward.
- [ ] I can prove maximum flow using the max-flow min-cut theorem.
- [ ] I can add a supersource for multiple sources.
- [ ] I can add a supersink for multiple sinks.
- [ ] I can split a restricted node into \(V_{\text{in}}\to V_{\text{out}}\).
- [ ] I can delete a blocked node and its incident arcs.

## 19.3 Exam technique checklist

- [ ] Did I use upper capacities for forward cut arcs?
- [ ] Did I subtract lower capacities for backward cut arcs?
- [ ] Did I include every arc crossed by the cut?
- [ ] Did I prove maximality using the max-flow min-cut theorem?
- [ ] Did I include units if the question used units?
- [ ] Did I avoid calling a feasible flow “maximum” without proof?
- [ ] Did I check every affected node after changing a flow?
- [ ] Did I label supersources/supersinks clearly?
- [ ] Did I preserve arc directions?
- [ ] Did I circle or clearly mark current flows where required?

## 19.4 Bridge checklist

- [ ] I understand capacities as inequality constraints.
- [ ] I understand node balance as equation logic.
- [ ] I understand a cut as a proof tool, not just a drawing.
- [ ] I know a maximum-flow proof needs a theorem.
- [ ] I can interpret a network model in context.

## 19.5 Diagram understanding checklist

- [ ] I can identify the source and sink.
- [ ] I can read each arc direction.
- [ ] I can distinguish capacity labels from current-flow labels.
- [ ] I can find arcs crossing a cut.
- [ ] I can tell whether each crossed arc is forward or backward.
- [ ] I can split a restricted node correctly.
- [ ] I can remove a blocked node correctly.
