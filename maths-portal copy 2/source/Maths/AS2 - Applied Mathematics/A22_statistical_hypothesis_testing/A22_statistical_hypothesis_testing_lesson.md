# A22 Statistical Hypothesis Testing: Binomial Hypothesis Testing 🎲

## Title and Metadata

| Field | Value |
|---|---|
| Course | CCEA GCE Mathematics |
| Unit code | `A22` |
| Unit name | A2 2 Applied Mathematics |
| Applied section | Statistics |
| Topic code | `A22-HT` |
| Topic name | Statistical hypothesis testing |
| Lesson focus | Binomial hypothesis testing |
| Topic slug | `statistical_hypothesis_testing` |
| Topic Pascal | `StatisticalHypothesisTesting` |
| Topic ID | `A22StatisticalHypothesisTesting` |
| Lesson file | `A22_statistical_hypothesis_testing_lesson.md` |
| Core LO IDs | `A22-HT-LO001`, `A22-HT-LO002`, `A22-HT-LO003` |
| Related prerequisite LO IDs | `AS2-DIST-LO001`, `AS2-DIST-LO002`, `AS2-DIST-LO003` |

---

## Evidence Map

| Evidence source | Used for |
|---|---|
| CCEA GCE Mathematics Specification Map | Unit, topic and LO identity; official syllabus boundary |
| Project README module map | File naming, metadata conventions and phase structure |
| Project Evidence Drop Checklist | Missing evidence, off-spec and visual placeholder discipline |
| Chapter 7 Hypothesis Testing, Binomial transcript | Main mathematical explanations, worked examples, warnings and test structure |
| Chapter 7 screenshots PDF | Visual support for chapter map, prize-game introduction and binomial distribution graph |

---

## Specification Alignment

### `A22-HT-LO001`

This lesson teaches the language of hypothesis testing:

\[
H_0,\quad H_1,\quad \text{significance level},\quad \text{test statistic},\quad \text{one-tailed test},\quad \text{two-tailed test},
\]
\[
\text{critical value},\quad \text{critical region},\quad \text{acceptance region},\quad \text{p-value}.
\]

### `A22-HT-LO002`

This lesson repeatedly uses the idea that a **sample result** is used to make an inference about a **population probability**. The significance level is treated as the probability threshold for rejecting \(H_0\):

\[
\text{small probability under }H_0 \quad \Rightarrow \quad \text{evidence against }H_0.
\]

### `A22-HT-LO003`

The main focus is binomial proportion testing:

\[
X\sim B(n,p).
\]

---

## Learning Objectives

By the end of this lesson, you should be able to:

1. Explain what a hypothesis test is trying to decide.
2. Write suitable null and alternative hypotheses for a binomial proportion.
3. Define a binomial test statistic.
4. Decide whether a test is one-tailed or two-tailed.
5. Calculate a p-value using binomial probabilities.
6. Compare a p-value with a significance level.
7. Find critical values and critical regions.
8. State an actual significance level.
9. Write a contextual conclusion that earns the final mark.

---

## Prerequisite Recap, A-Level Only

A binomial random variable has the form:

\[
X\sim B(n,p)
\]

where \(X\) is the number of successes, \(n\) is the number of trials, and \(p\) is the probability of success on each trial.

For example, if a game is played \(50\) times and the claimed probability of winning is \(0.2\), then:

\[
X\sim B(50,0.2).
\]

The expected number of successes is:

\[
np=50(0.2)=10.
\]

Expected does not mean guaranteed.

---

## Big Picture Explanation

Hypothesis testing asks:

> Could this sample result reasonably have happened by chance, assuming the original claim is true?

If a game apparently gives a prize \(20\%\) of the time and you play it \(50\) times, you expect:

\[
20\%\text{ of }50=0.2(50)=10.
\]

But seeing exactly \(10\) wins is not guaranteed. The probability of exactly \(10\) wins under \(X\sim B(50,0.2)\) is:

\[
P(X=10)=0.1398.
\]

A broader range around the expected value is much more likely:

\[
P(7\leq X\leq 13)=0.7860.
\]

The useful question is not “Did I get exactly what I expected?” but “Is my result so unusual that I should doubt the original claim?”

---

## Key Definitions and Notation

### Null hypothesis

The **null hypothesis** is the assumption we begin with. It is written with a colon:

\[
H_0:p=0.2.
\]

Do not write \(H_0=0.2\).

### Alternative hypothesis

The **alternative hypothesis** is what we suspect might be true instead:

\[
H_1:p<0.2,\qquad H_1:p>0.2,\qquad H_1:p\ne 0.2.
\]

| Alternative hypothesis | Type of test | Meaning |
|---|---|---|
| \(H_1:p<k\) | One-tailed | The probability may have decreased |
| \(H_1:p>k\) | One-tailed | The probability may have increased |
| \(H_1:p\ne k\) | Two-tailed | The probability may have changed either way |

### Test statistic

For a binomial hypothesis test:

\[
\boxed{\text{The test statistic is the count of successes.}}
\]

Example:

\[
X=\text{the number of people in the sample who support the candidate}.
\]

### Significance level

The **significance level** is the probability threshold used to decide whether an observed result is unusually rare.

\[
5\%=0.05,\qquad 1\%=0.01,\qquad 10\%=0.10.
\]

### P-value

The **p-value** is the probability, assuming \(H_0\) is true, of getting the observed result or something more extreme in the direction of \(H_1\).

Lower tail:

\[
P(X\leq x).
\]

Upper tail:

\[
P(X\geq x)=1-P(X\leq x-1).
\]

### Critical region and critical value

The **critical region** is the set of values that would make us reject \(H_0\). The **critical value** is the boundary value of that region.

If:

\[
X\leq 3,
\]

then \(3\) is the critical value.

### Acceptance region

The **acceptance region** is the set of values that do not lead to rejection of \(H_0\). Use careful wording:

\[
\boxed{\text{There is not enough evidence to reject }H_0.}
\]

Do not say \(H_0\) is proved true.

---

## Core Theory

## 1. Observed data and suspicion

Suppose a game claims:

\[
p=0.2.
\]

You play \(50\) times and only win \(5\) prizes:

\[
X=5.
\]

Since the expected number is:

\[
50(0.2)=10,
\]

\(5\) wins is low. There are two possible explanations:

1. The game is not rigged and the result was just unlucky.
2. The true probability of winning is less than \(0.2\).

Mathematically:

\[
H_0:p=0.2
\]

\[
H_1:p<0.2.
\]

Assuming \(H_0\):

\[
X\sim B(50,0.2).
\]

Calculate:

\[
P(X\leq 5)=0.0480.
\]

At the \(5\%\) level:

\[
0.0480<0.05.
\]

So reject \(H_0\). There is evidence that the probability of winning is less than \(20\%\).

---

## 2. Full p-value method

1. Define the test statistic: \(X=\text{number of successes}\).
2. Write hypotheses:

\[
H_0:p=k
\]

and one of:

\[
H_1:p<k,\qquad H_1:p>k,\qquad H_1:p\ne k.
\]

3. Assuming \(H_0\), write:

\[
X\sim B(n,k).
\]

4. Calculate the relevant tail probability.
5. Compare with the significance level.
6. Conclude in context.

---

## 3. Choosing the direction

| Question wording | Alternative hypothesis | Tail probability |
|---|---|---|
| lower, fewer, decreased, overestimating | \(H_1:p<k\) | \(P(X\leq x)\) |
| higher, more, increased, improvement | \(H_1:p>k\) | \(P(X\geq x)\) |
| different, changed, not equal | \(H_1:p\ne k\) | two-tailed, split significance level |

For a two-tailed \(5\%\) test:

\[
\frac{0.05}{2}=0.025.
\]

For a two-tailed \(10\%\) test:

\[
\frac{0.10}{2}=0.05.
\]

---

## 4. Critical regions

Suppose:

\[
X\sim B(40,0.2).
\]

The expected number of successes is:

\[
np=40(0.2)=8.
\]

### Lower-tail critical region at \(5\%\)

We want:

\[
P(X\leq a)<0.05.
\]

From cumulative probabilities:

\[
P(X\leq 3)=0.0285.
\]

So the critical region is:

\[
\boxed{X\leq 3.}
\]

The critical value is \(3\), and the actual significance level is \(0.0285\).

### Upper-tail critical region at \(5\%\)

We want:

\[
P(X\geq b)<0.05.
\]

Using:

\[
P(X\leq 12)=0.9568,
\]

