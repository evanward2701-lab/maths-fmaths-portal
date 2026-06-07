# FAS2 Geometric Distribution Lesson Pack

# 1. Lesson Title and Metadata

## Geometric Distribution as a Model

| Field | Value |
|---|---|
| Date generated | 2026-06-05 |
| Course | CCEA GCE Further Mathematics |
| Unit code | `FAS2` |
| Unit name | Further AS 2 Applied Mathematics |
| Applied section | Section C: Statistics |
| Topic code | `FAS2-DIST` |
| Topic name | Statistical distributions |
| Lesson topic | Geometric Distribution as a Model |
| Topic slug | `geometric_distribution` |
| Topic Pascal | `GeometricDistribution` |
| Topic ID | `FAS2GeometricDistribution` |
| Lesson file | `FAS2_geometric_distribution_lesson.md` |
| Core LO IDs | `FAS2-DIST-LO001`, `FAS2-DIST-LO002`, `FAS2-DIST-LO003`, `FAS2-DIST-LO008` |
| Supporting LO ID | `FAS2-DIST-LO006` |
| Boundary LO IDs not taught here | `FAS2-DIST-LO004`, `FAS2-DIST-LO005`, `FAS2-DIST-LO007` |
| Bridge tags | `#AS2Probability`, `#AS2BinomialDistribution`, `#A21SequencesAndSeries`, `#DiscreteRandomVariables` |
| Topic tags | `#FAS2`, `#DIST`, `#Statistics`, `#Distributions`, `#Geometric`, `#Expectation`, `#Variance`, `#ModelSelection` |

## Lesson boundary statement

This lesson teaches the **geometric distribution** as required by CCEA Further Mathematics `FAS2-DIST`.

The supplied lesson evidence also includes **negative binomial distribution**, but the supplied CCEA Further Mathematics specification map for `FAS2-DIST` does not list negative binomial as a required learning outcome. Negative binomial is therefore not taught as core content in this lesson. It is logged under off-spec or boundary-risk content.

# 2. Evidence Map

| Source | Type | Lesson use | Status |
|---|---|---|---|
| `CCEA_GCE_Further_Mathematics_Specification_Map.md` | Project Source | Authority for `FAS2-DIST`, LO IDs and syllabus boundary | Used |
| `Further_Maths_README_module_map.md` | Project Source | Metadata conventions and bridge mapping | Used |
| `Further_Maths_EVIDENCE_DROP_CHECKLIST.md` | Project Source | Evidence hierarchy and off-spec logging rules | Used |
| `Ordinary_A_Level_Maths_Bridge_Spec_Extracts.md` | Project Source | Ordinary Maths bridge context only | Used |
| `CCEA_GCE_Mathematics_Specification_Map.md` | Project Source | Ordinary Mathematics bridge evidence | Used as bridge only |
| `FS1-Chp3-GeometricNegativeBinomial.pdf` | Lesson evidence | Geometric definition, formulae, cumulative probabilities, examples, mean and variance | Used where on-spec |
| `transcripts.md` | Teacher transcript | Teacher reasoning, warnings, assumptions and worked-example explanations | Used where on-spec |
| `Chapter_3_Geometric_&_Negative_Binomial_Distributions_📊_(Further_Statistics_1)_screenshots.pdf` | Image-only visual PDF | Supporting visual evidence from visible/readable preview pages | Partially used |

Diagram evidence is partially unclear here. The screenshot PDF is image-only and has 150 pages. The description below preserves the visible/readable details only. No uninspected visual detail is claimed.

# 3. Specification Alignment

