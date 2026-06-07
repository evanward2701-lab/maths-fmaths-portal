# 1. Lesson Title and Metadata

# Critical Path Analysis

| Field | Value |
|---|---|
| Date generated | 2026-06-04 |
| Course | CCEA GCE Further Mathematics |
| Unit | FAS2: Further AS 2 Applied Mathematics |
| Applied section | Section D: Discrete and Decision Mathematics |
| Specification topic | Algorithms on graphs |
| Topic code | FAS2-ALGGRAPH |
| Topic name | Critical Path Analysis |
| Topic slug | critical_path_analysis |
| Topic Pascal | CriticalPathAnalysis |
| Topic ID | FAS2CriticalPathAnalysis |
| Lesson file name | FAS2_critical_path_analysis_lesson.md |
| Core LO IDs | FAS2-ALGGRAPH-LO002 |
| Supporting LO IDs | FAS2-ALGGRAPH-LO001 |
| Excluded sibling LO IDs | FAS2-ALGGRAPH-LO003, FAS2-ALGGRAPH-LO004, FAS2-ALGGRAPH-LO005 |
| Future extension, not this lesson | FA22-ALGGRAPH-LO002, Program Evaluation and Review Technique |
| Bridge tags | Ordinary A-Level Maths bridge: algebraic organisation, graph interpretation, table reading, inequalities, optimisation thinking, modelling assumptions |
| Topic tags | #FAS2 #ALGGRAPH #Decision #Algorithms #CriticalPath #ActivityNetwork #PrecedenceTable #EventTimes #FloatTimes #CriticalActivities #SectionD |

This lesson covers `FAS2-ALGGRAPH-LO002`: solve problems involving critical path analysis, including a precedence table for an activity network, event times and float times, and an algorithm for finding the critical path. `FAS2-ALGGRAPH-LO001` is used only as supporting context because critical path analysis is an algorithmic procedure.

This lesson does **not** teach Prim's algorithm, Dijkstra's algorithm, binary-tree traversals, PERT probability, resource histograms or scheduling diagrams as required core content.

---

# 2. Evidence Map

| Source | Role | Limitation |
|---|---|---|
| `CCEA_GCE_Further_Mathematics_Specification_Map.md` | Primary authority for `FAS2-ALGGRAPH-LO002`, wording and boundary. | None for this boundary. |
| `Further_Maths_README_module_map.md` | Metadata conventions and lesson-pack workflow. | Project support source. |
| `Further_Maths_EVIDENCE_DROP_CHECKLIST.md` | Evidence checks, missing evidence log, off-spec logging. | Project support source. |
| `Ordinary_A_Level_Maths_Bridge_Spec_Extracts.md` | Bridge context only. | Does not override Further Maths. |
| `Decision Maths 1 chapter 8 Critical Path Analysis (including A2 content) July 22.pdf` | Slide/PDF evidence for precedence tables, activity networks, dummies, event times, critical activities and float. | Cross-board; only on-spec material used as core. |
| `transcripts.md` | Teacher explanation, warnings, shortcuts and worked methods. | Cross-board; only on-spec material used as core. |
| `Chapter_8_Critical_Path_Analysis_💻_(Decision_1)_screenshots.pdf` | Visual reference where visible/readable. | No parsed text; no uninspected detail claimed. |

The uploaded evidence begins from the idea that critical path analysis is used to manage a project, such as planning an event, building a house or producing a car. The project is split into component activities, and some activities depend on the completion of previous activities. A table showing that order is called a dependence table or precedence table.

Core content retained for FAS2: precedence tables, activity-on-arc networks, dummy activities, durations, early/late event times, forward/backward passes, critical activities, critical paths and float times.

Boundary-risk or enrichment: Gantt/cascade charts, lower bounds for workers, resource histograms, scheduling diagrams and PERT probability.

---

# 3. Specification Alignment

| LO ID | Official wording | Lesson coverage | Boundary |
|---|---|---|---|
| FAS2-ALGGRAPH-LO001 | demonstrate understanding of the definition of an algorithm, including the term greedy algorithm | Used only to frame CPA as a repeatable algorithm. | Supporting context only. |
| FAS2-ALGGRAPH-LO002 | solve problems involving critical path analysis, including a precedence table for an activity network, event times and float times, and an algorithm for finding the critical path | Full coverage: precedence tables, networks, dummies, durations, early/late event times, forward/backward pass, critical path and float. | Core. |
| FAS2-ALGGRAPH-LO003 | Prim's algorithm | Not covered. | Excluded. |
| FAS2-ALGGRAPH-LO004 | Binary trees, breadth first search and depth first search | Not covered. | Excluded. |
| FAS2-ALGGRAPH-LO005 | Dijkstra's algorithm | Not covered. | Excluded. |
| FA22-ALGGRAPH-LO002 | PERT probability of project completion | Not covered. | Future extension only. |

---

# 4. Learning Objectives

## 4.1 Core Further Maths Objectives

By the end of this lesson, you should be able to:

1. explain what a project, activity, dependency and precedence table mean;
2. complete a precedence table using only **immediately preceding activities**;
3. draw and interpret an **activity-on-arc network**;
4. identify the source node and sink node;
5. use dummy activities to show dependencies without invalid double edges;
6. add durations to activities;
7. calculate early event times using a forward pass;
8. calculate late event times using a backward pass;
9. identify critical events, activities and paths;
10. calculate float times;
11. interpret which activities can be delayed;
12. present a CPA solution clearly for exam marking.

