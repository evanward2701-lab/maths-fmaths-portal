# FAS2_algorithms_on_graphs_lesson.md

# 1. Lesson Title and Metadata

## Lesson Title

**Algorithms on Graphs: Algorithm Definition, Flow Charts and Trace Tables**

This is a foundation CCEA Further Mathematics lesson for **FAS2-ALGGRAPH: Algorithms on graphs**. The lesson-specific evidence is a Decision 1 algorithms chapter and teacher transcript. The CCEA boundary is narrower than the uploaded D1 chapter, so this lesson uses the evidence for algorithm literacy, trace tables, flow-chart interpretation and greedy-algorithm vocabulary only. Sorting, bin packing and order-of-algorithm content are logged as off-spec or optional enrichment rather than core CCEA content.

| Field | Value |
|---|---|
| Date generated | 2026-06-04 |
| Course | CCEA GCE Further Mathematics |
| Unit | FAS2: Further AS 2 Applied Mathematics |
| Applied section | Section D: Discrete and Decision Mathematics |
| Topic code | FAS2-ALGGRAPH |
| Topic name | Algorithms on graphs |
| Topic slug | algorithms_on_graphs |
| Topic Pascal | AlgorithmsOnGraphs |
| Topic ID | FAS2AlgorithmsOnGraphs |
| Lesson file | FAS2_algorithms_on_graphs_lesson.md |
| Core LO IDs | FAS2-ALGGRAPH-LO001 |
| Related LO IDs | FAS2-ALGGRAPH-LO002, FAS2-ALGGRAPH-LO003, FAS2-ALGGRAPH-LO004, FAS2-ALGGRAPH-LO005 |
| Bridge tags | ordinary algebra, sequences, iteration, tables, inequalities, optimisation language |
| Topic tags | algorithm, greedy algorithm, trace table, flow chart, input, output, decision, termination, reproducible procedure |

## CCEA Learning Outcome Focus

```text
FAS2-ALGGRAPH-LO001
demonstrate understanding of the definition of an algorithm, including the term greedy algorithm
```

Later outcomes prepared for but not taught in this foundation lesson:

```text
FAS2-ALGGRAPH-LO002
solve problems involving critical path analysis, including a precedence table for an activity network, event times and float times, and an algorithm for finding the critical path

FAS2-ALGGRAPH-LO003
recall and use Prim's algorithm to find a minimal spanning tree for a connected weighted graph

FAS2-ALGGRAPH-LO004
recall binary trees and traverse them using breadth first search and depth first search

FAS2-ALGGRAPH-LO005
recall and use Dijkstra's algorithm to find a shortest path
```

## Boundary Statement

The uploaded Decision 1 evidence contains bubble sort, quick sort, bin packing and order-of-algorithm material. These are not treated as required CCEA FAS2-ALGGRAPH core content unless later CCEA evidence confirms them. The core CCEA aim here is:

> Can you understand what an algorithm is, follow it accurately, record changing variables clearly, identify its output and understand the idea of a greedy algorithm?

# 2. Evidence Map

| Evidence source | Evidence used in this lesson | How it is used |
|---|---|---|
| CCEA Further Mathematics Specification Map | FAS2-ALGGRAPH topic identity and LO IDs | Governs the syllabus boundary |
| Further Maths README module map | Project metadata, file naming and bridge requirements | Governs lesson-pack structure |
| Further Maths Evidence Drop Checklist | Missing evidence and off-spec logging rules | Governs quality control |
| Ordinary A-Level Maths Bridge Spec Extracts | Tables, inequalities, sequences, proof and step-by-step notation | Bridge only |
| Decision Maths 1 chapter 1 Algorithms PDF | Algorithm definition, code/flow-chart/list representations, happy algorithm, Fibonacci trace table, flow-chart examples | Core support for algorithm literacy |
| Teacher transcript | Intuitive approach, why algorithms work, trace-table clarity, Fibonacci trace example, smallest-value flow-chart example | Core support for teaching method and warnings |
| Screenshot PDF | Visual confirmation of annotated trace tables and flow charts | Visual evidence, partially limited |
| Cross-board/Pearson D1 content | Sorting, bin packing, order of algorithm | Excluded from core or enrichment only |

## Evidence Limitations

The screenshot PDF was visually available but did not provide machine-readable text. The lesson preserves only readable or supported visual details. No uninspected screenshot detail is claimed.

The uploaded lesson-specific evidence does not include CCEA-specific worked examples for critical path analysis, Prim’s algorithm, binary tree traversals or Dijkstra’s algorithm, so these are not taught here.

# 3. Specification Alignment

