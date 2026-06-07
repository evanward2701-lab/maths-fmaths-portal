# AS2 Probability

## Title and Metadata

| Field | Value |
|---|---|
| Lesson title | AS2 Probability |
| Course | CCEA GCE Mathematics |
| Unit | AS 2 Applied Mathematics |
| Applied strand | Statistics |
| Topic code | AS2-PROB |
| Topic name | Probability |
| Topic slug | probability |
| Topic Pascal | Probability |
| Topic ID | AS2Probability |
| Lesson file | AS2_probability_lesson.md |
| Learning outcome IDs | AS2-PROB-LO001, AS2-PROB-LO002, AS2-PROB-LO003 |
| Tags | `#AS2`, `#Probability`, `#VennDiagram`, `#TreeDiagram`, `#TwoWayTable`, `#Independence`, `#MutuallyExclusive`, `#ExamTechnique` |

---

## Evidence Map

| Source | What it contributes |
|---|---|
| CCEA Mathematics Specification Map | Official AS2 Probability topic identity, LO IDs and syllabus boundaries. |
| Project README Module Map | Lesson structure, naming conventions and asset placeholder format. |
| Project Evidence Checklist | Missing evidence log, off-spec log and visual evidence rules. |
| `S1-Chp5-Probability.pdf` | Definitions, overview, Venn diagram examples, mutually exclusive/independent examples, tree diagram examples. |
| `Chapter_5_Probability_🤖_(Applied_Year_1)_Transcript.md` | Teacher explanations, worked examples, warnings, arithmetic and method commentary. |
| `Chapter_5_Probability_🤖_(Applied_Year_1)_Screenshots.pdf` | Visual support only. Parsed text unavailable, so no uninspected details are claimed. |

### Missing Evidence Log

| Missing item | Expected use | Impact on lesson | Action taken |
|---|---|---|---|
| Topic-specific README/module map | Exact local topic metadata | Low | Metadata inferred from CCEA spec map and project module map. |
| Topic-specific evidence checklist | Evidence completion tracking | Low | Project-wide evidence checklist used. |
| Official CCEA probability questions and mark schemes | Exact CCEA mark allocation | Medium | Generated CCEA-style practice without claiming official status. |
| Pearson textbook pages 71-80 | Exercise detail | Medium | Did not reproduce unseen textbook exercises. |
| Fully parseable screenshot PDF | Visual details and teacher annotations | Medium | Used parsed slide PDF and transcript as core. |

### Off-Spec or Boundary-Risk Log

| Evidence item | Why it is risky | Decision |
|---|---|---|
| Conditional probability formula | AS2-PROB-LO003 explicitly excludes conditional probability | Excluded from core. |
| “Given that Jason runs” exercise part | Conditional probability-style wording | Excluded from AS2 core. |
| Binomial distribution links | Belongs to AS2 Statistical Distributions | Forward link only. |
| Transcript comment that set notation is not needed until Year 2 | CCEA AS2 says students must be familiar with set notation | Basic set notation included. |
| Pearson exercise references | Textbook pages not supplied | Not reproduced. |

---

## Specification Alignment

| LO ID | Official learning outcome focus | Lesson coverage |
|---|---|---|
| AS2-PROB-LO001 | Demonstrate understanding of and use the addition and multiplication laws | Complement rule, addition law, mutually exclusive addition, independent multiplication, tree-path multiplication. |
| AS2-PROB-LO002 | Demonstrate understanding of and use mutually exclusive events, exhaustive events and statistical dependence and independence | Definitions, diagrams, calculations and independence tests. |
| AS2-PROB-LO003 | Calculate combined probabilities of up to three events, using tree diagrams, Venn diagrams and two-way tables | Two-set Venn diagrams, three-set Venn diagrams, tree diagrams and two-way tables. Conditional probability excluded. |

---

## Learning Objectives

By the end of this lesson, you should be able to:

1. Define and use the language of probability: experiment, outcome, event and sample space.
2. Represent events using Venn diagrams, tree diagrams and two-way tables.
3. Use the addition law for probabilities.
4. Use the multiplication law for independent events.
5. Recognise and handle mutually exclusive events.
6. Recognise exhaustive events.
7. Test whether two events are statistically independent.
8. Calculate combined probabilities involving up to three events.
9. Know the AS2 boundary: conditional probability is not required in this topic.

---

## Prerequisite Recap

This lesson does not rely on external GCSE sources. The following skills are prior mathematical tools needed to access the A-Level material.

| Prior skill | Why it matters here |
|---|---|
| Fractions | Most exact probabilities should be left as fractions unless decimals are requested. |
| Decimals and percentages | Some examples use probabilities such as 0.6, 0.85 and 0.3. |
| Table reading | Sample spaces and two-way tables depend on accurate row and column reading. |
| Set language | CCEA expects familiarity with set notation in AS2 Probability. |
| Simple algebra | Independence tests require comparing products such as \(P(A)P(B)\) with \(P(A\cap B)\). |
| Diagram interpretation | Venn diagrams and tree diagrams are part of the method, not decoration. |

---

## Big Picture Explanation

Probability is the mathematical machinery for handling uncertainty. In statistics, it sits on the theoretical side of the course: instead of only describing collected data, we model what we expect to happen and compare that expectation with reality.

