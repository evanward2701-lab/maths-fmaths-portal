# AS2 Statistical Distributions: Binomial Distribution

## Title and Metadata

| Field | Value |
|---|---|
| Course | CCEA GCE Mathematics |
| Unit code | AS2 |
| Unit name | AS 2 Applied Mathematics |
| Applied section | Statistics |
| Topic code | AS2-DIST |
| Topic name | Statistical distributions |
| Topic slug | statistical_distributions |
| Topic Pascal | StatisticalDistributions |
| Topic ID | AS2StatisticalDistributions |
| Lesson file | AS2_statistical_distributions_lesson.md |
| LO IDs | AS2-DIST-LO001, AS2-DIST-LO002, AS2-DIST-LO003 |
| Main model | Binomial distribution |
| Core notation | `X ~ B(n,p)`, `P(X = r) = C(n,r)p^r(1-p)^(n-r)` |
| Tags | `#AS2`, `#Statistics`, `#StatisticalDistributions`, `#Binomial`, `#UseCalculator`, `#Modelling` |

---

## Evidence Map

| Evidence source | Used for |
|---|---|
| CCEA GCE Mathematics Specification Map | Unit identity, topic code, LO IDs, syllabus boundaries |
| Project README/module map | File naming conventions, topic metadata rules |
| Evidence checklist | Missing evidence and off-spec logging structure |
| `S1-Chp6-StatisticalDistributions.pdf` | Definitions, examples, diagrams, worked examples, cumulative probability methods |
| `Chapter_6_Statistical_Distributions,_Binomial_🎲_(Applied_Year_1,_Statistics)_Transcript.md` | Step-by-step reasoning, explanations, calculator procedures, exam warnings |
| `Chapter_6_Statistical_Distributions,_Binomial_🎲_(Applied_Year_1,_Statistics)_Screenshots.pdf` | Visual support only, since no text could be parsed |

The slide pack's chapter overview divides the material into general probability distributions, binomial distribution, and cumulative binomial probabilities. That structure is preserved here.

---

## Specification Alignment

### AS2-DIST-LO001

demonstrate understanding of and use the binomial distribution as an example of a discrete probability distribution

This lesson covers random variables, probability tables, probability functions, the discrete uniform distribution as a comparator, and the binomial distribution as the main discrete probability model.

### AS2-DIST-LO002

calculate probabilities using the binomial distribution

This lesson covers the binomial probability formula:

\[
P(X=r)=\binom nrp^r(1-p)^{n-r}
\]

and worked calculations such as:

\[
P(X=2),\quad P(X=9),\quad P(X\le 1),\quad P(X\ge 5).
\]

### AS2-DIST-LO003

link binomial probabilities to the binomial expansion and tree diagrams

This lesson covers repeated-trial path counting, binomial coefficients, Pascal's triangle logic, and cumulative probability transformations.

---

## Learning Objectives

By the end of this lesson, you should be able to:

1. Explain what a discrete random variable is.
2. Interpret \(P(X=x)\) and \(p(x)\).
3. Write simple probability distributions as tables and functions.
4. Use \(\sum p(x)=1\) to find unknown constants.
5. Recognise when a binomial model is appropriate.
6. Write a binomial model using \(X\sim B(n,p)\).
7. Calculate exact binomial probabilities using

\[
P(X=r)=\binom nrp^r(1-p)^{n-r}.
\]

8. Calculate cumulative binomial probabilities using tables, calculator functions or complements.
9. Translate words such as less than, at most, at least and greater than into probability notation.
10. Critique the assumptions behind a binomial model.

---

## Prerequisite Recap, A-Level Only

### Probability laws

For mutually exclusive outcomes:

\[
P(A\text{ or }B)=P(A)+P(B).
\]

For independent events happening together:

\[
P(A\text{ and }B)=P(A)P(B).
\]

When outcomes can happen in different ways, add their probabilities. For a fixed sequence of events, multiply along the sequence.

### Binomial coefficients

From binomial expansion work:

\[
\binom nr
\]

counts the number of ways of choosing \(r\) positions from \(n\) positions.

For example:

\[
\binom{15}{5}=3003.
\]

This means there are \(3003\) different orders in which exactly \(5\) successes can appear among \(15\) trials.

### Inequality notation

You must be fluent with:

\[
X<5,\quad X\le 5,\quad X>5,\quad X\ge 5.
\]

For discrete integer-valued distributions:

\[
P(X<5)=P(X\le 4).
\]

That tiny difference between \(<\) and \(\le\) is a classic probability gremlin.

---

## Big Picture Explanation

Statistical distributions are probability machines. Instead of listing every single real-world possibility from scratch, we choose a model that already knows the shape of the problem.

The evidence separates statistics into an experimental side, where we deal with collected data, and a theoretical side, where we use probability and modelling to predict what we expect to see. Statistical distributions sit on the theoretical side: they help us find probabilities under certain modelling conditions, such as the binomial distribution.

The binomial distribution is useful when a situation is made of repeated trials, each trial has only two outcomes, the probability of success stays fixed, and trials do not affect one another. When those assumptions are fair, the binomial distribution lets us avoid enormous tree diagrams and use a compact formula or calculator instead.

---

## Key Definitions and Notation

### Random variable

A random variable \(X\) represents a single experiment or trial. It consists of possible outcomes, each with a probability attached.

