# 1. Lesson Title and Metadata

```yaml
date_generated: 2026-06-05
course: CCEA GCE Further Mathematics
unit_code: FA22
unit_name: Further A2 2 Applied Mathematics
applied_section: Section D: Discrete and Decision Mathematics
topic_code: FA22-GRAPH
official_topic_name: Graph theory
lesson_topic_name: Flows in Networks
topic_slug: flows_in_networks
topic_pascal: FlowsInNetworks
topic_id: FA22FlowsInNetworks
lesson_file: FA22_flows_in_networks_lesson.md
core_lo_ids:
  - FA22-GRAPH-LO002
bridge_tags:
  - ordinary_maths_modelling
  - diagram_interpretation
  - proof_and_reasoning
  - inequalities
  - arithmetic_accuracy
topic_tags:
  - graph_theory
  - directed_networks
  - capacitated_networks
  - flow
  - cutsets
  - max_flow_min_cut
  - decision_mathematics
```

# Flows in Networks: Cutsets and the Max-Flow Min-Cut Theorem

This lesson teaches how to model movement through a **capacitated directed network** and how to prove that a proposed flow is **maximal** using the **maximum flow-minimum cut theorem**. Water, traffic, people or data move along one-way pipes, roads, corridors or connections, and every connection has a maximum safe amount it can carry.

| LO ID | Official wording |
|---|---|
| `FA22-GRAPH-LO002` | demonstrate understanding of cutsets and use the max-flow min-cut theorem |

---

# 2. Evidence Map

| Evidence source | How it is used in this lesson |
|---|---|
| `CCEA_GCE_Further_Mathematics_Specification_Map.md` | Establishes `FA22-GRAPH-LO002` as the core learning outcome and keeps the lesson inside the CCEA boundary. |
| `Further_Maths_README_module_map.md` | Sets metadata rules, topic ID rules and output structure. |
| `Further_Maths_EVIDENCE_DROP_CHECKLIST.md` | Controls evidence preservation, missing-evidence logging and visual placeholder rules. |
| `Ordinary_A_Level_Maths_Bridge_Spec_Extracts.md` | Supplies the bridge rule: graph theory has no direct ordinary A-Level predecessor, so bridge from modelling, proof, tables, inequalities and algorithmic reasoning. |
| `CCEA_GCE_Mathematics_Specification_Map.md` | Bridge source for ordinary Maths modelling, diagram interpretation, proof and problem solving. |
| Uploaded transcript: `transcripts.md` | Supplies the teaching sequence: capacities, source, sink, feasibility, conservation, saturated arcs, value of a flow, cuts, cut capacities, initial flows, labelling procedure, augmenting routes and maximum flow-minimum cut theorem. |
| Uploaded screenshot PDF: `Chapter_3_Flows_in_Networks_1_⌨️_(Decision_2)_screenshots.pdf` | Supplies visual evidence for diagrams. The PDF has no parsed text, so diagram details are only claimed where visible or transcript-supported. |

---

# 3. Specification Alignment

| LO ID | Official CCEA wording | Lesson coverage | Evidence source | Syllabus boundary | Ordinary A-Level bridge |
|---|---|---|---|---|---|
| `FA22-GRAPH-LO002` | demonstrate understanding of cutsets and use the max-flow min-cut theorem | Defines capacitated directed networks, flows, cuts and cut capacities. Teaches how to prove a flow is maximal by showing its value equals the capacity of a suitable cut. Includes the labelling procedure as a supporting way to find candidate maximum flows. | CCEA Further Maths specification map; transcript; screenshot PDF | Core lesson content. Do not extend to multiple source/sink transformations or full proof of theorem unless supplied later. | Ordinary A-Level has no direct graph-flow predecessor. Use modelling, diagram reading, proof, inequalities and arithmetic accuracy as the bridge. |

## Boundary statement

The CCEA specification gives the official boundary as **cutsets and the max-flow min-cut theorem**. The transcript contains a broader teaching route through flow logic, initial flows and the labelling procedure. These are included because they are natural machinery for using the theorem, but the lesson does not treat extra network-flow theory as a separate CCEA requirement.

---

# 4. Learning Objectives

## 4.1 Core Further Maths objectives

By the end of this lesson, you should be able to:

1. Recognise a **capacitated directed network**.
2. Identify the **source vertex** and **sink vertex**.
3. Interpret arc capacities and current flow values.
4. Apply the **feasibility condition**:

\[
0 \leq f(e) \leq c(e)
\]

for each arc \(e\).

5. Apply the **conservation condition** at an internal vertex:

\[
\text{flow into the vertex}=\text{flow out of the vertex}.
\]

6. Identify **saturated arcs**.
7. Find the **value of a flow**.
8. Find the capacity of a **cut**.
9. Use a cut to place an upper bound on possible flow.
10. Use the **maximum flow-minimum cut theorem** to prove that a flow is maximal.
11. Use the labelling procedure to improve a flow when required by a question.

## 4.2 Bridge objectives

You should connect this topic to ordinary A-Level skills by being able to read mathematical information from a diagram, translate a real context into variables, use arithmetic and inequalities, give written reasons, and keep a multi-step algorithm organised.

## 4.3 Exam technique objectives

You should be able to distinguish **capacity numbers** from **current flow numbers**, use the correct values when calculating cut capacities, write clear explanations for missing flow values, list saturated arcs using correct arc notation, and prove maximality with a theorem sentence.

---

# 5. Explicit Prerequisite Recap

## 5.1 GCSE foundations

You need directed arrows and basic diagram reading, substitution into simple equations, solving simple linear equations, accurate addition and subtraction, and comparing values using inequalities.

For example, if an arc has capacity \(8\) and current flow \(5\), the spare capacity is:

\[
8-5=3.
\]

## 5.2 Ordinary AS/A2 Mathematics foundations

There is no direct ordinary CCEA A-Level topic called “network flows”. The nearest ordinary Maths habits are modelling, interpreting diagrams, using tables, using inequalities and explaining why a result is true.