| LO ID | Official wording | Lesson coverage | Evidence source | Syllabus boundary | Ordinary A-Level Maths bridge |
|---|---|---|---|---|---|
| `FAS2-DIST-LO001` | demonstrate understanding of and use the geometric distribution as a model, including the calculation of probabilities using the geometric distribution | Defines `X~Geo(p)`, model conditions, probability function, cumulative probabilities and interpretation | CCEA spec map; slide PDF; transcript | Core | AS2 probability and AS2 binomial distribution |
| `FAS2-DIST-LO002` | demonstrate understanding of and use discrete probability distributions, including probability functions, mean, variance and standard deviation | Treats geometric distribution as a discrete distribution over `N={1,2,3,...}`; gives `P(X=x)`, `E(X)`, `Var(X)`, standard deviation | CCEA spec map; slide PDF | Core | AS2 statistical distributions |
| `FAS2-DIST-LO003` | calculate probabilities such as `P(a<=X<=b)`, `E(X)` and `Var(X)` for simple cases of a discrete random variable `X` | Calculates exact, cumulative, upper-tail and range probabilities | CCEA spec map; cumulative geometric slide; transcript | Core | AS2 probability, complement rule |
| `FAS2-DIST-LO006` | understand and use the expressions for `E(aX+b)` and `Var(aX+b)`, where `X` is a discrete or continuous random variable | Mentioned as later/synoptic extension | CCEA spec map | Supporting only | Ordinary random variable transformations |
| `FAS2-DIST-LO008` | use the expressions for the mean and variance of the binomial, geometric and Poisson distributions | Teaches `E(X)=1/p`, `Var(X)=(1-p)/p^2` and standard deviation | CCEA spec map; mean/variance slide; transcript | Core | AS2 binomial mean/variance; A21 series for proof |

# 4. Learning Objectives

## Core Further Maths objectives

By the end of this lesson, the student should be able to:

1. Recognise when a situation can be modelled by a geometric distribution.
2. State the assumptions for a geometric model: independent trials, fixed probability of success, two outcomes, success or failure.
3. Define the random variable `X` clearly as the **number of trials required to obtain the first success**.
4. Use the notation `X ~ Geo(p)`.
5. Use the probability function
   `P(X=x)=p(1-p)^(x-1), x=1,2,3,...`.
6. Use cumulative and tail probabilities:
   `P(X<=x)=1-(1-p)^x`, `P(X>x)=(1-p)^x`, `P(X>=x)=(1-p)^(x-1)`.
7. Use `E(X)=1/p`, `Var(X)=(1-p)/p^2`, and `sigma=sqrt(Var(X))`.
8. Explain why the probabilities form a geometric sequence.
9. Explain why `X` has no upper limit.

## Bridge objectives

The student should be able to connect this topic to ordinary A-Level Maths by explaining how geometric distribution differs from ordinary AS2 binomial distribution, why binomial has fixed trials but geometric does not, how the complement rule supports cumulative formulae, how geometric series explain the name, and why random variable definitions matter before calculation.

## Exam technique objectives

Translate wording such as “on the fifth attempt”, “five or fewer”, “more than five” and “at least seven” into correct probability notation; avoid mixing up `P(X=x)`, `P(X<=x)`, `P(X>x)` and `P(X>=x)`; state assumptions clearly in context; use exact formulae before calculator validation; interpret mean and standard deviation in context.

# 5. Explicit Prerequisite Recap

## GCSE foundations

| GCSE idea | Needed here because |
|---|---|
| Probability as a number between 0 and 1 | `p` is a probability of success. |
| Complementary probabilities | Failure probability is `1-p`. |
| Multiplying probabilities for independent events | `P(fail, fail, success)=(1-p)^2p`. |
| Powers and indices | Repeated failures are written as `(1-p)^k`. |
| Exact fractions and decimals | Probabilities may appear as `1/6`, `0.2`, `0.6`, etc. |

## A-Level Maths Bridge: What You Already Know and What Further Maths Changes

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| AS2 Probability | Independent repeated trials can be multiplied; complements use `1-P(A)`. | A repeated-trial situation becomes a named model when we wait until the first success. | Forgetting independence or fixed probability invalidates the model. |
| AS2 Binomial Distribution | `X~Bin(n,p)` counts successes in a fixed number `n` of trials. | `X~Geo(p)` counts how many trials are needed until the first success. | Do not use binomial just because the context mentions repeated trials. |
| AS2 Statistical Distributions | Discrete random variables have probability functions, mean, variance and standard deviation. | The geometric distribution is a discrete distribution on `1,2,3,...` with no upper limit. | Do not start at `0`. You cannot get a first success in zero trials. |
| A21 Sequences and Series | A geometric sequence has first term `a`, common ratio `r`; an infinite geometric series sums to `a/(1-r)`. | The probabilities `p, p(1-p), p(1-p)^2,...` form a geometric sequence. | The “geometric” in the name is about a probability sequence, not geometry with shapes. |
| A22 Normal Distribution, bridge context only | A probability distribution can model real data or random behaviour. | Further Statistics requires choosing between different distribution models. | Geometric is discrete and integer-valued, not continuous. |

In ordinary A-Level Maths, this idea appeared as binomial modelling: fixed number of trials, fixed probability of success, and the random variable counts how many successes occur.

