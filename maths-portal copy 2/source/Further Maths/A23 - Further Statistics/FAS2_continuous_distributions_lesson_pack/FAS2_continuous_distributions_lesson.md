# 1. Lesson Title and Metadata

| Field | Value |
|---|---|
| Lesson title | Continuous Distributions |
| Date generated | 2026-06-05 |
| Course | CCEA GCE Further Mathematics |
| Unit | `FAS2`: Further AS 2 Applied Mathematics |
| Applied section | Section C: Statistics |
| Topic code | `FAS2-DIST` |
| Topic area | Statistical distributions |
| Topic slug | `continuous_distributions` |
| Topic Pascal | `ContinuousDistributions` |
| Topic ID | `FAS2ContinuousDistributions` |
| Lesson file | `FAS2_continuous_distributions_lesson.md` |
| Core LO IDs | `FAS2-DIST-LO004`, `FAS2-DIST-LO005`, `FAS2-DIST-LO006` |
| Bridge/prerequisite LO IDs | `FAS2-DIST-LO002`, `FAS2-DIST-LO003` |
| Ordinary Maths bridge tags | `#AS2Statistics`, `#A22NormalDistribution`, `#Integration`, `#Histograms`, `#Probability` |
| Topic tags | `#FAS2`, `#Statistics`, `#ContinuousDistributions`, `#PDF`, `#CDF`, `#Mean`, `#Variance`, `#UniformDistribution`, `#AreaUnderCurve` |

## Source boundary statement

This lesson is built for **CCEA FAS2 Statistical distributions**. The uploaded DrFrost/Pearson FS2 Chapter 3 material is used as lesson-specific evidence only where it matches the CCEA Further Mathematics specification boundary. Pearson-only enrichment such as mode, median, quartiles, percentiles, skewness and some A2 integration-by-parts modelling examples is logged later as enrichment or excluded from the core lesson.

# 2. Evidence Map

| Evidence ID | Source | Evidence type | Lesson use |
|---|---|---|---|
| E1 | CCEA GCE Further Mathematics Specification Map | Specification map | Official unit, topic code, LO IDs and syllabus boundary. |
| E2 | Further Maths README module map | Project module map | Confirms `FAS2-DIST` and ordinary bridge route. |
| E3 | Further Maths Evidence Drop Checklist | Project checklist | Controls missing evidence, visual evidence and off-spec logging. |
| E4 | Ordinary A-Level Maths Bridge Spec Extracts | Bridge map | Provides ordinary Maths context only. |
| E5 | `FS2-Chp3-ContinuousDistributions.pdf` | Cross-board PDF/slides | Used for p.d.f., CDF, mean/variance and uniform distribution evidence, filtered through CCEA. |
| E6 | `transcripts.md` | Teacher transcript | Used for explanation style, warnings and worked-example detail, filtered through CCEA. |
| E7 | `Chapter_3_Continuous_Distributions_📈_(Further_Statistics_2)_screenshots.pdf` | Visual evidence | Used only for inspected visual details such as shaded area, handwritten area annotations and comparison diagrams. No uninspected detail is claimed. |

## Evidence-backed teaching details to preserve

- For a discrete distribution, `p(x)` is the probability of a particular outcome, and the probabilities add to 1.
- For a continuous distribution, the probability of a single exact value is 0.
- For a continuous distribution, probability is represented by **area under the graph**, not height.
- The vertical axis is probability density, `f(x)`, not probability.
- The total area under the p.d.f. is 1.
- Integration is the continuous version of summation.
- When finding a CDF, use a dummy variable such as `t` if `x` appears as a limit.
- In continuous distributions, inclusive and strict inequalities give the same probability at endpoints.
- Do not confuse `p(x)`, `f(x)` and `F(x)`.

# 3. Specification Alignment

| LO ID | Official wording | Lesson coverage | Evidence source | Syllabus boundary | Ordinary A-Level Maths bridge |
|---|---|---|---|---|---|
| `FAS2-DIST-LO004` | understand and use continuous probability distributions, including probability density functions, mean, variance and standard deviation | Defines continuous random variables, p.d.f.s, total area, probability as area, CDF link, mean and variance | E1, E5, E6 | Core | Histograms, normal distribution, integration |
| `FAS2-DIST-LO005` | calculate probabilities such as `P(a<X<b)`, `E(X)` and `Var(X)` for a continuous random variable `X`, where the probability density function is given as a simple function of `x` | Works through normalising `f(x)`, calculating interval probabilities, expectation and variance | E1, E5, E6 | Core, simple functions only | Definite integrals and area under curves |
| `FAS2-DIST-LO006` | understand and use the expressions for `E(aX+b)` and `Var(aX+b)`, where `X` is a discrete or continuous random variable | Applies linear transformation rules to continuous random variables | E1, E5, E6 | Core | Coding transformations from statistics |
| `FAS2-DIST-LO002` | demonstrate understanding of and use discrete probability distributions, including probability functions, mean, variance and standard deviation | Used as recap only | E1, E5, E6 | Bridge/prerequisite | Discrete random variables and binomial |
| `FAS2-DIST-LO003` | calculate probabilities such as `P(a≤X≤b)`, `E(X)` and `Var(X)` for simple cases of a discrete random variable `X` | Used to compare summation and integration | E1, E5, E6 | Bridge/prerequisite | Summation notation and expectation |

# 4. Learning Objectives

## Core Further Maths objectives

By the end of this lesson, you should be able to:

1. Distinguish between a discrete random variable and a continuous random variable.
2. Explain why \(P(X=x)=0\) for a continuous random variable.
3. Interpret \(f(x)\) as a probability density function, not as a probability.
4. Use \(f(x)\geq0\) and \(\int_{-\infty}^{\infty}f(x)\,dx=1\) to check or normalise a p.d.f.
5. Calculate interval probabilities using \(P(a<X<b)=\int_a^b f(x)\,dx\).
6. Find or use \(F(x)=P(X\leq x)=\int_{-\infty}^{x}f(t)\,dt\).
7. Recover a p.d.f. from a CDF using \(f(x)=F'(x)\) on the relevant interval.
8. Calculate \(E(X)=\int x f(x)\,dx\), \(E(X^2)=\int x^2f(x)\,dx\), \(\operatorname{Var}(X)=E(X^2)-[E(X)]^2\), and \(\sigma=\sqrt{\operatorname{Var}(X)}\).
9. Use \(E(aX+b)=aE(X)+b\) and \(\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)\).
10. Handle a continuous uniform distribution as a simple p.d.f. model when appropriate.

## Bridge objectives

You should be able to explain how \(\sum p(x)=1\) becomes \(\int f(x)\,dx=1\), how histogram frequency density prepares you for probability density, and why ordinary definite integration is now being used as a probability machine.

## Exam technique objectives

Define `X` clearly, use exact fractions unless decimals are required, use the support of the p.d.f. as integration limits, avoid rounding continuous endpoints as if `X` were discrete, and check total area before using a p.d.f.

# 5. Explicit Prerequisite Recap

## GCSE foundations

You should already be comfortable with area under straight-line graphs and curves, rectangles, triangles and trapezia, histograms, intervals, and solving simple equations.

## Ordinary AS/A2 Mathematics foundations