## 5.3 Previous Further Mathematics foundations

This lesson benefits from earlier graph vocabulary: **vertex**, **node**, **edge**, **arc**, **directed arc**, **weighted edge**, **digraph**, **route**, **path** and **network**.

### A-Level Maths Bridge: What You Already Know and What Further Maths Changes

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| Ordinary Mathematics: modelling and problem solving | A real situation can be simplified into a mathematical model | Flow through pipes, roads, corridors or computer links becomes a capacitated directed network | The model is discrete and diagram-based, so calculus instincts are not the main tool |
| Ordinary Mathematics: diagrams and interpretation | Diagrams carry mathematical information | A network diagram carries vertices, directed arcs, capacities, current flows and cuts | One diagram can contain two types of numbers: capacities and current flows |
| Ordinary Mathematics: proof and reasoning | A conclusion must follow from stated facts | Maximality is proved by matching a flow value to a cut capacity | “It looks full” is not a proof |
| Ordinary Mathematics: arithmetic and inequalities | Compare totals and limits | A route is limited by its smallest usable arc value, and a flow cannot exceed capacity | Adding all route capacities is usually the wrong move |
| Ordinary Mathematics: organised working | Multi-step calculations need structure | The labelling procedure needs forward and backward arrow labels | Messy diagrams cause silent errors; colour helps in learning but exams may require plain pen/pencil working |

In ordinary A-Level Maths, this idea appeared as **modelling plus diagram interpretation**. In Further Maths, the same idea becomes a **network-flow model**. The key upgrade is that a network has **capacity constraints** and **conservation constraints**. Each arc has a maximum possible flow, and each internal vertex must balance what enters and what leaves. The danger is that old “just calculate the total” habits can betray you: one narrow pipe can control the whole river.

---

# 6. Big Picture Explanation

A **flow network** models movement through a system where every connection has a limit.

The transcript gives several modelling examples:

- water through pipes;
- traffic along roads;
- people along one-way corridors;
- data through computer networks.

The mathematical object is a **capacitated directed network**.

- **Directed** means each arc has a direction.
- **Capacitated** means each arc has a maximum amount that can flow through it.
- A **source** is where the flow starts.
- A **sink** is where the flow ends.

The central exam question is usually:

```text
What is the maximum possible flow from the source to the sink, and how do we prove it is maximum?
```

There are two sides to the answer. First, find or improve a flow pattern. Second, find a cut. The theorem ties the two together:

\[
\boxed{\text{maximum flow}=\text{minimum cut capacity}}
\]

If we find a flow of value \(38\), and also find a cut of capacity \(38\), then the flow cannot be improved. The cut is a ceiling, the flow reaches the ceiling, and the proof lands with a click.

---

# 7. Key Definitions and Notation

## 7.1 Network

A **network** is a graph used to model connections between objects. The objects are **vertices** or **nodes**, and the connections are **arcs**.

## 7.2 Directed network

A **directed network** is a network where each arc has a direction. If an arc goes from \(A\) to \(B\), write \(AB\) or \(A\to B\).

## 7.3 Capacity

The **capacity** of an arc is the maximum amount that can flow through that arc. Let \(c(AB)\) mean the capacity of arc \(AB\). If \(c(AB)=8\), then at most \(8\) units may flow along \(AB\).

## 7.4 Current flow

The **current flow** along an arc is the amount currently flowing through that arc. Let \(f(AB)\) mean the current flow along arc \(AB\).

## 7.5 Feasibility condition

A flow is **feasible** only if no arc carries more than its capacity:

\[
0 \leq f(e) \leq c(e).
\]

This is the “pipe does not burst” rule.

## 7.6 Conservation condition

At every internal vertex, the total amount flowing in equals the total amount flowing out:

\[
\sum \text{flows into }V=\sum \text{flows out of }V.
\]

This is the “no flow mysteriously appears or disappears” rule.

## 7.7 Source vertex

The **source vertex** is where all the flow starts. It is often labelled \(S\).

## 7.8 Sink vertex

The **sink vertex** is where all the flow ends. It is often labelled \(T\).

## 7.9 Saturated arc

An arc is **saturated** if its current flow is equal to its capacity:

\[
f(e)=c(e).
\]

## 7.10 Value of a flow

The **value of a flow** is the total amount flowing through the network. It can be found as:

\[
\text{total flow out of the source}=\text{total flow into the sink}.
\]

## 7.11 Route flow

For a route, the current flow along the whole route is limited by the smallest current flow on the arcs in that route. If route \(CAE\) has current flow values \(19\) and \(11\), then:

\[
\text{current flow along }CAE=\min(19,11)=11.
\]

## 7.12 Cut

A **cut** splits the network into two parts: one containing at least the source, and one containing at least the sink.

## 7.13 Cut capacity

The **capacity of a cut** is found by adding the capacities of the arcs that cross the cut in the correct direction from the source side to the sink side.

\[
\boxed{\text{Use capacities, not current flows, when finding cut capacity.}}
\]

## 7.14 Maximum flow-minimum cut theorem

A flow is maximal if its value is equal to the minimum possible cut capacity:

\[
\boxed{\text{If a feasible flow has value }F\text{ and there is a cut of capacity }F,\text{ then the flow is maximal.}}
\]

---

# 8. Core Theory

## 8.1 Capacitated directed networks

A capacitated directed network is a directed graph where every arc has a maximum capacity. If \(c(AB)=8\) and \(f(AB)=5\), then the spare capacity is:

\[
c(AB)-f(AB)=8-5=3.
\]

**Bridge Note:** In ordinary A-Level Maths, a diagram might show a length, angle, force or probability. Here, a network diagram shows capacities and flows. The diagram is doing arithmetic in disguise.

## 8.2 Feasibility condition

A flow is feasible only when every arc obeys:

\[
0 \leq f(e) \leq c(e).
\]

If \(c(DE)=5\), then \(f(DE)=6\) is impossible because \(6>5\). A current flow of \(5\) is allowed and means the arc is saturated.

## 8.3 Conservation condition