In Further Maths, the same repeated-trial idea becomes a new model: the number of trials is not fixed. Instead, `X` counts how long we wait until the first success.

The key upgrade is that the support becomes infinite: `x=1,2,3,...`, rather than `x=0,1,2,...,n`.

The danger is treating “until” language as if it were still binomial. The word **until** is a little alarm bell: it often means the number of trials is random.

# 6. Big Picture Explanation

The geometric distribution answers:

> How long do I have to keep trying until the first success happens?

Contexts include rolling a die until the first six, taking a test until passing, clicking a link until the first visitor clicks, playing a game until the first win, or repeating an explanation until the class understands.

In a binomial distribution, the number of trials is fixed first. For example, `X~Bin(10,0.2)` could mean: I play the game 10 times. How many wins do I get?

In a geometric distribution, the number of trials is not fixed. Instead, `X~Geo(0.2)` could mean: I play the game until I win once. How many games do I need?

For applied statistics, the model only makes sense if every trial is independent, success probability is fixed, each trial has only success/failure outcomes, and the process stops after the first success.

A geometric distribution is a model. For example, a driving test example may be mathematically convenient, but the assumptions can be criticised because attempts may not be independent and the probability of passing may change after more lessons or after a confidence-shaking failure.

# 7. Key Definitions and Notation

A **trial** is one repeated attempt. A **success** is the outcome we are waiting for. A **failure** is any outcome that is not the chosen success. If the probability of success is `p`, then the probability of failure is `1-p`.

Let `X` be the number of trials required to obtain the first success. Then `X~Geo(p)` means `X` has a geometric distribution with success probability `p`.

For `X~Geo(p)`, the probability that the first success occurs on trial `x` is

`P(X=x)=p(1-p)^(x-1), x=1,2,3,...`

The possible values are `x=1,2,3,...`. There is no upper limit because, in theory, repeated failures could continue for a very long time before the first success.

The cumulative probability `P(X<=x)` means the first success happens within the first `x` trials:

`P(X<=x)=1-(1-p)^x`.

Upper-tail probabilities are:

`P(X>x)=(1-p)^x`, because the first `x` trials were all failures.

`P(X>=x)=(1-p)^(x-1)`, because the first `x-1` trials were all failures.

For `X~Geo(p)`,

`E(X)=1/p`, `Var(X)=(1-p)/p^2`, and `sigma=sqrt((1-p)/p^2)`.

# 8. Core Theory

## 8.1 When a geometric distribution applies

A geometric distribution applies when we want the number of trials required to achieve **one success**, and trials are independent, the probability of success is fixed, each trial has two outcomes, and the process stops when the first success occurs.

**Bridge Note:** In ordinary A-Level Maths, repeated independent trials often led to binomial distribution. Here, Further Maths extends that idea by making the number of trials random.

## 8.2 Hook-a-duck motivation

The supplied evidence uses a funfair hook-a-duck game with probability of winning a teddy bear `p=0.2`. The probability of not winning is `1-p=0.8`.

If I play the game 10 times and ask for the probability of winning at least one teddy bear, the number of trials is fixed, so this is binomial: `Y~Bin(10,0.2)` and the question is `P(Y>=1)`.

If I play until I win a teddy bear, the number of trials is not fixed. Let `X` be the number of games played until the first teddy bear is won. Then `X~Geo(0.2)`.

If I ask for the third teddy bear on the fifteenth attempt, this is not geometric because geometric stops at the first success. It is negative binomial in the supplied FS1 evidence, but excluded from CCEA core here.

## 8.3 Building the geometric formula from repeated failures

Suppose `X~Geo(p)`. To have `X=1`, the first trial must be a success:

`P(X=1)=p`.

To have `X=2`, the first trial must fail and the second trial must succeed:

`P(X=2)=(1-p)p`.

To have `X=3`, the first two trials must fail and the third must succeed:

`P(X=3)=(1-p)^2p`.

To have `X=4`, the first three trials must fail and the fourth must succeed:

`P(X=4)=(1-p)^3p`.

Therefore, to have `X=x`, the first `x-1` trials must fail and the `x`th trial must succeed:

`P(X=x)=(1-p)^(x-1)p=p(1-p)^(x-1)`.

## 8.4 Why `x` starts at 1, not 0

The smallest possible value of `X` is `1`, meaning the first trial is a success. It is impossible to have `X=0` because you cannot get the first success in zero trials.

## 8.5 Why there is no upper limit

