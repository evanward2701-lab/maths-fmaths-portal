# Dynamic Programming
## Off-Spec Enrichment Lesson for CCEA Further Mathematics Boundary Context

> **Boundary warning:** This lesson is based on supplied **Decision 2 Dynamic Programming** evidence. It is **not listed as a core CCEA GCE Further Mathematics topic** in the supplied CCEA Further Mathematics specification map. Use this lesson as enrichment or cross-board background only, not as required CCEA revision unless an official CCEA Dynamic Programming LO is later supplied.

# 1. Lesson Title and Metadata

| Field | Value |
|---|---|
| Date generated | 2026-06-05 |
| Course | CCEA GCE Further Mathematics portal, enrichment boundary file |
| Official CCEA status | Off-spec enrichment |
| Nearest CCEA unit for boundary context | `FA22` Further A2 2 Applied Mathematics |
| Nearest applied section | Section D: Discrete and Decision Mathematics |
| Official CCEA topic code | Not available |
| Evidence-supported topic name | Dynamic Programming |
| Topic slug | `dynamic_programming_off_spec_enrichment` |
| Topic Pascal | `DynamicProgrammingOffSpecEnrichment` |
| Topic ID | `FA22DynamicProgrammingOffSpecEnrichment` |
| Lesson file name | `FA22_dynamic_programming_off_spec_enrichment_lesson.md` |
| Official CCEA LO IDs | None found |
| Evidence topic identity | D2 Chapter 5: Dynamic Programming |
| Evidence subtopics | Bellman’s principle, shortest/longest paths, minimax/maximin, table-form dynamic programming |

## LO ID Notice

No official CCEA Further Mathematics LO ID has been found for Dynamic Programming in the supplied specification map. Therefore no LO ID is invented, no transcript content is promoted to CCEA core, and all dynamic programming methods are labelled as enrichment.

# 2. Evidence Map

| Source | Evidence type | What it contributes | Use |
|---|---|---|---|
| CCEA GCE Further Mathematics Specification Map | Project Source | Confirms no official Dynamic Programming LO was found | Boundary control |
| Further Maths README module map | Project Source | Metadata, workflow, LO preservation rules | Workflow control |
| Further Maths Evidence Drop Checklist | Project Source | Missing evidence and off-spec logging rules | Quality control |
| Ordinary A-Level Maths Bridge Extracts | Project Source | Bridge context only | Bridge context |
| CCEA GCE Mathematics Specification Map | Project Source | Ordinary Maths bridge support | Bridge context only |
| `transcripts.md` | Lesson-specific transcript | Definitions, examples, warnings, terminology and methods | Main enrichment content |
| `Chapter_5_Dynamic_Programming_⌨️_(Decision_2)_screenshots.pdf` | Visual PDF | Staged networks, tables, title pages and handwritten visual working | Visual evidence with limitations |

**Visual evidence limitation:** the screenshot PDF is visual-only in parsed form. This lesson and asset plan preserve visible/readable and transcript-confirmed details only. No uninspected visual detail is claimed.

# 3. Specification Alignment

| Official CCEA LO ID | Official wording | Lesson coverage | Evidence source | Syllabus boundary | Ordinary A-Level Maths bridge |
|---|---|---|---|---|---|
| None found | No official CCEA Dynamic Programming LO found | No core CCEA coverage claimed | Supplied transcript and visual PDF only | Off-spec enrichment | Arithmetic, tables, graph reading, optimisation, recursive thinking |

Nearby CCEA areas include graph theory and algorithms on graphs, but these do not authorise Dynamic Programming as core CCEA content. In a CCEA Dijkstra question, use Dijkstra’s algorithm, not dynamic programming.

# 4. Learning Objectives

## Core enrichment objectives

By the end of this off-spec enrichment lesson, the student should be able to explain Dynamic Programming as working backwards systematically, describe Bellman’s principle of optimality, complete shortest/longest path tables, distinguish minimax from maximin, complete table-form dynamic programming rows, trace starred choices forwards, and interpret routes, strategies, schedules and allocations.

## Bridge objectives

The student should connect the topic to exact arithmetic, table reading, graph interpretation, recursive/iterative thinking and applied interpretation.

## Exam technique objectives

For cross-board style questions only, the student should set out tables clearly, star optimal values, include tied routes, trace stars forwards and convert units.