At an internal vertex, whatever flows in must flow out. Suppose vertex \(D\) has one incoming arc with current flow \(x\), and two outgoing arcs with current flows \(5\) and \(2\). Then:

\[
x=5+2=7.
\]

**Bridge Note:** In ordinary mechanics, a balanced situation often means “in equals out” or “up equals down”. Here, conservation means the vertex does not store flow.

## 8.4 Value of a flow

If the source has outgoing current flows \(7,19,4\), then:

\[
\text{value of flow}=7+19+4=30.
\]

If the sink has incoming flows \(8,11,5,6\), then:

\[
8+11+5+6=30.
\]

The source total and sink total agree for a feasible flow.

## 8.5 Saturated arcs

An arc is saturated when \(f(e)=c(e)\). If \(c(CA)=20\) and \(f(CA)=19\), then \(CA\) is not saturated and has spare capacity \(1\).

## 8.6 Route flow is controlled by the bottleneck

For route \(C\to A\to E\), with current flows \(19\) and \(11\):

\[
\text{current flow along }CAE=\min(19,11)=11.
\]

One narrow pipe decides how much gets through the whole stretch.

## 8.7 Cuts

Let the source-side set be \(X\) and the sink-side set be \(Y\). Then:

\[
S\in X,\qquad T\in Y.
\]

The cut crosses arcs between \(X\) and \(Y\). For a directed network, the capacity of the cut is found by adding capacities of arcs going from the source side to the sink side.

## 8.8 Cut capacity examples

For \(C_1\):

\[
\text{capacity}(C_1)=14+15=29.
\]

For \(C_2\):

\[
\text{capacity}(C_2)=8+6+16=30.
\]

For \(C_3\):

\[
\text{capacity}(C_3)=8+4+7+9=28.
\]

## 8.9 Why cuts bound the flow

Every unit of flow that starts at the source and ends at the sink must cross any valid cut at least once. Therefore:

\[
\text{flow value}\leq \text{cut capacity}.
\]

For every cut \(C\):

\[
F\leq c(C).
\]

## 8.10 Maximum flow-minimum cut theorem

The theorem says:

\[
\boxed{\text{maximum flow value}=\text{minimum cut capacity}.}
\]

If \(\text{flow value}=38\) and a cut has capacity:

\[
8+10+9+11=38,
\]

then the flow is maximal.

**Bridge Note:** In ordinary A-Level proof, you often show two expressions are equal. Here, equality is a certificate. The cut says “you cannot go above \(38\)”, and the flow says “I have reached \(38\)”.

## 8.11 Finding an initial flow

For route \(SACT\) with capacities \(19,11,17\):

\[
\min(19,11,17)=11.
\]

For route \(SBADT\) with capacities \(18,17,20,23\):

\[
\min(18,17,20,23)=17.
\]

The initial flow value is:

\[
11+17=28.
\]

## 8.12 Labelling procedure: forward and backward arrows

For each arc, draw two labels:

1. a **forward label**, representing spare capacity;
2. a **backward label**, representing current flow.

If \(c(AB)=20\) and \(f(AB)=15\), then:

\[
\text{forward}=20-15=5,
\]

\[
\text{backward}=15.
\]

Check:

\[
5+15=20.
\]

## 8.13 Meaning of the forward label

The forward label tells us how much more flow could be sent along the original direction of the arc.

## 8.14 Meaning of the backward label

The backward label tells us how much current flow could be cancelled or rerouted. It is not literal reverse flow; it is permission to undo part of an existing flow so the whole network can carry more.

## 8.15 Augmenting route

An **augmenting route** is a route from the source to the sink where every label used along the route is positive. The amount by which the flow can be increased is the smallest label on the route.

If labels on a route are \(5,3,7,3\), then:

\[
\min(5,3,7,3)=3.
\]

## 8.16 Updating labels after augmenting

If the augmenting amount is \(3\):

- every forward label used decreases by \(3\);
- the paired backward label increases by \(3\).

For example:

\[
5\to 2,\qquad 15\to 18,
\]

and:

\[
2+18=20.
\]

## 8.17 Stopping condition for the labelling procedure

Continue finding augmenting routes until every possible source-to-sink route contains a zero label. When no augmenting route remains, the current flow is a candidate maximum flow. Then prove maximality using the maximum flow-minimum cut theorem.

## 8.18 Finding a minimum cut from saturated and empty arcs

A minimum cut can often be found by cutting:

1. saturated arcs going away from the source;
2. empty arcs going towards the source.

A non-empty arc pointing back towards the source can free up capacity elsewhere, so it does not behave like a simple bottleneck. An empty backward-towards-source arc does not free anything up, so it can be part of the cut certificate.

## 8.19 Exam-proof template

To prove that a flow is maximal:

1. State the value of the flow.
2. Find a cut.
3. Calculate the capacity of the cut using capacities, not current flows.
4. Show the cut capacity equals the flow value.
5. Conclude using the theorem.

Template:

```text
The value of the flow is F.
Consider the cut through the arcs ...
The capacity of this cut is ...
This is equal to F.
Hence, by the maximum flow-minimum cut theorem, the flow is maximal.
```

---

# 9. Visual Asset Integration

Diagram evidence is partially unclear here. The screenshot PDF has no parsed text, so the description below preserves only the visible/readable details and transcript-supported details. No uninspected visual detail is claimed.

[VISUAL PLACEHOLDER: FA22FlowsInNetworksMermaid-001 | Source: CCEA `FA22-GRAPH-LO002` + uploaded transcript | Insert from mermaid/FA22FlowsInNetworksMermaid-001.md | Purpose: Show the complete decision route from reading a capacitated directed network to proving maximality using the maximum flow-minimum cut theorem. The visual must include: identify source/sink, read capacities, check feasibility, apply conservation, find or improve flow, find cut capacity, compare flow value with cut value.]