There is no theoretical upper limit for `X`. If `p=0.2`, repeated failures have probability powers of `0.8`; they become small but are still possible in the model.

## 8.6 Why it is called geometric

The probabilities are:

`p, p(1-p), p(1-p)^2, p(1-p)^3, ...`

This is a geometric sequence with first term `a=p` and common ratio `r=1-p`. The infinite sum is

`S_infinity = a/(1-r) = p/[1-(1-p)] = p/p = 1`.

So all probabilities add to 1.

**Bridge Note:** This is where ordinary A21 sequences and series become a statistics proof tool.

## 8.7 Binomial vs geometric distribution

| Feature | Binomial distribution | Geometric distribution |
|---|---|---|
| Notation | `X~Bin(n,p)` | `X~Geo(p)` |
| What is fixed? | Number of trials `n` | Number of successes, exactly one |
| What varies? | Number of successes `X` | Number of trials `X` |
| Question type | “How many successes occur in `n` trials?” | “How many trials are needed until the first success?” |
| Possible values | `0,1,2,...,n` | `1,2,3,...` |
| Upper limit? | Yes, `n` | No |

## 8.8 Cumulative geometric probabilities

Exact probability answers “first success exactly on trial `x`”. Cumulative questions ask “five or fewer”, “less than 8”, “more than 5”, or “at least 7”.

## 8.9 Deriving `P(X<=x)` by geometric series

`P(X<=x)=P(X=1)+P(X=2)+...+P(X=x)`.

So:

`P(X<=x)=p+p(1-p)+p(1-p)^2+...+p(1-p)^(x-1)`.

This finite geometric series has `a=p`, `r=1-p`, `n=x`:

`P(X<=x)=p[1-(1-p)^x]/[1-(1-p)] = p[1-(1-p)^x]/p = 1-(1-p)^x`.

## 8.10 Deriving `P(X<=x)` by complement

The event `X<=x` means the first success appeared within the first `x` trials. The opposite is that the first `x` trials were all failures. Therefore:

`P(X>x)=(1-p)^x`.

So:

`P(X<=x)=1-P(X>x)=1-(1-p)^x`.

## 8.11 Tail probabilities

More than `x` trials means the first `x` trials failed:

`P(X>x)=(1-p)^x`.

At least `x` trials means the first `x-1` trials failed:

`P(X>=x)=(1-p)^(x-1)`.

Example:

`P(X>5)=(1-p)^5`, but `P(X>=5)=(1-p)^4`.

## 8.12 Converting inequality wording

| Wording | Probability notation | Geometric formula |
|---|---|---|
| exactly `x` trials | `P(X=x)` | `p(1-p)^(x-1)` |
| `x` or fewer trials | `P(X<=x)` | `1-(1-p)^x` |
| fewer than `x` trials | `P(X<x)=P(X<=x-1)` | `1-(1-p)^(x-1)` |
| more than `x` trials | `P(X>x)` | `(1-p)^x` |
| at least `x` trials | `P(X>=x)` | `(1-p)^(x-1)` |

## 8.13 Mean, variance and standard deviation

For `X~Geo(p)`,

`E(X)=1/p`.

If `p=1/6`, then `E(X)=6`, so if you roll a fair die until you get a six, you expect to roll about 6 times on average.

For `X~Geo(p)`,

`Var(X)=(1-p)/p^2`, and `sigma=sqrt((1-p)/p^2)`.

## 8.14 Proof that `E(X)=1/p`

Start from:

`E(X)=sum_{x=1}^infinity xP(X=x)`.

For `X~Geo(p)`, `P(X=x)=p(1-p)^(x-1)`, so

`E(X)=p+2p(1-p)+3p(1-p)^2+4p(1-p)^3+...`.

Multiply by `1-p`:

`(1-p)E(X)=p(1-p)+2p(1-p)^2+3p(1-p)^3+4p(1-p)^4+...`.

Subtract:

`E(X)-(1-p)E(X)=p+p(1-p)+p(1-p)^2+p(1-p)^3+...`.

Factor the left side:

`E(X)[1-(1-p)] = pE(X)`.

The right side is an infinite geometric series with first term `p` and ratio `1-p`, so it sums to `p/[1-(1-p)]=1`.

Therefore:

`pE(X)=1`, so `E(X)=1/p`.

## 8.15 Model assumptions and interpretation

When using `X~Geo(p)`, always define `X`, then check independence, fixed probability, two outcomes and stopping after the first success.

