# 1. Lesson Title and Metadata

# FAS2 Statistical Distributions: Discrete Random Variables

| Field | Value |
|---|---|
| Date generated | 2026-06-04 |
| Course | CCEA GCE Further Mathematics |
| Unit code | `FAS2` |
| Unit title | Further AS 2 Applied Mathematics |
| Applied section | Section C: Statistics |
| Topic code | `FAS2-DIST` |
| Official topic area | Statistical distributions |
| Lesson topic name | Discrete Random Variables |
| Topic slug | `discrete_random_variables` |
| Topic Pascal | `DiscreteRandomVariables` |
| Topic ID | `FAS2DiscreteRandomVariables` |
| Lesson file name | `FAS2_discrete_random_variables_lesson.md` |
| Core LO IDs | `FAS2-DIST-LO002`, `FAS2-DIST-LO003`, `FAS2-DIST-LO006` |
| Related but excluded/deferred LO IDs | `FAS2-DIST-LO001`, `FAS2-DIST-LO004`, `FAS2-DIST-LO005`, `FAS2-DIST-LO007`, `FAS2-DIST-LO008` |
| Bridge tags | `#AS2Probability`, `#AS2DataPresentation`, `#AS2BinomialDistribution`, `#SummaryStatistics`, `#Coding` |
| Topic tags | `#FAS2`, `#DIST`, `#Statistics`, `#DiscreteRandomVariables`, `#ExpectedValue`, `#Variance`, `#StandardDeviation`, `#LinearCoding`, `#SectionC` |

---

# 2. Evidence Map

| Evidence source | Used in lesson | Notes |
|---|---|---|
| CCEA Further Mathematics Specification Map | Specification Alignment, Learning Objectives, Syllabus Gap Check | Highest authority for topic boundary and LO IDs. |
| Further Maths README Module Map | File structure, phase workflow, bridge map, visual placeholder rules | Project workflow authority. |
| Further Maths Evidence Drop Checklist | Evidence intake, missing evidence log, off-spec log, preservation checks | Project workflow authority. |
| Ordinary A-Level Maths Bridge Extracts | A-Level bridge table and prerequisite recap | Bridge context only. |
| Uploaded transcript: `transcripts.md` | Definitions, explanations, examples, warnings, calculations | Lesson-specific supporting evidence. |
| Uploaded PDF: `FS1-Chp1-DiscreteRandomVariables.pdf` | Slide structure, formula displays, quickfire questions, problem-solving structure | Lesson-specific supporting evidence, cross-board source. |
| Uploaded screenshot PDF: `Chapter_1_Discrete_Random_Variables_📊_(Further_Statistics_1)_screenshots.pdf` | Visual evidence for motivational games, table layouts, annotations | No parsed text. Only visible/readable previewed details used. |
| Edexcel/Pearson/DrFrost references inside uploaded evidence | Supporting examples and technique | Cross-board, not CCEA authority. |
| Pearson exercise references in slides | Exercise structure only | Full exercise pages not supplied, so not quoted. |

---

# 3. Specification Alignment

## Core CCEA Further Mathematics Alignment

| LO ID | Official wording | Lesson coverage | Evidence source | Syllabus boundary | Ordinary A-Level Maths bridge |
|---|---|---|---|---|---|
| `FAS2-DIST-LO002` | demonstrate understanding of and use discrete probability distributions, including probability functions, mean, variance and standard deviation | Defines discrete random variables, probability functions, distribution tables, `E(X)`, `E(X^2)`, `Var(X)`, standard deviation | CCEA spec map, uploaded transcript, FS1 PDF | Discrete probability distributions only in this lesson. Continuous distributions excluded. | AS2 probability, AS2 data presentation, frequency table mean and variance |
| `FAS2-DIST-LO003` | calculate probabilities such as \(P(a\leq X\leq b)\), \(E(X)\) and \(\operatorname{Var}(X)\) for simple cases of a discrete random variable \(X\) | Covers range probabilities, expected value, variance, unknown probabilities and table-based calculations | CCEA spec map, uploaded transcript, FS1 PDF | Simple discrete random variables with finite outcome tables | Probability laws, inequalities, summary statistics |
| `FAS2-DIST-LO006` | understand and use the expressions for \(E(aX+b)\) and \(\operatorname{Var}(aX+b)\), where \(X\) is a discrete or continuous random variable | Covers linear coding for discrete random variables: \(E(aX+b)=aE(X)+b\), \(\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)\) | CCEA spec map, transcript coding section, FS1 PDF coding section | This lesson covers discrete case only. Continuous case deferred. | Ordinary statistics coding for mean and variance |

## Related Outcomes Not Taught as Core Here

| LO ID | Why excluded or deferred |
|---|---|
| `FAS2-DIST-LO001` | Geometric distribution is a later distribution model and not part of this discrete random variable foundation lesson. |
| `FAS2-DIST-LO004` | Continuous probability distributions are not covered in this lesson. |
| `FAS2-DIST-LO005` | Continuous random variable calculations with probability density functions are not covered in this lesson. |
| `FAS2-DIST-LO007` | Poisson distribution is mentioned as coming next in the transcript, so it is excluded from this lesson. |
| `FAS2-DIST-LO008` | Mean and variance formulae for binomial, geometric and Poisson distributions are not taught here. Binomial is bridge context only. |

---

# 4. Learning Objectives

## Core Further Maths Objectives

By the end of this lesson, the student should be able to:

1. Explain what a discrete random variable is.
2. Distinguish between the random variable \(X\) and a particular outcome \(x\).
3. Read and construct a probability distribution table.
4. Use \(P(X=x)\) and shorthand notation such as \(p(5)\) correctly.
5. Use the condition
   \[
   \sum P(X=x)=1
   \]
   to find unknown probabilities.
6. Calculate probabilities such as
   \[
   P(a\leq X\leq b),\qquad P(X>c),\qquad P(r<X\leq s).
   \]
7. Calculate the expected value
   \[
   E(X)=\sum xP(X=x).
   \]
8. Interpret \(E(X)\) as the long-run mean outcome.
9. Calculate
   \[
   E(X^2)=\sum x^2P(X=x).
   \]
10. Calculate
    \[
    \operatorname{Var}(X)=E(X^2)-[E(X)]^2.
    \]
11. Calculate the standard deviation
    \[
    \sigma_X=\sqrt{\operatorname{Var}(X)}.
    \]
12. Use linear coding:
    \[
    E(aX+b)=aE(X)+b,
    \]
    \[
    \operatorname{Var}(aX+b)=a^2\operatorname{Var}(X).
    \]
13. Solve unknown-probability problems using simultaneous equations.
14. Solve probability questions involving a transformed random variable such as \(Y=aX+b\).

## Bridge Objectives

The student should connect this lesson to ordinary A-Level Mathematics by recognising that:

1. Expected value is the probability version of a frequency-table mean.
2. Variance uses the same idea as ordinary statistics:
   \[
   \text{mean of the squares} - \text{square of the mean}.
   \]
3. Probability laws from ordinary A-Level still apply.
4. Coding rules from ordinary statistics still apply for linear transformations.
5. Binomial distribution random variable notation is helpful, but this topic often gives the distribution table directly.

## Exam Technique Objectives

The student should learn to:

1. Write the probability total equation first when unknown probabilities appear.
2. Use the expected value equation as a second equation when \(E(X)\) is given.
3. Add an \(x^2\) row to the table when variance is required.
4. Avoid confusing \(E(X^2)\) with \([E(X)]^2\).
5. Use exact fractions where possible.
6. Keep cross-board practice labelled correctly and not mistake it for CCEA past-paper material.
7. Check that probabilities are between \(0\) and \(1\).
8. Check that probabilities add to \(1\).
9. Interpret final answers in context when the random variable represents money, points or dice scores.

---

# 5. Explicit Prerequisite Recap

## GCSE Foundations

Before this lesson, the student should be comfortable with probability as a number between \(0\) and \(1\), adding probabilities for mutually exclusive outcomes, calculating a mean from a frequency table, substituting numbers into formulae, solving simultaneous equations, using inequalities, squaring negative numbers correctly and taking square roots.

## Ordinary AS/A2 Mathematics Foundations

From ordinary CCEA A-Level Mathematics, the main bridge ideas are probability laws, binomial distribution notation and random variable notation, data tables and summary statistics, variance and standard deviation, coding of data, and interpreting probability statements.

## Previous Further Mathematics Foundations

No previous Further Statistics lesson is required, but the general Further Maths habits are needed: define symbols before use, preserve exact notation, show algebraic steps clearly, state what the random variable represents, and check boundary conditions such as \(\sum p=1\).

### A-Level Maths Bridge: What You Already Know and What Further Maths Changes

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| AS2 Probability | Probability totals, independent events, mutually exclusive events and probability notation | These ideas are placed into a full distribution table for a random variable \(X\) | Do not add probabilities for outcomes that do not satisfy the inequality. |
| AS2 Data Presentation and Interpretation | Frequency tables and calculating means using \(\sum fx/\sum f\) | Expected value is the same weighted mean idea, but probabilities replace frequencies | Probabilities add to \(1\), not to a sample size. |
| Ordinary variance and standard deviation | Variance measures spread around the mean | Variance becomes \(\operatorname{Var}(X)=E(X^2)-[E(X)]^2\) | \(E(X^2)\) is not the same as \([E(X)]^2\). |
| Ordinary statistics coding | Linear coding changes mean and variance predictably | \(E(aX+b)=aE(X)+b\), \(\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)\) | The coding rule only applies to linear codings. |
| AS2 Binomial Distribution | A random variable can have a distribution model | A custom discrete distribution can be given directly in a table | Do not force a named distribution if the table is already supplied. |

In ordinary A-Level Maths, this idea appeared as frequency tables, probability laws and summary statistics. You already learned that a mean can be calculated by multiplying each value by its frequency, adding, then dividing by the total frequency.

In Further Maths, the same idea becomes more abstract: instead of frequencies, the weights are probabilities. Because the total probability is \(1\), the expected value is simply the sum of each outcome multiplied by its probability.

The key upgrade is that \(X\) becomes a random variable, not just a data column. We are now describing the behaviour of a repeatable experiment before it happens.

