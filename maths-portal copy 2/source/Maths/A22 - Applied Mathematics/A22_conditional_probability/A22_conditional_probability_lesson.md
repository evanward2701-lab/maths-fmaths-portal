# A22 Conditional Probability

## Title and Metadata

| Field | Value |
|---|---|
| Course | CCEA GCE Mathematics |
| Unit | A22: A2 2 Applied Mathematics |
| Section | Statistics |
| Topic code | A22-PROB |
| Lesson topic | Conditional Probability |
| Topic ID | A22ConditionalProbability |
| Lesson file | `A22_conditional_probability_lesson.md` |
| LO IDs | A22-PROB-LO001, A22-PROB-LO002, A22-PROB-LO003 |
| Tags | `#A22`, `#Probability`, `#ConditionalProbability`, `#VennDiagram`, `#TreeDiagram`, `#TwoWayTable`, `#ModelAssumptions` |

## Evidence Map

This lesson uses the CCEA specification map as the authority for topic boundaries and LO IDs.

The lesson content is built from the uploaded Conditional Probability transcript and DrFrost/lesson PDF, including set notation, Venn diagrams, two-way tables, conditional probability formulae, independence, mutually exclusive events, tree diagrams, probability modelling and critique of assumptions.

The uploaded DrFrost PDF chapter overview organises the chapter into set notation, conditional probability in Venn diagrams, the formula for conditional probability and tree diagrams.

The screenshot PDF was used only as visual context because it did not provide reliable parsed text for every page. No uninspected visual detail has been invented.

## Specification Alignment

| LO ID | Official learning outcome | Where covered |
|---|---|---|
| A22-PROB-LO001 | demonstrate understanding of and use conditional probability, including tree diagrams, Venn diagrams and two-way tables | Venn diagrams, tree diagrams, two-way tables, restricted sample spaces |
| A22-PROB-LO002 | demonstrate understanding of and use the conditional probability formula \(P(A\mid B)=\frac{P(A\cap B)}{P(B)}\) | Formula section, formula derivation, worked examples |
| A22-PROB-LO003 | model with probability, including critiquing assumptions made and the likely effect of more realistic assumptions | Independence, mutually exclusive events, fairness assumptions, changing probabilities, exam traps |

## Learning Objectives

By the end of this lesson, you should be able to:

1. Understand and use conditional probability notation such as
   \[
   P(A\mid B).
   \]
2. Use the conditional probability formula
   \[
   P(A\mid B)=\frac{P(A\cap B)}{P(B)}.
   \]
3. Interpret “given that” as a restriction of the sample space.
4. Use Venn diagrams, tree diagrams and two-way tables to solve conditional probability problems.
5. Decide whether events are independent by comparing probabilities.
6. Use mutually exclusive and independence information to complete probability diagrams.
7. Critique assumptions, such as fairness, independence or whether probabilities should change after previous outcomes.

## Prerequisite Recap: A-Level Probability Toolkit

No external GCSE source is used here. The recap uses A-Level probability knowledge needed for A22.

### Sample space and events

A **sample space** is the set of all possible outcomes. It is often written as

\[
\xi
\]

or sometimes

\[
S.
\]

In a Venn diagram, the sample space is represented by a rectangle.

An **event** is a set of one or more outcomes. In a Venn diagram, events are usually represented by circles and named using capital letters.

For a die:

\[
S=\{1,2,3,4,5,6\}.
\]

Let

\[
A=\text{rolling an even number}=\{2,4,6\},
\]

and

\[
B=\text{rolling a prime number}=\{2,3,5\}.
\]

[VISUAL PLACEHOLDER: A22ConditionalProbabilitySVG-001 | Source: Conditional Probability PDF page 4 and transcript | Insert from svg/A22ConditionalProbabilitySVG-001.svg | Purpose: Show die outcomes in a Venn diagram with \(A=\{2,4,6\}\), \(B=\{2,3,5\}\), and \(S=\{1,2,3,4,5,6\}\).]

### Set notation