| LO ID | Official wording | Lesson coverage | Evidence source | Syllabus boundary | Bridge |
|---|---|---|---|---|---|
| FAS2-ALGGRAPH-LO001 | demonstrate understanding of the definition of an algorithm, including the term greedy algorithm | Fully targeted. Defines algorithm, input, output, computation, instruction, decision, loop, termination, trace table, flow chart and greedy algorithm. | CCEA spec map; D1 PDF; transcript | Core | Ordinary arithmetic, sequences, tables and inequalities become explicit procedures. |
| FAS2-ALGGRAPH-LO002 | solve problems involving critical path analysis, including a precedence table for an activity network, event times and float times, and an algorithm for finding the critical path | Not taught here. Future context only. | CCEA spec map | Missing evidence | Table and ordering skills help, but CPA is new. |
| FAS2-ALGGRAPH-LO003 | recall and use Prim's algorithm to find a minimal spanning tree for a connected weighted graph | Not taught here. Future context only. | CCEA spec map | Missing evidence | Optimisation language helps. |
| FAS2-ALGGRAPH-LO004 | recall binary trees and traverse them using breadth first search and depth first search | Not taught here. | CCEA spec map | Missing evidence | No direct ordinary A-Level predecessor. |
| FAS2-ALGGRAPH-LO005 | recall and use Dijkstra's algorithm to find a shortest path | Not taught here. Future context only. | CCEA spec map | Missing evidence | Table organisation and inequality comparison help. |

# 4. Learning Objectives

## Core Further Maths objectives

1. State what an **algorithm** is.
2. Explain why an algorithm must be a clear, reproducible sequence of instructions.
3. Identify **input**, **output**, **instruction**, **decision**, **loop** and **termination**.
4. Use a **trace table** to record variable changes.
5. Interpret what an algorithm actually does from its output.
6. Define a **greedy algorithm** as one that makes the locally best permitted choice at each stage.
7. Explain why algorithm literacy prepares for later graph algorithms.

## Bridge objectives

1. Use substitution and arithmetic accurately.
2. Use sequence notation such as \(u_1,u_2,\ldots,u_n\).
3. Read inequalities such as \(T<A\), \(n<5\) and \(E=B\).
4. Organise repeated calculations in tables.
5. Avoid jumping straight to a pattern without following the required algorithm.

## Exam technique objectives

1. Make a trace table clear.
2. Leave cells blank or repeat values only where clarity is preserved.
3. State the final output explicitly.
4. State the purpose in words, not just as a number.
5. Explain stopping conditions and decision branches.

# 5. Explicit Prerequisite Recap

## GCSE foundations

- integer arithmetic;
- substitution;
- powers;
- factors, multiples and HCF;
- reading tables;
- reading inequalities;
- percentage error if using the numerical-approximation example.

## Ordinary AS/A2 Mathematics foundations

- sequences notation \(u_1,u_2,u_3,\ldots,u_n\);
- recurrence-style updates;
- exact arithmetic before rounding;
- definite integration only for optional bridge examples;
- clear written mathematical communication.

## Previous Further Mathematics foundations

No previous Further Mathematics content is strictly required.

### A-Level Maths Bridge: What You Already Know and What Further Maths Changes

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| GCSE and AS arithmetic | Follow a sequence of numerical operations. | The sequence of operations itself becomes the object being studied. | Do not skip steps just because the output looks obvious. |
| AS/A2 sequences | Use \(u_1,u_2,\ldots,u_n\). | Algorithms may read a list term by term. | \(u_n\) means the current indexed term, not a new independent variable. |
| AS/A2 algebra | Substitute and simplify. | Algorithm instructions overwrite variables. | Old values disappear unless recorded. |
| AS/A2 inequalities | Decide whether statements are true or false. | Flow charts use decisions to choose paths. | One wrong yes/no branch can spoil the table. |
| Ordinary table work | Organise repeated calculations. | Trace tables record live algorithm state. | A correct but unclear table can lose communication quality. |
| Optimisation language | Choose max/min/efficient options. | Greedy algorithms choose the locally best permitted option at each stage. | The choice must follow the stated rule exactly. |

In ordinary A-Level Maths, this idea appeared as repeated substitution, table work, sequences and inequality decisions. In Further Maths, the same idea becomes a formal object called an **algorithm**: a set of instructions that can be followed mechanically to turn an input into an output. The key upgrade is that the method itself matters. The danger is that human intuition wants to leapfrog the stated procedure.

# 6. Big Picture Explanation

An algorithm is a disciplined recipe. It tells you what to do, in what order, when to repeat, when to branch and when to stop.

A human can spot that the smallest number in

\[
10,\ 15,\ 9,\ 7,\ 11
\]

is \(7\). Decision Mathematics asks a different question:

> How could a machine, or a very obedient paper-and-pen process, be told to find the smallest number?

A computer-like procedure might:

1. store the first value;
2. inspect the next value;
3. compare;
4. replace the stored value if the new value is smaller;
5. repeat until the list ends;
6. output the stored value.

Later FAS2 graph algorithms use this same structure: clear inputs, controlled decisions, repeated updates and a final output.

# 7. Key Definitions and Notation

## Algorithm

An **algorithm** is a specific set of instructions for carrying out a procedure or solving a problem, usually with the requirement that the procedure terminates.

The same idea may also be called a method, procedure or technique. The process of applying an algorithm to an input to obtain an output is called a **computation**.

## Input

An **input** is the value, list, table, graph or other object fed into the algorithm at the start.

Examples:

\[
A=1,\quad B=3,\quad N=4
\]

or

\[
u_1=10,\quad u_2=15,\quad u_3=9,\quad u_4=7,\quad u_5=11.
\]

## Output

An **output** is the value, list, decision or result produced by the algorithm.

Examples:

\[
\text{Output}=7
\]

or

\[
1,\ 1,\ 2,\ 3,\ 5,\ 8.
\]

## Variable

A **variable** is a symbol whose value may change while the algorithm is running, for example

\[
n,\quad A,\quad B,\quad C,\quad T.
\]

In an algorithm, “Let \(A=B\)” means replace the current value of \(A\) by the current value of \(B\). It does not mean \(A\) and \(B\) have always been the same.

## Instruction

An **instruction** tells the algorithm to perform an action, such as

\[
\text{Let } C=A+B,\qquad \text{Let } n=n+1,\qquad \text{Print } C.
\]

The instruction \(n=n+1\) is not an ordinary algebra equation. It means:

\[
\text{new value of }n=\text{old value of }n+1.
\]

## Decision

A **decision** checks whether a condition is true or false and chooses a branch.

Examples:

\[
\text{If } n<5 \text{ go to Step 3},\qquad \text{Is }T<A?
\]

## Loop

A **loop** occurs when an algorithm returns to an earlier step and repeats part of the process.

## Termination

An algorithm must know when to stop. Examples include:

\[
\text{If } n=5 \text{ stop},\qquad \text{Stop},\qquad \text{End}.
\]

## Trace table

A **trace table** records the changing values of variables as an algorithm runs.

## Flow chart

A **flow chart** represents an algorithm using boxes and arrows.

| Shape | Meaning |
|---|---|
| Rounded rectangle / oval | Start or End |
| Rectangle | Instruction |
| Diamond | Decision |

## Greedy algorithm

A **greedy algorithm** makes the locally best permitted choice at each stage according to a fixed rule. “Locally best” means best right now, using the information and rule available at that step.

A greedy algorithm is not “guess the best answer”. It must follow its rule precisely.

# 8. Core Theory

## 8.1 Algorithm structure

An algorithm takes an input, applies a finite set of instructions and produces an output:

\[
\text{Input}\longrightarrow\text{Algorithm}\longrightarrow\text{Output}.
\]

For FAS2, the method itself is part of the mathematics. You must be able to follow and explain the procedure, not merely spot the answer.

**Bridge Note:** In ordinary A-Level Maths, a method is usually a tool. In Further Maths Decision, the method itself becomes the object being studied.

## 8.2 Algorithm representations

Algorithms may be written as:

1. code;
2. flow charts;
3. a list of instructions.

A list-of-instructions example is:

```text
1. Let n = 1, A = 1, B = 1
2. Write down A and B
3. Let C = A + B
4. Write down C
5. Let n = n + 1, A = B, B = C
6. If n < 5 go to step 3
7. If n = 5 stop
```

## 8.3 Variable updates

In ordinary algebra \(n=n+1\) is impossible. In an algorithm,

\[
\text{Let }n=n+1
\]

means:

\[
n_{\text{new}}=n_{\text{old}}+1.
\]

If \(n=1\), the new value is \(2\). If \(n=2\), the new value is \(3\). A trace table prevents old values disappearing unnoticed.

## 8.4 Trace-table clarity

The evidence stresses that trace tables do not need one rigid format, but they must be clear. You may leave cells blank where values are unchanged, or repeat values if this improves clarity. A good table shows inputs, updated variables, decisions, outputs and stopping conditions.

## 8.5 Fibonacci trace-table algorithm

Consider:

```text
1. Let n = 1, A = 1, B = 1
2. Write down A and B
3. Let C = A + B
4. Write down C
5. Let n = n + 1, A = B, B = C
6. If n < 5 go to step 3
7. If n = 5 stop
```

Initialise:

\[
n=1,\quad A=1,\quad B=1.
\]

Write down:

\[
1,\ 1.
\]

First loop:

\[
C=A+B=1+1=2.
\]

Write down \(2\). Update:

\[
n=1+1=2,\qquad A=B=1,\qquad B=C=2.
\]

Second loop:

\[
C=1+2=3.
\]

Write down \(3\). Update:

\[
n=2+1=3,\qquad A=2,\qquad B=3.
\]

Third loop:

\[
C=2+3=5.
\]

Write down \(5\). Update:

\[
n=3+1=4,\qquad A=3,\qquad B=5.
\]

Fourth loop:

\[
C=3+5=8.
\]

Write down \(8\). Update:

\[
n=4+1=5,\qquad A=5,\qquad B=8.
\]

Now \(n<5\) is false and \(n=5\), so the algorithm stops.

The output is

\[
1,\ 1,\ 2,\ 3,\ 5,\ 8.
\]

The algorithm generates Fibonacci-style terms by repeatedly replacing

\[
(A,B)\mapsto(B,A+B).
\]

## 8.6 Flow-chart logic

A flow chart must be followed by moving along arrows. A decision diamond must be answered exactly.

For example, if the decision is

\[
T<A?
\]

and \(T=15,\ A=10\), then \(15<10\) is false. Follow the “No” branch. If later \(T=9,\ A=10\), then \(9<10\) is true. Follow the “Yes” branch.

## 8.7 Smallest-value flow-chart algorithm

Use

\[
u_1=10,\quad u_2=15,\quad u_3=9,\quad u_4=7,\quad u_5=11.
\]

The algorithm begins:

\[
n=1,\qquad A=u_1=10.
\]

Then it repeatedly:

1. increases \(n\);
2. sets \(T=u_n\);
3. checks whether \(T<A\);
4. if yes, replaces \(A\) by \(T\);
5. checks whether \(n<5\);
6. repeats or outputs \(A\).

Trace table:

| \(n\) | \(A\) | \(T\) | Decision \(T<A\)? | Action |
|---:|---:|---:|---|---|
| 1 | 10 |  |  | Initial state |
| 2 | 10 | 15 | \(15<10\) false | Keep \(A=10\) |
| 3 | 9 | 9 | \(9<10\) true | Replace \(A\) by \(9\) |
| 4 | 7 | 7 | \(7<9\) true | Replace \(A\) by \(7\) |
| 5 | 7 | 11 | \(11<7\) false | Keep \(A=7\) |

The output is

\[
7.
\]

The purpose is:

\[
\text{The algorithm finds the smallest value in a list.}
\]

The invariant is:

\[
A=\text{smallest value among the terms inspected so far}.
\]

## 8.8 Greedy algorithms

A greedy algorithm makes a locally best permitted choice at each stage. This means it has a rule, applies the rule to the current situation, does not usually go back to reconsider earlier choices, and continues until complete.

Example wording:

> At each step, choose the smallest available value that does not break the rule.

The greedy choice is the smallest permitted value at that step. It is not a guess.

# 9. Visual Asset Integration

Diagram evidence is partially unclear here. The screenshot PDF was available as rendered images, but no uninspected visual detail is claimed.

[VISUAL PLACEHOLDER: FAS2AlgorithmsOnGraphsMermaid-001 | Source: CCEA FAS2-ALGGRAPH specification boundary + lesson evidence | Insert from mermaid/FAS2AlgorithmsOnGraphsMermaid-001.md | Purpose: Show how LO001 algorithm understanding sits before later graph algorithms such as critical path analysis, Prim’s algorithm, tree traversal and Dijkstra’s algorithm. Description: A flow-style dependency map with LO001 as the root node, branching to later algorithmic topics.]

[VISUAL PLACEHOLDER: FAS2AlgorithmsOnGraphsSVG-001 | Source: Decision 1 lesson PDF flow-chart evidence | Insert from svg/FAS2AlgorithmsOnGraphsSVG-001.svg | Purpose: Identify the three standard flow-chart box types. Description: A clean diagram showing a rounded Start/End box, rectangular Instruction box and diamond Decision box, each labelled with its examination meaning.]

[VISUAL PLACEHOLDER: FAS2AlgorithmsOnGraphsSVG-002 | Source: Teacher transcript + Fibonacci trace-table evidence | Insert from svg/FAS2AlgorithmsOnGraphsSVG-002.svg | Purpose: Show how a trace table records changing variables. Description: A table with columns \(n,A,B,C,\text{Write down}\), highlighting the update \((A,B)\mapsto(B,A+B)\) and the output \(1,1,2,3,5,8\).]

[VISUAL PLACEHOLDER: FAS2AlgorithmsOnGraphsBridgeSVG-001 | Source: Ordinary A-Level Maths bridge + Further Maths specification | Insert from svg/FAS2AlgorithmsOnGraphsBridgeSVG-001.svg | Purpose: Compare prior ordinary Maths method with Further Maths extension. Description: Left side shows ordinary substitution/table work; right side shows algorithm input, trace table, decision, loop, termination and output.]

