# 1. Lesson Title and Metadata

| Field | Value |
|---|---|
| Date generated | 2026-06-04 |
| Course | CCEA GCE Further Mathematics |
| Unit | `FAS2`: Further AS 2 Applied Mathematics |
| Applied section | Section C: Statistics |
| Topic code | `FAS2-DIST` |
| Topic name | Statistical distributions: Poisson Distribution |
| Topic slug | `poisson_distribution` |
| Topic Pascal | `PoissonDistribution` |
| Topic ID | `FAS2PoissonDistribution` |
| Lesson file name | `FAS2_poisson_distribution_lesson.md` |
| Core LO IDs | `FAS2-DIST-LO007`, `FAS2-DIST-LO008` |
| Supporting LO IDs | `FAS2-DIST-LO002`, `FAS2-DIST-LO003` |
| Bridge tags | ordinary probability, binomial distribution, cumulative probabilities, independent events, mean and variance |
| Topic tags | `#FAS2`, `#DIST`, `#Statistics`, `#Distributions`, `#Poisson`, `#DiscreteDistribution`, `#RateModel`, `#SectionC` |

## Lesson Title

# Poisson Distribution

## Student-facing description

This lesson teaches how to model the **number of events** occurring in a fixed interval of time, space, length, area or volume when the events happen at an **average rate**.

The Poisson distribution is the probability model you reach for when the question is not asking:

> “How many successes out of a fixed number of trials?”

but instead asks:

> “How many events occur in this interval, given the average rate?”

That is the key doorway. Binomial counts successes in a pre-built row of boxes. Poisson counts little event-sparks in a stretch of time or space. Same probability universe, different creature. 🜁

# 2. Evidence Map

| Source | Evidence used in this lesson | Lesson sections supported |
|---|---|---|
| Project Source: CCEA Further Mathematics specification map | FAS2-DIST learning outcomes and boundaries | Sections 3, 4, 16, 18 |
| Project Source: Further Maths module map | FAS2-DIST is Section C Statistics | Sections 1, 3 |
| Project Source: Ordinary A-Level bridge extracts | Binomial, probability, independence, cumulative probability, mean and variance | Sections 5, 8, 12 |
| `FS1-Chp2-PoissonDistribution.pdf` | Definition of Poisson, binomial-to-Poisson motivation, examples, table use, modelling assumptions, mean and variance | Sections 6, 7, 8, 9, 11, 12 |
| `transcripts.md` | Teacher explanation of Poisson as related to binomial, rate scaling, calculator use, modelling assumptions and common warnings | Sections 5, 6, 8, 12, 15 |
| `Chapter_2_Poisson_Distribution_📊_(Further_Statistics_1)_screenshots.pdf` | Visual evidence for motivation contexts and diagrams | Sections 9, 17 |
| Cross-board/Pearson-style examples | Used where matching CCEA FAS2-DIST; boundary-risk examples logged separately | Sections 11, 16, 17 |

The slide PDF states that the Poisson distribution counts how many events occur within some period of time, given an average rate, and compares this with the binomial model as counting successes out of fixed trials. The transcript reinforces the bridge by saying students should already have met the binomial distribution in ordinary A-Level Maths before this topic.

# 3. Specification Alignment

| LO ID | Official wording | Lesson coverage | Evidence source | Syllabus boundary | Ordinary A-Level bridge |
|---|---|---|---|---|---|
| `FAS2-DIST-LO002` | Demonstrate understanding of and use discrete probability distributions, including probability functions, mean, variance and standard deviation | Poisson as a discrete distribution over $0,1,2,\ldots$; probability function; mean and variance | CCEA Project Source; PDF/transcript evidence | Core supporting LO | Discrete random variables from ordinary Statistics |
| `FAS2-DIST-LO003` | Calculate probabilities such as $P(a\leq X\leq b)$, $E(X)$ and $\operatorname{Var}(X)$ for simple cases of a discrete random variable $X$ | Point probabilities, cumulative probabilities, complements, interval probabilities | CCEA Project Source; PDF page on examples and tables | Core supporting LO | Probability inequalities and cumulative methods |
| `FAS2-DIST-LO007` | Demonstrate understanding of and use the Poisson distribution as a model, including the calculation of probabilities using the Poisson distribution | Model selection, assumptions, rate scaling, calculation of probabilities | CCEA Project Source; PDF/transcript evidence | Primary core LO | Binomial distribution and probability modelling |
| `FAS2-DIST-LO008` | Use the expressions for the mean and variance of the binomial, geometric and Poisson distributions | $E(X)=\lambda$, $\operatorname{Var}(X)=\lambda$; comparison with binomial $E(X)=np$ and $\operatorname{Var}(X)=np(1-p)$ | CCEA Project Source; PDF/transcript evidence | Primary core LO | Mean, variance and binomial distribution |

# 4. Learning Objectives

## Core Further Maths objectives

By the end of this lesson, you should be able to:

1. Recognise when a situation may be modelled by a Poisson distribution.
2. Write suitable notation such as
   $$
   X\sim \operatorname{Po}(\lambda).
   $$
3. Explain what $\lambda$ represents as an average rate or mean number of events in the chosen interval.
4. Scale $\lambda$ when the interval changes, for example from per hour to per $90$ minutes.
5. Use the Poisson probability formula:
   $$
   P(X=x)=\frac{e^{-\lambda}\lambda^x}{x!}.
   $$
6. Calculate exact probabilities such as $P(X=3)$.
7. Calculate cumulative and interval probabilities such as $P(X<5)$, $P(X\geq 3)$ and $P(2\leq X\leq 5)$.
8. Use the facts
   $$
   E(X)=\lambda,\qquad \operatorname{Var}(X)=\lambda.
   $$
9. Use the similarity of sample mean and variance as evidence that a Poisson model may be suitable.
10. State modelling assumptions: events occur singly, independently and at a constant rate.

## Bridge objectives

You should also be able to:

1. Explain how Poisson extends ordinary A-Level binomial thinking.
2. Distinguish fixed-trial questions from rate-over-interval questions.
3. Translate ordinary probability language into discrete inequalities.
4. Use complement methods confidently:
   $$
   P(X\geq 1)=1-P(X=0),
   $$
   $$
   P(X\geq 3)=1-P(X\leq 2).
   $$

## Exam technique objectives

You should be able to:

1. Define the random variable before calculating.
2. State the correct interval attached to $\lambda$.
3. Convert strict inequalities carefully.
4. Avoid using a calculator result without showing the probability statement.
5. Interpret final answers in context.

# 5. Explicit Prerequisite Recap

## GCSE foundations

You should already be comfortable with:

| GCSE idea | Why it matters here |
|---|---|
| Whole-number counts | Poisson outcomes are $0,1,2,\ldots$ |
| Factorials such as $3!$ | The formula uses $x!$ |
| Powers and indices | The formula uses $\lambda^x$ |
| Decimals and rounding | Probabilities are often rounded to $3$ or $4$ significant figures |
| Basic probability scale | Probabilities must lie between $0$ and $1$ |

## Ordinary AS/A2 Mathematics foundations

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| Ordinary probability | Probability notation, complements, independent events | Poisson uses the same notation but with a new distribution | Writing $P(X<5)$ as $P(X\leq 5)$ is wrong because $X$ is discrete |
| Binomial distribution | $X\sim B(n,p)$ counts successes in $n$ trials | Poisson counts events in an interval using $\lambda$ as the average rate | Do not invent $n$ unless the model is genuinely binomial |
| Cumulative probability | Tables/calculator can find $P(X\leq k)$ | Poisson CDF works similarly | Strict and inclusive inequalities must be converted carefully |
| Mean and variance | Random variables have expected value and spread | Poisson has the special property $E(X)=\operatorname{Var}(X)=\lambda$ | If sample mean and variance are far apart, the model may be questionable |
| Exponential function | $e^x$ appears in growth/decay and calculus | Poisson uses $e^{-\lambda}$ | Do not treat $e$ as a variable |

### A-Level Maths Bridge: What You Already Know and What Further Maths Changes

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| Ordinary probability | Events, complements, independent events and conditional probability language | Poisson uses the same probability notation with a rate-based discrete distribution | Translating words such as “less than”, “at least” and “between” incorrectly changes the answer |
| Ordinary A-Level binomial distribution | $X\sim B(n,p)$ counts successes in a fixed number of trials | Poisson counts events in a fixed interval using an average rate $\lambda$ | Old binomial habits become risky if you invent a fixed $n$ when no fixed trial count exists |
| Ordinary cumulative probability | Tables and calculator functions give running totals like $P(X\leq k)$ | Poisson CDFs use the same left-tail logic | Because $X$ is discrete, $P(X<5)=P(X\leq4)$, not $P(X\leq5)$ |
| Ordinary mean and variance | Mean and variance describe centre and spread | For Poisson, $E(X)=\operatorname{Var}(X)=\lambda$ | If sample mean and variance are very different, the model may be poor |

In ordinary A-Level Maths, this idea appeared as **binomial distribution**: a fixed number of trials, each with success/failure and fixed probability $p$.

In Further Maths, the same idea becomes more flexible. Instead of a fixed row of $n$ trials, the Poisson distribution imagines events occurring across a stretch of time, length, area or volume. You do not ask, “How many successes out of $n$ trials?” You ask, “How many events occur in this interval?”

The key upgrade is that the parameter is no longer $p$ by itself. The important number is the **average rate**:
$$
\lambda.
$$

The danger is trying to force every question into binomial clothes. If the question says “per hour”, “per metre”, “per square”, “at a rate of”, or “on average”, Poisson may be whispering from the wings.

# 6. Big Picture Explanation

The Poisson distribution exists because many real situations are not naturally made of a fixed number of attempts.

For example:

- cars passing a checkpoint in an hour;
- calls arriving at a call centre in a day;
- defects in a length of material;
- particles emitted in a time period;
- flowers in a square metre of field;
- chocolate chips in a biscuit.

In these situations, the number of possible events has no obvious upper limit. A call centre might receive $0$ calls, $1$ call, $2$ calls, and so on. There is no fixed maximum in the same way that a binomial model has a maximum of $n$ successes.

The evidence introduces the Poisson distribution by comparing it with the binomial distribution. Binomial is described as counting the number of successes out of $n$ trials, each with probability $p$, while Poisson counts how many events occur in a period of time, given an average rate $\lambda$.

The slide evidence gives this key teaching question:

> Calculate the probability of $8$ cars passing in the next hour, given that on average $5$ pass an hour.

The first instinct is to chop the hour into time slots and pretend each slot is a binomial trial. But the transcript warns that the binomial approach becomes awkward because more than one car could pass in the same time slot, so the count of successes may not equal the count of cars.

The Poisson model fixes this by imagining the interval split into infinitely small slivers. In a tiny enough sliver, at most one event can occur. Then the count of successes really does become the count of events.

That is the big probability engine under the bonnet.

# 7. Key Definitions and Notation

## 7.1 Random variable

A **random variable** is a variable whose value depends on chance.

In this lesson, $X$ usually represents a count, for example:

$$
X=\text{the number of cars passing a point in one hour}.
$$

or

$$
Y=\text{the number of calls received in a 30 minute interval}.
$$

## 7.2 Poisson distribution

A random variable $X$ has a **Poisson distribution** with parameter $\lambda$ if it counts the number of events occurring in an interval where the events happen at average rate $\lambda$.

We write:

$$
X\sim \operatorname{Po}(\lambda).
$$

Some lesson evidence writes this as:

$$
X\sim Po(\lambda).
$$

Both mean the same thing, but this lesson will use:

$$
\operatorname{Po}(\lambda)
$$

for clear typesetting.

## 7.3 The parameter $\lambda$

The symbol $\lambda$ is the Greek letter **lambda**.

It represents the mean number of events in the interval you are currently using.

Examples:

| Situation | Meaning of $\lambda$ |
|---|---|
| $5$ cars per hour | $\lambda=5$ for a one-hour interval |
| $1.2$ emails per hour | $\lambda=1.2$ for a one-hour interval |
| $2.5$ radios sold per week | $\lambda=2.5$ for a one-week interval |
| $0.8$ flowers per square metre | $\lambda=0.8$ for a one-square-metre area |

The interval is part of the parameter. That little detail is a gremlin-trap. If the interval changes, $\lambda$ changes.

## 7.4 Probability function

If

$$
X\sim \operatorname{Po}(\lambda),
$$

then

$$
P(X=x)=\frac{e^{-\lambda}\lambda^x}{x!},
$$

where:

| Symbol | Meaning |
|---|---|
| $x$ | the exact number of events |
| $\lambda$ | the average number of events in the chosen interval |
| $e$ | the exponential constant |
| $x!$ | factorial, meaning $x(x-1)(x-2)\cdots 1$ for positive integers |

The slide PDF states the Poisson probability function in this form after explaining the limiting idea from binomial time-slicing.

## 7.5 Outcome set

For a Poisson random variable:

$$
X\in \{0,1,2,3,\ldots\}.
$$

There are no negative counts.

There is no fixed upper limit.

So:

$$
P(X=-1)=0,
$$

but values like $X=20$, $X=100$ or beyond are possible in principle, even if they may be very unlikely.

# 8. Core Theory

## 8.1 Binomial versus Poisson: the bridge that unlocks the topic

**Bridge Note:** In ordinary A-Level Maths, binomial distribution counted successes out of a fixed number of trials. Here, Further Maths extends this by counting events across an interval using a rate.

For a binomial distribution:

$$
X\sim B(n,p).
$$

This means:

- there are $n$ trials;
- each trial has two outcomes, success or failure;
- the probability of success is $p$;
- $X$ counts the number of successes;
- possible values are:
  $$
  X=0,1,2,\ldots,n.
  $$

For a Poisson distribution:

$$
X\sim \operatorname{Po}(\lambda).
$$

This means:

- events happen in an interval of time, length, area, volume or space;
- $\lambda$ is the average number of events in that interval;
- $X$ counts the number of events;
- possible values are:
  $$
  X=0,1,2,\ldots
  $$

There is no fixed maximum value.

### Comparison table

| Feature | Binomial | Poisson |
|---|---|---|
| Notation | $B(n,p)$ | $\operatorname{Po}(\lambda)$ |
| What is counted? | Successes | Events |
| Structure | Fixed number of trials | Fixed interval with average rate |
| Parameter(s) | $n$, $p$ | $\lambda$ |
| Outcomes | $0,1,\ldots,n$ | $0,1,2,\ldots$ |
| Typical wording | “out of $n$” | “at a rate of”, “on average”, “per hour”, “per cm” |

## 8.2 How Poisson arises from binomial thinking

The evidence uses this question:

> Calculate the probability of $8$ cars passing in the next hour, given that on average $5$ pass an hour.

Let:

$$
X=\text{the number of cars passing in one hour}.
$$

The average rate is:

$$
\lambda=5.
$$

Before using Poisson directly, the lesson evidence asks what happens if we try to model the hour with a binomial distribution.

### Step 1: Split the hour into 10 intervals

Suppose the hour from $2\text{pm}$ to $3\text{pm}$ is split into $10$ equal intervals.

Each interval has length:

$$
\frac{60}{10}=6\text{ minutes}.
$$

Treat each interval as a trial.

A “success” means:

$$
\text{a car passes during that interval}.
$$

If we expect $5$ cars per hour and there are $10$ time slots, then the probability of success in a slot is modelled as:

$$
p=\frac{5}{10}.
$$

So:

$$
p=0.5.
$$

Then a binomial approximation would be:

$$
X\sim B(10,0.5).
$$

The probability of exactly $8$ cars is approximated by:

$$
P(X=8)=\binom{10}{8}(0.5)^8(0.5)^2.
$$

Since

$$
\binom{10}{8}=45,
$$

we get:

$$
P(X=8)=45(0.5)^{10}.
$$

Now:

$$
(0.5)^{10}=\frac{1}{1024}.
$$

Therefore:

$$
P(X=8)=\frac{45}{1024}.
$$

So:

$$
P(X=8)=0.0439453125.
$$

To four decimal places:

$$
P(X=8)=0.0439.
$$

This matches the slide evidence value of $0.0439$ for the 10-slot binomial model.

### Step 2: Why this binomial model is flawed

The problem is that more than one car could pass in a single 6-minute interval.

For example, in the interval from $2{:}00$ to $2{:}06$:

- one car might pass at $2{:}01$;
- another might pass at $2{:}03$;
- another might pass at $2{:}05$.

The binomial model only records “success” or “failure” in that slot. It cannot record three separate cars in one slot.

So the count of successes is not necessarily the count of cars.

That is the crack in the binomial mask.

### Step 3: Split the hour into 20 intervals

Now split the hour into $20$ equal intervals.

Each interval has length:

$$
\frac{60}{20}=3\text{ minutes}.
$$

The average number of cars per hour is still:

$$
\lambda=5.
$$

Now:

$$
p=\frac{5}{20}.
$$

So:

$$
p=0.25.
$$

The binomial approximation becomes:

$$
X\sim B(20,0.25).
$$

For exactly $8$ cars:

$$
P(X=8)=\binom{20}{8}(0.25)^8(0.75)^{12}.
$$

Calculate the binomial coefficient:

$$
\binom{20}{8}=\frac{20!}{8!12!}.
$$

So:

$$
P(X=8)=\frac{20!}{8!12!}(0.25)^8(0.75)^{12}.
$$

The evidence gives the result:

$$
P(X=8)=0.0609
$$

to four decimal places.

This is already closer to the true Poisson value than $0.0439$.

### Step 4: Let the number of intervals become very large

If we keep increasing the number of intervals, the interval length becomes smaller and smaller.

Let:

$$
n=\text{number of time intervals}.
$$

Then:

$$
p=\frac{\lambda}{n}.
$$

For the cars example:

$$
p=\frac{5}{n}.
$$

The binomial model is:

$$
X\sim B\left(n,\frac{\lambda}{n}\right).
$$

The binomial probability for exactly $x$ events is:

$$
P(X=x)=\binom{n}{x}\left(\frac{\lambda}{n}\right)^x\left(1-\frac{\lambda}{n}\right)^{n-x}.
$$

Now let:

$$
n\to\infty.
$$

Then the time intervals become infinitely small. In an infinitely small time slice, it becomes acceptable to treat the event as either happening once or not happening.

The Poisson probability function is the limiting result:

$$
P(X=x)=\lim_{n\to\infty}\binom{n}{x}\left(\frac{\lambda}{n}\right)^x\left(1-\frac{\lambda}{n}\right)^{n-x}.
$$

The result is:

$$
P(X=x)=\frac{e^{-\lambda}\lambda^x}{x!}.
$$

The PDF states this limiting idea and notes that the proof is not required at this point.

## 8.3 The Poisson probability formula

If:

$$
X\sim \operatorname{Po}(\lambda),
$$

then:

$$
P(X=x)=\frac{e^{-\lambda}\lambda^x}{x!}.
$$

### Example: cars passing in an hour

Let:

$$
X=\text{the number of cars passing in the next hour}.
$$

Given that on average $5$ cars pass per hour:

$$
X\sim \operatorname{Po}(5).
$$

We want:

$$
P(X=8).
$$

Use the formula:

$$
P(X=8)=\frac{e^{-5}5^8}{8!}.
$$

Now:

$$
8!=8\times7\times6\times5\times4\times3\times2\times1.
$$

So:

$$
8!=40320.
$$

Therefore:

$$
P(X=8)=\frac{e^{-5}5^8}{40320}.
$$

Using a calculator:

$$
P(X=8)=0.0652780393\ldots
$$

So to four decimal places:

$$
P(X=8)=0.0653.
$$

The transcript gives the same “true” Poisson value of $0.0653$ and explains that the 20-slot binomial approximation was close, but not exact.

## 8.4 Calculating exact Poisson probabilities

### General method

To find an exact probability:

1. Define the random variable.
2. Identify the correct interval.
3. Find $\lambda$ for that interval.
4. Write the distribution.
5. Substitute into:
   $$
   P(X=x)=\frac{e^{-\lambda}\lambda^x}{x!}.
   $$
6. Round appropriately.

### Worked mini-example from evidence

Given:

$$
X\sim \operatorname{Po}(1.2),
$$

find:

$$
P(X=3).
$$

Here:

$$
\lambda=1.2,
$$

and:

$$
x=3.
$$

Use:

$$
P(X=x)=\frac{e^{-\lambda}\lambda^x}{x!}.
$$

So:

$$
P(X=3)=\frac{e^{-1.2}(1.2)^3}{3!}.
$$

Now:

$$
3!=3\times2\times1=6.
$$

Also:

$$
(1.2)^3=1.728.
$$

Therefore:

$$
P(X=3)=\frac{e^{-1.2}\times1.728}{6}.
$$

Using a calculator:

$$
P(X=3)=0.086743933\ldots
$$

To four decimal places:

$$
P(X=3)=0.0867.
$$

This is the value shown in the PDF example slide.

## 8.5 Complements with Poisson probabilities

**Bridge Note:** In ordinary A-Level Maths, complements helped avoid adding many probabilities. Here, the same trick is essential because a Poisson distribution has no fixed upper limit.

Suppose:

$$
X\sim \operatorname{Po}(1.2).
$$

Find:

$$
P(X\geq 1).
$$

The possible values of $X$ are:

$$
0,1,2,3,\ldots
$$

The event $X\geq 1$ means:

$$
1,2,3,\ldots
$$

That is every possible value except $0$.

So:

$$
P(X\geq 1)=1-P(X=0).
$$

Now:

$$
P(X=0)=\frac{e^{-1.2}(1.2)^0}{0!}.
$$

Use:

$$
(1.2)^0=1
$$

and

$$
0!=1.
$$

So:

$$
P(X=0)=e^{-1.2}.
$$

Therefore:

$$
P(X\geq 1)=1-e^{-1.2}.
$$

Using a calculator:

$$
P(X\geq 1)=1-0.3010\ldots
$$

So:

$$
P(X\geq 1)=0.6988\ldots
$$

To three decimal places:

$$
P(X\geq 1)=0.699.
$$

## 8.6 Interval probabilities with Poisson

Suppose:

$$
X\sim \operatorname{Po}(1.2).
$$

Find:

$$
P(3<X\leq 5).
$$

Because $X$ is discrete, the values satisfying

$$
3<X\leq 5
$$

are:

$$
4,\ 5.
$$

So:

$$
P(3<X\leq 5)=P(X=4)+P(X=5).
$$

Now:

$$
P(X=4)=\frac{e^{-1.2}(1.2)^4}{4!}.
$$

And:

$$
P(X=5)=\frac{e^{-1.2}(1.2)^5}{5!}.
$$

Therefore:

$$
P(3<X\leq 5)=\frac{e^{-1.2}(1.2)^4}{4!}+\frac{e^{-1.2}(1.2)^5}{5!}.
$$

Calculate:

$$
P(X=4)=0.0260\ldots
$$

and:

$$
P(X=5)=0.0062\ldots
$$

So:

$$
P(3<X\leq 5)=0.0322\ldots
$$

To four decimal places:

$$
P(3<X\leq 5)=0.0323.
$$

## 8.7 Cumulative distribution function and tables

The cumulative distribution function gives a running total:

$$
P(X\leq k).
$$

The PDF states that, as with the binomial distribution, tables can be used for the cumulative distribution function of a Poisson distribution, and a calculator can also be used with Poisson cumulative mode.

### Example: cars on a country road

On average, $8$ cars come down a country road in an hour.

Let:

$$
X=\text{the number of cars passing in the next hour}.
$$

Then:

$$
X\sim \operatorname{Po}(8).
$$

#### Part a: Less than 5 cars

Find:

$$
P(X<5).
$$

Since $X$ is discrete:

$$
X<5
$$

means:

$$
X\leq 4.
$$

So:

$$
P(X<5)=P(X\leq 4).
$$

Using Poisson cumulative tables or calculator:

$$
P(X\leq 4)=0.0996.
$$

Therefore:

$$
P(X<5)=0.0996.
$$

#### Part b: At least 3 cars

Find:

$$
P(X\geq 3).
$$

The event $X\geq 3$ means:

$$
3,4,5,\ldots
$$

It is easier to subtract the values not included:

$$
0,1,2.
$$

So:

$$
P(X\geq 3)=1-P(X\leq 2).
$$

Using tables or calculator:

$$
P(X\leq 2)=0.0138.
$$

Therefore:

$$
P(X\geq 3)=1-0.0138.
$$

So:

$$
P(X\geq 3)=0.9862.
$$

#### Part c: Between 2 and 5 inclusive

Find:

$$
P(2\leq X\leq 5).
$$

This means:

$$
X=2,3,4,5.
$$

Using cumulative probabilities:

$$
P(2\leq X\leq 5)=P(X\leq 5)-P(X\leq 1).
$$

From tables or calculator:

$$
P(X\leq 5)=0.1912,
$$

and:

$$
P(X\leq 1)=0.0030.
$$

Therefore:

$$
P(2\leq X\leq 5)=0.1912-0.0030.
$$

So:

$$
P(2\leq X\leq 5)=0.1882.
$$

## 8.8 Backwards use of cumulative tables

Sometimes you are given a probability and asked to find the integer boundary.

Suppose:

$$
X\sim \operatorname{Po}(7.5).
$$

Find $a,b,c$ if:

$$
P(X\leq a)=0.2414,
$$

$$
P(X<b)=0.5246,
$$

$$
P(X\geq c)=0.3380.
$$

### Part a

From the Poisson cumulative table for $\lambda=7.5$:

$$
P(X\leq 5)=0.2414.
$$

So:

$$
a=5.
$$

### Part b

We are told:

$$
P(X<b)=0.5246.
$$

For a discrete random variable:

$$
X<b
$$

means:

$$
X\leq b-1.
$$

From the table:

$$
P(X\leq 7)=0.5246.
$$

So:

$$
b-1=7.
$$

Therefore:

$$
b=8.
$$

### Part c

We are told:

$$
P(X\geq c)=0.3380.
$$

Use the complement:

$$
P(X\geq c)=1-P(X\leq c-1).
$$

So:

$$
1-P(X\leq c-1)=0.3380.
$$

Rearrange:

$$
P(X\leq c-1)=1-0.3380.
$$

Thus:

$$
P(X\leq c-1)=0.6620.
$$

From the table:

$$
P(X\leq 8)=0.6620.
$$

So:

$$
c-1=8.
$$

Therefore:

$$
c=9.
$$

The transcript warns that calculators may not handle backwards discrete distribution questions neatly, so students should be comfortable reading tables directly.

## 8.9 Modelling assumptions for a Poisson distribution

A Poisson model is not just a formula. It is a **model**, so the assumptions matter.

For a Poisson distribution to be suitable, the events should occur:

1. **Singly** in time, space, length, area or volume.
2. **Independently** of each other.
3. **At a constant rate**, meaning the mean number of occurrences is proportional to the length/size of the interval.

The slide evidence states these three restrictions explicitly and adds that events are treated as instantaneous, so multiple events should not occur “at once” in the model. It also notes that exam questions often signal Poisson by using the word **rate**.

### Assumption 1: Events occur singly

This means that the model treats events as separate little countable sparks.

If:

$$
X=\text{the number of website hits in one minute},
$$

then each hit is counted as a separate event.

A Poisson model assumes that two hits do not occur at exactly the same instant. In practice, we often accept this as a modelling simplification.

### Assumption 2: Events occur independently

This means that one event happening does not make another event more or less likely.

For example, if a website receives a hit at $10{:}00{:}01$, the model assumes this does not change the chance of another hit at $10{:}00{:}02$.

This assumption can fail in real life.

For example, if people share a link on social media, one hit may trigger more hits. That would weaken the independence assumption.

### Assumption 3: Events occur at a constant rate

If the average rate is $6$ events per hour, then the model assumes:

$$
3\text{ events per half hour},
$$

$$
12\text{ events per two hours},
$$

and so on.

The rate scales proportionally with the size of the interval.

This does **not** mean the actual observed count is constant. It means the long-run average rate is constant.

## 8.10 Deciding whether Poisson is suitable

**Bridge Note:** In ordinary A-Level Maths, you checked whether binomial conditions were reasonable: fixed $n$, fixed $p$, independence, two outcomes. Here, Further Maths asks you to check a different model: rate-based counts.

### Example: website hits

A website receives hits at a rate of $300$ per hour.

State a suitable distribution for the number of hits during a $1$ minute interval.

Since:

$$
300\text{ hits per hour}
$$

and:

$$
1\text{ hour}=60\text{ minutes},
$$

the mean number of hits per minute is:

$$
\lambda=\frac{300}{60}=5.
$$

Let:

$$
X=\text{the number of hits during a 1 minute interval}.
$$

Then:

$$
X\sim \operatorname{Po}(5).
$$

Two suitable reasons are:

- hits occur singly in time;
- hits are independent, or occur randomly;
- hits occur at a constant rate.

The slide evidence includes this exact exam-style reasoning and gives the mark-scheme style reasons: hits occur singly in time, independently/randomly, and at a constant rate.

### Example: volcano eruptions

A volcano erupts every $1000$ years. We are interested in the probability of at least one eruption next year.

This is **not** a good Poisson model if an eruption today makes another eruption next year less likely.

The independence assumption is doubtful.

So the issue is not the long average. The issue is that events may not be independent.

### Example: buses

A bus comes $10$ times per hour on average.

Could we model the number of buses arriving in the next hour using a Poisson distribution?

Usually, no.

Buses are normally scheduled. The chance of a bus arriving spikes near timetable times. The arrivals are not equally likely at every moment.

The slide evidence says this is “definitely not” Poisson because buses intend to arrive at regular intervals, not randomly.

### Example: call centre calls

A call centre receives on average $80$ calls per hour.

Could we model the number of calls in an hour using a Poisson distribution?

Yes, it may be reasonable, provided:

- the rate is roughly constant;
- calls are independent;
- calls are treated as occurring singly;
- repeat calls from the same customer are not causing dependence.

The evidence accepts this as justified if the average rate is constant, while noting the simplifying assumption about repeat calls.

## 8.11 Scaling the rate

The parameter $\lambda$ must match the exact interval in the question.

This is one of the biggest exam traps in the topic.

If the rate is:

$$
4\text{ per hour},
$$

then for $90$ minutes:

$$
90\text{ minutes}=1.5\text{ hours}.
$$

So:

$$
\lambda=4\times1.5=6.
$$

The transcript explicitly warns that we often need to scale the rate to the required time period or length, for example from one hour to $90$ minutes.

### General scaling rule

If the original rate is:

$$
\lambda_0\text{ events per original interval},
$$

and the new interval is $k$ times as long, then:

$$
\lambda_{\text{new}}=k\lambda_0.
$$

### Common scaling examples

| Given rate | Required interval | Scaling | New $\lambda$ |
|---|---:|---:|---:|
| $5$ per hour | $2$ hours | $5\times2$ | $10$ |
| $5$ per hour | $30$ minutes | $5\times\frac12$ | $2.5$ |
| $1.2$ per hour | $90$ minutes | $1.2\times1.5$ | $1.8$ |
| $0.5$ per $10$ cm | $100$ cm | $0.5\times10$ | $5$ |
| $2.5$ per week | $4$ weeks | $2.5\times4$ | $10$ |

### Worked scaling example: failed internet connections

An internet service provider has a large number of users regularly connecting to the internet. On average, $4$ users every hour fail to connect on their first attempt.

Let:

$$
X=\text{the number of users failing to connect on their first attempt in one hour}.
$$

Then:

$$
X\sim \operatorname{Po}(4).
$$

#### Find the probability that exactly 2 users fail to connect in one hour

We need:

$$
P(X=2).
$$

Use:

$$
P(X=x)=\frac{e^{-\lambda}\lambda^x}{x!}.
$$

Here:

$$
\lambda=4,\qquad x=2.
$$

So:

$$
P(X=2)=\frac{e^{-4}4^2}{2!}.
$$

Since:

$$
4^2=16
$$

and:

$$
2!=2,
$$

we get:

$$
P(X=2)=\frac{16e^{-4}}{2}.
$$

So:

$$
P(X=2)=8e^{-4}.
$$

Using a calculator:

$$
P(X=2)=0.1465251111\ldots
$$

To four decimal places:

$$
P(X=2)=0.1465.
$$

The transcript gives the same value, $0.1465$, for the one-hour failed-connection example.

#### Find the probability that more than 6 users fail to connect in one hour

We need:

$$
P(X>6).
$$

Because $X$ is discrete:

$$
X>6
$$

means:

$$
X\geq7.
$$

Use the complement:

$$
P(X>6)=1-P(X\leq6).
$$

Using Poisson cumulative probability with $\lambda=4$:

$$
P(X\leq6)=0.8893260216\ldots
$$

Therefore:

$$
P(X>6)=1-0.8893260216\ldots
$$

So:

$$
P(X>6)=0.1106739784\ldots
$$

To four decimal places:

$$
P(X>6)=0.1107.
$$

The transcript gives $0.1107$ for this calculation.

#### Find probabilities in a 90 minute interval

Now let:

$$
Y=\text{the number of users failing to connect on their first attempt in a 90 minute period}.
$$

Since:

$$
90\text{ minutes}=1.5\text{ hours},
$$

and the rate is $4$ per hour:

$$
\lambda=4\times1.5=6.
$$

So:

$$
Y\sim \operatorname{Po}(6).
$$

##### Probability that exactly 5 users fail to connect

We need:

$$
P(Y=5).
$$

Use:

$$
P(Y=5)=\frac{e^{-6}6^5}{5!}.
$$

Now:

$$
5!=120,
$$

and:

$$
6^5=7776.
$$

So:

$$
P(Y=5)=\frac{7776e^{-6}}{120}.
$$

Using a calculator:

$$
P(Y=5)=0.1606231410\ldots
$$

To four decimal places:

$$
P(Y=5)=0.1606.
$$

##### Probability that fewer than 7 users fail to connect

We need:

$$
P(Y<7).
$$

Since $Y$ is discrete:

$$
P(Y<7)=P(Y\leq6).
$$

Using a calculator or table:

$$
P(Y\leq6)=0.6063027824\ldots
$$

To four decimal places:

$$
P(Y<7)=0.6063.
$$

The transcript stresses that the random variable should be redefined when the interval changes, because the one-hour variable and $90$ minute variable have different $\lambda$ values.

## 8.12 Mean and variance of the Poisson distribution

If:

$$
X\sim \operatorname{Po}(\lambda),
$$

then:

$$
E(X)=\lambda,
$$

and:

$$
\operatorname{Var}(X)=\lambda.
$$

So the Poisson distribution has a special property:

$$
E(X)=\operatorname{Var}(X).
$$

The transcript states that for a Poisson distribution, both the expected value and the variance are $\lambda$, and that this can help assess whether a Poisson model is suitable.

### Standard deviation

The standard deviation is the square root of the variance.

So if:

$$
X\sim \operatorname{Po}(\lambda),
$$

then:

$$
\sigma=\sqrt{\operatorname{Var}(X)}.
$$

Since:

$$
\operatorname{Var}(X)=\lambda,
$$

we get:

$$
\sigma=\sqrt{\lambda}.
$$

### Example

If:

$$
X\sim \operatorname{Po}(9),
$$

then:

$$
E(X)=9,
$$

$$
\operatorname{Var}(X)=9,
$$

and:

$$
\sigma=\sqrt9=3.
$$

### Suitability check using mean and variance

If data has sample mean close to sample variance, a Poisson model may be sensible.

For example, if a sample gives:

$$
\bar{x}=3.69
$$

and:

$$
s^2=3.72,
$$

then these values are close.

So:

$$
\bar{x}\approx s^2.
$$

This supports, but does not prove, the use of a Poisson model.

A model is still only a model. The assumptions of independent, singly occurring events at a constant rate still matter.

## 8.13 Stock and “running out” problems

These are reverse cumulative probability questions wearing a shopkeeper’s apron.

### Evidence example: radios

A shop sells radios at a rate of $2.5$ per week.

#### Part a: Two-week period, at least 7 radios

Let:

$$
X=\text{the number of radios sold in a two-week period}.
$$

The rate is:

$$
2.5\text{ per week}.
$$

For two weeks:

$$
\lambda=2.5\times2=5.
$$

So:

$$
X\sim \operatorname{Po}(5).
$$

We want:

$$
P(X\geq7).
$$

Use the complement:

$$
P(X\geq7)=1-P(X\leq6).
$$

Using tables or calculator:

$$
P(X\leq6)=0.7621834629\ldots
$$

Therefore:

$$
P(X\geq7)=1-0.7621834629\ldots
$$

So:

$$
P(X\geq7)=0.2378165370\ldots
$$

To four decimal places:

$$
P(X\geq7)=0.2378.
$$

The slide evidence gives this result for the radios example.

#### Part b: Four-week period, fewer than 12 radios

Let:

$$
Y=\text{the number of radios sold in a four-week period}.
$$

For four weeks:

$$
\lambda=2.5\times4=10.
$$

So:

$$
Y\sim \operatorname{Po}(10).
$$

We want:

$$
P(Y<12).
$$

Since $Y$ is discrete:

$$
P(Y<12)=P(Y\leq11).
$$

Using tables or calculator:

$$
P(Y\leq11)=0.6967761463\ldots
$$

Therefore:

$$
P(Y<12)=0.6968
$$

to four decimal places.

The slide evidence gives this result as $0.6968$.

#### Part c: Minimum stock so probability of running out is less than 0.01

Let:

$$
s=\text{the number of radios in stock immediately after delivery}.
$$

The shop runs out if demand exceeds stock.

So:

$$
Y>s.
$$

The manager wants:

$$
P(Y>s)<0.01.
$$

Use the complement.

Since:

$$
P(Y>s)=1-P(Y\leq s),
$$

we require:

$$
1-P(Y\leq s)<0.01.
$$

Subtract $1$ from both sides:

$$
-P(Y\leq s)<-0.99.
$$

Multiply by $-1$ and reverse the inequality:

$$
P(Y\leq s)>0.99.
$$

Now use the cumulative table for:

$$
Y\sim \operatorname{Po}(10).
$$

Check values:

$$
P(Y\leq17)=0.9857\ldots
$$

This is not enough, because:

$$
0.9857<0.99.
$$

Next:

$$
P(Y\leq18)=0.9928\ldots
$$

This is enough, because:

$$
0.9928>0.99.
$$

Therefore the smallest suitable stock is:

$$
s=18.
$$

So the manager should have:

$$
18
$$

radios in stock immediately after the delivery.

The transcript explains the same logic: running out means selling more than the amount in stock, so the condition $P(Y>s)<0.01$ is rewritten as $P(Y\leq s)>0.99$.

## 8.14 Mixed distribution warning

Some questions start with Poisson and then switch to binomial.

This happens when you first calculate the probability of an event happening in one interval, then repeat the interval a fixed number of times.

### Structure

Suppose:

$$
X=\text{the number of complaint emails received in one day}.
$$

You calculate:

$$
P(X<7)=0.157447\ldots
$$

Now suppose the office worker works $5$ days in a week, and the question asks for the probability that **at least two days** have fewer than $7$ complaint emails.

This new random variable is no longer counting emails.

It counts days.

Let:

$$
Y=\text{the number of days in the week on which fewer than 7 complaint emails are received}.
$$

There are:

$$
5
$$

days.

Each day either is a “success”:

$$
\text{fewer than 7 complaint emails}
$$

or not.

The probability of success is:

$$
p=0.157447\ldots
$$

So:

$$
Y\sim B(5,0.157447\ldots).
$$

Then:

$$
P(Y\geq2)=1-P(Y\leq1).
$$

The transcript describes this as a classic situation where one distribution is blended with another, and warns that the question can feel like it has “too much information.”

### Exam rule

Do not stay in Poisson mode just because the chapter is Poisson.

Ask:

> What is the random variable counting **now**?

If it is counting events in an interval, Poisson may be right.

If it is counting the number of successful intervals out of a fixed number of intervals, binomial may be right.

# 9. Visual Asset Integration

## 9.1 Evidence-backed visual placeholders

[VISUAL PLACEHOLDER: FAS2PoissonDistributionSVG-001 | Source: Screenshot PDF motivation slide + transcript motivation | Insert from svg/FAS2PoissonDistributionSVG-001.svg | Purpose: Show why Poisson matters through three rate-based contexts: coins per hour in a video game, A&E patients per half hour, and accidents per month. The visual must show each context as a separate card with the “is this real change or random fluctuation?” question preserved.]

[VISUAL PLACEHOLDER: FAS2PoissonDistributionSVG-002 | Source: FS1-Chp2-PoissonDistribution.pdf and transcript time-slicing explanation | Insert from svg/FAS2PoissonDistributionSVG-002.svg | Purpose: Show the movement from a 10-slot binomial model to a 20-slot binomial model to infinitely small time slices. The visual must label 2pm, 3pm, time slots, ticks for cars passing, $p=\lambda/n$, and the issue “more than one event could occur in a slot”.]

[VISUAL PLACEHOLDER: FAS2PoissonDistributionSVG-003 | Source: FS1-Chp2-PoissonDistribution.pdf comparison table | Insert from svg/FAS2PoissonDistributionSVG-003.svg | Purpose: Compare Binomial $B(n,p)$ with Poisson $\operatorname{Po}(\lambda)$ using columns for notation, description, parameter and outcomes.]

[VISUAL PLACEHOLDER: FAS2PoissonDistributionBridgeSVG-001 | Source: Ordinary A-Level Maths bridge + FAS2-DIST specification | Insert from svg/FAS2PoissonDistributionBridgeSVG-001.svg | Purpose: Compare prior ordinary Maths method with Further Maths extension: fixed trials versus average rate over an interval.]

[VISUAL PLACEHOLDER: FAS2PoissonDistributionTikZ-001 | Source: FS1-Chp2-PoissonDistribution.pdf probability distribution examples | Insert from tikz/FAS2PoissonDistributionTikZ-001.tex | Purpose: Provide a precise discrete bar chart for $X\sim\operatorname{Po}(\lambda)$, showing integer-only outcomes $0,1,2,\ldots$ and a peak near $\lambda$.]

[VISUAL PLACEHOLDER: FAS2PoissonDistributionTikZ-002 | Source: FS1-Chp2-PoissonDistribution.pdf cumulative probability section | Insert from tikz/FAS2PoissonDistributionTikZ-002.tex | Purpose: Show how strict inequalities convert for discrete variables, including $X<5\iff X\leq4$ and $X\geq3\iff 1-P(X\leq2)$.]

[VISUAL PLACEHOLDER: FAS2PoissonDistributionMermaid-001 | Source: CCEA FAS2-DIST boundary + lesson evidence | Insert from mermaid/FAS2PoissonDistributionMermaid-001.md | Purpose: Decision flowchart for choosing Poisson: count variable, fixed interval, average rate, singly, independently, constant rate.]

## 9.2 Visual evidence limitation

Diagram evidence is partially unclear here. The screenshot PDF is image-only and no text was parsed from it. The description above preserves the visible/readable details from the rendered file preview and the parsed slide PDF only. No uninspected visual detail is claimed.

## 9.3 AI-proposed visual enhancements

The following visuals are proposed teaching enhancements, not direct evidence-backed diagrams:

[VISUAL PLACEHOLDER: FAS2PoissonDistributionSVG-004 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from svg/FAS2PoissonDistributionSVG-004.svg | Purpose: Create a “lambda scaling machine” showing original rate, interval multiplier and new $\lambda$.]

[VISUAL PLACEHOLDER: FAS2PoissonDistributionSVG-005 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from svg/FAS2PoissonDistributionSVG-005.svg | Purpose: Show a model suitability checklist with three gates: singly, independently, constant rate.]

# 10. Interactive Learning Widgets

[INTERACTIVE PLACEHOLDER: FAS2PoissonDistributionWidget-001 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FAS2PoissonDistributionWidget-001.html | Purpose: Poisson probability calculator.]

The student inputs:

- $\lambda$;
- exact value $x$;
- inequality type: $=x$, $\leq x$, $<x$, $\geq x$, $>x$.

The widget displays:

- distribution notation:
  $$
  X\sim\operatorname{Po}(\lambda);
  $$
- formula substitution for exact probabilities:
  $$
  P(X=x)=\frac{e^{-\lambda}\lambda^x}{x!};
  $$
- final probability;
- inequality conversion for discrete outcomes.

It reinforces:

- formula substitution;
- exact versus cumulative probability;
- strict/inclusive inequality handling.

It checks errors such as:

- negative $x$;
- non-integer $x$;
- $\lambda\leq0$;
- using $P(X<5)$ as $P(X\leq5)$.

[INTERACTIVE PLACEHOLDER: FAS2PoissonDistributionWidget-002 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FAS2PoissonDistributionWidget-002.html | Purpose: Rate-scaling trainer.]

The student inputs:

- original rate;
- original interval;
- target interval;
- event context.

The widget displays:

- interval multiplier;
- new $\lambda$;
- distribution notation;
- a warning if the original and target intervals do not use compatible units.

It reinforces:

$$
\lambda_{\text{new}}=\lambda_{\text{old}}\times\frac{\text{new interval}}{\text{old interval}}.
$$

[INTERACTIVE PLACEHOLDER: FAS2PoissonDistributionWidget-003 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FAS2PoissonDistributionWidget-003.html | Purpose: Poisson model suitability checklist.]

The student selects yes/no for:

- Are we counting events?
- Is the interval fixed?
- Is an average rate given?
- Do events occur singly?
- Are events independent?
- Is the rate constant?

The widget displays:

- “Poisson likely”;
- “Poisson questionable”;
- “Not Poisson, consider another distribution”;
- a reasoned explanation.

# 11. Worked Examples

## Worked Example 1: Exact Poisson probability

### Evidence source

This example is based on the slide/PDF example where:

$$
X\sim\operatorname{Po}(1.2)
$$

and the task is to find:

$$
P(X=3).
$$

The PDF gives the calculation using the Poisson probability formula and the result $0.0867$.

### On-spec status

Core CCEA FAS2-DIST: calculating probabilities using the Poisson distribution.

### Ordinary Maths idea used

Substitution into a formula and factorial notation.

### Further Maths upgrade

Using the Poisson probability function for a count distribution with rate parameter $\lambda$.

### Question

Given:

$$
X\sim\operatorname{Po}(1.2),
$$

find:

$$
P(X=3).
$$

### Solution

Since:

$$
X\sim\operatorname{Po}(1.2),
$$

we have:

$$
\lambda=1.2.
$$

The probability function is:

$$
P(X=x)=\frac{e^{-\lambda}\lambda^x}{x!}.
$$

For:

$$
x=3,
$$

we get:

$$
P(X=3)=\frac{e^{-1.2}(1.2)^3}{3!}.
$$

Now calculate the factorial:

$$
3!=3\times2\times1.
$$

So:

$$
3!=6.
$$

Calculate the power:

$$
(1.2)^3=1.2\times1.2\times1.2.
$$

First:

$$
1.2\times1.2=1.44.
$$

Then:

$$
1.44\times1.2=1.728.
$$

So:

$$
(1.2)^3=1.728.
$$

Substitute:

$$
P(X=3)=\frac{e^{-1.2}\times1.728}{6}.
$$

Using a calculator:

$$
P(X=3)=0.0867439330\ldots
$$

Therefore, to four decimal places:

$$
P(X=3)=0.0867.
$$