The danger is treating every formula as a calculator ritual. A discrete random variable question is usually a table-reading question wearing a very formal coat.

---

# 6. Big Picture Explanation

A discrete random variable is a mathematical way of describing a random experiment whose possible outcomes are separate values.

For example, when a fair die is rolled, the score can be

\[
1,\ 2,\ 3,\ 4,\ 5,\ 6.
\]

It cannot be \(2.4\), \(3.71\) or \(5.999\). The possible values are separate, so the random variable is **discrete**.

The point of this lesson is not just to calculate probabilities. Ordinary probability already does that. The new idea is that we can find special properties of the whole distribution:

- its long-run average outcome, called the **expected value**;
- its spread around that average, measured by the **variance**;
- its standard deviation;
- how these change when the random variable is transformed.

A casino-style game gives the motivation. A game might feel exciting because it has a small chance of a huge win, but expected value tells us what happens on average over many repetitions. Variance then tells us whether the outcomes are usually close to the average or wildly spread out.

Two games can have the same expected value but feel completely different because one has much larger variance. Expected value tells you where the centre of the distribution is. Variance tells you how stormy the sea is around that centre.

For CCEA Further Mathematics, the core skill is to move cleanly between:

\[
\text{context}
\quad\longrightarrow\quad
\text{distribution table}
\quad\longrightarrow\quad
\text{probabilities, expectation, variance and interpretation}.
\]

---

# 7. Key Definitions and Notation

## Random Variable

A **random variable** is a variable whose value depends on the outcome of a random experiment or trial.

We usually use a capital letter such as

\[
X,\ Y,\ W
\]

for the random variable.

Example:

\[
X=\text{the score on the uppermost face when a die is rolled}.
\]

Here, \(X\) is not one number. It is the whole random experiment.

## Outcome

A lowercase letter such as \(x\) represents a specific possible value of the random variable.

If \(X\) is the score on a die, then possible values of \(x\) are

\[
1,\ 2,\ 3,\ 4,\ 5,\ 6.
\]

## Discrete Random Variable

A **discrete random variable** has separate possible outcomes.

For a fair die:

\[
X\in\{1,2,3,4,5,6\}.
\]

The values are countable and separate.

## Probability Function

The notation

\[
P(X=x)
\]

means:

\[
\text{the probability that the random variable }X\text{ takes the specific value }x.
\]

For a fair die:

\[
P(X=1)=P(X=2)=P(X=3)=P(X=4)=P(X=5)=P(X=6)=\frac16.
\]

Sometimes the shorthand

\[
p(5)
\]

may be used to mean

\[
P(X=5).
\]

The lowercase \(p\) is a shorthand probability function. The full notation \(P(X=5)\) is usually clearer in exam work.

## Probability Distribution Table

A probability distribution table lists all possible outcomes and their probabilities.

For a fair die:

\[
\begin{array}{c|cccccc}
x & 1 & 2 & 3 & 4 & 5 & 6\\
\hline
P(X=x) & \frac16 & \frac16 & \frac16 & \frac16 & \frac16 & \frac16
\end{array}
\]

## Probability Total Rule

For any discrete probability distribution,

\[
\sum P(X=x)=1.
\]

## Expected Value

The **expected value** of \(X\), written \(E(X)\), is the long-run mean outcome. For a discrete random variable,

\[
E(X)=\sum xP(X=x).
\]

## Expected Value of a Function of \(X\)

For a function \(g(X)\),

\[
E(g(X))=\sum g(x)P(X=x).
\]

In this lesson, the main required version is

\[
E(X^2)=\sum x^2P(X=x),
\]

because it is needed for variance.

## Variance

The variance of \(X\), written \(\operatorname{Var}(X)\), measures how spread out the outcomes are around the expected value.

For a discrete random variable,

\[
\operatorname{Var}(X)=E(X^2)-[E(X)]^2.
\]

## Standard Deviation

The standard deviation is the square root of the variance:

\[
\sigma_X=\sqrt{\operatorname{Var}(X)}.
\]

If the random variable is measured in pounds, points or metres, the standard deviation has the same unit as the original random variable. The variance has squared units.

## Linear Coding

For constants \(a\) and \(b\),

\[
E(aX+b)=aE(X)+b.
\]

For variance,

\[
\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X).
\]

The \(+b\) or \(-b\) part shifts every value by the same amount, so it changes the expected value but does not change the spread. The multiplying factor \(a\) stretches or compresses the distribution, so the variance is multiplied by \(a^2\).

---

# 8. Core Theory

## 8.1 Reading a Discrete Random Variable Table

A distribution table usually has two rows. The first row gives possible values \(x_1,x_2,x_3,\ldots,x_n\). The second row gives probabilities \(p_1,p_2,p_3,\ldots,p_n\).

\[
\begin{array}{c|ccccc}
x & x_1 & x_2 & x_3 & \cdots & x_n\\
\hline
P(X=x) & p_1 & p_2 & p_3 & \cdots & p_n
\end{array}
\]

The probability total rule is

\[
p_1+p_2+p_3+\cdots+p_n=1.
\]

**Bridge Note:** In ordinary A-Level Maths, probabilities were often attached to tree diagrams, Venn diagrams or binomial models. Here, the distribution table is the model.

## 8.2 Example Structure: A Fair Die

Let

\[
X=\text{the score when a fair die is rolled}.
\]

Then

\[
X\in\{1,2,3,4,5,6\}.
\]

Because the die is fair,

\[
P(X=1)=P(X=2)=P(X=3)=P(X=4)=P(X=5)=P(X=6)=\frac16.
\]

The probability distribution is

\[
\begin{array}{c|cccccc}
x & 1 & 2 & 3 & 4 & 5 & 6\\
\hline
P(X=x) & \frac16 & \frac16 & \frac16 & \frac16 & \frac16 & \frac16
\end{array}
\]

Check:

\[
\frac16+\frac16+\frac16+\frac16+\frac16+\frac16
=
\frac66
=
1.
\]

## 8.3 Expected Value as a Probability-Weighted Mean

The expected value is

\[
E(X)=\sum xP(X=x).
\]

For the fair die:

\[
E(X)
=
1\cdot\frac16
+
2\cdot\frac16
+
3\cdot\frac16
+
4\cdot\frac16
+
5\cdot\frac16
+
6\cdot\frac16.
\]

Factor out \(\frac16\):

\[
E(X)
=
\frac16(1+2+3+4+5+6).
\]

Add the outcomes:

\[
1+2+3+4+5+6=21.
\]

So

\[
E(X)=\frac{21}{6}=\frac72=3.5.
\]

This does not mean you can roll a \(3.5\). It means that over many rolls, the mean score tends towards \(3.5\).

**Bridge Note:** This is the same idea as a frequency table mean. In a frequency table, you calculate \(\sum fx/\sum f\). In a probability distribution, the probabilities already add to \(1\), so the calculation becomes \(\sum xp(x)\).

## 8.4 The Frequency Table Connection

Suppose a fair die is rolled \(60\) times and the results are exactly consistent with equal probabilities. Then each outcome appears \(10\) times.

\[
\begin{array}{c|cccccc}
x & 1 & 2 & 3 & 4 & 5 & 6\\
\hline
f & 10 & 10 & 10 & 10 & 10 & 10
\end{array}
\]

The frequency table mean is

\[
\bar{x}
=
\frac{\sum fx}{\sum f}
=
\frac{1(10)+2(10)+3(10)+4(10)+5(10)+6(10)}{60}
=
\frac{210}{60}=3.5.
\]

This matches \(E(X)=3.5\).

## 8.5 Expected Value of a Game: Why Profit Matters

Suppose a game costs £10 to play. When calculating the expected value, the outcome should be the **net gain** or **profit**, not just the prize.

### Game A

The game costs £10 to play. There is a \(5\%\) chance of winning £50, a \(30\%\) chance of winning £25, a \(25\%\) chance of winning £10, and otherwise nothing.

Convert prizes into profit:

| Prize | Cost | Profit |
|---:|---:|---:|
| £50 | £10 | £40 |
| £25 | £10 | £15 |
| £10 | £10 | £0 |
| £0 | £10 | \(-£10\) |

The losing probability is

\[
1-0.05-0.30-0.25=0.40.
\]

So

\[
\begin{array}{c|cccc}
x & -10 & 0 & 15 & 40\\
\hline
P(X=x) & 0.40 & 0.25 & 0.30 & 0.05
\end{array}
\]

\[
E(X)=(-10)(0.40)+0(0.25)+15(0.30)+40(0.05).
\]

\[
E(X)=-4+0+4.5+2=2.5.
\]

So the expected profit is £2.50 per game.

### Game B

The game costs £10 to play. There is a \(1\%\) chance of winning £1000, a \(5\%\) chance of winning £50, and otherwise nothing.

Convert prizes into profit:

| Prize | Cost | Profit |
|---:|---:|---:|
| £1000 | £10 | £990 |
| £50 | £10 | £40 |
| £0 | £10 | \(-£10\) |

The losing probability is

\[
1-0.01-0.05=0.94.
\]

So

\[
\begin{array}{c|ccc}
y & -10 & 40 & 990\\
\hline
P(Y=y) & 0.94 & 0.05 & 0.01
\end{array}
\]

\[
E(Y)=(-10)(0.94)+40(0.05)+990(0.01)=-9.4+2+9.9=2.5.
\]

Game A and Game B have the same expected value. They do not have the same spread.

## 8.6 Quick Expected Value Calculations

For

\[
\begin{array}{c|ccc}
x & 1 & 2 & 3\\
\hline
p(x) & 0.1 & 0.6 & 0.3
\end{array}
\]

\[
E(X)=1(0.1)+2(0.6)+3(0.3)=0.1+1.2+0.9=2.2.
\]

For

\[
\begin{array}{c|ccc}
y & 4 & 6 & 8\\
\hline
P(Y=y) & 0.5 & 0.25 & 0.25
\end{array}
\]

\[
E(Y)=4(0.5)+6(0.25)+8(0.25)=2+1.5+2=5.5.
\]

For