You need definite integration as area under a curve, basic differentiation, function notation, probability notation such as \(P(X\leq x)\), and normal distribution intuition that continuous probabilities come from areas over intervals.

## Previous Further Mathematics foundations

This lesson grows from the discrete part of `FAS2-DIST`: probability functions \(p(x)\), \(\sum p(x)=1\), expectation, variance, and transformations of random variables.

### A-Level Maths Bridge: What You Already Know and What Further Maths Changes

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| GCSE histograms and ordinary statistics | The vertical axis can be frequency density, and area gives frequency | The vertical axis becomes probability density \(f(x)\), and area gives probability | Do not read \(f(x)\) as \(P(X=x)\). Density is not probability. |
| AS1 Integration | \(\int_a^b y\,dx\) gives area under a curve | \(\int_a^b f(x)\,dx\) gives \(P(a<X<b)\) | The limits must match the range where the p.d.f. is non-zero. |
| AS/A2 Differentiation | Differentiation reverses integration | \(f(x)=F'(x)\) recovers the p.d.f. from the CDF | Differentiate only the active interval expression, then state zero otherwise where appropriate. |
| AS2 Probability and distributions | Discrete probabilities can be attached to exact outcomes | Continuous random variables need ranges; \(P(X=x)=0\) | Do not use discrete endpoint corrections or rounding habits. |
| A22 Normal Distribution bridge | Areas under a smooth curve represent probabilities | General continuous distributions use a supplied p.d.f. rather than a normal table only | A smooth curve is not automatically normal. |

In ordinary A-Level Maths, this idea appeared as **area under a curve**, **histogram density**, and **normal distribution area**. In Further Maths, the same idea becomes a general machine: a supplied function \(f(x)\) describes probability density, and integration extracts probability from it. The key upgrade is that probability is no longer the height of a bar or a table entry. It is the area accumulated across an interval. The danger is trying to treat \(f(7)\) like \(P(X=7)\).

# 6. Big Picture Explanation

Continuous distributions are the smooth-curve version of probability distributions. In a discrete distribution, probability sits on separate outcomes. You can ask for \(P(X=10)\), and that can be a real non-zero probability. In a continuous distribution, the random variable can take any value in an interval, so a single exact value has no width. That means a single exact value has zero probability.

The key idea is:

\[
\boxed{\text{In a continuous distribution, probability is area.}}
\]

So instead of asking \(P(X=7)\), we ask for \(P(6<X<9)\). The vertical axis is probability density \(f(x)\), not probability. Integration is the continuous version of summation. In discrete distributions, we add probabilities:

\[
\sum p(x)=1.
\]

In continuous distributions, we integrate probability density:

\[
\int_{-\infty}^{\infty} f(x)\,dx=1.
\]

A small but dangerous notation goblin lives here: \(p(x)\), \(f(x)\), and \(F(x)\) are **not** interchangeable.

# 7. Key Definitions and Notation

## 7.1 Random variable

A random variable is a variable whose value depends on the outcome of a random process. We usually use a capital letter, such as \(X\), for the random variable, and a lower-case letter, such as \(x\), for a possible value.

## 7.2 Discrete random variable

A random variable \(X\) is discrete if its possible outcomes are separate values, usually countable values. For a discrete random variable:

\[
p(x)=P(X=x),\quad p(x)\geq0,\quad \sum p(x)=1.
\]

## 7.3 Continuous random variable

A random variable \(X\) is continuous if its possible outcomes form a continuum of values, usually values in an interval. For any exact value \(a\),

\[
\boxed{P(X=a)=0.}
\]

This does not mean that values near \(a\) are impossible. It means that a single exact point has no width, so the area at that point is zero.

## 7.4 Probability density function, \(f(x)\)

A probability density function, or p.d.f., is a function \(f(x)\) that describes how probability is distributed across a continuous range. For a continuous random variable \(X\):

\[
\boxed{f(x)\geq 0},\qquad \boxed{\int_{-\infty}^{\infty} f(x)\,dx=1.}
\]

## 7.5 Probability over an interval

\[
\boxed{P(a<X<b)=\int_a^b f(x)\,dx.}
\]

Because endpoint probabilities are zero,

\[
P(a<X<b)=P(a\leq X<b)=P(a<X\leq b)=P(a\leq X\leq b).
\]

## 7.6 Cumulative distribution function, \(F(x)\)

\[
\boxed{F(x)=P(X\leq x)=\int_{-\infty}^{x}f(t)\,dt.}
\]

The dummy variable \(t\) avoids confusing the integration variable with the upper limit \(x\).

## 7.7 Recovering \(f(x)\) from \(F(x)\)

\[
\boxed{f(x)=\frac{d}{dx}F(x).}
\]

## 7.8 Mean, variance and standard deviation

\[
\boxed{E(X)=\mu=\int_{-\infty}^{\infty}x f(x)\,dx.}
\]

\[
\boxed{E(X^2)=\int_{-\infty}^{\infty}x^2 f(x)\,dx.}
\]

\[
\boxed{\operatorname{Var}(X)=E(X^2)-[E(X)]^2.}
\]

\[
\boxed{\sigma=\sqrt{\operatorname{Var}(X)}.}
\]

## 7.9 Linear transformation of a random variable

If \(Y=aX+b\), then:

\[
\boxed{E(aX+b)=aE(X)+b}
\]

and

\[
\boxed{\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X).}
\]

# 8. Core Theory

## 8.1 Discrete distributions as the launchpad

For a discrete random variable \(X\), each possible value can have a probability attached directly to it. For example, if \(X\sim\operatorname{Bin}(15,0.8)\), possible values are \(0,1,2,\ldots,15\), and \(p(10)=P(X=10)\) can be non-zero. The three big discrete facts are:

\[
p(x)=P(X=x),\quad p(x)\geq0,\quad \sum p(x)=1.
\]

**Bridge Note:** In ordinary A-Level Maths and earlier Further Statistics, you used tables or bars for discrete random variables. Here, Further Maths trades summation for integration.

## 8.2 Continuous distributions: why exact-value probabilities are zero

If \(X\) is continuous, then \(P(X=7)=0\). A single point has no width. Since probability is area, and a line of zero width has zero area,

\[
P(X=7)=0.
\]

Therefore we work with intervals such as:

\[
P(6<X<9),\quad P(2.5<X<3.5),\quad P(a<X<b).
\]

**Bridge Note:** In the normal distribution from ordinary A-Level Maths, you already used probabilities over intervals. Further Maths now generalises that idea using any supplied p.d.f. \(f(x)\), not only the normal curve.

## 8.3 Probability density is not probability

For a continuous random variable, \(f(x)\) is a probability density function. It is not true that \(f(x)=P(X=x)\). In fact, for a continuous random variable, \(P(X=x)=0\), but \(f(x)\) may be positive.

**Exam warning:** If your answer to a continuous probability question is just a value of \(f(x)\), you have almost certainly given a height when the examiner wants an area.

## 8.4 The histogram bridge: why the word density appears

In a histogram, the vertical axis is frequency density, not frequency:

\[
\text{frequency}=\text{class width}\times\text{frequency density}.
\]

Continuous probability works similarly:

\[
\text{probability}=\text{area under the density curve}.
\]