## 4.2 Bridge Objectives

You should also be able to explain:

1. how ordinary table-reading becomes dependency modelling;
2. how ordinary graph interpretation differs from activity-on-arc modelling;
3. why “list everything that came before” is dangerous;
4. why **immediately preceding** matters;
5. how largest/smallest choices depend on pass direction.

## 4.3 Exam Technique Objectives

You should be able to explain dummies precisely, show pass calculations, avoid the false-critical-activity trap, calculate float with the correct event times, and state critical path plus project duration with units.

---

# 5. Explicit Prerequisite Recap

## 5.1 GCSE Foundations

You need accurate arithmetic, table reading, directed-arrow interpretation, largest/smallest comparisons and language such as before, after, depends on, earliest and latest.

## 5.2 Ordinary AS/A2 Mathematics Foundations

From ordinary A-Level Mathematics, the closest foundations are algebraic organisation, graph interpretation, tables, inequalities/optimisation and applied modelling. There is no direct ordinary A-Level predecessor for critical path analysis.

## 5.3 Previous Further Mathematics Foundations

Useful prior Further Mathematics ideas include vertices/nodes, edges/arcs, directed arcs, paths through a network and algorithms as repeatable procedures.

## 5.4 A-Level Maths Bridge: What You Already Know and What Further Maths Changes

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| Algebra and functions | Use symbols consistently. | Activity letters such as \(A,B,C,\ldots\) label jobs, not variables to solve. | Do not algebraically simplify activity letters. |
| Coordinate/graph interpretation | Interpret points, lines and direction. | Networks are discrete diagrams: arcs are activities, nodes are events. | Positions, lengths and angles have no meaning unless durations are labelled. |
| Data tables | Read headings and rows accurately. | A precedence table records immediate dependency structure. | “Depends on” means immediate predecessors, not all earlier activities. |
| Inequalities/optimisation | Choose maximum or minimum values. | Forward pass takes largest incoming; backward pass takes smallest outgoing-back. | The pass direction controls the choice. |
| Applied modelling | State assumptions and interpret outputs. | CPA models activities, durations and dependencies. | Do not invent real-world dependencies. |

In ordinary A-Level Maths, this idea appeared as reading tables, following graphs and choosing values under conditions. In Further Maths, the same idea becomes an algorithmic project model. A table becomes a network; a network becomes a timing algorithm; the timing algorithm reveals which activities control the whole project.

The key upgrade is that you are not merely calculating a number. You are building a logical machine. The danger is that old habits can be too blunt: listing every earlier activity, drawing curved arrows, or choosing the smallest value because it “feels efficient” will misfire.

---

# 6. Big Picture Explanation

Critical path analysis is about planning a project. A project might be building a house, manufacturing a sofa, producing a car, organising an event or preparing a building site. A project is split into activities. Some activities can begin immediately. Others must wait until previous activities are complete.

CPA answers:

1. What order must the activities happen in?
2. What is the earliest possible completion time?
3. Which activities cannot be delayed?
4. Which activities have spare time?
5. Which chain controls the whole project?

Core idea:

> A project can finish only when every required chain of activities has finished.

So when several paths meet, the project waits for the slowest required path. That is why the forward pass takes the largest value.

When working backwards, we ask how late an event can be left without delaying the project. So when several future paths leave an event, we must satisfy the most urgent future deadline. That is why the backward pass takes the smallest value.

## 6.1 Applied Modelling Context

CPA assumes:

- activities have known durations;
- dependencies are known;
- an activity cannot start until its immediate predecessors are complete;
- the network correctly represents the project;
- dummy activities have zero duration;
- the model ignores uncertainty unless later extended to PERT.

In real life, dependencies can involve judgement. In exam questions, use only the given information.

---

# 7. Key Definitions and Notation

## 7.1 Project

A **project** is a collection of activities that together produce a final outcome.

## 7.2 Activity

An **activity** is one component job in the project. Activities are usually labelled:

\[
A,\ B,\ C,\ D,\ldots
\]

Here, \(A\) is a name, not an algebraic variable.

## 7.3 Precedence Table or Dependence Table

A **precedence table**, also called a **dependence table**, shows which activities must be completed before other activities can start.

| Activity | Immediately preceding activities |
|---|---|
| \(A\) | - |
| \(B\) | \(A\) |
| \(C\) | \(A\) |
| \(D\) | \(B,C\) |

A dash means the activity has no immediate predecessor and can start at the beginning.

## 7.4 Immediately Preceding Activities

The **immediately preceding activities** are the activities that must be completed directly before another activity can start. They are not all activities that happened earlier.

Example:

\[
A\to B\to C
\]

For \(C\), the immediately preceding activity is \(B\), not \(A,B\). Activity \(A\) is already implied because \(B\) cannot happen without \(A\).

## 7.5 Activity-on-Arc Network

In an **activity-on-arc network**:

- arcs/edges represent activities;
- each arc is labelled with an activity letter;
- arrows show direction;
- nodes/vertices represent events;
- an event is the completion of one or more activities;
- arcs are drawn as straight lines by convention.

## 7.6 Source Node and Sink Node

The **source node** is the first node and represents the start of the project. The evidence uses the convention that the first node is numbered \(0\).

The **sink node** is the final node and represents completion of the whole project.

## 7.7 Duration