[VISUAL PLACEHOLDER: FA22FlowsInNetworksSVG-001 | Source: Screenshot PDF page 1 + uploaded transcript Video 1 | Insert from svg/FA22FlowsInNetworksSVG-001.svg | Purpose: Introduce a capacitated directed network. The visual must show vertices \(A,B,C,D,E,F\), directed arcs, capacities, source \(C\), sink \(E\), and the idea that numbers on arcs represent maximum possible flow.]

[VISUAL PLACEHOLDER: FA22FlowsInNetworksSVG-002 | Source: Screenshot PDF pages 2-18 + uploaded transcript Video 1 | Insert from svg/FA22FlowsInNetworksSVG-002.svg | Purpose: Compare capacity values with circled current-flow values. The visual must show non-circled capacities, circled current flows, saturated arcs, and the conservation equations used to find \(x=7\), \(y=6\), and flow value \(30\).]

[VISUAL PLACEHOLDER: FA22FlowsInNetworksSVG-003 | Source: Screenshot PDF pages 27-34 + uploaded transcript Video 2 | Insert from svg/FA22FlowsInNetworksSVG-003.svg | Purpose: Explain cuts and cut capacities. The visual must show dashed cut lines \(C_1,C_2,C_3\), source-side and sink-side regions, and highlight only arcs counted in the cut capacity.]

[VISUAL PLACEHOLDER: FA22FlowsInNetworksSVG-004 | Source: Uploaded transcript Video 3 + screenshot PDF pages 36-37 | Insert from svg/FA22FlowsInNetworksSVG-004.svg | Purpose: Show how route bottlenecks produce an initial flow. The visual must show routes \(SACT\) and \(SBADT\), bottleneck values \(11\) and \(17\), and final initial flow value \(28\).]

[VISUAL PLACEHOLDER: FA22FlowsInNetworksSVG-005 | Source: Uploaded transcript Video 4 | Insert from svg/FA22FlowsInNetworksSVG-005.svg | Purpose: Show the labelling procedure with forward spare-capacity labels and backward current-flow labels. The visual must include a key: forward label \(=c-f\), backward label \(=f\), and the check that the two labels sum to the arc capacity.]

[VISUAL PLACEHOLDER: FA22FlowsInNetworksSVG-006 | Source: Uploaded transcript Video 5 | Insert from svg/FA22FlowsInNetworksSVG-006.svg | Purpose: Show the maximum flow-minimum cut theorem as a proof certificate. The visual must show a feasible flow value \(38\), a cut through arcs \(AD,AC,BC,BE\), cut capacity \(8+10+9+11=38\), and the conclusion that the flow is maximal.]

[VISUAL PLACEHOLDER: FA22FlowsInNetworksBridgeSVG-001 | Source: Ordinary A-Level Maths bridge + Further Maths specification | Insert from svg/FA22FlowsInNetworksBridgeSVG-001.svg | Purpose: Compare ordinary diagram interpretation with Further Maths network-flow interpretation. The visual must show an ordinary diagram-reading habit evolving into capacity, flow, conservation and cut reasoning.]

[VISUAL PLACEHOLDER: FA22FlowsInNetworksTikZ-001 | Source: Uploaded transcript Video 1 | Insert from tikz/FA22FlowsInNetworksTikZ-001.tex | Purpose: Precise network diagram for the flow-logic example with vertices \(A,B,C,D,E,F\), source \(C\), sink \(E\), capacities and circled flow values.]

[VISUAL PLACEHOLDER: FA22FlowsInNetworksTikZ-002 | Source: Uploaded transcript Video 2 | Insert from tikz/FA22FlowsInNetworksTikZ-002.tex | Purpose: Precise cut diagram for cuts \(C_1,C_2,C_3\), showing which arcs contribute to each cut capacity.]

[VISUAL PLACEHOLDER: FA22FlowsInNetworksTikZ-003 | Source: Uploaded transcript Video 4 | Insert from tikz/FA22FlowsInNetworksTikZ-003.tex | Purpose: Labelling-procedure diagram with paired forward/backward arrow labels, chosen augmenting route and bottleneck value.]

---

# 10. Interactive Learning Widgets

[INTERACTIVE PLACEHOLDER: FA22FlowsInNetworksWidget-001 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FA22FlowsInNetworksWidget-001.html | Purpose: Feasibility and conservation checker.]

The student inputs each arc capacity \(c(e)\), current flow \(f(e)\), source vertex and sink vertex. The widget displays whether every arc satisfies \(0\leq f(e)\leq c(e)\), whether each internal vertex satisfies conservation, the value of the flow and saturated arcs.

[INTERACTIVE PLACEHOLDER: FA22FlowsInNetworksWidget-002 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FA22FlowsInNetworksWidget-002.html | Purpose: Cut capacity trainer.]

The student selects source-side vertices and sink-side vertices. The widget displays all crossing arcs, which arcs count, which arcs point the wrong way, and total cut capacity.

[INTERACTIVE PLACEHOLDER: FA22FlowsInNetworksWidget-003 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FA22FlowsInNetworksWidget-003.html | Purpose: Labelling procedure and augmenting-route trainer.]

The student inputs capacities, current flows and a proposed augmenting route. The widget displays forward labels \(c-f\), backward labels \(f\), route label values, bottleneck value and updated flows.

---

# 11. Worked Examples

## Worked Example 1: Flow logic, missing values and saturated arcs

**Evidence source:** Uploaded transcript Video 1 and screenshot PDF pages 11-18.  
**On-spec status:** Supporting method for `FA22-GRAPH-LO002`.  
**Ordinary Maths idea used:** Equations from diagram information.  
**Further Maths upgrade:** Conservation of flow at vertices and flow value across a directed network.

### Question

An initial flow pattern is shown on a capacitated directed network. The non-circled numbers show capacities. The circled numbers show current flow.

Find \(x\) and \(y\), explaining your reasoning.

The relevant flow values are:

- into \(D\): \(x\);
- out of \(D\): \(5\) and \(2\);
- out of source \(C\): \(x\), \(19\), \(4\);
- into sink \(E\): \(8\), \(11\), \(5\), \(y\).

### Solution for \(x\)