Example:

| \(x\) | red | green | blue | orange |
|---|---:|---:|---:|---:|
| \(P(X=x)\) | 0.3 | 0.4 | 0.1 | 0.2 |

Here:

\[
X=\text{the favourite colour of a randomly selected student}.
\]

The lowercase \(x\) is one particular outcome, such as red or blue.

### \(P(X=x)\)

\[
P(X=x)
\]

means:

\[
\text{the probability that the random variable }X\text{ takes the particular value }x.
\]

### \(p(x)\)

A shorthand for \(P(X=x)\) is:

\[
p(x).
\]

### Probability distribution

A probability distribution gives the probability of each possible outcome.

It can be written:

1. as a table;
2. as a function;
3. graphically.

### Probability mass function

For a discrete random variable, \(p(x)\) is called a probability mass function, because it gives the probability mass assigned to each outcome.

### Discrete uniform distribution

A discrete uniform distribution is a discrete distribution where each outcome has the same probability.

For a fair die:

| \(x\) | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---:|---:|---:|---:|---:|---:|
| \(p(x)\) | \(\frac16\) | \(\frac16\) | \(\frac16\) | \(\frac16\) | \(\frac16\) | \(\frac16\) |

### Binomial distribution notation

If \(X\) has a binomial distribution with \(n\) trials and success probability \(p\), write:

\[
X\sim B(n,p).
\]

This means:

\[
X=\text{the number of successes in }n\text{ trials}.
\]

---

## Core Theory

### 8.1 Probability distributions as tables and functions

A probability distribution maps outcomes to probabilities.

#### Table form

Example:

| \(x\) | 1 | 2 | 3 | 4 |
|---|---:|---:|---:|---:|
| \(p(x)\) | 0.1 | 0.2 | 0.3 | 0.4 |

This is usually easiest to read.

#### Function form

The same distribution can be written as:

\[
p(x)=
\begin{cases}
0.1x, & x=1,2,3,4,\\
0, & \text{otherwise}.
\end{cases}
\]

The curly bracket means this is a piecewise function. The rule depends on the input.

For example, if \(x=2\), then:

\[
p(2)=0.1(2)=0.2.
\]

If \(x=5\), then \(5\) is not in the allowed list \(1,2,3,4\), so:

\[
p(5)=0.
\]

### 8.2 The total probability must be 1

For a full probability distribution:

\[
\sum p(x)=1.
\]

This means all possible outcome probabilities must add to 1.

If the listed probabilities already add to 1, then every unlisted outcome has probability 0.

For example, if:

| \(x\) | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|
| \(p(x)\) | 0.1 | 0.3 | 0.2 | 0.4 |

then:

\[
0.1+0.3+0.2+0.4=1.
\]

So:

\[
P(X=6)=0.
\]

### 8.3 Probability of ranges

Using the distribution:

| \(x\) | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|
| \(p(x)\) | 0.1 | 0.3 | 0.2 | 0.4 |

#### Example 1

Find:

\[
P(X>3).
\]

The values greater than 3 are:

\[
4,\ 5.
\]

So:

\[
P(X>3)=P(X=4)+P(X=5).
\]

\[
P(X>3)=0.2+0.4.
\]

\[
P(X>3)=0.6.
\]

#### Example 2

Find:

\[
P(2\le X<4).
\]

The values included are:

\[
2,\ 3.
\]

The value \(4\) is not included because the inequality says \(X<4\), not \(X\le 4\).

\[
P(2\le X<4)=P(X=2)+P(X=3).
\]

\[
P(2\le X<4)=0.1+0.3.
\]

\[
P(2\le X<4)=0.4.
\]

#### Example 3

Find:

\[
P(2X+1\ge 6).
\]

First solve the inequality inside the probability statement:

\[
2X+1\ge 6.
\]

Subtract 1 from both sides:

\[
2X\ge 5.
\]

Divide both sides by 2:

\[
X\ge 2.5.
\]

So:

\[
P(2X+1\ge 6)=P(X\ge 2.5).
\]

From the table, the possible values satisfying \(X\ge 2.5\) are:

\[
3,\ 4,\ 5.
\]

Therefore:

\[
P(X\ge 2.5)=P(X=3)+P(X=4)+P(X=5).
\]

\[
P(X\ge 2.5)=0.3+0.2+0.4.
\]

\[
P(X\ge 2.5)=0.9.
\]

### 8.4 The binomial distribution

A random variable \(X\) can be modelled by a binomial distribution if all four conditions hold:

1. There is a fixed number of trials, \(n\).
2. There are two possible outcomes: success and failure.
3. There is a fixed probability of success, \(p\).
4. The trials are independent of each other.

If:

\[
X\sim B(n,p),
\]

then:

\[
P(X=r)=\binom nrp^r(1-p)^{n-r}.
\]

Where:

| Symbol | Meaning |
|---|---|
| \(n\) | number of trials |
| \(p\) | probability of success on each trial |
| \(r\) | number of successes |
| \(1-p\) | probability of failure |
| \(\binom nr\) | number of different orders in which \(r\) successes can occur |

The factor \(p^r\) accounts for the \(r\) successes, \((1-p)^{n-r}\) accounts for the remaining failures, and \(\binom nr\) counts the different orders that give the same number of successes.

