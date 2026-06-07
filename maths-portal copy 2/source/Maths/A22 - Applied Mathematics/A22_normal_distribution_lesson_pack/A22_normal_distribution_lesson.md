# Normal Distribution

## Title and Metadata

| Field | Value |
|---|---|
| Course | CCEA GCE Mathematics |
| Unit code | `A22` |
| Unit name | `A2 2 Applied Mathematics` |
| Section | Statistics |
| Primary topic code | `A22-NORMAL` |
| Topic name | Statistical distributions |
| Lesson title | Normal Distribution |
| topic_slug | `normal_distribution` |
| topic_pascal | `NormalDistribution` |
| topic_id | `A22NormalDistribution` |
| lesson_file | `A22_normal_distribution_lesson.md` |
| Primary LO IDs | `A22-NORMAL-LO001`, `A22-NORMAL-LO002`, `A22-NORMAL-LO003` |
| Adjacent on-spec LO IDs | `A22-HT-LO001`, `A22-HT-LO002`, `A22-HT-LO004` |
| Tags | `#A22`, `#Statistics`, `#NormalDistribution`, `#UseCalculator`, `#UseDistribution`, `#HypothesisTesting` |
| Phase status | Complete lesson pack written to files |

---

## Evidence Map

| Evidence source | Type | Use in this lesson |
|---|---|---|
| CCEA GCE Mathematics Specification Map | Official curriculum authority | Unit identity, topic code, LO IDs, boundaries, CCEA alignment |
| README Module Map | Project metadata source | Unit-code rules, file naming rules, folder structure, lesson structure |
| Source Evidence Drop Checklist | Evidence-control source | Missing evidence log, off-spec log, visual placeholder rules |
| `StatsYr2-Chp3-NormalDistribution.pdf` | Slide PDF / visual lesson evidence | Definitions, examples, diagrams, calculator processes, chapter structure |
| `Chapter_3_Normal_Distribution_🎲_(Applied_Year_2,_Statistics)_Transcript.md` | Teacher transcript | Explanation sequence, warnings, method commentary, calculator reasoning |
| `Chapter_3_Normal_Distribution_🎲_(Applied_Year_2,_Statistics)_Screenshots.pdf` | Screenshot evidence | Visual backup only; no searchable text parsed |

**Evidence limitation:** the screenshot PDF was not text-searchable. The lesson therefore uses it only as visual backup and relies mainly on the slide PDF and transcript for precise content.

---

## Specification Alignment

| LO ID | Lesson coverage |
|---|---|
| `A22-NORMAL-LO001` | Defines the normal distribution as a continuous probability distribution; explains bell-curve shape, symmetry, `X ~ N(mu, sigma^2)`, probability density, and area under the curve. |
| `A22-NORMAL-LO002` | Teaches calculator-based probability finding using Normal CD; includes left tail, right tail, interval, and outside-interval probabilities. |
| `A22-NORMAL-LO003` | Teaches distribution choice, binomial versus normal modelling, inverse normal, missing `mu`/`sigma`, and binomial-to-normal approximation. |
| `A22-HT-LO001` | Introduces hypothesis-testing language where the chapter evidence does so. |
| `A22-HT-LO002` | Explains sample-to-population inference and significance level. |
| `A22-HT-LO004` | Covers hypothesis testing for the mean of a normal distribution with known, given or assumed variance. |

---

## Learning Objectives

By the end of this lesson pack, the student should be able to:

1. Recognise when a normal distribution is a suitable model for a continuous random variable.
2. Interpret and write the notation
   \[
   X\sim N(\mu,\sigma^2).
   \]
3. Explain why probabilities in a continuous distribution are represented by **areas**, not single-point probabilities.
4. Use symmetry and the 68-95-99.7 rule to find simple normal probabilities without a calculator.
5. Use a calculator to find normal probabilities for left tails, right tails, intervals and combined outside regions.
6. Use inverse normal methods to find boundary values from probabilities.
7. Standardise a normal variable using
   \[
   Z=\frac{X-\mu}{\sigma}.
   \]
8. Find unknown `mu` and/or `sigma` from probability information.
9. Approximate a binomial distribution by a normal distribution where appropriate.
10. Apply continuity corrections carefully.
11. Use the normal distribution of a sample mean in hypothesis testing, when continuing into the adjacent `A22-HT` section.

---

## Prerequisite Recap

This recap uses **A-Level prior knowledge only**, because this pack is not relying on GCSE sources.

| Prior idea | Why it matters here |
|---|---|
| Random variables | A normal distribution models a random variable `X`. |
| Probability notation | You must read statements such as `P(X<109)`, `P(X>93)`, and `P(110<X<120)`. |
| Binomial distribution | You need to compare discrete binomial models with continuous normal models. |
| Mean, variance and standard deviation | The normal distribution is controlled by `mu` and `sigma`, and written using `sigma^2`. |
| Cumulative probabilities | Normal CD gives cumulative area under the curve. |
| Calculator distribution functions | The evidence uses calculator Normal CD and inverse Normal workflows. |
| Sampling ideas | Needed later for `Xbar` and hypothesis testing on the sample mean. |

---

## Big Picture Explanation

The normal distribution is the A2 statistics model for quantities that vary continuously: heights, times, measurements, masses, machine outputs and sample means. Unlike a binomial distribution, which counts successes in a fixed number of trials, the normal distribution spreads probability across a continuous curve.

The central picture is a bell-shaped curve. Values near the mean are most likely. Values far from the mean are less likely. The curve is symmetrical, so the left and right halves mirror each other. The probability is not found by reading the height of the curve; it is found by finding the **area under the curve**.

\[
\boxed{\text{Normal probability}=\text{area under the normal curve over the required interval}.}
\]

---

## Key Definitions and Notation

### Continuous random variable

A random variable is **continuous** if it can take any value in an interval, not just separate countable values.

Examples from the evidence include:

\[
\text{height},\qquad \text{speed},\qquad \text{time},\qquad \text{measured dimensions}.
\]

A continuous model is appropriate when the variable can be measured more and more accurately.

For example, a height reported as `172 cm` might actually be

\[
172.3\text{ cm},\quad 172.31\text{ cm},\quad 172.314\text{ cm},
\]

depending on how accurately it is measured.

### Normal distribution notation

If `X` is normally distributed with mean `mu` and variance `sigma^2`, we write

\[
\boxed{X\sim N(\mu,\sigma^2)}.
\]

| Symbol | Meaning |
|---|---|
| `X` | the random variable |
| `~` | “is distributed as” |
| `N` | normal distribution |
| `mu` | mean |
| `sigma` | standard deviation |
| `sigma^2` | variance |

Important: the notation uses the **variance** `sigma^2`, but calculator inputs usually ask for the **standard deviation** `sigma`.

So if

\[
X\sim N(100,15^2),
\]

then

\[
\mu=100,\qquad \sigma=15,\qquad \sigma^2=225.
\]

If

\[
X\sim N(8,0.2^2),
\]

then

\[
\mu=8,\qquad \sigma=0.2,\qquad \sigma^2=0.04.
\]

### Probability density

For a normal distribution, the vertical axis is not `P(X=x)`. It is a **probability density**, usually written as `f(x)`.

The evidence compares this to frequency density in histograms: the height is a density, and the area gives the quantity we care about.

\[
\boxed{\text{Area under }f(x)\text{ between two values}=\text{probability between those values}.}
\]

### Why `P(X=a)=0` for a continuous variable

For a continuous random variable,

\[
P(X=a)=0
\]

for any exact single value `a`.

This does **not** mean the value is impossible in ordinary language. It means that the probability of landing on exactly one infinitely precise value has no area.

For example, with height:

\[
P(X=200)
\]

would mean “exactly `200.000000... cm`”, with no width around it. Since probability comes from area, and a single vertical line has zero width,

\[
\boxed{P(X=200)=0.}
\]

So normal-distribution questions ask for intervals such as

\[
P(170<X<190),\qquad P(X>130),\qquad P(X<109).
\]

---

## Core Theory Part 1: What the Normal Distribution Looks Like

### 1. Bell-curve shape

A normal distribution has a bell-shaped curve.

For a height model with mean `180 cm`, the curve peaks at `180 cm`. Heights near `180 cm` are more likely, while much shorter or much taller heights are less likely.

[VISUAL PLACEHOLDER: A22NormalDistributionSVG-001 | Source: StatsYr2-Chp3-NormalDistribution.pdf p.4 + transcript lesson 1 | Insert from svg/A22NormalDistributionSVG-001.svg | Purpose: Show a bell curve for height with the mean at 180 cm, labelled axes `f(x)` and height `x`.]

### 2. Symmetry

The normal distribution is symmetrical about its mean.

This gives:

\[
\boxed{\text{mean}=\text{median}=\text{mode}.}
\]

It also gives:

\[
P(X>\mu)=0.5,
\]

and

\[
P(X<\mu)=0.5.
\]

The curve is a mathematical seesaw in perfect balance: half the area is on the left of the mean, and half is on the right.

### 3. Effect of changing `mu`

The mean `mu` shifts the centre of the curve.

If

\[
X\sim N(0,\sigma^2),
\]

the peak is at `0`.

If

\[
X\sim N(-2,\sigma^2),
\]

the peak is at `-2`.

Changing `mu` moves the curve left or right without changing its spread.

### 4. Effect of changing `sigma`

The standard deviation `sigma` controls the spread.

A larger standard deviation means the data are more spread out. The curve becomes wider and less peaky.

A smaller standard deviation means the data are more tightly clustered near the mean. The curve becomes narrower and taller.

[VISUAL PLACEHOLDER: A22NormalDistributionSVG-002 | Source: StatsYr2-Chp3-NormalDistribution.pdf p.5 | Insert from svg/A22NormalDistributionSVG-002.svg | Purpose: Compare normal curves with the same mean but different variances, showing that larger `sigma` gives a wider, flatter curve.]

### 5. Total area under the curve

For a discrete probability distribution, all probabilities add to 1.

For a continuous probability distribution, the corresponding statement is:

\[
\boxed{\text{The total area under the probability density curve is }1.}
\]

So for a normal distribution,

\[
P(-\infty<X<\infty)=1.
\]

This is why we use area under the curve to calculate probability.

### 6. Points of inflection

The normal curve has points of inflection one standard deviation away from the mean:

\[
\boxed{x=\mu-\sigma\quad\text{and}\quad x=\mu+\sigma.}
\]

At these points, the curve changes concavity.

[VISUAL PLACEHOLDER: A22NormalDistributionSVG-003 | Source: StatsYr2-Chp3-NormalDistribution.pdf p.7 | Insert from svg/A22NormalDistributionSVG-003.svg | Purpose: Show a normal curve with `mu-sigma`, `mu`, and `mu+sigma`, identifying the points of inflection.]

### 7. The 68-95-99.7 rule

For a normal distribution:

\[
\boxed{\text{About }68\%\text{ of data lies within }1\text{ standard deviation of the mean}.}
\]

\[
\boxed{\text{About }95\%\text{ of data lies within }2\text{ standard deviations of the mean}.}
\]

\[
\boxed{\text{About }99.7\%\text{ of data lies within }3\text{ standard deviations of the mean}.}
\]

So:

\[
P(\mu-\sigma<X<\mu+\sigma)\approx 0.68,
\]

\[
P(\mu-2\sigma<X<\mu+2\sigma)\approx 0.95,
\]

\[
P(\mu-3\sigma<X<\mu+3\sigma)\approx 0.997.
\]

For practical purposes, the evidence states that all data can be treated as lying within

\[
\mu\pm 5\sigma.
\]

[VISUAL PLACEHOLDER: A22NormalDistributionSVG-004 | Source: StatsYr2-Chp3-NormalDistribution.pdf p.8 | Insert from svg/A22NormalDistributionSVG-004.svg | Purpose: Show the 68-95-99.7 rule with regions labelled between `mu-sigma`, `mu+sigma`, `mu-2sigma`, `mu+2sigma`, `mu-3sigma`, and `mu+3sigma`.]

---

## Worked Example 1: Symmetry and the Mean

### Question

The diameters of a rivet produced by a particular machine, `X` mm, are modelled as

\[
X\sim N(8,0.2^2).
\]

Find:

\[
\text{a) }P(X>8)
\]

\[
\text{b) }P(7.8<X<8.2)
\]

### Solution to part a

We are given

\[
X\sim N(8,0.2^2).
\]

So the mean is

\[
\mu=8.
\]

The normal distribution is symmetrical about its mean, so half the area lies above the mean:

\[
P(X>8)=0.5.
\]

Therefore,

\[
\boxed{P(X>8)=0.5.}
\]

### Solution to part b

We are given

\[
\sigma=0.2.
\]

Now compare the interval endpoints with the mean:

\[
7.8=8-0.2=\mu-\sigma,
\]

and

\[
8.2=8+0.2=\mu+\sigma.
\]

So the interval

\[
7.8<X<8.2
\]

is the same as

\[
\mu-\sigma<X<\mu+\sigma.
\]

Using the 68-95-99.7 rule,

\[
P(\mu-\sigma<X<\mu+\sigma)\approx 0.68.
\]

Therefore,

\[
\boxed{P(7.8<X<8.2)=0.68.}
\]

---

## Worked Example 2: IQ and the 68-95-99.7 Rule

### Question

IQ is distributed as

\[
X\sim N(100,15^2).
\]

Find:

\[
\text{a) }P(70<X<130)
\]

\[
\text{b) }P(X>115)
\]

### Solution to part a

We are given

\[
\mu=100,\qquad \sigma=15.
\]

Now compare 70 and 130 with the mean:

\[
70=100-30=100-2(15)=\mu-2\sigma,
\]

and

\[
130=100+30=100+2(15)=\mu+2\sigma.
\]

So

\[
70<X<130
\]

is the same as

\[
\mu-2\sigma<X<\mu+2\sigma.
\]

Using the 68-95-99.7 rule,

\[
P(\mu-2\sigma<X<\mu+2\sigma)\approx 0.95.
\]

Therefore,

\[
\boxed{P(70<X<130)=0.95.}
\]

### Solution to part b

We are given

\[
\mu=100,\qquad \sigma=15.
\]

Now

\[
115=100+15=\mu+\sigma.
\]

The 68-95-99.7 rule gives

\[
P(\mu-\sigma<X<\mu+\sigma)\approx 0.68.
\]

By symmetry, this middle `0.68` is split equally either side of the mean:

\[
P(\mu<X<\mu+\sigma)=\frac{0.68}{2}=0.34.
\]

Also,

\[
P(X>\mu)=0.5.
\]

So

\[
P(X>115)=P(X>\mu+\sigma).
\]

The area to the right of `mu+sigma` is

\[
P(X>\mu+\sigma)=P(X>\mu)-P(\mu<X<\mu+\sigma).
\]

Substitute:

\[
P(X>115)=0.5-0.34.
\]

\[
P(X>115)=0.16.
\]

Therefore,

\[
\boxed{P(X>115)=0.16.}
\]

---

## Core Theory Part 2: Finding Normal Probabilities with a Calculator

The evidence uses calculator cumulative normal distribution functions. The key idea is:

\[
\boxed{\text{Normal CD finds the area between a lower bound and an upper bound.}}
\]

For

\[
X\sim N(\mu,\sigma^2),
\]

you enter:

\[
\text{lower bound},\quad \text{upper bound},\quad \sigma,\quad \mu.
\]

Important: the calculator usually wants `sigma`, not `sigma^2`.

### Left-tail probability

Suppose

\[
X\sim N(100,15^2)
\]

and we want

\[
P(X<109).
\]

There is no finite lower bound, so we use a very small number as a calculator stand-in for `-infinity`, for example

\[
-100000.
\]

Calculator setup:

\[
\text{lower}=-100000,
\]

\[
\text{upper}=109,
\]

\[
\sigma=15,
\]

\[
\mu=100.
\]

The evidence gives:

\[
P(X<109)=0.7257\quad\text{to 4 d.p.}
\]

So

\[
\boxed{P(X<109)=0.7257.}
\]

A diagram helps check whether this is sensible. Since `109` is greater than the mean `100`, the area to the left should be greater than `0.5`. The value `0.7257` is therefore reasonable.

[VISUAL PLACEHOLDER: A22NormalDistributionSVG-005 | Source: StatsYr2-Chp3-NormalDistribution.pdf p.12 | Insert from svg/A22NormalDistributionSVG-005.svg | Purpose: Show a normal curve with mean 100, upper bound 109, and left-tail area shaded.]

### Right-tail probability

Suppose

\[
X\sim N(100,15^2)
\]

and we want

\[
P(X\geq 93).
\]

Because `X` is continuous,

\[
P(X\geq 93)=P(X>93).
\]

Calculator setup:

\[
\text{lower}=93,
\]

\[
\text{upper}=100000,
\]

\[
\sigma=15,
\]

\[
\mu=100.
\]

The evidence gives:

\[
P(X\geq 93)=0.6796\quad\text{to 4 d.p.}
\]

So

\[
\boxed{P(X\geq 93)=0.6796.}
\]

### Interval probability

Suppose

\[
X\sim N(100,15^2)
\]

and we want

\[
P(110<X<120).
\]

Calculator setup:

\[
\text{lower}=110,
\]