\[
\begin{array}{c|ccc}
z & 10 & 20 & 30\\
\hline
P(Z=z) & \frac14 & \frac12 & \frac14
\end{array}
\]

\[
E(Z)=10\left(\frac14\right)+20\left(\frac12\right)+30\left(\frac14\right)=2.5+10+7.5=20.
\]

This distribution is symmetrical about \(20\), and the probabilities are also symmetrical about \(20\). Therefore the expected value is the central value.

## 8.7 Unknown Probabilities: Two Unknowns Need Two Equations

Suppose

\[
\begin{array}{c|ccccc}
x & 1 & 2 & 3 & 4 & 5\\
\hline
P(X=x) & 0.1 & p & 0.3 & q & 0.2
\end{array}
\]

and \(E(X)=3\). There are two unknowns, so we need two equations.

Probabilities add to \(1\):

\[
0.1+p+0.3+q+0.2=1.
\]

\[
p+q+0.6=1.
\]

\[
p+q=0.4. \tag{1}
\]

Expected value is \(3\):

\[
1(0.1)+2p+3(0.3)+4q+5(0.2)=3.
\]

\[
0.1+2p+0.9+4q+1=3.
\]

\[
2p+4q+2=3.
\]

\[
2p+4q=1. \tag{2}
\]

From equation \((1)\),

\[
q=0.4-p.
\]

Substitute into equation \((2)\):

\[
2p+4(0.4-p)=1.
\]

\[
2p+1.6-4p=1.
\]

\[
1.6-2p=1.
\]

\[
0.6=2p.
\]

\[
p=0.3.
\]

Then

\[
q=0.4-0.3=0.1.
\]

Therefore

\[
p=0.3,\qquad q=0.1.
\]

**Bridge Note:** This is just simultaneous equations from ordinary algebra, but the equations come from probability and expected value.

## 8.8 Expected Value of \(2X\), \(X^2\) and Other Functions

Suppose

\[
\begin{array}{c|ccc}
x & 1 & 2 & 3\\
\hline
P(X=x) & 0.1 & 0.4 & 0.5
\end{array}
\]

First,

\[
E(X)=1(0.1)+2(0.4)+3(0.5)=0.1+0.8+1.5=2.4.
\]

If the random variable is \(2X\), the outcomes are doubled but probabilities stay the same:

\[
E(2X)=2(0.1)+4(0.4)+6(0.5)=0.2+1.6+3=4.8.
\]

Notice

\[
E(2X)=2E(X).
\]

For \(X^2\), square each outcome but keep the same probabilities:

\[
E(X^2)=1(0.1)+4(0.4)+9(0.5)=0.1+1.6+4.5=6.2.
\]

Important warning:

\[
E(X^2)\ne [E(X)]^2
\]

in general. Here,

\[
[E(X)]^2=(2.4)^2=5.76,
\]

so

\[
6.2\ne 5.76.
\]

## 8.9 Variance: Spread Around the Expected Value

Variance measures how spread out the outcomes are around the expected value. A small variance means outcomes tend to lie close to \(E(X)\). A large variance means outcomes can be far from \(E(X)\).

For a discrete random variable,

\[
\operatorname{Var}(X)=E(X^2)-[E(X)]^2.
\]

There is also a definition-based version:

\[
\operatorname{Var}(X)=E\left((X-E(X))^2\right).
\]

This means: work out \(E(X)\), subtract it from each outcome, square the result, and find the expected value of those squared distances. In exam practice, the efficient formula is

\[
\operatorname{Var}(X)=E(X^2)-[E(X)]^2.
\]

**Bridge Note:** Ordinary statistics used mean of squares minus square of mean. Further Statistics writes the same idea using \(E(X)\) notation.

## 8.10 Variance Example

Suppose

\[
\begin{array}{c|ccc}
x & 1 & 2 & 3\\
\hline
P(X=x) & 0.1 & 0.5 & 0.4
\end{array}
\]

First find \(E(X)\):

\[
E(X)=1(0.1)+2(0.5)+3(0.4)=0.1+1+1.2=2.3.
\]

Now find \(E(X^2)\):

\[
E(X^2)=1(0.1)+4(0.5)+9(0.4)=0.1+2+3.6=5.7.
\]

Now calculate variance:

\[
\operatorname{Var}(X)=5.7-(2.3)^2=5.7-5.29=0.41.
\]

The standard deviation is

\[
\sigma_X=\sqrt{0.41}=0.640\ldots
\]

To three decimal places,

\[
\sigma_X=0.640.
\]

## 8.11 Calculator Check for Variance

A calculator can often find the variance from a statistics table if you enter the outcomes as the \(x\)-values and the probabilities as frequencies. This works because the probabilities behave like relative frequencies.

However, the lesson evidence treats this as a check, not as a replacement for method.

A safe manual structure is:

\[
E(X),\qquad E(X^2),\qquad \operatorname{Var}(X)=E(X^2)-[E(X)]^2.
\]

## 8.12 Probability Inequalities from a Table

Suppose the distribution of \(X\) is given in a table. To find a probability such as

\[
P(1<X\leq 3),
\]

do not integrate, approximate or use a continuous interval idea. You simply choose the table entries whose \(x\)-values satisfy the inequality.

If the possible values are \(0,1,2,3,4\), then the values satisfying \(1<X\leq3\) are \(2,3\). Therefore

\[
P(1<X\leq3)=P(X=2)+P(X=3).
\]

**Bridge Note:** Ordinary probability taught interval language, but Further Statistics asks you to apply it to the possible values of a discrete random variable. The endpoints matter.

## 8.13 Linear Coding for Expected Value

Let

\[
Y=aX+b.
\]

Then

\[
E(Y)=E(aX+b)=aE(X)+b.
\]

Examples:

\[
E(4X+1)=4E(X)+1.
\]

\[
E(1-X)=1-E(X).
\]

\[
E\left(\frac{X-1}{2}\right)
=E\left(\frac12X-\frac12\right)
=\frac12E(X)-\frac12.
\]

## 8.14 Linear Coding for Variance

Let

\[
Y=aX+b.
\]

Then

\[
\operatorname{Var}(Y)=\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X).
\]

Examples:

\[
\operatorname{Var}(4X)=16\operatorname{Var}(X).
\]

\[
\operatorname{Var}(X+1)=\operatorname{Var}(X).
\]

\[
\operatorname{Var}(3X+2)=9\operatorname{Var}(X).
\]

\[
\operatorname{Var}\left(\frac{X-1}{2}\right)
=\operatorname{Var}\left(\frac12X-\frac12\right)
=\left(\frac12\right)^2\operatorname{Var}(X)=\frac14\operatorname{Var}(X).
\]

## 8.15 Why the Coding Rule is Linear Only

The rules

\[
E(aX+b)=aE(X)+b
\]

and

\[
\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)
\]

apply to linear codings. They do not apply to non-linear functions.

In general,

\[
E(X^2)\ne [E(X)]^2
\]

and

\[
E(\sin X)\ne \sin(E(X)).
\]

Suppose

\[
P(X=30^\circ)=0.2,\qquad P(X=60^\circ)=0.8.
\]

Then

\[
E(\sin X)=0.2\sin(30^\circ)+0.8\sin(60^\circ)
=0.2\left(\frac12\right)+0.8\left(\frac{\sqrt3}{2}\right)
\approx0.793.
\]

But

\[
E(X)=30(0.2)+60(0.8)=54^\circ,
\]

so

\[
\sin(E(X))=\sin(54^\circ)\approx0.809.
\]

Therefore

\[
E(\sin X)\ne \sin(E(X)).
\]

## 8.16 Inverse Coding and Substitution

Sometimes a question defines a new random variable \(Y\) in terms of \(X\), then gives information about \(Y\).

For example:

\[
Y=\frac{X-150}{50}=\frac{1}{50}X-3.
\]

If

\[
E(Y)=5.1,
\]

then

\[
E\left(\frac{1}{50}X-3\right)=5.1.
\]

Using linearity:

\[
\frac{1}{50}E(X)-3=5.1.
\]

Add \(3\):

\[
\frac{1}{50}E(X)=8.1.
\]

Multiply by \(50\):

\[
E(X)=405.
\]

If

\[
\operatorname{Var}(Y)=2.5,
\]

then

\[
\operatorname{Var}\left(\frac{1}{50}X-3\right)=2.5.
\]

The variance rule gives

\[
\left(\frac{1}{50}\right)^2\operatorname{Var}(X)=2.5.
\]

So

\[
\frac{1}{2500}\operatorname{Var}(X)=2.5.
\]

Multiply by \(2500\):

\[
\operatorname{Var}(X)=6250.
\]

## 8.17 Solving Probability Questions Involving \(Y=aX+b\)

If a question asks for a probability involving \(Y\), and \(Y\) is defined in terms of \(X\), substitute.

Suppose

\[
Y=3X-1.
\]

To find

\[
P(X>Y),
\]

replace \(Y\) with \(3X-1\):

\[
P(X>3X-1).
\]

Solve:

\[
X>3X-1.
\]

\[
-2X>-1.
\]

Divide by \(-2\), remembering that the inequality sign reverses:

\[
X<\frac12.
\]

Therefore

\[
P(X>Y)=P\left(X<\frac12\right).
\]

---

# 9. Visual Asset Integration

## 9.1 Visual Evidence Limitation Statement

Diagram evidence is partially unclear here. The screenshot PDF was supplied as a 150-page visual capture, but no parsed text could be extracted from it. The visual descriptions below preserve visible/readable details from the previewed screenshot pages only. No uninspected visual detail is claimed.

Some visuals are evidence-backed because they reproduce the mathematical structure visible in the supplied slides or transcript. Others are AI-proposed teaching enhancements based on the evidence and are labelled as such.

## 9.2 Planned Visual Placeholders