we get:

\[
P(X\geq 13)=1-P(X\leq 12)=1-0.9568=0.0432.
\]

So the critical region is:

\[
\boxed{X\geq 13.}
\]

The critical value is \(13\), and the actual significance level is \(0.0432\).

---

## 5. Two-tailed critical regions

For a two-tailed test at the \(5\%\) level, split the significance level:

\[
0.05\div 2=0.025.
\]

Suppose:

\[
X\sim B(20,0.4).
\]

The expected value is:

\[
np=20(0.4)=8.
\]

Lower tail:

\[
P(X\leq 3)=0.0160<0.025.
\]

Upper tail:

\[
P(X\geq 13)=0.0210<0.025.
\]

So the critical region is:

\[
\boxed{X\leq 3\quad \text{or}\quad X\geq 13.}
\]

The actual significance level is:

\[
0.0160+0.0210=0.0370.
\]

---

## Visual Asset Integration

[VISUAL PLACEHOLDER: A22StatisticalHypothesisTestingSVG-001 | Source: screenshots PDF pages 1 and 5 plus transcript chapter overview | Insert from svg/A22StatisticalHypothesisTestingSVG-001.svg | Purpose: Show where hypothesis testing sits after probability and statistical distributions.]

[VISUAL PLACEHOLDER: A22StatisticalHypothesisTestingSVG-002 | Source: screenshots PDF pages 2 to 18 and transcript prize-game example | Insert from svg/A22StatisticalHypothesisTestingSVG-002.svg | Purpose: Show the claimed \(20\%\) prize game, expected wins and observed low outcome.]

[VISUAL PLACEHOLDER: A22StatisticalHypothesisTestingSVG-003 | Source: screenshots PDF pages 19 to 20 and transcript \(X\sim B(50,0.2)\) discussion | Insert from svg/A22StatisticalHypothesisTestingSVG-003.svg | Purpose: Show a binomial distribution centred near \(10\), with ordinary and suspicious regions shaded.]

[VISUAL PLACEHOLDER: A22StatisticalHypothesisTestingSVG-004 | Source: transcript critical-region section | Insert from svg/A22StatisticalHypothesisTestingSVG-004.svg | Purpose: Show one-tailed critical regions for \(X\sim B(40,0.2)\).]

[VISUAL PLACEHOLDER: A22StatisticalHypothesisTestingSVG-005 | Source: transcript two-tailed section | Insert from svg/A22StatisticalHypothesisTestingSVG-005.svg | Purpose: Show two-tailed critical regions for \(X\sim B(20,0.4)\).]

[VISUAL PLACEHOLDER: A22StatisticalHypothesisTestingMermaid-001 | Source: transcript decision process | Insert from mermaid/A22StatisticalHypothesisTestingMermaid-001.md | Purpose: Flowchart for deciding \(H_1:p<k\), \(H_1:p>k\), or \(H_1:p\ne k\).]

[INTERACTIVE PLACEHOLDER: A22StatisticalHypothesisTestingWidget-001 | Source: transcript binomial tail calculations | Insert from widgets/A22StatisticalHypothesisTestingWidget-001.html | Purpose: Let the student change \(n\), \(p\), observed \(x\), tail direction and significance level to see the decision change.]

---

## Worked Examples

## Worked Example 1: Prize game, lower-tailed p-value test

A game apparently gives out a prize \(20\%\) of the time. A player plays the game \(50\) times and wins \(5\) prizes. Test at the \(5\%\) significance level whether the probability of winning is less than \(20\%\).

Let:

\[
X=\text{the number of prizes won in }50\text{ plays}.
\]

Hypotheses:

\[
H_0:p=0.2
\]

\[
H_1:p<0.2
\]

Assuming \(H_0\):

\[
X\sim B(50,0.2).
\]

Observed:

\[
X=5.
\]

Since this is lower-tailed:

\[
P(X\leq 5)=0.0480.
\]

Compare:

\[
0.0480<0.05.
\]

Reject \(H_0\). There is evidence that the probability of winning a prize is less than \(20\%\).

---

## Worked Example 2: Election support

An election candidate believes she has the support of \(40\%\) of residents. A researcher tests whether she is overestimating her support. The researcher asks \(20\) people; \(3\) support the candidate.

Let:

\[
X=\text{the number of people in the sample who support the candidate}.
\]

Hypotheses:

\[
H_0:p=0.4
\]

\[
H_1:p<0.4.
\]

Assuming \(H_0\):

\[
X\sim B(20,0.4).
\]

Calculate:

\[
P(X\leq 3)=0.0160.
\]

Since:

\[
0.0160<0.05,
\]

reject \(H_0\). There is evidence that the candidate has overestimated her support.

---

## Worked Example 3: Lateness at school

In the UK, \(5\%\) of students turn up late to school each day. A teacher observes \(40\) students and \(6\) are late. Test at the \(10\%\) level whether the school has a problem with lateness.

Let:

\[
X=\text{the number of late students among the }40\text{ observed}.
\]

Hypotheses:

\[
H_0:p=0.05
\]

\[
H_1:p>0.05.
\]

Assuming \(H_0\):

\[
X\sim B(40,0.05).
\]

Use the upper tail:

\[
P(X\geq 6)=1-P(X\leq 5)=0.0139.
\]

Compare with \(0.10\):

\[
0.0139<0.10.
\]

Reject \(H_0\). There is evidence that the school has a problem with lateness.

---

## Worked Example 4: Critical region, lower tail

Let:

\[
X\sim B(40,0.2).
\]

Test whether \(p<0.2\) at the \(5\%\) level.

Find \(a\) such that:

\[
P(X\leq a)<0.05.
\]

Using cumulative probabilities:

\[
P(X\leq 3)=0.0285.
\]

So:

\[
\boxed{X\leq 3}
\]

is the critical region.

---

## Worked Example 5: Critical region, upper tail

Let:

\[
X\sim B(40,0.2).
\]

Test whether \(p>0.2\) at the \(5\%\) level.

Using:

\[
P(X\leq 12)=0.9568,
\]

\[
P(X\geq 13)=1-0.9568=0.0432.
\]

So:

\[
\boxed{X\geq 13}
\]

is the critical region.

---

## Worked Example 6: Coin bias

John tosses a coin \(8\) times and gets \(6\) heads. He claims the coin is biased towards heads. Test at the \(5\%\) level.

Let:

\[
X=\text{the number of heads in }8\text{ tosses}.
\]

\[
H_0:p=0.5
\]

\[
H_1:p>0.5.
\]

Assuming \(H_0\):

\[
X\sim B(8,0.5).
\]

Calculate:

\[
P(X\geq 6)=0.1445.
\]

Since:

\[
0.1445>0.05,
\]

there is not enough evidence to reject \(H_0\). There is not enough evidence to support John’s claim.

---

## Worked Example 7: New drug

A standard treatment has success rate \(\frac25=0.4\). A new drug succeeds with \(11\) out of \(20\) patients. Test at \(5\%\) whether the new drug is an improvement.

Let:

\[
X=\text{the number of successfully treated patients out of }20.
\]

\[
H_0:p=0.4
\]

\[
H_1:p>0.4.
\]

Assuming \(H_0\):

\[
X\sim B(20,0.4).
\]

\[
P(X\geq 11)=1-P(X\leq 10)=0.1275.
\]

Since:

\[
0.1275>0.05,
\]

there is not enough evidence to reject \(H_0\). The doctor’s claim is not supported at the \(5\%\) level.

---

## Worked Example 8: Two-tailed restaurant test

The ratio of non-vegetarian to vegetarian meals is \(2:1\), so:

\[
p=\frac13.
\]

In a sample of \(10\), only \(1\) person orders vegetarian. Test at \(5\%\) whether the proportion is different.

Let:

\[
X=\text{the number of vegetarian meals in the sample of }10.
\]

\[
H_0:p=\frac13
\]

\[
H_1:p\ne \frac13.
\]

Assuming \(H_0\):

\[
X\sim B\left(10,\frac13\right).
\]

Expected:

\[
np=10\left(\frac13\right)=\frac{10}{3}=3.333\ldots
\]

Observed \(X=1\) is low, so:

\[
P(X\leq 1)=0.1040.
\]

For a two-tailed \(5\%\) test, compare with:

\[
\frac{0.05}{2}=0.025.
\]

Since:

\[
0.1040>0.025,
\]

there is not enough evidence to reject \(H_0\). There is not enough evidence that the vegetarian proportion is different.

---