\[
\text{upper}=120,
\]

\[
\sigma=15,
\]

\[
\mu=100.
\]

The evidence gives:

\[
P(110<X<120)=0.1613\quad\text{to 4 d.p.}
\]

So

\[
\boxed{P(110<X<120)=0.1613.}
\]

### Outside two bounds

Suppose

\[
X\sim N(100,15^2)
\]

and we want

\[
P(X<80\text{ or }X>106).
\]

Rather than calculate each tail separately, find the middle area and subtract from 1:

\[
P(X<80\text{ or }X>106)=1-P(80<X<106).
\]

The evidence gives

\[
P(80<X<106)=0.5642.
\]

Therefore,

\[
P(X<80\text{ or }X>106)=1-0.5642.
\]

\[
P(X<80\text{ or }X>106)=0.4358.
\]

So

\[
\boxed{P(X<80\text{ or }X>106)=0.4358.}
\]

[VISUAL PLACEHOLDER: A22NormalDistributionSVG-006 | Source: StatsYr2-Chp3-NormalDistribution.pdf p.13 | Insert from svg/A22NormalDistributionSVG-006.svg | Purpose: Show two shaded outside regions `X<80` and `X>106`, with the unshaded middle region `80<X<106`.]

---

## Worked Example 3: Mensa Eligibility and a Binomial Follow-On

### Question

The criteria for joining Mensa is an IQ of at least `131`. Assume IQ has the distribution

\[
X\sim N(100,15^2).
\]

Determine:

a) What percentage of people are eligible to join Mensa.

b) If `30` adults are randomly chosen, find the probability that at least `3` of them will be eligible to join.

### Solution to part a

A person is eligible if their IQ is at least `131`.

Since `X` is continuous,

\[
P(X\geq 131)=P(X>131).
\]

Use Normal CD with:

\[
\text{lower}=131,
\]

\[
\text{upper}=100000,
\]

\[
\sigma=15,
\]

\[
\mu=100.
\]

The evidence gives:

\[
P(X\geq 131)=0.01938\quad\text{to 4 significant figures}.
\]

As a percentage,

\[
0.01938\times 100=1.938\%.
\]

Therefore,

\[
\boxed{1.938\%\text{ of people are eligible to join Mensa.}}
\]

### Solution to part b

Let

\[
Y=\text{the number of adults among 30 who are eligible to join Mensa}.
\]

For each adult:

\[
P(\text{eligible})=0.0193827\ldots
\]

There are:

\[
n=30
\]

adults.

Each adult is either eligible or not eligible, so there are two outcomes. The evidence also treats adults’ eligibility as independent for this model.

So

\[
Y\sim B(30,0.0193827\ldots).
\]

We want:

\[
P(Y\geq 3).
\]

Use the complement:

\[
P(Y\geq 3)=1-P(Y\leq 2).
\]

The evidence gives:

\[
P(Y\leq 2)=0.979986.
\]

Therefore,

\[
P(Y\geq 3)=1-0.979986.
\]

\[
P(Y\geq 3)=0.020014.
\]

To 4 significant figures:

\[
\boxed{P(Y\geq 3)=0.02001.}
\]

---

## Core Theory Part 3: Inverse Normal Distribution

The **inverse normal** process reverses ordinary normal probability work. Instead of being given a boundary and finding an area, we are given an area and must find the boundary value. Given a probability of being in a region, find the value of the boundary. Draw a sketch before using the calculator.

Suppose

\[
X\sim N(20,3^2).
\]

Find `a`, correct to two decimal places, such that:

\[
P(X<a)=0.75.
\]

Using inverse normal with

\[
\mu=20,\qquad \sigma=3,\qquad \text{area}=0.75,
\]

gives

\[
a=22.0235\ldots
\]

Therefore,

\[
\boxed{a=22.02.}
\]

[VISUAL PLACEHOLDER: A22NormalDistributionSVG-007 | Source: StatsYr2-Chp3-NormalDistribution.pdf inverse normal section | Insert from svg/A22NormalDistributionSVG-007.svg | Purpose: Show a left-tail inverse normal diagram with `P(X<a)=0.75`.]

### Right-tail inverse normal

Find `a` such that

\[
P(X>a)=0.4.
\]

The calculator usually wants the area to the **left** of the boundary. If

\[
P(X>a)=0.4,
\]

then

\[
P(X<a)=1-0.4.
\]

\[
P(X<a)=0.6.
\]

Using inverse normal with

\[
\mu=20,\qquad \sigma=3,\qquad \text{area}=0.6,
\]

gives

\[
a=20.760\ldots
\]

Therefore,

\[
\boxed{a=20.76.}
\]

### Interval inverse normal

Find `a` such that

\[
P(16<X<a)=0.3.
\]

This is not directly a left-tail probability, so we build the left-tail area first.

From calculator or normal table,

\[
P(X<16)=0.09121.
\]

The required middle area is

\[
P(16<X<a)=0.3.
\]

Therefore,

\[
P(X<a)=P(X<16)+P(16<X<a).
\]

\[
P(X<a)=0.09121+0.3.
\]

\[
P(X<a)=0.39121.
\]

Using inverse normal with

\[
\mu=20,\qquad \sigma=3,\qquad \text{area}=0.39121,
\]

gives

\[
a=19.17\ldots
\]

Therefore,

\[
\boxed{a=19.17.}
\]

Tiny exam goblin to watch: the calculator does not understand your diagram. You must translate the shaded region into the left-tail area it expects.

---

## Worked Example 4: IQ Top Percentage and Interquartile Range

Suppose IQ is distributed as

\[
X\sim N(100,15^2).
\]

### Part a: Determine the IQ corresponding to the top 30% of the population

“Top 30%” means

\[
P(X>k)=0.3.
\]

So the area below `k` is

\[
P(X<k)=1-0.3=0.7.
\]

Using inverse normal with

\[
\mu=100,\qquad \sigma=15,\qquad \text{area}=0.7,
\]

gives

\[
k=107.87\ldots
\]

Therefore,

\[
\boxed{k=107.87.}
\]

### Part b: Determine the interquartile range of IQs

The lower quartile `Q_1` satisfies

\[
P(X<Q_1)=0.25.
\]

Using inverse normal:

\[
Q_1=89.88.
\]

The upper quartile `Q_3` satisfies

\[
P(X<Q_3)=0.75.
\]

Using inverse normal:

\[
Q_3=110.12.
\]

The interquartile range is

\[
IQR=Q_3-Q_1.
\]

\[
IQR=110.12-89.88.
\]

\[
IQR=20.24.
\]

Therefore,

\[
\boxed{IQR=20.24.}
\]

---

## Core Theory Part 4: Standardising and Z-Values

The standard normal distribution is

\[
Z\sim N(0,1^2).
\]

That means

\[
\mu=0,\qquad \sigma=1.
\]

To convert a normal variable `X` into a standard normal variable `Z`, use

\[
\boxed{Z=\frac{X-\mu}{\sigma}.}
\]

This is called **standardising**.

### The `Phi` notation

We write

\[
\Phi(z)=P(Z<z).
\]

So `Phi(z)` is the area to the left of `z` under the standard normal curve.

---

## Worked Example 5: Writing Normal Probabilities in Terms of `Phi`

Let

\[
X\sim N(50,4^2).
\]

### Part a: Write `P(X<53)` in terms of `Phi`

Start with

\[
P(X<53).
\]

Standardise:

\[
Z=\frac{X-\mu}{\sigma}.
\]

Here,

\[
\mu=50,\qquad \sigma=4.
\]

So

\[
P(X<53)=P\left(\frac{X-50}{4}<\frac{53-50}{4}\right).
\]

Now calculate:

\[
\frac{53-50}{4}=\frac{3}{4}=0.75.
\]

Therefore,

\[
P(X<53)=P(Z<0.75).
\]

Using `Phi` notation,

\[
\boxed{P(X<53)=\Phi(0.75).}
\]

### Part b: Write `P(X>=55)` in terms of `Phi`

Start with

\[
P(X\geq 55).
\]

Standardise:

\[
P(X\geq 55)=P\left(\frac{X-50}{4}\geq \frac{55-50}{4}\right).
\]

Now calculate:

\[
\frac{55-50}{4}=\frac{5}{4}=1.25.
\]

So

\[
P(X\geq 55)=P(Z\geq 1.25).
\]

Since

\[
P(Z\geq 1.25)=1-P(Z<1.25),
\]

we get

\[
P(X\geq 55)=1-\Phi(1.25).
\]

Therefore,

\[
\boxed{P(X\geq 55)=1-\Phi(1.25).}
\]

---

## Worked Example 6: Percentiles Using Z

The systolic blood pressure of an adult population, `X` mmHg, is modelled as