[VISUAL PLACEHOLDER: FAS2DiscreteRandomVariablesMermaid-001 | Source: CCEA FAS2-DIST specification boundary + uploaded transcript method flow | Insert from mermaid/FAS2DiscreteRandomVariablesMermaid-001.md | Purpose: Show the decision pathway for a discrete random variable table question. Description: The flowchart should begin with “Read the table”, then branch into “Check probabilities sum to 1”, “Find required probability by selecting outcomes”, “Find \(E(X)\) using \(\sum xp(x)\)”, “Find \(E(X^2)\) using \(\sum x^2p(x)\)”, “Find \(\operatorname{Var}(X)\) using \(E(X^2)-[E(X)]^2\)”, and “Apply coding if \(Y=aX+b\)”.]

[VISUAL PLACEHOLDER: FAS2DiscreteRandomVariablesSVG-001 | Source: Screenshot PDF pages showing Game A and Game B motivation + transcript explanation | Insert from svg/FAS2DiscreteRandomVariablesSVG-001.svg | Purpose: Compare two games with the same expected value but different spread. Description: The visual should show Game A and Game B side by side. Game A should show net gains \(-10,0,15,40\) with probabilities \(0.40,0.25,0.30,0.05\). Game B should show net gains \(-10,40,990\) with probabilities \(0.94,0.05,0.01\). Both should display \(E=2.5\), with Game B marked as higher spread.]

[VISUAL PLACEHOLDER: FAS2DiscreteRandomVariablesSVG-002 | Source: FS1 PDF recap slide and screenshot PDF fair die table | Insert from svg/FAS2DiscreteRandomVariablesSVG-002.svg | Purpose: Define a discrete random variable using a fair die. Description: The visual should show a die icon or simple cube symbol, a two-row table with \(x=1,2,3,4,5,6\), \(P(X=x)=\frac16\) for each outcome, and labels explaining uppercase \(X\) as the random variable and lowercase \(x\) as a specific outcome.]

[VISUAL PLACEHOLDER: FAS2DiscreteRandomVariablesSVG-003 | Source: FS1 PDF expected value slides + transcript frequency table bridge | Insert from svg/FAS2DiscreteRandomVariablesSVG-003.svg | Purpose: Show expected value as a probability-weighted mean. Description: The visual should compare a frequency table calculation \(\bar{x}=\frac{\sum fx}{\sum f}\) with a probability table calculation \(E(X)=\sum xp(x)\), highlighting that probabilities sum to \(1\).]

[VISUAL PLACEHOLDER: FAS2DiscreteRandomVariablesSVG-004 | Source: Transcript variance explanation comparing Game A and Game B | Insert from svg/FAS2DiscreteRandomVariablesSVG-004.svg | Purpose: Show that equal expected values can have different variances. Description: The visual should show two horizontal number lines centred at \(2.5\). Game A should have outcomes nearer the centre overall; Game B should have a far-right outcome \(990\) and a strong mass at \(-10\), indicating a much larger spread.]

[VISUAL PLACEHOLDER: FAS2DiscreteRandomVariablesBridgeSVG-001 | Source: Ordinary A-Level Maths bridge + Further Maths specification | Insert from svg/FAS2DiscreteRandomVariablesBridgeSVG-001.svg | Purpose: Compare prior ordinary Maths method with Further Maths extension. Description: The visual should show three bridge lanes: frequency table mean \(\to\) expected value, listed-data variance \(\to\) \(\operatorname{Var}(X)=E(X^2)-[E(X)]^2\), and ordinary coding \(\to\) \(E(aX+b)\), \(\operatorname{Var}(aX+b)\).]

[VISUAL PLACEHOLDER: FAS2DiscreteRandomVariablesTikZ-001 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from tikz/FAS2DiscreteRandomVariablesTikZ-001.tex | Purpose: Provide a clean calculation table template. Description: The TikZ table should have rows \(x\), \(P(X=x)\), \(xP(X=x)\), \(x^2\), \(x^2P(X=x)\), with a final column for totals \(1\), \(E(X)\), and \(E(X^2)\).]

[VISUAL PLACEHOLDER: FAS2DiscreteRandomVariablesTikZ-002 | Source: Transcript coding section + CCEA LO006 | Insert from tikz/FAS2DiscreteRandomVariablesTikZ-002.tex | Purpose: Visualise linear coding \(Y=aX+b\). Description: The diagram should show an input distribution for \(X\), an arrow labelled “multiply by \(a\), then add \(b\)” leading to \(Y\), with formula boxes \(E(Y)=aE(X)+b\) and \(\operatorname{Var}(Y)=a^2\operatorname{Var}(X)\).]

---

# 10. Interactive Learning Widgets

## 10.1 Widget Evidence Limitation Statement

The uploaded evidence does not contain interactive widgets. The following widgets are AI-proposed teaching enhancements based on the lesson evidence and the CCEA FAS2-DIST boundary. They are not evidence-backed original assets.

## 10.2 Planned Interactive Placeholders

[INTERACTIVE PLACEHOLDER: FAS2DiscreteRandomVariablesWidget-001 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FAS2DiscreteRandomVariablesWidget-001.html | Purpose: Build and check a discrete random variable table.]

Student input: possible outcomes \(x_1,x_2,\ldots,x_n\) and corresponding probabilities \(p_1,p_2,\ldots,p_n\). The widget displays \(\sum p_i\), whether probabilities sum to \(1\), whether any probability is outside \(0\leq p\leq1\), \(E(X)\), \(E(X^2)\), \(\operatorname{Var}(X)\) and standard deviation.

[INTERACTIVE PLACEHOLDER: FAS2DiscreteRandomVariablesWidget-002 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FAS2DiscreteRandomVariablesWidget-002.html | Purpose: Practise linear coding for expectation and variance.]

Student input: \(E(X)\), \(\operatorname{Var}(X)\), constants \(a\) and \(b\) in \(Y=aX+b\). The widget displays \(E(Y)=aE(X)+b\), \(\operatorname{Var}(Y)=a^2\operatorname{Var}(X)\), a warning that \(b\) does not affect variance, and an optional standard deviation comparison.

[INTERACTIVE PLACEHOLDER: FAS2DiscreteRandomVariablesWidget-003 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FAS2DiscreteRandomVariablesWidget-003.html | Purpose: Select outcomes satisfying inequalities such as \(P(a\leq X<b)\).]

Student input: a distribution table and an inequality statement such as \(1<X\leq3\), \(X>0.2\), or \(X<\frac12\). The widget highlights outcomes satisfying the inequality, selected probabilities and the total probability.

---

# 11. Worked Examples

## Worked Example 1: Game A Expected Profit

### Evidence source

Uploaded teacher transcript and visible screenshot slide motivation.

### On-spec status

On-spec as an expected value example for a simple discrete random variable under `FAS2-DIST-LO002` and `FAS2-DIST-LO003`.

### Question

Game A costs £10 to play. You have a \(5\%\) chance of winning £50, a \(30\%\) chance of winning £25, a \(25\%\) chance of winning £10, and otherwise nothing. Find the expected profit per game.

### Step-by-step solution

Let

\[
X=\text{profit from playing Game A once}.
\]

Convert each prize into profit:

\[
50-10=40,
\]

\[
25-10=15,
\]

\[
10-10=0,
\]

\[
0-10=-10.
\]

The remaining probability is

\[
1-0.05-0.30-0.25=0.40.
\]

So

\[
\begin{array}{c|cccc}
x & -10 & 0 & 15 & 40\\
\hline
P(X=x) & 0.40 & 0.25 & 0.30 & 0.05
\end{array}
\]

Use

\[
E(X)=\sum xP(X=x).
\]

Therefore

\[
E(X)=(-10)(0.40)+0(0.25)+15(0.30)+40(0.05).
\]

\[
E(X)=-4+0+4.5+2=2.5.
\]

### Final exam-style answer

The expected profit is

\[
\boxed{£2.50}
\]

per game.

### Teaching note

The outcome is profit, not prize. The entry cost must be subtracted before calculating expected value.

## Worked Example 2: Game B Expected Profit

### Evidence source

Uploaded teacher transcript and visible screenshot slide motivation.

### On-spec status

On-spec as an expected value example for a simple discrete random variable under `FAS2-DIST-LO002` and `FAS2-DIST-LO003`.

### Question

Game B costs £10 to play. You have a \(1\%\) chance of winning £1000, a \(5\%\) chance of winning £50, and otherwise nothing. Find the expected profit per game.

### Step-by-step solution

Let

\[
Y=\text{profit from playing Game B once}.
\]

Convert each prize into profit:

\[
1000-10=990,
\]

\[
50-10=40,
\]

\[
0-10=-10.
\]

The losing probability is

\[
1-0.01-0.05=0.94.
\]

So

\[
\begin{array}{c|ccc}
y & -10 & 40 & 990\\
\hline
P(Y=y) & 0.94 & 0.05 & 0.01
\end{array}
\]

\[
E(Y)=(-10)(0.94)+40(0.05)+990(0.01)=-9.4+2+9.9=2.5.
\]

### Final exam-style answer

\[
\boxed{£2.50}
\]

per game.

### Teaching note

Game A and Game B have the same expected value. They are not equally “safe”. The variance of Game B is much larger because the outcomes are more spread out.

## Worked Example 3: Expected Value from a Simple Distribution

Find \(E(X)\) for

\[
\begin{array}{c|ccc}
x & 1 & 2 & 3\\
\hline
p(x) & 0.1 & 0.6 & 0.3
\end{array}
\]

Use

\[
E(X)=\sum xp(x).
\]

So

\[
E(X)=1(0.1)+2(0.6)+3(0.3)=0.1+1.2+0.9=2.2.
\]

\[
\boxed{E(X)=2.2}
\]

## Worked Example 4: Symmetrical Distribution

Find \(E(Z)\) for

\[
\begin{array}{c|ccc}
z & 10 & 20 & 30\\
\hline
P(Z=z) & \frac14 & \frac12 & \frac14
\end{array}
\]

The distribution is symmetrical about \(20\). Confirm by calculation:

\[
E(Z)=10\left(\frac14\right)+20\left(\frac12\right)+30\left(\frac14\right)
=\frac52+10+\frac{15}{2}
=\frac{5+20+15}{2}
=20.
\]

\[
\boxed{E(Z)=20}
\]

## Worked Example 5: Unknown Probabilities Using \(E(X)\)

The probability distribution of \(X\) is

