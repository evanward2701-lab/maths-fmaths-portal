# FA22 Game Theory Enrichment Lesson

# 1. Lesson Title and Metadata

## Lesson Title

**Optional Enrichment: Game Theory, Pay-off Matrices and Optimal Strategies**

## Metadata

| Field | Entry |
|---|---|
| Date generated | 2026-06-05 |
| Course | CCEA GCE Further Mathematics enrichment |
| Core CCEA status | **Optional enrichment only. Not required by CCEA unless further official CCEA evidence is supplied.** |
| Suggested unit placement | FA22: Further A2 2 Applied Mathematics |
| Suggested applied section | Section D: Discrete and Decision Mathematics, enrichment link |
| Official CCEA topic code | **None found** |
| Enrichment topic code | `ENR-GAMETHEORY` |
| Topic name | Game Theory |
| Topic slug | `game_theory_enrichment` |
| Topic Pascal | `GameTheoryEnrichment` |
| Topic ID | `FA22GameTheoryEnrichment` |
| Lesson file name | `FA22_game_theory_enrichment_lesson.md` |
| Official CCEA LO IDs | **None found** |
| Enrichment objectives | `ENR-GT-001` to `ENR-GT-010` |
| Bridge tags | `#Algebra`, `#Matrices`, `#Inequalities`, `#Probability`, `#ExpectedValue`, `#Optimisation`, `#LinearProgramming` |
| Topic tags | `#GameTheory`, `#PayoffMatrix`, `#ZeroSumGame`, `#Maximin`, `#Minimax`, `#SaddlePoint`, `#MixedStrategy`, `#GraphicalMethod`, `#Dominance`, `#SimplexEnrichment` |

## Boundary Notice

This lesson is deliberately labelled as **off-spec enrichment**.

The supplied evidence is from **Decision 2 Chapter 6: Game Theory**. The CCEA Further Mathematics specification map supplied in the Project Sources does not list Game Theory as a CCEA topic, and no official Game Theory learning outcome IDs were found. Therefore, this lesson must not be presented as compulsory CCEA Further Mathematics content.

This enrichment is useful because it connects naturally to CCEA-style mathematical skills: reading structured tables and matrices; comparing values using inequalities; using probabilities and expected values; maximising and minimising quantities; and understanding why linear programming and simplex methods matter.

# 2. Evidence Map

| Evidence source | Type | Status | Used for |
|---|---|---|---|
| `transcripts.md` | Teacher transcript | Available | Main enrichment content: play-safe strategies, zero-sum games, stable solutions, dominance, mixed strategies, graphical methods and linear programming. |
| `Chapter_6_Game_Theory_⌨️_(Decision_2)_screenshots.pdf` | Screenshot PDF | Partially available visually | Visual evidence for chapter title, prisoner’s dilemma, play-safe strategy matrices, annotations, zero-sum game tables and handwritten maximin/minimax work. |
| CCEA GCE Further Mathematics Specification Map | Project source | Inspected | Used to confirm Game Theory is not listed as an official CCEA topic. |
| Further Maths README module map | Project source | Inspected | Used to preserve project naming discipline and enrichment labelling. |
| Further Maths Evidence Drop Checklist | Project source | Inspected | Used to enforce off-spec logging. |
| Ordinary A-Level Mathematics bridge extracts | Project source | Inspected | Used only for bridge context: algebra, inequalities, matrices, probability, expected values and optimisation. |
| Cross-board Decision 2 evidence | Lesson-specific evidence | Used as enrichment only | The entire Game Theory chapter is treated as non-CCEA enrichment. |

## Visual Evidence Limitation

Diagram evidence is partially unclear here. The description below preserves the visible/readable details only. No uninspected visual detail is claimed.

The screenshot PDF contains rendered images of pages, not parsed text. The visible early pages show: title page “D2: Chapter 6, Game Theory”; chapter menu with Ex 6A Play-safe strategies and stable solutions, Ex 6B Reducing the pay-off matrix, Ex 6C Optimal strategies for unstable games, Ex 6D Linear programming, Exam Questions; prisoner’s dilemma payoff table; play-safe strategy payoff matrix with row and column labels; handwritten annotations marking minima, maxima, maximin and minimax; zero-sum game explanation and payoff tables.

# 3. Specification Alignment

## Official CCEA Further Mathematics Alignment

| Official CCEA LO ID | Official wording | Lesson coverage | Boundary decision |
|---|---|---|---|
| None found | No official CCEA Game Theory LO found in the supplied specification map. | Game Theory is taught only as enrichment. | Do not treat as core CCEA content. |

## Related CCEA Skill Links, Not Topic Authority

| CCEA-related skill area | Why it is related | Boundary warning |
|---|---|---|
| FA22 Section D: Discrete and Decision Mathematics | Game Theory belongs naturally near decision mathematics because it studies strategic choices and optimisation. | Related placement only; not official Game Theory coverage. |
| Linear programming / simplex ideas | The transcript uses simplex-style linear programming for game theory. | CCEA simplex content must remain inside its official linear programming boundary. |
| Counting and probability foundations | Mixed strategies use probabilities and expected values. | Probability links are bridge support, not Game Theory LO evidence. |

# 4. Learning Objectives

## Enrichment Objectives

