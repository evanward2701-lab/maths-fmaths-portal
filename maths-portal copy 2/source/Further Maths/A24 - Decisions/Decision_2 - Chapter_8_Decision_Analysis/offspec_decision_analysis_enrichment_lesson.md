# offspec_decision_analysis_enrichment_lesson.md

# 1. Lesson Title and Metadata

## Lesson title

**Off-Spec Enrichment: Decision Analysis, Decision Trees, EMV and Utility**

## Metadata

| Field | Value |
|---|---|
| Date generated | 2026-06-04 |
| Portal status | Optional enrichment lesson |
| CCEA Further Mathematics status | Off-spec enrichment only |
| CCEA unit code | Not applicable |
| CCEA topic code | Not applicable |
| CCEA LO IDs | None found |
| Enrichment topic code | OFFSPEC-DA |
| Topic name | Decision Analysis |
| Topic slug | decision_analysis |
| Topic Pascal | DecisionAnalysis |
| Topic ID | OffSpecDecisionAnalysis |
| Suggested lesson file | offspec_decision_analysis_enrichment_lesson.md |
| Applied section | Decision Mathematics enrichment |
| Core warning | This lesson is not part of the supplied CCEA GCE Further Mathematics specification map unless a valid CCEA source is later supplied. |
| Bridge tags | Probability trees, expected value, binomial distribution, exponential functions, logarithms |
| Topic tags | Decision trees, EMV, utility, expected utility, risk aversion, payoff, strategy |

## Off-spec boundary statement

This lesson is designed as a **mathematical enrichment chapter** for a Further Mathematics portal. It should not be presented as required CCEA Further Mathematics content.

The supplied evidence is from a **Decision 2** style chapter titled **Decision Analysis**, covering decision trees, EMV and utility. The supplied CCEA Further Mathematics map did not identify a matching CCEA learning outcome for this topic. Therefore:

- no CCEA LO IDs are assigned;
- no CCEA topic code is invented;
- all examples are treated as enrichment;
- any “exam-style” wording is from the supplied Decision 2 material, not claimed as CCEA exam wording.

---

# 2. Evidence Map

| Evidence source | Type | How it is used |
|---|---|---|
| `transcripts.md` | Teacher transcript | Main mathematical evidence for decision trees, EMV, utility, risk aversion, worked examples and warnings. |
| `Chapter_8_Decision_Analysis_⌨️_(Decision_2)_screenshots.pdf` | Screenshot PDF | Visual evidence for the chapter title, opening decision-analysis summary, node shapes and diagrams. |
| CCEA Further Mathematics specification map | Project source | Used only to establish that this chapter is not currently mapped to a CCEA Further Mathematics LO. |
| Ordinary CCEA A-Level Mathematics bridge extracts | Project bridge source | Used only for prerequisite context: probability trees, expected value, binomial probability, exponentials and logarithms. |

## Evidence limitations

The screenshot PDF contains image pages rather than searchable text. The first pages were readable through rendered previews, but the entire PDF was not fully transcribed here. The transcript is therefore the main text evidence for worked examples.

Visual evidence is partially image-based. Diagram descriptions below preserve the visible/readable details and the transcript descriptions only. No uninspected visual detail is claimed.

---

# 3. Specification Alignment

## CCEA alignment table

| CCEA LO ID | Official wording | Lesson coverage | Boundary decision |
|---|---|---|---|
| None found | None found for Decision Analysis, decision trees, EMV or utility | This lesson covers these ideas as enrichment | Off-spec. Do not treat as CCEA-assessed content. |

## Enrichment objective table

These are **not CCEA LO IDs**. They are internal enrichment objectives for the portal.

| Enrichment objective ID | Student should be able to… | Evidence source |
|---|---|---|
| OFFSPEC-DA-EO001 | distinguish decision nodes, chance nodes and end/pay-off nodes | Transcript and screenshot evidence |
| OFFSPEC-DA-EO002 | draw a decision tree from a written scenario | Transcript examples |
| OFFSPEC-DA-EO003 | calculate expected monetary value, EMV, at a chance node | Transcript examples |
| OFFSPEC-DA-EO004 | choose an optimal strategy by comparing EMVs at decision nodes | Transcript examples |
| OFFSPEC-DA-EO005 | use double-line crossing to reject unused decision branches | Transcript explanation |
| OFFSPEC-DA-EO006 | explain why decision trees resemble but are not probability trees | Transcript warnings |
| OFFSPEC-DA-EO007 | calculate expected utility by transforming payoffs using a utility function | Utility transcript |
| OFFSPEC-DA-EO008 | interpret the role of a risk-aversion parameter such as \(R\) | Utility transcript |
| OFFSPEC-DA-EO009 | solve threshold-prize problems using utility inequalities | Tim/Aisha-style transcript examples |

---

# 4. Learning Objectives

## Enrichment objectives

By the end of this lesson, you should be able to:

1. explain what decision analysis is for;
2. identify the three key node shapes in a decision tree;
3. build a tree from left to right using decisions, chance events and pay-offs;
4. place probabilities only on branches from chance nodes;
5. place pay-offs next to end/pay-off nodes;
6. calculate EMV using weighted averages;
7. write EMV values inside chance nodes;
8. write the best available value inside a decision node;
9. cross off rejected decision branches with a double line;
10. explain why EMV can be misleading when risk matters;
11. convert monetary pay-offs into utility values;
12. calculate expected utility;
13. decide whether an option is preferable under EMV or utility;
14. solve simple inequalities involving utility functions.

## Bridge objectives

You should also be able to connect this enrichment topic back to ordinary A-Level Mathematics by using:

- probability trees;
- sample spaces;
- expected value;
- binomial modelling;
- exponential functions;
- logarithms;
- inequalities.

## Exam-technique objectives

Even though this is off-spec for CCEA, the Decision 2-style technique is strict:

- label every branch;
- use the correct node shape;
- do not put probabilities on decision branches;
- show working for each EMV or expected utility;
- compare only like with like;
- cross off decision branches only, never chance branches;
- state the strategy in words after completing the tree.

---

# 5. Explicit Prerequisite Recap

## GCSE foundations

You should already be comfortable with:

- fractions;
- decimals;
- percentages;
- multiplying fractions;
- probability as:

\[
\frac{\text{number of successful outcomes}}{\text{number of possible outcomes}};
\]

- listing outcomes in a sample space;
- negative numbers for losses;
- interpreting money values such as \(£4\), \(-£2\), \(25\text{p}\).

## Ordinary A-Level Mathematics foundations

You should already know:

- probability trees;
- independent events;
- mutually exclusive branches;
- expected value as:

\[
E(X)=\sum xP(X=x);
\]

- binomial distribution ideas for repeated independent trials;
- exponentials such as \(e^x\);
- logarithms as the inverse of exponentials.