### Final exam-style answer

$$
\boxed{0.0867}
$$

### Teaching note

The value $x=3$ goes into the power and the factorial. The parameter $\lambda=1.2$ goes into $e^{-\lambda}$ and $\lambda^x$. Do not swap them. That is the tiny algebra goblin under the floorboard.

---

## Worked Example 2: Website hits

### Evidence source

The PDF asks:

> Given that www.drfrostmaths.com receives $25$ hits a second on average, determine the probability it receives $20$ hits in the second.

### On-spec status

Core CCEA FAS2-DIST: using Poisson to calculate probabilities.

### Question

A website receives $25$ hits per second on average.

Find the probability that it receives exactly $20$ hits in a particular second.

### Solution

Let:

$$
X=\text{the number of hits received in one second}.
$$

The average rate is:

$$
25\text{ hits per second}.
$$

The interval in the question is one second, so:

$$
\lambda=25.
$$

Therefore:

$$
X\sim\operatorname{Po}(25).
$$

We need:

$$
P(X=20).
$$

Use:

$$
P(X=x)=\frac{e^{-\lambda}\lambda^x}{x!}.
$$

Substitute:

$$
P(X=20)=\frac{e^{-25}25^{20}}{20!}.
$$

Using a calculator:

$$
P(X=20)=0.0519174686\ldots
$$

To four decimal places:

$$
P(X=20)=0.0519.
$$

### Final exam-style answer

$$
\boxed{0.0519}
$$

### Teaching note

The phrase “on average” and the unit “per second” identify the rate. The interval in the question is also one second, so no scaling is needed.

---

## Worked Example 3: Failed internet connections

### Evidence source

This is based on the transcript modelling example where an internet service provider has, on average, $4$ users every hour failing to connect on their first attempt. The transcript gives $0.1465$ for exactly two failures in an hour and $0.1107$ for more than six failures in an hour.

### On-spec status

Core CCEA FAS2-DIST: modelling with Poisson and calculating probabilities.

### Question

An internet service provider has a large number of users regularly connecting to the internet. On average, $4$ users every hour fail to connect on their first attempt.

1. Give two reasons why a Poisson distribution may be suitable.
2. Find the probability that exactly $2$ users fail to connect in a randomly chosen hour.
3. Find the probability that more than $6$ users fail to connect in a randomly chosen hour.
4. Find the probability that exactly $5$ users fail to connect in a randomly chosen $90$ minute interval.

### Solution

#### Part 1: Model suitability

A Poisson distribution may be suitable because:

- failed connections occur singly in time;
- failed connections may be assumed independent;
- failed connections occur at a constant average rate.

Only two reasons are requested, so any two of these would be sufficient.

#### Part 2: Exactly 2 failures in one hour

Let:

$$
X=\text{the number of users failing to connect on their first attempt in one hour}.
$$

Since the mean rate is $4$ per hour:

$$
X\sim\operatorname{Po}(4).
$$

We need:

$$
P(X=2).
$$

Using the Poisson formula:

$$
P(X=2)=\frac{e^{-4}4^2}{2!}.
$$

Calculate:

$$
4^2=16
$$

and:

$$
2!=2.
$$

So:

$$
P(X=2)=\frac{16e^{-4}}{2}.
$$

Thus:

$$
P(X=2)=8e^{-4}.
$$

Using a calculator:

$$
P(X=2)=0.1465251111\ldots
$$

So:

$$
P(X=2)=0.1465
$$

to four decimal places.

#### Part 3: More than 6 failures in one hour

We need:

$$
P(X>6).
$$

Since $X$ is discrete:

$$
P(X>6)=P(X\geq7).
$$

Use the complement:

$$
P(X\geq7)=1-P(X\leq6).
$$

Using a calculator:

$$
P(X\leq6)=0.8893260216\ldots
$$

Therefore:

$$
P(X>6)=1-0.8893260216\ldots
$$

So:

$$
P(X>6)=0.1106739784\ldots
$$

To four decimal places:

$$
P(X>6)=0.1107.
$$

#### Part 4: Exactly 5 failures in 90 minutes

Now the interval has changed.

Since:

$$
90\text{ minutes}=1.5\text{ hours},
$$

the new mean is:

$$
\lambda=4\times1.5=6.
$$

Let:

$$
Y=\text{the number of users failing to connect on their first attempt in 90 minutes}.
$$

Then:

$$
Y\sim\operatorname{Po}(6).
$$

We need:

$$
P(Y=5).
$$

Use:

$$
P(Y=5)=\frac{e^{-6}6^5}{5!}.
$$

Now:

$$
6^5=7776,
$$

and:

$$
5!=120.
$$

So:

$$
P(Y=5)=\frac{7776e^{-6}}{120}.
$$

Using a calculator:

$$
P(Y=5)=0.1606231410\ldots
$$

Therefore:

$$
P(Y=5)=0.1606
$$

to four decimal places.

### Final exam-style answers

$$
\boxed{P(X=2)=0.1465}
$$

$$
\boxed{P(X>6)=0.1107}
$$

$$
\boxed{P(Y=5)=0.1606}
$$

### Teaching note

The most important move is redefining the random variable when the interval changes. $X$ counts failures in one hour; $Y$ counts failures in $90$ minutes. Same story, different stopwatch.

---

## Worked Example 4: Radios and minimum stock

### Evidence source

This is based on the slide example where a shop sells radios at a rate of $2.5$ per week and the manager wants the probability of running out during a four-week period to be less than $0.01$.

### On-spec status

Core CCEA FAS2-DIST: rate scaling, cumulative probability and reverse cumulative reasoning.

### Question

A shop sells radios at a rate of $2.5$ per week.

1. Find the probability that in a two-week period the shop sells at least $7$ radios.
2. Deliveries of these radios come every $4$ weeks. Find the probability of selling fewer than $12$ radios in a four-week period.
3. The manager wishes to make sure that the probability of the shop running out of radios during a four-week period is less than $0.01$. Find the smallest number of radios the manager should have in stock immediately after the delivery.

### Solution

#### Part 1: At least 7 radios in two weeks

Let:

$$
X=\text{the number of radios sold in a two-week period}.
$$

The rate is:

$$
2.5\text{ per week}.
$$

For two weeks:

$$
\lambda=2.5\times2=5.
$$

Therefore:

$$
X\sim\operatorname{Po}(5).
$$

We need:

$$
P(X\geq7).
$$

Use the complement:

$$
P(X\geq7)=1-P(X\leq6).
$$

Using tables or calculator:

$$
P(X\leq6)=0.7621834629\ldots
$$

Therefore:

$$
P(X\geq7)=1-0.7621834629\ldots
$$

So:

$$
P(X\geq7)=0.2378165370\ldots
$$

To four decimal places:

$$
P(X\geq7)=0.2378.
$$

#### Part 2: Fewer than 12 radios in four weeks

Let:

$$
Y=\text{the number of radios sold in a four-week period}.
$$

For four weeks:

$$
\lambda=2.5\times4=10.
$$

Therefore:

$$
Y\sim\operatorname{Po}(10).
$$

We need:

$$
P(Y<12).
$$

Since $Y$ is discrete:

$$
Y<12
$$

means:

$$
Y\leq11.
$$

So:

$$
P(Y<12)=P(Y\leq11).
$$

Using tables or calculator:

$$
P(Y\leq11)=0.6967761463\ldots
$$

Therefore:

$$
P(Y<12)=0.6968
$$

to four decimal places.

#### Part 3: Minimum stock

Let:

$$
s=\text{the number of radios in stock immediately after delivery}.
$$

The shop runs out if:

$$
Y>s.
$$

The manager wants:

$$
P(Y>s)<0.01.
$$

Use:

$$
P(Y>s)=1-P(Y\leq s).
$$

So:

$$
1-P(Y\leq s)<0.01.
$$

Subtract $1$:

$$
-P(Y\leq s)<-0.99.
$$

Multiply by $-1$ and reverse the inequality:

$$
P(Y\leq s)>0.99.
$$

Now test cumulative probabilities for:

$$
Y\sim\operatorname{Po}(10).
$$

From cumulative tables or calculator:

$$
P(Y\leq17)=0.9857\ldots
$$

This is too small:

$$
0.9857<0.99.
$$

Next:

$$
P(Y\leq18)=0.9928\ldots
$$

This is large enough:

$$
0.9928>0.99.
$$

Therefore the smallest possible stock is:

$$
s=18.
$$

### Final exam-style answers

$$
\boxed{0.2378}
$$

$$
\boxed{0.6968}
$$

$$
\boxed{18\text{ radios}}
$$

### Teaching note

“Running out” means demand is greater than stock, not greater than or equal to stock. If $s=18$ and exactly $18$ radios are sold, the shop ends with zero radios, but has not failed to meet demand.

# 12. Common Mistakes and Exam Traps

## 12.1 Using the wrong interval for $\lambda$

Wrong:

$$
X\sim\operatorname{Po}(2.5)
$$

for a four-week period when the rate is $2.5$ per week.

Correct:

$$
\lambda=2.5\times4=10,
$$

so:

$$
X\sim\operatorname{Po}(10).
$$

## 12.2 Treating strict inequalities as inclusive

Wrong:

$$
P(X<5)=P(X\leq5).
$$

Correct:

$$
P(X<5)=P(X\leq4).
$$

Wrong:

$$
P(X>6)=P(X\geq6).
$$

Correct:

$$
P(X>6)=P(X\geq7).
$$

## 12.3 Forgetting that Poisson has no upper limit

For:

$$
P(X\geq1),
$$

do not try to add:

$$
P(X=1)+P(X=2)+P(X=3)+\cdots
$$

Use:

$$
P(X\geq1)=1-P(X=0).
$$

## 12.4 Failing to define the random variable

Weak exam working:

$$
X\sim\operatorname{Po}(5).
$$

Better:

$$
X=\text{the number of cars passing in one hour},
$$

$$
X\sim\operatorname{Po}(5).
$$

## 12.5 Using binomial just because the derivation involved binomial

The derivation helps explain Poisson. It does not mean every Poisson question should be solved using binomial.

If the question gives an average rate and asks about counts in an interval, use Poisson unless instructed otherwise.

## 12.6 Staying in Poisson when the question switches to binomial

If you calculate the probability of “fewer than seven emails in one day” and then ask how many days out of five have this property, the new variable is binomial.

The transcript highlights this kind of mixed-distribution question as a classic source of difficulty.

## 12.7 Claiming Poisson without checking independence

A rate alone does not magically guarantee Poisson.

For example, buses may have a rate per hour, but scheduled buses do not arrive randomly. The slide evidence rejects the bus example because arrivals spike around regular timetable intervals.

## 12.8 Rounding too early

If an answer is used in a later part, keep extra digits internally.

For example, if:

$$
P(X<7)=0.1574470461\ldots,
$$

then use:

$$
0.1574470461\ldots
$$

in the next calculation rather than just:

$$
0.157.
$$

The transcript warns that using the more accurate version is better when the probability is used again, because rounding error compounds.

## 12.9 Calculator mode traps

The lesson evidence mentions calculator modes:

- **Poisson PD** for exact probabilities such as $P(X=3)$;
- **Poisson CD/CF** for cumulative probabilities such as $P(X\leq4)$.

A calculator can validate answers, but the exam method still needs probability statements.

Write:

$$
P(X<5)=P(X\leq4)=0.0996,
$$

not just:

$$
0.0996.
$$

# 13. Practice Questions

These are **AI-generated on-spec practice questions**, not past-paper questions.

## 13.1 Basic fluency questions

### Question 1

Let:

$$
X\sim\operatorname{Po}(2.4).
$$

Find:

1. $P(X=0)$
2. $P(X=3)$
3. $P(X\leq2)$
4. $P(X>4)$

Give answers to four decimal places.

### Question 2

A call centre receives calls at an average rate of $12$ per hour.

Let:

$$
X=\text{the number of calls received in 15 minutes}.
$$