The **duration** of an activity is the time it takes to complete. \(A(5)\) means activity \(A\) takes 5 time units.

## 7.8 Dummy Activity

A **dummy activity** is a dotted arc used to show dependency. It has:

\[
\text{duration}=0
\]

It is not real work. It carries dependency only and may be needed to avoid invalid double edges.

## 7.9 Unique Representation in Terms of Events

Every activity must be uniquely represented by its start event and finish event. Therefore:

\[
\text{there can be at most one activity between any two events.}
\]

## 7.10 Early Event Time

The **early event time** is the earliest time of arrival at an event, allowing for completion of all preceding activities.

\[
E_i=\text{early event time at event }i
\]

## 7.11 Late Event Time

The **late event time** is the latest time an event can be left without extending the project duration.

\[
L_i=\text{late event time at event }i
\]

## 7.12 Forward and Backward Pass

A **forward pass** calculates early event times from source to sink.

A **backward pass** calculates late event times from sink to source.

## 7.13 Critical Activity and Critical Path

An activity is **critical** if any increase in its duration increases the duration of the whole project.

A **critical path** is a path from source to sink that entirely follows critical activities. There may be more than one.

## 7.14 Float Time

For an activity from event \(i\) to event \(j\) with duration \(d\):

\[
\text{float}=L_j-d-E_i
\]

A critical activity has float \(0\).

---

# 8. Core Theory

## 8.1 From Project to Precedence Table

Suppose:

- \(A\) can start immediately;
- \(B\) depends on \(A\);
- \(C\) depends on \(B\);
- \(D\) depends on \(B\);
- \(E\) can only be completed once all other activities have been completed.

A wrong first attempt for \(E\) is:

\[
E:A,B,C,D
\]

but the table asks for **immediately preceding activities**.

Since \(C\) implies \(B\), and \(B\) implies \(A\), and \(D\) also implies \(B\) and \(A\), it is enough to require:

\[
E:C,D
\]

| Activity | Immediately preceding activities |
|---|---|
| \(A\) | - |
| \(B\) | \(A\) |
| \(C\) | \(B\) |
| \(D\) | \(B\) |
| \(E\) | \(C,D\) |

**Bridge Note:** In ordinary A-Level Maths, a table row often gives a value. Here each row is a dependency rule.

### Shortcut for a Final Activity

If an activity \(G\) can only be completed once all other activities are complete, look for activities not already represented in the dependency column.

Example:

| Activity | Immediately preceding activities |
|---|---|
| \(A\) | - |
| \(B\) | - |
| \(C\) | \(A\) |
| \(D\) | \(A\) |
| \(E\) | \(B\) |
| \(F\) | \(C,E\) |
| \(G\) | ? |

The activities before \(G\) are \(A,B,C,D,E,F\). Already written in the dependency column are \(A,B,C,E\). Missing are \(D,F\), so:

\[
G:D,F
\]

This shortcut applies only when the activity must wait for **all other activities**.

## 8.2 Drawing Activity-on-Arc Networks

Rules:

1. Start with a source node.
2. Activities with no predecessors leave the source.
3. Draw a new node when an activity has completed and another activity starts from that completion.
4. Label each arc with the activity letter.
5. Use arrows to show direction.
6. Use straight lines.
7. Avoid crossings where possible.
8. Finish at one sink node.

Practical advice: use pencil, expect to redraw, swap branches when needed, and check every activity against the precedence table.

## 8.3 Reading Dependencies from a Network

To find the immediate predecessors of activity \(X\):

1. find activity \(X\);
2. look at the start node of \(X\);
3. list all real activities entering that node;
4. include any dependency carried by dummies.

**Bridge Note:** Ordinary graph interpretation becomes stricter here: you follow arrows into an event node to read dependency.

## 8.4 Dummy Activities

Dummies are needed when dependency cannot be shown correctly using only real activities.

Suppose:

| Activity | Depends on |
|---|---|
| \(A\) | - |
| \(B\) | - |
| \(C\) | \(A,B\) |
| \(D\) | \(A\) |

Activity \(D\) depends only on \(A\), while \(C\) depends on both \(A\) and \(B\). A dummy can carry the fact that \(A\) is complete into the event where \(C\) starts, without making \(C\) depend on \(D\).

Exam wording:

> The dummy is needed to show that \(C\) depends on \(A\) as well as \(B\), while \(D\) depends only on \(A\).

Another use:

> The dummy is needed so that activities are uniquely represented in terms of their events, avoiding two activities between the same pair of events.

## 8.5 Event-Time Boxes

Use a two-part event-time box:

\[
\begin{array}{|c|}
\hline
E_i\\
\hline
L_i\\
\hline
\end{array}
\]

Top = early event time. Bottom = late event time.

The source has \(E=0\). The sink has:

\[
E_{\text{sink}}=L_{\text{sink}}
\]

## 8.6 Forward Pass

A forward pass calculates early event times.

For an activity from event \(i\) to event \(j\) with duration \(d\):

\[
E_j=\max(E_i+d)
\]

over all incoming activities.

Choose the largest because an event cannot occur until all incoming required activities are complete.

Example:

\[
\max(4+5,\;6+3)=\max(9,9)=9
\]

A dummy has duration \(0\), so through a dummy:

\[
E_i+0=E_i
\]

## 8.7 Backward Pass

A backward pass calculates late event times.

Set:

\[
L_{\text{sink}}=E_{\text{sink}}
\]

For an activity from \(i\) to \(j\) with duration \(d\):