[VISUAL PLACEHOLDER: FAS2AlgorithmsOnGraphsTikZ-001 | Source: Flow-chart example from lesson evidence | Insert from tikz/FAS2AlgorithmsOnGraphsTikZ-001.tex | Purpose: Give a precise mathematical flow-chart for the smallest-value algorithm. Description: Start, \(n=1,A=u_1\), \(n=n+1\), \(T=u_n\), decision \(T<A?\), update \(A=T\), decision \(n<5?\), output \(A\), Stop.]

[VISUAL PLACEHOLDER: FAS2AlgorithmsOnGraphsSVG-003 | Source: AI-proposed teaching enhancement based on CCEA LO001 | Insert from svg/FAS2AlgorithmsOnGraphsSVG-003.svg | Purpose: Explain greedy algorithm vocabulary. Description: A staged diagram showing current situation, permitted choices, locally best permitted choice, update, repeat and output.]

[VISUAL PLACEHOLDER: FAS2AlgorithmsOnGraphsSVG-004 | Source: Lesson evidence + exam technique notes | Insert from svg/FAS2AlgorithmsOnGraphsSVG-004.svg | Purpose: Distinguish output from purpose. Description: A two-column visual comparing specific output \(7\) with general purpose “finds the smallest number in a list”.]

# 10. Interactive Learning Widgets

[INTERACTIVE PLACEHOLDER: FAS2AlgorithmsOnGraphsWidget-001 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FAS2AlgorithmsOnGraphsWidget-001.html | Purpose: Let the student step through a trace table and reveal variable updates.]

This widget lets the student enter \(u_1,\ldots,u_5\), then steps through the smallest-value algorithm. It displays \(n\), \(A\), \(T\), the decision \(T<A\), whether \(A\) updates, and the final output.

[INTERACTIVE PLACEHOLDER: FAS2AlgorithmsOnGraphsWidget-002 | Source: AI-proposed teaching enhancement based on lesson evidence and CCEA LO001 | Insert from widgets/FAS2AlgorithmsOnGraphsWidget-002.html | Purpose: Help students classify algorithm statements as input, instruction, decision, output, loop or termination.]

This widget classifies statements such as `Input A, B and N`, `Let H = (B - A)/N`, `If n < 5 go to Step 3`, `Print C` and `Stop`.

[INTERACTIVE PLACEHOLDER: FAS2AlgorithmsOnGraphsWidget-003 | Source: AI-proposed teaching enhancement based on CCEA LO001 | Insert from widgets/FAS2AlgorithmsOnGraphsWidget-003.html | Purpose: Introduce greedy algorithm vocabulary before later graph algorithms.]

This widget lets the student practise selecting the locally best permitted choice according to a stated greedy rule.

# 11. Worked Examples

## Worked Example 1: Happy algorithm

The “happy” algorithm is:

1. Write down any integer.
2. Square its digits and find the sum.
3. Continue with this number.
4. Repeat until the number becomes \(1\), or until a previous value repeats.

Show that \(70\) is happy.

\[
7^2+0^2=49
\]

\[
4^2+9^2=16+81=97
\]

\[
9^2+7^2=81+49=130
\]

\[
1^2+3^2+0^2=1+9+0=10
\]

\[
1^2+0^2=1.
\]

So

\[
70\to49\to97\to130\to10\to1.
\]

Since the algorithm reaches \(1\), \(70\) is happy.

## Worked Example 2: Fibonacci trace table

Using the algorithm in Section 8.5, the output is:

\[
1,\ 1,\ 2,\ 3,\ 5,\ 8.
\]

It prints Fibonacci-style terms because it repeatedly updates:

\[
(A,B)\mapsto(B,A+B).
\]

## Worked Example 3: Numerical approximation trace-table example

Algorithm:

```text
Input A, B and N
Let H = (B - A) / N
Let C = H / 2
Let D = 0
Let D = D + A^4 + B^4
Let E = A
Let E = E + H
If E = B go to final calculation
Let D = D + 2E^4
Repeat
Let F = C × D
Output F
```

For

\[
A=1,\quad B=3,\quad N=4,
\]

\[
H=\frac{3-1}{4}=0.5,
\qquad
C=\frac{H}{2}=0.25.
\]

Endpoint update:

\[
D=0+1^4+3^4=0+1+81=82.
\]

Set \(E=1\), then \(E=1.5\).

\[
D=82+2(1.5)^4.
\]

Since

\[
1.5^2=2.25,\qquad 1.5^4=5.0625,
\]

\[
D=82+2(5.0625)=82+10.125=92.125.
\]

Next \(E=2\):

\[
D=92.125+2(2^4)=92.125+32=124.125.
\]

Next \(E=2.5\):

\[
D=124.125+2(2.5^4).
\]