Driving test warning: mathematically, a driving-test example with `p=0.6` can be modelled by `X~Geo(0.6)`, but the assumptions are questionable because lessons, confidence and experience may change the probability over attempts.

# 9. Visual Asset Integration

[VISUAL PLACEHOLDER: FAS2GeometricDistributionMermaid-001 | Source: CCEA FAS2-DIST boundary + lesson evidence | Insert from mermaid/FAS2GeometricDistributionMermaid-001.md | Purpose: Help the student choose between binomial, geometric, Poisson boundary-link and excluded negative binomial.]

[VISUAL PLACEHOLDER: FAS2GeometricDistributionSVG-001 | Source: FS1 slide PDF page 3 + transcript explanation | Insert from svg/FAS2GeometricDistributionSVG-001.svg | Purpose: Show why `P(X=x)=p(1-p)^(x-1)`.]

[VISUAL PLACEHOLDER: FAS2GeometricDistributionSVG-002 | Source: FS1 slide PDF page 3 + transcript explanation of geometric sequence | Insert from svg/FAS2GeometricDistributionSVG-002.svg | Purpose: Show why the distribution is called geometric.]

[VISUAL PLACEHOLDER: FAS2GeometricDistributionBridgeSVG-001 | Source: Ordinary A-Level Maths bridge + Further Maths specification + FS1 slide PDF page 4 | Insert from svg/FAS2GeometricDistributionBridgeSVG-001.svg | Purpose: Compare prior ordinary Maths method with Further Maths extension.]

[VISUAL PLACEHOLDER: FAS2GeometricDistributionTikZ-001 | Source: FS1 slide PDF page 5 + transcript cumulative-probability explanation | Insert from tikz/FAS2GeometricDistributionTikZ-001.tex | Purpose: Show why `P(X<=x)=1-(1-p)^x` and `P(X>x)=(1-p)^x`.]

[VISUAL PLACEHOLDER: FAS2GeometricDistributionSVG-003 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from svg/FAS2GeometricDistributionSVG-003.svg | Purpose: Prevent inequality wording errors.]

# 10. Interactive Learning Widgets

[INTERACTIVE PLACEHOLDER: FAS2GeometricDistributionWidget-001 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FAS2GeometricDistributionWidget-001.html | Purpose: Reinforce exact, cumulative and tail probabilities for `X~Geo(p)`.]

Student inputs: success probability `p`, trial number `x`, probability type `P(X=x)`, `P(X<=x)`, `P(X>x)`, or `P(X>=x)`. The widget displays the formula, substitution, final decimal probability and a trial-strip explanation.

[INTERACTIVE PLACEHOLDER: FAS2GeometricDistributionWidget-002 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FAS2GeometricDistributionWidget-002.html | Purpose: Train students to translate exam wording into probability notation.]

The widget checks strict versus inclusive inequalities and whether the endpoint has been shifted correctly.

[INTERACTIVE PLACEHOLDER: FAS2GeometricDistributionWidget-003 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FAS2GeometricDistributionWidget-003.html | Purpose: Distinguish binomial, geometric, Poisson boundary-link and excluded negative binomial contexts.]

The widget classifies scenarios as binomial, geometric, Poisson boundary-link or not core in this lesson.

# 11. Worked Examples

## Worked Example 1: Hook-a-duck model choice

The probability of winning a teddy bear is `0.2`.

(a) If I play the game 10 times, let `Y` be the number of wins. Then `Y~Bin(10,0.2)`. We want `P(Y>=1)=1-P(Y=0)=1-0.8^10=0.8926258176`, so `0.8926` to 4 d.p.

(b) If I play until I win, let `X` be the number of games played until the first win. Then `X~Geo(0.2)`. “At least 7” means the first 6 games failed, so `P(X>=7)=0.8^6=0.262144`.

(c) “Third teddy bear on the fifteenth attempt” is not geometric because geometric stops at the first success. It is negative binomial in the supplied evidence, but excluded from CCEA core here.

## Worked Example 2: Rolling doubles to start a board game

Jack rolls two dice and must roll a double to begin. A success is rolling a double. There are 6 doubles out of 36 outcomes, so `p=6/36=1/6`, and failure probability is `5/6`. Let `X` be the number of attempts needed to roll the first double. Then `X~Geo(1/6)`.

(a) Exactly 4 attempts:

`P(X=4)=(1/6)(5/6)^3=125/1296=0.0965` to 4 d.p.