\[
\begin{array}{c|ccccc}
x & 1 & 2 & 3 & 4 & 5\\
\hline
P(X=x) & 0.1 & p & 0.3 & q & 0.2
\end{array}
\]

Given \(E(X)=3\), find \(p\) and \(q\).

Probabilities add to \(1\):

\[
0.1+p+0.3+q+0.2=1.
\]

\[
p+q=0.4. \tag{1}
\]

Expected value is \(3\):

\[
1(0.1)+2p+3(0.3)+4q+5(0.2)=3.
\]

\[
2p+4q=1. \tag{2}
\]

From \((1)\), \(q=0.4-p\). Substitute into \((2)\):

\[
2p+4(0.4-p)=1.
\]

\[
2p+1.6-4p=1.
\]

\[
1.6-2p=1.
\]

\[
0.6=2p.
\]

\[
p=0.3.
\]

Then

\[
q=0.4-0.3=0.1.
\]

\[
\boxed{p=0.3,\qquad q=0.1}
\]

## Worked Example 6: Biased Die with Unknowns

A biased die has probability distribution

\[
\begin{array}{c|cccccc}
x & 1 & 2 & 3 & 4 & 5 & 6\\
\hline
P(X=x) & a & a & a & b & b & 0.3
\end{array}
\]

Given \(E(X)=4.2\), find \(a\) and \(b\).

Probabilities add to \(1\):

\[
a+a+a+b+b+0.3=1.
\]

\[
3a+2b=0.7. \tag{1}
\]

Expected value:

\[
1a+2a+3a+4b+5b+6(0.3)=4.2.
\]

\[
6a+9b+1.8=4.2.
\]

\[
6a+9b=2.4. \tag{2}
\]

Multiply \((1)\) by \(2\):

\[
6a+4b=1.4. \tag{3}
\]

Subtract \((3)\) from \((2)\):

\[
5b=1.
\]

\[
b=0.2.
\]

Substitute into \((1)\):

\[
3a+2(0.2)=0.7.
\]

\[
3a+0.4=0.7.
\]

\[
3a=0.3.
\]

\[
a=0.1.
\]

\[
\boxed{a=0.1,\qquad b=0.2}
\]

## Worked Example 7: Calculating \(E(2X)\)

Let

\[
\begin{array}{c|ccc}
x & 1 & 2 & 3\\
\hline
P(X=x) & 0.1 & 0.4 & 0.5
\end{array}
\]

The outcomes of \(2X\) are \(2,4,6\). Probabilities do not change.

\[
E(2X)=2(0.1)+4(0.4)+6(0.5)=0.2+1.6+3=4.8.
\]

\[
\boxed{E(2X)=4.8}
\]

## Worked Example 8: Calculating \(E(X^2)\)

For the same table,

\[
E(X^2)=1(0.1)+4(0.4)+9(0.5)=0.1+1.6+4.5=6.2.
\]

\[
\boxed{E(X^2)=6.2}
\]

Do not calculate \([E(X)]^2\) instead.

## Worked Example 9: Variance and Standard Deviation

Let

\[
\begin{array}{c|ccc}
x & 1 & 2 & 3\\
\hline
P(X=x) & 0.1 & 0.5 & 0.4
\end{array}
\]

\[
E(X)=1(0.1)+2(0.5)+3(0.4)=2.3.
\]

\[
E(X^2)=1(0.1)+4(0.5)+9(0.4)=5.7.
\]

\[
\operatorname{Var}(X)=5.7-(2.3)^2=5.7-5.29=0.41.
\]

\[
\sigma_X=\sqrt{0.41}=0.640\ldots
\]

\[
\boxed{E(X)=2.3},\qquad \boxed{E(X^2)=5.7},\qquad \boxed{\operatorname{Var}(X)=0.41},\qquad \boxed{\sigma_X=0.640\text{ to 3 d.p.}}
\]

## Worked Example 10: Variance with an Unknown Probability

The random variable \(X\) has distribution

\[
\begin{array}{c|ccccc}
x & -1 & 0 & 1 & 2 & 3\\
\hline
P(X=x) & \frac15 & a & \frac{1}{10} & a & \frac15
\end{array}
\]

Find \(a\), \(E(X)\), and \(\operatorname{Var}(X)\).

Probabilities add to \(1\):

\[
\frac15+a+\frac{1}{10}+a+\frac15=1.
\]

\[
0.2+a+0.1+a+0.2=1.
\]

\[
2a+0.5=1.
\]

\[
a=0.25=\frac14.
\]

Now

\[
E(X)=(-1)(0.2)+0(0.25)+1(0.1)+2(0.25)+3(0.2)
=-0.2+0+0.1+0.5+0.6=1.
\]

Square the outcomes:

\[
(-1)^2=1,\quad 0^2=0,\quad 1^2=1,\quad 2^2=4,\quad 3^2=9.
\]

\[
E(X^2)=1(0.2)+0(0.25)+1(0.1)+4(0.25)+9(0.2)
=0.2+0+0.1+1+1.8=3.1.
\]

\[
\operatorname{Var}(X)=3.1-1^2=2.1.
\]

\[
\boxed{a=\frac14},\qquad \boxed{E(X)=1},\qquad \boxed{\operatorname{Var}(X)=2.1}
\]

## Worked Example 11: Probability Inequalities from a Table

If the possible outcomes are

\[
0,\ 1,\ 2,\ 3,\ 4
\]

then the values satisfying

\[
1<X\leq3
\]

are

\[
2,\ 3.
\]

Therefore

\[
P(1<X\leq3)=P(X=2)+P(X=3).
\]

If

\[
P(X=2)=0.3,\qquad P(X=3)=0.05,
\]

then

\[
P(1<X\leq3)=0.3+0.05=0.35.
\]

\[
\boxed{P(1<X\leq3)=0.35}
\]

## Worked Example 12: Linear Coding with \(Y=10X-30\)

Suppose

\[
Y=10X-30,
\]

\[
E(X)=6.55,
\]

and

\[
\operatorname{Var}(X)=98.9475.
\]

Use expectation:

\[
E(Y)=10E(X)-30=10(6.55)-30=65.5-30=35.5.
\]

Use variance:

\[
\operatorname{Var}(Y)=10^2\operatorname{Var}(X)=100(98.9475)=9894.75.
\]

\[
\boxed{E(Y)=35.5},\qquad \boxed{\operatorname{Var}(Y)=9894.75}
\]

## Worked Example 13: Showing Linear Rules Do Not Apply to Non-Linear Functions

Let

\[
P(X=30^\circ)=0.2,\qquad P(X=60^\circ)=0.8.
\]

Then

\[
E(\sin X)=0.2\sin(30^\circ)+0.8\sin(60^\circ).
\]

Using

\[
\sin(30^\circ)=\frac12,\qquad \sin(60^\circ)=\frac{\sqrt3}{2},
\]

\[
E(\sin X)=0.2\left(\frac12\right)+0.8\left(\frac{\sqrt3}{2}\right)=0.1+0.4\sqrt3\approx0.793.
\]

But

\[
E(X)=30(0.2)+60(0.8)=54^\circ,
\]

so

\[
\sin(E(X))=\sin(54^\circ)\approx0.809.
\]

Therefore

\[
\boxed{E(\sin X)\ne \sin(E(X))}.
\]

## Worked Example 14: Inverse Coding \(Y=\frac{X-150}{50}\)

\[
Y=\frac{X-150}{50}=\frac{1}{50}X-3.
\]

Given

\[
E(Y)=5.1,\qquad \operatorname{Var}(Y)=2.5,
\]

find \(E(X)\) and \(\operatorname{Var}(X)\).

For expectation:

\[
5.1=\frac{1}{50}E(X)-3.
\]

\[
8.1=\frac{1}{50}E(X).
\]

\[
E(X)=50(8.1)=405.
\]

For variance:

\[
2.5=\left(\frac{1}{50}\right)^2\operatorname{Var}(X).
\]

\[
2.5=\frac{1}{2500}\operatorname{Var}(X).
\]

\[
\operatorname{Var}(X)=2.5(2500)=6250.
\]

\[
\boxed{E(X)=405},\qquad \boxed{\operatorname{Var}(X)=6250}
\]

## Worked Example 15: Using \(Y=3X-1\) and Solving \(P(X>Y)\)

Given

\[
Y=3X-1,
\]

find a simplified probability statement for

\[
P(X>Y).
\]

Substitute:

\[
P(X>Y)=P(X>3X-1).
\]

Solve:

\[
X>3X-1.
\]

\[
-2X>-1.
\]

Divide by \(-2\), reversing the inequality:

\[
X<\frac12.
\]

Therefore

\[
\boxed{P(X>Y)=P\left(X<\frac12\right)}.
\]

For the evidence table, this becomes

\[
P\left(X<\frac12\right)=0.3+0.2+0.25=0.75.
\]

\[
\boxed{P(X>Y)=0.75}
\]

---

# 12. Common Mistakes and Exam Traps

## 12.1 Treating Prize as Profit

If a game costs money to play, the random variable should usually represent net gain or profit. The entry cost changes every outcome.

Wrong method:

\[
0.05(50)+0.30(25)+0.25(10).
\]

Correct method:

\[
0.05(40)+0.30(15)+0.25(0)+0.40(-10).
\]

## 12.2 Forgetting the “Otherwise” Probability

If probabilities are listed but do not add to \(1\), the missing probability is

\[
1-\text{sum of listed probabilities}.
\]

## 12.3 Confusing \(X\) and \(x\)

\(X\) is the random variable. \(x\) is a particular outcome. The standard table heading is \(P(X=x)\).

## 12.4 Forgetting That Probabilities Add to \(1\)

For every probability distribution,

\[
\sum P(X=x)=1.
\]

Unknown probability questions almost always use this rule.

## 12.5 Doubling the Probabilities When Finding \(E(2X)\)

If \(2X\) is used, only the outcomes are doubled. The probabilities do not change.

## 12.6 Confusing \(E(X^2)\) with \([E(X)]^2\)

Usually,

\[
E(X^2)\ne [E(X)]^2.
\]

To find \(E(X^2)\), square each \(x\)-value first, then multiply by its probability.

## 12.7 Using the Variance Formula Backwards