## Worked Example 9: Two-tailed shiny-card test

A company claims \(8\%\) of packs contain a shiny. Jack buys \(50\) packs and only \(1\) contains a shiny. Test at \(10\%\) whether the claim is supported.

Let:

\[
X=\text{the number of packs containing a shiny}.
\]

\[
H_0:p=0.08
\]

\[
H_1:p\ne 0.08.
\]

Assuming \(H_0\):

\[
X\sim B(50,0.08).
\]

Expected:

\[
np=50(0.08)=4.
\]

Observed \(X=1\) is low, so:

\[
P(X\leq 1)=0.0827.
\]

For a two-tailed \(10\%\) test, compare with:

\[
\frac{0.10}{2}=0.05.
\]

Since:

\[
0.0827>0.05,
\]

there is not enough evidence to reject \(H_0\). The company’s claim is supported at the \(10\%\) significance level.

Evidence note: the transcript appears to say \(0.827\), but the binomial calculation for \(P(X\leq 1)\), where \(X\sim B(50,0.08)\), is \(0.0827\). This lesson uses the mathematically correct value.

---

## Guided Practice

### Question 1

A game claims that the probability of winning is \(0.3\). A player plays \(20\) times and wins \(3\) times. Test at the \(5\%\) significance level whether the probability of winning is less than \(0.3\).

### Question 2

A school claims that \(15\%\) of students cycle to school. A sample of \(40\) students is taken and \(11\) cycle to school. Test at the \(5\%\) significance level whether the true proportion is greater than \(15\%\).

### Question 3

A coin is tossed \(10\) times. It lands heads \(9\) times. Find the critical region at the \(5\%\) level for testing whether the coin is biased towards heads.

### Question 4

Let:

\[
X\sim B(20,0.2).
\]

Find the upper-tail critical region at the \(5\%\) significance level.

### Question 5

A company claims that \(25\%\) of customers choose a premium plan. A researcher believes the proportion is different from \(25\%\). In a sample of \(30\), only \(3\) choose the premium plan. Test at the \(10\%\) significance level.

### Question 6

For:

\[
X\sim B(20,0.4),
\]

a two-tailed \(5\%\) critical region is:

\[
X\leq 3\quad \text{or}\quad X\geq 13.
\]

Find the actual significance level.

---

## Common Mistakes and Exam Traps

1. Writing \(H_0=0.4\) instead of \(H_0:p=0.4\).
2. Choosing the wrong tail.
3. Calculating \(P(X=x)\) instead of \(P(X\leq x)\) or \(P(X\geq x)\).
4. Forgetting to halve the significance level in a two-tailed test.
5. Saying “accept \(H_0\)” too strongly.
6. Giving no contextual conclusion.

---

## Exam Technique Notes

Use this template:

\[
\begin{aligned}
&\text{Let }X=\text{number of successes.}\\
&H_0:p=k\\
&H_1:p<k\quad \text{or}\quad p>k\quad \text{or}\quad p\ne k\\
&\text{Assuming }H_0\text{ is true, }X\sim B(n,k).\\
&\text{Calculate the relevant tail probability.}\\
&\text{Compare with the significance level.}\\
&\text{Write a contextual conclusion.}
\end{aligned}
\]

For upper-tail probabilities:

\[
P(X\geq b)=1-P(X\leq b-1).
\]

---

## Full Worked Solutions to Guided Practice

## Solution 1

\[
H_0:p=0.3,\qquad H_1:p<0.3.
\]

Assuming \(H_0\):

\[
X\sim B(20,0.3).
\]

\[
P(X\leq 3)=0.1071.
\]

Since \(0.1071>0.05\), there is not enough evidence to reject \(H_0\). There is not enough evidence that the probability of winning is less than \(0.3\).

## Solution 2

\[
H_0:p=0.15,\qquad H_1:p>0.15.
\]

Assuming \(H_0\):

\[
X\sim B(40,0.15).
\]

\[
P(X\geq 11)=0.0433.
\]

Since \(0.0433<0.05\), reject \(H_0\). There is evidence that the true proportion cycling to school is greater than \(15\%\).

## Solution 3

For \(X\sim B(10,0.5)\):

\[
P(X\geq 9)=P(X=9)+P(X=10).
\]