For a curve:

\[
P(a<X<b)=\int_a^b f(x)\,dx.
\]

## 8.5 Conditions for a valid p.d.f.

Let \(X\) be a continuous random variable with p.d.f. \(f(x)\). A valid p.d.f. must satisfy:

\[
\boxed{f(x)\geq 0 \quad \text{for all }x}
\]

and

\[
\boxed{\int_{-\infty}^{\infty}f(x)\,dx=1.}
\]

If

\[
f(x)=\begin{cases}g(x),&a\leq x\leq b,\\0,&\text{otherwise},\end{cases}
\]

then the total-area condition is:

\[
\int_a^b g(x)\,dx=1.
\]

## 8.6 Normalising a p.d.f.: finding \(k\)

A common question gives a p.d.f. with an unknown constant \(k\). The method is:

1. Identify the support where \(f(x)\ne0\).
2. Integrate \(f(x)\) over that support.
3. Set the integral equal to 1.
4. Solve for \(k\).
5. Check \(f(x)\geq0\) on the support.

### Evidence example: \(f(x)=kx(4-x)\), \(2\leq x\leq4\)

\[
f(x)=\begin{cases}kx(4-x),&2\leq x\leq4,\\0,&\text{otherwise}.\end{cases}
\]

Total probability is 1:

\[
\int_2^4 kx(4-x)\,dx=1.
\]

Expand:

\[
x(4-x)=4x-x^2.
\]

So:

\[
k\int_2^4(4x-x^2)\,dx=1.
\]

Integrate:

\[
\int(4x-x^2)\,dx=2x^2-\frac{x^3}{3}.
\]

Therefore:

\[
k\left[2x^2-\frac{x^3}{3}\right]_2^4=1.
\]

At \(x=4\):

\[
2(4)^2-\frac{4^3}{3}=32-\frac{64}{3}=\frac{32}{3}.
\]

At \(x=2\):

\[
2(2)^2-\frac{2^3}{3}=8-\frac{8}{3}=\frac{16}{3}.
\]

Subtract:

\[
\frac{32}{3}-\frac{16}{3}=\frac{16}{3}.
\]

So:

\[
k\cdot\frac{16}{3}=1,
\]

hence:

\[
\boxed{k=\frac{3}{16}.}
\]

The sketch is the right half of the downward parabola

\[
f(x)=\frac{3}{16}x(4-x)
\]

on \(2\leq x\leq4\), with \((2,\frac34)\) and \((4,0)\) marked, and \(f(x)=0\) outside the support.

## 8.7 Calculating interval probabilities from a p.d.f.

Once \(f(x)\) is known, interval probabilities are areas:

\[
P(a<X<b)=\int_a^b f(x)\,dx.
\]

Using the previous p.d.f.,

\[
P(2.5<X<3.5)=\int_{5/2}^{7/2}\frac{3}{16}x(4-x)\,dx.
\]

Expand and integrate:

\[
P\left(\frac52<X<\frac72\right)=\frac{3}{16}\left[2x^2-\frac{x^3}{3}\right]_{5/2}^{7/2}.
\]

At \(x=\frac72\):

\[
2\left(\frac72\right)^2-\frac{(\frac72)^3}{3}=\frac{245}{24}.
\]

At \(x=\frac52\):

\[
2\left(\frac52\right)^2-\frac{(\frac52)^3}{3}=\frac{175}{24}.
\]

Subtract:

\[
\frac{245}{24}-\frac{175}{24}=\frac{70}{24}=\frac{35}{12}.
\]

Multiply:

\[
\frac{3}{16}\cdot\frac{35}{12}=\frac{105}{192}=\frac{35}{64}.
\]

So:

\[
\boxed{P(2.5<X<3.5)=\frac{35}{64}.}
\]

## 8.8 Endpoint signs do not affect continuous probabilities

For a continuous random variable:

\[
P(X=a)=0.
\]

Therefore:

\[
P(a<X<b)=P(a\leq X\leq b).
\]

## 8.9 Piecewise p.d.f.s

For

\[
f(x)=\begin{cases}k,&1\leq x<2,\\k(x-1),&2\leq x\leq4,\\0,&\text{otherwise},\end{cases}
\]

use areas. First part: rectangle width 1, height \(k\), area \(k\). Second part: trapezium with vertical sides \(k\) and \(3k\), width 2:

\[
\frac12(k+3k)(2)=4k.
\]

Total:

\[
k+4k=1\Rightarrow5k=1\Rightarrow\boxed{k=\frac15}.
\]

For \(P(X>3)\):

\[
P(X>3)=\int_3^4\frac15(x-1)\,dx=\frac15\left[\frac{x^2}{2}-x\right]_3^4=\frac12.
\]

## 8.10 Cumulative distribution function

The cumulative distribution function is:

\[
F(x)=P(X\leq x).
\]

For a continuous random variable:

\[
F(x)=\int_{-\infty}^{x}f(t)\,dt.
\]

A CDF usually has three pieces:

\[
F(x)=0 \text{ below the support},\quad F(x)=\text{integrated expression on the support},\quad F(x)=1 \text{ above the support}.
\]

## 8.11 Finding \(F(x)\) from a simple p.d.f.

Let

\[
f(x)=\begin{cases}\frac14x,&1\leq x\leq3,\\0,&\text{otherwise}.\end{cases}
\]

For \(x<1\), \(F(x)=0\). For \(1\leq x\leq3\):

\[
F(x)=\int_1^x\frac14t\,dt=\left[\frac{t^2}{8}\right]_1^x=\frac{x^2}{8}-\frac18.
\]

For \(x>3\), \(F(x)=1\). Therefore:

\[
\boxed{F(x)=\begin{cases}0,&x<1,\\\frac{x^2}{8}-\frac18,&1\leq x\leq3,\\1,&x>3.\end{cases}}
\]

## 8.12 Alternative method: indefinite integration plus boundary condition

Integrate indefinitely:

\[
F(x)=\int\frac14x\,dx=\frac{x^2}{8}+C.
\]

Use \(F(1)=0\):

\[
0=\frac18+C\Rightarrow C=-\frac18.
\]

So again:

\[
F(x)=\frac{x^2}{8}-\frac18.
\]

## 8.13 CDFs with multiple intervals

For

\[
f(x)=\begin{cases}\frac15,&1\leq x<2,\\\frac15(x-1),&2\leq x\leq4,\\0,&\text{otherwise},\end{cases}
\]

we get:

\[
F(x)=\begin{cases}
0,&x<1,\\
\frac{x}{5}-\frac15,&1\leq x<2,\\
\frac{x^2}{10}-\frac{x}{5}+\frac15,&2\leq x\leq4,\\
1,&x>4.
\end{cases}
\]

The key step for \(2\leq x\leq4\) is:

\[
F(x)=F(2)+\int_2^x\frac15(t-1)\,dt.
\]

## 8.14 Recovering \(f(x)\) from \(F(x)\)

If

\[
F(x)=\begin{cases}0,&x<0,\\\frac15x+\frac{3}{20}x^2,&0\leq x\leq2,\\1,&x>2,\end{cases}
\]

then on \(0\leq x\leq2\):