\[
\text{flow into }D=\text{flow out of }D.
\]

\[
x=5+2=7.
\]

Therefore:

\[
\boxed{x=7}.
\]

### Solution for \(y\)

\[
\text{flow out of source}=\text{flow into sink}.
\]

\[
x+19+4=8+11+5+y.
\]

Substitute \(x=7\):

\[
7+19+4=8+11+5+y.
\]

\[
30=24+y.
\]

\[
y=6.
\]

Therefore:

\[
\boxed{y=6}.
\]

### Saturated arcs

The five saturated arcs are:

\[
AB,\quad AE,\quad DF,\quad CF,\quad DE.
\]

### Value of the initial flow

\[
\text{flow value}=x+19+4=7+19+4=30.
\]

Therefore:

\[
\boxed{\text{value of initial flow}=30}.
\]

### Current flow along route \(CAE\)

\[
\min(19,11)=11.
\]

So:

\[
\boxed{\text{current flow along }CAE=11}.
\]

---

## Worked Example 2: Your Turn flow logic with \(x,y,z\)

At vertex \(A\):

\[
26=10+x+9.
\]

\[
26=19+x.
\]

\[
x=7.
\]

At vertex \(B\):

\[
10+9=y+12.
\]

\[
19=y+12.
\]

\[
y=7.
\]

At vertex \(D\):

\[
7+7+4=z.
\]

\[
z=18.
\]

Therefore:

\[
\boxed{x=7,\quad y=7,\quad z=18}.
\]

The saturated arc identified in the transcript is:

\[
ET.
\]

The value of the initial flow is:

\[
26+10=36.
\]

The current flow along \(BED\) is:

\[
\min(12,4)=4.
\]

The current flow along \(SABET\) is:

\[
\min(26,9,12,8)=8.
\]

---

## Worked Example 3: Cut capacities \(C_1,C_2,C_3\)

For \(C_1\):

\[
\text{capacity}(C_1)=14+15=29.
\]

For \(C_2\):

\[
\text{capacity}(C_2)=8+6+16=30.
\]

For \(C_3\):

\[
\text{capacity}(C_3)=8+4+7+9=28.
\]

The transcript stresses that cut capacities use the **arc capacities**, not the current flow pattern.

---

## Worked Example 4: Cut capacities with current-flow circles shown

For \(C_1\), the included capacities are \(10,8,14,10\):

\[
\text{capacity}(C_1)=10+8+14+10=42.
\]

For \(C_2\), the included capacities are \(9,14,7,6,7\):

\[
\text{capacity}(C_2)=9+14+7+6+7=43.
\]

Some arcs crossed by the cut are not counted because they flow in the wrong direction relative to the cut.

---

## Worked Example 5: Additional cut values \(C_4\) and \(C_5\)

For \(C_4\), included capacities are \(14,7,9\):

\[
\text{value}(C_4)=14+7+9=30.
\]

For \(C_5\), included capacities are \(15,3,4,11\):

\[
\text{value}(C_5)=15+3+4+11=33.
\]

The excluded capacity \(6\) flows back into the cut, so it is not included.

---

## Worked Example 6: Finding an initial flow from two routes

For route \(SACT\), the capacities are \(19,11,17\):

\[
\min(19,11,17)=11.
\]

Assign:

\[
f(SA)=11,\quad f(AC)=11,\quad f(CT)=11.
\]

For route \(SBADT\), the capacities are \(18,17,20,23\):

\[
\min(18,17,20,23)=17.
\]

Assign:

\[
f(SB)=17,\quad f(BA)=17,\quad f(AD)=17,\quad f(DT)=17.
\]

The value of the initial flow is:

\[
11+17=28.
\]

So:

\[
\boxed{\text{value of the initial flow}=28}.
\]

---

## Worked Example 7: Initial flow using saturated arcs and conservation

The following arcs are saturated:

\[
SG,\quad GE,\quad EJ,\quad GJ,\quad GK,\quad JT.
\]

The corresponding saturated current flows are:

\[
17,\quad 2,\quad 10,\quad 28,\quad 14,\quad 12.
\]

At \(J\), the flow out is \(28\). The known flow into \(J\) is:

\[
12+2=14.
\]

So the missing flow into \(J\) is:

\[
28-14=14.
\]

At \(K\), the flow in is \(10\), so the flow out is \(10\). At \(H\), the flow in is \(14\), so the flow out is \(14\). At \(E\), the flow out is \(26\), so the flow in is \(26\). At \(G\), the flow in is \(17\), and known flow out is \(10+2=12\), so the missing flow out is \(5\). At \(F\), flow out is \(14\), so the missing flow in is \(14-5=9\).

The value of the flow is:

\[
26+9+17=52.
\]

---

## Worked Example 8: Labelling procedure, augmenting routes and maximal flow \(38\)

For each arc:

\[
\text{forward label}=c-f,
\]

\[
\text{backward label}=f.
\]

Initial flow value:

\[
F_0=15+15=30.
\]

First augmenting route:

\[
SACDT,
\]

with increase \(3\):

\[
F_1=30+3=33.
\]

Second augmenting route:

\[
SBET,
\]

with increase \(2\):

\[
F_2=33+2=35.
\]

Third augmenting route:

\[
SBCDET,
\]

with increase \(3\):

\[
F_3=35+3=38.
\]

After these updates, no more augmenting routes can be used because every possible remaining route contains a zero label. So the candidate maximum flow is:

\[
\boxed{38}.
\]

The final arc flows are read from the backward-label values.

---

## Worked Example 9: Labelling procedure with a reverse arc and maximal flow \(17\)

Initial flow value:

\[
F_0=8+5=13.
\]

The augmenting route is:

\[
SBDAC T.
\]

This uses \(DA\) in reverse relative to an existing arc, allowing some existing flow to be cancelled and rerouted.

The increase is:

\[
\Delta F=4.
\]

New flow value:

\[
F_1=13+4=17.
\]

So:

\[
\boxed{\text{maximal flow}=17}.
\]

A backward label is not “flow physically going backwards”. It is permission to undo an earlier choice.