# 5. Explicit Prerequisite Recap

GCSE and ordinary A-Level foundations include integer arithmetic, comparison, table reading, directed graph reading, units, applied modelling and recurrence-style thinking.

### A-Level Maths Bridge: What You Already Know and What Further Maths Changes

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| AS/A2 arithmetic | Substitute, add and compare exact numbers | Candidate values are repeatedly calculated and compared | One arithmetic slip can redirect the route |
| Graph/table interpretation | Read labelled diagrams and tables | Directed staged networks with state/action/destination/value columns | Do not follow an edge backwards unless allowed |
| Recursive or iterative thinking | Later values can depend on earlier values | DP works backwards using already-computed future values | Students may look forwards too early |
| Applied Maths modelling | Interpret units and constraints | Routes become business strategies, schedules or allocations | A number alone may not answer the question |

In ordinary A-Level Maths, this idea appeared as table work, graph reading and exact comparison. In Dynamic Programming, the same habits become a formal backwards optimisation method. The key upgrade is that best future values are reused. The danger is that “try a route and see” becomes too risky when many decisions are chained.

# 6. Big Picture Explanation

Dynamic Programming solves optimisation problems by working backwards systematically. The evidence describes it as a management tool developed in the 1950s, associated with Richard Bellman, for production planning, machine scheduling, resource allocation and efficient decision-making.

Instead of guessing a full route from the beginning, solve the final stage first, record the best continuation from each state, move one stage backwards, reuse the starred values already found, and continue until the source. Then trace the stars forwards.

The supplied evidence covers three main families: shortest/longest path problems, minimax/maximin problems, and table-form resource problems.

# 7. Key Definitions and Notation

A **source** is the starting vertex, usually `S`. A **sink** is the final vertex, usually `T`. A **route** or **path** is a sequence of connected vertices such as `SAEIT`. An **arc** is a directed movement such as `AE`. A **weight** is the value attached to an arc.

A **stage** is how many moves away from the sink in a network, or a time period/product/resource category in a table-form problem. A **state** is the current vertex or current resource situation. An **action** is the movement or decision. A **destination** is where the action takes us. A **value** is the quantity being optimised. A **starred value** is the optimal value for a state.

**Bellman’s principle of optimality:** any part of an optimal path is an optimal path. If the shortest route is `SABCT`, then `SABC`, `SAB`, `SA` and `ABC` are optimal subpaths between their respective endpoints.

A **minimax** problem minimises the maximum arc value:

```math
V(X)=\min_Y\max(w(XY),V(Y)).
```

A **maximin** problem maximises the minimum arc value:

```math
V(X)=\max_Y\min(w(XY),V(Y)).
```

# 8. Core Theory

## 8.1 Shortest and longest path dynamic programming

For a shortest path problem:

```math
V(X)=\min_Y\{w(XY)+V(Y)\}.
```

For a longest path problem:

```math
V(X)=\max_Y\{w(XY)+V(Y)\}.
```

Work backwards. If `GT=12`, `HT=11`, `IT=9`, then `V(G)=12`, `V(H)=11`, `V(I)=9`. If `DG=13` and `DH=12`, then for minimum cost:

```math
DG:13+12=25,\qquad DH:12+11=23.
```

Since `23<25`, star `DH`.

## 8.2 Bellman’s principle in use

If an optimal route contains a subroute that is not optimal, replacing that subroute would improve the whole route. This contradicts optimality. Therefore an optimal route contains optimal subroutes.

## 8.3 Minimax and maximin

For minimax, do not add route totals. Take maximums, then choose the smallest maximum. For maximin, take minimums, then choose the largest minimum.

| Problem type | Candidate calculation | Starred value |
|---|---|---|
| Shortest path | `w(XY)+V(Y)` | smallest total |
| Longest path | `w(XY)+V(Y)` | largest total |
| Minimax | `max(w(XY),V(Y))` | smallest maximum |
| Maximin | `min(w(XY),V(Y))` | largest minimum |

## 8.4 Table-form dynamic programming

In table-form problems, the same headings are used but their meanings change. Stage may be a month or product type; state is a resource value; action is an amount made, used or allocated; destination is the resource left after the action; value is cumulative cost or profit.

The key rule is:

```math
\text{destination in current stage}=\text{state used for the future starred value}.
```