1. Find $\lambda$ for the $15$ minute interval.
2. Write the distribution of $X$.
3. Find $P(X=2)$.
4. Find $P(X\geq4)$.

### Question 3

A machine produces flaws in wire at a rate of $0.8$ flaws per metre.

Let:

$$
X=\text{the number of flaws in a 5 metre length of wire}.
$$

1. Find the distribution of $X$.
2. Find $P(X=4)$.
3. Find $P(X<3)$.

## 13.2 Bridge questions

### Question 4

Explain the difference between:

$$
X\sim B(20,0.25)
$$

and:

$$
Y\sim\operatorname{Po}(5).
$$

Your answer should mention:

- fixed trials;
- average rate;
- possible values;
- why both might appear in a derivation.

### Question 5

A website receives hits at an average rate of $6$ per minute.

1. Give two assumptions needed for a Poisson model.
2. Explain why a scheduled train arrival process is usually not a good Poisson model.

## 13.3 Standard exam-style questions

### Question 6

A helpdesk receives support tickets at a rate of $3.5$ per hour.

1. Find the probability that exactly $5$ tickets arrive in a randomly selected hour.
2. Find the probability that fewer than $4$ tickets arrive in a randomly selected hour.
3. Find the probability that at least $10$ tickets arrive in a randomly selected $2$ hour period.

### Question 7

A shop sells calculators at a rate of $1.8$ per day. The shop is open $6$ days per week.

1. Find the probability that the shop sells fewer than $8$ calculators in a week.
2. The shop receives calculator deliveries weekly. Find the smallest number of calculators the manager should have in stock immediately after delivery so that the probability of running out during the week is less than $0.05$.

### Question 8

A biologist counts insects in square metre plots. The number of insects per square metre is modelled by:

$$
X\sim\operatorname{Po}(4.2).
$$

1. Find $E(X)$.
2. Find $\operatorname{Var}(X)$.
3. Find the standard deviation of $X$.
4. Find $P(3\leq X\leq6)$.

## 13.4 Harder synthesis questions

### Question 9

A server receives error messages at a rate of $0.9$ per hour.

1. Find the probability that at least one error message is received in a two-hour period.
2. A technician monitors the server for five separate two-hour periods. Find the probability that at least one error occurs in at least three of the five periods.

### Question 10

A bakery finds that raisins are distributed randomly in buns at an average rate of $7$ raisins per bun.

1. State a suitable distribution for the number of raisins in a bun.
2. Find the probability that a randomly selected bun contains fewer than $5$ raisins.
3. In a packet of $6$ buns, find the probability that exactly $2$ buns contain fewer than $5$ raisins.

# 14. Worked Solutions

These are **generated practice solutions** for the AI-generated practice questions in Section 13.

## 14.1 Solution to Question 1

Given:

$$
X\sim\operatorname{Po}(2.4).
$$

So:

$$
\lambda=2.4.
$$

The probability function is:

$$
P(X=x)=\frac{e^{-\lambda}\lambda^x}{x!}.
$$

Therefore:

$$
P(X=x)=\frac{e^{-2.4}(2.4)^x}{x!}.
$$

### Part 1: Find \(P(X=0)\)

Substitute:

$$
x=0.
$$

Then:

$$
P(X=0)=\frac{e^{-2.4}(2.4)^0}{0!}.
$$

Now:

$$
(2.4)^0=1
$$

and:

$$
0!=1.
$$

So:

$$
P(X=0)=e^{-2.4}.
$$

Using a calculator:

$$
P(X=0)=0.0907179532\ldots
$$

To four decimal places:

$$
\boxed{P(X=0)=0.0907}
$$

### Part 2: Find \(P(X=3)\)

Substitute:

$$
x=3.
$$

Then:

$$
P(X=3)=\frac{e^{-2.4}(2.4)^3}{3!}.
$$

Calculate the power:

$$
(2.4)^3=2.4\times2.4\times2.4.
$$

First:

$$
2.4\times2.4=5.76.
$$

Then:

$$
5.76\times2.4=13.824.
$$

So:

$$
(2.4)^3=13.824.
$$

Calculate the factorial:

$$
3!=3\times2\times1=6.
$$

Therefore:

$$
P(X=3)=\frac{e^{-2.4}\times13.824}{6}.
$$

Using a calculator:

$$
P(X=3)=0.2090141644\ldots
$$

To four decimal places:

$$
\boxed{P(X=3)=0.2090}
$$

### Part 3: Find \(P(X\leq2)\)

Since this is cumulative:

$$
P(X\leq2)=P(X=0)+P(X=1)+P(X=2).
$$

We already have:

$$
P(X=0)=e^{-2.4}.
$$

Next:

$$
P(X=1)=\frac{e^{-2.4}(2.4)^1}{1!}.
$$

Since:

$$
1!=1,
$$

we get:

$$
P(X=1)=2.4e^{-2.4}.
$$

Next:

$$
P(X=2)=\frac{e^{-2.4}(2.4)^2}{2!}.
$$

Now:

$$
(2.4)^2=5.76
$$

and:

$$
2!=2.
$$

So:

$$
P(X=2)=\frac{5.76e^{-2.4}}{2}=2.88e^{-2.4}.
$$

Therefore:

$$
P(X\leq2)=e^{-2.4}+2.4e^{-2.4}+2.88e^{-2.4}.
$$

Factorise:

$$
P(X\leq2)=e^{-2.4}(1+2.4+2.88).
$$

Add:

$$
1+2.4+2.88=6.28.
$$

So:

$$
P(X\leq2)=6.28e^{-2.4}.
$$

Using a calculator:

$$
P(X\leq2)=0.5697087467\ldots
$$

To four decimal places:

$$
\boxed{P(X\leq2)=0.5697}
$$

### Part 4: Find \(P(X>4)\)

Use the complement:

$$
P(X>4)=1-P(X\leq4).
$$

Using a calculator or cumulative table:

$$
P(X\leq4)=0.9041314097\ldots
$$

Therefore:

$$
P(X>4)=1-0.9041314097\ldots
$$

So:

$$
P(X>4)=0.0958685903\ldots
$$

To four decimal places:

$$
\boxed{P(X>4)=0.0959}
$$

---

## 14.2 Solution to Question 2

A call centre receives calls at an average rate of $12$ per hour.

Let:

$$
X=\text{the number of calls received in 15 minutes}.
$$

### Part 1: Find \(\lambda\) for the 15 minute interval

Since:

$$
15\text{ minutes}=\frac{15}{60}\text{ hours},
$$

we get:

$$
15\text{ minutes}=\frac14\text{ hour}.
$$

The rate is:

$$
12\text{ calls per hour}.
$$

So for $15$ minutes:

$$
\lambda=12\times\frac14.
$$

Therefore:

$$
\lambda=3.
$$

### Part 2: Write the distribution of \(X\)

Since $X$ counts calls in a fixed interval and the average number in that interval is $3$:

$$
\boxed{X\sim\operatorname{Po}(3)}
$$

### Part 3: Find \(P(X=2)\)

Use:

$$
P(X=x)=\frac{e^{-\lambda}\lambda^x}{x!}.
$$

Here:

$$
\lambda=3,\qquad x=2.
$$

So:

$$
P(X=2)=\frac{e^{-3}3^2}{2!}.
$$

Calculate:

$$
3^2=9,
$$

and:

$$
2!=2.
$$

Therefore:

$$
P(X=2)=\frac{9e^{-3}}{2}.
$$

Using a calculator:

$$
P(X=2)=0.2240418077\ldots
$$

To four decimal places:

$$
\boxed{P(X=2)=0.2240}
$$

### Part 4: Find \(P(X\geq4)\)

Use the complement:

$$
P(X\geq4)=1-P(X\leq3).
$$

Using a calculator or cumulative table:

$$
P(X\leq3)=0.6472318888\ldots
$$

Therefore:

$$
P(X\geq4)=1-0.6472318888\ldots
$$

So:

$$
P(X\geq4)=0.3527681112\ldots
$$

To four decimal places:

$$
\boxed{P(X\geq4)=0.3528}
$$

---

## 14.3 Solution to Question 3

A machine produces flaws in wire at a rate of $0.8$ flaws per metre.

Let:

$$
X=\text{the number of flaws in a 5 metre length of wire}.
$$

### Part 1: Find the distribution of \(X\)

The rate is:

$$
0.8\text{ flaws per metre}.
$$

For $5$ metres:

$$
\lambda=0.8\times5.
$$

So:

$$
\lambda=4.
$$

Therefore:

$$
\boxed{X\sim\operatorname{Po}(4)}
$$

### Part 2: Find \(P(X=4)\)

Use:

$$
P(X=x)=\frac{e^{-\lambda}\lambda^x}{x!}.
$$

Here:

$$
\lambda=4,\qquad x=4.
$$

So:

$$
P(X=4)=\frac{e^{-4}4^4}{4!}.
$$

Calculate:

$$
4^4=4\times4\times4\times4=256.
$$

Also:

$$
4!=4\times3\times2\times1=24.
$$

Therefore:

$$
P(X=4)=\frac{256e^{-4}}{24}.
$$

Using a calculator:

$$
P(X=4)=0.1953668148\ldots
$$

To four decimal places:

$$
\boxed{P(X=4)=0.1954}
$$

### Part 3: Find \(P(X<3)\)

Since $X$ is discrete:

$$
X<3
$$

means:

$$
X\leq2.
$$

So:

$$
P(X<3)=P(X\leq2).
$$

Now:

$$
P(X\leq2)=P(X=0)+P(X=1)+P(X=2).
$$

Using a calculator or cumulative table:

$$
P(X\leq2)=0.2381033056\ldots
$$

To four decimal places:

$$
\boxed{P(X<3)=0.2381}
$$

---

## 14.4 Solution to Question 4

The two distributions are:

$$
X\sim B(20,0.25)
$$

and:

$$
Y\sim\operatorname{Po}(5).
$$

### Binomial distribution

The distribution:

$$
X\sim B(20,0.25)
$$

means:

- there are $20$ fixed trials;
- each trial has probability $0.25$ of success;
- $X$ counts the number of successes;
- possible values are:
  $$
  X=0,1,2,\ldots,20.
  $$

### Poisson distribution

The distribution:

$$
Y\sim\operatorname{Po}(5)
$$

means:

- events are counted in a fixed interval;
- the average number of events in that interval is $5$;
- $Y$ counts the number of events;
- possible values are:
  $$
  Y=0,1,2,3,\ldots
  $$

There is no fixed upper limit.

### Why both appear in the derivation

The Poisson distribution can be motivated by splitting an interval into many tiny binomial-style trials.

If an interval is split into $n$ small pieces and the average number of events is $\lambda$, then:

$$
p=\frac{\lambda}{n}.
$$

So a binomial approximation is:

$$
B\left(n,\frac{\lambda}{n}\right).
$$

As:

$$
n\to\infty,
$$

the tiny intervals become so small that the binomial approximation approaches a Poisson distribution:

$$
\operatorname{Po}(\lambda).
$$

### Final answer

The binomial distribution has a fixed number of trials and an upper limit of $20$ successes. The Poisson distribution counts events occurring at an average rate of $5$ per interval and has no fixed upper limit.

---

## 14.5 Solution to Question 5

A website receives hits at an average rate of $6$ per minute.

### Part 1: Give two assumptions needed for a Poisson model

Suitable assumptions include:

1. Hits occur singly in time.
2. Hits occur independently of each other.
3. Hits occur at a constant average rate.

Any two of these are acceptable.

### Part 2: Explain why a scheduled train arrival process is usually not a good Poisson model

A scheduled train process is usually not a good Poisson model because the arrivals are not random across time.

If trains are scheduled every $10$ minutes, the probability of a train arriving is much higher near the scheduled times and much lower just after a train has left.

So the constant-rate/random-arrival assumption is not reasonable.

Also, train arrivals may not be independent. A delay to one train can affect later trains.

Therefore, a Poisson model is usually unsuitable for scheduled train arrivals.

---

## 14.6 Solution to Question 6