### 8.5 Why binomial coefficients appear

Suppose the probability of winning a game is \(0.25\), and the game is played 3 times.

Find the probability of winning exactly once.

The possible winning exactly once sequences are:

\[
WLL,\quad LWL,\quad LLW.
\]

There are 3 possible orders.

Each order has probability:

\[
0.25(0.75)(0.75).
\]

So:

\[
P(\text{exactly one win})=3(0.25)(0.75)^2.
\]

\[
P(\text{exactly one win})=3(0.25)(0.5625).
\]

\[
P(\text{exactly one win})=0.421875.
\]

As a fraction:

\[
0.421875=\frac{27}{64}.
\]

The powers add to the number of trials:

\[
1+2=3.
\]

The front coefficient counts the possible orders.

### 8.6 Cumulative binomial probabilities

A cumulative probability adds probabilities up to a value.

For example:

\[
P(X\le 6)=P(X=0)+P(X=1)+P(X=2)+\cdots+P(X=6).
\]

This becomes computationally expensive if done by hand, so tables or calculators are used.

#### Key translations

For integer-valued \(X\):

\[
P(X<5)=P(X\le 4).
\]

\[
P(X\ge 7)=1-P(X\le 6).
\]

\[
P(X>7)=1-P(X\le 7).
\]

\[
P(10\le X<20)=P(X\le 19)-P(X\le 9).
\]

\[
P(10\le X\le 20)=P(X\le 20)-P(X\le 9).
\]

\[
P(X=100)=P(X\le 100)-P(X\le 99).
\]

\[
P(20<X<30)=P(X\le 29)-P(X\le 20).
\]

\[
P(X\ge 30)=1-P(X\le 29).
\]

\[
P(X>30)=1-P(X\le 30).
\]

---

## Visual Asset Integration

[VISUAL PLACEHOLDER: AS2StatisticalDistributionsSVG-001 | Source: CCEA spec map + slide pages 5-6 | Insert from svg/AS2StatisticalDistributionsSVG-001.svg | Purpose: Show the mapping from outcomes \(x\) to probabilities \(p(x)\) as both a table and a function.]

[VISUAL PLACEHOLDER: AS2StatisticalDistributionsSVG-002 | Source: slide page 7 + transcript section 1 | Insert from svg/AS2StatisticalDistributionsSVG-002.svg | Purpose: Show the sample space for three coin tosses and group outcomes by number of heads.]

[VISUAL PLACEHOLDER: AS2StatisticalDistributionsSVG-003 | Source: slide page 10 | Insert from svg/AS2StatisticalDistributionsSVG-003.svg | Purpose: Show a fair die as a discrete uniform distribution with equal probability bars.]

[VISUAL PLACEHOLDER: AS2StatisticalDistributionsSVG-004 | Source: slide page 14 + transcript section 4 | Insert from svg/AS2StatisticalDistributionsSVG-004.svg | Purpose: Show the four binomial model conditions as a decision checklist.]

[VISUAL PLACEHOLDER: AS2StatisticalDistributionsSVG-005 | Source: transcript sections 3-4 | Insert from svg/AS2StatisticalDistributionsSVG-005.svg | Purpose: Link repeated-trial paths, binomial coefficients and \(\binom nrp^r(1-p)^{n-r}\).]

[INTERACTIVE PLACEHOLDER: AS2StatisticalDistributionsWidget-001 | Source: slide pages 18-22 + transcript sections 5-8 | Insert from widgets/AS2StatisticalDistributionsWidget-001.html | Purpose: Let students change \(n,p,r\) and compare \(P(X=r)\), \(P(X\le r)\), and complement probabilities.]

---

## Worked Examples

### Worked Example 1: Three coins as a probability distribution

The random variable \(X\) represents the number of heads when three coins are tossed.

#### Step 1: List the sample space

\[
\{HHH,\ HHT,\ HTT,\ HTH,\ THH,\ THT,\ TTH,\ TTT\}.
\]

There are:

\[
8
\]

equally likely outcomes.

#### Step 2: Count the number of heads

| Outcome | Number of heads |
|---|---:|
| HHH | 3 |
| HHT | 2 |
| HTH | 2 |
| THH | 2 |
| HTT | 1 |
| THT | 1 |
| TTH | 1 |
| TTT | 0 |

#### Step 3: Create the probability table

| \(x\) | 0 | 1 | 2 | 3 |
|---|---:|---:|---:|---:|
| \(P(X=x)\) | \(\frac18\) | \(\frac38\) | \(\frac38\) | \(\frac18\) |

#### Step 4: Write the distribution as a function

\[
P(X=x)=
\begin{cases}
\frac18, & x=0,3,\\[4pt]
\frac38, & x=1,2,\\[4pt]
0, & \text{otherwise}.
\end{cases}
\]

### Worked Example 2: Finding an unknown constant in a probability function

A discrete random variable \(X\) has probability function:

\[
P(X=x)=
\begin{cases}
k(1-x)^2, & x=-1,0,1,2,\\
0, & \text{otherwise}.
\end{cases}
\]

Show that:

\[
k=\frac16.
\]

For \(x=-1\):

\[
P(X=-1)=k(1-(-1))^2=k(2)^2=4k.
\]

For \(x=0\):

\[
P(X=0)=k(1-0)^2=k(1)^2=k.
\]