(b) At least 10 attempts:

`P(X>=10)=(5/6)^9=0.1938` to 4 d.p.

(c) Less than 5 attempts:

`P(X<5)=P(X<=4)=1-(5/6)^4=671/1296=0.5177` to 4 d.p.

## Worked Example 3: Genevieve’s driving test

The probability that Genevieve passes on any one attempt is `0.6`. Let `X` be the number of attempts needed to pass. Then `X~Geo(0.6)`, and failure probability is `0.4`.

(i) `P(X=5)=0.6(0.4)^4=0.01536`.

(ii) `P(X<=5)=1-0.4^5=0.98976`.

(iii) `P(X>5)=0.4^5=0.01024`.

Assumptions: each attempt is independent and the probability of passing remains fixed at `0.6` each time.

## Worked Example 4: Teacher explaining until the class understands

The probability the class all understands each explanation is `0.3`. Let `X` be the number of explanations needed. Then `X~Geo(0.3)` and failure probability is `0.7`.

(a) `P(X=4)=0.3(0.7)^3=0.1029`.

(b) `P(X<8)=P(X<=7)=1-0.7^7=0.9176` to 4 d.p.

(c) `P(X>5)=0.7^5=0.16807`.

## Worked Example 5: Dorothy’s biased coin

Dorothy flips a biased coin until it lands on heads. Let `Y` be the number of flips. If `E(Y)=2.5` and `Y~Geo(p)`, then `2.5=1/p`, so `p=1/2.5=0.4`.

`Var(Y)=(1-0.4)/(0.4)^2=0.6/0.16=3.75`.

The standard deviation is `sqrt(3.75)=1.94` to 3 s.f.

## Worked Example 6: Mixed Poisson-to-geometric synthesis, boundary-link example

This is a synthesis example. The geometric part is core; the Poisson part is a boundary-link to another `FAS2-DIST` lesson.

If the probability that a cookie has at least 10 chocolate chips is `0.0839`, then the number of cookies eaten until the first such cookie can be modelled as `Y~Geo(0.0839)`.

`P(Y>=7)=(1-0.0839)^6=0.9161^6=0.5911` to 4 d.p.

`E(Y)=1/0.0839=11.9` to 1 d.p.

`Var(Y)=(1-0.0839)/(0.0839)^2=130.1` to 1 d.p.

# 12. Common Mistakes and Exam Traps

1. Using binomial whenever repeated trials appear. Better: ask whether the number of trials is fixed or whether the process runs until the first success.
2. Defining `X` as number of successes. For geometric, `X` is number of trials until first success.
3. Starting `X` at 0. Correct support is `1,2,3,...`.
4. Mixing up `P(X>x)` and `P(X>=x)`: `P(X>x)=(1-p)^x`, but `P(X>=x)=(1-p)^(x-1)`.
5. Treating “less than 8” as `P(X<=8)`. Correct: `P(X<8)=P(X<=7)`.
6. Forgetting the final success in `P(X=x)`. Correct: `(1-p)^(x-1)p`.
7. Using `(1-p)^x p` for `P(X=x)`. There are only `x-1` failures before the success.
8. Assuming the model is automatically valid. Always check independence and fixed probability.
9. Calculator-only answers with no formula working.
10. Treating negative binomial as core content here. It is excluded.

# 13. Practice Questions

These are **generated practice questions**. They are not claimed to be past-paper or textbook questions.

1. Let `X~Geo(0.25)`. Find `P(X=3)`, `P(X<=4)`, `P(X>4)`, `P(X>=4)`.
2. A biased coin lands heads with probability `0.3` and is flipped until the first head. Write down the distribution of `X`; find `P(X=5)`, `P(X<5)`, and `P(X>=5)`.
3. A die is rolled until the first six appears. Find `E(X)`, `Var(X)`, and the standard deviation to 3 s.f.
4. Classify: fixed 12 multiple-choice questions; answer until first correct; calls in one hour; answer until third correct.
5. Probability of winning a game is `0.2`. Compare `Y`, number of wins in 10 games, and `X`, number of games until the first win.
6. Components are inspected until the first defective component, with defect probability `0.04`. Find the distribution, `P(X=8)`, `P(X<8)`, `P(X>12)`, and assumptions.
7. Website visitors click an advert with probability `0.015`. Find `P(X<=100)`, `P(X>100)`, `E(X)`, and interpret.
8. Spinner lands red with probability `p`; spun until first red. Given `E(X)=8`, find `p`, `Var(X)`, and `P(X<=3)`.
9. A game is played until first win. Given `P(X>3)=0.512`, find `p`.
10. Explain and correct the error: `X~Geo(0.4)`, `P(X>=6)=0.6^6`.
11. Tokens are drawn with replacement until the first gold token, with probability `0.08`. Find the smallest `k` such that `P(X<=k)>0.9`.