## A-Level Maths Bridge: What You Already Know and What Further Maths Changes

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| Probability trees | Branches represent random outcomes and probabilities are written on branches. | Decision trees also use branches, but some branches represent choices, not random outcomes. | A decision branch has no probability. Do not force probabilities onto decisions. |
| Expected value | For a random variable \(X\), calculate \(E(X)=\sum xP(X=x)\). | EMV is the same weighted-average idea applied to monetary pay-offs at chance nodes. | EMV is long-run average money, not a guarantee for one play. |
| Sample spaces | Count outcomes such as dice totals. | Decision analysis often needs sample-space work before filling probabilities on the tree. | The tree structure is useless if the probabilities are wrong. |
| Binomial distribution | Use \(X\sim\operatorname{Bin}(n,p)\) for repeated independent trials. | Some decision problems use a binomial model to calculate the chance that at least one person wins. | Check whether “at least one” means \(1-P(X=0)\). |
| Exponentials and logarithms | Use \(e^x\), \(e^{-x}\) and logarithms to solve equations. | Utility functions such as \(U(x)=1-e^{-x/R}\) transform money into subjective value. | Utility is not ordinary probability; it measures subjective value or risk preference. |

In ordinary A-Level Maths, this idea appeared as probability trees and expected value. In this enrichment lesson, the same machinery becomes a decision-making system: some branches are choices, some branches are random events, and pay-offs are rolled backwards through the tree.

The key upgrade is that decisions are optimised backwards. The danger is treating the whole thing like a probability tree. Probability trees flow forward. Decision trees are drawn forward but evaluated backward.

---

# 6. Big Picture Explanation

Decision analysis is used when a person or organisation faces a chain of choices and uncertain outcomes.

A normal probability tree asks:

> What is the probability of this outcome?

A decision tree asks:

> Which action should I choose, given the possible outcomes?

The structure is like a railway junction in a foggy finance forest:

- a **decision node** is where the driver chooses a track;
- a **chance node** is where the weather, dice, market or game decides what happens;
- an **end/pay-off node** is where the journey stops and the final value is recorded.

The basic method is:

1. draw the tree from left to right;
2. label all decisions and chance outcomes;
3. put probabilities only after chance nodes;
4. write pay-offs at the end;
5. work backwards;
6. calculate EMVs at chance nodes;
7. choose the highest value at decision nodes;
8. cross off rejected decision branches;
9. state the best strategy.

For risk-neutral decision-making, use **expected monetary value**.

For risk-sensitive decision-making, use **expected utility**.

---

# 7. Key Definitions and Notation

## Decision analysis

Decision analysis is a way to organise decisions and outcomes when there are several choices and uncertain results.

## Decision tree

A **decision tree** is a diagram showing decisions, chance events and final pay-offs.

## Decision node

A **decision node** is drawn as a box or rectangle.

It represents a choice made by the person or organisation.

Example:

\[
\boxed{\phantom{D}}
\]

At a decision node, there is no probability attached to the outgoing branches. The person chooses one of the branches.

## Chance node

A **chance node** is drawn as a circle.

It represents a random event.

Example:

\[
\bigcirc
\]

Probabilities are written on branches coming out of a chance node.

## End node or pay-off node

An **end node**, also called a **pay-off node**, is drawn as a backwards triangle.

It represents the end of a branch.

A pay-off value is written next to it.

## Pay-off

A **pay-off** is the final monetary outcome or value attached to an end node.

Positive pay-offs are gains.

Negative pay-offs are losses.

Examples:

\[
4,\quad -2,\quad 0,\quad -1600,\quad 400.
\]

## Expected monetary value, EMV

The **expected monetary value** is the weighted average monetary outcome at a chance node.

If a chance node has outcomes \(x_1,x_2,\ldots,x_n\) with probabilities \(p_1,p_2,\ldots,p_n\), then:

\[
\operatorname{EMV}=p_1x_1+p_2x_2+\cdots+p_nx_n.
\]

Equivalently:

\[
\operatorname{EMV}=\sum p_ix_i.
\]

## Optimal strategy

An **optimal strategy** is the best set of choices indicated by the decision tree.

Usually, this means choosing the branch with the greatest EMV or expected utility.

## Utility

**Utility** is a numerical measure of how useful, important or attractive an outcome is to a decision-maker.

Utility may differ between people, because different people have different attitudes to risk.

## Utility function

A **utility function** transforms money or pay-off into utility.

One common form in the evidence is:

\[
U(x)=1-e^{-x/R},
\]

where:

- \(x\) is the monetary pay-off;
- \(R>0\) is a parameter linked to risk attitude;
- \(U(x)\) is the utility of the pay-off.

## Expected utility

Expected utility is calculated like EMV, but using utilities instead of monetary pay-offs.

If a chance node has utility outcomes \(u_1,u_2,\ldots,u_n\) with probabilities \(p_1,p_2,\ldots,p_n\), then:

\[
\operatorname{Expected\ Utility}=p_1u_1+p_2u_2+\cdots+p_nu_n.
\]

## Risk aversion

A decision-maker is **risk averse** if losses feel especially bad compared with equal-sized gains.

In the utility function:

\[
U(x)=1-e^{-x/R},
\]

a smaller value of \(R\) makes losses more damaging in utility terms.

---

# 8. Core Theory

## 8.1 The three node shapes

A decision tree uses three main shapes.

| Situation | Shape | Name | What goes on outgoing branches? |
|---|---|---|---|
| A person or organisation chooses | Box/rectangle | Decision node | Decision labels only |
| A random event occurs | Circle | Chance node | Probabilities and outcome labels |
| A branch finishes | Backwards triangle | End/pay-off node | No outgoing branches |

**Bridge Note:** In ordinary A-Level probability trees, most branch points are chance events. Here, decision analysis separates a voluntary choice from a random outcome.

## 8.2 Why decision trees are not probability trees

A probability tree usually has probabilities on every branch.

A decision tree does not.

At a decision node, the person chooses. There is no probability such as \(0.5\) for “play” unless the question explicitly models a random choice. In decision analysis, the decision-maker is not random.

So:

\[
\text{decision branch} \neq \text{probability branch}.
\]

**Warning:** Do not write probabilities after a box unless the question says the choice itself is random.

## 8.3 How to draw a decision tree

Use this order:

1. Start with the first decision.
2. Draw a decision node.
3. Add one branch for each possible decision.
4. If a branch immediately ends, draw an end/pay-off node.
5. If a branch leads to a random event, draw a chance node.
6. Add chance branches and probabilities.
7. Continue until every branch ends.
8. Write final pay-offs next to end nodes.

## 8.4 How to evaluate a tree

Decision trees are drawn left to right but evaluated right to left.

At a chance node, calculate:

\[
\operatorname{EMV}=\sum p_ix_i.
\]

At a decision node, choose the branch with the greatest value.

For example, if the two available branches are worth:

\[
0.25 \quad \text{and} \quad 0,
\]

then choose \(0.25\).

If the two available branches are worth:

\[
-1 \quad \text{and} \quad -2,
\]

then choose \(-1\), because:

\[
-1>-2.
\]

A smaller loss is better.

## 8.5 Crossing off branches

Rejected decision branches can be crossed off with a double line.

Only cross off branches coming out of decision nodes.

Do not cross off chance branches, because the decision-maker cannot choose which random outcome happens.

**Bridge Note:** In probability trees, all possible random branches remain possible. In decision trees, some choice branches are deliberately rejected.

## 8.6 EMV formula

For two outcomes:

\[
\operatorname{EMV}=p_1x_1+p_2x_2.
\]

If \(p_2=1-p_1\), then:

\[
\operatorname{EMV}=p_1x_1+(1-p_1)x_2.
\]

If a game gives \(£4\) with probability \(\frac38\) and loses \(£2\) with probability \(\frac58\), then:

\[
\operatorname{EMV}
=
\frac38(4)+\frac58(-2).
\]

Calculate each part:

\[
\frac38(4)=\frac{12}{8}=\frac32,
\]

\[
\frac58(-2)=-\frac{10}{8}=-\frac54.
\]

Therefore:

\[
\operatorname{EMV}
=
\frac32-\frac54.
\]

Use a common denominator:

\[
\frac32=\frac64,
\]

so:

\[
\operatorname{EMV}
=
\frac64-\frac54
=
\frac14.
\]

As a decimal:

\[
\frac14=0.25.
\]

So the EMV is:

\[
£0.25.
\]

## 8.7 Why EMV can be misleading

A positive EMV means the long-run average gain is positive.

It does not mean the person will definitely gain money on one play.

For example, if a game has EMV \(£0.25\), playing it 100 times would suggest an expected gain:

\[
100(0.25)=25.
\]

So over 100 plays, the expected gain is:

\[
£25.
\]

But for one play, the person may still lose money.

This is why risk attitude matters.

## 8.8 Utility and risk aversion

Suppose a school fair game has a positive EMV, but if one person wins the school loses \(£1600\).

A casino might accept this because it can play the long-run game.

A school might reject it because one bad result matters too much.

Utility handles this by replacing money with subjective value.

Instead of calculating:

\[
\operatorname{EMV}=\sum p_ix_i,
\]

we calculate:

\[
\operatorname{Expected\ Utility}=\sum p_iU(x_i).
\]

## 8.9 The utility function \(U(x)=1-e^{-x/R}\)

Let:

\[
U(x)=1-e^{-x/R},
\]

where:

- \(x\) is the pay-off;
- \(R>0\);
- \(U(x)\) is measured in utils.

If \(x=0\), then:

\[
U(0)=1-e^{-0/R}.
\]

Since:

\[
-\frac{0}{R}=0,
\]

we have:

\[
U(0)=1-e^0.
\]

Since:

\[
e^0=1,
\]

therefore:

\[
U(0)=1-1=0.
\]

So a zero pay-off has zero utility for this function.

If \(x\) is negative, then:

\[
-\frac{x}{R}
\]

is positive, so \(e^{-x/R}\) can become large. This makes:

\[
1-e^{-x/R}
\]

very negative.

That models risk aversion.

## 8.10 Effect of \(R\)

If \(R\) is smaller, losses become more painful in utility terms.

If \(R\) is larger, the decision-maker is more willing to take risks.

For example, for \(x=-1600\):

### Case 1: \(R=400\)

\[
U(-1600)
=
1-e^{-(-1600)/400}.
\]

Simplify the exponent:

\[
-\frac{-1600}{400}=4.
\]

Therefore:

\[
U(-1600)=1-e^4.
\]

Using a calculator:

\[
e^4\approx 54.59815003.
\]

So:

\[
U(-1600)
\approx 1-54.59815003
=
-53.59815003.
\]

To three significant figures:

\[
U(-1600)\approx -53.6.
\]

### Case 2: \(R=200\)

\[
U(-1600)
=
1-e^{-(-1600)/200}.
\]

Simplify the exponent:

\[
-\frac{-1600}{200}=8.
\]

Therefore:

\[
U(-1600)=1-e^8.
\]

Using a calculator:

\[
e^8\approx 2980.957987.
\]

So:

\[
U(-1600)
\approx 1-2980.957987
=
-2979.957987.
\]

To three significant figures:

\[
U(-1600)\approx -2980.
\]

The same loss is much worse when \(R=200\) than when \(R=400\).

---

# 9. Visual Asset Integration

The following placeholders match the split asset files in this lesson pack.

[VISUAL PLACEHOLDER: OffSpecDecisionAnalysisMermaid-001 | Source: transcripts.md | Insert from mermaid/OffSpecDecisionAnalysisMermaid-001.md | Purpose: Summarise the decision-tree node grammar.]

[VISUAL PLACEHOLDER: OffSpecDecisionAnalysisMermaid-002 | Source: transcripts.md + ordinary A-Level Maths bridge | Insert from mermaid/OffSpecDecisionAnalysisMermaid-002.md | Purpose: Compare probability-tree thinking with decision-tree thinking.]

[VISUAL PLACEHOLDER: OffSpecDecisionAnalysisMermaid-003 | Source: transcripts.md | Insert from mermaid/OffSpecDecisionAnalysisMermaid-003.md | Purpose: Show James’s play/not-play EMV decision tree.]

[VISUAL PLACEHOLDER: OffSpecDecisionAnalysisMermaid-004 | Source: transcripts.md | Insert from mermaid/OffSpecDecisionAnalysisMermaid-004.md | Purpose: Show Jess’s multi-stage decision tree and backward EMV logic.]

[VISUAL PLACEHOLDER: OffSpecDecisionAnalysisMermaid-005 | Source: transcripts.md | Insert from mermaid/OffSpecDecisionAnalysisMermaid-005.md | Purpose: Show the workflow from monetary pay-offs to expected utility.]

[VISUAL PLACEHOLDER: OffSpecDecisionAnalysisMermaid-006 | Source: transcripts.md | Insert from mermaid/OffSpecDecisionAnalysisMermaid-006.md | Purpose: Summarise how the risk parameter R affects utility decisions.]

[VISUAL PLACEHOLDER: OffSpecDecisionAnalysisMermaid-007 | Source: transcripts.md | Insert from mermaid/OffSpecDecisionAnalysisMermaid-007.md | Purpose: Show why positive EMV does not always settle a risky decision.]

[VISUAL PLACEHOLDER: OffSpecDecisionAnalysisSVG-001 | Source: Screenshot PDF opening page + transcript | Insert from svg/OffSpecDecisionAnalysisSVG-001.svg | Purpose: Show the three node shapes: decision box, chance circle and backwards end/pay-off triangle. Description: A clean reference panel with a box labelled decision node, a circle labelled chance node, and a backwards triangle labelled end/pay-off node.]

[VISUAL PLACEHOLDER: OffSpecDecisionAnalysisSVG-002 | Source: Transcript James example | Insert from svg/OffSpecDecisionAnalysisSVG-002.svg | Purpose: Show a simple play/not-play decision tree with EMV. Description: Initial decision box branches to play and not play; play leads to a chance node with outcomes “6 or more” and “less than 6”; end pay-offs \(4\), \(-2\), and \(0\); EMV \(0.25\).]

[VISUAL PLACEHOLDER: OffSpecDecisionAnalysisSVG-003 | Source: Transcript Jess example | Insert from svg/OffSpecDecisionAnalysisSVG-003.svg | Purpose: Show a multi-stage decision tree with a second decision after losing. Description: Initial play/not-play decision, chance node for same/different dice scores, later decision to play again or not, final chance node for third dice matching.]

[VISUAL PLACEHOLDER: OffSpecDecisionAnalysisSVG-004 | Source: Utility transcript | Insert from svg/OffSpecDecisionAnalysisSVG-004.svg | Purpose: Compare monetary pay-off with utility for different risk attitudes. Description: Axes labelled profit/pay-off \(x\) and utility \(U(x)\), with two curves for larger and smaller \(R\), showing losses becoming more negative faster when \(R\) is smaller.]