\[
2.5^2=6.25,\qquad 2.5^4=39.0625,
\]

\[
D=124.125+78.125=202.25.
\]

Next \(E=3=B\), so calculate

\[
F=C\times D=0.25\times202.25=50.5625.
\]

The exact value of

\[
I=\int_1^3x^4\,dx
\]

is

\[
I=\left[\frac{x^5}{5}\right]_1^3=\frac{3^5}{5}-\frac{1^5}{5}
=\frac{243}{5}-\frac{1}{5}=\frac{242}{5}=48.4.
\]

Percentage error:

\[
\frac{50.5625-48.4}{48.4}\times100
=
4.467975\ldots\%=4.47\%\quad(3\text{ s.f.})
\]

The approximation is an overestimate.

## Worked Example 4: Flow chart finding the smallest value

For

\[
u_1=10,\quad u_2=15,\quad u_3=9,\quad u_4=7,\quad u_5=11,
\]

initialise

\[
n=1,\quad A=10.
\]

Trace:

| \(n\) | \(A\) | \(T\) | Decision | Result |
|---:|---:|---:|---|---|
| 1 | 10 |  |  | Start |
| 2 | 10 | 15 | \(15<10\) false | keep \(A=10\) |
| 3 | 9 | 9 | \(9<10\) true | update \(A=9\) |
| 4 | 7 | 7 | \(7<9\) true | update \(A=7\) |
| 5 | 7 | 11 | \(11<7\) false | keep \(A=7\) |

Output:

\[
7.
\]

Purpose:

\[
\text{The algorithm finds the smallest value in the list.}
\]

## Worked Example 5: Output versus purpose

For the list

\[
10,\ 15,\ 9,\ 7,\ 11,
\]

the output is

\[
7.
\]

The purpose is not “7”. The purpose is:

> The algorithm finds the smallest number in a list.

# 12. Common Mistakes and Exam Traps

1. Treating \(n=n+1\) as ordinary algebra.
2. Overwriting variables in the wrong order.
3. Filling a trace table beautifully but unclearly.
4. Moving to a new row after every tiny action.
5. Not stating the final output separately.
6. Confusing output with purpose.
7. Following intuition instead of the stated algorithm.
8. Taking the wrong branch in a flow chart.
9. Returning to the wrong step in a loop.
10. Assuming every algorithm is greedy.
11. Thinking greedy automatically means globally optimal.
12. Importing bubble sort, quick sort, bin packing or order-of-algorithm content as core CCEA content.

# 13. Practice Questions

## Basic fluency

1. Define an algorithm.
2. Explain what `Let n = n + 1` means in an algorithm.
3. State the meaning of rounded rectangle/oval, rectangle and diamond in a flow chart.
4. Classify each statement as input, instruction, decision, output or termination:
   - `Input A, B and N`
   - `Let H = (B - A)/N`
   - `If n < 5 go to Step 3`
   - `Print C`
   - `Stop`

## Bridge questions

5. The old value of \(n\) is \(4\). An algorithm says `Let n = n + 1`. Find the new value of \(n\).
6. Current values are \(A=12,\ B=5,\ C=17\). An algorithm says `Let A = B, B = C`. Find new \(A\) and \(B\).
7. For each pair, decide whether \(T<A\) is true:
   - \(T=6,\ A=10\)
   - \(T=14,\ A=9\)
   - \(T=7,\ A=7\)

## Standard exam-style questions

8. Implement:

```text
1. Let n = 1, A = 2, B = 3
2. Write down A and B
3. Let C = A + B
4. Write down C
5. Let n = n + 1, A = B, B = C
6. If n < 4 go to Step 3
7. Stop
```

9. Apply the smallest-value algorithm to

\[
u_1=18,\quad u_2=14,\quad u_3=21,\quad u_4=9,\quad u_5=16.
\]

10. Change the decision to \(T>A\) and apply it to

\[
u_1=4,\quad u_2=11,\quad u_3=8,\quad u_4=15,\quad u_5=10.
\]

11. Apply the digit-square algorithm starting with \(13\).

12. Apply the square-version numerical approximation algorithm with \(A=2,\ B=6,\ N=4\).

## Harder synthesis

13. Explain why “The purpose of the algorithm is 3” is not acceptable when \(3\) is the output.
14. Define greedy algorithm and explain “locally best permitted choice”.
15. Correct a table where \(A\) is replaced every time instead of only when \(T<A\).

# 14. Worked Solutions

## Solution 1

An algorithm is a specific set of instructions for carrying out a procedure or solving a problem, usually with the requirement that the procedure terminates.

## Solution 2

`Let n = n + 1` means:

\[
n_{\text{new}}=n_{\text{old}}+1.
\]

## Solution 3