---

## Worked Example 10: Proving maximality with a cut of value \(38\)

Flow value:

\[
18+20=38.
\]

Choose a cut through:

\[
AD,\quad AC,\quad BC,\quad BE.
\]

The capacities are:

\[
8,\quad 10,\quad 9,\quad 11.
\]

Cut capacity:

\[
8+10+9+11=38.
\]

Since:

\[
\text{flow value}=\text{cut capacity}=38,
\]

by the maximum flow-minimum cut theorem:

\[
\boxed{\text{the flow is maximal}.}
\]

---

## Worked Example 11: Proving maximality with a cut of value \(72\)

Flow value:

\[
15+28+29=72.
\]

Choose a cut through:

\[
AF,\quad DF,\quad GT,\quad HT.
\]

The capacities are:

\[
11,\quad 5,\quad 31,\quad 25.
\]

Cut capacity:

\[
11+5+31+25=72.
\]

Since:

\[
\text{flow value}=\text{cut capacity}=72,
\]

by the maximum flow-minimum cut theorem:

\[
\boxed{\text{the flow is maximal}.}
\]

---

## Worked Example 12: Minimum cut with an empty arc towards the source

A minimum cut may cut:

- saturated arcs flowing away from the source;
- empty arcs flowing towards the source.

The flow value is:

\[
8+9=17.
\]

The cut capacity is:

\[
8+3+6=17.
\]

Since:

\[
\text{flow value}=\text{cut capacity}=17,
\]

by the maximum flow-minimum cut theorem:

\[
\boxed{\text{the flow is maximal}.}
\]

---

# 12. Common Mistakes and Exam Traps

## 12.1 Mistaking capacity for flow

Capacity is the maximum possible amount \(c(e)\). Current flow is the actual amount currently flowing \(f(e)\). For cut capacity, use \(c(e)\), not \(f(e)\).

## 12.2 Forgetting the conservation condition

At an internal vertex:

\[
\sum f_{\text{in}}=\sum f_{\text{out}}.
\]

A common wrong method is to use capacities instead of flows when solving for missing values.

## 12.3 Treating source and sink like ordinary internal vertices

The source is where net flow leaves. The sink is where net flow arrives. Do not force internal-vertex conservation at the source or sink.

## 12.4 Adding all route values instead of taking the bottleneck

For route \(CAE\), if the current values are \(19\) and \(11\), the route flow is \(\min(19,11)=11\), not \(19+11\).

## 12.5 Listing saturated arcs using the wrong comparison

An arc is saturated if \(f(e)=c(e)\). A large flow is not enough.

## 12.6 Counting wrong-direction arcs in a cut

When finding a cut capacity, count arcs that cross from the source side to the sink side.

## 12.7 Using current-flow circles for cut capacity

If a capacity is \(14\) and the current flow is \(12\), the cut contribution is \(14\), not \(12\).

## 12.8 Forgetting to justify missing values

If the question says “explaining your reasoning”, write a sentence such as:

```text
At vertex D, flow in equals flow out.
```

Then show:

\[
x=5+2=7.
\]

## 12.9 Labelling procedure direction errors

Forward label:

\[
c-f.
\]

Backward label:

\[
f.
\]

Check:

\[
(c-f)+f=c.
\]

## 12.10 Updating labels the wrong way

If augmenting by \(k\) along a forward arc, the forward label decreases by \(k\), and the backward label increases by \(k\).

## 12.11 Thinking a backward route means physical reverse flow

A backward label means “we may reduce existing flow along this arc”. It does not mean the pipe has become a two-way pipe.

## 12.12 Failing to state the theorem in the conclusion

A complete proof needs:

```text
Since the value of the flow equals the capacity of this cut, the flow is maximal by the maximum flow-minimum cut theorem.
```

---

# 13. Practice Questions

The following questions are **AI-generated practice questions** based on the lesson evidence. They are not labelled as past-paper or textbook questions.

## Practice Question 1: Basic flow logic

In a capacitated directed network, vertex \(D\) has one incoming arc with current flow \(x\). It has two outgoing arcs with current flows \(6\) and \(4\). Find \(x\), explaining your reasoning.

## Practice Question 2: Saturated arcs

| Arc | Capacity | Current flow |
|---|---:|---:|
| \(AB\) | \(12\) | \(12\) |
| \(BC\) | \(8\) | \(5\) |
| \(CD\) | \(7\) | \(7\) |
| \(DE\) | \(10\) | \(9\) |
| \(AE\) | \(6\) | \(6\) |

List all saturated arcs.

## Practice Question 3: Value of a flow

A source \(S\) has outgoing current flows \(13,9,5\). Find the value of the flow.

## Practice Question 4: Route bottleneck

A route \(SABT\) has current flow values:

\[
f(SA)=14,\quad f(AB)=9,\quad f(BT)=11.
\]

Find the current flow along route \(SABT\).

## Practice Question 5: Missing values in a flow network

At vertex \(A\), flow in \(=24\), and the outgoing current flows are \(8,x,7\). At vertex \(B\), flow in \(=x+5\), and the outgoing current flows are \(y,6\). Find \(x\) and \(y\).

## Practice Question 6: Cut capacity

A cut \(C_1\) crosses arcs from the source side to the sink side with capacities \(9,14,6,11\). Find the capacity of \(C_1\).

## Practice Question 7: Direction trap in a cut

| Arc | Capacity | Direction relative to cut |
|---|---:|---|
| \(SA\) | \(10\) | source side to sink side |
| \(BC\) | \(7\) | sink side to source side |
| \(AD\) | \(8\) | source side to sink side |
| \(CE\) | \(5\) | source side to sink side |
| \(DB\) | \(4\) | sink side to source side |

Find the cut capacity.

## Practice Question 8: Initial flow from routes

Find an initial flow using routes \(SACT\) with capacities \(16,10,12\), and \(SBDT\) with capacities \(15,13,17\). State the value of the initial flow.

## Practice Question 9: Labelling procedure, one augmenting route