\[
f(x)=F'(x)=\frac15+\frac{3}{10}x.
\]

So:

\[
\boxed{f(x)=\begin{cases}\frac15+\frac{3}{10}x,&0\leq x\leq2,\\0,&\text{otherwise}.\end{cases}}
\]

## 8.15 Using a CDF to calculate probabilities

\[
P(X\leq a)=F(a),\qquad P(a\leq X\leq b)=F(b)-F(a).
\]

Using the CDF above:

\[
F(1.5)=\frac15(1.5)+\frac{3}{20}(1.5)^2=0.6375.
\]

\[
F(0.5)=\frac15(0.5)+\frac{3}{20}(0.5)^2=0.1375.
\]

So:

\[
P(0.5\leq X\leq1.5)=0.6375-0.1375=0.5.
\]

And:

\[
P(X=1)=0.
\]

## 8.16 Mean and variance of a continuous random variable

For a discrete random variable:

\[
E(X)=\sum x p(x).
\]

For a continuous random variable:

\[
E(X)=\int x f(x)\,dx.
\]

For

\[
f(x)=\begin{cases}\frac14x,&1\leq x\leq3,\\0,&\text{otherwise},\end{cases}
\]

we have:

\[
E(X)=\int_1^3x\cdot\frac14x\,dx=\int_1^3\frac14x^2\,dx=\left[\frac{x^3}{12}\right]_1^3=\frac{13}{6}.
\]

Then:

\[
E(X^2)=\int_1^3x^2\cdot\frac14x\,dx=\int_1^3\frac14x^3\,dx=\left[\frac{x^4}{16}\right]_1^3=5.
\]

So:

\[
\operatorname{Var}(X)=5-\left(\frac{13}{6}\right)^2=\frac{11}{36},\qquad \sigma=\frac{\sqrt{11}}{6}.
\]

## 8.17 Linear transformations

If \(Y=aX+b\), then:

\[
E(Y)=aE(X)+b,
\]

and

\[
\operatorname{Var}(Y)=a^2\operatorname{Var}(X).
\]

Using \(E(X)=\frac{13}{6}\), \(\operatorname{Var}(X)=\frac{11}{36}\):

\[
E(2X-3)=2\left(\frac{13}{6}\right)-3=\frac43,
\]

and

\[
\operatorname{Var}(2X-3)=2^2\cdot\frac{11}{36}=\frac{11}{9}.
\]

## 8.18 Continuous uniform distribution

If \(X\sim U[a,b]\), then:

\[
f(x)=\begin{cases}\frac{1}{b-a},&a\leq x\leq b,\\0,&\text{otherwise}.\end{cases}
\]

For \(a\leq c<d\leq b\):

\[
P(c<X<d)=\frac{d-c}{b-a}.
\]

For example, if \(X\sim U[3,5]\), then:

\[
P(3.2<X<4.3)=\frac{4.3-3.2}{5-3}=0.55.
\]

Also:

\[
E(X)=\frac{a+b}{2},\qquad \operatorname{Var}(X)=\frac{(b-a)^2}{12}.
\]

### Derivation of \(E(X)\)

\[
E(X)=\int_a^b x\cdot\frac{1}{b-a}\,dx=\frac{1}{b-a}\left[\frac{x^2}{2}\right]_a^b=\frac{b^2-a^2}{2(b-a)}=\frac{a+b}{2}.
\]

### Derivation of \(\operatorname{Var}(X)\)

\[
E(X^2)=\int_a^b x^2\cdot\frac{1}{b-a}\,dx=\frac{1}{b-a}\left[\frac{x^3}{3}\right]_a^b=\frac{a^2+ab+b^2}{3}.
\]

Then:

\[
\operatorname{Var}(X)=\frac{a^2+ab+b^2}{3}-\left(\frac{a+b}{2}\right)^2=\frac{(b-a)^2}{12}.
\]

## 8.19 Continuous distribution modelling assumptions

When a question uses a continuous distribution as a model, the assumptions must match the context. Common assumptions include: the variable can reasonably be treated as continuous, exact point probabilities are zero, probabilities are represented by areas over intervals, the p.d.f. is non-negative and has total area 1, and values outside the support have density zero.

# 9. Visual Asset Integration

[VISUAL PLACEHOLDER: FAS2ContinuousDistributionsMermaid-001 | Source: CCEA FAS2-DIST specification boundary + DrFrost/Pearson Chapter 3 lesson evidence | Insert from mermaid/FAS2ContinuousDistributionsMermaid-001.md | Purpose: Show the learning route from discrete distributions to continuous p.d.f.s, CDFs, mean, variance and transformation rules.]

[VISUAL PLACEHOLDER: FAS2ContinuousDistributionsSVG-001 | Source: DrFrost/Pearson FS2 PDF page 4 and transcript discussion of discrete versus continuous distributions | Insert from svg/FAS2ContinuousDistributionsSVG-001.svg | Purpose: Compare a discrete random variable displayed as bars with a continuous random variable displayed as a smooth p.d.f. curve.]

[VISUAL PLACEHOLDER: FAS2ContinuousDistributionsSVG-002 | Source: Screenshot PDF visible pages 5–15 + transcript explanation of `P(6<X<9)=0.66` | Insert from svg/FAS2ContinuousDistributionsSVG-002.svg | Purpose: Show that interval probability is shaded area under the p.d.f. between two `x`-values, not the curve height.]

[VISUAL PLACEHOLDER: FAS2ContinuousDistributionsBridgeSVG-001 | Source: Ordinary A-Level Maths bridge + DrFrost/Pearson p.d.f. slide | Insert from svg/FAS2ContinuousDistributionsBridgeSVG-001.svg | Purpose: Compare histogram frequency density with probability density and show why “density” appears in p.d.f.]

[VISUAL PLACEHOLDER: FAS2ContinuousDistributionsTikZ-001 | Source: DrFrost/Pearson p.d.f. worked example `f(x)=kx(4-x)`, `2≤x≤4` | Insert from tikz/FAS2ContinuousDistributionsTikZ-001.tex | Purpose: Sketch the p.d.f. after finding `k=3/16`, showing the active support only.]

[VISUAL PLACEHOLDER: FAS2ContinuousDistributionsTikZ-002 | Source: DrFrost/Pearson CDF slide and transcript explanation | Insert from tikz/FAS2ContinuousDistributionsTikZ-002.tex | Purpose: Show `F(x)` as accumulated area from the lower support up to `x`.]

[VISUAL PLACEHOLDER: FAS2ContinuousDistributionsSVG-003 | Source: DrFrost/Pearson continuous uniform distribution section + CCEA FAS2-DIST simple p.d.f. boundary | Insert from svg/FAS2ContinuousDistributionsSVG-003.svg | Purpose: Show a uniform p.d.f. as a rectangle with height `1/(b-a)`, total area 1 and interval probability as a sub-rectangle.]

[VISUAL PLACEHOLDER: FAS2ContinuousDistributionsSVG-004 | Source: CCEA FAS2-DIST-LO006 + lesson theory | Insert from svg/FAS2ContinuousDistributionsSVG-004.svg | Purpose: Show how `Y=aX+b` changes mean and variance.]

# 10. Interactive Learning Widgets