\[
X\sim N(127,16^2).
\]

A medical researcher wants adults with blood pressure higher than the 95th percentile. Find the minimum blood pressure for an adult included in the study.

The 95th percentile means

\[
P(X<s)=0.95.
\]

Equivalently, the top tail is

\[
P(X>s)=0.05.
\]

From the standard normal table,

\[
z=1.6449
\]

corresponds to the top `5%`, or left-tail area `0.95`.

Use

\[
Z=\frac{X-\mu}{\sigma}.
\]

Substitute:

\[
1.6449=\frac{s-127}{16}.
\]

Multiply both sides by `16`:

\[
16(1.6449)=s-127.
\]

\[
26.3184=s-127.
\]

Add `127`:

\[
s=153.3184.
\]

To 3 significant figures,

\[
\boxed{s=153\text{ mmHg}.}
\]

---

## Core Theory Part 5: Missing `mu` and/or `sigma`

The way through missing-parameter questions is to standardise and form equations.

### General method

1. Draw a normal curve sketch.
2. Decide whether the `z`-value should be positive or negative.
3. Use a table or inverse normal to find the `z`-value.
4. Substitute into

\[
\boxed{Z=\frac{X-\mu}{\sigma}.}
\]

5. Solve the resulting equation.

---

## Worked Example 7: Missing Mean

Let

\[
X\sim N(\mu,3^2).
\]

Given that

\[
P(X>20)=0.2,
\]

find `mu`.

Since

\[
P(X>20)=0.2,
\]

the area to the left of `20` is

\[
P(X<20)=0.8.
\]

From the standard normal table,

\[
P(Z<0.8416)=0.8.
\]

So

\[
\frac{20-\mu}{3}=0.8416.
\]

Multiply both sides by `3`:

\[
20-\mu=3(0.8416).
\]

\[
20-\mu=2.5248.
\]

Subtract `20` from both sides:

\[
-\mu=2.5248-20.
\]

\[
-\mu=-17.4752.
\]

Multiply by `-1`:

\[
\mu=17.4752.
\]

To 3 significant figures,

\[
\boxed{\mu=17.5.}
\]

---

## Worked Example 8: Missing Standard Deviation

A machine makes metal sheets with width `X` cm, modelled as

\[
X\sim N(50,\sigma^2).
\]

Given that

\[
P(X<46)=0.2119,
\]

find `sigma`.

From the standard normal table,

\[
P(Z<-0.80)=0.2119.
\]

So

\[
\frac{46-50}{\sigma}=-0.80.
\]

Simplify the numerator:

\[
\frac{-4}{\sigma}=-0.80.
\]

Multiply both sides by `sigma`:

\[
-4=-0.80\sigma.
\]

Divide by `-0.80`:

\[
\sigma=\frac{-4}{-0.80}.
\]

\[
\sigma=5.
\]

Therefore,

\[
\boxed{\sigma=5.}
\]

### Find the 90th percentile of the widths

Now

\[
X\sim N(50,5^2).
\]

Let `a` be the 90th percentile.

\[
P(X<a)=0.9.
\]

From the standard normal table,

\[
z=1.2816.
\]

Use

\[
z=\frac{a-\mu}{\sigma}.
\]

\[
1.2816=\frac{a-50}{5}.
\]

Multiply by `5`:

\[
5(1.2816)=a-50.
\]

\[
6.408=a-50.
\]

Add `50`:

\[
a=56.408.
\]

To 1 decimal place,

\[
\boxed{a=56.4\text{ cm}.}
\]

---

## Worked Example 9: Both `mu` and `sigma` Missing

The weight `Y` grams of soup put into a carton by a machine is normally distributed with mean `mu` grams and standard deviation `sigma` grams.

Given:

\[
P(Y<160)=0.99,
\]

and

\[
P(Y>152)=0.90,
\]

find `mu` and `sigma`.

From the standard normal table,

\[
P(Z<2.3263)=0.99.
\]

So

\[
\frac{160-\mu}{\sigma}=2.3263.
\]

This gives

\[
160-\mu=2.3263\sigma.\tag{1}
\]

Also,

\[
P(Y>152)=0.90.
\]

So

\[
P(Y<152)=0.10.
\]

From the standard normal table,

\[
P(Z<-1.2816)=0.10.
\]

So

\[
\frac{152-\mu}{\sigma}=-1.2816.
\]

This gives

\[
152-\mu=-1.2816\sigma.\tag{2}
\]

Subtract equation (2) from equation (1):

\[
(160-\mu)-(152-\mu)=2.3263\sigma-(-1.2816\sigma).
\]

Simplify the left side:

\[
160-\mu-152+\mu=8.
\]

Simplify the right side:

\[
2.3263\sigma+1.2816\sigma=3.6079\sigma.
\]

So

\[
8=3.6079\sigma.
\]

Divide by `3.6079`:

\[
\sigma=\frac{8}{3.6079}.
\]

\[
\sigma=2.217\ldots
\]

So

\[
\boxed{\sigma=2.22\text{ to 3 s.f.}}
\]

Now find `mu`. Use

\[
160-\mu=2.3263\sigma.
\]

Substitute:

\[
160-\mu=2.3263(2.217\ldots).
\]

\[
160-\mu=5.158\ldots
\]

Subtract `160`:

\[
-\mu=5.158\ldots-160.
\]

\[
-\mu=-154.841\ldots
\]

Therefore,

\[
\mu=154.841\ldots
\]

So

\[
\boxed{\mu=155\text{ to 3 s.f.}}
\]

---

## Core Theory Part 6: Binomial-to-Normal Approximation

If

\[
X\sim B(n,p),
\]

then

\[
E(X)=np,
\]

and

\[
\operatorname{Var}(X)=np(1-p).
\]

So we approximate using

\[
Y\sim N(np,np(1-p)).
\]

That is,

\[
\boxed{X\sim B(n,p)\approx Y\sim N(np,np(1-p)).}
\]

### Quick examples

#### Example 1

\[
X\sim B(10,0.2).
\]

Mean:

\[
np=10(0.2)=2.
\]

Variance:

\[
np(1-p)=10(0.2)(0.8)=1.6.
\]

So

\[
\boxed{X\sim B(10,0.2)\approx Y\sim N(2,1.6).}
\]

#### Example 2

\[
X\sim B(20,0.5).
\]

Mean:

\[
np=20(0.5)=10.
\]

Variance:

\[
np(1-p)=20(0.5)(0.5)=5.
\]

So

\[
\boxed{X\sim B(20,0.5)\approx Y\sim N(10,5).}
\]

#### Example 3

\[
X\sim B(6,0.3).
\]

Mean:

\[
np=6(0.3)=1.8.
\]

Variance:

\[
np(1-p)=6(0.3)(0.7)=1.26.
\]

So

\[
\boxed{X\sim B(6,0.3)\approx Y\sim N(1.8,1.26).}
\]

Boundary warning: `n=6` is small, so this is an algebraic illustration of matching mean and variance, not automatically a high-quality approximation.

---

## Core Theory Part 7: Continuity Corrections

A binomial variable is discrete. A normal variable is continuous.

That creates a problem when we use a continuous curve to approximate a discrete count. A **continuity correction** bridges that gap.

\[
\boxed{\text{Approximate a discrete range using a continuous interval.}}
\]

### Rule

1. If the original inequality uses `>` or `<`, first rewrite it using `>=` or `<=`.
2. Enlarge the range by `0.5` at each relevant boundary.

### Continuity correction table

Let `X` be the discrete binomial variable, and `Y` be the continuous normal approximation.

| Discrete statement | Continuous approximation |
|---|---|
| `P(X<=7)` | `P(Y<=7.5)` |
| `P(X<10)` | `P(X<=9) approx P(Y<=9.5)` |
| `P(X>9)` | `P(X>=10) approx P(Y>=9.5)` |
| `P(1<=X<=10)` | `P(0.5<=Y<=10.5)` |
| `P(3<X<6)` | `P(4<=X<=5) approx P(3.5<=Y<=5.5)` |
| `P(3<=X<6)` | `P(2.5<=Y<=5.5)` |
| `P(3<X<=6)` | `P(3.5<=Y<=6.5)` |
| `P(X=3)` | `P(2.5<=Y<=3.5)` |

[VISUAL PLACEHOLDER: A22NormalDistributionSVG-008 | Source: StatsYr2-Chp3-NormalDistribution.pdf continuity correction section | Insert from svg/A22NormalDistributionSVG-008.svg | Purpose: Show how a discrete value such as `X=6` becomes the continuous interval `5.5<Y<6.5`.]

---

## Worked Example 10: Full Binomial Approximation

For a particular type of flower bulb, `55%` will produce yellow flowers. A random sample of `80` bulbs is planted.