An augmenting route has labels \(6,4,9,5\). Find the maximum amount by which the flow can be augmented. If the current flow value is \(31\), find the new flow value.

## Practice Question 10: Forward and backward labels

An arc \(AB\) has capacity \(18\) and current flow \(11\). Find the forward label, backward label, and a consistency check.

## Practice Question 11: Max-flow min-cut proof

A feasible flow has value \(42\). A cut crosses arcs with capacities \(10,8,13,11\). Use the maximum flow-minimum cut theorem to prove that the flow is maximal.

## Practice Question 12: Empty reverse arc in a cut

A cut contains two saturated arcs going away from the source with capacities \(9\) and \(12\), and one empty arc going towards the source with capacity \(4\). The value of the flow is \(25\). Explain why the empty arc may be included in the cut certificate, calculate the cut capacity, and conclude whether the flow is maximal.

---

# 14. Worked Solutions

## Solution 1

\[
x=6+4=10.
\]

So \(\boxed{x=10}\).

## Solution 2

An arc is saturated if capacity equals current flow. Therefore:

\[
\boxed{AB,\ CD,\ AE}.
\]

## Solution 3

\[
13+9+5=27.
\]

So \(\boxed{27}\).

## Solution 4

\[
\min(14,9,11)=9.
\]

So \(\boxed{9}\).

## Solution 5

At \(A\):

\[
24=8+x+7=15+x.
\]

\[
x=9.
\]

At \(B\):

\[
x+5=y+6.
\]

Substitute \(x=9\):

\[
14=y+6.
\]

\[
y=8.
\]

So:

\[
\boxed{x=9,\quad y=8}.
\]

## Solution 6

\[
9+14+6+11=40.
\]

So \(\boxed{\text{capacity}(C_1)=40}\).

## Solution 7

Include only \(SA,AD,CE\). Therefore:

\[
10+8+5=23.
\]

So \(\boxed{23}\).

## Solution 8

For \(SACT\):

\[
\min(16,10,12)=10.
\]

For \(SBDT\):

\[
\min(15,13,17)=13.
\]

Initial flow value:

\[
10+13=23.
\]

So \(\boxed{23}\).

## Solution 9

\[
\min(6,4,9,5)=4.
\]

New value:

\[
31+4=35.
\]

So:

\[
\boxed{\text{augmenting amount}=4,\quad \text{new flow value}=35}.
\]

## Solution 10

\[
\text{forward}=18-11=7.
\]

\[
\text{backward}=11.
\]

Check:

\[
7+11=18.
\]

So:

\[
\boxed{\text{forward}=7,\quad \text{backward}=11}.
\]

## Solution 11

Cut capacity:

\[
10+8+13+11=42.
\]

The flow value is \(42\). Since the flow value equals the cut capacity, by the maximum flow-minimum cut theorem, the flow is maximal.

## Solution 12

The empty arc going towards the source may be included because it has zero current flow, so it is not freeing up capacity by carrying flow back towards the source.

Cut capacity:

\[
9+12+4=25.
\]

The flow value is \(25\), so the flow is maximal by the maximum flow-minimum cut theorem.

---

# 15. Exam Technique Notes

## 15.1 When asked to find missing flow values

Use conservation. Write:

```text
At vertex D, flow in equals flow out.
```

Then show:

\[
x=5+2=7.
\]

## 15.2 When asked to list saturated arcs

Compare current flow with capacity and list arcs using notation such as:

\[
AB,\ AE,\ DF,\ CF,\ DE.
\]

## 15.3 When asked for the value of a flow

Use total flow out of the source or total flow into the sink.

## 15.4 When asked for the current flow along a route

Take the smallest current flow along the route. Do not add.

## 15.5 When asked for cut capacity

Use capacities crossing from source side to sink side. Do not use circled flow values.

## 15.6 When using the labelling procedure

For each arc:

\[
\text{forward}=c-f,
\]

\[
\text{backward}=f.
\]

Check:

\[
\text{forward}+\text{backward}=c.
\]

## 15.7 When proving maximality

State:

\[
\text{flow value}=F,
\]

\[
\text{cut capacity}=F,
\]

therefore the flow is maximal by the maximum flow-minimum cut theorem.

## 15.8 Exact values and decimals

This topic is usually integer-based. Keep integer values exact.

## 15.9 Calculator use

A calculator can help arithmetic, but the marks usually come from selecting correct arcs, direction, conservation and theorem application.

---

# 16. Syllabus Gap Check

## 16.1 LO coverage table

| LO ID | Official wording | Covered? | Evidence coverage | Notes |
|---|---|---:|---|---|
| `FA22-GRAPH-LO002` | demonstrate understanding of cutsets and use the max-flow min-cut theorem | Yes | Sections 7, 8, 11, 12, 14, 15 | Core theorem and cutset logic taught explicitly |

## 16.2 Supporting-method coverage table

| Supporting method | Covered? | Where |
|---|---:|---|
| Capacitated directed networks | Yes | Sections 6-8 |
| Source and sink | Yes | Sections 7-8 |
| Feasibility condition | Yes | Sections 7-8 |
| Conservation condition | Yes | Sections 7-8, 11 |
| Saturated arcs | Yes | Sections 7, 11, 12 |
| Value of a flow | Yes | Sections 7, 8, 11 |
| Cuts and cut capacities | Yes | Sections 7, 8, 11 |
| Initial flows | Yes | Sections 8, 11 |
| Flow-augmenting routes | Yes | Sections 8, 11 |
| Labelling procedure | Yes | Sections 8, 11, 15 |
| Max-flow min-cut proof | Yes | Sections 8, 11, 14, 15 |

## 16.3 Off-Spec Content Found but Excluded