The central question is:

> How do we calculate the chance of combined events without double-counting, missing cases, or pretending related events are independent?

| Tool | Best for |
|---|---|
| Sample-space table | Listing equally likely outcomes from two simple experiments, such as two spinners or two dice. |
| Venn diagram | Combining event sets, especially with “and”, “or”, “not”, frequencies and probabilities. |
| Tree diagram | Events happening in succession, especially when branch probabilities multiply along paths. |
| Two-way table | Sorting outcomes by two categories and extracting row, column and intersection probabilities. |

This topic is also a launchpad for later statistics. Tree diagrams and repeated-event reasoning help prepare for the binomial distribution, but binomial distribution calculations belong to the next topic, not this one.

---

## Key Definitions and Notation

### Experiment

An **experiment** is a repeatable process that gives rise to a number of outcomes.

Examples include rolling a die, spinning a spinner, choosing a student at random, selecting a counter from a bag, or checking whether it is raining.

### Outcome

An **outcome** is one possible result of an experiment.

For a fair six-sided die:

\[
1,\ 2,\ 3,\ 4,\ 5,\ 6
\]

### Event

An **event** is a set of one or more outcomes. We often use capital letters to represent events.

Example:

Let \(E\) be the event “rolling an even number”.

\[
E=\{2,4,6\}
\]

Let \(P\) be the event “rolling a prime number”.

\[
P=\{2,3,5\}
\]

The outcome \(2\) belongs to both \(E\) and \(P\), because \(2\) is both even and prime.

### Sample Space

The **sample space** is the set of all possible outcomes.

For a fair six-sided die:

\[
S=\{1,2,3,4,5,6\}
\]

In a Venn diagram, the sample space is usually shown as the rectangle.

### Probability of an Event

For equally likely outcomes:

\[
P(A)=\frac{\text{number of outcomes in event }A}{\text{total number of outcomes in the sample space}}
\]

A probability must satisfy:

\[
0\leq P(A)\leq 1
\]

The whole sample space has probability:

\[
P(S)=1
\]

The impossible event has probability:

\[
0
\]

### Complement