Let

\[
X=\text{the number of bulbs producing yellow flowers}.
\]

Then

\[
X\sim B(80,0.55).
\]

### Part a: Calculate the actual probability that exactly 50 flowers are yellow

We want

\[
P(X=50).
\]

Using the binomial formula:

\[
P(X=50)=\binom{80}{50}(0.55)^{50}(0.45)^{30}.
\]

The evidence gives

\[
P(X=50)=0.0365.
\]

So

\[
\boxed{P(X=50)=0.0365.}
\]

### Part b: Use a normal approximation to estimate the probability

Mean:

\[
np=80(0.55)=44.
\]

Variance:

\[
np(1-p)=80(0.55)(0.45).
\]

\[
np(1-p)=19.8.
\]

So

\[
Y\sim N(44,19.8).
\]

We want

\[
P(X=50).
\]

Using continuity correction:

\[
P(X=50)\approx P(49.5<Y<50.5).
\]

Using normal probabilities, the evidence gives:

\[
P(Y<50.5)=0.9280,
\]

and

\[
P(Y<49.5)=0.8918.
\]

Therefore,

\[
P(49.5<Y<50.5)=P(Y<50.5)-P(Y<49.5).
\]

\[
P(49.5<Y<50.5)=0.9280-0.8918.
\]

\[
P(49.5<Y<50.5)=0.0362.
\]

So

\[
\boxed{P(X=50)\approx 0.0362.}
\]

### Part c: Percentage error

The exact value is `0.0365`. The approximate value is `0.0362`.

Percentage error:

\[
\frac{0.0365-0.0362}{0.0365}\times 100.
\]

Subtract:

\[
0.0365-0.0362=0.0003.
\]

So

\[
\frac{0.0003}{0.0365}\times 100=0.8219\ldots
\]

Therefore,

\[
\boxed{\text{percentage error}=0.82\%.}
\]

---

## Core Theory Part 8: Hypothesis Testing on the Sample Mean

This is adjacent on-spec content under `A22-HT`, not part of the primary `A22-NORMAL` topic identity. It is included because the supplied chapter evidence includes normal-distribution hypothesis testing, and the CCEA specification includes tests for the mean of a normal distribution with known, given or assumed variance.

If a random sample of size `n` is taken from a population with

\[
X\sim N(\mu,\sigma^2),
\]

then the sample mean is

\[
\bar X.
\]

The distribution of sample means is

\[
\boxed{\bar X\sim N\left(\mu,\frac{\sigma^2}{n}\right).}
\]

This means:

| Quantity | Meaning |
|---|---|
| `X` | individual observation |
| `Xbar` | sample mean |
| `mu` | population mean |
| `sigma^2` | population variance |
| `sigma^2/n` | variance of the sample mean |

[VISUAL PLACEHOLDER: A22NormalDistributionSVG-009 | Source: StatsYr2-Chp3-NormalDistribution.pdf hypothesis testing on sample mean section | Insert from svg/A22NormalDistributionSVG-009.svg | Purpose: Show individual observations `X` versus sample means `Xbar`, and how larger `n` makes `Xbar` less spread out.]

---

## Worked Example 11: Hypothesis Test for a Mean

A company sells fruit juice in cartons. The amount of juice in a carton has a normal distribution with standard deviation `3 ml`.

The company claims that the mean amount of juice per carton is `60 ml`. A trading inspector receives complaints that the company is overstating the mean amount of juice per carton.

The inspector takes a random sample of `16` cartons and finds that the mean amount of juice per carton is

\[
59.1\text{ ml}.
\]

Using a `5%` significance level, test whether there is evidence to uphold this complaint.

### Step 1: State the hypotheses

The complaint says the true mean is less than `60`, so this is a lower-tail test.

\[
H_0:\mu=60
\]

\[
H_1:\mu<60
\]

### Step 2: State the distribution under `H_0`

Let

\[
X=\text{amount of juice in one carton}.
\]

Under `H_0`,

\[
X\sim N(60,3^2).
\]

The sample size is

\[
n=16.
\]

So

\[
\bar X\sim N\left(60,\frac{3^2}{16}\right).
\]

Simplify the variance:

\[
\frac{3^2}{16}=\frac{9}{16}.
\]

The standard deviation of `Xbar` is

\[
\sqrt{\frac{9}{16}}=\frac{3}{4}=0.75.
\]

Therefore,

\[
\bar X\sim N(60,0.75^2).
\]

### Step 3: Find the probability of the observed result or more extreme

The observed sample mean is

\[
\bar x=59.1.
\]

Since this is a lower-tail test, calculate

\[
P(\bar X<59.1).
\]

Using

\[
\bar X\sim N(60,0.75^2),
\]

the evidence gives

\[
P(\bar X<59.1)=0.1151.
\]

### Step 4: Compare with the significance level

The significance level is

\[
0.05.
\]

We have

\[
0.1151>0.05.
\]

So the result is not sufficiently unlikely under `H_0`.

### Step 5: Conclusion in context

There is insufficient evidence to reject `H_0`.

Therefore,

\[
\boxed{\text{There is insufficient evidence to conclude that the mean amount of juice in the population is less than }60\text{ ml}.}
\]

---

## Worked Example 12: Critical Region for a Sample Mean

A machine produces bolts with diameter `D`, where `D` has a normal distribution with mean `0.580 cm` and standard deviation `0.015 cm`.

The machine is serviced. After the service, a random sample of `50` bolts is taken to see if the mean diameter has changed from `0.580 cm`. The standard deviation is still `0.015 cm`.

### Part a: Find, at the `1%` level, the critical region for this test

The mean might have changed in either direction, so this is a two-tailed test.

\[
H_0:\mu=0.580
\]

\[
H_1:\mu\neq 0.580
\]

Under `H_0`,

\[
D\sim N(0.580,0.015^2).
\]

For a sample of size `50`,

\[
\bar D\sim N\left(0.580,\frac{0.015^2}{50}\right).
\]

The standard deviation of `Dbar` is

\[
\frac{0.015}{\sqrt{50}}.
\]

At the `1%` level for a two-tailed test, each tail has probability

\[
0.005.
\]

The corresponding `z`-values are

\[
z=\pm 2.5758.
\]

Use

\[
z=\frac{\bar d-0.580}{0.015/\sqrt{50}}.
\]

#### Lower critical value

\[
-2.5758=\frac{\bar d-0.580}{0.015/\sqrt{50}}.
\]

Multiply both sides by `0.015/sqrt(50)`:

\[
-2.5758\left(\frac{0.015}{\sqrt{50}}\right)=\bar d-0.580.
\]

Add `0.580`:

\[
\bar d=0.580-2.5758\left(\frac{0.015}{\sqrt{50}}\right).
\]

\[
\bar d=0.5745\ldots
\]

#### Upper critical value

\[
2.5758=\frac{\bar d-0.580}{0.015/\sqrt{50}}.
\]

Multiply both sides by `0.015/sqrt(50)`:

\[
2.5758\left(\frac{0.015}{\sqrt{50}}\right)=\bar d-0.580.
\]

Add `0.580`:

\[
\bar d=0.580+2.5758\left(\frac{0.015}{\sqrt{50}}\right).
\]

\[
\bar d=0.5854\ldots
\]

So the critical region is approximately

\[
\boxed{\bar D\leq 0.575\quad\text{or}\quad \bar D\geq 0.585.}
\]

### Part b: Comment if the observed sample mean is `0.587 cm`

The observed value is

\[
\bar d=0.587.
\]

Compare with the upper critical boundary:

\[
0.587\geq 0.585.
\]

So the observed value lies in the critical region.

Therefore,

\[
\boxed{\text{There is sufficient evidence at the }1\%\text{ level that the mean bolt diameter has changed from }0.580\text{ cm}.}
\]

---

## Visual Asset Integration

The lesson uses normal-curve visuals, shaded normal curves, calculator workflow diagrams, distribution-choice flowcharts, inverse-probability shading, sampling-distribution diagrams and critical-region diagrams.

### Planned visual placeholders