A helpdesk receives support tickets at a rate of $3.5$ per hour.

### Part 1: Exactly 5 tickets in one hour

Let:

$$
X=\text{the number of support tickets received in one hour}.
$$

Then:

$$
X\sim\operatorname{Po}(3.5).
$$

We need:

$$
P(X=5).
$$

Use:

$$
P(X=5)=\frac{e^{-3.5}(3.5)^5}{5!}.
$$

Calculate:

$$
5!=120.
$$

Also:

$$
(3.5)^5=525.21875.
$$

So:

$$
P(X=5)=\frac{e^{-3.5}\times525.21875}{120}.
$$

Using a calculator:

$$
P(X=5)=0.1321685998\ldots
$$

To four decimal places:

$$
\boxed{P(X=5)=0.1322}
$$

### Part 2: Fewer than 4 tickets in one hour

We need:

$$
P(X<4).
$$

Since $X$ is discrete:

$$
P(X<4)=P(X\leq3).
$$

Using calculator or tables:

$$
P(X\leq3)=0.5366326679\ldots
$$

To four decimal places:

$$
\boxed{P(X<4)=0.5366}
$$

### Part 3: At least 10 tickets in two hours

Let:

$$
Y=\text{the number of support tickets received in two hours}.
$$

The rate is $3.5$ per hour.

For two hours:

$$
\lambda=3.5\times2=7.
$$

So:

$$
Y\sim\operatorname{Po}(7).
$$

We need:

$$
P(Y\geq10).
$$

Use the complement:

$$
P(Y\geq10)=1-P(Y\leq9).
$$

Using calculator or tables:

$$
P(Y\leq9)=0.8304959372\ldots
$$

Therefore:

$$
P(Y\geq10)=1-0.8304959372\ldots
$$

So:

$$
P(Y\geq10)=0.1695040628\ldots
$$

To four decimal places:

$$
\boxed{P(Y\geq10)=0.1695}
$$

---

## 14.7 Solution to Question 7

A shop sells calculators at a rate of $1.8$ per day. The shop is open $6$ days per week.

### Part 1: Probability of selling fewer than 8 calculators in a week

Let:

$$
X=\text{the number of calculators sold in one week}.
$$

Since the shop is open $6$ days per week and sells at a rate of $1.8$ per day:

$$
\lambda=1.8\times6.
$$

So:

$$
\lambda=10.8.
$$

Therefore:

$$
X\sim\operatorname{Po}(10.8).
$$

We need:

$$
P(X<8).
$$

Since $X$ is discrete:

$$
P(X<8)=P(X\leq7).
$$

Using calculator or tables:

$$
P(X\leq7)=0.1565829072\ldots
$$

To four decimal places:

$$
\boxed{P(X<8)=0.1566}
$$

### Part 2: Smallest stock so probability of running out is less than \(0.05\)

Let:

$$
s=\text{the number of calculators in stock immediately after delivery}.
$$

Running out means:

$$
X>s.
$$

The manager wants:

$$
P(X>s)<0.05.
$$

Use the complement:

$$
P(X>s)=1-P(X\leq s).
$$

So:

$$
1-P(X\leq s)<0.05.
$$

Subtract $1$:

$$
-P(X\leq s)<-0.95.
$$

Multiply by $-1$ and reverse the inequality:

$$
P(X\leq s)>0.95.
$$

Now check cumulative values for:

$$
X\sim\operatorname{Po}(10.8).
$$

Try:

$$
s=15.
$$

Using calculator:

$$
P(X\leq15)=0.9176793093\ldots
$$

This is too small:

$$
0.9177<0.95.
$$

Try:

$$
s=16.
$$

Using calculator:

$$
P(X\leq16)=0.9510818952\ldots
$$

This is large enough:

$$
0.9511>0.95.
$$

Therefore the smallest suitable stock is:

$$
\boxed{16\text{ calculators}}
$$

---

## 14.8 Solution to Question 8

A biologist counts insects in square metre plots. The number of insects per square metre is modelled by:

$$
X\sim\operatorname{Po}(4.2).
$$

So:

$$
\lambda=4.2.
$$

### Part 1: Find \(E(X)\)

For a Poisson distribution:

$$
E(X)=\lambda.
$$

Therefore:

$$
\boxed{E(X)=4.2}
$$

### Part 2: Find \(\operatorname{Var}(X)\)

For a Poisson distribution:

$$
\operatorname{Var}(X)=\lambda.
$$

Therefore:

$$
\boxed{\operatorname{Var}(X)=4.2}
$$

### Part 3: Find the standard deviation

The standard deviation is:

$$
\sigma=\sqrt{\operatorname{Var}(X)}.
$$

Since:

$$
\operatorname{Var}(X)=4.2,
$$

we get:

$$
\sigma=\sqrt{4.2}.
$$

Using a calculator:

$$
\sigma=2.049390153\ldots
$$

To three decimal places:

$$
\boxed{\sigma=2.049}
$$

### Part 4: Find \(P(3\leq X\leq6)\)

We need:

$$
P(3\leq X\leq6).
$$

Using cumulative probabilities:

$$
P(3\leq X\leq6)=P(X\leq6)-P(X\leq2).
$$

Using calculator or tables:

$$
P(X\leq6)=0.8310505768\ldots
$$

and:

$$
P(X\leq2)=0.1738245679\ldots
$$

Therefore:

$$
P(3\leq X\leq6)=0.8310505768\ldots-0.1738245679\ldots
$$

So:

$$
P(3\leq X\leq6)=0.6572260089\ldots
$$

To four decimal places:

$$
\boxed{P(3\leq X\leq6)=0.6572}
$$

---

## 14.9 Solution to Question 9

A server receives error messages at a rate of $0.9$ per hour.

### Part 1: At least one error in a two-hour period

Let:

$$
X=\text{the number of error messages received in a two-hour period}.
$$

The rate is:

$$
0.9\text{ per hour}.
$$

For two hours:

$$
\lambda=0.9\times2=1.8.
$$

So:

$$
X\sim\operatorname{Po}(1.8).
$$

We need:

$$
P(X\geq1).
$$

Use the complement:

$$
P(X\geq1)=1-P(X=0).
$$

Now:

$$
P(X=0)=\frac{e^{-1.8}(1.8)^0}{0!}.
$$

Since:

$$
(1.8)^0=1
$$

and:

$$
0!=1,
$$

we get:

$$
P(X=0)=e^{-1.8}.
$$

So:

$$
P(X\geq1)=1-e^{-1.8}.
$$

Using a calculator:

$$
P(X\geq1)=0.8347011118\ldots
$$

To four decimal places:

$$
\boxed{P(X\geq1)=0.8347}
$$

### Part 2: At least one error in at least three of five periods

Now the random variable changes.

Let:

$$
Y=\text{the number of two-hour periods, out of five, in which at least one error occurs}.
$$

There are:

$$
5
$$

fixed two-hour periods.

For each period, the probability of at least one error is:

$$
p=0.8347011118\ldots
$$

So:

$$
Y\sim B(5,0.8347011118\ldots).
$$

We need:

$$
P(Y\geq3).
$$

Use the binomial formula:

$$
P(Y=r)=\binom{5}{r}p^r(1-p)^{5-r}.
$$

Therefore:

$$
P(Y\geq3)=P(Y=3)+P(Y=4)+P(Y=5).
$$

So:

$$
P(Y\geq3)=\binom{5}{3}p^3(1-p)^2+\binom{5}{4}p^4(1-p)+\binom{5}{5}p^5.
$$

With:

$$
p=0.8347011118\ldots,
$$

we get:

$$
P(Y\geq3)=0.9652925189\ldots
$$

To four decimal places:

$$
\boxed{P(Y\geq3)=0.9653}
$$

### Teaching note

This is a mixed-distribution question.

Poisson is used first to calculate the probability of at least one error in a two-hour period.

Binomial is used next because we are counting successful periods out of a fixed number of periods.

---

## 14.10 Solution to Question 10

A bakery finds that raisins are distributed randomly in buns at an average rate of $7$ raisins per bun.

### Part 1: State a suitable distribution

Let:

$$
X=\text{the number of raisins in a randomly selected bun}.
$$

The average number of raisins per bun is:

$$
7.
$$

So:

$$
\boxed{X\sim\operatorname{Po}(7)}
$$

### Part 2: Probability that a bun contains fewer than 5 raisins

We need:

$$
P(X<5).
$$

Since $X$ is discrete:

$$
P(X<5)=P(X\leq4).
$$

Using calculator or tables:

$$
P(X\leq4)=0.1729916079\ldots
$$

To four decimal places:

$$
\boxed{P(X<5)=0.1730}
$$

### Part 3: In a packet of 6 buns, exactly 2 contain fewer than 5 raisins

Now define a new random variable.

Let:

$$
Y=\text{the number of buns in the packet that contain fewer than 5 raisins}.
$$

There are:

$$
6
$$

buns.

Each bun either has fewer than $5$ raisins or does not.

The probability that a bun has fewer than $5$ raisins is:

$$
p=0.1729916079\ldots
$$

So:

$$
Y\sim B(6,0.1729916079\ldots).
$$

We need:

$$
P(Y=2).
$$

Use the binomial formula:

$$
P(Y=2)=\binom{6}{2}p^2(1-p)^4.
$$

Substitute:

$$
P(Y=2)=\binom{6}{2}(0.1729916079\ldots)^2(1-0.1729916079\ldots)^4.
$$

Now:

$$
\binom{6}{2}=15.
$$

So:

$$
P(Y=2)=15(0.1729916079\ldots)^2(0.8270083921\ldots)^4.
$$

Using a calculator:

$$
P(Y=2)=0.2099814817\ldots
$$

To four decimal places:

$$
\boxed{P(Y=2)=0.2100}
$$

# 15. Exam Technique Notes

## 15.1 Always define the random variable

Write:

$$
X=\text{the number of calls received in 30 minutes}.
$$

Then write:

$$
X\sim\operatorname{Po}(\lambda).
$$

This avoids a fog-machine answer where the examiner has to guess what $X$ means.

## 15.2 Match \(\lambda\) to the interval

If the question gives:

$$
12\text{ per hour},
$$

and asks about:

$$
15\text{ minutes},
$$

then:

$$
\lambda=12\times\frac{15}{60}=3.
$$

Do not use:

$$
\lambda=12
$$

unless the interval is one hour.

## 15.3 Convert inequalities before calculating

| Wording | Probability | Poisson/CDF form |
|---|---|---|
| fewer than 5 | $P(X<5)$ | $P(X\leq4)$ |
| less than 5 | $P(X<5)$ | $P(X\leq4)$ |
| at most 5 | $P(X\leq5)$ | $P(X\leq5)$ |
| more than 5 | $P(X>5)$ | $1-P(X\leq5)$ |
| at least 5 | $P(X\geq5)$ | $1-P(X\leq4)$ |
| between 2 and 5 inclusive | $P(2\leq X\leq5)$ | $P(X\leq5)-P(X\leq1)$ |

## 15.4 Use complements for upper-tail probabilities

Because Poisson has no fixed maximum, expressions such as:

$$
P(X\geq7)
$$

are usually easier as:

$$
P(X\geq7)=1-P(X\leq6).
$$

## 15.5 Be precise with model assumptions

For a Poisson model, be ready to write:

- events occur singly;
- events occur independently;
- events occur at a constant rate.

The slide evidence gives these as the key modelling restrictions, and mark-scheme style language includes “hits occur singly in time”, “hits are independent or occur randomly”, and “hits occur at a constant rate.”

## 15.6 Watch for mixed distributions

If you calculate the probability of one Poisson event first, and then repeat a fixed number of intervals, you may need a binomial distribution.

Pattern:

1. Use Poisson to find:
   $$
   p=P(\text{event in one interval}).
   $$

2. Then use:
   $$
   Y\sim B(n,p)
   $$
   to count how many intervals have that property.

## 15.7 Mean and variance clue

For:

$$
X\sim\operatorname{Po}(\lambda),
$$