[INTERACTIVE PLACEHOLDER: FAS2ContinuousDistributionsWidget-001 | Source: AI-proposed teaching enhancement based on CCEA FAS2-DIST + DrFrost/Pearson p.d.f. normalisation examples | Insert from widgets/FAS2ContinuousDistributionsWidget-001.html | Purpose: Let the student find `k` by enforcing total area `=1`.]

[INTERACTIVE PLACEHOLDER: FAS2ContinuousDistributionsWidget-002 | Source: AI-proposed teaching enhancement based on CDF evidence and `F(x)=∫f(t)dt` | Insert from widgets/FAS2ContinuousDistributionsWidget-002.html | Purpose: Help the student build a piecewise CDF from a p.d.f. and understand accumulation.]

[INTERACTIVE PLACEHOLDER: FAS2ContinuousDistributionsWidget-003 | Source: AI-proposed teaching enhancement based on continuous uniform p.d.f. evidence and CCEA simple continuous distribution boundary | Insert from widgets/FAS2ContinuousDistributionsWidget-003.html | Purpose: Let the student explore rectangular area probabilities and mean/variance for `X~U[a,b]`.]

[INTERACTIVE PLACEHOLDER: FAS2ContinuousDistributionsWidget-004 | Source: AI-proposed teaching enhancement based on transcript warning not to confuse `p(x)`, `f(x)` and `F(x)` | Insert from widgets/FAS2ContinuousDistributionsWidget-004.html | Purpose: Train notation recognition for discrete probability, p.d.f. and CDF.]

# 11. Worked Examples

## Worked Example 1: Find `k` and sketch a p.d.f.

The random variable \(X\) has probability density function:

\[
f(x)=\begin{cases}kx(4-x),&2\leq x\leq4,\\0,&\text{otherwise}.\end{cases}
\]

For a valid p.d.f.:

\[
\int_2^4kx(4-x)\,dx=1.
\]

Expand and integrate:

\[
k\int_2^4(4x-x^2)\,dx=1,
\]

\[
k\left[2x^2-\frac{x^3}{3}\right]_2^4=1.
\]

At \(x=4\):

\[
32-\frac{64}{3}=\frac{32}{3}.
\]

At \(x=2\):

\[
8-\frac83=\frac{16}{3}.
\]

So:

\[
k\left(\frac{16}{3}\right)=1\Rightarrow\boxed{k=\frac{3}{16}}.
\]

The sketch uses only \(2\leq x\leq4\). The underlying quadratic has roots \(0\) and \(4\), symmetry at \(x=2\), and the p.d.f. falls from \((2,\frac34)\) to \((4,0)\).

## Worked Example 2: Piecewise p.d.f. using areas and integration

\[
f(x)=\begin{cases}k,&1\leq x<2,\\k(x-1),&2\leq x\leq4,\\0,&\text{otherwise}.\end{cases}
\]

First area:

\[
(2-1)k=k.
\]

Second area is a trapezium:

\[
\frac12(k+3k)(2)=4k.
\]

Total:

\[
k+4k=1\Rightarrow\boxed{k=\frac15}.
\]

Then:

\[
P(X>3)=\int_3^4\frac15(x-1)\,dx=\frac12.
\]

## Worked Example 3: Find a CDF from a p.d.f.

\[
f(x)=\begin{cases}\frac14x,&1\leq x\leq3,\\0,&\text{otherwise}.\end{cases}
\]

For \(x<1\), \(F(x)=0\). For \(1\leq x\leq3\):

\[
F(x)=\int_1^x\frac14t\,dt=\left[\frac{t^2}{8}\right]_1^x=\frac{x^2}{8}-\frac18.
\]

For \(x>3\), \(F(x)=1\). Hence:

\[
\boxed{F(x)=\begin{cases}0,&x<1,\\\frac{x^2-1}{8},&1\leq x\leq3,\\1,&x>3.\end{cases}}
\]

## Worked Example 4: Multiple-interval CDF

For

\[
f(x)=\begin{cases}\frac15,&1\leq x<2,\\\frac15(x-1),&2\leq x\leq4,\\0,&\text{otherwise},\end{cases}
\]

\[
F(x)=\begin{cases}0,&x<1,\\\frac{x}{5}-\frac15,&1\leq x<2,\\\frac{x^2}{10}-\frac{x}{5}+\frac15,&2\leq x\leq4,\\1,&x>4.\end{cases}
\]

The key step is:

\[
F(x)=F(2)+\int_2^x\frac15(t-1)\,dt.
\]

## Worked Example 5: Use a CDF and recover the p.d.f.

\[
F(x)=\begin{cases}0,&x<0,\\\frac15x+\frac{3}{20}x^2,&0\leq x\leq2,\\1,&x>2.\end{cases}
\]

\[
P(X\leq1.5)=F(1.5)=0.6375.
\]

\[
P(0.5\leq X\leq1.5)=F(1.5)-F(0.5)=0.5.
\]

\[
P(X=1)=0.
\]

Differentiate on \(0\leq x\leq2\):

\[
f(x)=\frac15+\frac{3}{10}x.
\]

So:

\[
\boxed{f(x)=\begin{cases}\frac15+\frac{3}{10}x,&0\leq x\leq2,\\0,&\text{otherwise}.\end{cases}}
\]

## Worked Example 6: Mean, variance and a transformation

For

\[
f(x)=\begin{cases}\frac14x,&1\leq x\leq3,\\0,&\text{otherwise},\end{cases}
\]

\[
E(X)=\int_1^3x\left(\frac14x\right)\,dx=\left[\frac{x^3}{12}\right]_1^3=\frac{13}{6}.
\]

\[
E(X^2)=\int_1^3x^2\left(\frac14x\right)\,dx=\left[\frac{x^4}{16}\right]_1^3=5.
\]

\[
\operatorname{Var}(X)=5-\left(\frac{13}{6}\right)^2=\frac{11}{36}.
\]

\[
E(2X-3)=2\left(\frac{13}{6}\right)-3=\frac43.
\]

\[
\operatorname{Var}(2X-3)=4\cdot\frac{11}{36}=\frac{11}{9}.
\]

# 12. Common Mistakes and Exam Traps

1. Treating \(f(x)\) as a probability. Correct: \(f(x)\) is density and \(P(X=x)=0\).
2. Forgetting that probability is area. Correct: \(P(a<X<b)=\int_a^b f(x)\,dx\).
3. Forgetting the total-area condition when finding \(k\).
4. Ignoring \(f(x)\geq0\).
5. Confusing \(p(x)\), \(f(x)\) and \(F(x)\).
6. Forgetting the outer pieces \(F(x)=0\) and \(F(x)=1\) in a CDF.
7. Using \(x\) as both an upper limit and the integration variable.
8. Forgetting previously accumulated probability in piecewise CDFs.
9. Rounding as if \(X\) were discrete.
10. Using the wrong transformation rule for variance.
11. Treating continuous uniform as “each exact value equally likely”. Exact values still have probability zero.
12. Importing Pearson-only mode, quartile, percentile or skewness material into core CCEA answers.

# 13. Practice Questions

All questions in this section are **AI-generated on-spec practice questions** for CCEA `FAS2-DIST-LO004`, `FAS2-DIST-LO005` and `FAS2-DIST-LO006`. They are **not** past-paper questions and are **not** textbook questions.