\[
L_i=\min(L_j-d)
\]

over all outgoing activities when working backwards.

Choose the smallest because the event must satisfy the strictest future deadline.

Example:

\[
\min(9-3,\;16-8)=\min(6,8)=6
\]

## 8.8 Critical Path Algorithm

1. Draw/use the activity-on-arc network.
2. Add durations.
3. Perform the forward pass.
4. Perform the backward pass.
5. Find events where \(E_i=L_i\).
6. Check activities using:
   \[
   E_i+d=E_j
   \]
7. List critical activities.
8. Trace the critical path from source to sink.
9. State project duration.

Minimum project completion time is:

\[
E_{\text{sink}}=L_{\text{sink}}
\]

## 8.9 Critical Events and Critical Activities

A critical event has:

\[
E_i=L_i
\]

A critical activity from \(i\) to \(j\) with duration \(d\) must satisfy:

\[
E_i+d=E_j
\]

### Major Warning

Not all activities joining critical events are critical.

Example:

\[
E_i=L_i=16,\quad E_j=L_j=22,\quad d=5
\]

Then:

\[
16+5=21\neq 22
\]

so the activity is not critical.

## 8.10 Float Times

For an activity from \(i\) to \(j\):

\[
\text{float}=L_j-d-E_i
\]

This comes from:

\[
\text{available window}=L_j-E_i
\]

\[
\text{spare time}=L_j-E_i-d
\]

So:

\[
\text{float}=L_j-d-E_i
\]

A critical activity has float \(0\).

## 8.11 Summary Algorithm Table

| Task | Method | Choice rule |
|---|---|---|
| Precedence table | List immediate predecessors | Do not list implied earlier activities |
| Network | Activities are arcs; events are nodes | Use dummies where needed |
| Forward pass | Add source to sink | Choose largest incoming value |
| Backward pass | Subtract sink to source | Choose smallest outgoing-back value |
| Critical path | Check event times and durations | Do not rely only on equal endpoints |
| Float | \(L_j-d-E_i\) | Zero float means critical |

## 8.12 What Is Not Core Here

The uploaded evidence includes Gantt charts, lower bounds for workers, resource histograms and scheduling diagrams. These are not treated as required core under the supplied CCEA FAS2 CPA LO.

---

# 9. Visual Asset Integration

Diagram evidence is partially unclear where it depends on the screenshot PDF. The screenshot PDF had no parsed text; no uninspected visual detail is claimed.

[VISUAL PLACEHOLDER: FAS2CriticalPathAnalysisMermaid-001 | Source: CCEA FAS2 critical path analysis LO + uploaded CPA slides/transcript | Insert from mermaid/FAS2CriticalPathAnalysisMermaid-001.md | Purpose: Show the overall critical path analysis workflow from project activities to precedence table, activity network, event times, float and critical path.]

[VISUAL PLACEHOLDER: FAS2CriticalPathAnalysisSVG-001 | Source: Uploaded activity-on-arc network definitions | Insert from svg/FAS2CriticalPathAnalysisSVG-001.svg | Purpose: Identify the basic parts of an activity-on-arc network.]

[VISUAL PLACEHOLDER: FAS2CriticalPathAnalysisSVG-002 | Source: Uploaded early/late event time slides and transcript | Insert from svg/FAS2CriticalPathAnalysisSVG-002.svg | Purpose: Show how event-time boxes are read during the forward and backward pass.]

[VISUAL PLACEHOLDER: FAS2CriticalPathAnalysisSVG-003 | Source: Uploaded dummy activity and unique representation slides | Insert from svg/FAS2CriticalPathAnalysisSVG-003.svg | Purpose: Compare an invalid double-edge network with a valid dummy-activity network.]

[VISUAL PLACEHOLDER: FAS2CriticalPathAnalysisBridgeSVG-001 | Source: Ordinary A-Level Maths bridge + Further Maths specification | Insert from svg/FAS2CriticalPathAnalysisBridgeSVG-001.svg | Purpose: Compare prior ordinary Maths method with Further Maths extension.]

[VISUAL PLACEHOLDER: FAS2CriticalPathAnalysisTikZ-001 | Source: Uploaded CPA slides/transcript, AI-redrawn for clarity | Insert from tikz/FAS2CriticalPathAnalysisTikZ-001.tex | Purpose: Provide a precise activity-on-arc network with durations and event-time boxes for print/PDF use.]

Visual palette: `#FAF9F6`, `#FFFFF0`, `#E5E5EA`, `#C5A059`, `#D4AF37`, `#FBEFEF`, `#2C2C2E`.

---

# 10. Interactive Learning Widgets

[INTERACTIVE PLACEHOLDER: FAS2CriticalPathAnalysisWidget-001 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FAS2CriticalPathAnalysisWidget-001.html | Purpose: Help the student practise completing precedence tables using immediate predecessors only.]

[INTERACTIVE PLACEHOLDER: FAS2CriticalPathAnalysisWidget-002 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FAS2CriticalPathAnalysisWidget-002.html | Purpose: Let the student practise early and late event time calculations.]

[INTERACTIVE PLACEHOLDER: FAS2CriticalPathAnalysisWidget-003 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FAS2CriticalPathAnalysisWidget-003.html | Purpose: Help the student calculate float and identify critical activities.]

---

# 11. Worked Examples

## 11.1 Sofa Precedence Table

Activities:

| Activity | Meaning |
|---|---|
| \(A\) | build wooden frame |
| \(B\) | cut out fabric for cushions |
| \(C\) | stitch and fill cushions |
| \(D\) | attach springs to frame |
| \(E\) | cover frame |
| \(F\) | complete assembly |
| \(G\) | inspect |
| \(H\) | wrap |

Precedence table:

| Activity | Immediately preceding activities |
|---|---|
| \(A\) | - |
| \(B\) | - |
| \(C\) | \(B\) |
| \(D\) | \(A\) |
| \(E\) | \(D\) |
| \(F\) | \(C,E\) |
| \(G\) | \(F\) |
| \(H\) | \(G\) |

Explanation:

- \(A\) and \(B\) can begin immediately.
- \(C\) starts after \(B\).
- \(D\) starts after \(A\).
- \(E\) starts after \(D\).
- \(F\) starts only after both \(C\) and \(E\).
- \(G\) starts after \(F\).
- \(H\) starts after \(G\).

Final chain after assembly:

\[
F\to G\to H
\]

Teaching note: \(E\) lists \(D\), not \(A,D\), because \(A\) is already implied by \(D\).

## 11.2 Completing a Final Activity Row

Table:

| Activity | Immediately preceding activities |
|---|---|
| \(A\) | - |
| \(B\) | \(A\) |
| \(C\) | \(B\) |
| \(D\) | \(B\) |
| \(E\) | ? |

Given \(E\) can only be completed once all other activities are complete.

The activities before \(E\) are \(A,B,C,D\). Since \(C\) implies \(B,A\), and \(D\) implies \(B,A\), the immediate predecessors are:

\[
\boxed{C,D}
\]

## 11.3 Missing Letters Shortcut

Table:

| Activity | Immediately preceding activities |
|---|---|
| \(A\) | - |
| \(B\) | - |
| \(C\) | \(A\) |
| \(D\) | \(A\) |
| \(E\) | \(B\) |
| \(F\) | \(C,E\) |
| \(G\) | ? |

Since \(G\) waits for all other activities, check which activities are not yet written in the dependency column. Written: \(A,B,C,E\). Missing: \(D,F\). Therefore:

\[
\boxed{G:D,F}
\]

## 11.4 Drawing an Activity-on-Arc Network

For:

| Activity | Depends on |
|---|---|
| \(A\) | - |
| \(B\) | \(A\) |
| \(C\) | \(A\) |
| \(D\) | \(B\) |
| \(E\) | \(C\) |
| \(F\) | \(E\) |
| \(G\) | \(C\) |
| \(H\) | \(D,F\) |
| \(I\) | \(G\) |
| \(J\) | \(G\) |
| \(K\) | \(I\) |
| \(L\) | \(J\) |

A correct network has:

- \(A\) leaving the source;
- \(B,C\) after \(A\);
- \(D\) after \(B\);
- \(E,G\) after \(C\);
- \(F\) after \(E\);
- \(H\) after both \(D\) and \(F\);
- \(I,J\) after \(G\);
- \(K\) after \(I\);
- \(L\) after \(J\);
- \(H,K,L\) finishing at the sink.

## 11.5 Explaining a Dummy Activity

Table:

| Activity | Meaning | Depends on |
|---|---|---|
| \(A\) | put key in ignition | - |
| \(B\) | put on seatbelt | - |
| \(C\) | drive away | \(A,B\) |
| \(D\) | turn radio on | \(A\) |

A dummy is needed to show that \(C\) depends on both \(A\) and \(B\), while \(D\) depends only on \(A\). The dummy has zero duration and represents dependency only.

## 11.6 Unique Representation and Double Edges

For:

| Activity | Meaning | Depends on |
|---|---|---|
| \(A\) | put on socks | - |
| \(B\) | put on trousers | - |
| \(C\) | put on shoes | \(A,B\) |

Drawing \(A\) and \(B\) as two arcs between the same pair of events is invalid because every activity must be uniquely represented by its start and finish events. A dummy is required so that there is at most one activity between any two events.

## 11.7 Forward Pass Example

Start:

\[
E_{\text{source}}=0
\]

If possible incoming times to an event are:

\[
3,\quad 5
\]

then:

\[
E=\max(3,5)=5
\]

If possible incoming times are:

\[
12,\quad 10,\quad 13
\]

then:

\[
E=\max(12,10,13)=13
\]

## 11.8 Backward Pass Example

If project duration is \(24\), then at the sink:

\[
L_{\text{sink}}=24
\]

If an activity \(J(6)\) enters the sink from event \(x\):

\[
L_x=24-6=18
\]

If possible latest departure times are:

\[
18,\quad 15
\]

then:

\[
L=\min(18,15)=15
\]

## 11.9 Critical Path Example

Path:

\[
C-D-G-I-J
\]

Durations:

\[
C(3),\quad D(6),\quad G(4),\quad I(5),\quad J(6)
\]

Total:

\[
3+6+4+5+6=24
\]

So the critical path is:

\[
\boxed{C-D-G-I-J}
\]

and the minimum project completion time is:

\[
\boxed{24}
\]

## 11.10 Float Table Example

Use:

\[
\text{float}=L_j-d-E_i
\]