Correct:

\[
\operatorname{Var}(X)=E(X^2)-[E(X)]^2.
\]

Rearranged:

\[
E(X^2)=\operatorname{Var}(X)+[E(X)]^2.
\]

## 12.8 Forgetting That Variance Cannot Be Negative

Since variance measures squared spread,

\[
\operatorname{Var}(X)\geq0.
\]

## 12.9 Adding \(b\) to the Variance in \(aX+b\)

Correct:

\[
E(aX+b)=aE(X)+b.
\]

Correct:

\[
\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X).
\]

Wrong:

\[
\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)+b.
\]

## 12.10 Multiplying Variance by \(a\) Instead of \(a^2\)

If \(Y=3X-10\), then

\[
\operatorname{Var}(Y)=9\operatorname{Var}(X),
\]

not \(3\operatorname{Var}(X)-10\).

## 12.11 Applying Linear Coding Rules to Non-Linear Functions

The rule \(E(aX+b)=aE(X)+b\) works for linear expressions. It does not mean \(E(X^2)=[E(X)]^2\) or \(E(\sin X)=\sin(E(X))\).

## 12.12 Reading Inequality Endpoints Incorrectly

For \(P(1<X\leq3)\), include values greater than \(1\) and less than or equal to \(3\). So \(1\) is excluded and \(3\) is included.

## 12.13 Forgetting to Reverse the Inequality

If solving

\[
-2X>-1,
\]

divide by \(-2\). The inequality reverses:

\[
X<\frac12.
\]

## 12.14 Calculator Mode Trap

If using a calculator’s statistics mode to check variance, probabilities can be entered as frequencies because they behave as relative frequencies. However, for exam working, show \(E(X)\), \(E(X^2)\), and \(\operatorname{Var}(X)=E(X^2)-[E(X)]^2\).

---

# 13. Practice Questions

The following questions are generated practice questions aligned with the CCEA FAS2 discrete random variable boundary. They are not past-paper or textbook questions.

## 13.1 Basic Fluency Questions

### Question 1

The discrete random variable \(X\) has distribution

\[
\begin{array}{c|ccc}
x & 0 & 1 & 2\\
\hline
P(X=x) & 0.2 & 0.5 & 0.3
\end{array}
\]

Find \(E(X)\), \(E(X^2)\), and \(\operatorname{Var}(X)\).

### Question 2

The random variable \(Y\) has distribution

\[
\begin{array}{c|cccc}
y & -2 & 0 & 1 & 4\\
\hline
P(Y=y) & 0.1 & 0.4 & 0.3 & 0.2
\end{array}
\]

Find \(P(Y>0)\), \(P(-1\leq Y<4)\), and \(E(Y)\).

### Question 3

The random variable \(Z\) has distribution

\[
\begin{array}{c|ccc}
z & 5 & 10 & 15\\
\hline
P(Z=z) & \frac14 & \frac12 & \frac14
\end{array}
\]

Find \(E(Z)\) without doing a long calculation, then confirm it by calculation.

## 13.2 Bridge Questions

### Question 4

A frequency table is shown below.

\[
\begin{array}{c|ccc}
x & 1 & 2 & 3\\
\hline
f & 2 & 6 & 2
\end{array}
\]

1. Find the mean using ordinary frequency table methods.
2. Convert the frequencies into relative frequencies.
3. Treat the relative frequencies as probabilities and find \(E(X)\).
4. Explain why the answers match.

### Question 5

In ordinary statistics, the coded variable \(Y=4X+7\) is formed.

Given that

\[
E(X)=3.2,\qquad \operatorname{Var}(X)=1.5,
\]

find \(E(Y)\) and \(\operatorname{Var}(Y)\).

## 13.3 Standard Exam-Style Questions

### Question 6

The probability distribution of \(X\) is

\[
\begin{array}{c|cccc}
x & 1 & 2 & 3 & 4\\
\hline
P(X=x) & 0.2 & p & 0.1 & q
\end{array}
\]

Given that \(E(X)=2.7\), find \(p\) and \(q\).

### Question 7

The discrete random variable \(X\) has distribution

\[
\begin{array}{c|cccc}
x & -1 & 0 & 2 & 3\\
\hline
P(X=x) & 0.25 & 0.35 & 0.25 & 0.15
\end{array}
\]

Find \(E(X)\), \(E(X^2)\), \(\operatorname{Var}(X)\), and the standard deviation of \(X\) to three decimal places.

## 13.4 Harder Synthesis Questions

### Question 8

The random variable \(X\) has distribution

\[
\begin{array}{c|ccccc}
x & -2 & -1 & 0 & 1 & 2\\
\hline
P(X=x) & 0.1 & a & 0.4 & b & 0.1
\end{array}
\]

Given that \(E(X)=0.1\), find \(a\) and \(b\).

### Question 9

Let \(Y=5X-2\). Given that \(E(Y)=18\) and \(\operatorname{Var}(Y)=75\), find \(E(X)\) and \(\operatorname{Var}(X)\).

### Question 10

Let \(Y=2X+1\). Find a simplified probability statement in terms of \(X\) for \(P(Y<X)\). Then, using the distribution

\[
\begin{array}{c|cccc}
x & -2 & -1 & 0 & 1\\
\hline
P(X=x) & 0.2 & 0.3 & 0.1 & 0.4
\end{array}
\]

calculate \(P(Y<X)\).

---

# 14. Worked Solutions

## Solution 1

\[
E(X)=0(0.2)+1(0.5)+2(0.3)=0+0.5+0.6=1.1.
\]

\[
E(X^2)=0(0.2)+1(0.5)+4(0.3)=0+0.5+1.2=1.7.
\]

\[
\operatorname{Var}(X)=1.7-(1.1)^2=1.7-1.21=0.49.
\]

\[
\boxed{E(X)=1.1},\qquad \boxed{E(X^2)=1.7},\qquad \boxed{\operatorname{Var}(X)=0.49}
\]

## Solution 2

The outcomes greater than \(0\) are \(1\) and \(4\), so

\[
P(Y>0)=0.3+0.2=0.5.
\]

The outcomes satisfying \(-1\leq Y<4\) are \(0\) and \(1\), so

\[
P(-1\leq Y<4)=0.4+0.3=0.7.
\]

\[
E(Y)=(-2)(0.1)+0(0.4)+1(0.3)+4(0.2)=-0.2+0+0.3+0.8=0.9.
\]

\[
\boxed{P(Y>0)=0.5},\qquad \boxed{P(-1\leq Y<4)=0.7},\qquad \boxed{E(Y)=0.9}
\]

## Solution 3

The distribution is symmetrical about \(10\), so \(E(Z)=10\). Confirm:

\[
E(Z)=5\left(\frac14\right)+10\left(\frac12\right)+15\left(\frac14\right)
=\frac54+5+\frac{15}{4}
=\frac{5+20+15}{4}=10.
\]

\[
\boxed{E(Z)=10}
\]

## Solution 4

\[
\bar{x}=\frac{\sum fx}{\sum f}=\frac{1(2)+2(6)+3(2)}{2+6+2}=\frac{20}{10}=2.
\]

Relative frequencies are

\[
\frac{2}{10}=0.2,\qquad \frac{6}{10}=0.6,\qquad \frac{2}{10}=0.2.
\]

Then

\[
E(X)=1(0.2)+2(0.6)+3(0.2)=0.2+1.2+0.6=2.
\]

The answers match because probabilities are relative frequencies and add to \(1\).

## Solution 5

\[
E(Y)=E(4X+7)=4E(X)+7=4(3.2)+7=12.8+7=19.8.
\]

\[
\operatorname{Var}(Y)=\operatorname{Var}(4X+7)=4^2\operatorname{Var}(X)=16(1.5)=24.
\]

\[
\boxed{E(Y)=19.8},\qquad \boxed{\operatorname{Var}(Y)=24}
\]

## Solution 6

Probabilities add to \(1\):

\[
0.2+p+0.1+q=1.
\]

\[
p+q=0.7. \tag{1}
\]

Expected value:

\[
1(0.2)+2p+3(0.1)+4q=2.7.
\]

\[
2p+4q+0.5=2.7.
\]

\[
2p+4q=2.2. \tag{2}
\]

From \((1)\), \(p=0.7-q\). Substitute:

\[
2(0.7-q)+4q=2.2.
\]

\[
1.4-2q+4q=2.2.
\]

\[
1.4+2q=2.2.
\]

\[
2q=0.8.
\]

\[
q=0.4.
\]

Then

\[
p=0.7-0.4=0.3.
\]

\[
\boxed{p=0.3,\qquad q=0.4}
\]

## Solution 7

\[
E(X)=(-1)(0.25)+0(0.35)+2(0.25)+3(0.15)
=-0.25+0+0.5+0.45=0.7.
\]

\[
E(X^2)=1(0.25)+0(0.35)+4(0.25)+9(0.15)
=0.25+0+1+1.35=2.6.
\]

\[
\operatorname{Var}(X)=2.6-(0.7)^2=2.6-0.49=2.11.
\]

\[
\sigma_X=\sqrt{2.11}=1.45258\ldots=1.453\text{ to 3 d.p.}
\]

\[
\boxed{E(X)=0.7},\qquad \boxed{E(X^2)=2.6},\qquad \boxed{\operatorname{Var}(X)=2.11},\qquad \boxed{\sigma_X=1.453}
\]

## Solution 8

Probabilities add to \(1\):

\[
0.1+a+0.4+b+0.1=1.
\]

\[
a+b=0.4. \tag{1}
\]

Expected value:

\[
(-2)(0.1)+(-1)a+0(0.4)+1b+2(0.1)=0.1.
\]

\[
-0.2-a+b+0.2=0.1.
\]

\[
-a+b=0.1. \tag{2}
\]

Add \((1)\) and \((2)\):

\[
2b=0.5.
\]

\[
b=0.25.
\]

Then

\[
a=0.4-0.25=0.15.
\]

\[
\boxed{a=0.15,\qquad b=0.25}
\]

## Solution 9

\[
E(Y)=E(5X-2)=5E(X)-2.
\]

Given \(E(Y)=18\):