For allocation problems:

```math
\text{destination}=\text{state}-\text{action}.
```

For production/storage problems:

```math
\text{destination}=\text{state}+\text{made}-\text{demand}.
```

# 9. Visual Asset Integration

[VISUAL PLACEHOLDER: FA22DynamicProgrammingOffSpecEnrichmentMermaid-001 | Source: Supplied transcript, Dynamic Programming chapter structure | Insert from mermaid/FA22DynamicProgrammingOffSpecEnrichmentMermaid-001.md | Purpose: Show the universal dynamic programming workflow.]

[VISUAL PLACEHOLDER: FA22DynamicProgrammingOffSpecEnrichmentMermaid-002 | Source: Supplied transcript, shortest/longest and minimax/maximin comparison | Insert from mermaid/FA22DynamicProgrammingOffSpecEnrichmentMermaid-002.md | Purpose: Decision tree for choosing the correct calculation rule.]

[VISUAL PLACEHOLDER: FA22DynamicProgrammingOffSpecEnrichmentMermaid-003 | Source: Supplied transcript, Bellman principle and starred route tracing | Insert from mermaid/FA22DynamicProgrammingOffSpecEnrichmentMermaid-003.md | Purpose: Connect optimal substructure to table reuse.]

[VISUAL PLACEHOLDER: FA22DynamicProgrammingOffSpecEnrichmentMermaid-004 | Source: Supplied transcript, table-form examples | Insert from mermaid/FA22DynamicProgrammingOffSpecEnrichmentMermaid-004.md | Purpose: Show state-action-destination matching.]

[VISUAL PLACEHOLDER: FA22DynamicProgrammingOffSpecEnrichmentSVG-001 | Source: Screenshot PDF pages showing staged network from S to T | Insert from svg/FA22DynamicProgrammingOffSpecEnrichmentSVG-001.svg | Purpose: Recreate the evidence network used for shortest/longest path DP.]

[VISUAL PLACEHOLDER: FA22DynamicProgrammingOffSpecEnrichmentSVG-002 | Source: Supplied transcript introduction to Bellman’s principle | Insert from svg/FA22DynamicProgrammingOffSpecEnrichmentSVG-002.svg | Purpose: Show Bellman’s principle using route SABCT and subpaths.]

[VISUAL PLACEHOLDER: FA22DynamicProgrammingOffSpecEnrichmentSVG-003 | Source: Supplied transcript, minimax and maximin explanations | Insert from svg/FA22DynamicProgrammingOffSpecEnrichmentSVG-003.svg | Purpose: Compare minimax and maximin.]

[VISUAL PLACEHOLDER: FA22DynamicProgrammingOffSpecEnrichmentSVG-004 | Source: Supplied transcript, table-form definitions | Insert from svg/FA22DynamicProgrammingOffSpecEnrichmentSVG-004.svg | Purpose: Explain stage/state/action/destination/value in network and table-form problems.]

[VISUAL PLACEHOLDER: FA22DynamicProgrammingOffSpecEnrichmentBridgeSVG-001 | Source: Ordinary A-Level Maths bridge + Further Maths boundary inspection | Insert from svg/FA22DynamicProgrammingOffSpecEnrichmentBridgeSVG-001.svg | Purpose: Compare ordinary Maths habits with DP enrichment.]

[VISUAL PLACEHOLDER: FA22DynamicProgrammingOffSpecEnrichmentTikZ-001 | Source: Screenshot PDF staged network and transcript values | Insert from tikz/FA22DynamicProgrammingOffSpecEnrichmentTikZ-001.tex | Purpose: Precise staged network for print-quality notes.]

[VISUAL PLACEHOLDER: FA22DynamicProgrammingOffSpecEnrichmentTikZ-002 | Source: Supplied transcript, Bellman’s principle explanation | Insert from tikz/FA22DynamicProgrammingOffSpecEnrichmentTikZ-002.tex | Purpose: Formal diagram of an optimal route and subroutes.]

[VISUAL PLACEHOLDER: FA22DynamicProgrammingOffSpecEnrichmentTikZ-003 | Source: Supplied transcript, minimax and maximin explanations | Insert from tikz/FA22DynamicProgrammingOffSpecEnrichmentTikZ-003.tex | Purpose: Print-quality comparison of minimax and maximin.]