| Asset ID | Type | Purpose |
|---|---|---|
| `A22NormalDistributionSVG-001` | SVG | Bell curve with mean |
| `A22NormalDistributionSVG-002` | SVG | Effect of changing `sigma` |
| `A22NormalDistributionSVG-003` | SVG | Points of inflection |
| `A22NormalDistributionSVG-004` | SVG | 68-95-99.7 rule |
| `A22NormalDistributionSVG-005` | SVG | Left-tail calculator probability |
| `A22NormalDistributionSVG-006` | SVG | Outside two bounds |
| `A22NormalDistributionSVG-007` | SVG | Inverse normal left-tail area |
| `A22NormalDistributionSVG-008` | SVG | Continuity correction |
| `A22NormalDistributionSVG-009` | SVG | Sampling distribution of `Xbar` |
| `A22NormalDistributionMER-001` | Mermaid | Distribution-choice flowchart |
| `A22NormalDistributionMER-002` | Mermaid | Normal probability method selector |
| `A22NormalDistributionMER-003` | Mermaid | Hypothesis-test decision route |
| `A22NormalDistributionTIKZ-001` | TikZ | Exam-style normal curve |
| `A22NormalDistributionTIKZ-002` | TikZ | Continuity correction diagram |
| `A22NormalDistributionTIKZ-003` | TikZ | Two-tailed critical region |
| `A22NormalDistributionTIKZ-004` | TikZ | Inverse normal diagram |
| `A22NormalDistributionWID-001` | Widget | Normal curve slider |
| `A22NormalDistributionWID-002` | Widget | Continuity-correction converter |
| `A22NormalDistributionWID-003` | Widget | Normal probability concept demo |
| `A22NormalDistributionWID-004` | Widget | Normal mean hypothesis-test trainer |

[VISUAL PLACEHOLDER: A22NormalDistributionMER-001 | Source: CCEA specification map + lesson evidence | Insert from mermaid/A22NormalDistributionMER-001.md | Purpose: Distribution-choice flowchart: binomial, normal, normal approximation, or neither.]

[VISUAL PLACEHOLDER: A22NormalDistributionSVG-010 | Source: CCEA specification map + lesson evidence | Insert from svg/A22NormalDistributionSVG-010.svg | Purpose: Calculator decision diagram for lower/upper bounds in Normal CD and inverse normal.]

[VISUAL PLACEHOLDER: A22NormalDistributionSVG-011 | Source: CCEA specification map + lesson evidence | Insert from svg/A22NormalDistributionSVG-011.svg | Purpose: Hypothesis-test decision diagram showing p-value versus significance level.]

[VISUAL PLACEHOLDER: A22NormalDistributionTIKZ-001 | Source: Lesson evidence | Insert from tikz/A22NormalDistributionTIKZ-001.tex | Purpose: Clean exam-style normal curve with labelled mean, standard deviations and shaded tail.]

[INTERACTIVE PLACEHOLDER: A22NormalDistributionWID-001 | Source: CCEA specification map + lesson evidence | Insert from widgets/A22NormalDistributionWID-001.html | Purpose: Slider widget showing how changing `mu` and `sigma` moves and reshapes the normal curve.]

[INTERACTIVE PLACEHOLDER: A22NormalDistributionWID-002 | Source: CCEA specification map + lesson evidence | Insert from widgets/A22NormalDistributionWID-002.html | Purpose: Continuity-correction practice widget that converts discrete binomial inequalities into continuous normal intervals.]

---

## Guided Practice

### Practice Question 1: Reading the notation

Let

\[
X\sim N(64,5^2).
\]

State:

a) the mean of `X`;  
b) the standard deviation of `X`;  
c) the variance of `X`;  
d) whether `P(X=64)` is positive, zero, or impossible to decide.

### Practice Question 2: Symmetry

Let

\[
X\sim N(40,6^2).
\]

Find:

a) `P(X>40)`  
b) `P(X<40)`  
c) `P(34<X<46)` using the 68-95-99.7 rule.

### Practice Question 3: Calculator probability

Let

\[
X\sim N(100,12^2).
\]

Use normal distribution calculator methods to find:

a) `P(X<110)`  
b) `P(X>85)`  
c) `P(90<X<115)`  
d) `P(X<82 or X>108)`  

Round answers to 4 decimal places.

### Practice Question 4: Inverse normal

Let

\[
X\sim N(30,4^2).
\]

Find `a`, to 2 decimal places, such that:

a) `P(X<a)=0.8`  
b) `P(X>a)=0.15`  
c) `P(25<X<a)=0.5`

### Practice Question 5: Missing standard deviation

A machine fills bags of rice. The mass `X` grams in a bag is modelled as

\[
X\sim N(500,\sigma^2).
\]

Given that

\[
P(X<488)=0.1587,
\]

find `sigma`.

### Practice Question 6: Missing mean

A battery lifetime `T` hours is modelled as

\[
T\sim N(\mu,8^2).
\]

Given that

\[
P(T>70)=0.2119,
\]

find `mu`.

### Practice Question 7: Normal approximation to binomial

Let

\[
X\sim B(120,0.35).
\]

a) Find a normal approximation to `X`.  
b) Use a continuity correction to estimate

\[
P(X\leq 45).
\]

### Practice Question 8: Hypothesis test for a mean

A population is normally distributed with known standard deviation `6`. A researcher claims that the population mean is `80`.

A random sample of `25` observations has sample mean

\[
\bar x=77.2.
\]

Test, at the `5%` significance level, whether there is evidence that the population mean is less than `80`.

---

## Common Mistakes and Exam Traps

### Trap 1: Reading `N(mu,sigma^2)` as `N(mu,sigma)`

The notation is:

\[
X\sim N(\mu,\sigma^2).
\]

The second parameter is the variance. If the question says

\[
X\sim N(64,5^2),
\]

then

\[
\sigma=5,
\]

not

\[
\sigma=25.
\]

If the question says

\[
X\sim N(64,25),
\]

then

\[
\sigma^2=25,
\]

so

\[
\sigma=\sqrt{25}=5.
\]

### Trap 2: Forgetting single-point probabilities are zero

For a continuous random variable,

\[
P(X=a)=0.
\]

So

\[
P(X>93)=P(X\geq 93).
\]

The boundary value is a line with no area.

### Trap 3: Using the wrong tail in inverse normal

If the question gives

\[
P(X>a)=0.4,
\]

then the left-tail area is

\[
P(X<a)=1-0.4=0.6.
\]

Inverse normal usually wants the area to the left of the boundary. Always draw a sketch before pressing buttons.

### Trap 4: Losing the sign of the `z`-value

If a value lies below the mean, its `z`-value is negative.

For example, if

\[
X\sim N(50,5^2),
\]

then for `X=42`,

\[
z=\frac{42-50}{5}.
\]

\[
z=\frac{-8}{5}.
\]

\[
z=-1.6.
\]

The minus sign tells you the value is below the mean.

### Trap 5: Forgetting the continuity correction

When approximating a binomial distribution with a normal distribution, do not write

\[
P(X\leq 45)\approx P(Y\leq 45).
\]

Use

\[
P(X\leq 45)\approx P(Y<45.5).
\]

Discrete bars need continuous width. Give the count half a unit on each side.

### Trap 6: Mixing up `X` and `Xbar`

For individual observations:

\[
X\sim N(\mu,\sigma^2).
\]

For a sample mean:

\[
\bar X\sim N\left(\mu,\frac{\sigma^2}{n}\right).
\]

The standard deviation of `Xbar` is

\[
\frac{\sigma}{\sqrt n},
\]

not

\[
\sigma.
\]

---

## Exam Technique Notes

### 1. Always write the distribution clearly

For normal probability questions, start with something like:

\[
X\sim N(100,15^2).
\]

For normal approximation questions, write:

\[
X\sim B(n,p)
\]

then

\[
Y\sim N(np,np(1-p)).
\]

For sample-mean hypothesis tests, write:

\[
\bar X\sim N\left(\mu,\frac{\sigma^2}{n}\right).
\]

This makes your method visible to the examiner.

### 2. Sketch before calculating

A quick sketch tells you whether the answer should be:

\[
<0.5,\quad >0.5,\quad \text{very small},\quad \text{or near }1.
\]

### 3. Use exact complement statements

For outside regions:

\[
P(X<80\text{ or }X>106)=1-P(80<X<106).
\]

For “at least” binomial follow-ons:

\[
P(Y\geq 3)=1-P(Y\leq 2).
\]

For right-tail inverse normal:

\[
P(X>a)=0.15
\]

means

\[
P(X<a)=0.85.
\]

### 4. In a hypothesis test, finish in context

Not enough:

\[
\text{Do not reject }H_0.
\]

Better:

\[
\text{There is insufficient evidence at the }5\%\text{ level to conclude that the population mean is less than }80.
\]

Statistics answers need words, not just numbers.

---

## Full Worked Solutions to Guided Practice

### Solution to Practice Question 1

Given:

\[
X\sim N(64,5^2).
\]

The normal distribution notation is

\[
X\sim N(\mu,\sigma^2).
\]

So:

\[
\mu=64.
\]

\[
\sigma=5.
\]

\[
\sigma^2=5^2=25.
\]

Therefore:

\[
\boxed{\text{mean}=64}
\]

\[
\boxed{\text{standard deviation}=5}
\]

\[
\boxed{\text{variance}=25}
\]

Since `X` is continuous,