\[
18=5E(X)-2.
\]

\[
20=5E(X).
\]

\[
E(X)=4.
\]

For variance:

\[
\operatorname{Var}(Y)=\operatorname{Var}(5X-2)=25\operatorname{Var}(X).
\]

\[
75=25\operatorname{Var}(X).
\]

\[
\operatorname{Var}(X)=3.
\]

\[
\boxed{E(X)=4},\qquad \boxed{\operatorname{Var}(X)=3}
\]

## Solution 10

Given

\[
Y=2X+1.
\]

\[
P(Y<X)=P(2X+1<X).
\]

Solve:

\[
2X+1<X.
\]

\[
X+1<0.
\]

\[
X<-1.
\]

Therefore

\[
P(Y<X)=P(X<-1).
\]

From the table, the only outcome satisfying \(X<-1\) is \(X=-2\), so

\[
P(Y<X)=P(X=-2)=0.2.
\]

\[
\boxed{P(Y<X)=P(X<-1)},\qquad \boxed{P(Y<X)=0.2}
\]

---

# 15. Exam Technique Notes

## 15.1 First Question to Ask: “What Does the Random Variable Represent?”

Before calculating anything, write a clear definition such as

\[
X=\text{the profit from playing the game once}
\]

or

\[
X=\text{the score on the uppermost face of the die}.
\]

This matters because the numbers in the table depend on the meaning of the random variable.

## 15.2 Always Check the Probability Total

For any discrete probability distribution,

\[
\sum P(X=x)=1.
\]

Use this as a validity check. If the table contains unknowns, this is usually the first equation.

## 15.3 Expected Value Method Layout

For expected value, write the formula first:

\[
E(X)=\sum xP(X=x).
\]

Then substitute from the table. Do not just write the numerical answer; show the multiplication of outcomes by probabilities.

## 15.4 Variance Method Layout

For variance, use the three-step structure:

1. Find \(E(X)\).
2. Find \(E(X^2)\).
3. Use
   \[
   \operatorname{Var}(X)=E(X^2)-[E(X)]^2.
   \]

Only after \(E(X)\) and \(E(X^2)\) are known should you calculate the variance.

## 15.5 Standard Deviation

If asked for standard deviation, calculate variance first.

\[
\sigma_X=\sqrt{\operatorname{Var}(X)}.
\]

Check the wording of the question. If it asks for variance, do not accidentally give the standard deviation only.

## 15.6 Exact Values and Rounding

Use exact fractions where the table gives fractions. Decimals are acceptable when the evidence or question uses decimals, but avoid premature rounding. A variance question can become inaccurate if you round \(E(X)\) before squaring it.

## 15.7 Unknown Probabilities

If there are two unknown probabilities, expect two equations. Common sources of equations are

\[
\sum P(X=x)=1
\]

and

\[
E(X)=\sum xP(X=x).
\]

If variance is given, another possible equation is

\[
\operatorname{Var}(X)=E(X^2)-[E(X)]^2.
\]

## 15.8 Probability Inequality Questions

For a discrete random variable, inequalities are solved by selecting listed outcomes. Do not draw an area under a curve.

## 15.9 Linear Coding Questions

For

\[
Y=aX+b,
\]

use

\[
E(Y)=aE(X)+b,
\]

\[
\operatorname{Var}(Y)=a^2\operatorname{Var}(X).
\]

The \(+b\) does not affect variance.

## 15.10 Fractional Coding

If the coding is written as a fraction, split it first. For example,

\[
Y=\frac{X-1}{2}=\frac12X-\frac12.
\]

Then

\[
E(Y)=\frac12E(X)-\frac12,
\]

and

\[
\operatorname{Var}(Y)=\left(\frac12\right)^2\operatorname{Var}(X)=\frac14\operatorname{Var}(X).
\]

## 15.11 Inverse Coding

If information is given about \(Y\) and the question asks about \(X\), use the coding formula backwards.

For example,

\[
Y=\frac{X-150}{50}=\frac{1}{50}X-3.
\]

Then

\[
E(Y)=\frac{1}{50}E(X)-3,
\]

and

\[
\operatorname{Var}(Y)=\left(\frac{1}{50}\right)^2\operatorname{Var}(X).
\]

## 15.12 Transformed Probability Statements

If a probability contains both \(X\) and \(Y\), substitute the definition of \(Y\).

For example, if \(Y=3X-1\), then

\[
P(X>Y)=P(X>3X-1)=P\left(X<\frac12\right).
\]

## 15.13 Calculator Use

A calculator can help check simultaneous equations, expected value, variance and standard deviation. For written work, always show

\[
E(X)=\sum xP(X=x),
\]

\[
E(X^2)=\sum x^2P(X=x),
\]

\[
\operatorname{Var}(X)=E(X^2)-[E(X)]^2.
\]

---

# 16. Syllabus Gap Check

## 16.1 LO Coverage Table

| LO ID | Official CCEA Further Maths wording | Covered in this lesson? | Evidence coverage | Notes |
|---|---|---:|---|---|
| `FAS2-DIST-LO002` | demonstrate understanding of and use discrete probability distributions, including probability functions, mean, variance and standard deviation | Yes | Definitions, notation, distribution tables, expected value, variance, standard deviation | Fully covered for discrete random variables. |
| `FAS2-DIST-LO003` | calculate probabilities such as \(P(a\leq X\leq b)\), \(E(X)\) and \(\operatorname{Var}(X)\) for simple cases of a discrete random variable \(X\) | Yes | Probability inequalities, \(E(X)\), \(E(X^2)\), \(\operatorname{Var}(X)\), unknown probabilities | Fully covered for finite table examples. |
| `FAS2-DIST-LO006` | understand and use the expressions for \(E(aX+b)\) and \(\operatorname{Var}(aX+b)\), where \(X\) is a discrete or continuous random variable | Partly | Discrete case covered in depth | Continuous random variable case excluded from this lesson and deferred. |
| `FAS2-DIST-LO001` | demonstrate understanding of and use the geometric distribution as a model, including the calculation of probabilities using the geometric distribution | No | Not in lesson evidence | Excluded. |
| `FAS2-DIST-LO004` | understand and use continuous probability distributions, including probability density functions, mean, variance and standard deviation | No | Not in lesson evidence | Excluded. |
| `FAS2-DIST-LO005` | calculate probabilities such as \(P(a<X<b)\), \(E(X)\) and \(\operatorname{Var}(X)\) for a continuous random variable \(X\), where the probability density function is given as a simple function of \(x\) | No | Not in lesson evidence | Excluded. |
| `FAS2-DIST-LO007` | demonstrate understanding of and use the Poisson distribution as a model, including the calculation of probabilities using the Poisson distribution | No | Mentioned only as coming later in transcript | Excluded. |
| `FAS2-DIST-LO008` | use the expressions for the mean and variance of the binomial, geometric and Poisson distributions | No | Not a core part of this lesson | Excluded except bridge reference. |

## 16.2 Evidence Coverage Table

| Evidence item | Covered? | Where covered |
|---|---:|---|
| Game A and Game B motivation | Yes | Big Picture, Core Theory, Worked Examples 1 and 2, Visual Asset Register |
| Discrete random variable definition | Yes | Key Definitions and Notation, Core Theory |
| Fair die distribution table | Yes | Key Definitions, Core Theory, Visual Asset Register |
| \(P(X=x)\) meaning | Yes | Key Definitions and Notation |
| Shorthand \(p(5)\) | Yes | Key Definitions and Notation, Common Mistakes |
| Expected value \(E(X)\) | Yes | Core Theory, Worked Examples, Practice |
| Expected value as long-run mean | Yes | Big Picture, Core Theory, Exam Technique |
| Frequency table bridge | Yes | Prerequisite Recap, Core Theory, Practice Question 4 |
| Symmetry shortcut for expected value | Yes | Core Theory, Worked Example 4, Practice Question 3 |
| Unknown probabilities using \(\sum p=1\) and \(E(X)\) | Yes | Core Theory, Worked Examples 5 and 6, Practice Questions 6 and 8 |
| \(E(2X)\) | Yes | Core Theory, Worked Example 7 |
| \(E(X^2)\) | Yes | Core Theory, Worked Example 8, variance work |
| Variance formula | Yes | Core Theory, Worked Examples 9 and 10 |
| Standard deviation | Yes | Definitions, Worked Example 9, Practice Question 7 |
| Calculator probabilities as frequencies | Yes | Core Theory and Exam Technique, as validation only |
| Linear coding | Yes | Core Theory, Worked Examples 12 and 14 |
| Non-linear coding warning | Yes | Core Theory, Worked Example 13, Common Mistakes |
| Probability inequalities | Yes | Core Theory, Worked Example 11, Practice Questions 2 and 10 |
| Substitution with \(Y=aX+b\) | Yes | Core Theory, Worked Examples 14 and 15, Practice Questions 9 and 10 |

## 16.3 Bridge Coverage Table

| Bridge area | Covered? | How |
|---|---:|---|
| Frequency table mean | Yes | Expected value explained as probability-weighted mean. |
| Ordinary probability laws | Yes | Probability totals and inequality probability selection. |
| Variance and standard deviation | Yes | Ordinary “mean of squares minus square of mean” linked to \(E(X^2)-[E(X)]^2\). |
| Coding of data | Yes | Mean and variance coding extended to random variables. |
| Binomial random variable notation | Lightly | Mentioned as prior familiarity only, not used as a model here. |
| Continuous distributions | No | Deliberately excluded because this lesson is discrete. |

## 16.4 Off-Spec Content Found but Excluded