The complement of \(A\), written \(A'\), means “not \(A\)”.

\[
P(A')=1-P(A)
\]

### Intersection

The intersection of \(A\) and \(B\), written:

\[
A\cap B
\]

means “\(A\) and \(B\)”.

\[
P(A\cap B)=P(\text{\(A\) and \(B\)})
\]

### Union

The union of \(A\) and \(B\), written:

\[
A\cup B
\]

means “\(A\) or \(B\) or both”.

\[
P(A\cup B)=P(\text{\(A\) or \(B\)})
\]

The word “or” in probability normally includes the overlap unless the question clearly says otherwise.

### Mutually Exclusive Events

Two events are **mutually exclusive** if they cannot happen at the same time.

If \(A\) and \(B\) are mutually exclusive, then:

\[
P(A\cap B)=0
\]

and:

\[
P(A\cup B)=P(A)+P(B)
\]

### Exhaustive Events

Events are **exhaustive** if together they cover the whole sample space.

If \(A\) and \(B\) are exhaustive, then:

\[
P(A\cup B)=1
\]

Events can be exhaustive without being mutually exclusive unless the question states or implies no overlap.

### Independent Events

Two events are **independent** if whether one event happens does not affect the probability of the other happening.

If \(A\) and \(B\) are independent, then:

\[
P(A\cap B)=P(A)P(B)
\]

This formula is also used as a test for independence.

If:

\[
P(A\cap B)\neq P(A)P(B)
\]

then \(A\) and \(B\) are **not independent**. They are statistically dependent.

---

## Core Theory

## 1. Probability from a Sample Space

When all outcomes are equally likely, probability is a counting fraction:

\[
P(A)=\frac{\text{favourable outcomes}}{\text{total outcomes}}
\]

For a fair six-sided die:

\[
S=\{1,2,3,4,5,6\}
\]

Let \(E=\) “rolling an even number”.

\[
E=\{2,4,6\}
\]

So:

\[
P(E)=\frac{3}{6}=\frac12
\]

Let \(P=\) “rolling a prime number”.

\[
P=\{2,3,5\}
\]

So:

\[
P(P)=\frac{3}{6}=\frac12
\]

The event “even and prime” is:

\[
E\cap P=\{2\}
\]

So:

\[
P(E\cap P)=\frac16
\]

The event “neither even nor prime” is:

\[
\{1\}
\]

So:

\[
P(\text{neither even nor prime})=\frac16
\]

[VISUAL PLACEHOLDER: AS2ProbabilitySVG-001 | Source: DrFrost probability concepts slide + transcript | Insert from svg/AS2ProbabilitySVG-001.svg | Purpose: Show a sample space rectangle for a die with event sets \(E\) for even and \(P\) for prime.]

## 2. Sample-Space Tables

If an experiment is made from two underlying experiments, a table is often the cleanest way to list outcomes.

For example:

- spinner 1 gives \(1,2,3,4\);
- spinner 2 gives \(1,2,3,4\);
- the recorded outcome is the sum.

There are:

\[
4\times 4=16
\]

equally likely ordered outcomes.

A sample-space table prevents missing or double-counting outcomes.

[VISUAL PLACEHOLDER: AS2ProbabilitySVG-002 | Source: DrFrost spinner example | Insert from svg/AS2ProbabilitySVG-002.svg | Purpose: Show the \(4\times4\) spinner sum table with sums from \(2\) to \(8\).]

## 3. The Complement Rule

If \(A\) is an event, then either \(A\) happens or \(A'\) happens.

\[
P(A)+P(A')=1
\]

Rearrange:

\[
P(A')=1-P(A)
\]

Common forms:

\[
P(\text{not }A)=1-P(A)
\]

\[
P(\text{neither }A\text{ nor }B)=1-P(A\cup B)
\]

\[
P(\text{at least one})=1-P(\text{none})
\]

## 4. The Addition Law

For two events \(A\) and \(B\):

\[
P(A\cup B)=P(A)+P(B)-P(A\cap B)
\]

When we add \(P(A)+P(B)\), the overlap \(A\cap B\) has been counted twice. Subtracting \(P(A\cap B)\) corrects the double-count.

If \(A\) and \(B\) are mutually exclusive:

\[
P(A\cap B)=0
\]

so:

\[
P(A\cup B)=P(A)+P(B)
\]

[VISUAL PLACEHOLDER: AS2ProbabilitySVG-003 | Source: DrFrost Venn diagram slides | Insert from svg/AS2ProbabilitySVG-003.svg | Purpose: Show why the overlap is subtracted in the general addition law.]

## 5. Venn Diagram Regions

A Venn diagram can contain outcomes, frequencies or probabilities.

| Region | Meaning |
|---|---|
| \(A\cap B\) | \(A\) and \(B\) |
| \(A\cap B'\) | \(A\) but not \(B\) |
| \(A'\cap B\) | \(B\) but not \(A\) |
| \(A'\cap B'\) | neither \(A\) nor \(B\) |

| Expression | Meaning | Diagram instruction |
|---|---|---|
| \(A\cap B\) | \(A\) and \(B\) | Shade only the overlap. |
| \(A\cup B\) | \(A\) or \(B\), including both | Shade all of \(A\) and all of \(B\). |
| \(A'\) | not \(A\) | Shade everything outside \(A\). |
| \(A\cap B'\) | \(A\) and not \(B\) | Shade the part of \(A\) outside \(B\). |

[VISUAL PLACEHOLDER: AS2ProbabilitySVG-004 | Source: DrFrost Venn diagrams slide | Insert from svg/AS2ProbabilitySVG-004.svg | Purpose: Show four Venn shading cases: \(A\cap B\), \(A\cup B\), \(A'\), and \(A\cap B'\).]

## 6. Venn Diagrams with Probabilities

If a Venn diagram is filled with probabilities, all the regions in the sample space must add to:

\[
1
\]

Suppose:

\[
P(A)=0.6
\]

and:

\[
P(A\cup B)=0.85
\]

Then:

\[
P(A'\cap B)=P(A\cup B)-P(A)
\]

\[
P(A'\cap B)=0.85-0.6=0.25
\]

The probability of neither \(A\) nor \(B\) is:

\[
P((A\cup B)')=1-P(A\cup B)=1-0.85=0.15
\]

## 7. Venn Diagrams with Frequencies

If a Venn diagram is filled with frequencies, each region contains a number of items or people.

\[
P(\text{required region})=\frac{\text{frequency in the required region}}{\text{total frequency}}
\]

For three-set Venn diagrams, the safest method is:

1. Start with the centre region, the “all three” overlap.
2. Work out each two-way overlap by subtracting the centre.
3. Work out each “only” region by subtracting all overlaps already inside that set.
4. Work out the outside region last.
5. Check all regions add to the total.

[VISUAL PLACEHOLDER: AS2ProbabilitySVG-005 | Source: DrFrost three-set Venn frequency example | Insert from svg/AS2ProbabilitySVG-005.svg | Purpose: Show the centre-outwards method for filling a three-set Venn diagram.]

## 8. Mutually Exclusive Events

Events \(A\) and \(B\) are mutually exclusive if they cannot happen at the same time.

\[
P(A\cap B)=0
\]

Their Venn diagram has separate loops.

\[
P(A\cup B)=P(A)+P(B)
\]

Picking a heart from a standard deck and picking a diamond from the same single card draw are mutually exclusive. A single card cannot be both a heart and a diamond.

## 9. Exhaustive Events

Events are exhaustive when they cover all possibilities in the sample space.

\[
P(A\cup B)=1
\]

Example: when choosing one counter from a bag containing only red and blue counters, red and blue are exhaustive because every counter is either red or blue.

## 10. Independent and Dependent Events

Two events are independent if one happening does not affect the probability of the other happening.

\[
P(A\cap B)=P(A)P(B)
\]

If this equality is true, the events are independent. If false, they are dependent.

Important warning: independence does **not** mean the Venn circles must be separate. Separate circles mean mutually exclusive, not independent. Independence is tested by probabilities, not by whether the circles “look separate”.

[VISUAL PLACEHOLDER: AS2ProbabilitySVG-006 | Source: DrFrost independent events slide | Insert from svg/AS2ProbabilitySVG-006.svg | Purpose: Compare mutually exclusive Venn diagrams with overlapping Venn diagrams used for independence tests.]

## 11. Tree Diagrams

Tree diagrams show events that happen in succession.

| Rule | Meaning |
|---|---|
| Multiply along a path | This gives the probability of that exact sequence. |
| Add separate successful paths | This gives the probability of any one of several mutually exclusive sequences. |
| Branch probabilities from the same point add to 1 | Each branching point should account for all possibilities from that point. |

If items are selected without replacement, the denominator changes after each selection.

[VISUAL PLACEHOLDER: AS2ProbabilitySVG-007 | Source: DrFrost tree diagrams slide | Insert from svg/AS2ProbabilitySVG-007.svg | Purpose: Show a two-draw without-replacement tree for 3 yellow and 2 green counters.]

## 12. Two-Way Tables

CCEA explicitly includes two-way tables in AS2 Probability.

|  | \(B\) | \(B'\) | Total |
|---|---:|---:|---:|
| \(A\) | \(A\cap B\) | \(A\cap B'\) | \(A\) total |
| \(A'\) | \(A'\cap B\) | \(A'\cap B'\) | \(A'\) total |
| Total | \(B\) total | \(B'\) total | Grand total |

If the table contains frequencies, then:

\[
P(A)=\frac{\text{row total for }A}{\text{grand total}}
\]

\[
P(B)=\frac{\text{column total for }B}{\text{grand total}}
\]

\[
P(A\cap B)=\frac{\text{cell in both }A\text{ and }B}{\text{grand total}}
\]

[VISUAL PLACEHOLDER: AS2ProbabilitySVG-008 | Source: CCEA AS2-PROB-LO003 + lesson-aligned teaching enhancement | Insert from svg/AS2ProbabilitySVG-008.svg | Purpose: Show how a two-way table connects row totals, column totals and intersection probabilities.]

---

## Visual Asset Integration

[INTERACTIVE PLACEHOLDER: AS2ProbabilityWidget-001 | Source: CCEA AS2 Probability specification + DrFrost Venn evidence | Insert from widgets/AS2ProbabilityWidget-001.html | Purpose: Let students select Venn regions and connect notation to shaded areas.]

[INTERACTIVE PLACEHOLDER: AS2ProbabilityWidget-002 | Source: CCEA AS2 Probability specification + DrFrost tree diagram evidence | Insert from widgets/AS2ProbabilityWidget-002.html | Purpose: Let students multiply along tree paths and add mutually exclusive paths.]

---

## Worked Examples

## Worked Example 1: Two fair spinners and a sample-space table

Two fair spinners each have four sectors numbered \(1\) to \(4\). The two spinners are spun together and the sum of the numbers indicated on each spinner is recorded.

Find the probability of a sum of exactly \(5\) and more than \(5\).

The sample-space table is:

\[
\begin{array}{c|cccc}
+ & 1 & 2 & 3 & 4\\
\hline
1 & 2 & 3 & 4 & 5\\
2 & 3 & 4 & 5 & 6\\
3 & 4 & 5 & 6 & 7\\
4 & 5 & 6 & 7 & 8
\end{array}
\]

There are:

\[
4\times 4=16
\]

outcomes.

Exactly \(5\):

\[
(1,4),(2,3),(3,2),(4,1)
\]

so:

\[
P(5)=\frac{4}{16}=\frac14
\]

More than \(5\): there are \(6\) outcomes, so:

\[
P(>5)=\frac{6}{16}=\frac38
\]

Final answers:

\[
\boxed{P(5)=\frac14},\qquad \boxed{P(>5)=\frac38}
\]

## Worked Example 2: Grouped-time probability estimate

The evidence gives frequencies:

\[
6,\ 13,\ 12,\ 5,\ 4
\]

so the total frequency is:

\[
6+13+12+5+4=40
\]

Under \(9\) minutes:

\[
P(\text{under }9)=\frac{6+13}{40}=\frac{19}{40}
\]

Over \(10.5\) minutes is estimated from the interval \(9\leq t<11\), frequency \(12\). The part from \(10.5\) to \(11\) is:

\[
\frac{11-10.5}{11-9}=\frac{0.5}{2}=\frac14
\]

Estimated number in that part:

\[
\frac14\times 12=3
\]

Add later intervals:

\[
3+5+4=12
\]

So:

\[
P(\text{over }10.5)=\frac{12}{40}=\frac{3}{10}
\]

## Worked Example 3: Venn diagram with probabilities

Given:

\[
P(A)=0.6,\qquad P(A\cup B)=0.85
\]

Find \(P(A'\cap B)\):

\[
P(A'\cap B)=P(A\cup B)-P(A)=0.85-0.6=0.25
\]

Find neither:

\[
P(\text{neither }A\text{ nor }B)=1-P(A\cup B)=1-0.85=0.15
\]

## Worked Example 4: Three-set Venn diagram with frequencies

A vet surveys \(100\) clients. She finds:

\[
25 \text{ own dogs},\quad 15 \text{ own dogs and cats},\quad 11 \text{ own dogs and tropical fish}
\]

\[
53 \text{ own cats},\quad 10 \text{ own cats and tropical fish},\quad 7 \text{ own dogs, cats and tropical fish},\quad 40 \text{ own tropical fish}
\]

Let \(D\) = dogs, \(C\) = cats and \(F\) = tropical fish.

Centre:

\[
D\cap C\cap F=7
\]

Pairwise-only regions:

\[
D\cap C\text{ only}=15-7=8
\]

\[
D\cap F\text{ only}=11-7=4
\]

\[
C\cap F\text{ only}=10-7=3
\]

Single-only regions:

\[
D\text{ only}=25-(8+7+4)=6
\]

\[
C\text{ only}=53-(8+7+3)=35
\]

\[
F\text{ only}=40-(4+7+3)=26
\]

Inside total:

\[
6+8+35+4+7+3+26=89
\]

Outside:

\[
100-89=11
\]

Questions:

\[
P(\text{dog only})=\frac{6}{100}=\frac{3}{50}
\]

\[
P(\text{does not own tropical fish})=\frac{60}{100}=\frac35
\]

\[
P(\text{none})=\frac{11}{100}
\]

## Worked Example 5: Exercise survey three-set Venn diagram

A survey of \(100\) people records:

\[
65 \text{ run},\quad 48 \text{ swim},\quad 60 \text{ cycle}
\]

\[
40 \text{ run and swim},\quad 30 \text{ swim and cycle},\quad 35 \text{ run and cycle},\quad 25 \text{ all three}
\]

Centre:

\[
R\cap S\cap C=25
\]

Pairwise-only:

\[
R\cap S\text{ only}=40-25=15
\]

\[
S\cap C\text{ only}=30-25=5
\]

\[
R\cap C\text{ only}=35-25=10
\]

Single-only:

\[
R\text{ only}=65-(15+25+10)=15
\]

\[
C\text{ only}=60-(10+25+5)=20
\]

\[
S\text{ only}=48-(15+25+5)=3
\]

Inside total:

\[
15+15+10+25+5+3+20=93
\]

Outside:

\[
100-93=7
\]

None:

\[
P(\text{none})=\frac{7}{100}=0.07
\]

Swims but does not run:

\[
\frac{3+5}{100}=\frac{8}{100}=0.08
\]

At least two:

\[
\frac{15+10+5+25}{100}=\frac{55}{100}=0.55
\]

Evidence correction note: the transcript arithmetic gives \(55/100\) and then says \(0.05\). The correct decimal is \(0.55\).

The “Given that Jason runs” part is conditional probability-style wording and is excluded from AS2 core.

## Worked Example 6: Mutually exclusive events

Events \(A\) and \(B\) are mutually exclusive.

\[
P(A)=0.2,\qquad P(B)=0.4
\]

Since mutually exclusive:

\[
P(A\cap B)=0
\]

\[
P(A\cup B)=P(A)+P(B)=0.2+0.4=0.6
\]

\[
P(A\cap B')=P(A)=0.2
\]

\[
P(\text{neither})=1-0.6=0.4
\]

## Worked Example 7: Independent events multiplication law

Events \(A\) and \(B\) are independent.

\[
P(A)=\frac13,\qquad P(B)=\frac15
\]

Therefore:

\[
P(A\cap B)=P(A)P(B)=\frac13\times\frac15=\frac{1}{15}
\]

## Worked Example 8: Testing independence from a Venn diagram

A Venn diagram has regions:

\[
A\text{ only}=3,
\quad A\cap B=4,
\quad B\text{ only}=5,
\quad B\cap C=10,
\quad C\text{ only}=7,
\quad \text{outside}=1
\]

Total:

\[
3+4+5+10+7+1=30
\]

\[
P(B\cup C)=\frac{4+5+10+7}{30}=\frac{26}{30}=\frac{13}{15}
\]

Test \(A\) and \(B\):

\[
P(A)=\frac{3+4}{30}=\frac{7}{30}
\]

\[
P(B)=\frac{4+5+10}{30}=\frac{19}{30}
\]

\[
P(A\cap B)=\frac{4}{30}
\]

\[
P(A)P(B)=\frac{7}{30}\times\frac{19}{30}=\frac{133}{900}
\]

\[
P(A\cap B)=\frac{4}{30}=\frac{120}{900}
\]

Since:

\[
\frac{120}{900}\neq\frac{133}{900}
\]

\(A\) and \(B\) are not independent.

## Worked Example 9: Testing independence from a two-set Venn diagram

Regions:

\[
A\text{ only}=6,
\quad A\cap B=4,
\quad B\text{ only}=5,
\quad \text{outside}=0
\]

Total:

\[
6+4+5+0=15
\]

\[
P(A)=\frac{6+4}{15}=\frac{10}{15}=\frac23
\]

\[
P(B)=\frac{4+5}{15}=\frac{9}{15}=\frac35
\]

\[
P(A\cap B)=\frac{4}{15}
\]

\[
P(A)P(B)=\frac23\times\frac35=\frac{6}{15}
\]

Since:

\[
\frac{4}{15}\neq\frac{6}{15}
\]

\(A\) and \(B\) are not independent.

## Worked Example 10: Unknown probabilities and independence

A Venn diagram has:

\[
A\text{ only}=0.3,
\quad A\cap B=x,
\quad B\text{ only}=0.2,
\quad \text{outside}=y
\]

Given \(A\) and \(B\) are independent:

\[
P(A)=0.3+x
\]

\[
P(B)=0.2+x
\]

\[
P(A\cap B)=x
\]

Independence gives:

\[
x=(0.3+x)(0.2+x)
\]

Expand:

\[
x=0.06+0.3x+0.2x+x^2
\]

\[
x=0.06+0.5x+x^2
\]

Move all terms to one side:

\[
0=x^2+0.5x-x+0.06
\]

\[
0=x^2-0.5x+0.06
\]

\[
x^2-0.5x+0.06=0
\]

Factorise:

\[
(x-0.2)(x-0.3)=0
\]

So:

\[
x=0.2 \quad \text{or} \quad x=0.3
\]

All regions add to 1:

\[
0.3+x+0.2+y=1
\]

\[
y=0.5-x
\]

If \(x=0.2\), then \(y=0.3\). If \(x=0.3\), then \(y=0.2\).

## Worked Example 11: Tree diagram with counters, without replacement

There are \(3\) yellow counters and \(2\) green counters in a bag. Two counters are taken at random without replacement.

Total counters:

\[
3+2=5
\]

\[
P(Y)=\frac35,\qquad P(G)=\frac25
\]

If first is yellow:

\[
P(Y\text{ second after }Y\text{ first})=\frac24
\]

\[
P(G\text{ second after }Y\text{ first})=\frac24
\]

If first is green:

\[
P(Y\text{ second after }G\text{ first})=\frac34
\]

\[
P(G\text{ second after }G\text{ first})=\frac14
\]

Same colour:

\[
P(YY)=\frac35\times\frac24=\frac{6}{20}
\]

\[
P(GG)=\frac25\times\frac14=\frac{2}{20}
\]

\[
P(\text{same})=\frac{6}{20}+\frac{2}{20}=\frac{8}{20}=\frac25
\]

Different colours:

\[
P(YG)=\frac35\times\frac24=\frac{6}{20}
\]

\[
P(GY)=\frac25\times\frac34=\frac{6}{20}
\]

\[
P(\text{different})=\frac{6}{20}+\frac{6}{20}=\frac{12}{20}=\frac35
\]

## Worked Example 12: Repeated attempts until first hit

The probability of hitting a target on each shot is:

\[
0.3
\]

The probability of missing is:

\[
1-0.3=0.7
\]

To hit the target on the fifth shot, the first four shots must be misses and the fifth must be a hit.

\[
P(\text{hit on fifth})=0.7\times0.7\times0.7\times0.7\times0.3
\]

\[
P(\text{hit on fifth})=0.7^4\times0.3
\]

\[
P(\text{hit on fifth})=0.07203
\]

## Worked Example 13: Two-way table, CCEA-spec supplement

A survey of \(80\) students records whether they study Mathematics and Physics.

\[
42 \text{ study Mathematics},\quad 30 \text{ study Physics},\quad 18 \text{ study both}
\]

Let \(M\) = studies Mathematics and \(P\) = studies Physics.

Both:

\[
M\cap P=18
\]

Mathematics but not Physics:

\[
42-18=24
\]

Physics but not Mathematics:

\[
30-18=12
\]

Neither:

\[
80-(18+24+12)=26
\]

\[
\begin{array}{c|ccc}
 & P & P' & \text{Total}\\
\hline
M & 18 & 24 & 42\\
M' & 12 & 26 & 38\\
\hline
\text{Total} & 30 & 50 & 80
\end{array}
\]

\[
P(M)=\frac{42}{80}=\frac{21}{40}
\]

\[
P(P)=\frac{30}{80}=\frac38
\]

\[
P(M\cap P)=\frac{18}{80}=\frac{9}{40}
\]

Test independence:

\[
P(M)P(P)=\frac{21}{40}\times\frac38=\frac{63}{320}
\]

\[
P(M\cap P)=\frac{9}{40}=\frac{72}{320}
\]

Since:

\[
\frac{72}{320}\neq\frac{63}{320}
\]

\(M\) and \(P\) are not independent.

---

## Guided Practice

1. Two fair dice are thrown. Find the probability that the sum of the two dice is more than \(6\).
2. Given \(P(A)=0.55\) and \(P(A\cup B)=0.8\), find \(P(A'\cap B)\) and \(P(\text{neither }A\text{ nor }B)\).
3. Events \(A\) and \(B\) are mutually exclusive. \(P(A)=0.35\), \(P(B)=0.25\). Find \(P(A\cup B)\), \(P(A\cap B)\), and \(P(\text{neither})\).
4. A number is chosen at random from \(\{1,2,3,4,5,6\}\). Let \(A\) be choosing an even number and \(B\) be choosing a multiple of \(3\). Determine whether \(A\) and \(B\) are independent.
5. In a group of \(100\) students, \(58\) study Art, \(46\) Biology, \(40\) Chemistry, \(25\) Art and Biology, \(20\) Art and Chemistry, \(15\) Biology and Chemistry, and \(8\) all three. Find the probability that a randomly selected student studies none, studies Biology but not Art, and studies at least two.
6. A bag contains \(4\) red counters and \(3\) blue counters. Two counters are taken without replacement. Find the probability that both are red and that the colours are different.
7. The probability that a machine produces a faulty item is \(0.04\). Items are produced independently. Find the probability that the first faulty item is the fourth item produced.
8. A survey of \(60\) students records whether they walk to school and whether they bring lunch. \(28\) walk, \(35\) bring lunch and \(18\) do both. Complete a two-way table and determine whether the events are independent.

---

## Common Mistakes and Exam Traps

1. **Forgetting the sample-space box around a Venn diagram.** Without the box, the “neither” region has nowhere to go.
2. **Putting totals directly into overlap regions.** Pairwise totals include the all-three centre unless the question says “only”.
3. **Mixing up “at least two” and “exactly two”.** At least two includes all three.
4. **Treating mutually exclusive and independent as the same idea.** Mutually exclusive means \(P(A\cap B)=0\); independent means \(P(A\cap B)=P(A)P(B)\).
5. **Thinking independence can be seen from the Venn diagram shape.** It must be tested with probabilities.
6. **Forgetting to add separate tree paths.** For different colours, \(YG\) and \(GY\) are different paths and both must be included.
7. **Using replacement probabilities when there is no replacement.** Without replacement, the denominator changes.
8. **Introducing conditional probability notation in AS2.** The formula \(P(A\mid B)=\frac{P(A\cap B)}{P(B)}\) is not required in AS2.

---

## Exam Technique Notes

- Draw the representation early: table, Venn diagram, tree diagram or two-way table.
- Label events before calculating.
- Use exact fractions where possible.
- For independence, write the comparison explicitly:

\[
P(A\cap B) \quad \text{versus} \quad P(A)P(B)
\]

- For mutually exclusive events, state why the overlap is zero.
- For three-set Venn diagrams, work centre-outwards.

---

## Full Worked Solutions to Guided Practice

### Solution 1

Two dice give \(36\) equally likely outcomes. Sums greater than \(6\) are \(7,8,9,10,11,12\), with counts \(6,5,4,3,2,1\).

\[
6+5+4+3+2+1=21
\]

\[
P(\text{sum}>6)=\frac{21}{36}=\frac{7}{12}
\]

### Solution 2

\[
P(A'\cap B)=P(A\cup B)-P(A)=0.8-0.55=0.25
\]

\[
P(\text{neither})=1-P(A\cup B)=1-0.8=0.2
\]

### Solution 3

Mutually exclusive means:

\[
P(A\cap B)=0
\]

\[
P(A\cup B)=0.35+0.25=0.60
\]

\[
P(\text{neither})=1-0.60=0.40
\]

### Solution 4

\[
A=\{2,4,6\},\qquad B=\{3,6\}
\]

\[
P(A)=\frac36=\frac12
\]

\[
P(B)=\frac26=\frac13
\]

\[
A\cap B=\{6\}
\]

\[
P(A\cap B)=\frac16
\]

\[
P(A)P(B)=\frac12\times\frac13=\frac16
\]

Therefore \(A\) and \(B\) are independent.

### Solution 5

Centre:

\[
8
\]

Pairwise-only:

\[
25-8=17,\qquad 20-8=12,\qquad 15-8=7
\]

Single-only:

\[
58-(17+12+8)=21
\]

\[
46-(17+7+8)=14
\]

\[
40-(12+7+8)=13
\]

Inside total:

\[
21+14+13+17+12+7+8=92
\]

Outside:

\[
100-92=8
\]

\[
P(\text{none})=\frac{8}{100}=0.08
\]

Biology but not Art:

\[
\frac{14+7}{100}=0.21
\]

At least two:

\[
\frac{17+12+7+8}{100}=0.44
\]

### Solution 6

\[
P(RR)=\frac47\times\frac36=\frac{12}{42}=\frac27
\]

Different colours:

\[
P(RB)=\frac47\times\frac36=\frac{12}{42}
\]

\[
P(BR)=\frac37\times\frac46=\frac{12}{42}
\]

\[
P(\text{different})=\frac{24}{42}=\frac47
\]

### Solution 7

\[
P(\text{not faulty})=1-0.04=0.96
\]

\[
P(\text{first faulty is fourth})=0.96^3\times0.04=0.03538944
\]

### Solution 8

Both:

\[
W\cap L=18
\]

Walks but no lunch:

\[
28-18=10
\]

Lunch but does not walk:

\[
35-18=17
\]

Neither:

\[
60-(18+10+17)=15
\]

\[
\begin{array}{c|ccc}
 & L & L' & \text{Total}\\
\hline
W & 18 & 10 & 28\\
W' & 17 & 15 & 32\\
\hline
\text{Total} & 35 & 25 & 60
\end{array}
\]

\[
P(W)=\frac{28}{60}=\frac{7}{15}
\]

\[
P(L)=\frac{35}{60}=\frac{7}{12}
\]

\[
P(W\cap L)=\frac{18}{60}=\frac{3}{10}
\]

\[
P(W)P(L)=\frac{7}{15}\times\frac{7}{12}=\frac{49}{180}
\]

\[
P(W\cap L)=\frac{3}{10}=\frac{54}{180}
\]

Since:

\[
\frac{54}{180}\neq\frac{49}{180}
\]

\(W\) and \(L\) are not independent.

---

## Common CCEA-Style Wording

| Wording | What it usually wants |
|---|---|
| “mutually exclusive” | State or use \(P(A\cap B)=0\). |
| “exhaustive” | State or use \(P(A\cup B)=1\). |
| “independent” | Compare \(P(A\cap B)\) with \(P(A)P(B)\). |
| “at least one” | Consider using \(1-P(\text{none})\). |
| “at least two” | Include exactly two and all three. |
| “neither \(A\) nor \(B\)” | Use \(1-P(A\cup B)\). |
| “\(A\) but not \(B\)” | Use \(A\cap B'\). |
| “or” | Usually means union, including overlap. |
| “two counters without replacement” | Denominators reduce after the first draw. |

---

## Syllabus Gap Check

| LO ID | Status | Evidence and lesson coverage |
|---|---|---|
| AS2-PROB-LO001 | Covered | Addition law, multiplication law, complement rule, Venn examples, tree examples and independence products. |
| AS2-PROB-LO002 | Covered | Mutually exclusive events, exhaustive events, dependence and independence are defined and used. |
| AS2-PROB-LO003 | Covered | Combined probabilities using Venn diagrams, tree diagrams and two-way tables. |

### Off-spec or excluded from core

| Item | Decision | Reason |
|---|---|---|
| Conditional probability formula | Excluded from core | CCEA AS2 says conditional probability is not required. |
| “Given that Jason runs” part of exercise survey | Excluded from core | This is conditional probability. |
| Binomial distribution calculations | Excluded from this lesson | Belongs to AS2 Statistical Distributions. |
| A2 probability modelling assumptions | Excluded from this lesson | Belongs to A22 Probability. |
| Pearson textbook exercise pages | Not reproduced | The pages are referenced but not supplied. |

---

## Visual and Interactive Asset Plan

| Asset ID | File | Purpose |
|---|---|---|
| AS2ProbabilityMermaid-001 | `mermaid/AS2ProbabilityMermaid-001.md` | Representation-choice flowchart. |
| AS2ProbabilityMermaid-002 | `mermaid/AS2ProbabilityMermaid-002.md` | Independence test flowchart. |
| AS2ProbabilityMermaid-003 | `mermaid/AS2ProbabilityMermaid-003.md` | Three-set Venn method flowchart. |
| AS2ProbabilityMermaid-004 | `mermaid/AS2ProbabilityMermaid-004.md` | Tree diagram calculation workflow. |
| AS2ProbabilitySVG-001 to 008 | `svg/` | Venn, table, tree and probability law diagrams. |
| AS2ProbabilityTikZ-001 to 003 | `tikz/` | Print-friendly Venn, tree and two-way-table diagrams. |
| AS2ProbabilityWidget-001 | `widgets/AS2ProbabilityWidget-001.html` | Venn region selector. |
| AS2ProbabilityWidget-002 | `widgets/AS2ProbabilityWidget-002.html` | Tree path multiplier. |

---

## Supplementary Sources Used

| Source | Status |
|---|---|
| CCEA GCE Mathematics Specification Map | Core authority for topic identity, LO IDs and boundaries. |
| Project README Module Map | Core project structure source. |
| Project Evidence Drop Checklist | Core evidence-control source. |
| DrFrost/Pearson Applied Year 1 probability PDF | Lesson evidence, used where it matches CCEA AS2 Probability. |
| DrFrost Applied Year 1 probability transcript | Lesson evidence, used for explanations and method commentary. |
| Screenshot PDF | Visual support only; parsed text unavailable. |
| Cross-board or third-party web sources | Not used. |
| GCSE sources | Not used. |

---

## Final Student Checklist

### Definitions

- [ ] I can define an experiment.
- [ ] I can define an outcome.
- [ ] I can define an event.
- [ ] I can define a sample space.
- [ ] I know what \(A'\), \(A\cap B\) and \(A\cup B\) mean.
- [ ] I know that probabilities across a full sample space add to \(1\).

### Probability laws

- [ ] I can use \(P(A')=1-P(A)\).
- [ ] I can use \(P(A\cup B)=P(A)+P(B)-P(A\cap B)\).
- [ ] I know that mutually exclusive events have \(P(A\cap B)=0\).
- [ ] I know that exhaustive events have \(P(A\cup B)=1\).
- [ ] I can test independence using \(P(A\cap B)=P(A)P(B)\).

### Diagrams and tables

- [ ] I can use a sample-space table for two simple experiments.
- [ ] I can fill a two-set Venn diagram.
- [ ] I can fill a three-set Venn diagram from the centre outwards.
- [ ] I can use a tree diagram by multiplying along paths.
- [ ] I can add separate successful paths.
- [ ] I can complete and use a two-way table.

### Exam readiness

- [ ] I include the outside box on Venn diagrams.
- [ ] I do not confuse “exactly two” with “at least two”.
- [ ] I do not confuse mutually exclusive with independent.
- [ ] I state a clear conclusion when testing independence.
- [ ] I watch for “without replacement” in tree diagrams.
- [ ] I avoid using conditional probability formulae in AS2 unless explicitly told the question is A2.