\[
P(X=64)=0.
\]

So:

\[
\boxed{P(X=64)=0.}
\]

### Solution to Practice Question 2

Given:

\[
X\sim N(40,6^2).
\]

So:

\[
\mu=40,\qquad \sigma=6.
\]

#### Part a

The normal distribution is symmetrical about its mean, so half the area lies above the mean:

\[
P(X>40)=0.5.
\]

\[
\boxed{P(X>40)=0.5}
\]

#### Part b

Similarly, half the area lies below the mean:

\[
P(X<40)=0.5.
\]

\[
\boxed{P(X<40)=0.5}
\]

#### Part c

We need:

\[
P(34<X<46).
\]

Now:

\[
34=40-6=\mu-\sigma,
\]

and

\[
46=40+6=\mu+\sigma.
\]

So:

\[
P(34<X<46)=P(\mu-\sigma<X<\mu+\sigma).
\]

Using the 68-95-99.7 rule:

\[
P(\mu-\sigma<X<\mu+\sigma)\approx 0.68.
\]

Therefore:

\[
\boxed{P(34<X<46)=0.68.}
\]

### Solution to Practice Question 3

Given:

\[
X\sim N(100,12^2).
\]

So:

\[
\mu=100,\qquad \sigma=12.
\]

#### Part a

Find:

\[
P(X<110).
\]

Standardising check:

\[
z=\frac{110-100}{12}=\frac{10}{12}=0.8333\ldots
\]

Using calculator:

\[
P(X<110)=0.7977.
\]

\[
\boxed{P(X<110)=0.7977}
\]

#### Part b

Find:

\[
P(X>85).
\]

Standardising check:

\[
z=\frac{85-100}{12}=\frac{-15}{12}=-1.25.
\]

So:

\[
P(X>85)=P(Z>-1.25)=0.8944.
\]

\[
\boxed{P(X>85)=0.8944}
\]

#### Part c

Find:

\[
P(90<X<115).
\]

Using calculator:

\[
P(90<X<115)=0.6920.
\]

\[
\boxed{P(90<X<115)=0.6920}
\]

#### Part d

Find:

\[
P(X<82\text{ or }X>108).
\]

Use the complement:

\[
P(X<82\text{ or }X>108)=1-P(82<X<108).
\]

Calculator gives:

\[
P(82<X<108)=0.6815.
\]

Therefore:

\[
P(X<82\text{ or }X>108)=1-0.6815.
\]

\[
P(X<82\text{ or }X>108)=0.3185.
\]

\[
\boxed{P(X<82\text{ or }X>108)=0.3185}
\]

### Solution to Practice Question 4

Given:

\[
X\sim N(30,4^2).
\]

So:

\[
\mu=30,\qquad \sigma=4.
\]

#### Part a

Find `a` such that

\[
P(X<a)=0.8.
\]

Using inverse normal:

\[
a=33.366\ldots
\]

Therefore:

\[
\boxed{a=33.37}
\]

#### Part b

Find `a` such that

\[
P(X>a)=0.15.
\]

Convert to a left-tail probability:

\[
P(X<a)=1-0.15=0.85.
\]

Using inverse normal:

\[
a=34.145\ldots
\]

Therefore:

\[
\boxed{a=34.15}
\]

#### Part c

Find `a` such that

\[
P(25<X<a)=0.5.
\]

First find:

\[
P(X<25).
\]

Standardise:

\[
z=\frac{25-30}{4}=\frac{-5}{4}=-1.25.
\]

So:

\[
P(X<25)=P(Z<-1.25)=0.1056.
\]

Now:

\[
P(X<a)=P(X<25)+P(25<X<a).
\]

\[
P(X<a)=0.1056+0.5=0.6056.
\]

Using inverse normal:

\[
a=31.070\ldots
\]

Therefore:

\[
\boxed{a=31.07}
\]

### Solution to Practice Question 5

Given:

\[
X\sim N(500,\sigma^2).
\]

Also:

\[
P(X<488)=0.1587.
\]

From standard normal values:

\[
P(Z<-1)=0.1587.
\]

So:

\[
\frac{488-500}{\sigma}=-1.
\]

Simplify:

\[
\frac{-12}{\sigma}=-1.
\]

Multiply by `sigma`:

\[
-12=-\sigma.
\]

Multiply by `-1`:

\[
\sigma=12.
\]

Therefore:

\[
\boxed{\sigma=12}
\]

### Solution to Practice Question 6

Given:

\[
T\sim N(\mu,8^2).
\]

Also:

\[
P(T>70)=0.2119.
\]

So:

\[
P(T<70)=1-0.2119=0.7881.
\]

From standard normal values:

\[
P(Z<0.80)=0.7881.
\]

So:

\[
\frac{70-\mu}{8}=0.80.
\]

Multiply by `8`:

\[
70-\mu=8(0.80)=6.4.
\]

Subtract `70`:

\[
-\mu=6.4-70=-63.6.
\]

Multiply by `-1`:

\[
\mu=63.6.
\]

Therefore:

\[
\boxed{\mu=63.6}
\]

### Solution to Practice Question 7

Given:

\[
X\sim B(120,0.35).
\]

#### Part a

For a binomial distribution:

\[
E(X)=np,
\]

and

\[
\operatorname{Var}(X)=np(1-p).
\]

Here:

\[
n=120,\qquad p=0.35.
\]

Mean:

\[
np=120(0.35)=42.
\]

Variance:

\[
np(1-p)=120(0.35)(1-0.35)=120(0.35)(0.65)=27.3.
\]

So the normal approximation is:

\[
Y\sim N(42,27.3).
\]

Therefore:

\[
\boxed{X\sim B(120,0.35)\approx Y\sim N(42,27.3)}
\]

#### Part b

Estimate:

\[
P(X\leq 45).
\]

Use continuity correction:

\[
P(X\leq 45)\approx P(Y<45.5).
\]

Now:

\[
Y\sim N(42,27.3).
\]

So:

\[
\mu=42,
\]

and

\[
\sigma=\sqrt{27.3}=5.225\ldots
\]

Standardise:

\[
z=\frac{45.5-42}{\sqrt{27.3}}=\frac{3.5}{5.225\ldots}=0.6698\ldots
\]

So:

\[
P(Y<45.5)=P(Z<0.6698\ldots).
\]

Using calculator:

\[
P(Y<45.5)=0.7485.
\]

Therefore:

\[
\boxed{P(X\leq 45)\approx 0.7485}
\]

### Solution to Practice Question 8

The population is normally distributed with known standard deviation:

\[
\sigma=6.
\]

The claim is:

\[
\mu=80.
\]

The sample size is:

\[
n=25.
\]

The observed sample mean is:

\[
\bar x=77.2.
\]

The researcher wants to test whether the population mean is less than `80`, so this is a lower-tail test.

#### Step 1: State hypotheses

\[
H_0:\mu=80
\]

\[
H_1:\mu<80
\]

#### Step 2: State distribution of the sample mean under `H_0`

Since

\[
X\sim N(\mu,\sigma^2),
\]

we use

\[
\bar X\sim N\left(\mu,\frac{\sigma^2}{n}\right).
\]

Under `H_0`:

\[
\bar X\sim N\left(80,\frac{6^2}{25}\right).
\]

Simplify:

\[
\frac{6^2}{25}=\frac{36}{25}.
\]

The standard deviation of `Xbar` is:

\[
\sqrt{\frac{36}{25}}=\frac{6}{5}=1.2.
\]

So:

\[
\bar X\sim N(80,1.2^2).
\]

#### Step 3: Find the p-value

Observed:

\[
\bar x=77.2.
\]

Since this is a lower-tail test:

\[
p=P(\bar X\leq 77.2).
\]

Standardise:

\[
z=\frac{77.2-80}{1.2}=\frac{-2.8}{1.2}=-2.3333\ldots
\]

So:

\[
p=P(Z\leq -2.3333\ldots).
\]

Using calculator:

\[
p=0.0098.
\]

#### Step 4: Compare with significance level

The significance level is:

\[
5\%=0.05.
\]

Now:

\[
0.0098<0.05.
\]

So reject `H_0`.

#### Step 5: Conclusion in context

There is sufficient evidence at the `5%` significance level to conclude that the population mean is less than `80`.

\[
\boxed{\text{Reject }H_0.\text{ There is sufficient evidence that }\mu<80.}
\]

---

## Common CCEA-Style Wording

### “Modelled as”

When a question says

\[
X\text{ is modelled as }N(\mu,\sigma^2),
\]

you should treat the normal distribution as an assumption about the real-world variable. You may later need to comment on whether that model is appropriate.

### “Determine the probability”

Usually means use Normal CD, a standardised `Z`-value, or a symmetry rule.

Example:

\[
\text{Determine }P(X>130).
\]

### “Find the value of `a` such that...”

Usually means inverse normal.

Example:

\[
P(X<a)=0.75.
\]

### “Use a normal approximation”

Usually means:

\[
X\sim B(n,p)
\]

becomes

\[
Y\sim N(np,np(1-p)).
\]

Then apply a continuity correction.

### “At least”, “more than”, “fewer than”

Translate carefully:

\[
\text{at least }3 \quad\Longrightarrow\quad X\geq 3.
\]

\[
\text{more than }3 \quad\Longrightarrow\quad X>3 \quad\Longrightarrow\quad X\geq 4\text{ for discrete }X.
\]

\[
\text{fewer than }3 \quad\Longrightarrow\quad X<3 \quad\Longrightarrow\quad X\leq 2\text{ for discrete }X.
\]

### “Known, given or assumed variance”

For a hypothesis test on the mean of a normal distribution, use the population variance or standard deviation supplied by the question. Do not use the sample standard deviation unless the question explicitly moves into methods not included in this CCEA boundary.

---

## Syllabus Gap Check

| LO ID | Coverage status | Evidence-backed coverage |
|---|---|---|
| `A22-NORMAL-LO001` | Covered | Normal distribution as continuous probability distribution; `X~N(mu,sigma^2)`; area under curve; symmetry; `P(X=a)=0`. |
| `A22-NORMAL-LO002` | Covered | Normal probabilities using calculator, left-tail, right-tail, interval and outside-region probabilities. |
| `A22-NORMAL-LO003` | Covered | Appropriate distribution choice, binomial-to-normal approximation, continuity correction, inverse normal and missing `mu,sigma`. |
| `A22-HT-LO001` | Partially covered as adjacent | Hypotheses, significance level, p-value and critical region language introduced. |
| `A22-HT-LO002` | Partially covered as adjacent | Sample used to infer population mean; interpretation in context. |
| `A22-HT-LO004` | Covered as adjacent | Hypothesis test for the mean of a normal distribution with known variance; `Xbar~N(mu,sigma^2/n)`. |
| `A22-HT-LO003` | Not covered in this lesson | Binomial proportion test belongs to separate hypothesis-testing lesson. |
| `A22-HT-LO005` | Not covered in this lesson | Correlation coefficient p-value/critical-value interpretation belongs to separate hypothesis-testing or correlation lesson. |

---

## Off-Spec Content Found but Excluded

| Evidence item | Decision |
|---|---|
| DrFrostMaths website practice instructions | Source/practice context only, not core CCEA content. |
| Pearson/Edexcel exercise labels | Kept only as source labels, not treated as CCEA authority. |
| MAT extension references | Excluded from core. |
| Bayesian statistics and maximum entropy explanation | Optional enrichment only; not required by CCEA normal-distribution outcomes. |
| CERN 5-sigma context | Optional enrichment only; not used as examinable CCEA content. |
| Correlation hypothesis testing | Excluded from this normal-distribution lesson; belongs to `A22-HT-LO005`. |
| Binomial proportion hypothesis testing | Excluded from this normal-distribution lesson; belongs to `A22-HT-LO003`. |

---

## Optional Enrichment Not Required by CCEA

These ideas may help a curious student, but they are not required for this lesson’s core assessment boundary:

1. The normal distribution as a maximum-entropy distribution for fixed mean and standard deviation.
2. The CERN “5 sigma” context.
3. Bayesian prior modelling.
4. MAT-style extension probability questions.
5. Formal Type I error theory beyond the CCEA expectation.

---

## Visual and Interactive Asset Plan

### Mermaid assets for Phase 2

| Asset file | Purpose |
|---|---|
| `mermaid/A22NormalDistributionMER-001.md` | Distribution-choice flowchart. |
| `mermaid/A22NormalDistributionMER-002.md` | Normal-probability method selector: symmetry, calculator CD, inverse normal, standardising. |
| `mermaid/A22NormalDistributionMER-003.md` | Hypothesis-test decision route: hypotheses, distribution, p-value, compare, conclude. |

### SVG assets for Phase 3

| Asset file | Purpose |
|---|---|
| `svg/A22NormalDistributionSVG-001.svg` | Bell curve with mean. |
| `svg/A22NormalDistributionSVG-002.svg` | Effect of changing `sigma`. |
| `svg/A22NormalDistributionSVG-003.svg` | Points of inflection at `mu±sigma`. |
| `svg/A22NormalDistributionSVG-004.svg` | 68-95-99.7 rule. |
| `svg/A22NormalDistributionSVG-005.svg` | Left-tail calculator probability. |
| `svg/A22NormalDistributionSVG-006.svg` | Outside two bounds. |
| `svg/A22NormalDistributionSVG-007.svg` | Inverse normal left-tail area. |
| `svg/A22NormalDistributionSVG-008.svg` | Continuity correction. |
| `svg/A22NormalDistributionSVG-009.svg` | Sampling distribution of `Xbar`. |
| `svg/A22NormalDistributionSVG-010.svg` | Calculator workflow. |
| `svg/A22NormalDistributionSVG-011.svg` | Hypothesis-test p-value decision diagram. |

### TikZ assets for Phase 4

| Asset file | Purpose |
|---|---|
| `tikz/A22NormalDistributionTIKZ-001.tex` | Exam-style labelled normal curve. |
| `tikz/A22NormalDistributionTIKZ-002.tex` | Continuity correction diagram. |
| `tikz/A22NormalDistributionTIKZ-003.tex` | Two-tailed critical region diagram. |
| `tikz/A22NormalDistributionTIKZ-004.tex` | Inverse normal diagram. |

### Widget assets for Phase 5

| Asset file | Purpose |
|---|---|
| `widgets/A22NormalDistributionWID-001.html` | Interactive `mu,sigma` normal curve slider. |
| `widgets/A22NormalDistributionWID-002.html` | Continuity correction converter. |
| `widgets/A22NormalDistributionWID-003.html` | Normal probability calculator concept demo. |
| `widgets/A22NormalDistributionWID-004.html` | Hypothesis-test p-value decision trainer. |

---

## Supplementary Sources Used

| Source | Status |
|---|---|
| CCEA GCE Mathematics Specification Map | Core authority for unit, topic and LO boundaries. |
| Project README Module Map | Core project convention source for metadata and folder naming. |
| Source Evidence Drop Checklist | Core project process source for evidence and missing-item logs. |
| DrFrostMaths slide PDF | Lesson evidence and visual source; cross-board labels controlled by CCEA boundaries. |
| Teacher transcript | Lesson evidence for explanations, examples and warnings. |
| Screenshot PDF | Visual backup only; not text-searchable. |
| Pearson/Edexcel exercise references in slides | Source labels only; not treated as CCEA authority. |

---

## Final Student Checklist

### Normal distribution foundations

- [ ] I can explain why the normal distribution is used for continuous variables.
- [ ] I know that the total area under the normal curve is `1`.
- [ ] I know that the normal distribution is symmetrical.
- [ ] I know that for a normal distribution:

\[
\text{mean}=\text{median}=\text{mode}.
\]

- [ ] I can interpret:

\[
X\sim N(\mu,\sigma^2).
\]

- [ ] I can identify `mu`, `sigma`, and `sigma^2`.

### Probability calculations

- [ ] I can find left-tail probabilities.
- [ ] I can find right-tail probabilities.
- [ ] I can find interval probabilities.
- [ ] I can find outside-region probabilities using the complement.
- [ ] I know that for continuous `X`:

\[
P(X>a)=P(X\geq a).
\]

### Inverse normal and standardising

- [ ] I can use inverse normal when a probability is given and a boundary is unknown.
- [ ] I can convert right-tail areas into left-tail areas.
- [ ] I can standardise using:

\[
Z=\frac{X-\mu}{\sigma}.
\]

- [ ] I can use standardising to find missing `mu` or `sigma`.

### Binomial-to-normal approximation

- [ ] I know that if

\[
X\sim B(n,p),
\]

then the normal approximation is:

\[
Y\sim N(np,np(1-p)).
\]

- [ ] I can apply continuity corrections.
- [ ] I know when a binomial model has two outcomes, fixed trials, independence and constant probability.
- [ ] I can explain that a normal approximation may be poor if the binomial distribution is too skewed or `n` is too small.

### Hypothesis testing with the normal mean

- [ ] I can write `H_0` and `H_1` correctly.
- [ ] I can tell whether a test is one-tailed or two-tailed.
- [ ] I can use:

\[
\bar X\sim N\left(\mu,\frac{\sigma^2}{n}\right).
\]

- [ ] I can calculate a p-value.
- [ ] I can compare the p-value with the significance level.
- [ ] I can write a conclusion in context.