For \(x=1\):

\[
P(X=1)=k(1-1)^2=k(0)^2=0.
\]

For \(x=2\):

\[
P(X=2)=k(1-2)^2=k(-1)^2=k.
\]

Add the probabilities:

\[
4k+k+0+k=1.
\]

\[
6k=1.
\]

\[
k=\frac16.
\]

### Worked Example 3: The left-handed people example

The probability a randomly chosen person is left-handed is \(0.1\). There is a group of 3 people.

Let:

\[
X=\text{the number of left-handed people in the group}.
\]

Here success means left-handed.

#### a) Probability all 3 are left-handed

\[
P(X=3)=0.1^3=0.001.
\]

#### b) Probability 0 are left-handed

If a person is not left-handed, the probability is:

\[
1-0.1=0.9.
\]

So:

\[
P(X=0)=0.9^3=0.729.
\]

#### c) Probability exactly 1 person is left-handed

List the possibilities:

\[
LRR,\quad RLR,\quad RRL.
\]

For one fixed order, such as \(LRR\):

\[
0.1\times 0.9\times 0.9=0.081.
\]

There are 3 such orders, so:

\[
P(X=1)=3(0.081)=0.243.
\]

#### d) Probability exactly 2 people are left-handed

List the possibilities:

\[
LLR,\quad RLL,\quad LRL.
\]

For one fixed order, such as \(LLR\):

\[
0.1\times 0.1\times 0.9=0.009.
\]

There are 3 such orders, so:

\[
P(X=2)=3(0.009)=0.027.
\]

#### Generalisation

For \(x\) left-handed people out of 3:

\[
P(X=x)=\binom 3x(0.1)^x(0.9)^{3-x}.
\]

### Worked Example 4: Modelling left-handed people with a binomial distribution

At a table of 8 people, 6 people are left-handed. Suppose the probability of being left-handed is \(0.1\).

Let:

\[
X=\text{the number of left-handed people in the group of 8}.
\]

Assuming a binomial model:

\[
X\sim B(8,0.1).
\]

Find:

\[
P(X=6).
\]

Using the binomial formula:

\[
P(X=6)=\binom86(0.1)^6(1-0.1)^{8-6}.
\]

\[
P(X=6)=\binom86(0.1)^6(0.9)^2.
\]

\[
\binom86=28.
\]

So:

\[
P(X=6)=28(0.1)^6(0.9)^2.
\]

\[
P(X=6)=0.00002268.
\]

#### Model critique

This binomial model assumes each person being left-handed is independent of each other. That may not be appropriate if the people are from the same family, because left-handedness may have a genetic link.

### Worked Example 5: Binomial probabilities with \(X\sim B(12,\frac16)\)

Let:

\[
X\sim B\left(12,\frac16\right).
\]

So:

\[
n=12,\qquad p=\frac16,\qquad 1-p=\frac56.
\]

#### a) Find \(P(X=2)\)

\[
P(X=2)=\binom{12}{2}\left(\frac16\right)^2\left(\frac56\right)^{12-2}.
\]

\[
P(X=2)=\binom{12}{2}\left(\frac16\right)^2\left(\frac56\right)^{10}.
\]

\[
\binom{12}{2}=66.
\]

\[
P(X=2)=66\left(\frac16\right)^2\left(\frac56\right)^{10}.
\]

\[
P(X=2)=0.296\quad\text{to 3 significant figures}.
\]

#### b) Find \(P(X=9)\)

\[
P(X=9)=\binom{12}{9}\left(\frac16\right)^9\left(\frac56\right)^{12-9}.
\]

\[
P(X=9)=\binom{12}{9}\left(\frac16\right)^9\left(\frac56\right)^3.
\]

\[
\binom{12}{9}=220.
\]

\[
P(X=9)=220\left(\frac16\right)^9\left(\frac56\right)^3.
\]

\[
P(X=9)=0.0000126.
\]

#### c) Find \(P(X\le 1)\)

\[
P(X\le 1)=P(X=0)+P(X=1).
\]

Now:

\[
P(X=0)=\binom{12}{0}\left(\frac16\right)^0\left(\frac56\right)^{12}
=\left(\frac56\right)^{12}.
\]

Also:

\[
P(X=1)=\binom{12}{1}\left(\frac16\right)^1\left(\frac56\right)^{11}
=12\left(\frac16\right)\left(\frac56\right)^{11}.
\]

Therefore:

\[
P(X\le 1)=\left(\frac56\right)^{12}+12\left(\frac16\right)\left(\frac56\right)^{11}.
\]

\[
P(X\le 1)=0.381.
\]

### Worked Example 6: Suitability of a binomial model

A company claims that a quarter of the bolts sent to them are faulty. To test this claim, the number of faulty bolts in a random sample of 50 is recorded.

Give reasons why a binomial distribution may be a suitable model.

A binomial model may be suitable because:

1. There is a fixed number of trials:

\[
n=50.
\]

2. There are two outcomes for each bolt:

\[
\text{faulty or not faulty}.
\]

3. The probability of success is fixed:

\[
p=\frac14.
\]

4. It is reasonable to assume independence if the bolts are randomly sampled and one bolt being faulty does not affect another being faulty.

### Worked Example 7: \(X\sim B(6,0.2)\)

Let:

\[
X\sim B(6,0.2).
\]

So:

\[
n=6,\qquad p=0.2,\qquad 1-p=0.8.
\]

#### a) Find \(P(X=2)\)

\[
P(X=2)=\binom62(0.2)^2(0.8)^{6-2}.
\]

\[
P(X=2)=\binom62(0.2)^2(0.8)^4.
\]

\[
\binom62=15.
\]

\[
P(X=2)=15(0.2)^2(0.8)^4.
\]

\[
P(X=2)=0.24576.
\]

#### b) Find \(P(X\ge 5)\)

\[
P(X\ge 5)=P(X=5)+P(X=6).
\]

Now:

\[
P(X=5)=\binom65(0.2)^5(0.8)^{1}.
\]

and:

\[
P(X=6)=\binom66(0.2)^6(0.8)^0.
\]

Since:

\[
\binom66=1,\qquad (0.8)^0=1,
\]

we get:

\[
P(X=6)=0.2^6.
\]

Therefore:

\[
P(X\ge 5)=\binom65(0.2)^5(0.8)^1+0.2^6.
\]

\[
P(X\ge 5)=6(0.2)^5(0.8)+0.2^6.
\]

\[
P(X\ge 5)=0.0016.
\]

### Worked Example 8: Bag of red and white balls

A bag contains 2 red balls and 8 white balls. \(X\) represents the number of red balls chosen after 5 selections with replacement.

#### a) How is \(X\) distributed?

There are:

\[
2+8=10
\]

balls in total.

The probability of choosing a red ball is:

\[
p=\frac{2}{10}=0.2.
\]

There are 5 selections, and because the selections are with replacement, the probability stays fixed and the trials are independent.

So:

\[
X\sim B(5,0.2).
\]

#### b) Determine the probability of choosing exactly 3 red balls

\[
P(X=3)=\binom53(0.2)^3(0.8)^{5-3}.
\]

\[
P(X=3)=\binom53(0.2)^3(0.8)^2.
\]

\[
\binom53=10.
\]

\[
P(X=3)=10(0.2)^3(0.8)^2.
\]

\[
P(X=3)=0.0512.
\]

### Worked Example 9: Cumulative probability using \(X\sim B(10,0.3)\)

Let:

\[
X\sim B(10,0.3).
\]

Find:

\[
P(X\le 6).
\]

Using the cumulative distribution function:

\[
P(X\le 6)=0.9894.
\]

Three ways to find this are:

1. calculator binomial cumulative distribution;
2. binomial tables;
3. adding individual probabilities, although this is slower.

### Worked Example 10: Cumulative transformations for \(X\sim B(20,0.4)\)

Let:

\[
X\sim B(20,0.4).
\]

#### a) Find \(P(X\le 7)\)

This is already in cumulative form:

\[
P(X\le 7)=0.4159.
\]

#### b) Find \(P(X<6)\)

Because \(X\) is discrete and integer-valued:

\[
X<6
\]

means:

\[
X\le 5.
\]

So:

\[
P(X<6)=P(X\le 5).
\]

Using the table/calculator value:

\[
P(X<6)=0.1256.
\]

#### c) Find \(P(X\ge 15)\)

At least 15 means:

\[
X\ge 15.
\]

The opposite of \(X\ge 15\) is:

\[
X\le 14.
\]

So:

\[
P(X\ge 15)=1-P(X\le 14).
\]

Using the evidence value:

\[
P(X\ge 15)=0.0016.
\]

### Worked Example 11: More challenging cumulative binomial example

An awkward boy asks 20 girls out on a date. The probability each girl says yes is \(0.3\).

Let:

\[
X=\text{number of girls who say yes}.
\]

Then:

\[
X\sim B(20,0.3).
\]

#### a) Probability fewer than 6 say yes

Fewer than 6 means:

\[
X<6.
\]

Because \(X\) is integer-valued:

\[
P(X<6)=P(X\le 5).
\]

Using the cumulative probability:

\[
P(X\le 5)=0.4164.
\]

So:

\[
P(X<6)=0.4164.
\]

#### b) Probability at least 9 say yes

At least 9 means:

\[
X\ge 9.
\]

The opposite is:

\[
X\le 8.
\]

So:

\[
P(X\ge 9)=1-P(X\le 8).
\]

Using the cumulative value:

\[
P(X\le 8)=0.8867.
\]

Therefore:

\[
P(X\ge 9)=1-0.8867.
\]

\[
P(X\ge 9)=0.1133.
\]

#### c) Repeating the process across 5 evenings

The evening is considered a success if at least 9 girls say yes.

From part b:

\[
P(\text{successful evening})=0.1133.
\]

Let:

\[
Y=\text{number of successful evenings out of 5}.
\]

Then:

\[
Y\sim B(5,0.1133).
\]

Find the probability of at least 4 successful evenings:

\[
P(Y\ge 4)=P(Y=4)+P(Y=5).
\]

Now:

\[
P(Y=4)=\binom54(0.1133)^4(1-0.1133)^{5-4}.
\]

\[
P(Y=4)=\binom54(0.1133)^4(0.8867)^1.
\]

Also:

\[
P(Y=5)=\binom55(0.1133)^5(0.8867)^0.
\]

\[
P(Y=5)=0.1133^5.
\]

Therefore:

\[
P(Y\ge 4)=\binom54(0.1133)^4(0.8867)+0.1133^5.
\]

\[
P(Y\ge 4)=5(0.1133)^4(0.8867)+0.1133^5.
\]

\[
P(Y\ge 4)=0.000749.
\]

### Worked Example 12: Finding a threshold using cumulative probabilities

A spinner lands on red with probability \(0.3\). Jane has 12 spins.

Let:

\[
X=\text{number of reds in 12 spins}.
\]

Then:

\[
X\sim B(12,0.3).
\]

#### a) Find the probability that Jane obtains at least 5 reds

At least 5 means:

\[
X\ge 5.
\]

The opposite is:

\[
X\le 4.
\]

So:

\[
P(X\ge 5)=1-P(X\le 4).
\]

Using the cumulative probability:

\[
P(X\ge 5)=0.2763.
\]

#### b) Find how many reds are needed to make the prize probability less than \(0.05\)

Let \(r\) be the number of reds needed to win.

We want:

\[
P(X\ge r)<0.05.
\]

Use the complement:

\[
P(X\ge r)=1-P(X\le r-1).
\]

So:

\[
1-P(X\le r-1)<0.05.
\]

Subtract 1 from both sides:

\[
-P(X\le r-1)<-0.95.
\]

Multiply by \(-1\), reversing the inequality:

\[
P(X\le r-1)>0.95.
\]

Using the table backwards, identify:

\[
r-1=6.
\]

So:

\[
r=7.
\]

Therefore Jane needs:

\[
\boxed{7\text{ reds}}
\]

to win the prize.

### Worked Example 13: Camford University threshold problem

At Camford University, students have 20 exams. All students pass each individual exam with probability \(0.45\). Students continue into the next year if they pass some minimum number of exams.

Let:

\[
X=\text{number of exams passed}.
\]

Then:

\[
X\sim B(20,0.45).
\]

Let \(k\) be the minimum number of exams needed to continue.

The condition is:

\[
P(X\ge k)\ge 0.9.
\]

Use the complement:

\[
P(X\ge k)=1-P(X\le k-1).
\]

So:

\[
1-P(X\le k-1)\ge 0.9.
\]

Rearrange:

\[
-P(X\le k-1)\ge -0.1.
\]

Multiply by \(-1\), reversing the inequality:

\[
P(X\le k-1)\le 0.1.
\]

From the cumulative binomial table/calculator, identify:

\[
k-1=5.
\]

So:

\[
k=6.
\]

Therefore the minimum number is:

\[
\boxed{6}.
\]

---

## Guided Practice

### Practice 1: Probability function to table

A random variable has probability function:

\[
p(x)=
\begin{cases}
0.1x, & x=1,2,3,4,\\
0, & \text{otherwise}.
\end{cases}
\]

Complete the probability table.

| \(x\) | 1 | 2 | 3 | 4 |
|---|---:|---:|---:|---:|
| \(p(x)\) |  |  |  |  |

Then verify that:

\[
\sum p(x)=1.
\]

### Practice 2: Binomial model decision

A machine produces items. Each item is either faulty or not faulty. A random sample of 40 items is inspected. The probability an item is faulty is claimed to be \(0.08\).

State a suitable binomial model and list the assumptions needed.

### Practice 3: Exact binomial probability

Let:

\[
X\sim B(8,0.25).
\]

Find:

\[
P(X=3).
\]

### Practice 4: Cumulative probability transformation

Let:

\[
X\sim B(30,0.2).
\]

Rewrite each expression using only probabilities of the form \(P(X\le a)\):

a)

\[
P(X<9)
\]

b)

\[
P(X\ge 12)
\]

c)

\[
P(5<X\le 14)
\]

d)

\[
P(X=10)
\]

### Practice 5: Threshold problem

Let:

\[
X\sim B(15,0.4).
\]

A prize is awarded if \(X\ge r\). The organiser wants the probability of winning to be less than \(0.1\).

Write the inequality in terms of \(P(X\le r-1)\).

---

## Common Mistakes and Exam Traps

### Trap 1: Forgetting the binomial coefficient

Wrong:

\[
P(X=3)=p^3(1-p)^{n-3}.
\]

Correct:

\[
P(X=3)=\binom n3p^3(1-p)^{n-3}.
\]

The coefficient counts the different orders in which those successes can happen.

### Trap 2: Powers not adding to \(n\)

For:

\[
P(X=r)=\binom nrp^r(1-p)^{n-r},
\]

the powers must add to:

\[
r+(n-r)=n.
\]

### Trap 3: Using binomial when there are more than two outcomes

A binomial trial must have exactly two outcomes: success or failure.

A game with win/draw/loss is not automatically binomial unless you redefine success and failure, such as:

\[
\text{success}=\text{win},\qquad \text{failure}=\text{not win}.
\]

### Trap 4: Ignoring independence

If trials affect one another, binomial may not be appropriate.

### Trap 5: Confusing \(<\) and \(\le\)

For integer \(X\):

\[
P(X<6)=P(X\le 5).
\]

Not:

\[
P(X<6)=P(X\le 6).
\]

### Trap 6: Wrong complement for at least

At least 15 means:

\[
X\ge 15.
\]

Its opposite is:

\[
X\le 14.
\]

So:

\[
P(X\ge 15)=1-P(X\le 14).
\]

Not:

\[
1-P(X\le 15).
\]

### Trap 7: Treating cross-board examples as CCEA exam promises

The supplied slides include Edexcel/Pearson-style examples. They are mathematically useful and on-spec where they match the CCEA topic, but they are not official CCEA question evidence.

---

## Exam Technique Notes

### When to use the formula

Use:

\[
P(X=r)=\binom nrp^r(1-p)^{n-r}
\]

when you need an exact probability such as:

\[
P(X=2).
\]

### When to use cumulative mode

Use cumulative binomial mode or tables when you need:

\[
P(X\le r).
\]

Use complements for upper-tail probabilities:

\[
P(X\ge r)=1-P(X\le r-1).
\]

\[
P(X>r)=1-P(X\le r).
\]

### Calculator note: Binomial PD

For a non-cumulative exact probability, use binomial probability distribution mode.

A ClassWiz-style route is: Menu, Distribution, Binomial PD, choose Variable, then enter \(n\), \(p\), and \(x\).

### Calculator note: Binomial CD

For cumulative probabilities, use binomial cumulative distribution mode.

For example, to find:

\[
P(X\le 6)
\]

for:

\[
X\sim B(10,0.3),
\]

enter:

\[
x=6,\quad n=10,\quad p=0.3,
\]

and obtain:

\[
0.9894.
\]

### Writing model assumptions

For a suitable binomial model question, write at least two of:

- fixed number of trials;
- two outcomes;
- constant probability;
- independent trials.

In a context, use the context words. For example:

Each bolt is either faulty or not faulty

is better than only writing:

two outcomes.

---

## Full Worked Solutions to Guided Practice

### Solution 1: Probability function to table

Given:

\[
p(x)=
\begin{cases}
0.1x, & x=1,2,3,4,\\
0, & \text{otherwise}.
\end{cases}
\]

For \(x=1\):

\[
p(1)=0.1(1)=0.1.
\]

For \(x=2\):

\[
p(2)=0.1(2)=0.2.
\]

For \(x=3\):

\[
p(3)=0.1(3)=0.3.
\]

For \(x=4\):

\[
p(4)=0.1(4)=0.4.
\]

So:

| \(x\) | 1 | 2 | 3 | 4 |
|---|---:|---:|---:|---:|
| \(p(x)\) | 0.1 | 0.2 | 0.3 | 0.4 |

Now check:

\[
\sum p(x)=0.1+0.2+0.3+0.4.
\]

\[
\sum p(x)=1.
\]

So this is a valid probability distribution.

### Solution 2: Binomial model decision

There are 40 items, so:

\[
n=40.
\]

Faulty can be treated as success, so:

\[
p=0.08.
\]

Let:

\[
X=\text{number of faulty items in the sample}.
\]

Then:

\[
X\sim B(40,0.08).
\]

The assumptions are:

1. The number of trials is fixed:

\[
n=40.
\]

2. Each item has two outcomes:

\[
\text{faulty or not faulty}.
\]

3. The probability of being faulty is constant:

\[
p=0.08.
\]

4. The trials are independent, so one item being faulty does not affect whether another item is faulty.

### Solution 3: Exact binomial probability

Given:

\[
X\sim B(8,0.25).
\]

So:

\[
n=8,\qquad p=0.25,\qquad 1-p=0.75.
\]

Find:

\[
P(X=3).
\]

Use:

\[
P(X=r)=\binom nrp^r(1-p)^{n-r}.
\]

Here:

\[
r=3.
\]

So:

\[
P(X=3)=\binom83(0.25)^3(0.75)^{8-3}.
\]

\[
P(X=3)=\binom83(0.25)^3(0.75)^5.
\]

\[
\binom83=56.
\]

\[
P(X=3)=56(0.25)^3(0.75)^5.
\]

\[
P(X=3)=0.2076416015625.
\]

To 4 decimal places:

\[
P(X=3)=0.2076.
\]

### Solution 4: Cumulative probability transformations

Let:

\[
X\sim B(30,0.2).
\]

#### a)

\[
P(X<9)
\]

Since \(X\) is integer-valued:

\[
X<9\quad\text{means}\quad X\le 8.
\]

So:

\[
P(X<9)=P(X\le 8).
\]

#### b)

\[
P(X\ge 12)
\]

The opposite of \(X\ge 12\) is:

\[
X\le 11.
\]

So:

\[
P(X\ge 12)=1-P(X\le 11).
\]

#### c)

\[
P(5<X\le 14)
\]

The included values are:

\[
6,7,8,\ldots,14.
\]

Start with:

\[
P(X\le 14),
\]

then remove:

\[
P(X\le 5).
\]

So:

\[
P(5<X\le 14)=P(X\le 14)-P(X\le 5).
\]

#### d)

\[
P(X=10)
\]

Use cumulative probabilities:

\[
P(X=10)=P(X\le 10)-P(X\le 9).
\]

### Solution 5: Threshold problem

Given:

\[
X\sim B(15,0.4).
\]

A prize is awarded if:

\[
X\ge r.
\]

The organiser wants:

\[
P(X\ge r)<0.1.
\]

Use the complement:

\[
P(X\ge r)=1-P(X\le r-1).
\]

So:

\[
1-P(X\le r-1)<0.1.
\]