| Activity | Latest finish \(L_j\) | Duration \(d\) | Earliest start \(E_i\) | Float |
|---|---:|---:|---:|---:|
| \(A\) | 5 | 3 | 0 | \(5-3-0=2\) |
| \(B\) | 5 | 5 | 0 | \(5-5-0=0\) |
| \(C\) | 11 | 6 | 5 | \(11-6-5=0\) |
| \(D\) | 21 | 7 | 5 | \(21-7-5=9\) |
| \(E\) | 21 | 3 | 5 | \(21-3-5=13\) |
| \(F\) | 21 | 10 | 11 | \(21-10-11=0\) |
| \(G\) | 29 | 2 | 12 | \(29-2-12=15\) |
| \(H\) | 30 | 1 | 14 | \(30-1-14=15\) |
| \(I\) | 30 | 9 | 21 | \(30-9-21=0\) |

Critical activities:

\[
\boxed{B,\ C,\ F,\ I}
\]

---

# 12. Common Mistakes and Exam Traps

## 12.1 Listing All Previous Activities

Wrong:

\[
E:A,B,C,D
\]

when \(E\) only immediately depends on:

\[
C,D
\]

## 12.2 Ignoring “Immediately”

The word **immediately** controls the answer. A precedence table is not a family tree of every ancestor activity.

## 12.3 Drawing Activities as Nodes

In activity-on-arc networks, activities are arcs and events are nodes.

## 12.4 Forgetting Arrows

Every activity arc should show direction.

## 12.5 Drawing Curved Arcs

Use straight lines. If the drawing becomes tangled, redraw rather than curl arcs around the problem like spaghetti seeking revenge.

## 12.6 Drawing Double Edges

There can be at most one activity between any two events.

## 12.7 Treating a Dummy as Real Work

A dummy has duration \(0\). It carries dependency only.

## 12.8 Forgetting That a Dummy Can Affect Event Times

A dummy has zero duration but can carry a large early time into another event:

\[
E_i+0=E_i
\]

## 12.9 Forward/Backward Pass Reversal

Forward pass:

\[
E_j=\max(E_i+d)
\]

Backward pass:

\[
L_i=\min(L_j-d)
\]

## 12.10 Assuming Critical Endpoints Are Enough

An activity between two critical events is not automatically critical. Check:

\[
E_i+d=E_j
\]

## 12.11 Forgetting Units

State days, hours or weeks if supplied.

## 12.12 Importing Real-World Judgement

Do not invent dependencies. Use only the question data.

---

# 13. Practice Questions

These are AI-generated on-spec practice questions. They are not past-paper questions and not textbook questions.

## 13.1 Basic Fluency

1. Complete the missing row:
   | Activity | Immediately preceding activities |
   |---|---|
   | \(A\) | - |
   | \(B\) | \(A\) |
   | \(C\) | \(A\) |
   | \(D\) | \(B,C\) |
   | \(E\) | ? |
   Activity \(E\) waits for all other activities.

2. Explain what a dash means in a precedence table.

3. In an activity-on-arc network, state what is represented by an arc, a node, the source and the sink.

## 13.2 Bridge Questions

4. A student says, “If \(F\) happens last, I should write every other activity in row \(F\).” Explain why this may be wrong.

5. A forward pass reaches an event by values \(8,11,9\). What early event time is recorded and why?

6. A backward pass gives possible latest departure times \(14,10,12\). What late event time is recorded and why?

## 13.3 Exam-Style Questions

7. Complete this precedence table from the data:
   - \(A,B\) can start immediately;
   - \(C\) depends on \(A\);
   - \(D\) depends on \(B,C\);
   - \(E\) depends on \(D\);
   - \(F\) depends on \(E\);
   - \(G\) depends on \(F\).

8. Draw an activity-on-arc network for:
   | Activity | Immediately preceding activities |
   |---|---|
   | \(A\) | - |
   | \(B\) | - |
   | \(C\) | \(A\) |
   | \(D\) | \(B\) |
   | \(E\) | \(C,D\) |
   | \(F\) | \(C,D\) |
   Use a dummy if needed.

9. Explain why a dummy may be needed in Question 8.

10. For the network:
   | Activity | From | To | Duration |
   |---|---:|---:|---:|
   | \(A\) | 0 | 1 | 4 |
   | \(B\) | 0 | 2 | 6 |
   | \(C\) | 1 | 3 | 5 |
   | \(D\) | 2 | 3 | 3 |
   | \(E\) | 3 | 4 | 7 |
   | \(F\) | 2 | 4 | 8 |
   calculate all early and late event times.

11. For Question 10, find the critical path, project duration and floats.

12. For:
   | Activity | From | To | Duration |
   |---|---:|---:|---:|
   | \(A\) | 0 | 1 | 5 |
   | \(B\) | 0 | 2 | 4 |
   | \(C\) | 1 | 3 | 4 |
   | \(D\) | 2 | 3 | 5 |
   | \(E\) | 3 | 4 | 6 |
   | \(F\) | 1 | 4 | 7 |
   calculate event times, critical paths and float of \(F\).

13. Given \(E_i=L_i=10\), \(E_j=L_j=18\), and activity \(X\) has duration \(6\), decide whether \(X\) is critical.

---

# 14. Worked Solutions

## 14.1 Solution 1

Since \(D\) depends on \(B,C\), and \(B,C\) imply \(A\), completion of \(D\) implies all previous activities are complete. Therefore:

\[
\boxed{E:D}
\]

## 14.2 Solution 2

A dash means the activity has no immediately preceding activities and can start at the beginning.

## 14.3 Solution 3

Arc = activity. Node = event. Source = start of project. Sink = completion of project.