| Notation | Meaning | Die example |
|---|---|---|
| \(A'\) | not \(A\), the complement of \(A\) | \(\{1,3,5\}\) |
| \(A\cup B\) | \(A\) or \(B\), the union | \(\{2,3,4,5,6\}\) |
| \(A\cap B\) | \(A\) and \(B\), the intersection | \(\{2\}\) |
| \(A\cap B'\) | \(A\) and not \(B\) | \(\{4,6\}\) |
| \((A\cup B)'\) | not \(A\) or \(B\) | \(\{1\}\) |
| \((A\cap B)'\) | not both \(A\) and \(B\) | \(\{1,3,4,5,6\}\) |

## Big Picture Explanation

Conditional probability is probability with a trapdoor: once you know that one event has happened, the world you are calculating inside may become smaller.

\[
P(A\mid B)
\]

does **not** mean \(P(A)\times P(B)\). It means:

\[
\text{the probability of }A\text{, given that }B\text{ has already happened.}
\]

The event after the vertical bar is the condition. It is the new fence around the sample space.

## Key Definitions and Notation

### Conditional probability

\[
P(A\mid B)
\]

means

\[
\text{the probability that }A\text{ happens, given that }B\text{ has happened.}
\]

The condition is \(B\), because \(B\) appears after the vertical bar.

### Conditional probability formula

For \(P(B)>0\),

\[
P(A\mid B)=\frac{P(A\cap B)}{P(B)}.
\]

The numerator is the probability that both events happen.

The denominator is the probability of the event you are conditioning on.

### Rearranged formula

Starting with

\[
P(A\mid B)=\frac{P(A\cap B)}{P(B)},
\]

multiply both sides by \(P(B)\):

\[
P(A\mid B)P(B)=P(A\cap B).
\]

So

\[
P(A\cap B)=P(B)P(A\mid B).
\]

### Independence

Events \(A\) and \(B\) are independent if knowing that \(B\) happened does not change the probability of \(A\):

\[
P(A\mid B)=P(A).
\]

Equivalently,

\[
P(A\cap B)=P(A)P(B).
\]

### Mutually exclusive events

Events \(A\) and \(B\) are mutually exclusive if they cannot happen at the same time:

\[
P(A\cap B)=0.
\]

If they are mutually exclusive, then

\[
P(A\cup B)=P(A)+P(B).
\]

### Addition law

For any two events,

\[
P(A\cup B)=P(A)+P(B)-P(A\cap B).
\]

The subtraction prevents the overlap from being counted twice.

## Core Theory

### 1. “Given that” means restrict the sample space

When a question says

\[
P(A\mid B),
\]

you are no longer looking at the whole sample space. You are only looking inside \(B\).

So

\[
P(A\mid B)=\frac{\text{part of }B\text{ that is also in }A}{\text{all of }B}.
\]

That is why

\[
P(A\mid B)=\frac{P(A\cap B)}{P(B)}.
\]

[VISUAL PLACEHOLDER: A22ConditionalProbabilitySVG-002 | Source: CCEA A22-PROB and Conditional Probability PDF | Insert from svg/A22ConditionalProbabilitySVG-002.svg | Purpose: Show \(B\) as the restricted sample space and \(A\cap B\) as the favourable part.]

### 2. Tree diagrams and conditional branches

In a tree diagram, probabilities after the first branch are often conditional.

If the first event is \(A\), then the branch for \(B\) after \(A\) is

\[
P(B\mid A).
\]

Along a path, multiply:

\[
P(A\cap B)=P(A)P(B\mid A).
\]

Then rearrange:

\[
P(B\mid A)=\frac{P(A\cap B)}{P(A)}.
\]

[VISUAL PLACEHOLDER: A22ConditionalProbabilityTikZ-001 | Source: Transcript Conditional Probability 2 | Insert from tikz/A22ConditionalProbabilityTikZ-001.tex | Purpose: Show a two-stage probability tree with \(P(A)\), \(P(A')\), \(P(B\mid A)\), \(P(B'\mid A)\), \(P(B\mid A')\), and \(P(B'\mid A')\).]

[VISUAL PLACEHOLDER: A22ConditionalProbabilityTikZ-002 | Source: CCEA A22-PROB + teacher transcript | Insert from tikz/A22ConditionalProbabilityTikZ-002.tex | Purpose: Show a two-day late/not-late conditional probability tree where the second-day probability depends on the first day.]

### 3. Two-way tables

Two-way tables are excellent for “given that” questions because the given condition usually tells you which row or column to use.

If the table shows 100 students and the question asks

\[
P(F\mid B'),
\]

you read this as

\[
\text{probability of French given not boy}.
\]

So the denominator is the total number of non-boys, not the total number of students.

### 4. Venn diagrams

Venn diagrams help with:

- identifying \(A\cap B\);
- identifying \(A\cup B\);
- identifying complements such as \(A'\);
- seeing restricted sample spaces;
- filling in unknown probabilities.

A key exam habit from the transcript is to draw the outside rectangle. Missing the rectangle can lose marks because the outside region is part of the sample space.

## Visual Asset Integration

[VISUAL PLACEHOLDER: A22ConditionalProbabilityMermaid-001 | Source: CCEA Maths specification map + lesson evidence | Insert from mermaid/A22ConditionalProbabilityMermaid-001.md | Purpose: Show the exam-method decision flow for conditional probability questions.]

[VISUAL PLACEHOLDER: A22ConditionalProbabilitySVG-003 | Source: Conditional Probability PDF page 16 | Insert from svg/A22ConditionalProbabilitySVG-003.svg | Purpose: Show aces and diamonds in a 52-card Venn diagram with regions \(3,1,12,36\).]

[VISUAL PLACEHOLDER: A22ConditionalProbabilitySVG-004 | Source: Conditional Probability transcript and lesson evidence | Insert from svg/A22ConditionalProbabilitySVG-004.svg | Purpose: Show the completed three-event Venn diagram where \(A\) and \(C\) are mutually exclusive, \(B\) overlaps both, and \(B\) and \(C\) are independent.]

[INTERACTIVE PLACEHOLDER: A22ConditionalProbabilityWidget-001 | Source: CCEA A22-PROB and lesson evidence | Insert from widgets/A22ConditionalProbabilityWidget-001.html | Purpose: Let the student click a condition such as \(B\), \(B'\), or \(A\cup B\), then see the sample space shrink and the conditional probability update.]

## Worked Examples

### Worked Example 1: Set notation with a die

Let

\[
S=\{1,2,3,4,5,6\},
\]

\[
A=\text{rolling an even number}=\{2,4,6\},
\]

\[
B=\text{rolling a prime number}=\{2,3,5\}.
\]

#### a) Find \(A'\)

\[
A'=\text{not rolling an even number}.
\]

The outcomes not in \(A\) are \(1,3,5\). So

\[
A'=\{1,3,5\}.
\]

#### b) Find \(A\cup B\)

\[
A\cup B=\text{rolling an even number or a prime number}.
\]

\[
A=\{2,4,6\},\qquad B=\{2,3,5\}.
\]

Therefore

\[
A\cup B=\{2,3,4,5,6\}.
\]

Do not repeat the \(2\).

#### c) Find \(A\cap B\)

\[
A\cap B=\text{rolling a number that is even and prime}.
\]

The only outcome in both sets is \(2\). So

\[
A\cap B=\{2\}.
\]

#### d) Find \(A\cap B'\)

First find

\[
B'=\text{not prime}.
\]

Since

\[
B=\{2,3,5\},
\]

we have

\[
B'=\{1,4,6\}.
\]

Now intersect with \(A\):

\[
A\cap B'=\{2,4,6\}\cap \{1,4,6\}=\{4,6\}.
\]

### Worked Example 2: Cards, aces and diamonds

A card is selected at random from a pack of 52 playing cards. Let

\[
A=\text{the event that the card is an ace},
\]

and

\[
D=\text{the event that the card is a diamond}.
\]

The Venn regions are:

\[
A\cap D=1,
\]

\[
A\cap D'=3,
\]

\[
A'\cap D=12,
\]

\[
A'\cap D'=36.
\]

These add to

\[
1+3+12+36=52.
\]

#### a) Find \(P(A\cap D)\)

\[
P(A\cap D)=\frac{1}{52}.
\]

#### b) Find \(P(A\cup D)\)

The union contains all aces and all diamonds:

\[
3+1+12=16.
\]

So

\[
P(A\cup D)=\frac{16}{52}.
\]

#### c) Find \(P(A')\)

There are 4 aces, so there are

\[
52-4=48
\]

cards that are not aces.

\[
P(A')=\frac{48}{52}.
\]

#### d) Find \(P(A'\cap D)\)

This means the card is not an ace but is a diamond. The diamond-but-not-ace region is 12.

\[
P(A'\cap D)=\frac{12}{52}.
\]

### Worked Example 3: Independent and mutually exclusive events in a Venn diagram

Given

\[
P(A)=0.3,
\]

\[
P(B)=0.4,
\]

\[
P(A\cap B)=0.25.
\]

#### a) Explain why \(A\) and \(B\) are not independent

If \(A\) and \(B\) were independent, then

\[
P(A\cap B)=P(A)P(B).
\]

Calculate:

\[
P(A)P(B)=0.3\times 0.4=0.12.
\]

But

\[
P(A\cap B)=0.25.
\]

Since

\[
0.12\ne 0.25,
\]

the events are not independent.

#### b) Add a third event \(C\)

Given also:

\[
P(C)=0.2,
\]

\(A\) and \(C\) are mutually exclusive, and \(B\) and \(C\) are independent.

Since \(A\) and \(C\) are mutually exclusive,

\[
P(A\cap C)=0.
\]

So \(A\) and \(C\) do not overlap.

Since \(B\) and \(C\) are independent,

\[
P(B\cap C)=P(B)P(C).
\]

Substitute:

\[
P(B\cap C)=0.4\times 0.2=0.08.
\]

We already know

\[
P(A\cap B)=0.25.
\]

Since

\[
P(A)=0.3,
\]

the part of \(A\) not in \(B\) is

\[
0.3-0.25=0.05.
\]

Since

\[
P(C)=0.2
\]

and

\[
P(B\cap C)=0.08,
\]

the part of \(C\) not in \(B\) is

\[
0.2-0.08=0.12.
\]

Since

\[
P(B)=0.4,
\]

and \(B\) contains

\[
0.25+0.08+\text{middle-only part of }B,
\]

we get

\[
0.25+0.08=0.33.
\]

Therefore the remaining part of \(B\) is

\[
0.4-0.33=0.07.
\]

Now add all known regions:

\[
0.25+0.05+0.08+0.12+0.07=0.57.
\]

The outside region is

\[
1-0.57=0.43.
\]

#### c) Find \(P(C\cup(A\cap B'))\)

First identify \(C\):

\[
P(C)=0.2.
\]

Next identify

\[
A\cap B'.
\]

This is the part in \(A\) but not in \(B\), which is

\[
0.05.
\]

Since \(A\) and \(C\) are mutually exclusive, these two regions do not overlap.

Therefore

\[
P(C\cup(A\cap B'))=0.2+0.05=0.25.
\]

### Worked Example 4: The conditional probability formula

Suppose

\[
P(C\mid D)=0.3,
\]

and

\[
P(D)=0.6.
\]

Find

\[
P(C\cap D).
\]

Start with the conditional probability formula:

\[
P(C\mid D)=\frac{P(C\cap D)}{P(D)}.
\]

Substitute the known values:

\[
0.3=\frac{P(C\cap D)}{0.6}.
\]

Multiply both sides by \(0.6\):

\[
0.3\times 0.6=P(C\cap D).
\]

\[
0.18=P(C\cap D).
\]

So

\[
P(C\cap D)=0.18.
\]

### Worked Example 5: Two-way table and restricted sample space

A two-way table shows students by gender and whether they study French.

|  | French | Not French | Total |
|---|---:|---:|---:|
| Boys | 14 | 26 | 40 |
| Not boys | 38 | 22 | 60 |
| Total | 52 | 48 | 100 |

Let

\[
B=\text{student is a boy},
\]

and

\[
F=\text{student studies French}.
\]

#### a) Find \(P(F\mid B')\)

This means:

\[
\text{probability the student studies French given the student is not a boy}.
\]

The condition is \(B'\), so restrict to the \(B'\) row.

There are 60 students who are not boys. Of these, 38 study French.

Therefore

\[
P(F\mid B')=\frac{38}{60}.
\]

#### b) Find \(P(B\mid F')\)

This means:

\[
\text{probability the student is a boy given the student does not study French}.
\]

The condition is \(F'\), so restrict to the Not French column.

There are 48 students who do not study French. Of these, 26 are boys.

Therefore

\[
P(B\mid F')=\frac{26}{48}.
\]

### Worked Example 6: Esports Venn diagram and independence

Shumi and Tom both play for an esports team.

Let

\[
S=\text{Shumi wins her match},
\]

and

\[
T=\text{Tom wins his match}.
\]

Given:

\[
P(S)=0.25,
\]

\[
P(T)=0.3,
\]

\[
P(S\cup T)=0.4.
\]

#### a) Find \(P(S\cap T)\)

Use the addition law:

\[
P(S\cup T)=P(S)+P(T)-P(S\cap T).
\]

Substitute:

\[
0.4=0.25+0.3-P(S\cap T).
\]

\[
0.4=0.55-P(S\cap T).
\]

Rearrange:

\[
P(S\cap T)=0.55-0.4=0.15.
\]

#### b) Complete the Venn diagram

The \(S\)-only region is

\[
P(S)-P(S\cap T)=0.25-0.15=0.10.
\]

The \(T\)-only region is

\[
P(T)-P(S\cap T)=0.3-0.15=0.15.
\]

The outside region is

\[
1-P(S\cup T)=1-0.4=0.6.
\]

#### c) Find \(P(S'\mid T')\)

The condition is \(T'\), so the denominator is everything outside \(T\).

From the Venn diagram, \(T'\) contains:

\[
0.10+0.60=0.70.
\]

The event \(S'\cap T'\) is outside both circles:

\[
0.60.
\]

Therefore

\[
P(S'\mid T')=\frac{P(S'\cap T')}{P(T')}=\frac{0.60}{0.70}=\frac{6}{7}.
\]

#### d) Explain why \(S\) and \(T\) are not independent

One way is to compare:

\[
P(S'\mid T')
\]

with

\[
P(S').
\]

We have

\[
P(S'\mid T')=\frac{6}{7}.
\]

Also

\[
P(S')=1-P(S)=1-0.25=0.75.
\]

Since

\[
\frac{6}{7}\ne 0.75,
\]

the events are not independent.

### Worked Example 7: Tree diagram with changing probabilities

Jerry may be late to school on Monday, Tuesday and Wednesday.

Given:

\[
P(\text{late on Monday})=0.2.
\]

If Jerry was late one day, then

\[
P(\text{late the next day})=0.3.
\]

So

\[
P(\text{not late the next day}\mid \text{late the previous day})=1-0.3=0.7.
\]

If Jerry was not late one day, then

\[
P(\text{late the next day})=0.15.
\]

So

\[
P(\text{not late the next day}\mid \text{not late the previous day})=1-0.15=0.85.
\]

Find the probability that Jerry is late exactly one day out of Monday, Tuesday and Wednesday.

There are three possible paths.

#### Path 1: Late, not late, not late

\[
0.2\times 0.7\times 0.85=0.119.
\]

#### Path 2: Not late, late, not late

\[
0.8\times 0.15\times 0.7=0.084.
\]

#### Path 3: Not late, not late, late

\[
0.8\times 0.85\times 0.15=0.102.
\]

Add these:

\[
P(\text{exactly one late day})=0.119+0.084+0.102=0.305.
\]

## Guided Practice

### Question 1

Let

\[
A=\{2,4,6\},\qquad B=\{2,3,5\},\qquad S=\{1,2,3,4,5,6\}.
\]

Find:

a) \(B'\)

b) \(A\cap B\)

c) \(A\cup B\)

d) \(A'\cap B\)

### Question 2

Given

\[
P(A)=0.45,
\]

\[
P(B)=0.6,
\]

\[
P(A\cap B)=0.18,
\]

find

\[
P(A\mid B).
\]

### Question 3

Given

\[
P(C\mid D)=0.25,
\]

and

\[
P(D)=0.8,
\]

find

\[
P(C\cap D).
\]

### Question 4

A table shows students who study Spanish.

|  | Spanish | Not Spanish | Total |
|---|---:|---:|---:|
| Boys | 18 | 12 | 30 |
| Girls | 22 | 28 | 50 |
| Total | 40 | 40 | 80 |

Let

\[
B=\text{student is a boy},
\]

and

\[
S=\text{student studies Spanish}.
\]

Find:

a) \(P(S\mid B)\)

b) \(P(B\mid S)\)

c) \(P(S'\mid B')\)

### Question 5

Given

\[
P(A)=0.4,
\]

\[
P(B)=0.5,
\]

\[
P(A\cap B)=0.2,
\]

are \(A\) and \(B\) independent?

### Question 6

A student catches a bus on Monday, Tuesday and Wednesday.

\[
P(\text{late on Monday})=0.1.
\]

If the bus is late one day, the probability it is late the next day is \(0.25\).

If the bus is not late one day, the probability it is late the next day is \(0.05\).

Find the probability that the bus is late exactly one day.

## Common Mistakes and Exam Traps

### Trap 1: Reading \(P(A\mid B)\) backwards

\[
P(A\mid B)
\]

means probability of \(A\), given \(B\).

It does **not** mean probability of \(B\), given \(A\).

The denominator is

\[
P(B),
\]

not

\[
P(A).
\]

### Trap 2: Forgetting to shrink the sample space

For

\[
P(A\mid B),
\]

you only count inside \(B\).

The new total is not always 1, 52, 100 or the full table total. It is the size or probability of the condition.

### Trap 3: Treating independent and mutually exclusive as the same

Independent means one event does not affect the probability of the other:

\[
P(A\mid B)=P(A).
\]

Mutually exclusive means the events cannot happen together:

\[
P(A\cap B)=0.
\]

### Trap 4: Missing the outside of a Venn diagram

The outside region is part of the sample space. Draw the rectangle. Include the outside probability.

### Trap 5: Using tree diagrams without checking whether probabilities change

If the second-stage probability depends on the first-stage result, label it as conditional:

\[
P(B\mid A),
\]

not simply

\[
P(B).
\]

### Trap 6: Not writing the formula immediately

If a question uses “given that”, immediately write down the conditional probability law:

\[
P(A\mid B)=\frac{P(A\cap B)}{P(B)}.
\]

If it says events are independent, immediately write down the independence laws.

## Exam Technique Notes

When you see **given that**, write:

\[
P(A\mid B)=\frac{P(A\cap B)}{P(B)}.
\]

When you see **independent**, write:

\[
P(A\cap B)=P(A)P(B),
\]

or

\[
P(A\mid B)=P(A).
\]

When you see **mutually exclusive**, write:

\[
P(A\cap B)=0.
\]

When you see **or**, think union:

\[
P(A\cup B)=P(A)+P(B)-P(A\cap B).
\]

When you see a **table**, use the row or column named after “given that”.

When you see a **Venn diagram**, label every region before answering the final probability question.

## Full Worked Solutions to Guided Practice

### Solution 1

\[
A=\{2,4,6\},\qquad B=\{2,3,5\},\qquad S=\{1,2,3,4,5,6\}.
\]

#### a)

\[
B'=\{1,4,6\}.
\]

#### b)

\[
A\cap B=\{2,4,6\}\cap \{2,3,5\}=\{2\}.
\]

#### c)

\[
A\cup B=\{2,4,6\}\cup \{2,3,5\}=\{2,3,4,5,6\}.
\]

#### d)

\[
A'=S\setminus A=\{1,3,5\}.
\]

\[
A'\cap B=\{1,3,5\}\cap \{2,3,5\}=\{3,5\}.
\]

### Solution 2

Given:

\[
P(A)=0.45,\qquad P(B)=0.6,\qquad P(A\cap B)=0.18.
\]

Use:

\[
P(A\mid B)=\frac{P(A\cap B)}{P(B)}.
\]

Substitute:

\[
P(A\mid B)=\frac{0.18}{0.6}=0.3.
\]

### Solution 3

Given:

\[
P(C\mid D)=0.25,\qquad P(D)=0.8.
\]

Use:

\[
P(C\mid D)=\frac{P(C\cap D)}{P(D)}.
\]

Substitute:

\[
0.25=\frac{P(C\cap D)}{0.8}.
\]

Multiply both sides by \(0.8\):

\[
0.25\times 0.8=P(C\cap D).
\]

\[
P(C\cap D)=0.2.
\]

### Solution 4

|  | Spanish | Not Spanish | Total |
|---|---:|---:|---:|
| Boys | 18 | 12 | 30 |
| Girls | 22 | 28 | 50 |
| Total | 40 | 40 | 80 |

#### a) Find \(P(S\mid B)\)

The condition is \(B\), so only use the Boys row.

There are 30 boys. Of these, 18 study Spanish.

\[
P(S\mid B)=\frac{18}{30}=\frac{3}{5}.
\]

#### b) Find \(P(B\mid S)\)

The condition is \(S\), so only use the Spanish column.

There are 40 Spanish students. Of these, 18 are boys.

\[
P(B\mid S)=\frac{18}{40}=\frac{9}{20}.
\]

#### c) Find \(P(S'\mid B')\)

The condition is \(B'\), so use the Girls row.

There are 50 girls. Of these, 28 do not study Spanish.

\[
P(S'\mid B')=\frac{28}{50}=\frac{14}{25}.
\]

### Solution 5

Given:

\[
P(A)=0.4,\qquad P(B)=0.5,\qquad P(A\cap B)=0.2.
\]

If \(A\) and \(B\) are independent,

\[
P(A\cap B)=P(A)P(B).
\]

Calculate:

\[
P(A)P(B)=0.4\times 0.5=0.2.
\]

Since

\[
P(A\cap B)=0.2
\]

and

\[
P(A)P(B)=0.2,
\]

we have

\[
P(A\cap B)=P(A)P(B).
\]

Therefore \(A\) and \(B\) are independent.

### Solution 6

Let

\[
L=\text{late},\qquad N=\text{not late}.
\]

Given:

\[
P(L\text{ on Monday})=0.1.
\]

So

\[
P(N\text{ on Monday})=1-0.1=0.9.
\]

If late one day:

\[
P(L\text{ next day}\mid L\text{ previous day})=0.25,
\]

so

\[
P(N\text{ next day}\mid L\text{ previous day})=1-0.25=0.75.
\]

If not late one day:

\[
P(L\text{ next day}\mid N\text{ previous day})=0.05,
\]

so

\[
P(N\text{ next day}\mid N\text{ previous day})=1-0.05=0.95.
\]

Exactly one late day can happen in three ways.

#### Case 1: Late, not late, not late

\[
0.1\times 0.75\times 0.95=0.07125.
\]

#### Case 2: Not late, late, not late

\[
0.9\times 0.05\times 0.75=0.03375.
\]

#### Case 3: Not late, not late, late

\[
0.9\times 0.95\times 0.05=0.04275.
\]

Now add:

\[
0.07125+0.03375+0.04275=0.14775.
\]

Therefore

\[
P(\text{late exactly one day})=0.14775.
\]

## Common CCEA-Style Wording

| Wording | First mathematical move |
|---|---|
| “Given that \(B\) occurred…” | Write \(P(A\mid B)=\frac{P(A\cap B)}{P(B)}\) |
| “Events \(A\) and \(B\) are independent…” | Write \(P(A\cap B)=P(A)P(B)\) |
| “Events \(A\) and \(B\) are mutually exclusive…” | Write \(P(A\cap B)=0\) |
| “Find the probability of \(A\) or \(B\)” | Use \(P(A\cup B)\) |
| “Find the probability of \(A\) and \(B\)” | Use \(P(A\cap B)\) |
| “Explain why the events are not independent” | Show \(P(A\mid B)\ne P(A)\) or \(P(A\cap B)\ne P(A)P(B)\) |
| “Critique the assumption” | Explain whether independence, fairness or equal likelihood is realistic |

## Syllabus Gap Check

| LO ID | Status | Notes |
|---|---|---|
| A22-PROB-LO001 | Covered | Venn diagrams, tree diagrams and two-way tables included |
| A22-PROB-LO002 | Covered | Formula derived, rearranged and applied |
| A22-PROB-LO003 | Covered | Independence, mutual exclusivity, fairness and changing probabilities discussed |

## Visual and Interactive Asset Plan

| Asset ID | Type | Phase | Purpose |
|---|---|---:|---|
| A22ConditionalProbabilityMermaid-001 | Mermaid | Phase 2 | Decision flow for choosing formula/table/Venn/tree |
| A22ConditionalProbabilitySVG-001 | SVG | Phase 3 | Die Venn diagram for set notation |
| A22ConditionalProbabilitySVG-002 | SVG | Phase 3 | Restricted sample space diagram for \(P(A\mid B)\) |
| A22ConditionalProbabilitySVG-003 | SVG | Phase 3 | Cards Venn diagram |
| A22ConditionalProbabilitySVG-004 | SVG | Phase 3 | Completed three-event Venn diagram |
| A22ConditionalProbabilityTikZ-001 | TikZ | Phase 4 | Conditional tree diagram |
| A22ConditionalProbabilityTikZ-002 | TikZ | Phase 4 | Concrete late/not-late conditional tree |
| A22ConditionalProbabilityWidget-001 | HTML widget | Phase 5 | Interactive restricted sample space highlighter |

## Supplementary Sources Used

No external web sources were used.

The uploaded DrFrost/Statistics Year 2 material is treated as cross-board or third-party lesson evidence, used only because the CCEA A22-PROB specification confirms that conditional probability, Venn diagrams, tree diagrams, two-way tables and modelling assumptions are on-spec.

## Missing Evidence Log

| Missing item | Expected use | Impact on lesson | Action taken |
|---|---|---|---|
| Topic-specific README for this exact chapter | Confirm exact topic slug and file naming | Low | Inferred from CCEA specification map and lesson evidence |
| Topic-specific evidence checklist | Confirm intended evidence coverage for this exact chapter | Low | Used project-wide evidence checklist |
| CCEA-branded conditional probability exam questions | Provide exact CCEA exam wording | Medium | Used only on-spec lesson evidence and generated aligned practice |
| Fully parsed text from screenshot PDF | Verify every screenshot page | Low/Medium | Logged limitation; used transcript and parsed lesson PDF as core evidence |
| Complete context for every screenshot visual | Rebuild every visual exactly | Medium | Created evidence-aligned teaching visuals only where supported |

## Off-Spec or Boundary-Risk Log

| Evidence item | Why it is risky | Decision |
|---|---|---|
| DrFrostMaths PDF and lesson evidence | Cross-board or third-party source, not CCEA branded | Used only where CCEA A22-PROB confirms content is on-spec |
| MAT/UKMT extension references | Extension material outside CCEA core lesson requirement | Excluded from core lesson |
| Hypothesis testing references | Future A22 topic, not this conditional probability lesson | Excluded except as onward context |
| GCSE recap references in transcript | Not A-Level core evidence | Treated only as prerequisite context, no GCSE source used |
| Uninspected screenshot-only details | Visual evidence not fully parsed | No uninspected detail invented |

## Final Student Checklist

Before moving on, check that you can:

- [ ] Explain what \(P(A\mid B)\) means.
- [ ] Identify the event being conditioned on.
- [ ] Use \(P(A\mid B)=\frac{P(A\cap B)}{P(B)}\).
- [ ] Rearrange to find \(P(A\cap B)=P(B)P(A\mid B)\).
- [ ] Use a Venn diagram to identify intersections, unions and complements.
- [ ] Use a two-way table by restricting to the correct row or column.
- [ ] Use a tree diagram when later probabilities depend on earlier outcomes.
- [ ] Test independence using \(P(A\cap B)=P(A)P(B)\).
- [ ] Recognise mutually exclusive events using \(P(A\cap B)=0\).
- [ ] Critique assumptions such as independence, fairness and equal likelihood.