Rounded rectangle/oval: Start or End. Rectangle: Instruction. Diamond: Decision.

## Solution 4

- `Input A, B and N`: input.
- `Let H = (B - A)/N`: instruction.
- `If n < 5 go to Step 3`: decision and loop.
- `Print C`: output.
- `Stop`: termination.

## Solution 5

\[
n=4+1=5.
\]

## Solution 6

Using old values:

\[
A=5,\qquad B=17.
\]

## Solution 7

\[
6<10 \text{ true},\qquad 14<9 \text{ false},\qquad 7<7 \text{ false}.
\]

## Solution 8

Initial:

\[
n=1,\quad A=2,\quad B=3.
\]

Write down \(2,3\).

\[
C=2+3=5.
\]

Write down \(5\). Update:

\[
n=2,\quad A=3,\quad B=5.
\]

Since \(2<4\), repeat.

\[
C=3+5=8.
\]

Write down \(8\). Update:

\[
n=3,\quad A=5,\quad B=8.
\]

Since \(3<4\), repeat.

\[
C=5+8=13.
\]

Write down \(13\). Update:

\[
n=4,\quad A=8,\quad B=13.
\]

Since \(4<4\) is false, stop.

Output:

\[
2,\ 3,\ 5,\ 8,\ 13.
\]

## Solution 9

Trace:

| \(n\) | \(A\) | \(T\) | Decision |
|---:|---:|---:|---|
| 1 | 18 |  | Start |
| 2 | 14 | 14 | \(14<18\) true |
| 3 | 14 | 21 | \(21<14\) false |
| 4 | 9 | 9 | \(9<14\) true |
| 5 | 9 | 16 | \(16<9\) false |

Output:

\[
9.
\]

Purpose: finds the smallest value.

## Solution 10

The condition \(T>A\) stores the largest inspected value.

Trace:

| \(n\) | \(A\) | \(T\) | Decision |
|---:|---:|---:|---|
| 1 | 4 |  | Start |
| 2 | 11 | 11 | \(11>4\) true |
| 3 | 11 | 8 | \(8>11\) false |
| 4 | 15 | 15 | \(15>11\) true |
| 5 | 15 | 10 | \(10>15\) false |

Output:

\[
15.
\]

Purpose: finds the largest value.

## Solution 11

\[
13\to 1^2+3^2=10\to 1^2+0^2=1.
\]

So \(13\) reaches \(1\).

## Solution 12

Given

\[
A=2,\quad B=6,\quad N=4.
\]

\[
H=\frac{6-2}{4}=1,\qquad C=\frac12.
\]

\[
D=0+2^2+6^2=40.
\]

Set \(E=2\). Then

\[
E=3,\quad D=40+2(3^2)=58.
\]

\[
E=4,\quad D=58+2(4^2)=90.
\]

\[
E=5,\quad D=90+2(5^2)=140.
\]

\[
E=6=B,
\]

so

\[
F=C\times D=0.5\times140=70.
\]

Output:

\[
70.
\]

The algorithm stops because \(E\) reaches \(B\).

## Solution 13

The number \(3\) is the output for that input, not the purpose. A better answer is:

> The algorithm finds the smallest value in a list.

## Solution 14

A greedy algorithm makes the locally best permitted choice at each stage according to a fixed rule. “Locally best permitted” means best now among the choices allowed by the rule. It does not automatically mean globally optimal.

## Solution 15

If the algorithm says update \(A\) only when \(T<A\), then \(A\) must not be replaced every time. For

\[
u_1=20,\quad u_2=17,\quad u_3=19,\quad u_4=13,\quad u_5=15,
\]

the correct table is:

| \(n\) | \(A\) | \(T\) | Decision |
|---:|---:|---:|---|
| 1 | 20 |  | start |
| 2 | 17 | 17 | \(17<20\) true |
| 3 | 17 | 19 | \(19<17\) false |
| 4 | 13 | 13 | \(13<17\) true |
| 5 | 13 | 15 | \(15<13\) false |

Output:

\[
13.
\]

# 15. Exam Technique Notes

1. Read the full algorithm before filling the table.
2. Identify inputs, variables, decisions, loops and output.
3. Treat `Let` as an instruction, not an equation.
4. Use old values when updating variables.
5. Answer decisions exactly: \(7<7\) is false.
6. Identify the stopping condition.
7. State the final output separately.
8. Distinguish output from purpose.
9. Use exact values unless decimals are required.
10. Define greedy precisely as locally best permitted choice at each stage.
11. Do not import off-spec algorithms into CCEA core answers.

# 16. Syllabus Gap Check

## LO coverage