## 13.1 Basic fluency questions

1. \(f(x)=kx\), \(0\leq x\leq4\), zero otherwise. Find \(k\).
2. \(f(x)=\frac{1}{18}x\), \(0\leq x\leq6\), zero otherwise. Find \(P(2<X<5)\) and \(P(X=3)\).
3. \(f(x)=\frac12\), \(1\leq x\leq3\), zero otherwise. Find \(F(x)\).
4. \(F(x)=0\) for \(x<0\), \(F(x)=x^2/16\) for \(0\leq x\leq4\), and \(F(x)=1\) for \(x>4\). Find \(f(x)\).

## 13.2 Bridge questions

5. Explain why \(P(X=2)=0\), but \(P(1.9<X<2.1)\) may be positive.
6. Explain how histogram frequency density helps you understand probability density.
7. For discrete \(X\), one condition is \(\sum p(x)=1\). Write down the continuous equivalent.

## 13.3 Standard exam-style questions

8. \(f(x)=k(3-x)\), \(1\leq x\leq3\), zero otherwise. Find \(k\), \(P(1.5<X<2.5)\), and \(E(X)\).
9. \(f(x)=kx\) for \(0\leq x<2\), \(f(x)=k(4-x)\) for \(2\leq x\leq4\), zero otherwise. Find \(k\), \(F(x)\), and \(P(1<X<3)\).
10. Given \(F(x)=0\) for \(x<1\), \(F(x)=\frac{x^2-1}{8}\) for \(1\leq x\leq3\), and \(F(x)=1\) for \(x>3\), find \(P(X\leq2)\), \(P(1.5<X<2.5)\), \(f(x)\), and \(P(X=2)\).
11. \(f(x)=\frac{3}{16}x(4-x)\), \(2\leq x\leq4\), zero otherwise. Find \(P(2<X<3)\), \(E(X)\), and \(\operatorname{Var}(X)\).
12. Let \(X\sim U[5,13]\). Find \(f(x)\), \(P(7<X<10)\), \(E(X)\), \(\operatorname{Var}(X)\), and \(\operatorname{SD}(X)\).

## 13.4 Harder synthesis questions

13. \(f(x)=kx^2\), \(0\leq x\leq3\), zero otherwise. Find \(k\), \(F(x)\), \(E(X)\), \(\operatorname{Var}(X)\), \(E(4X-7)\), and \(\operatorname{Var}(4X-7)\).
14. \(f(x)=kx\) for \(0\leq x<1\), \(f(x)=k\) for \(1\leq x\leq3\), zero otherwise. Find \(k\), \(F(x)\), \(P(0.5<X<2)\), and \(E(X)\).
15. A machine fills packets with flour. The mass \(X\), in kg, is modelled by \(X\sim U[0.95,1.05]\). Find the p.d.f., \(P(X<1)\), \(P(0.98<X<1.03)\), \(E(X)\), \(\operatorname{Var}(X)\), and one model limitation.

# 14. Worked Solutions

## Solution 1

\[
\int_0^4kx\,dx=1\Rightarrow k\left[\frac{x^2}{2}\right]_0^4=1\Rightarrow8k=1\Rightarrow\boxed{k=\frac18}.
\]

## Solution 2

\[
P(2<X<5)=\int_2^5\frac{x}{18}\,dx=\left[\frac{x^2}{36}\right]_2^5=\frac{25}{36}-\frac{4}{36}=\boxed{\frac{7}{12}}.
\]

Since \(X\) is continuous:

\[
\boxed{P(X=3)=0.}
\]

## Solution 3

\[
F(x)=\begin{cases}0,&x<1,\\\int_1^x\frac12\,dt,&1\leq x\leq3,\\1,&x>3.\end{cases}
\]

So:

\[
\boxed{F(x)=\begin{cases}0,&x<1,\\\frac{x}{2}-\frac12,&1\leq x\leq3,\\1,&x>3.\end{cases}}
\]

## Solution 4

Differentiate \(x^2/16\):

\[
\boxed{f(x)=\begin{cases}\frac{x}{8},&0\leq x\leq4,\\0,&\text{otherwise}.\end{cases}}
\]

## Solution 5

A single exact value has zero width, so zero area. Thus \(P(X=2)=0\). The interval \(1.9<X<2.1\) has positive width, so \(\int_{1.9}^{2.1}f(x)\,dx\) may be positive.

## Solution 6

Histogram frequency density uses area to give frequency. Continuous probability density uses area under \(f(x)\) to give probability.

## Solution 7

\[
\boxed{\int_{-\infty}^{\infty}f(x)\,dx=1.}
\]

The symbol changes because continuous probability is accumulated by integration rather than summing separate probabilities.

## Solution 8

\[
\int_1^3k(3-x)\,dx=1.
\]

\[
k\left[3x-\frac{x^2}{2}\right]_1^3=1.
\]

The bracket gives \(2\), so:

\[
\boxed{k=\frac12}.
\]

\[
P(1.5<X<2.5)=\int_{3/2}^{5/2}\frac12(3-x)\,dx=\boxed{\frac12}.
\]

\[
E(X)=\int_1^3x\cdot\frac12(3-x)\,dx=\boxed{\frac53}.
\]

## Solution 9

\[
\int_0^2kx\,dx+\int_2^4k(4-x)\,dx=1\Rightarrow2k+2k=1\Rightarrow\boxed{k=\frac14}.
\]

\[
F(x)=\begin{cases}
0,&x<0,\\
\frac{x^2}{8},&0\leq x<2,\\
x-\frac{x^2}{8}-1,&2\leq x\leq4,\\
1,&x>4.
\end{cases}
\]

\[
P(1<X<3)=F(3)-F(1)=\frac78-\frac18=\boxed{\frac34}.
\]

## Solution 10

\[
P(X\leq2)=F(2)=\frac{4-1}{8}=\boxed{\frac38}.
\]

\[
P(1.5<X<2.5)=F(2.5)-F(1.5)=\frac{21}{32}-\frac{5}{32}=\boxed{\frac12}.
\]

\[
f(x)=\begin{cases}\frac{x}{4},&1\leq x\leq3,\\0,&\text{otherwise}.\end{cases}
\]

\[
\boxed{P(X=2)=0.}
\]

## Solution 11

\[
P(2<X<3)=\frac{3}{16}\left[2x^2-\frac{x^3}{3}\right]_2^3=\boxed{\frac{11}{16}}.
\]

\[
E(X)=\frac{3}{16}\int_2^4(4x^2-x^3)\,dx=\boxed{\frac{11}{4}}.
\]

\[
E(X^2)=\frac{3}{16}\int_2^4(4x^3-x^4)\,dx=\frac{39}{5}.
\]

\[
\operatorname{Var}(X)=\frac{39}{5}-\left(\frac{11}{4}\right)^2=\boxed{\frac{19}{80}}.
\]

## Solution 12

For \(X\sim U[5,13]\):

\[
f(x)=\begin{cases}\frac18,&5\leq x\leq13,\\0,&\text{otherwise}.\end{cases}
\]

\[
P(7<X<10)=\frac{10-7}{13-5}=\boxed{\frac38}.
\]