we have:

$$
E(X)=\lambda
$$

and:

$$
\operatorname{Var}(X)=\lambda.
$$

So if a question asks whether a Poisson model is reasonable from data, compare:

$$
\bar{x}
$$

with:

$$
s^2.
$$

If they are close, this supports the model.

If they are very different, this raises doubt.

## 15.8 Calculator notes

Use calculator distribution modes as validation and speed tools.

Typical modes:

- Poisson **PD** for exact probabilities:
  $$
  P(X=x)
  $$
- Poisson **CD/CF** for cumulative probabilities:
  $$
  P(X\leq x)
  $$

But still show the probability statement.

Good:

$$
P(X\geq7)=1-P(X\leq6)=0.2378.
$$

Weak:

$$
0.2378.
$$

The second answer is a lonely number wearing no name badge.

# 16. Syllabus Gap Check

## 16.1 LO coverage table

| LO ID | Covered? | Evidence coverage | Lesson sections |
|---|---|---|---|
| `FAS2-DIST-LO002` | Yes | Discrete probability function, outcomes, mean, variance, standard deviation | 7, 8, 11, 14 |
| `FAS2-DIST-LO003` | Yes | Probability calculations, intervals, expectations and variance | 8, 11, 13, 14 |
| `FAS2-DIST-LO007` | Yes | Poisson model, assumptions, probability calculations, rate scaling | 6, 7, 8, 11, 12, 15 |
| `FAS2-DIST-LO008` | Yes | $E(X)=\lambda$, $\operatorname{Var}(X)=\lambda$ | 8.12, 14.8, 15.7 |

## 16.2 Evidence coverage table

| Evidence item | Covered? | Notes |
|---|---|---|
| Binomial versus Poisson comparison | Yes | Sections 5, 8.1, 8.2 |
| Motivation contexts | Partly | Described and assigned to visual asset plan |
| Time-slicing derivation | Yes | Section 8.2 |
| Poisson probability formula | Yes | Section 8.3 |
| Exact probability examples | Yes | Sections 8.4, 11, 14 |
| Cumulative probabilities | Yes | Sections 8.7, 8.8 |
| Model assumptions | Yes | Sections 8.9, 8.10, 12, 15 |
| Rate scaling | Yes | Sections 8.11, 11, 14 |
| Mean and variance | Yes | Section 8.12 |
| Calculator tips | Yes | Sections 12.9, 15.8 |
| Mixed Poisson then binomial | Yes, as warning/synthesis | Sections 8.14, 14.9, 14.10 |
| Adding Poisson distributions | Not core | Logged as optional enrichment |
| Poisson approximation to binomial | Not core | Logged as optional enrichment |
| Proof from binomial limit | Not core | Mentioned only as enrichment/context |

## 16.3 Bridge coverage table

| Bridge topic | Covered? | Lesson location |
|---|---|---|
| Binomial distribution | Yes | Sections 5, 8.1, 8.2, 14.4 |
| Probability complements | Yes | Sections 8.5, 8.7, 14 |
| Strict/inclusive inequalities | Yes | Sections 8.6, 8.7, 12.2, 15.3 |
| Independence | Yes | Sections 8.9, 8.10, 15.5 |
| Mean and variance | Yes | Sections 8.12, 14.8, 15.7 |
| Mixed distribution logic | Yes | Sections 8.14, 14.9, 14.10 |

## 16.4 Off-Spec Content Found but Excluded

| Off-spec or boundary-risk content | Evidence location | Decision |
|---|---|---|
| Full proof of Poisson formula from binomial limit | PDF/transcript derivation appendix | Excluded from core. Mentioned only as optional enrichment. |
| Adding independent Poisson distributions | Slide/PDF evidence | Excluded from core CCEA lesson because not confirmed in supplied FAS2-DIST LO boundary. |
| Poisson approximation to binomial | Slide/PDF evidence | Excluded from core unless later CCEA evidence confirms it. |
| Conditional probability with Poisson | Slide/PDF exercise reference | Excluded from core. Ordinary conditional probability may remain bridge context only. |
| Hypothesis testing using Poisson | Motivation examples in transcript | Future-topic context only, not taught as hypothesis testing here. |

## 16.5 Optional Enrichment Not Required by CCEA

These may be useful later but are not required as core in this lesson:

1. Full derivation:
   $$
   \lim_{n\to\infty}\binom{n}{x}\left(\frac{\lambda}{n}\right)^x\left(1-\frac{\lambda}{n}\right)^{n-x}
   =
   \frac{e^{-\lambda}\lambda^x}{x!}.
   $$

2. Adding independent Poisson variables:
   $$
   X\sim\operatorname{Po}(\lambda_1),\quad Y\sim\operatorname{Po}(\lambda_2)
   $$
   implies, under suitable independence and same-interval conditions:
   $$
   X+Y\sim\operatorname{Po}(\lambda_1+\lambda_2).
   $$

3. Poisson approximation to binomial:
   $$
   B(n,p)\approx\operatorname{Po}(np)
   $$
   when $n$ is large and $p$ is small.

4. Conditional probability questions involving Poisson counts in subintervals.

## 16.6 Weak evidence warnings

| Issue | Warning |
|---|---|
| Screenshot PDF is image-only | Visual details should be checked directly before producing final SVG/TikZ assets. |
| Cross-board/Pearson evidence | Used only where it aligns with CCEA FAS2-DIST. Boundary-risk material has been excluded from core. |
| Teacher transcript contains speech-to-text errors | Errors such as “python distribution” have been interpreted as “Poisson distribution” where mathematically obvious. |
| CCEA past-paper evidence not attached | Generated practice questions must not be labelled as CCEA past-paper questions. |

## 16.7 Missing Evidence Log

| Missing item | Impact |
|---|---|
| Official CCEA formula booklet extract | No major issue, but would strengthen formula presentation. |
| Official CCEA mark schemes for Poisson questions | Exam phrasing and marking detail could be improved if supplied. |
| Original textbook pages | Slide-embedded textbook examples are used only as slide evidence. |
| Full inspection of all 150 screenshot pages | Later asset phases should inspect pages selectively before claiming exact visual details. |

# 17. Recommended Enhancements Not in the Evidence

These are AI-proposed enhancements designed to make the self-study portal stronger. They are not claimed as evidence-backed CCEA content unless separately verified.

## 17.1 Extra diagrams

1. **Rate scaling machine**
   - Shows:
     $$
     \lambda_{\text{new}}=\lambda_{\text{old}}\times\frac{\text{new interval}}{\text{old interval}}.
     $$
   - Useful for preventing “wrong interval” errors.

2. **Discrete inequality converter**
   - Shows:
     $$
     X<5\Longleftrightarrow X\leq4,
     $$
     $$
     X>6\Longleftrightarrow X\geq7.
     $$

3. **Poisson suitability gate**
   - Three gates:
     - singly;
     - independently;
     - constant rate.

4. **Binomial-to-Poisson bridge visual**
   - Compares:
     $$
     B(10,0.5),\quad B(20,0.25),\quad \operatorname{Po}(5).
     $$

## 17.2 Extra widgets

1. **Poisson probability calculator**
   - Shows formula substitution before numerical result.
   - Flags strict inequality conversion.

2. **Rate-scaling trainer**
   - Lets student convert per hour, per minute, per week, per cm and per metre.

3. **Model suitability sorter**
   - Presents contexts such as buses, calls, radioactive emissions, defects and asks whether Poisson is reasonable.

4. **Mean-variance model checker**
   - Student enters sample mean and variance.
   - Widget comments on whether the Poisson model is plausible.

## 17.3 Extra examples

1. Defects per length of material.
2. Emails per day with mixed binomial follow-up.
3. Website hits per minute.
4. Flowers per square metre.
5. Stock/run-out question with reverse cumulative probability.

## 17.4 Bridge visuals

1. Fixed-trial binomial row of boxes.
2. Rate-based Poisson timeline.
3. Complement probability number line.
4. “What is being counted now?” decision tree.

# 18. Supplementary Sources Used

## 18.1 Project Sources used

- `CCEA_GCE_Further_Mathematics_Specification_Map.md`
- `Further_Maths_README_module_map.md`
- `Further_Maths_EVIDENCE_DROP_CHECKLIST.md`
- `Further Maths Portal Build – Knowledge Evidence.txt`
- `Ordinary_A_Level_Maths_Bridge_Spec_Extracts.md`
- `CCEA_GCE_Mathematics_Specification_Map.md`

## 18.2 Lesson-specific evidence used

- `FS1-Chp2-PoissonDistribution.pdf`
- `transcripts.md`
- `Chapter_2_Poisson_Distribution_📊_(Further_Statistics_1)_screenshots.pdf`

## 18.3 Ordinary A-Level Maths bridge sources

Ordinary A-Level Mathematics sources were used only as bridge context for:

- binomial distribution;
- cumulative probability;
- complements;
- independence;
- mean and variance.

They do **not** override the CCEA Further Mathematics specification boundary.

## 18.4 Cross-board source notes

The Dr Frost/Pearson-style FS1 material was used as lesson-specific explanatory evidence only where it matched the CCEA Further Mathematics FAS2-DIST topic boundary.

Boundary-risk items from that material were excluded from core lesson content and logged separately.

## 18.5 Evidence limitations

1. The screenshot PDF was image-only, with no parsed text.
2. Only previewed visual details were used for asset planning.
3. Official CCEA past-paper and mark-scheme examples were not supplied.
4. Some transcript wording contains automated transcription errors, for example “python distribution” where the intended phrase is Poisson distribution.

# 19. Final Student Checklist

## 19.1 Prerequisite confidence checklist

Before moving on, check that you can:

- [ ] Explain what a random variable is.
- [ ] Use factorials such as $4!$ and $0!$.
- [ ] Use complements such as:
  $$
  P(X\geq1)=1-P(X=0).
  $$
- [ ] Interpret strict and inclusive inequalities.
- [ ] Recall what a binomial distribution counts.
- [ ] Explain independence in a probability model.

## 19.2 Further Maths method checklist

You should now be able to:

- [ ] Recognise a Poisson situation from words such as “rate”, “on average”, “per hour” or “per metre”.
- [ ] Define the random variable clearly.
- [ ] Write:
  $$
  X\sim\operatorname{Po}(\lambda).
  $$
- [ ] Match $\lambda$ to the interval in the question.
- [ ] Use:
  $$
  P(X=x)=\frac{e^{-\lambda}\lambda^x}{x!}.
  $$
- [ ] Calculate exact probabilities.
- [ ] Calculate cumulative probabilities.
- [ ] Convert:
  $$
  P(X<5)
  $$
  into:
  $$
  P(X\leq4).
  $$
- [ ] Use:
  $$
  E(X)=\lambda,
  $$
  and:
  $$
  \operatorname{Var}(X)=\lambda.
  $$

## 19.3 Exam technique checklist

In an exam answer, remember to:

- [ ] State the random variable.
- [ ] State the distribution.
- [ ] Show rate scaling.
- [ ] Use complements for upper tails.
- [ ] Avoid rounding too early.
- [ ] Interpret final answers in context.
- [ ] State modelling assumptions when asked.
- [ ] Switch to binomial if the question changes to counting successful intervals.

## 19.4 Bridge checklist

You should understand that:

- [ ] Binomial counts successes out of fixed trials.
- [ ] Poisson counts events in an interval.
- [ ] Poisson can be motivated by very small binomial time slices.
- [ ] $\lambda$ replaces the binomial idea of fixed $n$ and $p$ as the key rate parameter.
- [ ] Probability language from ordinary A-Level Maths still matters.

## 19.5 Diagram and visual understanding checklist

When visual assets are added, you should be able to explain:

- [ ] Why the 10-slot binomial model is only an approximation.
- [ ] Why the 20-slot model improves the approximation.
- [ ] Why infinitely small time slices lead to the Poisson model.
- [ ] How the Poisson bar chart shows integer-only outcomes.
- [ ] How the model suitability flowchart checks the assumptions.