Subtract 1 from both sides:

\[
-P(X\le r-1)<-0.9.
\]

Multiply both sides by \(-1\), reversing the inequality:

\[
P(X\le r-1)>0.9.
\]

So the table/calculator search should look for the first suitable value satisfying:

\[
P(X\le r-1)>0.9.
\]

Then:

\[
r=(r-1)+1.
\]

---

## Common CCEA-Style Wording

- Show that a binomial distribution may be a suitable model.
- State the distribution of \(X\).
- Find \(P(X=r)\).
- Find \(P(X\le r)\).
- Find the probability of at least \(r\) successes.
- Find the smallest value of \(r\) such that a probability condition is satisfied.
- Interpret your probability in context.

---

## Syllabus Gap Check

| LO ID | Covered? | Evidence-backed coverage |
|---|---|---|
| AS2-DIST-LO001 | Yes | Random variables, discrete distributions, probability tables/functions, discrete uniform contrast, binomial model |
| AS2-DIST-LO002 | Yes | Formula calculations, exact binomial examples, calculator PD |
| AS2-DIST-LO003 | Yes | Repeated trial paths, binomial coefficients, cumulative probabilities, calculator/table use |

### Excluded from core

| Content | Reason |
|---|---|
| Continuous probability density functions | Mentioned in evidence, but not AS2-DIST core |
| Normal distribution | CCEA A22 topic, not AS2 binomial |
| Expected value and variance of random variables | Not in supplied AS2-DIST LO list |
| Cross-board-only exam style details | Not treated as CCEA-specific |

---

## Visual and Interactive Asset Plan

| Asset ID | Type | Source | Purpose | Phase |
|---|---|---|---|---|
| AS2StatisticalDistributionsMermaid-001 | Mermaid | Lesson structure | Overall topic flow | Phase 2 |
| AS2StatisticalDistributionsMermaid-002 | Mermaid | Transcript binomial conditions | Suitability checklist | Phase 2 |
| AS2StatisticalDistributionsMermaid-003 | Mermaid | Transcript repeated trials | Tree paths to binomial formula | Phase 2 |
| AS2StatisticalDistributionsMermaid-004 | Mermaid | Cumulative probability evidence | Cumulative translation map | Phase 2 |
| AS2StatisticalDistributionsMermaid-005 | Mermaid | Calculator guidance | PD versus CD decision route | Phase 2 |
| AS2StatisticalDistributionsSVG-001 | SVG | Slides 5-6 | Table/function mapping | Phase 3 |
| AS2StatisticalDistributionsSVG-002 | SVG | Slide 7 | Coin-toss sample space | Phase 3 |
| AS2StatisticalDistributionsSVG-003 | SVG | Slide 10 | Discrete uniform die distribution | Phase 3 |
| AS2StatisticalDistributionsSVG-004 | SVG | Slide 14 | Binomial conditions checklist | Phase 3 |
| AS2StatisticalDistributionsSVG-005 | SVG | Transcript sections 3-4 | Path-counting to binomial coefficient | Phase 3 |
| AS2StatisticalDistributionsTikZ-001 | TikZ | Slide 10 | Probability bar chart for fair die | Phase 4 |
| AS2StatisticalDistributionsTikZ-002 | TikZ | Transcript conditions | Binomial model checklist | Phase 4 |
| AS2StatisticalDistributionsTikZ-003 | TikZ | Transcript binomial formula | Tree/path logic to formula | Phase 4 |
| AS2StatisticalDistributionsTikZ-004 | TikZ | Cumulative transformations | Conversion map | Phase 4 |
| AS2StatisticalDistributionsWidget-001 | HTML widget | Slides 18-22 | Binomial PD/CD calculator explorer | Phase 5 |

---

## Supplementary Sources Used

| Source | Status |
|---|---|
| CCEA specification map | Core authority |
| Project README/module map | Metadata and workflow support |
| Evidence checklist | Evidence logging support |
| DrFrostMaths slide PDF | Lesson evidence; cross-board/third-party but on-spec support |
| Teacher transcript | Lesson evidence; explanations and worked methods |
| Screenshots PDF | Visual support only |
| Edexcel/Pearson-labelled examples inside slides | Cross-board support only, not official CCEA evidence |

---

## Final Student Checklist

You are ready for this topic when you can:

- [ ] Explain the difference between \(X\) and \(x\).
- [ ] Interpret \(P(X=x)\) correctly.
- [ ] Write a probability distribution as a table.
- [ ] Use \(\sum p(x)=1\) to find an unknown constant.
- [ ] Recognise a discrete uniform distribution.
- [ ] State the four binomial conditions.
- [ ] Write \(X\sim B(n,p)\) correctly.
- [ ] Identify \(n\), \(p\), \(r\), and \(1-p\) in a binomial question.
- [ ] Use \(P(X=r)=\binom nrp^r(1-p)^{n-r}\).
- [ ] Remember that the powers must add to \(n\).
- [ ] Use complements for \(P(X\ge r)\) and \(P(X>r)\).
- [ ] Convert \(P(X<r)\) into \(P(X\le r-1)\).
- [ ] Use calculator binomial PD for exact probabilities.
- [ ] Use calculator binomial CD or tables for cumulative probabilities.
- [ ] Critique whether a binomial model is appropriate in context.