\[
P(X=9)=\binom{10}{9}(0.5)^{10}=\frac{10}{1024}.
\]

\[
P(X=10)=\binom{10}{10}(0.5)^{10}=\frac{1}{1024}.
\]

\[
P(X\geq 9)=\frac{11}{1024}=0.0107<0.05.
\]

Critical region:

\[
\boxed{X\geq 9.}
\]

## Solution 4

For \(X\sim B(20,0.2)\):

\[
P(X\geq 8)=0.0321<0.05.
\]

Critical region:

\[
\boxed{X\geq 8.}
\]

Actual significance level:

\[
\boxed{0.0321.}
\]

## Solution 5

\[
H_0:p=0.25,\qquad H_1:p\ne 0.25.
\]

Assuming \(H_0\):

\[
X\sim B(30,0.25).
\]

Observed \(X=3\) is low. Calculate:

\[
P(X\leq 3)=0.1509.
\]

For a two-tailed \(10\%\) test, compare with \(0.05\). Since \(0.1509>0.05\), there is not enough evidence to reject \(H_0\).

## Solution 6

\[
\text{Actual significance level}=P(X\leq 3)+P(X\geq 13).
\]

\[
P(X\leq 3)=0.0160,\qquad P(X\geq 13)=0.0210.
\]

\[
0.0160+0.0210=0.0370.
\]

So the actual significance level is:

\[
\boxed{0.0370=3.70\%.}
\]

---

## Syllabus Gap Check

| LO ID | Status | Notes |
|---|---|---|
| `A22-HT-LO001` | Covered | Definitions and use of hypothesis testing language are included |
| `A22-HT-LO002` | Covered | Sample-to-population inference and significance level are explained |
| `A22-HT-LO003` | Covered | Binomial proportion tests are the core of the lesson |
| `A22-HT-LO004` | Not covered | Normal mean tests require separate evidence |
| `A22-HT-LO005` | Not covered | Correlation coefficient tests require separate evidence |

---

## Visual and Interactive Asset Plan

| Asset ID | Type | Purpose |
|---|---|---|
| `A22StatisticalHypothesisTestingSVG-001` | SVG | Chapter map showing hypothesis testing after probability and distributions |
| `A22StatisticalHypothesisTestingSVG-002` | SVG | Prize-game model: expected \(10\) wins vs observed \(5\) wins |
| `A22StatisticalHypothesisTestingSVG-003` | SVG | Binomial distribution \(X\sim B(50,0.2)\) with shaded tail |
| `A22StatisticalHypothesisTestingSVG-004` | SVG | One-tailed critical regions for \(X\sim B(40,0.2)\) |
| `A22StatisticalHypothesisTestingSVG-005` | SVG | Two-tailed critical regions for \(X\sim B(20,0.4)\) |
| `A22StatisticalHypothesisTestingMermaid-001` | Mermaid | Decision flowchart for choosing test direction |
| `A22StatisticalHypothesisTestingTikZ-001` | TikZ | Printable hypothesis-test structure diagram |
| `A22StatisticalHypothesisTestingTikZ-002` | TikZ | Printable prize-game structure diagram |
| `A22StatisticalHypothesisTestingTikZ-003` | TikZ | Printable one-tailed critical regions |
| `A22StatisticalHypothesisTestingTikZ-004` | TikZ | Printable two-tailed critical regions |
| `A22StatisticalHypothesisTestingWidget-001` | HTML widget | Binomial tail probability explorer |

---

## Supplementary Sources Used

No external or cross-board sources were used.

The transcript supplies teaching examples and explanations only. The CCEA specification map remains the authority for topic identity and syllabus boundaries.

---

## Final Student Checklist

- I can write \(H_0\) and \(H_1\) correctly using a colon.
- I can define \(X\) as the number of successes.
- I can state \(X\sim B(n,p)\) under \(H_0\).
- I can decide whether the test is lower-tailed, upper-tailed or two-tailed.
- I can calculate \(P(X\leq x)\) for a low observed value.
- I can calculate \(P(X\geq x)=1-P(X\leq x-1)\) for a high observed value.
- I can halve the significance level for a two-tailed test.
- I can find a critical region.
- I can state an actual significance level.
- I can write “there is not enough evidence to reject \(H_0\)” when the result is not significant.
- I can finish with a contextual conclusion, not just a symbol sentence.