## 14.4 Solution 4

The row should list direct dependencies only. In \(A\to B\to C\to F\), \(F\)'s immediate predecessor is \(C\), not \(A,B,C\).

## 14.5 Solution 5

Forward pass chooses the largest:

\[
\max(8,11,9)=11
\]

because the event must wait for all incoming activities.

## 14.6 Solution 6

Backward pass chooses the smallest:

\[
\min(14,10,12)=10
\]

because it must satisfy the strictest future deadline.

## 14.7 Solution 7

| Activity | Immediately preceding activities |
|---|---|
| \(A\) | - |
| \(B\) | - |
| \(C\) | \(A\) |
| \(D\) | \(B,C\) |
| \(E\) | \(D\) |
| \(F\) | \(E\) |
| \(G\) | \(F\) |

## 14.8 Solution 8

A valid network has \(A,B\) from the source, \(C\) after \(A\), \(D\) after \(B\), a dummy carrying the missing dependency so that \(E,F\) both depend on \(C,D\), and \(E,F\) finishing at the sink.

## 14.9 Solution 9

The dummy is needed to show that \(E,F\) depend on both \(C,D\), while keeping each activity uniquely represented in terms of its events.

## 14.10 Solution 10

Forward pass:

\[
E_0=0
\]

\[
E_1=0+4=4
\]

\[
E_2=0+6=6
\]

\[
E_3=\max(4+5,\;6+3)=\max(9,9)=9
\]

\[
E_4=\max(9+7,\;6+8)=\max(16,14)=16
\]

Backward pass:

\[
L_4=16
\]

\[
L_3=16-7=9
\]

\[
L_2=\min(9-3,\;16-8)=\min(6,8)=6
\]

\[
L_1=9-5=4
\]

\[
L_0=\min(4-4,\;6-6)=0
\]

Completed table:

| Event | Early \(E_i\) | Late \(L_i\) |
|---|---:|---:|
| 0 | 0 | 0 |
| 1 | 4 | 4 |
| 2 | 6 | 6 |
| 3 | 9 | 9 |
| 4 | 16 | 16 |

## 14.11 Solution 11

Critical activities:

\[
A,\ B,\ C,\ D,\ E
\]

Non-critical:

\[
F
\]

Critical paths:

\[
A-C-E
\]

and

\[
B-D-E
\]

Project duration:

\[
16
\]

Floats:

\[
\text{float}_A=4-4-0=0
\]

\[
\text{float}_B=6-6-0=0
\]

\[
\text{float}_C=9-5-4=0
\]

\[
\text{float}_D=9-3-6=0
\]

\[
\text{float}_E=16-7-9=0
\]

\[
\text{float}_F=16-8-6=2
\]

## 14.12 Solution 12

Forward pass:

\[
E_0=0,\quad E_1=5,\quad E_2=4
\]

\[
E_3=\max(5+4,\;4+5)=9
\]

\[
E_4=\max(9+6,\;5+7)=15
\]

Backward pass:

\[
L_4=15,\quad L_3=15-6=9
\]

\[
L_1=\min(9-4,\;15-7)=\min(5,8)=5
\]

\[
L_2=9-5=4
\]

\[
L_0=\min(5-5,\;4-4)=0
\]

Critical paths:

\[
A-C-E
\]

and

\[
B-D-E
\]

Float of \(F\):

\[
15-7-5=3
\]

## 14.13 Solution 13

Check:

\[
E_i+d=10+6=16
\]

but:

\[
E_j=18
\]

So \(X\) is not critical.

Float:

\[
18-6-10=2
\]

---

# 15. Exam Technique Notes

1. Start with the precedence table, not the drawing.
2. Use immediate precedence language.
3. Check every network backwards from each activity's start node.
4. Explain dummies specifically: say what dependency they carry.
5. Forward pass layout:
   \[
   E_j=\max(E_i+d)
   \]
6. Backward pass layout:
   \[
   L_i=\min(L_j-d)
   \]
7. Memory hook: forward = add and choose largest; backward = subtract and choose smallest.
8. For critical activities, check:
   \[
   E_i+d=E_j
   \]
9. Float:
   \[
   L_j-d-E_i
   \]
10. State units.
11. Do not invent dependencies.
12. Use pencil for networks.
13. A full answer usually includes table/network, event times, project duration, critical path, floats and interpretation.

---

# 16. Syllabus Gap Check

## 16.1 LO Coverage Table

| LO ID | Requirement | Covered? |
|---|---|---:|
| FAS2-ALGGRAPH-LO001 | Definition of algorithm, including greedy algorithm | Partial support only |
| FAS2-ALGGRAPH-LO002 | CPA: precedence table, activity network, event times, float times, critical path algorithm | Yes |
| FAS2-ALGGRAPH-LO003 | Prim's algorithm | No |
| FAS2-ALGGRAPH-LO004 | Binary trees, BFS, DFS | No |
| FAS2-ALGGRAPH-LO005 | Dijkstra's algorithm | No |
| FA22-ALGGRAPH-LO002 | PERT probability | No |

## 16.2 Evidence Coverage Table

| Evidence item | Covered? |
|---|---:|
| Project management context | Yes |
| Precedence/dependence tables | Yes |
| Immediate preceding activities | Yes |
| Activity-on-arc networks | Yes |
| Source and sink | Yes |
| Straight-line arcs and arrows | Yes |
| Dummy activities | Yes |
| Unique representation | Yes |
| Durations | Yes |
| Early/late event times | Yes |
| Forward/backward pass | Yes |
| Critical activities/path | Yes |
| Float times | Yes |
| Gantt/cascade charts | Boundary only |
| Resource histograms | Excluded |
| Scheduling diagrams | Excluded |