\[
E(X)=\frac{5+13}{2}=\boxed{9}.
\]

\[
\operatorname{Var}(X)=\frac{(13-5)^2}{12}=\boxed{\frac{16}{3}}.
\]

\[
\operatorname{SD}(X)=\sqrt{\frac{16}{3}}=\boxed{\frac{4\sqrt3}{3}}.
\]

## Solution 13

\[
\int_0^3kx^2\,dx=1\Rightarrow9k=1\Rightarrow\boxed{k=\frac19}.
\]

\[
F(x)=\begin{cases}0,&x<0,\\\frac{x^3}{27},&0\leq x\leq3,\\1,&x>3.\end{cases}
\]

\[
E(X)=\frac19\int_0^3x^3\,dx=\boxed{\frac94}.
\]

\[
E(X^2)=\frac19\int_0^3x^4\,dx=\frac{27}{5}.
\]

\[
\operatorname{Var}(X)=\frac{27}{5}-\left(\frac94\right)^2=\boxed{\frac{27}{80}}.
\]

\[
E(4X-7)=4\cdot\frac94-7=\boxed{2}.
\]

\[
\operatorname{Var}(4X-7)=16\cdot\frac{27}{80}=\boxed{\frac{27}{5}}.
\]

## Solution 14

\[
\int_0^1kx\,dx+\int_1^3k\,dx=1\Rightarrow\frac{k}{2}+2k=1\Rightarrow\boxed{k=\frac25}.
\]

\[
F(x)=\begin{cases}0,&x<0,\\\frac{x^2}{5},&0\leq x<1,\\\frac{2x}{5}-\frac15,&1\leq x\leq3,\\1,&x>3.\end{cases}
\]

\[
P(0.5<X<2)=F(2)-F(0.5)=\frac35-\frac{1}{20}=\boxed{\frac{11}{20}}.
\]

\[
E(X)=\int_0^1x\left(\frac25x\right)\,dx+\int_1^3x\left(\frac25\right)\,dx=\frac{2}{15}+\frac85=\boxed{\frac{26}{15}}.
\]

## Solution 15

For \(X\sim U[0.95,1.05]\), width is \(0.10\), so:

\[
f(x)=\begin{cases}10,&0.95\leq x\leq1.05,\\0,&\text{otherwise}.\end{cases}
\]

\[
P(X<1)=\frac{1-0.95}{1.05-0.95}=\boxed{\frac12}.
\]

\[
P(0.98<X<1.03)=\frac{1.03-0.98}{0.10}=\boxed{\frac12}.
\]

\[
E(X)=\frac{0.95+1.05}{2}=\boxed{1\text{ kg}}.
\]

\[
\operatorname{Var}(X)=\frac{(0.10)^2}{12}=\boxed{\frac{1}{1200}\text{ kg}^2}.
\]

A limitation is that real packet masses may cluster around 1 kg rather than being equally dense across the interval.

# 15. Exam Technique Notes

1. Start every p.d.f. problem with the support.
2. Use total area \(=1\) for unknown constants.
3. Use interval probabilities, not point probabilities.
4. Inclusive endpoints do not change continuous probabilities.
5. Write CDFs as full piecewise functions.
6. Use \(t\) inside CDF integrals when \(x\) is the upper limit.
7. For piecewise CDFs, carry forward accumulated area.
8. To go from \(F(x)\) to \(f(x)\), differentiate the active expression and state zero otherwise.
9. For mean and variance, use \(E(X)=\int xf(x)\,dx\), \(E(X^2)=\int x^2f(x)\,dx\), then \(\operatorname{Var}(X)=E(X^2)-[E(X)]^2\).
10. Use exact fractions where possible.
11. Sketches should show support and zero regions.
12. Modelling questions need interpretation, units and limitations.
13. Do not spend core CCEA revision time on Pearson-only mode, quartiles, percentiles or skewness unless a CCEA-specific source requires them.

# 16. Syllabus Gap Check

## 16.1 LO coverage table

| LO ID | Official CCEA Further Maths focus | Covered in this lesson? | Evidence-backed coverage | Remaining issue |
|---|---|---:|---|---|
| `FAS2-DIST-LO004` | Continuous probability distributions, p.d.f.s, mean, variance and standard deviation | Yes | Sections 6–8 define continuous random variables, p.d.f.s, total area, interval probabilities, CDFs, mean, variance and standard deviation. | None found. |
| `FAS2-DIST-LO005` | Calculate `P(a<X<b)`, `E(X)` and `Var(X)` from a simple p.d.f. | Yes | Worked Examples 1–6 and Practice Questions 1–15 include p.d.f. normalisation, probability integrals, expectation and variance. | None found. |
| `FAS2-DIST-LO006` | Use `E(aX+b)` and `Var(aX+b)` | Yes | Sections 8.17 and Worked Example 6 cover transformation rules. | More CCEA-style exam questions would strengthen this, but the core rule is covered. |
| `FAS2-DIST-LO002` | Discrete probability functions, mean, variance and standard deviation | Bridge only | Used to compare `p(x)`, sums, discrete exact probabilities, expectation and variance with continuous analogues. | Not taught as a full discrete lesson here. |
| `FAS2-DIST-LO003` | Discrete probabilities, `E(X)`, `Var(X)` for simple discrete random variables | Bridge only | Used to explain why summation becomes integration. | Not taught as a full discrete calculation lesson here. |

## 16.2 Evidence coverage table

| Evidence source | Used? | Covered content | Limitation |
|---|---:|---|---|
| CCEA Further Mathematics Specification Map | Yes | Determines `FAS2-DIST`, LO boundary and exclusion decisions | Project source available, but not as original CCEA PDF page image. |
| Further Maths README module map | Yes | Confirms module route and bridge context | Used for project mapping, not mathematical authority above the specification. |
| Evidence Drop Checklist | Yes | Governs evidence preservation, missing evidence and asset logging | Procedural source only. |
| Ordinary A-Level Maths Bridge Extracts | Yes | Histograms, integration, normal distribution and probability bridge | Used only as bridge context. |
| `FS2-Chp3-ContinuousDistributions.pdf` | Yes | Discrete vs continuous distributions, p.d.f.s, total area, CDFs, `F(x)` to `f(x)`, mean, variance and uniform distribution | Cross-board/Pearson/DrFrost source, filtered through CCEA. |
| `transcripts.md` | Yes | Teacher explanations, warnings, worked-example narration, endpoint and notation warnings | Transcript is long and partially truncated in preview; used for relevant chapter content. |
| Screenshot PDF | Partially | Visible slide details: shaded area, handwritten area annotation, discrete/continuous comparison, histogram bridge | Text could not be parsed; only visible/readable details are preserved. |

## 16.3 Off-Spec Content Found but Excluded