| Enrichment ID | Objective |
|---|---|
| `ENR-GT-001` | Explain what Game Theory studies in simple strategic situations. |
| `ENR-GT-002` | Interpret a pay-off matrix from player A’s point of view. |
| `ENR-GT-003` | Explain the meaning of a zero-sum game. |
| `ENR-GT-004` | Find player A’s play-safe strategy using the row maximin. |
| `ENR-GT-005` | Find player B’s play-safe strategy using the column minimax. |
| `ENR-GT-006` | Decide whether a zero-sum game has a stable solution. |
| `ENR-GT-007` | Identify a saddle point in a pay-off matrix. |
| `ENR-GT-008` | Reduce a pay-off matrix using dominated rows or columns. |
| `ENR-GT-009` | Use mixed strategies and expected winnings for unstable games. |
| `ENR-GT-010` | Understand, at enrichment level, how larger matrix games can be converted into linear programming problems. |

## Bridge Objectives

The student should be able to connect this lesson to ordinary A-Level Maths by using inequalities to compare possible outcomes, using tables and matrices to organise numerical information, using probability weights such as \(p\) and \(1-p\), forming expected values, interpreting optimisation as “make the worst-case outcome as good as possible”, and recognising why linear programming needs non-negative variables.

# 5. Explicit Prerequisite Recap

## GCSE Foundations

You should already be comfortable with reading tables, comparing positive and negative numbers, identifying largest and smallest values, substituting values into expressions and solving simple linear equations.

Example:

\[
-4 < -1 < 0 < 3.
\]

This matters because in zero-sum games, a negative entry is bad for player A but good for player B.

## Ordinary AS/A2 Mathematics Foundations

You should already have seen inequalities, simultaneous equations, straight-line graphs, probability and expected value, matrices or table-style arrays and optimisation language such as maximise and minimise.

## A-Level Maths Bridge: What You Already Know and What Further Maths Changes

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| Algebra and inequalities | Compare numbers and solve equations. | Compare pay-offs and choose strategies using row minima, row maxima, column minima and column maxima. | For player B, the “best” entry may be the most negative entry in a matrix written from A’s point of view. |
| Tables and matrices | Read entries using row and column positions. | A pay-off matrix encodes the outcome of two players’ strategic choices. | Do not read the matrix symmetrically. Rows belong to A, columns belong to B. |
| Probability | Use \(p\), \(1-p\) and expected values. | A mixed strategy means playing different pure strategies with assigned probabilities. | A probability strategy is long-run behaviour, not a single guaranteed choice. |
| Straight-line graphs | Plot linear functions and solve intersections. | Graphical Game Theory uses expected winning lines and selects the highest lower envelope. | Not every intersection is chosen. The correct point maximises the minimum expected winnings. |
| Linear programming | Maximise or minimise an objective subject to constraints. | Larger zero-sum games can be converted into a linear programming problem. | Game Theory linear programming here is enrichment, not a CCEA Game Theory requirement. |

In ordinary A-Level Maths, this idea appeared as comparing quantities, solving equations and using expected values. In this enrichment topic, the same ideas become a model of strategic conflict. The key upgrade is that optimisation becomes defensive: instead of asking “What is the biggest amount I could win?”, Game Theory often asks “What is the best worst-case outcome I can guarantee?” The danger is that old habits can mislead you. A positive number is good for A and bad for B. A negative number is bad for A and good for B.

# 6. Big Picture Explanation

Game Theory is the mathematics of strategic decisions. A “game” here means a situation where there are decision-makers, each player has a choice of strategies, each player’s outcome depends on both their own choice and the other player’s choice, and the players may try to protect themselves from bad outcomes.

The lesson evidence begins with the prisoner’s dilemma because it shows something strange and important: rational individual choices can lead to a worse joint outcome. Each prisoner has an incentive to confess, but if both confess, both do worse than if both had cooperated.

For this enrichment lesson, we then move away from prisoner-style coordinate-pair payoffs and focus on **zero-sum games**. In a zero-sum game, one player’s gain is exactly balanced by the other player’s loss. That is why a single number can describe the whole outcome.

\[
\text{A wins } 4 \quad \Rightarrow \quad \text{B loses }4.
\]

\[
\text{A wins } -3 \quad \Rightarrow \quad \text{A loses }3,\quad \text{so B wins }3.
\]

# 7. Key Definitions and Notation

A **player** is a decision-maker in the game. We usually have two players, \(A\) and \(B\).

A **strategy** is one of the choices available to a player. If player A has four strategies, we may label them \(A_1,A_2,A_3,A_4\). If player B has three strategies, we may label them \(B_1,B_2,B_3\).

A **pay-off matrix** is a table showing the outcome for each combination of strategies. A typical zero-sum pay-off matrix written from player A’s point of view is:

\[
\begin{array}{c|ccc}
 & B_1 & B_2 & B_3\\
\hline
A_1 & 3 & -4 & 2\\
A_2 & -1 & 4 & -2\\
A_3 & -3 & 1 & 4\\
A_4 & 1 & -1 & 1
\end{array}
\]

The entry in row \(A_i\), column \(B_j\) is the pay-off to player A. Since the game is zero-sum,

\[
\text{B's pay-off}=-(\text{A's pay-off}).
\]

A **zero-sum game** is a game where each player’s gain or loss is exactly balanced by the losses or gains of the other player:

\[
\text{A's pay-off}+\text{B's pay-off}=0.
\]

A **play-safe strategy** is a strategy chosen by asking: what is the worst that can happen, and how can I make that worst case as good as possible?

For player A:

\[
\text{row maximin}=\max(\text{row minima}).
\]

For player B:

\[
\text{column minimax}=\min(\text{column maxima}).
\]

A game has a **stable solution** if neither player can improve by changing strategy, assuming the other player sticks with their chosen strategy. For a two-player zero-sum game:

\[
\text{stable solution exists} \iff \text{row maximin}=\text{column minimax}.
\]

A **saddle point** is an entry in the pay-off matrix that is the smallest entry in its row and the largest entry in its column.

A **pure strategy** means a player chooses one strategy definitely. A **mixed strategy** means a player chooses between strategies with assigned probabilities. If \(P(A_1)=p\), then for two strategies \(P(A_2)=1-p\), where \(0\leq p\leq1\).

The **value of the game** is the expected pay-off when optimal strategies are used. If the value to A is \(V\), then the value to B is \(-V\).

# 8. Core Theory

## 8.1 The Prisoner’s Dilemma as Context

Suppose two people, A and B, are arrested for a suspected crime. They are questioned separately and cannot communicate. If neither confesses, both go to prison for \(1\) year; if both confess, both go to prison for \(4\) years; if A confesses and B does not, A goes free and B goes to prison for \(10\) years; if B confesses and A does not, B goes free and A goes to prison for \(10\) years.

\[
\begin{array}{c|cc}
 & B\text{ confesses} & B\text{ does not confess}\\
\hline
A\text{ confesses} & (-4,-4) & (0,-10)\\
A\text{ does not confess} & (-10,0) & (-1,-1)
\end{array}
\]

Each ordered pair is \((\text{A's outcome},\text{B's outcome})\). The negative values are used because prison time is bad.

For A, confessing gives either \(-4\) or \(0\). Not confessing gives either \(-10\) or \(-1\). Since \(-4>-10\) and \(0>-1\), A seems better off confessing. B reasons symmetrically. Both confess and get \((-4,-4)\), even though mutual silence would have given \((-1,-1)\). This shows why Game Theory is not just “pick the biggest number”.

## 8.2 Reading Zero-Sum Pay-off Matrices

In a zero-sum pay-off matrix written from A’s point of view, the single entry is A’s pay-off. Positive entries are good for A and bad for B; negative entries are bad for A and good for B.

Using

\[
\begin{array}{c|ccc}
 & B_1 & B_2 & B_3\\
\hline
A_1 & 3 & -4 & 2\\
A_2 & -1 & 4 & -2\\
A_3 & -3 & 1 & 4\\
A_4 & 1 & -1 & 1
\end{array}
\]

if A plays \(A_3\) and B plays \(B_2\), the entry is \(1\). A wins \(1\), so B loses \(1\). If A plays \(A_1\) and B plays \(B_2\), the entry is \(-4\). A loses \(4\), so B wins \(4\).

**Bridge Note:** In ordinary A-Level Maths, a negative number simply meant less than zero. Here, a negative pay-off means something strategic: it is bad for A but good for B.

## 8.3 Player A’s Play-Safe Strategy: Row Maximin

Player A controls the rows. A looks across each row and finds the smallest value in that row.

For

\[
\begin{array}{c|ccc}
 & B_1 & B_2 & B_3\\
\hline
A_1 & 3 & -4 & 2\\
A_2 & -1 & 4 & -2\\
A_3 & -3 & 1 & 4\\
A_4 & 1 & -1 & 1
\end{array}
\]

Row \(A_1\):

\[
\min(3,-4,2)=-4.
\]

Row \(A_2\):

\[
\min(-1,4,-2)=-2.
\]

Row \(A_3\):

\[
\min(-3,1,4)=-3.
\]

Row \(A_4\):

\[
\min(1,-1,1)=-1.
\]

So the row minima are

\[
-4,-2,-3,-1.
\]

A chooses the largest of these:

\[
\max(-4,-2,-3,-1)=-1.
\]

Therefore:

\[
\boxed{\text{A's play-safe strategy is to play }A_4.}
\]

## 8.4 Player B’s Play-Safe Strategy: Column Minimax

Player B controls the columns. Since the matrix is written from A’s point of view, B wants A’s pay-off to be as small as possible. B first finds the maximum in each column, then chooses the smallest of those maxima.

For column \(B_1\):

\[
\max(3,-1,-3,1)=3.
\]

For column \(B_2\):

\[
\max(-4,4,1,-1)=4.
\]

For column \(B_3\):

\[
\max(2,-2,4,1)=4.
\]

So the column maxima are

\[
3,4,4.
\]

The column minimax is

\[
\min(3,4,4)=3.
\]

Therefore:

\[
\boxed{\text{B's play-safe strategy is to play }B_1.}
\]

## 8.5 Stable and Unstable Solutions

For the matrix above,

\[
\text{row maximin}=-1,
\]

and

\[
\text{column minimax}=3.
\]

Since \(-1\neq3\), there is no stable solution. The game is unstable.

A zero-sum game has a stable solution if and only if

\[
\boxed{\text{row maximin}=\text{column minimax}.}
\]

If the equality holds, the common value is the value of the game to A. Since the game is zero-sum, the value to B is its negative.

## 8.6 Saddle Points

A saddle point is an entry that is smallest in its row and largest in its column. It represents a stable solution. It is not “largest in row and smallest in column”. The saddle point is the row-player’s protected minimum and the column-player’s protected maximum meeting in the same cell.

## 8.7 Stable Solution Example

Consider

\[
\begin{array}{c|ccc}
 & B_1 & B_2 & B_3\\
\hline
A_1 & 6 & -4 & 7\\
A_2 & 8 & 5 & 9\\
A_3 & 5 & -3 & 6
\end{array}
\]

Row minima:

\[
\min(6,-4,7)=-4,
\]

\[
\min(8,5,9)=5,
\]

\[
\min(5,-3,6)=-3.
\]

So

\[
\text{row maximin}=\max(-4,5,-3)=5.
\]

Column maxima:

\[
\max(6,8,5)=8,
\]

\[
\max(-4,5,-3)=5,
\]

\[
\max(7,9,6)=9.
\]

So

\[
\text{column minimax}=\min(8,5,9)=5.
\]

Since the row maximin equals the column minimax, there is a stable solution. The stable solution is

\[
\boxed{A_2, B_2}
\]

and the value of the game to A is

\[
\boxed{5}.
\]

## 8.8 Reducing a Pay-off Matrix by Dominance

Rows are player A’s choices, so A prefers larger numbers. If every entry in one row is greater than or equal to the corresponding entry in another row, the better row dominates the worse row. The dominated row can be deleted.

Columns are player B’s choices, so B prefers smaller numbers. If every entry in one column is less than or equal to the corresponding entry in another column, the smaller column dominates the larger column. The dominated column can be deleted.

Example:

\[
\begin{array}{c|ccc}
 & B_1 & B_2 & B_3\\
\hline
A_1 & 3 & 0 & 1\\
A_2 & 1 & -1 & 5\\
A_3 & 5 & 2 & 2
\end{array}
\]

Compare \(A_3\) with \(A_1\):

\[
5>3,\quad 2>0,\quad 2>1.
\]

So row \(A_3\) dominates row \(A_1\), and row \(A_1\) can be deleted.

Compare \(B_2\) with \(B_1\):

\[
0<3,\quad -1<1,\quad 2<5.
\]

So column \(B_2\) dominates column \(B_1\), and column \(B_1\) can be deleted.

## 8.9 Mixed Strategies for Unstable Games

If a game has no stable solution, pure strategies may not be enough. A player may use a mixed strategy.

For

\[
\begin{array}{c|cc}
 & B_1 & B_2\\
\hline
A_1 & 4 & -2\\
A_2 & -5 & 3
\end{array}
\]

let

\[
P(A_1)=p,\quad P(A_2)=1-p.
\]

If B plays \(B_1\), A’s expected winnings are

\[
E_1=4p+(-5)(1-p)=4p-5+5p=9p-5.
\]

If B plays \(B_2\), A’s expected winnings are

\[
E_2=(-2)p+3(1-p)=-2p+3-3p=3-5p.
\]

Equalise the two expected winnings:

\[
9p-5=3-5p.
\]

Add \(5p\) to both sides:

\[
14p-5=3.
\]

Add \(5\) to both sides:

\[
14p=8.
\]

Divide by \(14\):

\[
p=\frac{8}{14}=\frac47.
\]

Therefore

\[
P(A_1)=\frac47,\quad P(A_2)=\frac37.
\]

The value to A is

\[
9\left(\frac47\right)-5=\frac{36}{7}-\frac{35}{7}=\frac17.
\]

So

\[
\boxed{\text{value to A}=\frac17},\quad \boxed{\text{value to B}=-\frac17}.
\]

## 8.10 Mixed Strategy for Player B

Let

\[
P(B_1)=q,\quad P(B_2)=1-q.
\]

Because the matrix is from A’s point of view, B’s expected winnings are the negative of A’s expected pay-offs.

If A plays \(A_1\), A’s expected pay-off is

\[
4q+(-2)(1-q)=4q-2+2q=6q-2.
\]

So B’s expected winning is

\[
F_1=-(6q-2)=2-6q.
\]

If A plays \(A_2\), A’s expected pay-off is

\[
(-5)q+3(1-q)=-5q+3-3q=3-8q.
\]

So B’s expected winning is

\[
F_2=-(3-8q)=8q-3.
\]

Equalise:

\[
2-6q=8q-3.
\]

Add \(6q\) to both sides:

\[
2=14q-3.
\]

Add \(3\) to both sides:

\[
5=14q.
\]

So

\[
q=\frac5{14}.
\]

Therefore

\[
P(B_1)=\frac5{14},\quad P(B_2)=\frac9{14}.
\]

The value to B is

\[
2-6\left(\frac5{14}\right)=2-\frac{30}{14}=2-\frac{15}{7}=\frac{14}{7}-\frac{15}{7}=-\frac17.
\]

## 8.11 Graphical Method

The graphical method plots expected winnings as straight lines. For the matrix above,

\[
E_1=9p-5,
\]

\[
E_2=3-5p.
\]

At \(p=0\),

\[
E_1=-5,\quad E_2=3.
\]

At \(p=1\),

\[
E_1=4,\quad E_2=-2.
\]

The optimal point is the intersection that gives the **highest minimum expected winning**. Solve

\[
9p-5=3-5p
\]

which gives

\[
p=\frac47,\quad V=\frac17.
\]

With three lines, not every intersection matters. The correct point is the point on the lower envelope that is as high as possible.

## 8.12 Linear Programming Enrichment

If a larger game cannot be reduced so that one player has only two choices, it can be formulated as a linear programming problem.

Suppose the original matrix is

\[
M=\begin{pmatrix}
-2 & 4 & 2\\
0 & -3 & -3\\
-2 & -6 & 1
\end{pmatrix}.
\]

The smallest entry is \(-6\). Add \(7\) to every entry so that all entries are positive:

\[
M+7=\begin{pmatrix}
5 & 11 & 9\\
7 & 4 & 4\\
5 & 1 & 8
\end{pmatrix}.
\]

Let

\[
p_1=P(A_1),\quad p_2=P(A_2),\quad p_3=P(A_3).
\]

Then

\[
p_1+p_2+p_3=1,
\]

and

\[
p_1,p_2,p_3\geq0.
\]

Let \(v\) be the value of the original game and \(V\) be the value of the augmented game. Since every entry has had \(7\) added,

\[
V=v+7,
\]

so

\[
v=V-7.
\]

The constraints are:

\[
5p_1+7p_2+5p_3\geq V,
\]

\[
11p_1+4p_2+p_3\geq V,
\]

\[
9p_1+4p_2+8p_3\geq V.
\]

The objective is:

\[
\boxed{\text{Maximise }V.}
\]

This section is enrichment only.

# 9. Visual Asset Integration

[VISUAL PLACEHOLDER: FA22GameTheoryEnrichmentMermaid-001 | Source: CCEA boundary check + Decision 2 transcript evidence | Insert from mermaid/FA22GameTheoryEnrichmentMermaid-001.md | Purpose: Show that Game Theory is optional enrichment and map the learning flow from pay-off matrices to mixed strategies and linear programming.]

[VISUAL PLACEHOLDER: FA22GameTheoryEnrichmentSVG-001 | Source: Screenshot PDF pages showing prisoner’s dilemma + transcript explanation | Insert from svg/FA22GameTheoryEnrichmentSVG-001.svg | Purpose: Preserve the prisoner’s dilemma coordinate-pair pay-off table as enrichment context.]

[VISUAL PLACEHOLDER: FA22GameTheoryEnrichmentSVG-002 | Source: Transcript explanation of zero-sum games and pay-off matrices | Insert from svg/FA22GameTheoryEnrichmentSVG-002.svg | Purpose: Show how a single pay-off entry gives A’s win and B’s loss.]

[VISUAL PLACEHOLDER: FA22GameTheoryEnrichmentSVG-003 | Source: Transcript and screenshot PDF play-safe strategy annotations | Insert from svg/FA22GameTheoryEnrichmentSVG-003.svg | Purpose: Show row minima, row maximin, column maxima and column minimax on one pay-off matrix.]

[VISUAL PLACEHOLDER: FA22GameTheoryEnrichmentSVG-004 | Source: Transcript explanation of saddle point | Insert from svg/FA22GameTheoryEnrichmentSVG-004.svg | Purpose: Show why a saddle point is smallest in its row but largest in its column.]

[VISUAL PLACEHOLDER: FA22GameTheoryEnrichmentSVG-005 | Source: Transcript section on reducing the pay-off matrix | Insert from svg/FA22GameTheoryEnrichmentSVG-005.svg | Purpose: Show how dominated rows and columns are deleted.]

[VISUAL PLACEHOLDER: FA22GameTheoryEnrichmentTikZ-001 | Source: Transcript graphical method for two expected winnings lines | Insert from tikz/FA22GameTheoryEnrichmentTikZ-001.tex | Purpose: Draw the \(p=0\) to \(p=1\) graphical method with expected winnings lines.]

[VISUAL PLACEHOLDER: FA22GameTheoryEnrichmentTikZ-002 | Source: Transcript graphical method for 2 by 3 or 3 by 2 games | Insert from tikz/FA22GameTheoryEnrichmentTikZ-002.tex | Purpose: Show that with three expected-winnings lines, not every intersection is optimal.]

[VISUAL PLACEHOLDER: FA22GameTheoryEnrichmentTikZ-003 | Source: Transcript linear programming section | Insert from tikz/FA22GameTheoryEnrichmentTikZ-003.tex | Purpose: Show the conversion from a 3 by 3 pay-off matrix to augmented matrix, probability variables and constraints.]

[VISUAL PLACEHOLDER: FA22GameTheoryEnrichmentBridgeSVG-001 | Source: Ordinary A-Level Maths bridge + Game Theory enrichment evidence | Insert from svg/FA22GameTheoryEnrichmentBridgeSVG-001.svg | Purpose: Compare ordinary algebra/probability/optimisation with Game Theory enrichment methods.]

# 10. Interactive Learning Widgets

[INTERACTIVE PLACEHOLDER: FA22GameTheoryEnrichmentWidget-001 | Source: AI-proposed teaching enhancement based on transcript and screenshot evidence | Insert from widgets/FA22GameTheoryEnrichmentWidget-001.html | Purpose: Help students read a zero-sum pay-off matrix from A’s point of view.]

[INTERACTIVE PLACEHOLDER: FA22GameTheoryEnrichmentWidget-002 | Source: AI-proposed teaching enhancement based on play-safe strategy evidence | Insert from widgets/FA22GameTheoryEnrichmentWidget-002.html | Purpose: Calculate row minima, row maximin, column maxima, column minimax and stability.]

[INTERACTIVE PLACEHOLDER: FA22GameTheoryEnrichmentWidget-003 | Source: AI-proposed teaching enhancement based on saddle point evidence | Insert from widgets/FA22GameTheoryEnrichmentWidget-003.html | Purpose: Help students identify saddle points visually.]

[INTERACTIVE PLACEHOLDER: FA22GameTheoryEnrichmentWidget-004 | Source: AI-proposed teaching enhancement based on matrix reduction evidence | Insert from widgets/FA22GameTheoryEnrichmentWidget-004.html | Purpose: Let students test whether a row or column is dominated.]

[INTERACTIVE PLACEHOLDER: FA22GameTheoryEnrichmentWidget-005 | Source: AI-proposed teaching enhancement based on graphical method evidence | Insert from widgets/FA22GameTheoryEnrichmentWidget-005.html | Purpose: Explore \(p\), \(1-p\), expected winnings lines and the optimal mixed strategy.]

# 11. Worked Examples

## Worked Example 1: Reading a Zero-Sum Pay-off Matrix

The following pay-off matrix is written from player A’s point of view:

\[
\begin{array}{c|ccc}
 & B_1 & B_2 & B_3\\
\hline
A_1 & 3 & -4 & 2\\
A_2 & -1 & 4 & -2\\
A_3 & -3 & 1 & 4\\
A_4 & 1 & -1 & 1
\end{array}
\]

If A plays \(A_3\) and B plays \(B_2\), the entry is \(1\). Since the matrix is written from A’s point of view, A wins \(1\), and B loses \(1\). If A plays \(A_1\) and B plays \(B_2\), the entry is \(-4\). A loses \(4\), and B wins \(4\).

## Worked Example 2: Finding Play-Safe Strategies

For

\[
\begin{array}{c|ccc}
 & B_1 & B_2 & B_3\\
\hline
A_1 & 3 & -4 & 2\\
A_2 & -1 & 4 & -2\\
A_3 & -3 & 1 & 4\\
A_4 & 1 & -1 & 1
\end{array}
\]

A’s row minima are \(-4,-2,-3,-1\), so A’s row maximin is \(-1\), and A plays \(A_4\). B’s column maxima are \(3,4,4\), so B’s column minimax is \(3\), and B plays \(B_1\). Since \(-1\neq3\), there is no stable solution.

## Worked Example 3: Stable Solution and Value

For

\[
\begin{array}{c|ccc}
 & B_1 & B_2 & B_3\\
\hline
A_1 & 6 & -4 & 7\\
A_2 & 8 & 5 & 9\\
A_3 & 5 & -3 & 6
\end{array}
\]

row minima are \(-4,5,-3\), so the row maximin is \(5\). Column maxima are \(8,5,9\), so the column minimax is \(5\). Therefore there is a stable solution at \((A_2,B_2)\), and the value of the game to A is \(5\).

## Worked Example 4: Reducing a Matrix by Dominance

For

\[
\begin{array}{c|ccc}
 & B_1 & B_2 & B_3\\
\hline
A_1 & 7 & 1 & -2\\
A_2 & -3 & 6 & 1\\
A_3 & 4 & 0 & -3
\end{array}
\]

Compare \(A_1\) with \(A_3\):

\[
7>4,\quad 1>0,\quad -2>-3.
\]

So \(A_1\) dominates \(A_3\), and row \(A_3\) can be deleted. Using the remaining rows, compare \(B_3\) with \(B_2\):

\[
-2<1,\quad 1<6.
\]

So \(B_3\) dominates \(B_2\), and column \(B_2\) can be deleted. The reduced matrix is

\[
\begin{array}{c|cc}
 & B_1 & B_3\\
\hline
A_1 & 7 & -2\\
A_2 & -3 & 1
\end{array}.
\]

## Worked Example 5: Mixed Strategy for A

For

\[
\begin{array}{c|cc}
 & B_1 & B_2\\
\hline
A_1 & 4 & -2\\
A_2 & -5 & 3
\end{array}
\]

let \(P(A_1)=p\), so \(P(A_2)=1-p\). If B plays \(B_1\),

\[
E_1=4p-5(1-p)=9p-5.
\]

If B plays \(B_2\),

\[
E_2=-2p+3(1-p)=3-5p.
\]

Set them equal:

\[
9p-5=3-5p,
\]

\[
14p=8,
\]

\[
p=\frac47.
\]

So A plays \(A_1\) with probability \(\frac47\) and \(A_2\) with probability \(\frac37\). The value is

\[
9\left(\frac47\right)-5=\frac17.
\]

# 12. Common Mistakes and Exam Traps

- Treating a negative entry as bad for both players. In a matrix written from A’s point of view, negative is bad for A and good for B.
- Using row maxima instead of row minima for A.
- Using column minima instead of column maxima for B.
- Claiming a stable solution just because play-safe strategies exist.
- Reversing the saddle point definition. It is smallest in its row and largest in its column.
- Deleting the dominant row instead of the dominated row.
- Deleting the dominant column instead of the dominated column.
- Forgetting to negate A’s pay-offs when calculating B’s mixed strategy.
- Choosing the wrong intersection in a graphical method with three or more lines.
- Forgetting that probabilities must satisfy \(0\leq p\leq1\).
- Forgetting to undo augmentation in linear programming enrichment: if \(V=v+k\), then \(v=V-k\).
- Treating this enrichment as core CCEA content.

# 13. Practice Questions

These are AI-generated enrichment questions based on the lesson evidence. They are not past-paper questions.

## Question 1

The following pay-off matrix is written from A’s point of view:

\[
\begin{array}{c|cc}
 & B_1 & B_2\\
\hline
A_1 & 5 & -2\\
A_2 & -1 & 3
\end{array}
\]

1. What is A’s pay-off if A plays \(A_1\) and B plays \(B_2\)?
2. What is B’s pay-off if A plays \(A_1\) and B plays \(B_2\)?
3. What is B’s pay-off if A plays \(A_2\) and B plays \(B_1\)?

## Question 2

For

\[
\begin{array}{c|ccc}
 & B_1 & B_2 & B_3\\
\hline
A_1 & 4 & 1 & -3\\
A_2 & 2 & -2 & 5\\
A_3 & -1 & 3 & 0
\end{array}
\]

find A’s play-safe strategy and B’s play-safe strategy.

## Question 3

For

\[
\begin{array}{c|ccc}
 & B_1 & B_2 & B_3\\
\hline
A_1 & 2 & -1 & 4\\
A_2 & 3 & 2 & 5\\
A_3 & -2 & 0 & 1
\end{array}
\]

find the row maximin, the column minimax, and decide whether the game has a stable solution.

## Question 4

Reduce the following matrix by dominance, if possible:

\[
\begin{array}{c|ccc}
 & B_1 & B_2 & B_3\\
\hline
A_1 & 1 & 5 & 2\\
A_2 & 3 & 6 & 4\\
A_3 & 0 & 2 & -1
\end{array}
\]

## Question 5

For

\[
\begin{array}{c|cc}
 & B_1 & B_2\\
\hline
A_1 & 6 & -1\\
A_2 & -2 & 4
\end{array}
\]

find A’s optimal mixed strategy and the value of the game to A.

## Question 6

For the same matrix as Question 5, find B’s optimal mixed strategy and the value of the game to B.

## Question 7

For

\[
\begin{array}{c|ccc}
 & B_1 & B_2 & B_3\\
\hline
A_1 & -2 & 4 & 2\\
A_2 & 0 & -3 & -3\\
A_3 & -2 & -6 & 1
\end{array}
\]

1. Explain why augmentation is needed before forming a standard linear programming problem.
2. Augment the matrix by \(7\).
3. Define \(p_1,p_2,p_3\).
4. Write the probability constraint.
5. Write the expected pay-off constraints for A in terms of \(V\), the value of the augmented game.

# 14. Worked Solutions

## Solution 1

The entry for \(A_1,B_2\) is \(-2\). So A’s pay-off is \(-2\). Since the game is zero-sum, B’s pay-off is \(-(-2)=2\). The entry for \(A_2,B_1\) is \(-1\), so B’s pay-off is \(-(-1)=1\).

## Solution 2

Row minima:

\[
\min(4,1,-3)=-3,
\]

\[
\min(2,-2,5)=-2,
\]

\[
\min(-1,3,0)=-1.
\]

So the row maximin is \(-1\), and A plays \(A_3\).

Column maxima:

\[
\max(4,2,-1)=4,
\]

\[
\max(1,-2,3)=3,
\]

\[
\max(-3,5,0)=5.
\]

So the column minimax is \(3\), and B plays \(B_2\).

## Solution 3

Row minima:

\[
\min(2,-1,4)=-1,
\]

\[
\min(3,2,5)=2,
\]

\[
\min(-2,0,1)=-2.
\]

So the row maximin is \(2\). Column maxima:

\[
\max(2,3,-2)=3,
\]

\[
\max(-1,2,0)=2,
\]

\[
\max(4,5,1)=5.
\]

So the column minimax is \(2\). Since they are equal, there is a stable solution. The value of the game to A is \(2\), and the stable solution is \((A_2,B_2)\).

## Solution 4

Compare row \(A_2\) with row \(A_1\):

\[
3>1,\quad 6>5,\quad 4>2.
\]

So row \(A_2\) dominates row \(A_1\). Compare row \(A_2\) with row \(A_3\):

\[
3>0,\quad 6>2,\quad 4>-1.
\]

So row \(A_2\) dominates row \(A_3\). Only row \(A_2\) remains. B chooses the smallest entry in that row, which is \(3\), so the reduced outcome is \((A_2,B_1)\) with pay-off \(3\).

## Solution 5

Let \(P(A_1)=p\), so \(P(A_2)=1-p\). If B plays \(B_1\),

\[
E_1=6p-2(1-p)=8p-2.
\]

If B plays \(B_2\),

\[
E_2=-p+4(1-p)=4-5p.
\]

Set equal:

\[
8p-2=4-5p.
\]

\[
13p=6.
\]

\[
p=\frac6{13}.
\]

So A plays \(A_1\) with probability \(\frac6{13}\) and \(A_2\) with probability \(\frac7{13}\). The value to A is

\[
8\left(\frac6{13}\right)-2=\frac{48}{13}-\frac{26}{13}=\frac{22}{13}.
\]

## Solution 6

Let \(P(B_1)=q\), so \(P(B_2)=1-q\). If A plays \(A_1\), A’s expected pay-off is

\[
6q-(1-q)=7q-1.
\]

B’s expected winning is

\[
F_1=1-7q.
\]

If A plays \(A_2\), A’s expected pay-off is

\[
-2q+4(1-q)=4-6q.
\]

B’s expected winning is

\[
F_2=6q-4.
\]

Set equal:

\[
1-7q=6q-4.
\]

\[
5=13q.
\]

\[
q=\frac5{13}.
\]

So B plays \(B_1\) with probability \(\frac5{13}\) and \(B_2\) with probability \(\frac8{13}\). The value to B is

\[
1-7\left(\frac5{13}\right)=\frac{13}{13}-\frac{35}{13}=-\frac{22}{13}.
\]

## Solution 7

The smallest entry is \(-6\), so add \(7\) to every entry to make all entries positive.

\[
\begin{array}{c|ccc}
 & B_1 & B_2 & B_3\\
\hline
A_1 & 5 & 11 & 9\\
A_2 & 7 & 4 & 4\\
A_3 & 5 & 1 & 8
\end{array}
\]

Let

\[
p_1=P(A_1),\quad p_2=P(A_2),\quad p_3=P(A_3).
\]

The probability constraint is

\[
p_1+p_2+p_3=1,
\]

with

\[
p_1,p_2,p_3\geq0.
\]

If \(V\) is the value of the augmented game, the expected pay-off constraints are

\[
5p_1+7p_2+5p_3\geq V,
\]

\[
11p_1+4p_2+p_3\geq V,
\]

\[
9p_1+4p_2+8p_3\geq V.
\]

The objective is to maximise \(V\), and the original game value is \(v=V-7\).

# 15. Exam Technique Notes

Always state that the matrix is written from A’s point of view. For A, use row minima then row maximin. For B, use column maxima then column minimax. Quote the stable solution theorem. State the value of the game with the correct sign. For dominance, show the entry-by-entry comparisons. For mixed strategies, use exact fractions where possible. For B’s mixed strategy, explicitly negate A’s expected pay-off. For graphical methods, choose the highest lower-envelope point. For linear programming enrichment, undo augmentation.

# 16. Syllabus Gap Check

| Enrichment ID | Objective | Covered? |
|---|---|---|
| `ENR-GT-001` | Explain what Game Theory studies. | Yes |
| `ENR-GT-002` | Interpret a pay-off matrix from A’s point of view. | Yes |
| `ENR-GT-003` | Explain zero-sum games. | Yes |
| `ENR-GT-004` | Find A’s play-safe strategy. | Yes |
| `ENR-GT-005` | Find B’s play-safe strategy. | Yes |
| `ENR-GT-006` | Decide whether a game has a stable solution. | Yes |
| `ENR-GT-007` | Identify saddle point. | Yes |
| `ENR-GT-008` | Reduce a pay-off matrix by dominance. | Yes |
| `ENR-GT-009` | Use mixed strategies and expected winnings. | Yes |
| `ENR-GT-010` | Understand linear programming formulation. | Yes |

No official CCEA Game Theory LO is claimed. Game Theory remains optional enrichment only.

## Off-Spec Content Found but Excluded from Core

| Off-spec content | Treatment |
|---|---|
| Game Theory chapter | Built as optional enrichment only. |
| Prisoner’s dilemma | Included as enrichment context only. |
| Decision 2 exercise labels | Preserved as evidence context, not CCEA topic labels. |
| Pay-off matrix reduction | Enrichment only. |
| Mixed strategies | Enrichment only. |
| Game Theory linear programming | Enrichment only, with CCEA boundary warning. |

# 17. Recommended Enhancements Not in the Evidence

AI-proposed enhancements include the pay-off matrix reader, maximin/minimax calculator, saddle point detector, dominance comparison tool, mixed strategy graph explorer, bridge diagram, saddle point surface sketch and lower-envelope diagrams. These are proposed enhancements, not official evidence-backed CCEA content.

# 18. Supplementary Sources Used

Project Sources used: CCEA GCE Further Mathematics Specification Map, Further Maths README module map, Further Maths Evidence Drop Checklist, Ordinary A-Level Mathematics bridge extracts and Further Maths Portal Build Knowledge Evidence.

Lesson-specific evidence used: `transcripts.md` and `Chapter_6_Game_Theory_⌨️_(Decision_2)_screenshots.pdf`.

Ordinary A-Level Mathematics evidence was used only as bridge context for inequalities, probability, expected value, straight-line graphs, matrices and optimisation. It was not used as authority to add Game Theory to the CCEA Further Mathematics specification.

# 19. Final Student Checklist

## Prerequisite Confidence Checklist

- [ ] I can read a table using row and column headings.
- [ ] I can compare negative numbers correctly.
- [ ] I can find the maximum and minimum of a list.
- [ ] I can solve a linear equation.
- [ ] I can use probabilities such as \(p\) and \(1-p\).
- [ ] I can calculate an expected value.
- [ ] I can sketch or interpret straight-line graphs.

## Game Theory Method Checklist

- [ ] I can explain what a pay-off matrix represents.
- [ ] I can state that a zero-sum game has total pay-off zero.
- [ ] I can interpret positive entries as good for A.
- [ ] I can interpret negative entries as good for B.
- [ ] I can find A’s row minima and row maximin.
- [ ] I can find B’s column maxima and column minimax.
- [ ] I can test for a stable solution.
- [ ] I can identify a saddle point.
- [ ] I can reduce a matrix by dominance.
- [ ] I can form expected winnings for a mixed strategy.
- [ ] I can find the value of the game.

## Boundary Checklist

- [ ] I understand this is optional enrichment.
- [ ] I understand Game Theory is not confirmed as a CCEA Further Mathematics topic in the supplied Project Sources.
- [ ] I understand no official CCEA Game Theory LO IDs were found.