| LO ID | Covered? | Notes |
|---|---:|---|
| FAS2-ALGGRAPH-LO001 | Yes | Algorithm definition, trace tables, flow charts, greedy vocabulary |
| FAS2-ALGGRAPH-LO002 | No | Missing CPA evidence |
| FAS2-ALGGRAPH-LO003 | No | Missing Prim’s algorithm evidence |
| FAS2-ALGGRAPH-LO004 | No | Missing tree traversal evidence |
| FAS2-ALGGRAPH-LO005 | No | Missing Dijkstra evidence |

## Evidence coverage

| Evidence item | Covered? |
|---|---:|
| Algorithm definition | Yes |
| Code/flow-chart/list representations | Yes |
| Happy algorithm | Yes |
| Fibonacci trace table | Yes |
| Numerical approximation trace table | Yes |
| Flow-chart shapes | Yes |
| Smallest-value flow chart | Yes |
| Bubble sort | Excluded from core |
| Quick sort | Excluded from core |
| Bin packing | Excluded from core |
| Order of an algorithm | Excluded from core |

## Off-Spec Content Found but Excluded

| Content | Reason |
|---|---|
| Bubble sort | Not listed in supplied CCEA FAS2-ALGGRAPH LO boundary |
| Quick sort | Not listed in supplied CCEA FAS2-ALGGRAPH LO boundary |
| Bin packing | Not listed in supplied CCEA FAS2-ALGGRAPH LO boundary |
| Order of an algorithm | Not listed in supplied CCEA FAS2-ALGGRAPH LO boundary |
| Pearson/Edexcel exercise references | Not CCEA authority |
| Euclidean algorithm | Not taught as named CCEA method |
| Happy numbers | Practice only, not named CCEA method |
| Integration approximation algorithm | Trace-table bridge only, not Decision core |

## Missing Evidence Log

| Missing evidence | Current handling |
|---|---|
| CCEA greedy worked examples | Generic definition included |
| CPA examples | Not taught |
| Prim’s algorithm examples | Not taught |
| BFS/DFS examples | Not taught |
| Dijkstra examples | Not taught |
| CCEA mark scheme extracts | General evidence-backed technique only |

# 17. Recommended Enhancements Not in the Evidence

AI-proposed enhancements, not direct evidence-backed content unless later matched to CCEA sources:

- algorithm pipeline diagram;
- trace-table anatomy diagram;
- flow-chart symbol card;
- output-versus-purpose comparison card;
- greedy algorithm choice diagram;
- row-reveal trace-table animation;
- flow-chart path highlighter;
- variable-overwriting animation;
- trace-table stepper widget;
- algorithm statement classifier;
- greedy choice checker;
- output-versus-purpose checker.

# 18. Supplementary Sources Used

## Project Sources

- CCEA GCE Further Mathematics Specification Map.
- Further Maths Portal Build Knowledge Evidence.
- Further Maths README module map.
- Further Maths Evidence Drop Checklist.
- Ordinary A-Level Maths Bridge Spec Extracts.
- CCEA GCE Mathematics Specification Map, bridge only.

## Lesson-specific evidence

- `Decision Maths 1 chapter 1 Algorithms.pdf`
- `Chapter_1_Algorithms_💻_(Decision_1)_screenshots.pdf`
- `transcripts.md`

## Bridge-source boundary

Ordinary A-Level Maths sources were used only for arithmetic, sequences, recurrence-style thinking, table organisation, inequalities, definite integration in the optional numerical approximation example and percentage error. They do not override the CCEA Further Mathematics specification.

## Evidence limitations

The screenshot PDF was visually available but not machine-readable. No CCEA-specific worked examples were supplied for CPA, Prim’s algorithm, binary tree traversal or Dijkstra’s algorithm.

# 19. Final Student Checklist

## Prerequisite confidence

- [ ] I can use arithmetic accurately.
- [ ] I can substitute values into formulae.
- [ ] I can use \(u_1,u_2,\ldots,u_n\).
- [ ] I can decide whether inequalities are true or false.
- [ ] I can organise repeated calculations in a table.

## Further Maths method

- [ ] I can define algorithm.
- [ ] I can explain input and output.
- [ ] I can identify instruction, decision, loop and termination.
- [ ] I can complete a trace table.
- [ ] I can explain the purpose of an algorithm.
- [ ] I can define greedy algorithm.

## Exam technique

- [ ] I read the whole algorithm first.
- [ ] I update variables in the correct order.
- [ ] I answer decision checks exactly.
- [ ] I follow the correct flow-chart branch.
- [ ] I state the final output separately.
- [ ] I give the purpose in words.
- [ ] I exclude off-spec sorting/bin-packing material from core CCEA answers unless explicitly asked.

## Final readiness statement

You are ready to move into later CCEA graph algorithms when you can confidently say:

> I can follow a finite set of instructions, record changing variables clearly, explain why the algorithm stops, state the output and describe the purpose of the procedure.