## 16.3 Bridge Coverage Table

| Bridge idea | Covered? |
|---|---:|
| Table-reading becomes dependency modelling | Yes |
| Graph interpretation becomes activity-on-arc modelling | Yes |
| Max/min choices become algorithmic rules | Yes |
| Modelling assumptions carry over | Yes |
| Old habits become risky | Yes |

## 16.4 Off-Spec Content Found but Excluded

| Content | Reason excluded |
|---|---|
| Resource histograms | Uploaded evidence labels them as A2-style; not in supplied FAS2 CPA LO. |
| Scheduling diagrams | Not in supplied FAS2 CPA LO. |
| Resource levelling | Beyond core FAS2 CPA wording. |
| PERT probability | FA22 extension, not FAS2. |
| Prim, Dijkstra, binary tree traversal | Separate FAS2 LOs. |

## 16.5 Missing Evidence Log

| Missing evidence | Impact |
|---|---|
| Direct CCEA CPA past-paper questions and mark schemes | Generated questions are not labelled as past-paper. |
| Full direct visual inspection of all 150 screenshot pages | Some visual details may be absent. |
| Direct Pearson textbook page extracts | Textbook wording cannot be independently verified beyond slide/transcript evidence. |

---

# 17. Recommended Enhancements Not in the Evidence

AI-proposed enhancements:

- CPA workflow diagram;
- activity-on-arc anatomy diagram;
- early/late event-time diagram;
- dummy activity comparison;
- ordinary-to-Further bridge diagram;
- printable TikZ activity network;
- precedence table builder widget;
- forward/backward pass checker;
- float and critical path checker.

Optional future enrichment:

- Gantt/cascade chart interpretation;
- lower bound for workers;
- resource histograms;
- scheduling diagrams;
- PERT probability for FA22.

---

# 18. Supplementary Sources Used

Project sources used:

- `CCEA_GCE_Further_Mathematics_Specification_Map.md`;
- `Further_Maths_README_module_map.md`;
- `Further_Maths_EVIDENCE_DROP_CHECKLIST.md`;
- `Ordinary_A_Level_Maths_Bridge_Spec_Extracts.md`.

Lesson-specific sources used:

- `Decision Maths 1 chapter 8 Critical Path Analysis (including A2 content) July 22.pdf`;
- `transcripts.md`;
- `Chapter_8_Critical_Path_Analysis_💻_(Decision_1)_screenshots.pdf`.

Ordinary A-Level Mathematics sources are labelled as bridge context only, not Further Maths authority.

Cross-board source note: uploaded evidence is Decision 1/Edexcel/Pearson-style material. It is used only where it matches the CCEA FAS2 CPA boundary.

Final evidence boundary statement: this lesson is restricted to precedence tables, activity networks, event times, float times and the algorithm for finding the critical path.

---

# 19. Final Student Checklist

## 19.1 Prerequisite Confidence Checklist

- [ ] I can read a table accurately.
- [ ] I can follow arrows in a directed diagram.
- [ ] I can distinguish largest from smallest choices.
- [ ] I can add and subtract durations accurately.
- [ ] I can keep units attached to final answers.
- [ ] I can explain what a model assumption is.

## 19.2 Further Maths Method Checklist

- [ ] I can define a project activity.
- [ ] I can define a precedence table.
- [ ] I can explain immediately preceding activities.
- [ ] I can complete missing precedence table rows.
- [ ] I can draw an activity-on-arc network.
- [ ] I can identify source and sink nodes.
- [ ] I can explain arcs and nodes.
- [ ] I can use dummy activities.
- [ ] I can explain the purpose of a dummy.
- [ ] I can avoid double edges.
- [ ] I can complete a forward pass.
- [ ] I can complete a backward pass.
- [ ] I can identify critical activities.
- [ ] I can find the critical path.
- [ ] I can calculate total float.

## 19.3 Exam Technique Checklist

- [ ] Immediate predecessors only.
- [ ] Activities are arcs.
- [ ] Events are nodes.
- [ ] Dummies have duration \(0\).
- [ ] Forward pass: add and choose largest.
- [ ] Backward pass: subtract and choose smallest.
- [ ] Sink early time equals sink late time.
- [ ] Source early and late times are usually \(0\).
- [ ] Activity between critical events may be non-critical.
- [ ] Float formula is \(L_j-d-E_i\).
- [ ] Zero float means critical.
- [ ] Always state project duration with units.

## 19.4 Final Self-Test

1. What does a dash mean in a precedence table?
2. What is the difference between a predecessor and an immediately preceding activity?
3. In activity-on-arc, what does an arc represent?
4. What does a node represent?
5. Why might a dummy be necessary?
6. Why does a dummy have duration \(0\)?
7. In a forward pass, why choose the largest value?
8. In a backward pass, why choose the smallest value?
9. What is a critical activity?
10. What is the formula for float?
11. Why is an activity between critical events not automatically critical?
12. What does the sink event time tell you?

You have completed the lesson when you can take a project description, build its precedence table, draw its activity-on-arc network, calculate early and late event times, find floats, and state the critical path with the minimum project duration. 🧭