[VISUAL PLACEHOLDER: OffSpecDecisionAnalysisBridgeSVG-001 | Source: Ordinary A-Level Maths bridge + decision analysis transcript | Insert from svg/OffSpecDecisionAnalysisBridgeSVG-001.svg | Purpose: Compare ordinary probability trees with decision trees. Description: Side-by-side comparison showing probability branches versus decision branches, with warning that decision branches do not carry probabilities.]

[VISUAL PLACEHOLDER: OffSpecDecisionAnalysisTikZ-001 | Source: transcripts.md | Insert from tikz/OffSpecDecisionAnalysisTikZ-001.tex | Purpose: Provide a precise LaTeX/TikZ decision-tree notation key.]

[VISUAL PLACEHOLDER: OffSpecDecisionAnalysisTikZ-002 | Source: transcripts.md | Insert from tikz/OffSpecDecisionAnalysisTikZ-002.tex | Purpose: Show James's play/not-play EMV decision tree.]

[VISUAL PLACEHOLDER: OffSpecDecisionAnalysisTikZ-003 | Source: transcripts.md | Insert from tikz/OffSpecDecisionAnalysisTikZ-003.tex | Purpose: Show Jess's multi-stage decision tree and backward EMV logic.]

[VISUAL PLACEHOLDER: OffSpecDecisionAnalysisTikZ-004 | Source: transcripts.md | Insert from tikz/OffSpecDecisionAnalysisTikZ-004.tex | Purpose: Sketch utility functions and show how smaller R increases risk aversion.]

[VISUAL PLACEHOLDER: OffSpecDecisionAnalysisTikZ-005 | Source: transcripts.md + ordinary A-Level Maths bridge | Insert from tikz/OffSpecDecisionAnalysisTikZ-005.tex | Purpose: Compare probability trees with decision trees and warn against probabilities on decision branches.]

---

# 10. Interactive Learning Widgets

[INTERACTIVE PLACEHOLDER: OffSpecDecisionAnalysisWidget-001 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/OffSpecDecisionAnalysisWidget-001.html | Purpose: Practise EMV calculation at a chance node.]

The widget lets the student input probability \(p\), pay-offs \(x_1\) and \(x_2\), and a comparison value. It displays \(\operatorname{EMV}=px_1+(1-p)x_2\), checks probability complements and warns about sign errors.

[INTERACTIVE PLACEHOLDER: OffSpecDecisionAnalysisWidget-002 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/OffSpecDecisionAnalysisWidget-002.html | Purpose: Explore utility and risk aversion.]

The widget lets the student input pay-offs and a risk parameter \(R\), then calculates utility values using \(U(x)=1-e^{-x/R}\). It displays expected utility and a utility graph.

[INTERACTIVE PLACEHOLDER: OffSpecDecisionAnalysisWidget-003 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/OffSpecDecisionAnalysisWidget-003.html | Purpose: Build a simple decision tree from choices and outcomes.]

The widget checks whether the student has put probabilities on the correct type of branch and reinforces that branches can only be crossed off from decision nodes.

---

# 11. Worked Examples

## Worked Example 1: James and two tetrahedral dice

### Evidence status

Off-spec enrichment, based on supplied Decision 2 transcript and screenshots.

### Question

James is trying to decide whether or not to play a game using two fair tetrahedral dice, with sides numbered from \(1\) to \(4\).

If he scores a total of \(6\) or more, then he wins \(£4\).

Otherwise, he loses \(£2\).

1. Draw a decision tree to model his possible decisions and outcomes.
2. Determine whether James should play the game and state his EMV.

### Step 1: Identify the first decision

James decides whether to play.

So draw a decision node.

The two branches are:

\[
p=\text{play},
\]

and:

\[
\sim p=\text{do not play}.
\]

The notation \(\sim p\) is used here as a shorthand for “not play”.

### Step 2: If James does not play

If James does not play, the game ends.

The pay-off is:

\[
0.
\]

### Step 3: If James plays

If James plays, the result depends on two fair tetrahedral dice.

That is a chance event, so use a chance node.

The possible outcomes are:

- total is \(6\) or more;
- total is less than \(6\).

### Step 4: Find \(P(\text{total }6\text{ or more})\)

The possible outcomes for two tetrahedral dice are:

\[
(1,1),(1,2),(1,3),(1,4),
\]

\[
(2,1),(2,2),(2,3),(2,4),
\]

\[
(3,1),(3,2),(3,3),(3,4),
\]

\[
(4,1),(4,2),(4,3),(4,4).
\]

There are:

\[
4\times 4=16
\]

equally likely outcomes.

The outcomes with total \(6\) or more are:

\[
(2,4),\quad (3,3),\quad (3,4),\quad (4,2),\quad (4,3),\quad (4,4).
\]

There are \(6\) such outcomes.

Therefore:

\[
P(\text{total }6\text{ or more})=\frac{6}{16}.
\]

Simplify:

\[
\frac{6}{16}=\frac{3}{8}.
\]

So:

\[
P(\text{total }6\text{ or more})=\frac38.
\]

### Step 5: Find \(P(\text{less than }6)\)

The two outcomes are complementary.

Therefore:

\[
P(\text{less than }6)=1-\frac38.
\]

Write \(1\) as \(\frac88\):

\[
P(\text{less than }6)=\frac88-\frac38.
\]

So:

\[
P(\text{less than }6)=\frac58.
\]

### Step 6: Add pay-offs

If James scores \(6\) or more, the pay-off is:

\[
4.
\]

If James scores less than \(6\), the pay-off is:

\[
-2.
\]

If James does not play, the pay-off is:

\[
0.
\]

### Step 7: Calculate the EMV of playing

\[
\operatorname{EMV}
=
\frac38(4)+\frac58(-2).
\]

Calculate the first term:

\[
\frac38(4)=\frac{12}{8}.
\]

Simplify:

\[
\frac{12}{8}=\frac32.
\]

Calculate the second term:

\[
\frac58(-2)=-\frac{10}{8}.
\]

Simplify:

\[
-\frac{10}{8}=-\frac54.
\]

So:

\[
\operatorname{EMV}
=
\frac32-\frac54.
\]

Use denominator \(4\):

\[
\frac32=\frac64.
\]

Therefore:

\[
\operatorname{EMV}
=
\frac64-\frac54
=
\frac14.
\]

As a decimal:

\[
\frac14=0.25.
\]

So:

\[
\operatorname{EMV}=£0.25.
\]

### Step 8: Compare choices

Playing has value:

\[
0.25.
\]

Not playing has value:

\[
0.
\]

Since:

\[
0.25>0,
\]

James should play.

### Final answer

James should play the game.

His EMV is:

\[
£0.25.
\]

That is \(25\text{p}\).

### Teaching note

This recommendation is based on EMV. It means that over many repetitions, James would expect an average gain of \(25\text{p}\) per play. It does not mean he cannot lose \(£2\) on one play.

## Worked Example 2: Jess and the second-chance dice game

### Evidence status

Off-spec enrichment, based on supplied Decision 2 transcript.

### Question

Jess pays \(£2\) to play a game.

She rolls two dice. If they both show the same score, she wins \(£5\). Otherwise she loses.

If she loses, she can pay a further \(£1\) to roll a third dice. If the score on the third dice matches the score on either of the first two dice, then she wins \(£6\). Otherwise she loses.

1. Draw a decision tree to model the decisions and possible outcomes.
2. Find the best strategy for Jess as indicated by the decision tree.

### Step 1: First decision

Jess first decides whether to play.

Branches:

\[
p=\text{play},
\]

\[
\sim p=\text{do not play}.
\]

If she does not play, the pay-off is:

\[
0.
\]

### Step 2: If Jess plays

She pays \(£2\).

Then she rolls two dice.

This is a chance event.

The possible outcomes are:

- same score;
- different score.

### Step 3: Probability of same score

For two fair six-sided dice, the same-score outcomes are:

\[
(1,1),(2,2),(3,3),(4,4),(5,5),(6,6).
\]

There are \(6\) same-score outcomes.

The total number of equally likely outcomes is:

\[
6\times 6=36.
\]

Therefore:

\[
P(\text{same score})=\frac{6}{36}=\frac16.
\]

The probability of a different score is:

\[
P(\text{different score})=1-\frac16=\frac56.
\]

### Step 4: Pay-off if the first two dice match

If the dice show the same score, Jess wins \(£5\), but she paid \(£2\) to play.

Net pay-off:

\[
5-2=3.
\]

So the pay-off is:

\[
3.
\]

### Step 5: If the first two dice are different

If the dice are different, Jess has another decision:

- play again;
- do not play again.

If she does not play again, she has already paid \(£2\) and won nothing.

So the pay-off is:

\[
-2.
\]

### Step 6: If Jess plays again

She pays a further \(£1\). Total cost so far:

\[
2+1=3.
\]

She rolls a third die.

Since the first two dice were different, there are two different scores that the third die could match.

For example, if the first two dice were \(2\) and \(3\), then the third die matches if it is \(2\) or \(3\).

So:

\[
P(\text{third die matches one of the first two})=\frac26=\frac13.
\]

Therefore:

\[
P(\text{third die does not match})=1-\frac13=\frac23.
\]

### Step 7: Pay-off if third die matches

If the third die matches, Jess wins \(£6\).

She has paid:

\[
£2+£1=£3.
\]

Net pay-off:

\[
6-3=3.
\]

So the pay-off is:

\[
3.
\]

### Step 8: Pay-off if third die does not match

If the third die does not match, Jess wins nothing and has paid:

\[
£3.
\]

So the pay-off is:

\[
-3.
\]

### Step 9: EMV of playing again

At the final chance node:

\[
\operatorname{EMV}
=
\frac13(3)+\frac23(-3).
\]

Calculate:

\[
\frac13(3)=1,
\]

and:

\[
\frac23(-3)=-2.
\]

Therefore:

\[
\operatorname{EMV}=1-2=-1.
\]

So playing again has value:

\[
-1.
\]

Not playing again has value:

\[
-2.
\]

Since:

\[
-1>-2,
\]

if Jess has already played and lost at first, she should play again.

### Step 10: EMV of playing the original game

Now the first chance node has:

- same score with probability \(\frac16\) and pay-off \(3\);
- different score with probability \(\frac56\), after which the best continuation value is \(-1\).

Therefore:

\[
\operatorname{EMV}
=
\frac16(3)+\frac56(-1).
\]

Calculate:

\[
\frac16(3)=\frac36=\frac12.
\]

And:

\[
\frac56(-1)=-\frac56.
\]

So:

\[
\operatorname{EMV}
=
\frac12-\frac56.
\]

Use denominator \(6\):

\[
\frac12=\frac36.
\]

Therefore:

\[
\operatorname{EMV}
=
\frac36-\frac56
=
-\frac26
=
-\frac13.
\]

As a decimal:

\[
-\frac13\approx -0.33.
\]

So playing initially has value:

\[
-0.33.
\]

Not playing has value:

\[
0.
\]

Since:

\[
0>-0.33,
\]

Jess should not play the game.

### Final answer

The best strategy is:

- Jess should not play the game.
- If she did play and lost at first, she should play again.

The reasoning is:

\[
0>-0.33,
\]

so not playing is better initially.

But:

\[
-1>-2,
\]

so if she has already lost at first, playing again is better than stopping.

### Teaching note

This example is the first real “tree goblin” moment. The best first decision is not to play, but the best later decision, conditional on already having played and lost, is to play again.

## Worked Example 3: School fair game and EMV

### Evidence status

Off-spec enrichment, based on supplied Decision 2 utility theory transcript.

### Scenario

A school is deciding whether to offer a game at a school fair.

The game costs \(£1\) to play.

Each player rolls six dice.

If all six dice are sixes, the player wins \(£2000\).

If more than one person rolls all sixes, a single winner is picked at random from those people, so the school only gives out one \(£2000\) prize.

The school expects \(400\) people to play.

### Step 1: Probability that one person rolls six sixes

For one player:

\[
P(\text{six sixes})=\left(\frac16\right)^6.
\]

Compute:

\[
6^6=46656.
\]

Therefore:

\[
P(\text{six sixes})=\frac{1}{46656}.
\]

As a decimal:

\[
\frac{1}{46656}\approx 0.0000214.
\]

### Step 2: Probability at least one person wins

Let:

\[
X=\text{number of people who roll six sixes}.
\]

Then:

\[
X\sim \operatorname{Bin}\left(400,\frac{1}{46656}\right).
\]

We need:

\[
P(X\ge 1).
\]

Use the complement:

\[
P(X\ge 1)=1-P(X=0).
\]

Now:

\[
P(X=0)=\left(1-\frac{1}{46656}\right)^{400}.
\]

Using a calculator:

\[
P(X\ge 1)\approx 0.008537.
\]

Therefore:

\[
P(X=0)\approx 1-0.008537=0.991463.
\]

The transcript uses approximately:

\[
P(\text{prize claimed})=0.008537,
\]

and:

\[
P(\text{prize not claimed})\approx 0.99115.
\]

There is a small rounding/transcription inconsistency in the displayed probability for not claimed. For this lesson, we preserve the transcript’s teaching intention: the claimed probability is small, and the not-claimed probability is close to \(0.991\).

### Step 3: Pay-off if prize is claimed

The school receives:

\[
400(£1)=£400.
\]

If the prize is claimed, the school pays:

\[
£2000.
\]

Net pay-off:

\[
400-2000=-1600.
\]

So:

\[
\text{pay-off}=-1600.
\]

### Step 4: Pay-off if prize is not claimed

The school receives:

\[
£400.
\]

It pays no prize.

So:

\[
\text{pay-off}=400.
\]

### Step 5: EMV of offering the game

Using the transcript probabilities:

\[
\operatorname{EMV}
=
0.008537(-1600)+0.99115(400).
\]

Calculate the first term:

\[
0.008537(-1600)=-13.6592.
\]

Calculate the second term:

\[
0.99115(400)=396.46.
\]

Therefore:

\[
\operatorname{EMV}
=
-13.6592+396.46
=
382.8008.
\]

So approximately:

\[
\operatorname{EMV}\approx £382.80.
\]

### EMV conclusion

The EMV is positive, so EMV alone suggests the school should offer the game.

### Risk warning

The school might still refuse, because one unlucky winner causes a loss of:

\[
£1600.
\]

A school is likely risk averse because it is managing public or limited funds.

This motivates utility.

## Worked Example 4: School fair expected utility with \(R=400\)

### Question

Using:

\[
U(x)=1-e^{-x/R},
\]

calculate the school’s expected utility when \(R=400\).

Use the pay-offs:

\[
-1600,\quad 400,\quad 0.
\]

Use probabilities:

\[
P(\text{prize claimed})=0.008537,
\]

\[
P(\text{prize not claimed})=0.99115.
\]

### Step 1: Utility of \(-1600\)

\[
U(-1600)=1-e^{-(-1600)/400}.
\]

Simplify:

\[
-\frac{-1600}{400}=4.
\]

Therefore:

\[
U(-1600)=1-e^4.
\]

Using a calculator:

\[
e^4\approx 54.598.
\]

So:

\[
U(-1600)\approx 1-54.598=-53.598.
\]

To three significant figures:

\[
U(-1600)\approx -53.6.
\]

### Step 2: Utility of \(400\)

\[
U(400)=1-e^{-400/400}.
\]

Simplify:

\[
-\frac{400}{400}=-1.
\]

So:

\[
U(400)=1-e^{-1}.
\]

Using a calculator:

\[
e^{-1}\approx 0.367879.
\]

Therefore:

\[
U(400)\approx 1-0.367879=0.632121.
\]

To three significant figures:

\[
U(400)\approx 0.632.
\]

### Step 3: Utility of \(0\)

\[
U(0)=1-e^0=1-1=0.
\]

### Step 4: Expected utility

\[
\operatorname{Expected\ Utility}
=
0.008537(-53.6)+0.99115(0.632).
\]

Calculate the first term:

\[
0.008537(-53.6)\approx -0.4575832.
\]

Calculate the second term:

\[
0.99115(0.632)\approx 0.6268068.
\]

Therefore:

\[
\operatorname{Expected\ Utility}
\approx -0.4575832+0.6268068.
\]

So:

\[
\operatorname{Expected\ Utility}
\approx 0.1692236.
\]

To three significant figures:

\[
\operatorname{Expected\ Utility}\approx 0.169.
\]

### Conclusion

Since:

\[
0.169>0,
\]

this utility model suggests the school should offer the game when \(R=400\).

The interpretation is that \(R=400\) represents a decision-maker more willing to take risk.

## Worked Example 5: Company choices by EMV and utility

### Question

A company can choose one of three business options \(A\), \(B\) and \(C\).

The outcomes are:

| Option | Probability | Pay-off |
|---|---:|---:|
| \(A\) | \(0.7\) | \(750\) |
| \(A\) | \(0.3\) | \(-550\) |
| \(B\) | \(0.7\) | \(400\) |
| \(B\) | \(0.3\) | \(-200\) |
| \(C\) | \(0.7\) | \(500\) |
| \(C\) | \(0.3\) | \(-300\) |

First calculate the optimal EMV.

Then use:

\[
U(x)=\sqrt{x+600}
\]

to decide using expected utility.

### Part A: EMV for option \(A\)

\[
\operatorname{EMV}_A=0.7(750)+0.3(-550).
\]

Calculate:

\[
0.7(750)=525.
\]

\[
0.3(-550)=-165.
\]

Therefore:

\[
\operatorname{EMV}_A=525-165=360.
\]

### EMV for option \(B\)

\[
\operatorname{EMV}_B=0.7(400)+0.3(-200).
\]

Calculate:

\[
0.7(400)=280.
\]

\[
0.3(-200)=-60.
\]

Therefore:

\[
\operatorname{EMV}_B=280-60=220.
\]

### EMV for option \(C\)

\[
\operatorname{EMV}_C=0.7(500)+0.3(-300).
\]

Calculate:

\[
0.7(500)=350.
\]

\[
0.3(-300)=-90.
\]

Therefore:

\[
\operatorname{EMV}_C=350-90=260.
\]

### EMV decision

Compare:

\[
360,\quad 220,\quad 260.
\]

The greatest is:

\[
360.
\]

So the best option by EMV is:

\[
A.
\]

### Part B: Utility values

Use:

\[
U(x)=\sqrt{x+600}.
\]

For \(x=750\):

\[
U(750)=\sqrt{750+600}=\sqrt{1350}\approx 36.7.
\]

For \(x=-550\):

\[
U(-550)=\sqrt{-550+600}=\sqrt{50}\approx 7.07.
\]

For \(x=400\):

\[
U(400)=\sqrt{1000}\approx 31.6.
\]

For \(x=-200\):

\[
U(-200)=\sqrt{400}=20.
\]

For \(x=500\):

\[
U(500)=\sqrt{1100}\approx 33.2.
\]

For \(x=-300\):

\[
U(-300)=\sqrt{300}\approx 17.3.
\]

### Expected utility for \(A\)

\[
EU_A=0.7(36.7)+0.3(7.07).
\]

\[
EU_A=25.69+2.121=27.811\approx 27.8.
\]

### Expected utility for \(B\)

\[
EU_B=0.7(31.6)+0.3(20)=22.12+6=28.12\approx 28.1.
\]

### Expected utility for \(C\)

\[
EU_C=0.7(33.2)+0.3(17.3)=23.24+5.19=28.43\approx 28.4.
\]

### Utility decision

Compare:

\[
EU_A\approx 27.8,\quad EU_B\approx 28.1,\quad EU_C\approx 28.4.
\]

The greatest is:

\[
28.4.
\]

So the best option using expected utility is:

\[
C.
\]

### Teaching note

EMV chooses \(A\), but expected utility chooses \(C\). This is not a contradiction. It means the utility function changes how the decision-maker values risky outcomes.

---

# 12. Common Mistakes and Exam Traps

## Mistake 1: Treating decision trees like probability trees

Wrong habit:

\[
P(\text{play})=\frac12.
\]

There is no such probability unless the question says the person chooses randomly.

Correct idea:

- decision branches are choices;
- chance branches are random events.

## Mistake 2: Putting probabilities on branches from boxes

Probabilities belong after chance nodes, not decision nodes.

## Mistake 3: Forgetting the cost to play

If someone pays \(£2\) to play and wins \(£5\), the net gain is:

\[
5-2=3,
\]

not:

\[
5.
\]

## Mistake 4: Comparing a future decision incorrectly

In Jess’s example, after she loses the first roll:

- stopping gives \(-2\);
- playing again gives EMV \(-1\).

Because:

\[
-1>-2,
\]

playing again is better.

Students often think \(-2\) is “smaller” and accidentally choose it.

## Mistake 5: Crossing off chance branches

Do not cross off random outcomes. You cannot decide that a die will not roll a certain value.

Only cross off decision branches.

## Mistake 6: Using raw pay-offs after introducing utility

Once utility is introduced, transform all relevant pay-offs first.

Then calculate expected utility.

Do not mix:

\[
\text{pounds}
\]

with:

\[
\text{utils}.
\]

## Mistake 7: Forgetting \(U(0)\)

For:

\[
U(x)=1-e^{-x/R},
\]

\[
U(0)=0.
\]

But for another utility function, \(U(0)\) may not be zero. Always check.

## Mistake 8: Rounding too early

In utility questions, small differences may matter.

Keep several decimal places during calculation, then round at the end.

## Mistake 9: Misreading “at least one”

If:

\[
X=\text{number of winners},
\]

then:

\[
P(X\ge 1)=1-P(X=0).
\]

This is often easier than adding:

\[
P(X=1)+P(X=2)+\cdots.
\]

---

# 13. Practice Questions

These are AI-generated enrichment questions. They are not past-paper or textbook questions.

## Question 1: Basic EMV

A player can choose to play or not play a game.

If she plays, she wins \(£6\) with probability \(\frac14\), and loses \(£2\) with probability \(\frac34\).

If she does not play, her pay-off is \(0\).

1. Draw the structure of the decision tree.
2. Calculate the EMV of playing.
3. State whether she should play using EMV.

## Question 2: Cost included

A game costs \(£3\) to play.

If Amir plays, he rolls one fair six-sided die.

If he rolls a \(6\), he receives \(£15\).

Otherwise, he receives nothing.

If Amir does not play, his pay-off is \(0\).

1. Find the net pay-off if he wins.
2. Find the net pay-off if he loses.
3. Calculate the EMV of playing.
4. Decide whether Amir should play.

## Question 3: Multi-stage decision

Maya pays \(£1\) to play a game.

She tosses a fair coin.

If it lands heads, she wins \(£4\).

If it lands tails, she may pay another \(£1\) to toss again.

On the second toss, heads wins \(£5\), and tails wins nothing.

1. Draw the decision tree.
2. Find the best strategy.
3. State the optimal EMV.

## Question 4: Utility calculation

Use:

\[
U(x)=1-e^{-x/100}.
\]

A decision has two possible pay-offs:

- \(x=200\) with probability \(0.4\);
- \(x=-50\) with probability \(0.6\).

Calculate the expected utility.

## Question 5: Utility versus EMV

A company can choose option \(A\) or \(B\).

| Option | Probability | Pay-off |
|---|---:|---:|
| \(A\) | \(0.5\) | \(500\) |
| \(A\) | \(0.5\) | \(-300\) |
| \(B\) | \(0.5\) | \(200\) |
| \(B\) | \(0.5\) | \(0\) |

1. Choose using EMV.
2. Use:

\[
U(x)=\sqrt{x+400}
\]

to choose using expected utility.
3. Explain why the answer may change.

---

# 14. Worked Solutions

## Solution 1

Playing has EMV:

\[
\operatorname{EMV}
=
\frac14(6)+\frac34(-2).
\]

Calculate:

\[
\frac14(6)=\frac64=\frac32.
\]

\[
\frac34(-2)=-\frac64=-\frac32.
\]

Therefore:

\[
\operatorname{EMV}=\frac32-\frac32=0.
\]

Not playing gives:

\[
0.
\]

So the player is indifferent by EMV.

Final answer:

\[
\operatorname{EMV}=£0.
\]

She does not have a monetary advantage from playing.

## Solution 2

The game costs \(£3\).

If Amir wins, he receives \(£15\).

Net winning pay-off:

\[
15-3=12.
\]

If Amir loses, he receives nothing and pays \(£3\).

Net losing pay-off:

\[
0-3=-3.
\]

The probability of rolling a \(6\) is:

\[
\frac16.
\]

The probability of not rolling a \(6\) is:

\[
\frac56.
\]

Therefore:

\[
\operatorname{EMV}
=
\frac16(12)+\frac56(-3).
\]

Calculate:

\[
\frac16(12)=2.
\]

\[
\frac56(-3)=-\frac{15}{6}=-\frac52=-2.5.
\]

Therefore:

\[
\operatorname{EMV}=2-2.5=-0.5.
\]

So:

\[
\operatorname{EMV}=-£0.50.
\]

Not playing gives:

\[
0.
\]

Since:

\[
0>-0.5,
\]

Amir should not play.

## Solution 3

Maya first decides whether to play.

If she does not play, pay-off:

\[
0.
\]

If she plays, she pays \(£1\).

First toss:

- heads with probability \(\frac12\);
- tails with probability \(\frac12\).

If first toss is heads, she receives \(£4\).

Net pay-off:

\[
4-1=3.
\]

If first toss is tails, she may pay another \(£1\) to toss again.

If she stops after tails, she has paid \(£1\), so pay-off:

\[
-1.
\]

If she pays to toss again, total cost:

\[
1+1=2.
\]

Second toss:

- heads with probability \(\frac12\);
- tails with probability \(\frac12\).

If second toss is heads, she receives \(£5\).

Net pay-off:

\[
5-2=3.
\]

If second toss is tails, she receives nothing and paid \(£2\).

Net pay-off:

\[
-2.
\]

EMV of tossing again:

\[
\operatorname{EMV}
=
\frac12(3)+\frac12(-2).
\]

Calculate:

\[
\frac12(3)=\frac32.
\]

\[
\frac12(-2)=-1.
\]

Therefore:

\[
\operatorname{EMV}=\frac32-1=\frac12.
\]

So tossing again is worth:

\[
0.5.
\]

Stopping is worth:

\[
-1.
\]

Since:

\[
0.5>-1,
\]

if Maya gets tails first, she should toss again.

Now calculate the EMV of playing initially:

\[
\operatorname{EMV}
=
\frac12(3)+\frac12(0.5).
\]

Calculate:

\[
\frac12(3)=1.5.
\]

\[
\frac12(0.5)=0.25.
\]

Therefore:

\[
\operatorname{EMV}=1.5+0.25=1.75.
\]

Not playing gives:

\[
0.
\]

Since:

\[
1.75>0,
\]

Maya should play.

Final strategy:

- play the game;
- if first toss is tails, pay for the second toss.

Optimal EMV:

\[
£1.75.
\]

## Solution 4

Use:

\[
U(x)=1-e^{-x/100}.
\]

For \(x=200\):

\[
U(200)=1-e^{-200/100}.
\]

Simplify:

\[
-\frac{200}{100}=-2.
\]

So:

\[
U(200)=1-e^{-2}.
\]

Using a calculator:

\[
e^{-2}\approx 0.135335.
\]

Therefore:

\[
U(200)\approx 1-0.135335=0.864665.
\]

For \(x=-50\):

\[
U(-50)=1-e^{-(-50)/100}.
\]

Simplify:

\[
-\frac{-50}{100}=0.5.
\]

So:

\[
U(-50)=1-e^{0.5}.
\]

Using a calculator:

\[
e^{0.5}\approx 1.648721.
\]

Therefore:

\[
U(-50)\approx 1-1.648721=-0.648721.
\]

Expected utility:

\[
EU=0.4(0.864665)+0.6(-0.648721).
\]

Calculate:

\[
0.4(0.864665)=0.345866.
\]

\[
0.6(-0.648721)=-0.389233.
\]

Therefore:

\[
EU\approx 0.345866-0.389233=-0.043367.
\]

So:

\[
EU\approx -0.0434.
\]

## Solution 5

### Part 1: EMV

For \(A\):

\[
\operatorname{EMV}_A=0.5(500)+0.5(-300)=250-150=100.
\]

For \(B\):

\[
\operatorname{EMV}_B=0.5(200)+0.5(0)=100+0=100.
\]

By EMV, the decision-maker is indifferent:

\[
\operatorname{EMV}_A=\operatorname{EMV}_B=100.
\]

### Part 2: Expected utility

Use:

\[
U(x)=\sqrt{x+400}.
\]

For option \(A\):

\[
U(500)=\sqrt{900}=30.
\]

\[
U(-300)=\sqrt{100}=10.
\]

So:

\[
EU_A=0.5(30)+0.5(10)=15+5=20.
\]

For option \(B\):

\[
U(200)=\sqrt{600}\approx 24.4949.
\]

\[
U(0)=\sqrt{400}=20.
\]

So:

\[
EU_B=0.5(24.4949)+0.5(20)=12.24745+10=22.24745.
\]

Therefore:

\[
EU_B\approx 22.2.
\]

Compare:

\[
EU_A=20,
\]

\[
EU_B\approx 22.2.
\]

So expected utility chooses:

\[
B.
\]

### Part 3: Explanation

EMV treats \(A\) and \(B\) as equal because both have average monetary value \(100\).

Utility chooses \(B\) because \(A\) contains a risky loss of \(-300\). The utility function penalises that risk.

---

# 15. Exam Technique Notes

Although this is off-spec for CCEA, the Decision 2 technique is tidy and mark-scheme-like.

## For drawing trees

1. Use a box for a decision.
2. Use a circle for chance.
3. Use a backwards triangle for every terminal branch.
4. Label every branch.
5. Put probabilities only after chance nodes.
6. Put pay-offs next to end nodes.
7. Leave enough horizontal space.

## For EMV

Write:

\[
\operatorname{EMV}=p_1x_1+p_2x_2+\cdots.
\]

Show the substituted values.

For example:

\[
\operatorname{EMV}=\frac38(4)+\frac58(-2)=0.25.
\]

## For utility

First transform pay-offs:

\[
x\mapsto U(x).
\]

Then use probabilities:

\[
EU=p_1U(x_1)+p_2U(x_2)+\cdots.
\]

## For decision nodes

Pick the greatest value.

Remember:

\[
-1>-2.
\]

A smaller loss is better.

## For final answers

Do not only leave a number.

State the strategy in words.

Example:

> Jess should not play the game. However, if she did play and lost at first, she should play again.

---

# 16. Syllabus Gap Check

## CCEA LO coverage table

| CCEA LO ID | Covered? | Comment |
|---|---:|---|
| None | No | No CCEA LO was found for this topic in the supplied CCEA Further Mathematics map. |

## Enrichment coverage table

| Enrichment objective ID | Covered? |
|---|---:|
| OFFSPEC-DA-EO001 | Yes |
| OFFSPEC-DA-EO002 | Yes |
| OFFSPEC-DA-EO003 | Yes |
| OFFSPEC-DA-EO004 | Yes |
| OFFSPEC-DA-EO005 | Yes |
| OFFSPEC-DA-EO006 | Yes |
| OFFSPEC-DA-EO007 | Yes |
| OFFSPEC-DA-EO008 | Yes |
| OFFSPEC-DA-EO009 | Partially, with generated practice and Aisha-style theory |

## Evidence coverage table

| Evidence item | Covered? | Notes |
|---|---:|---|
| Decision node shape | Yes | Box/rectangle |
| Chance node shape | Yes | Circle |
| End/pay-off node shape | Yes | Backwards triangle |
| EMV definition | Yes | Weighted average of pay-offs |
| James example | Yes | Full solution included |
| Jess example | Yes | Full solution included |
| School fair EMV | Yes | Included with rounding warning |
| Utility function | Yes | \(U(x)=1-e^{-x/R}\) |
| \(R\) and risk aversion | Yes | Explained |
| Company utility example | Yes | Included |
| Tim threshold example | Not fully included | Mentioned through practice style, but full transcript example not expanded in this lesson file |
| Aisha exam-style utility example | Partially included | Used in theory and referenced, but not fully expanded as a worked example |

## Off-Spec Content Found but Excluded from CCEA Core

The entire lesson remains excluded from CCEA core because no matching CCEA LO was found.

## Weak evidence warnings

- The screenshot PDF is image-based, so not all pages were fully text-parsed.
- Some transcript wording appears to contain speech-to-text slips, especially around utility-function notation and occasional monetary values.
- Where the transcript’s algebra clearly identifies the intended formula, the algebraic interpretation is used and ambiguity is flagged.

---

# 17. Recommended Enhancements Not in the Evidence

The following are AI-proposed enhancements, not evidence-backed CCEA content:

1. A clean node-shape reference SVG.
2. A decision-tree builder widget.
3. A utility curve slider for \(R\).
4. A side-by-side ordinary probability tree versus decision tree visual.
5. A “cross off only decisions” mini-animation.
6. A practice bank with EMV-only, utility-only and threshold-prize questions.
7. A calculator panel for \(U(x)=1-e^{-x/R}\).
8. A worked example comparing EMV and expected utility for the same decision.

---

# 18. Supplementary Sources Used

## Project sources used

- CCEA Further Mathematics specification map: used only to check syllabus boundaries.
- Further Maths module/evidence workflow sources: used only to follow the evidence-first lesson workflow.
- Ordinary A-Level Maths bridge extracts: used only for prerequisite context.

## Lesson-specific evidence used

- `transcripts.md`
- `Chapter_8_Decision_Analysis_⌨️_(Decision_2)_screenshots.pdf`

## Cross-board/off-spec source notes

The uploaded Decision 2 content is treated as cross-board or non-CCEA enrichment. It is not presented as required CCEA Further Mathematics content.

## Evidence boundary statement

This lesson teaches Decision Analysis as a mathematically useful enrichment topic. It should live in an enrichment/off-spec area of the portal, not inside the CCEA core lesson sequence.

---

# 19. Final Student Checklist

## Prerequisite confidence checklist

Before studying this lesson, check that you can:

- [ ] calculate simple probabilities;
- [ ] list sample spaces for dice;
- [ ] use complementary probability;
- [ ] multiply probabilities by outcomes;
- [ ] work with negative numbers;
- [ ] understand expected value;
- [ ] use \(e^x\) on a calculator;
- [ ] solve simple inequalities.

## Decision tree checklist

You should now be able to:

- [ ] draw a decision node as a box;
- [ ] draw a chance node as a circle;
- [ ] draw an end/pay-off node as a backwards triangle;
- [ ] label decision branches;
- [ ] label chance branches;
- [ ] put probabilities only after chance nodes;
- [ ] put pay-offs at the ends;
- [ ] calculate EMV at a chance node;
- [ ] write EMV inside a chance node;
- [ ] choose the greatest value at a decision node;
- [ ] cross off rejected decision branches only;
- [ ] state the final strategy in words.

## Utility checklist

You should now be able to:

- [ ] explain why EMV can ignore risk;
- [ ] define utility as subjective value;
- [ ] use \(U(x)=1-e^{-x/R}\);
- [ ] calculate \(U(0)\);
- [ ] calculate \(U(x)\) for positive and negative \(x\);
- [ ] explain why smaller \(R\) means stronger risk aversion;
- [ ] calculate expected utility;
- [ ] compare decisions using expected utility.

## Off-spec awareness checklist

Remember:

- [ ] This is an enrichment topic.
- [ ] This is not currently mapped to a supplied CCEA Further Mathematics LO.
- [ ] Do not tag this as a CCEA core lesson unless a valid CCEA source is later supplied.
- [ ] Do not invent CCEA LO IDs for it.
- [ ] Keep it in an optional enrichment section of the portal.