# 14. Worked Solutions

## Solution 1

`p=0.25`, so `1-p=0.75`.

(a) `P(X=3)=0.25(0.75)^2=0.140625`.

(b) `P(X<=4)=1-0.75^4=1-0.31640625=0.68359375`.

(c) `P(X>4)=0.75^4=0.31640625`.

(d) `P(X>=4)=0.75^3=0.421875`.

## Solution 2

`X~Geo(0.3)`, with failure probability `0.7`.

`P(X=5)=0.3(0.7)^4=0.07203`.

`P(X<5)=P(X<=4)=1-0.7^4=0.7599`.

`P(X>=5)=0.7^4=0.2401`.

## Solution 3

For rolling until a six, `p=1/6`, so `X~Geo(1/6)`.

`E(X)=1/(1/6)=6`.

`Var(X)=(1-1/6)/(1/6)^2=(5/6)/(1/36)=30`.

`sigma=sqrt(30)=5.48` to 3 s.f.

## Solution 4

(a) Fixed 12 questions and count correct: binomial.

(b) Until first correct: geometric.

(c) Calls in one hour: Poisson boundary-link.

(d) Until third correct: not core in this lesson; negative binomial-style, excluded.

## Solution 5

`Y~Bin(10,0.2)` because there are 10 fixed games and `Y` counts wins.

`X~Geo(0.2)` because games continue until the first win and `X` counts trials.

`Y` has possible values `0,1,...,10`; `X` has possible values `1,2,3,...`.

## Solution 6

`X~Geo(0.04)`, failure probability `0.96`.

`P(X=8)=0.04(0.96)^7=0.0301` to 4 d.p.

`P(X<8)=P(X<=7)=1-0.96^7=0.2486` to 4 d.p.

`P(X>12)=0.96^12=0.6127` to 4 d.p.

Assumptions: components are independent and defect probability remains fixed at `0.04`.

## Solution 7

`X~Geo(0.015)`, failure probability `0.985`.

`P(X<=100)=1-0.985^100=0.7794` to 4 d.p.

`P(X>100)=0.985^100=0.2206` to 4 d.p.

`E(X)=1/0.015=66.7` visitors to 3 s.f. On average, about 67 visitors are needed before the first advert click.

## Solution 8

`E(X)=1/p=8`, so `p=1/8`.

`Var(X)=(1-1/8)/(1/8)^2=(7/8)/(1/64)=56`.

`P(X<=3)=1-(7/8)^3=1-343/512=169/512=0.330078125`.

## Solution 9

`P(X>3)=(1-p)^3=0.512`.

`0.512=64/125=(4/5)^3`, so `1-p=4/5`, hence `p=1/5=0.2`.

## Solution 10

The error is using 6 failures instead of 5 failures. For `P(X>=6)`, the first 5 trials must fail.

Correct calculation:

`P(X>=6)=0.6^5=0.07776`.

## Solution 11

`X~Geo(0.08)`, so `P(X<=k)=1-0.92^k`.

Need `1-0.92^k>0.9`, so `0.92^k<0.1`.

Taking logs:

`k > log(0.1)/log(0.92)=27.615...`

Smallest integer is `k=28`.

Check: `P(X<=27)=0.8947...<0.9`, while `P(X<=28)=0.9031...>0.9`.

# 15. Exam Technique Notes

1. Always define the random variable: `X = the number of trials required until the first success`.
2. Identify success before calculating.
3. Use the failure probability carefully: `1-p`.
4. Translate wording before choosing a formula.
5. Use exact values when they are clean, for example `1/6` rather than `0.1666...`.
6. State assumptions in context.
7. Use calculator results as validation, not as a replacement for formula working.
8. Expect questions to ask you to state a distribution, calculate a probability, find a mean or variance, interpret a mean, state assumptions, or select a model from wording.

# 16. Syllabus Gap Check