| Off-spec or boundary-risk content | Source | Why excluded from core |
|---|---|---|
| Mode of a continuous distribution | DrFrost/Pearson Chapter 3 | Not explicitly part of the CCEA FAS2-DIST LOs used for this lesson. |
| Median, quartiles and percentiles for p.d.f.s | DrFrost/Pearson Chapter 3 | Useful but not listed in the selected CCEA FAS2 continuous-distribution LO boundary. |
| Skewness using mean, median and mode | DrFrost/Pearson Chapter 3 | Boundary-risk enrichment, not core. |
| Student’s `t`-distribution examples | DrFrost/Pearson Chapter 3 intro | Mentioned as a continuous distribution example, but not taught in this CCEA FAS2 lesson. |
| `χ²` distribution examples | DrFrost/Pearson Chapter 3 intro | Mentioned as a continuous distribution example, but not taught in this CCEA FAS2 lesson. |
| A2-style integration by parts modelling examples | DrFrost/Pearson later chapter material | Goes beyond “simple function of `x`” boundary for this FAS2 core lesson. |

## 16.4 Optional Enrichment Not Required by CCEA

- locating the mode of a p.d.f.;
- finding medians, quartiles and percentiles from a CDF;
- comparing mean, median and mode for skewness;
- exploring named continuous distributions beyond normal/uniform examples;
- using more advanced A2 integration techniques for probability models;
- conditional probability with continuous uniform distributions.

## 16.5 Missing evidence log

| Missing or unavailable evidence | Impact | Logged action |
|---|---|---|
| Original CCEA specification page image | Low | Project specification map used as authority. |
| Full readable OCR of screenshot PDF | Medium | No unseen annotations claimed. |
| CCEA mark-scheme examples for this topic | Medium | Generated questions are not labelled as past-paper. |
| Complete Pearson textbook extract pages | Medium | Slide examples used only where supplied in PDF/transcript. |
| Teacher’s exact board-specific CCEA exam technique notes | Medium | General CCEA-aligned exam technique generated from specification and evidence. |

# 17. Recommended Enhancements Not in the Evidence

These are AI-proposed teaching enhancements. They are not claimed as evidence-backed lesson content unless they directly restate the supplied evidence or CCEA boundary.

## 17.1 Proposed diagrams

| Enhancement | Purpose | Status |
|---|---|---|
| Discrete-to-continuous probability machine diagram | Show `p(x) → f(x)`, `Σ → ∫`, exact value to interval | Proposed |
| Histogram-to-p.d.f. bridge diagram | Make the density idea feel familiar before calculus appears | Proposed |
| Support interval highlighter | Show why integrals run only over the non-zero interval | Proposed |
| CDF accumulation animation | Show `F(x)` growing from 0 to 1 as `x` moves right | Proposed |
| Transformation visual for `Y=aX+b` | Show shift versus stretch and why variance uses `a²` | Proposed |

## 17.2 Proposed animations and widgets

- A vertical line at `X=7` shrinking to zero area, followed by an interval widening into visible probability.
- A discrete bar chart morphing into a smooth density curve.
- A shaded region moving from left to right to build `F(x)`.
- A uniform distribution rectangle with draggable endpoints.
- A notation sorter for `p(x)`, `f(x)` and `F(x)`.

# 18. Supplementary Sources Used

## 18.1 Project Sources used

- CCEA GCE Further Mathematics Specification Map.
- Further Maths README module map.
- Further Maths Evidence Drop Checklist.
- Ordinary A-Level Maths Bridge Spec Extracts.
- CCEA GCE Mathematics Specification Map for bridge context.

## 18.2 Lesson-specific evidence used

- `FS2-Chp3-ContinuousDistributions.pdf`: uploaded DrFrost/Pearson slide evidence.
- `transcripts.md`: teacher explanations, warnings and step-by-step commentary.
- `Chapter_3_Continuous_Distributions_📈_(Further_Statistics_2)_screenshots.pdf`: visible visual evidence and annotation planning only.

## 18.3 Ordinary A-Level Maths bridge sources

Ordinary A-Level Maths sources are used only for bridge context. They do not override the Further Maths specification.

Bridge areas used: histogram frequency density, ordinary probability notation, definite integration as area, differentiation as inverse of integration, normal distribution area intuition, and expectation/variance language.

## 18.4 Cross-board source notes

The DrFrost/Pearson source is not a CCEA specification authority. It is valuable lesson evidence, but it has been filtered through the CCEA `FAS2-DIST` boundary.

Material retained in the core lesson: p.d.f.s, total area, interval probability, CDFs, recovering `f(x)` from `F(x)`, expectation, variance, transformation rules and continuous uniform distribution as a simple p.d.f./model.

Material excluded from the core lesson: mode, median, quartiles, percentiles, skewness, named distributions not required in this FAS2 lesson, and advanced A2 integration-based modelling examples.

# 19. Final Student Checklist

## 19.1 Prerequisite confidence checklist

- [ ] I can explain the difference between a discrete and a continuous random variable.
- [ ] I know that discrete probabilities can be attached to exact values.
- [ ] I know that continuous exact-value probabilities are zero.
- [ ] I can calculate areas using definite integration.
- [ ] I understand histogram frequency density and why area matters.
- [ ] I can differentiate simple polynomial expressions.
- [ ] I can work with piecewise functions.

## 19.2 Further Maths method checklist

- [ ] I can state that a p.d.f. must satisfy \(f(x)\geq0\) and \(\int f(x)\,dx=1\).
- [ ] I can find \(k\) in a p.d.f. by setting total area equal to 1.
- [ ] I can calculate \(P(a<X<b)=\int_a^b f(x)\,dx\).
- [ ] I know that endpoint signs do not change continuous probabilities.
- [ ] I can write a complete CDF with 0, an integrated expression and 1.
- [ ] I can use \(F(x)=\int_{-\infty}^{x}f(t)\,dt\).
- [ ] I can recover \(f(x)=F'(x)\).
- [ ] I can calculate \(E(X)\), \(E(X^2)\), variance and standard deviation.
- [ ] I can use \(E(aX+b)=aE(X)+b\).
- [ ] I can use \(\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)\).

## 19.3 Continuous uniform distribution checklist

- [ ] I know that if \(X\sim U[a,b]\), then \(f(x)=1/(b-a)\) for \(a\leq x\leq b\).
- [ ] I can calculate \(P(c<X<d)=(d-c)/(b-a)\).
- [ ] I know \(E(X)=(a+b)/2\).
- [ ] I know \(\operatorname{Var}(X)=(b-a)^2/12\).
- [ ] I remember that equal density does not mean each exact value has positive probability.

## 19.4 Exam technique checklist

- [ ] I define the support before integrating.
- [ ] I use the p.d.f. only where it is non-zero.
- [ ] I use exact fractions where possible.
- [ ] I do not treat \(f(x)\) as \(P(X=x)\).
- [ ] I do not round continuous values like discrete values.
- [ ] I include \(F(x)=0\) below the support and \(F(x)=1\) above it.
- [ ] I carry forward accumulated probability in piecewise CDFs.
- [ ] I use \(t\) inside CDF integrals when \(x\) is the upper limit.
- [ ] I include units and model limitations where relevant.

## 19.5 Bridge checklist

- [ ] I can explain how \(\sum p(x)=1\) becomes \(\int f(x)\,dx=1\).
- [ ] I can explain why histogram frequency density prepares me for probability density.
- [ ] I can explain why the area under a p.d.f. gives probability.
- [ ] I can explain why a single exact continuous value has probability zero.
- [ ] I can explain why differentiation takes me from \(F(x)\) back to \(f(x)\).