| Off-spec or boundary-risk item | Status | Reason |
|---|---|---|
| Multiple sources and multiple sinks | Excluded from core | Transcript says this is later material. This lesson keeps to one source and one sink. |
| Full proof of max-flow min-cut theorem | Excluded from core | CCEA wording requires using the theorem, not proving the theorem from first principles. |
| General residual graph theory | Excluded from core | Labelling procedure is taught in evidence style only. |
| Linear programming formulation of max-flow | Excluded | Not in supplied evidence or CCEA boundary for this lesson. |
| Cross-board “D2 Chapter 3” identity | Not used for metadata | Lesson metadata follows CCEA `FA22-GRAPH`. |

## 16.4 Optional Enrichment Not Required by CCEA

- Residual network formal notation.
- Computer implementation of max-flow algorithms.
- Multiple-source/multiple-sink transformations.
- Formal theorem proof.

## 16.5 Weak evidence warnings

- The screenshot PDF is visual-only in this chat and had no parsed text, so visual claims are restricted to visible pages and transcript-supported information.
- The transcript is teacher-spoken and contains occasional wording issues, such as “sync” where the mathematical term is “sink”.
- The transcript references textbook exercises and exam questions, but the original textbook pages and original exam papers were not supplied.

---

# 17. Recommended Enhancements Not in the Evidence

These enhancements are AI-proposed teaching aids based on the supplied evidence. They are not additional CCEA requirements.

## 17.1 Diagrams

1. A clean “capacity versus current flow” network diagram.
2. A colour-free exam version of the labelling procedure.
3. A cut-direction diagram showing why some crossed arcs are counted and some are ignored.
4. A “flow certificate” diagram where the flow value and cut capacity meet at the same number.

## 17.2 Animations

1. Water filling a network until a bottleneck saturates.
2. A moving cut line that dynamically adds capacities.
3. An augmenting route animation showing labels decreasing and increasing.
4. A reverse-arc animation showing flow being cancelled rather than physically reversed.

## 17.3 Widgets

1. Feasibility checker.
2. Cut capacity calculator.
3. Augmenting route trainer.
4. Max-flow min-cut proof builder.

## 17.4 Extra examples

1. A tiny 4-vertex network for first exposure.
2. A medium 6-vertex network with one missing flow value.
3. A cut diagram with two wrong-direction arcs.
4. A theorem-proof question where the cut must include an empty reverse arc.

## 17.5 Bridge visuals

1. Ordinary diagram-reading to network-reading comparison.
2. “Equation from diagram” bridge: from ordinary algebra to vertex conservation.
3. “Inequality from model” bridge: from ordinary constraints to \(f(e)\leq c(e)\).

---

# 18. Supplementary Sources Used

## 18.1 Project Sources used

- `CCEA_GCE_Further_Mathematics_Specification_Map.md`
- `Further_Maths_README_module_map.md`
- `Further_Maths_EVIDENCE_DROP_CHECKLIST.md`
- `Ordinary_A_Level_Maths_Bridge_Spec_Extracts.md`
- `CCEA_GCE_Mathematics_Specification_Map.md`

## 18.2 Lesson-specific evidence used

- `transcripts.md`
- `Chapter_3_Flows_in_Networks_1_⌨️_(Decision_2)_screenshots.pdf`

## 18.3 Ordinary A-Level Maths bridge sources used

Ordinary A-Level Mathematics evidence is used only for bridge context: modelling, diagram interpretation, arithmetic, inequalities, proof and reasoning, and organised multi-step working. It does not override the CCEA Further Mathematics specification.

## 18.4 Cross-board source notes

The lesson-specific transcript uses “D2” and “AS section” language. This is not used as CCEA metadata. It is used only as mathematical teaching evidence where it supports the CCEA Further Mathematics topic `FA22-GRAPH`.

## 18.5 Evidence limitations

- The screenshot PDF contains visual pages but no parsed text, so detailed visual extraction is limited.
- Original textbook pages were not supplied.
- Original CCEA exam papers/mark schemes were not supplied for the transcript’s exam-question segment.

---

# 19. Final Student Checklist

## 19.1 Prerequisite confidence checklist

You are ready for this lesson if you can:

- [ ] read a directed diagram with arrows;
- [ ] add several integers accurately;
- [ ] solve equations such as \(24=15+x\);
- [ ] identify the smallest value in a list;
- [ ] explain a conclusion in words.

## 19.2 Further Maths method checklist

You can handle flows in networks if you can:

- [ ] define a capacitated directed network;
- [ ] identify source and sink;
- [ ] distinguish capacity from current flow;
- [ ] apply \(0\leq f(e)\leq c(e)\);
- [ ] apply conservation at internal vertices;
- [ ] identify saturated arcs;
- [ ] find the value of a flow;
- [ ] calculate cut capacity;
- [ ] ignore wrong-direction arcs in a cut;
- [ ] use the labelling procedure when needed;
- [ ] find an augmenting route;
- [ ] update forward and backward labels;
- [ ] stop when no augmenting route remains;
- [ ] prove maximality using the maximum flow-minimum cut theorem.

## 19.3 Exam technique checklist

Before submitting an answer, check:

- [ ] Did I use capacities for cut capacity?
- [ ] Did I use current flows for flow value?
- [ ] Did I show conservation equations for missing values?
- [ ] Did I list arcs using correct notation?
- [ ] Did I state the theorem when proving maximality?
- [ ] Did I compare flow value and cut capacity explicitly?
- [ ] Did I avoid adding route values when I should take the minimum?
- [ ] Did I check all forward/backward labels add to the original capacity?

## 19.4 Bridge checklist

You should be able to explain:

- [ ] how ordinary diagram reading becomes network interpretation;
- [ ] how ordinary algebra becomes vertex conservation;
- [ ] how ordinary inequalities become capacity constraints;
- [ ] how ordinary proof becomes a max-flow min-cut certificate.

## 19.5 Diagram and visual understanding checklist

You should be able to point to a diagram and say:

- [ ] this is the source;
- [ ] this is the sink;
- [ ] this number is a capacity;
- [ ] this number is a current flow;
- [ ] this arc is saturated;
- [ ] this cut separates source from sink;
- [ ] these arcs contribute to cut capacity;
- [ ] these arcs do not contribute because of direction;
- [ ] this flow is maximal because the cut capacity matches it.