| LO ID | Coverage status | Lesson coverage |
|---|---|---|
| `FAS2-DIST-LO001` | Fully covered | Geometric model, assumptions, notation and probabilities. |
| `FAS2-DIST-LO002` | Fully covered for geometric distribution | Probability function, mean, variance and standard deviation. |
| `FAS2-DIST-LO003` | Covered for simple discrete geometric cases | Exact, cumulative, tail and range-style probability methods. |
| `FAS2-DIST-LO006` | Mentioned only as supporting/synoptic | No detailed transformed-variable examples. |
| `FAS2-DIST-LO008` | Fully covered for geometric distribution | Mean and variance formulae used and interpreted. |
| `FAS2-DIST-LO007` | Boundary-link only | Poisson mentioned only for model-choice awareness. |
| `FAS2-DIST-LO004` | Not covered | Continuous distributions out of scope. |
| `FAS2-DIST-LO005` | Not covered | Continuous probability calculations out of scope. |

## Off-Spec Content Found but Excluded

Negative binomial distribution, third success on the fifteenth attempt, Bernoulli/beta/multinomial/multivariate/Dirichlet distributions, the full coupon collector problem, and probability generating function motivation are excluded from core content.

## Optional Enrichment Not Required by CCEA

Negative binomial distribution, coupon collector’s problem, full derivation of the variance formula, probability generating functions, and simulation of waiting times.

## Missing Evidence Log

Original CCEA specification PDF pages, CCEA geometric-distribution worked examples, CCEA mark schemes, fully inspected screenshot PDF and exact calculator button route were not supplied. The CCEA specification map was used as authority.

# 17. Recommended Enhancements Not in the Evidence

Recommended enhancements include a trial-strip diagram, complement diagram, binomial versus geometric split-screen, probability decay graph, assumptions checklist card, animations of trials revealing one-by-one, geometric probability calculator, wording classifier, model selector mini-game, and assumption critic.

# 18. Supplementary Sources Used

Project Sources used: `CCEA_GCE_Further_Mathematics_Specification_Map.md`, `Further_Maths_README_module_map.md`, `Further_Maths_EVIDENCE_DROP_CHECKLIST.md`, `Ordinary_A_Level_Maths_Bridge_Spec_Extracts.md`, and `CCEA_GCE_Mathematics_Specification_Map.md`.

Lesson-specific evidence used: `FS1-Chp3-GeometricNegativeBinomial.pdf`, `transcripts.md`, and `Chapter_3_Geometric_&_Negative_Binomial_Distributions_📊_(Further_Statistics_1)_screenshots.pdf`.

The Dr Frost / Pearson Further Statistics 1 evidence is not treated as CCEA authority. It is used only where the supplied CCEA FAS2-DIST specification map confirms the geometric distribution content is on-spec.

Ordinary A-Level Maths sources are used only to explain what the student already knows and how Further Maths extends it. They do not override the CCEA Further Mathematics specification boundary.

# 19. Final Student Checklist

## Prerequisite confidence checklist

- [ ] I can calculate a complement probability using `1-P(A)`.
- [ ] I can multiply probabilities for independent events.
- [ ] I can explain what `1-p` means.
- [ ] I can use powers such as `(1-p)^x`.
- [ ] I can distinguish `<`, `<=`, `>` and `>=`.
- [ ] I can recognise a geometric sequence.

## Further Maths method checklist

- [ ] I can state when a geometric distribution is appropriate.
- [ ] I can define `X` as the number of trials until the first success.
- [ ] I can write `X~Geo(p)`.
- [ ] I can use `P(X=x)=p(1-p)^(x-1)`.
- [ ] I can use `P(X<=x)=1-(1-p)^x`.
- [ ] I can use `P(X>x)=(1-p)^x`.
- [ ] I can use `P(X>=x)=(1-p)^(x-1)`.
- [ ] I can use `E(X)=1/p`.
- [ ] I can use `Var(X)=(1-p)/p^2`.
- [ ] I can find `sigma=sqrt(Var(X))`.

## Exam technique checklist

- [ ] I can translate “exactly `x`” into `P(X=x)`.
- [ ] I can translate “`x` or fewer” into `P(X<=x)`.
- [ ] I can translate “fewer than `x`” into `P(X<=x-1)`.
- [ ] I can translate “more than `x`” into `P(X>x)`.
- [ ] I can translate “at least `x`” into `P(X>=x)`.
- [ ] I can explain the difference between `P(X>5)` and `P(X>=5)`.
- [ ] I can state assumptions in context.
- [ ] I can give exact working before rounding.
- [ ] I can avoid using negative binomial as core content in this lesson.