[VISUAL PLACEHOLDER: FA22DynamicProgrammingOffSpecEnrichmentTikZ-004 | Source: Supplied transcript, table-form definitions | Insert from tikz/FA22DynamicProgrammingOffSpecEnrichmentTikZ-004.tex | Purpose: Print-quality state-action-destination diagram.]

# 10. Interactive Learning Widgets

[INTERACTIVE PLACEHOLDER: FA22DynamicProgrammingOffSpecEnrichmentWidget-001 | Source: AI-proposed teaching enhancement based on supplied shortest/longest path evidence | Insert from widgets/FA22DynamicProgrammingOffSpecEnrichmentWidget-001.html | Purpose: Complete a staged table for shortest/longest path DP.]

[INTERACTIVE PLACEHOLDER: FA22DynamicProgrammingOffSpecEnrichmentWidget-002 | Source: AI-proposed teaching enhancement based on supplied minimax/maximin evidence | Insert from widgets/FA22DynamicProgrammingOffSpecEnrichmentWidget-002.html | Purpose: Distinguish minimax from maximin and apply the correct rule.]

[INTERACTIVE PLACEHOLDER: FA22DynamicProgrammingOffSpecEnrichmentWidget-003 | Source: AI-proposed teaching enhancement based on supplied table-form DP evidence | Insert from widgets/FA22DynamicProgrammingOffSpecEnrichmentWidget-003.html | Purpose: Practise matching destination values to future states.]

[INTERACTIVE PLACEHOLDER: FA22DynamicProgrammingOffSpecEnrichmentWidget-004 | Source: AI-proposed teaching enhancement based on CCEA boundary finding and lesson evidence | Insert from widgets/FA22DynamicProgrammingOffSpecEnrichmentWidget-004.html | Purpose: Prevent students treating this off-spec topic as CCEA core.]

# 11. Worked Examples

## 11.1 Bellman’s principle

If the shortest path from `S` to `T` is `SABCT`, then the subpaths are:

```math
S\to C:SABC,\quad S\to B:SAB,\quad S\to A:SA,\quad A\to C:ABC.
```

This uses Bellman’s principle: any part of an optimal path is an optimal path.

## 11.2 Minimum cost route from S to T, hence S to I

Using the transcript-confirmed network values:

```math
SA=10, SB=11, SC=12, AD=11, AE=10, BD=9, BE=13, BF=12, CE=12, CF=13,
DG=13, DH=12, EG=14, EH=10, EI=11, FH=14, FI=12, GT=12, HT=11, IT=9.
```

Stage 1:

```math
V(G)=12,\quad V(H)=11,\quad V(I)=9.
```

Stage 2:

```math
D: DG=13+12=25,\quad DH=12+11=23^*,\quad V(D)=23.
```

```math
E: EG=14+12=26,\quad EH=10+11=21,\quad EI=11+9=20^*,\quad V(E)=20.
```

```math
F: FH=14+11=25,\quad FI=12+9=21^*,\quad V(F)=21.
```

Stage 3:

```math
A: AD=11+23=34,\quad AE=10+20=30^*,\quad V(A)=30.
```

```math
B: BD=9+23=32^*,\quad BE=13+20=33,\quad BF=12+21=33,\quad V(B)=32.
```

```math
C: CE=12+20=32^*,\quad CF=13+21=34,\quad V(C)=32.
```

Stage 4:

```math
S: SA=10+30=40^*,\quad SB=11+32=43,\quad SC=12+32=44.
```

Thus the minimum route is:

```math
SAEIT,\qquad 10+10+11+9=40.
```

By Bellman’s principle, the minimum route from `S` to `I` is `SAEI`, with cost:

```math
10+10+11=31.
```

## 11.3 Maximum profit strategy for business expansion

The transcript gives a maximisation network with positive revenue and negative expansion costs in hundreds of thousands of pounds. Working backwards gives route:

```math
SBEHT
```

with maximum value:

```math
240.
```

The strategy is: expand in year 1, expand in year 2, no expansion in year 3, then sell assets. Since values are in hundreds of thousands of pounds:

```math
240\times100000=24000000.
```

Final profit: `£24,000,000`.

## 11.4 Maximum route with three equal optimal routes

For the standard network, the transcript’s maximum route calculation gives value `50` with three tied routes:

```math
SBEGT,\quad SCEGT,\quad SCFHT.
```

Tied optimal values must all be starred and all valid routes should be reported unless the question asks for one.

## 11.5 Minimax route from S to T

Minimax means minimise the maximum arc value. The transcript gives minimax value:

```math
11
```

with routes:

```math
SAEHT\quad\text{and}\quad SAEIT.
```

For `SAEIT`, the arc values are `10,10,11,9`, so:

```math
\max(10,10,11,9)=11.
```

## 11.6 Maximin route from S to T

Maximin means maximise the minimum arc value. The transcript gives route:

```math
SCEGT
```

with value:

```math
12.
```

The arc values are `12,12,14,12`, so:

```math
\min(12,12,14,12)=12.
```

## 11.7 Clock-maker table-form Dynamic Programming

The transcript describes a clock maker with monthly orders, production limit 4, extra help cost if making more than 2 clocks, overheads, storage limit 2 and storage cost. The evidence-backed schedule is:

| Month | Clocks made |
|---|---:|
| October | 2 |
| November | 4 |
| December | 4 |
| January | 4 |
| February | 0 |

Minimum cost: `£2,900`.

If the clock maker definitely makes 4 clocks in October, the adjusted schedule is:

| Month | Clocks made |
|---|---:|
| October | 4 |
| November | 2 |
| December | 4 |
| January | 4 |
| February | 0 |

Total cost: `£3,100`.

## 11.8 House-building maximin order

The transcript gives the final build order:

```math
B, C, A
```

with minimum estimated annual profit:

```math
£70000.
```

This is a maximin problem because the minimum annual profit is to be maximised.

## 11.9 Fairground ride route planning

The fairground example uses weeks as stages, fairs as states, travel as actions and net income as value. The calculation form is:

```math
\text{profit at current fair}-\text{travel cost}+\text{future starred value}.
```

The transcript-visible final-stage example is:

```math
14-8=6.
```

The full numeric table and final route were not fully recoverable from the supplied snippets, so no missing values are invented.

## 11.10 Footwear batch allocation

Stage meanings: type of shoe; state is batches needing allocation; action is batches allocated; destination is batches left; value is maximum profit in thousands.

The transcript gives final high-heels calculations:

```math
5:305+0=305,\quad 4:235+70=305,\quad 3:X+120,\quad 2:115+170=285,\quad 1:75+245=320,\quad 0:0+300=300.
```

The two possible maximum values are:

```math
320\quad\text{and}\quad X+120
```

in thousands of pounds. If the maximum profit is `£320,000`, then:

```math
X+120=320,\qquad X=200.
```

Possible allocations are:

```math
1\text{ high heel},4\text{ sandals},0\text{ trainers}
```

and

```math
3\text{ high heels},1\text{ sandal},1\text{ trainer}.
```

# 12. Common Mistakes and Exam Traps

- Treating Dynamic Programming as core CCEA content.
- Confusing Dynamic Programming with Dijkstra’s algorithm.
- Working forwards instead of backwards.
- Using the wrong future starred value for a destination.
- Forgetting to star optimum values.
- Failing to star tied values.
- Mixing up shortest path with minimax.
- Mixing up longest path with maximin.
- Reversing minimax and maximin.
- Adding values in minimax/maximin problems.
- Forgetting the value column changes meaning by problem type.
- Tracing stars backwards instead of forwards.
- Writing the route but not the value.
- Failing to translate a route into a real-world strategy.
- Missing unit conversions such as `240 × 100,000`.
- In table-form DP, using a future value that does not match the destination.
- Ignoring constraints such as storage limits or production limits.
- Double-charging storage or production costs.
- Tiny arithmetic slips causing wrong starred rows.

# 13. Practice Questions

All questions are AI-generated off-spec enrichment practice, not CCEA past-paper questions.