| Content | Reason excluded from core lesson |
|---|---|
| Continuous probability density functions | These belong to `FAS2-DIST-LO004` and `FAS2-DIST-LO005`, not this discrete random variable lesson. |
| Geometric distribution | This belongs to `FAS2-DIST-LO001`. |
| Poisson distribution | This belongs to `FAS2-DIST-LO007`; the transcript indicates it comes after this chapter. |
| Mean and variance of named distributions such as binomial, geometric and Poisson | These belong to `FAS2-DIST-LO008`, not the table-based DRV foundation here. |
| Full Pearson exercise page content | The slide references exercise pages, but the full textbook pages were not supplied. |
| Cross-board Edexcel mark scheme claims as CCEA evidence | The mathematics is useful, but the source is not CCEA. It is used as supporting practice only. |
| General higher moments such as \(E(X^3)\) as core content | The CCEA core boundary here requires \(E(X)\), \(\operatorname{Var}(X)\), and linear transformations. Higher moments may appear in enrichment-style problem solving but are not taught as core. |
| Cumulative distribution function notation such as \(F(1.5)\) | Mentioned in transcript as crossed out or removed from that old context. Not included as core CCEA content here. |

## 16.5 Optional Enrichment Not Required by CCEA

The following enrichment ideas are useful but not required for the core lesson:

1. Comparing \(E(X^2)\), \(E(X^3)\), and \(E(g(X))\) for general functions.
2. Exploring why \(E(f(X))\ne f(E(X))\) using curved functions.
3. Simulating repeated games to see long-run mean and variance.
4. Comparing two games with the same expected value but different standard deviations.
5. Using matrix inverse methods for three unknown probabilities.
6. Building a distribution table from a piecewise probability function.

## 16.6 Weak Evidence Warnings

| Issue | Warning |
|---|---|
| Screenshot PDF has no parsed text | Only visible/readable previewed details are used. No uninspected diagram or slide detail is claimed. |
| Uploaded source is DrFrost/Edexcel-style FS1, not CCEA | Used only where CCEA FAS2-DIST confirms the content is on-spec. |
| Pearson exercises are referenced but not supplied | No unseen Pearson questions are reproduced. |
| Official CCEA examples are not supplied | Practice questions in this lesson are generated and must not be labelled as CCEA past-paper questions. |
| Calculator instructions are general | No model-specific button sequence is invented. |

## 16.7 Missing Evidence Log

| Missing evidence | Impact |
|---|---|
| Official CCEA question examples for DRVs | Limits CCEA-specific exam phrasing. |
| Official CCEA mark schemes for this exact DRV topic | Mark allocation guidance is inferred from mathematical method, not CCEA mark schemes. |
| Full textbook exercise pages | Prevents exact reproduction of Pearson exercise questions. |
| Fully parsed screenshot PDF | Visual audit is limited to readable preview pages. |
| Topic-specific CCEA teaching notes beyond specification map | Specification boundary is still clear, but detailed CCEA examples are missing. |

---

# 17. Recommended Enhancements Not in the Evidence

The following enhancements are AI-proposed and should be labelled as portal additions, not original evidence content.

## 17.1 Additional Diagrams

1. Distribution Table Anatomy Diagram showing \(X\), \(x\), \(P(X=x)\), \(p(x)\), and \(\sum p=1\).
2. Expected Value Balance Diagram showing outcomes on a horizontal axis with probability weights pulling the centre of mass to \(E(X)\).
3. Variance Spread Diagram comparing two distributions with the same expected value but different spread.
4. Coding Transformation Diagram showing the effect of \(Y=aX+b\) on outcomes, expected value and variance.
5. Endpoint Inequality Selector showing open and closed endpoints for statements like \(P(a<X\leq b)\).

## 17.2 Additional Animations

1. Long-run expected value simulation.
2. Variance comparison animation.
3. Probability total checker.
4. Coding stretch and shift animation.

## 17.3 Additional Widgets

1. DRV Table Builder.
2. Unknown Probability Solver.
3. Variance Step Trainer.
4. Linear Coding Checker.
5. Inequality Outcome Selector.

## 17.4 Additional Examples

1. A probability table where the expected value is negative.
2. A table with fractions only, requiring exact variance.
3. A table with three unknowns, using probability total, \(E(X)\), and \(E(X^2)\).
4. A transformed inequality example involving \(Y=2-5X\).
5. A context example where \(X\) represents profit, requiring conversion from prize to net gain.

---

# 18. Supplementary Sources Used

## 18.1 Project Sources Used

| Source | Role in lesson |
|---|---|
| CCEA GCE Further Mathematics Specification Map | Authoritative unit, topic and LO boundary. |
| Further Maths README Module Map | Project file naming, metadata and asset workflow. |
| Further Maths Evidence Drop Checklist | Evidence validation, missing evidence log and off-spec logging. |
| Ordinary A-Level Maths Bridge Extracts | Bridge context only for probability, statistics, variance and coding. |
| Further Maths Portal Build Knowledge Evidence | Portal build style and self-study lesson-pack workflow. |

## 18.2 Lesson-Specific Evidence Used

| Source | Role in lesson |
|---|---|
| `transcripts.md` | Main source for explanations, worked examples, warnings, teacher phrasing and method flow. |
| `FS1-Chp1-DiscreteRandomVariables.pdf` | Slide source for definitions, formulas, recap structure, expected value, variance, coding and problem-solving examples. |
| `Chapter_1_Discrete_Random_Variables_📊_(Further_Statistics_1)_screenshots.pdf` | Visual evidence source for slide layout, annotations and game motivation, with limitations. |

## 18.3 Cross-Board Sources Used

The uploaded lesson evidence includes DrFrostMaths, Edexcel S1 old references and Pearson exercise references. These are not CCEA authority. They are used only because the mathematical content aligns with the CCEA Further Mathematics specification boundary for discrete probability distributions, \(E(X)\), \(E(X^2)\), \(\operatorname{Var}(X)\), probability intervals and linear coding.

Cross-board examples must not be labelled as CCEA past-paper questions.

## 18.4 Ordinary A-Level Maths Sources Used

Ordinary A-Level Mathematics sources are used only as bridge context. They support probability totals, frequency table means, variance and standard deviation, coding of data, and random variable notation from distribution work. They do not override the CCEA Further Mathematics specification.

## 18.5 Evidence Limitations

1. The screenshot PDF had no parsed text.
2. Only visible previewed screenshot details are used.
3. No complete Pearson exercise pages were supplied.
4. No official CCEA past-paper questions or mark schemes were supplied for this exact lesson.
5. Some examples come from cross-board evidence and are therefore marked as supporting examples, not CCEA exam evidence.
6. Continuous random variables, geometric distribution and Poisson distribution are outside this lesson boundary and are excluded.

---

# 19. Final Student Checklist

## 19.1 Prerequisite Confidence Checklist

You are ready for this lesson if you can:

- [ ] add probabilities and check they total \(1\);
- [ ] calculate a mean from a frequency table;
- [ ] solve two simultaneous linear equations;
- [ ] square negative numbers correctly;
- [ ] use inequalities such as \(1<X\leq3\);
- [ ] calculate a variance using mean of squares minus square of mean;
- [ ] understand that standard deviation is the square root of variance;
- [ ] handle simple linear coding such as \(Y=3X-2\).

## 19.2 Further Maths Method Checklist

You can handle discrete random variables if you can:

- [ ] define the random variable \(X\);
- [ ] identify possible values \(x\);
- [ ] read \(P(X=x)\) correctly;
- [ ] explain the difference between \(X\) and \(x\);
- [ ] check \(\sum P(X=x)=1\);
- [ ] calculate \(E(X)=\sum xP(X=x)\);
- [ ] calculate \(E(X^2)=\sum x^2P(X=x)\);
- [ ] calculate \(\operatorname{Var}(X)=E(X^2)-[E(X)]^2\);
- [ ] calculate \(\sigma_X=\sqrt{\operatorname{Var}(X)}\);
- [ ] solve for unknown probabilities using probability total and expected value;
- [ ] select outcomes satisfying probability inequalities;
- [ ] use \(E(aX+b)=aE(X)+b\);
- [ ] use \(\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)\).

## 19.3 Exam Technique Checklist

In an exam solution, remember to:

- [ ] write the formula before substituting;
- [ ] show products such as \(xP(X=x)\);
- [ ] show an \(x^2\) row or equivalent working before variance;
- [ ] avoid rounding too early;
- [ ] keep exact fractions when possible;
- [ ] state final probabilities as decimals or fractions consistently;
- [ ] include units or context where relevant;
- [ ] not call cross-board practice CCEA past-paper evidence;
- [ ] check variance is not negative;
- [ ] check probabilities are between \(0\) and \(1\);
- [ ] check probabilities add to \(1\).

## 19.4 Bridge Checklist

You have connected this lesson to ordinary A-Level Maths if you understand that:

- [ ] expected value is like a frequency-table mean;
- [ ] probabilities behave like relative frequencies;
- [ ] \(E(X)\) is a long-run average, not necessarily an outcome;
- [ ] variance is still “mean of squares minus square of mean”;
- [ ] coding rules for mean and variance still work for linear transformations;
- [ ] non-linear transformations do not use the same shortcut;
- [ ] binomial distribution is a named model, while this lesson often gives a custom table directly.

## 19.5 Diagram and Visual Understanding Checklist

You should be able to explain:

- [ ] what each row in a probability distribution table means;
- [ ] why a fair die table has six probabilities of \(\frac16\);
- [ ] why Game A and Game B can have the same expected value but different spread;
- [ ] why the \(x^2\) row is needed for variance;
- [ ] how a coding \(Y=aX+b\) changes outcomes;
- [ ] why adding \(b\) changes the expected value but not the variance;
- [ ] why multiplying by \(a\) changes variance by \(a^2\);
- [ ] which outcomes are included in inequalities such as \(P(a<X\leq b)\).

## 19.6 Final “Can I Do This?” Questions

1. What does \(P(X=x)\) mean?
2. Why must probabilities in a discrete distribution add to \(1\)?
3. How do you calculate \(E(X)\)?
4. Why is \(E(X)\) not always a possible value of \(X\)?
5. How do you calculate \(E(X^2)\)?
6. Why is \(E(X^2)\) usually not equal to \([E(X)]^2\)?
7. What formula gives \(\operatorname{Var}(X)\)?
8. How do you calculate standard deviation from variance?
9. What happens to \(E(X)\) under the coding \(aX+b\)?
10. What happens to \(\operatorname{Var}(X)\) under the coding \(aX+b\)?
11. Why does the \(+b\) not affect variance?
12. How do you solve \(P(X>Y)\) if \(Y\) is defined in terms of \(X\)?