1. If the shortest route is `SDEHKT`, write the optimal subroutes `S` to `H`, `S` to `E`, `D` to `K`, and `E` to `T`.
2. Explain the headings Stage, State, Action, Destination and Value in a network and in a table-form problem.
3. Classify problems as shortest path, longest path, minimax or maximin.
4. Match each optimisation type to its calculation rule.
5. Use a generated network to find a shortest route.
6. Use the same network to find longest routes.
7. Use Bellman’s principle to extract a subroute.
8. Spot an error where the wrong future state value is used.
9. Find a minimax route.
10. Find a maximin route.
11. Solve a small production planning table-form problem.
12. Allocate advertising slots across platforms to maximise profit.
13. Solve an allocation problem containing an unknown `X`.
14. Explain the bridge from ordinary Maths to Dynamic Programming.
15. Explain why Dynamic Programming is not just Dijkstra’s algorithm in a table.
16. Compare shortest, longest, minimax and maximin on one network.
17. Design a small staged network and solve it.
18. Set up a volunteer allocation dynamic programming table.

# 14. Worked Solutions

Solutions use the full backwards-table method from the chat-generated Phase 1 lesson. Key generated results include:

- Q1: `SDEH`, `SDE`, `DEHK`, `EHKT`.
- Q5 shortest route: `SBDGT`, value `18`.
- Q6 longest routes: `SACFT`, `SADFT`, `SBCFT`, value `22`.
- Q7 shortest subroute to `G`: `SBDG`, cost `15`.
- Q8 correction: row `DG` should use `V(G)=3`, giving `5+3=8`, not `5+7=12`.
- Q9 minimax route: `SBDGT`, minimax value `6`.
- Q10 maximin routes: `SACFT` and `SBDFT`, maximin value `4`.
- Q11 generated production schedule: March `2`, April `4`, May `0`; minimum cost `£750`.
- Q12 generated advertising allocation: Search `0`, Social `2`, Video `2`; maximum profit `£145,000`.
- Q13 generated unknown-profit result: possible maximum values `190` and `X+85` thousand; if maximum is `£205,000`, then `X=120` and allocation is `A=0`, `B=3`, `C=2`.

# 15. Exam Technique Notes

Use the method named in the question. For Dynamic Programming enrichment, write the table headings, separate stages and states, show candidate arithmetic, star all optimum values, trace stars forwards, include tied routes, and convert units.

For minimax and maximin, do not add route totals. Minimax takes maximums then chooses the smallest. Maximin takes minimums then chooses the largest.

# 16. Syllabus Gap Check

| Check | Result |
|---|---|
| Official CCEA Dynamic Programming LO found | No |
| LO IDs invented | No |
| Core CCEA status claimed | No |
| Off-spec status logged | Yes |
| Ordinary Maths bridge labelled as bridge only | Yes |
| Screenshot PDF limitation logged | Yes |
| Missing fairground full table values invented | No |

### Off-Spec Content Found but Excluded from Core

Dynamic Programming, Bellman’s principle, minimax/maximin DP and table-form resource-allocation DP are excluded from core CCEA lesson status because no official CCEA LO was found in the supplied map.

### Optional Enrichment Not Required by CCEA

This whole lesson is optional enrichment unless new official CCEA evidence is supplied.

# 17. Recommended Enhancements Not in the Evidence

Recommended enhancements include the staged network visual, Bellman subpath diagram, four-method comparison grid, table-form pipeline, backwards table fill animation, star-tracing animation, minimax/maximin scanners and resource allocation widgets. These are AI-proposed teaching enhancements, not evidence-backed source content.

# 18. Supplementary Sources Used

Project sources used: CCEA Further Mathematics Specification Map, Further Maths README module map, Further Maths Evidence Drop Checklist, Ordinary A-Level Maths Bridge Extracts, CCEA Mathematics Specification Map. Lesson-specific evidence used: `transcripts.md` and `Chapter_5_Dynamic_Programming_⌨️_(Decision_2)_screenshots.pdf`.

Ordinary A-Level Maths sources are bridge context only and do not override Further Mathematics boundaries.

# 19. Final Student Checklist

- [ ] I know Dynamic Programming is off-spec enrichment unless official CCEA evidence is supplied.
- [ ] I can define stage, state, action, destination and value.
- [ ] I can work backwards from the final stage.
- [ ] I can calculate `w(XY)+V(Y)` for shortest/longest path problems.
- [ ] I can use maximums then choose the smallest for minimax.
- [ ] I can use minimums then choose the largest for maximin.
- [ ] I can match destination to the correct future state in table-form DP.
- [ ] I can star tied optimum values.
- [ ] I can trace routes forwards from `S`.
- [ ] I can interpret routes as strategies, schedules or allocations.
- [ ] I can convert units correctly.
