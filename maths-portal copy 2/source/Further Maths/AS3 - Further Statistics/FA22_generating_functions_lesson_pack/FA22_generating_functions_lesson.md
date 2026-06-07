# FA22_generating_functions_lesson.md

# 1. Lesson Title and Metadata

## Lesson Title

**Generating Functions, with Probability Generating Functions as Cross-Board Enrichment**

This lesson has two lanes:

- **Core CCEA lane:** generating functions as a way of encoding sequences and extracting coefficients.
- **Optional enrichment lane:** probability generating functions, where probabilities are encoded as coefficients of powers of \(t\).

The enrichment lane is mathematically useful, but it is not confirmed as CCEA core from the supplied specification map.

## Metadata

| Field | Value |
|---|---|
| Date generated | 2026-06-05 |
| Course | CCEA GCE Further Mathematics |
| Unit | `FA22` – Further A2 2 Applied Mathematics |
| Applied section | Section D: Discrete and Decision Mathematics |
| Topic code | `FA22-GENFUNC` |
| Official topic name | Generating functions |
| Evidence topic name | Probability Generating Functions |
| Topic slug | `generating_functions` |
| Topic Pascal | `GeneratingFunctions` |
| Topic ID | `FA22GeneratingFunctions` |
| Lesson file name | `FA22_generating_functions_lesson.md` |
| Primary LO IDs | `FA22-GENFUNC-LO001`, `FA22-GENFUNC-LO002`, `FA22-GENFUNC-LO003` |
| Boundary flag | PGF-specific statistics content is optional enrichment, not confirmed CCEA core |
| Bridge tags | `#AS1BinomialExpansion`, `#AS2Probability`, `#A21Differentiation`, `#A21Series`, `#FAS2StatisticalDistributions` |
| Topic tags | `#FA22`, `#GENFUNC`, `#GeneratingFunctions`, `#CoefficientExtraction`, `#Combinatorics`, `#OptionalPGFEnrichment` |

# 2. Evidence Map

| Evidence | Used in this lesson | Boundary note |
|---|---|---|
| CCEA Further Mathematics Specification Map | Determines official topic code, unit, section and LO IDs | Highest authority |
| Further Maths README Module Map | Confirms metadata rules and unit prefixes | Workflow authority |
| Further Maths Evidence Drop Checklist | Used to log missing CCEA-specific evidence and off-spec risks | Workflow authority |
| Ordinary A-Level Maths Bridge Extracts | Used for bridge table and prerequisite explanation | Bridge only |
| CCEA GCE Mathematics Specification Map | Used for ordinary AS/A2 Maths foundations | Bridge only |
| DrFrost / Pearson-style FS1 PGF PDF | Supplies PGF definitions, examples, properties and visuals | Cross-board enrichment unless confirmed by CCEA |
| Screenshots PDF | Supplies visual evidence and handwritten solutions where visible | Cross-board enrichment; not all pages parsed |
| Transcript file | Supplies teacher phrasing, warnings and worked-example commentary | Cross-board enrichment unless confirmed by CCEA |

The PDF evidence defines a probability generating function as an encoding of a probability distribution as a polynomial, with outcomes as powers and probabilities as coefficients. The transcript reinforces that \(t\) is a dummy variable, powers of \(t\) represent outcomes, and coefficients represent probabilities.

# 3. Specification Alignment

| LO ID | Official wording | Lesson coverage | Evidence source | Syllabus boundary | Ordinary A-Level bridge |
|---|---|---|---|---|---|
| `FA22-GENFUNC-LO001` | demonstrate understanding of the meaning of a generating function | Covered through general coefficient encoding and coefficient extraction | CCEA Further Maths spec map; PGF evidence used only as an analogy | Core | AS1 binomial expansion; sequences and series |
| `FA22-GENFUNC-LO002` | formulate a generating function to solve simple summation problems | Introduced conceptually; full CCEA-style examples missing | CCEA spec map only | Core but evidence incomplete | AS1 sequences and series |
| `FA22-GENFUNC-LO003` | use combinatorial arguments and elementary generating functions to prove simple formulae involving, for example, binomial coefficients | Introduced through coefficient language; full CCEA-style combinatorial proof evidence missing | CCEA spec map only | Core but evidence incomplete | AS1 binomial coefficients and \({}^nC_r\) |

## Related but not primary CCEA context

| Related LO area | Relevance |
|---|---|
| FAS2 Statistical distributions | PGF enrichment uses discrete random variables, geometric distribution, Poisson distribution, expectation and variance. |
| FA22 Linear combinations of independent variables | PGF enrichment includes sums and transformations of random variables, but CCEA’s linear-combination topic is about expectation/variance and normal variables, not PGFs. |

# 4. Learning Objectives

## Core Further Maths objectives

By the end of the CCEA core lane, you should be able to:

1. Explain what a generating function is.
2. Read coefficients from a power series or polynomial.
3. Understand that a generating function stores information in the coefficients of powers.
4. Use coefficient extraction notation such as \([t^r]G(t)\).
5. Recognise why binomial coefficients naturally appear in generating-function arguments.
6. State clearly that the supplied PGF statistics results are enrichment unless CCEA-specific evidence confirms otherwise.

## Bridge objectives

You should be able to connect this topic to ordinary A-Level Maths by:

1. Using binomial expansion without expanding more than necessary.
2. Recognising powers and coefficients from polynomial algebra.
3. Using probability distribution tables where probabilities sum to 1.
4. Understanding how differentiation and series become useful tools in extended generating-function work.
5. Knowing the difference between a general generating function and a probability generating function.

## Exam technique objectives

You should be able to:

1. Extract the required coefficient rather than expand an entire expression blindly.
2. Label the variable used in the generating function.
3. Avoid mixing up powers and coefficients.
4. Check whether a method is CCEA core or optional enrichment.
5. Use exact values where possible.
6. State conclusions in terms of the original counting, sequence or probability problem.

# 5. Explicit Prerequisite Recap

## GCSE foundations

You need powers and indices, expanding brackets, collecting like terms, reading tables, basic probability, fractions and exact arithmetic.

## Ordinary AS/A2 Mathematics foundations

You need binomial expansion of \((a+bx)^n\), factorial notation \(n!\), binomial coefficients \({}^nC_r\), probability distributions and probability tables, discrete random variables, expectation and variance as background for PGF enrichment, differentiation of polynomials and exponentials, and series notation.

## Previous Further Mathematics foundations

For the official CCEA `FA22-GENFUNC` topic, the most relevant foundations are algebraic manipulation, binomial coefficients, proof structure, combinatorial reasoning and summation notation.

For the optional PGF enrichment, the most relevant Further Statistics foundations are binomial, geometric and Poisson distributions, expectation and variance, and independent random variables.

### A-Level Maths Bridge: What You Already Know and What Further Maths Changes

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| AS1 Sequences and series | Expand \((a+bx)^n\) and use \({}^nC_r\) | Instead of merely expanding, use coefficients as stored information | Expanding the whole expression can be slow when only one coefficient is needed. |
| AS2 Probability | Work with probability tables and probabilities summing to 1 | PGF enrichment stores probabilities as coefficients | This is not confirmed as CCEA core; do not treat all PGF statistics formulae as examinable without CCEA evidence. |
| AS2 Statistical distributions | Use binomial distributions and discrete probability distributions | PGFs can encode distributions compactly | The dummy variable \(t\) is not a random variable. |
| A21 Differentiation | Differentiate polynomials and exponentials | PGF enrichment uses derivatives at \(t=1\) | Differentiate with respect to \(t\), not with respect to the outcome value \(x\). |
| A21 Series | Work with expansions and series | Infinite generating functions may encode infinitely many terms | Some generating functions simplify to non-polynomial forms. |

In ordinary A-Level Maths, this idea appeared as binomial expansion, probability tables and sequences. In Further Maths, the same idea becomes an encoding machine: powers mark positions, outcomes or counts, while coefficients store the information. The key upgrade is that algebra becomes a storage system. The danger is that PGF-specific probability formulae are not automatically CCEA core.

# 6. Big Picture Explanation

A generating function is a way of putting a sequence into algebraic form. If the sequence is

\[
a_0,\ a_1,\ a_2,\ a_3,\ldots,
\]

then its generating function is usually written as

\[
G(t)=a_0+a_1t+a_2t^2+a_3t^3+\cdots.
\]

The coefficient of \(t^r\) is \(a_r\). So the power tells you where to look, and the coefficient tells you what is stored there.

For example, if

\[
G(t)=4+7t+2t^2+11t^3,
\]

then

\[
[t^0]G(t)=4,\qquad [t^1]G(t)=7,\qquad [t^2]G(t)=2,\qquad [t^3]G(t)=11.
\]

The notation

\[
[t^r]G(t)
\]

means “the coefficient of \(t^r\) in \(G(t)\).”

Generating functions turn counting or summation problems into algebra problems. Instead of counting one case at a time, we encode the situation into a polynomial or power series, manipulate it, and then extract the coefficient we need.

# 7. Key Definitions and Notation

## Definition: generating function

A **generating function** is a function, often written as a polynomial or power series, whose coefficients encode a sequence.

If

\[
a_0,\ a_1,\ a_2,\ldots
\]

is a sequence, then an ordinary generating function for the sequence is

\[
G(t)=\sum_{r=0}^{\infty}a_rt^r.
\]

Expanded:

\[
G(t)=a_0+a_1t+a_2t^2+a_3t^3+\cdots.
\]

Here:

- \(t\) is a dummy variable;
- \(r\) is the index;
- \(a_r\) is the coefficient of \(t^r\);
- \([t^r]G(t)\) means the coefficient of \(t^r\) in \(G(t)\).

## Definition: coefficient extraction

\[
[t^r]G(t)
\]

means “extract the coefficient of \(t^r\) from \(G(t)\).”

Example:

\[
G(t)=5-3t+8t^2+10t^5.
\]

Then

\[
[t^0]G(t)=5,
\]

\[
[t^1]G(t)=-3,
\]

\[
[t^2]G(t)=8,
\]

\[
[t^3]G(t)=0,
\]

and

\[
[t^5]G(t)=10.
\]

## Optional enrichment definition: probability generating function

If \(X\) is a discrete random variable taking non-negative integer values, its probability generating function is

\[
G_X(t)=E(t^X).
\]

Equivalently,

\[
G_X(t)=\sum_{x=0}^{\infty}P(X=x)t^x.
\]

If the distribution is finite, this becomes a polynomial.

If

| \(x\) | 0 | 1 | 2 | 3 |
|---|---:|---:|---:|---:|
| \(P(X=x)\) | 0.2 | 0.3 | 0.35 | 0.15 |

then

\[
G_X(t)=0.2t^0+0.3t^1+0.35t^2+0.15t^3.
\]

Since \(t^0=1\) and \(t^1=t\),

\[
G_X(t)=0.2+0.3t+0.35t^2+0.15t^3.
\]

Do not confuse \(G_X(t)\) with \(P(X=x)\). The first is a function in the dummy variable \(t\). The second is a probability assigned to a particular outcome \(x\).

# 8. Core Theory

## 8.1 Core CCEA idea: storing information in coefficients

A generating function takes a sequence and stores it as coefficients. Suppose

\[
a_0=2,\qquad a_1=5,\qquad a_2=9,\qquad a_3=14.
\]

The generating function begins

\[
G(t)=2+5t+9t^2+14t^3+\cdots.
\]

So:

\[
[t^0]G(t)=2,\qquad [t^1]G(t)=5,\qquad [t^2]G(t)=9,\qquad [t^3]G(t)=14.
\]

**Bridge Note:** In ordinary A-Level Maths, you expanded expressions and read coefficients. Here, Further Maths turns that habit into a method: coefficients are the objects we are actually trying to find.

## 8.2 Coefficients can be missing

If

\[
G(t)=1+4t^2+6t^5,
\]

then

\[
[t^0]G(t)=1,
\]

\[
[t^1]G(t)=0,
\]

\[
[t^2]G(t)=4,
\]

\[
[t^3]G(t)=0,
\]

\[
[t^4]G(t)=0,
\]

\[
[t^5]G(t)=6.
\]

A missing power means its coefficient is zero.

## 8.3 Optional PGF enrichment: from probability table to polynomial

For a probability generating function,

\[
G_X(t)=\sum P(X=x)t^x.
\]

Using the distribution

| \(x\) | 0 | 1 | 2 | 3 |
|---|---:|---:|---:|---:|
| \(P(X=x)\) | 0.2 | 0.3 | 0.35 | 0.15 |

we get

\[
G_X(t)=P(X=0)t^0+P(X=1)t^1+P(X=2)t^2+P(X=3)t^3.
\]

Now insert the probabilities:

\[
G_X(t)=0.2t^0+0.3t^1+0.35t^2+0.15t^3.
\]

Since \(t^0=1\) and \(t^1=t\),

\[
G_X(t)=0.2+0.3t+0.35t^2+0.15t^3.
\]

Each term stores one probability. For example,

\[
0.35t^2
\]

stores

\[
P(X=2)=0.35.
\]

## 8.4 Optional PGF enrichment: from polynomial back to table

Suppose

\[
G_X(t)=0.1+0.3t^2+0.6t^3.
\]

Read the powers:

- \(0.1=0.1t^0\), so \(x=0\) has probability \(0.1\);
- \(0.3t^2\), so \(x=2\) has probability \(0.3\);
- \(0.6t^3\), so \(x=3\) has probability \(0.6\).

So the distribution is

| \(x\) | 0 | 2 | 3 |
|---|---:|---:|---:|
| \(P(X=x)\) | 0.1 | 0.3 | 0.6 |

Check:

\[
0.1+0.3+0.6=1.
\]

## 8.5 Optional PGF enrichment: why \(G_X(1)=1\)

For

\[
G_X(t)=0.2+0.3t+0.35t^2+0.15t^3,
\]

substitute \(t=1\):

\[
G_X(1)=0.2+0.3(1)+0.35(1)^2+0.15(1)^3.
\]

Since \((1)^2=1\) and \((1)^3=1\),

\[
G_X(1)=0.2+0.3+0.35+0.15=1.
\]

In general,

\[
G_X(t)=\sum_x P(X=x)t^x.
\]

Putting \(t=1\),

\[
G_X(1)=\sum_x P(X=x)1^x=\sum_xP(X=x)=1.
\]

## 8.6 Optional PGF enrichment: finding a constant using \(G_X(1)=1\)

Let

\[
G_X(t)=k(1+t)^2.
\]

Since \(G_X(t)\) is a PGF,

\[
G_X(1)=1.
\]

Substitute:

\[
k(1+1)^2=1.
\]

Thus

\[
k(2)^2=1,
\]

\[
4k=1,
\]

\[
k=\frac14.
\]

Then

\[
G_X(t)=\frac14(1+t)^2=\frac14(1+2t+t^2)=\frac14+\frac12t+\frac14t^2.
\]

So

| \(x\) | 0 | 1 | 2 |
|---|---:|---:|---:|
| \(P(X=x)\) | \(\frac14\) | \(\frac12\) | \(\frac14\) |

## 8.7 Core coefficient extraction: do not expand everything unless necessary

Suppose

\[
G(t)=t^4(2+3t)^5.
\]

Find

\[
[t^7]G(t).
\]

Because of the factor \(t^4\), we need the coefficient of \(t^3\) in

\[
(2+3t)^5.
\]

Why?

\[
t^4\cdot t^3=t^7.
\]

Use the binomial theorem:

\[
(2+3t)^5=\sum_{r=0}^{5}{}^5C_r(2)^{5-r}(3t)^r.
\]

The \(t^3\) term occurs when \(r=3\):

\[
{}^5C_3(2)^{5-3}(3t)^3={}^5C_3(2)^2(3t)^3.
\]

Now

\[
{}^5C_3=10,
\]

\[
2^2=4,
\]

and

\[
(3t)^3=27t^3.
\]

Therefore the \(t^3\) coefficient is

\[
10\cdot4\cdot27=1080.
\]

So

\[
[t^7]\left[t^4(2+3t)^5\right]=1080.
\]

## 8.8 Optional PGF enrichment: \(G_X(t)=E(t^X)\)

For a discrete random variable \(X\),

\[
G_X(t)=\sum_x P(X=x)t^x.
\]

Recall

\[
E(h(X))=\sum_x h(x)P(X=x).
\]

Choose \(h(X)=t^X\). Then \(h(x)=t^x\), so

\[
E(t^X)=\sum_xt^xP(X=x)=\sum_xP(X=x)t^x=G_X(t).
\]

## 8.9 Optional PGF enrichment: standard PGFs

Let \(q=1-p\).

| Distribution | Support | PGF |
|---|---:|---|
| \(X\sim B(n,p)\) | \(0,1,\ldots,n\) | \(G_X(t)=(q+pt)^n\) |
| \(X\sim \operatorname{Po}(\lambda)\) | \(0,1,2,\ldots\) | \(G_X(t)=e^{\lambda(t-1)}\) |
| \(X\sim \operatorname{Geo}(p)\), first success on trial \(1,2,\ldots\) | \(1,2,\ldots\) | \(G_X(t)=\dfrac{pt}{1-qt}\) |
| \(X\sim \operatorname{Negative\ B}(r,p)\), number of trials to \(r\) successes | \(r,r+1,\ldots\) | \(G_X(t)=\left(\dfrac{pt}{1-qt}\right)^r\) |

The negative binomial distribution was not found in the supplied CCEA Further Mathematics specification map. Treat it as off-spec enrichment.

## 8.10 Optional PGF enrichment: binomial PGF from first principles

Suppose \(X\sim B(n,p)\). Then

\[
P(X=x)={}^nC_xp^xq^{n-x},\qquad q=1-p.
\]

The PGF is

\[
G_X(t)=\sum_{x=0}^{n}P(X=x)t^x.
\]

Substitute:

\[
G_X(t)=\sum_{x=0}^{n}{}^nC_xp^xq^{n-x}t^x.
\]

Group \(p^x\) and \(t^x\):

\[
p^xt^x=(pt)^x.
\]

So

\[
G_X(t)=\sum_{x=0}^{n}{}^nC_x(pt)^xq^{n-x}.
\]

By the binomial theorem,

\[
(q+pt)^n=\sum_{x=0}^{n}{}^nC_xq^{n-x}(pt)^x.
\]

Thus

\[
G_X(t)=(q+pt)^n=(1-p+pt)^n.
\]

### Evidence example: archer

If an archer hits the bullseye with probability \(0.6\) and fires three shots, then

\[
X\sim B(3,0.6).
\]

So \(p=0.6\), \(q=0.4\), and

\[
G_X(t)=(0.4+0.6t)^3.
\]

From first principles,

\[
G_X(t)=0.4^3+3(0.6)(0.4)^2t+3(0.6)^2(0.4)t^2+0.6^3t^3.
\]

This is exactly the expansion of

\[
(0.4+0.6t)^3.
\]

## 8.11 Optional PGF enrichment: Poisson PGF from first principles

Suppose \(X\sim \operatorname{Po}(\lambda)\). Then

\[
P(X=x)=e^{-\lambda}\frac{\lambda^x}{x!},\qquad x=0,1,2,\ldots.
\]

The PGF is

\[
G_X(t)=\sum_{x=0}^{\infty}P(X=x)t^x.
\]

Substitute:

\[
G_X(t)=\sum_{x=0}^{\infty}e^{-\lambda}\frac{\lambda^x}{x!}t^x.
\]

Factor out \(e^{-\lambda}\):

\[
G_X(t)=e^{-\lambda}\sum_{x=0}^{\infty}\frac{\lambda^xt^x}{x!}.
\]

Combine powers:

\[
\lambda^xt^x=(\lambda t)^x.
\]

So

\[
G_X(t)=e^{-\lambda}\sum_{x=0}^{\infty}\frac{(\lambda t)^x}{x!}.
\]

Using

\[
e^u=\sum_{x=0}^{\infty}\frac{u^x}{x!},
\]

with \(u=\lambda t\),

\[
G_X(t)=e^{-\lambda}e^{\lambda t}=e^{-\lambda+\lambda t}=e^{\lambda(t-1)}.
\]

## 8.12 Optional PGF enrichment: geometric PGF from first principles

Suppose \(X\) is the number of trials up to and including the first success, with success probability \(p\). Then

\[
X\sim \operatorname{Geo}(p),\qquad x=1,2,3,\ldots.
\]

Let \(q=1-p\). Then

\[
P(X=x)=q^{x-1}p.
\]

The PGF is

\[
G_X(t)=\sum_{x=1}^{\infty}P(X=x)t^x.
\]

Substitute:

\[
G_X(t)=\sum_{x=1}^{\infty}q^{x-1}pt^x.
\]

Write out terms:

\[
G_X(t)=pt+qpt^2+q^2pt^3+q^3pt^4+\cdots.
\]

Factor out \(pt\):

\[
G_X(t)=pt(1+qt+q^2t^2+q^3t^3+\cdots).
\]

This is an infinite geometric series with first term \(1\) and common ratio \(qt\), so

\[
1+qt+q^2t^2+q^3t^3+\cdots=\frac{1}{1-qt}.
\]

Therefore

\[
G_X(t)=\frac{pt}{1-qt}=\frac{pt}{1-(1-p)t}.
\]

## 8.13 Optional PGF enrichment: expectation from a PGF

Start with

\[
G_X(t)=\sum_{x=0}^{\infty}P(X=x)t^x.
\]

Differentiate with respect to \(t\):

\[
G'_X(t)=\sum_{x=0}^{\infty}P(X=x)\frac{d}{dt}(t^x).
\]

Since

\[
\frac{d}{dt}(t^x)=xt^{x-1},
\]

we get

\[
G'_X(t)=\sum_{x=0}^{\infty}xP(X=x)t^{x-1}.
\]

Substitute \(t=1\):

\[
G'_X(1)=\sum_{x=0}^{\infty}xP(X=x)1^{x-1}.
\]

Since \(1^{x-1}=1\),

\[
G'_X(1)=\sum_{x=0}^{\infty}xP(X=x)=E(X).
\]

Therefore

\[
E(X)=G'_X(1).
\]

## 8.14 Optional PGF enrichment: variance from a PGF

Differentiate twice:

\[
G''_X(t)=\sum_{x=0}^{\infty}x(x-1)P(X=x)t^{x-2}.
\]

Substitute \(t=1\):

\[
G''_X(1)=\sum_{x=0}^{\infty}x(x-1)P(X=x)=E[X(X-1)].
\]

Since

\[
X(X-1)=X^2-X,
\]

\[
G''_X(1)=E(X^2)-E(X).
\]

Therefore

\[
E(X^2)=G''_X(1)+E(X)=G''_X(1)+G'_X(1).
\]

Variance is

\[
\operatorname{Var}(X)=E(X^2)-[E(X)]^2.
\]

So

\[
\boxed{\operatorname{Var}(X)=G''_X(1)+G'_X(1)-[G'_X(1)]^2.}
\]

## 8.15 Optional PGF enrichment: sums of independent random variables

If \(X\) and \(Y\) are independent non-negative integer-valued random variables, and \(Z=X+Y\), then

\[
G_Z(t)=G_X(t)G_Y(t).
\]

Why?

\[
G_Z(t)=E(t^Z)=E(t^{X+Y})=E(t^Xt^Y).
\]

Because \(X\) and \(Y\) are independent,

\[
E(t^Xt^Y)=E(t^X)E(t^Y)=G_X(t)G_Y(t).
\]

## 8.16 Optional PGF enrichment: linear coding of variables

If \(Y=aX+b\), then

\[
G_Y(t)=t^bG_X(t^a).
\]

Derivation:

\[
G_Y(t)=E(t^Y)=E(t^{aX+b})=E(t^bt^{aX}).
\]

Since \(t^b\) does not depend on \(X\),

\[
G_Y(t)=t^bE(t^{aX}).
\]

Now

\[
t^{aX}=(t^a)^X,
\]

so

\[
G_Y(t)=t^bE((t^a)^X)=t^bG_X(t^a).
\]

## 8.17 Boundary summary for Core Theory

The CCEA-safe core from this section is

\[
G(t)=a_0+a_1t+a_2t^2+\cdots,
\]

and

\[
[t^r]G(t)=a_r.
\]

The CCEA-safe method is:

1. Encode information as coefficients.
2. Manipulate the generating function algebraically.
3. Extract the coefficient needed.
4. Interpret the coefficient in the original problem.

The PGF enrichment adds probability-specific meaning:

\[
G_X(t)=\sum_xP(X=x)t^x=E(t^X).
\]

That enrichment is useful, but it remains outside confirmed CCEA core from the supplied Project Sources.

# 9. Visual Asset Integration

## 9.1 Visual evidence limitations

Diagram evidence is partially unclear here. The description below preserves the visible/readable details only. No uninspected visual detail is claimed.

The screenshot PDF contains rendered slide images, but its text was not parsed as normal text. The readable visual evidence from the screenshots and PDF shows:

- a probability table being converted into a polynomial;
- powers of \(t\) representing outcomes;
- coefficients representing probabilities;
- arrows from tables to PGFs;
- handwritten examples converting between tables and PGFs;
- a dice absolute-difference table;
- standard PGF tables for binomial, Poisson, geometric and negative binomial distributions.

The lesson uses these as PGF enrichment visuals, not as confirmed CCEA core.

[VISUAL PLACEHOLDER: FA22GeneratingFunctionsMermaid-001 | Source: CCEA FA22-GENFUNC boundary + supplied PGF enrichment evidence | Insert from mermaid/FA22GeneratingFunctionsMermaid-001.md | Purpose: Show the flow from encoded information to generating function to coefficient extraction. The visual must show: sequence/table → powers of \(t\) → coefficients → extract \([t^r]G(t)\) → interpret answer.]

[VISUAL PLACEHOLDER: FA22GeneratingFunctionsSVG-001 | Source: FS1 PGF PDF page explaining outcomes as powers and probabilities as coefficients | Insert from svg/FA22GeneratingFunctionsSVG-001.svg | Purpose: Preserve the evidence-backed PGF idea that outcomes are powers and probabilities are coefficients. The visual must show a two-row probability table and its PGF \(G_X(t)=0.2+0.3t+0.35t^2+0.15t^3\).]

[VISUAL PLACEHOLDER: FA22GeneratingFunctionsBridgeSVG-001 | Source: Ordinary A-Level Maths bridge + Further Maths generating functions topic | Insert from svg/FA22GeneratingFunctionsBridgeSVG-001.svg | Purpose: Compare ordinary binomial expansion with Further Maths coefficient extraction. The visual must show full expansion as the slower route and \([t^r]\) extraction as the targeted route.]

[VISUAL PLACEHOLDER: FA22GeneratingFunctionsTikZ-001 | Source: CCEA core generating functions concept | Insert from tikz/FA22GeneratingFunctionsTikZ-001.tex | Purpose: Provide a clean coefficient-extraction diagram for \(G(t)=a_0+a_1t+a_2t^2+a_3t^3+\cdots\). The visual must label \(a_r=[t^r]G(t)\).]

[VISUAL PLACEHOLDER: FA22GeneratingFunctionsTikZ-002 | Source: Supplied PGF enrichment evidence | Insert from tikz/FA22GeneratingFunctionsTikZ-002.tex | Purpose: Show probability table to PGF encoding. The visual must label \(t\) as a dummy variable, powers as outcomes, and coefficients as probabilities.]

[VISUAL PLACEHOLDER: FA22GeneratingFunctionsTikZ-003 | Source: Supplied PGF enrichment evidence on independent sums | Insert from tikz/FA22GeneratingFunctionsTikZ-003.tex | Purpose: Show how multiplying PGFs makes powers add and coefficients combine. The visual must show \(G_{X+Y}(t)=G_X(t)G_Y(t)\), with a note that this is optional PGF enrichment.]

# 10. Interactive Learning Widgets

[INTERACTIVE PLACEHOLDER: FA22GeneratingFunctionsWidget-001 | Source: AI-proposed teaching enhancement based on CCEA core generating-function evidence | Insert from widgets/FA22GeneratingFunctionsWidget-001.html | Purpose: Practise coefficient extraction from ordinary generating functions.]

Student inputs a polynomial such as \(4+3t+7t^2+2t^5\) and a requested power \(r\). The widget displays the coefficient \([t^r]G(t)\), whether the power is present or missing, and a table of powers and coefficients.

[INTERACTIVE PLACEHOLDER: FA22GeneratingFunctionsWidget-002 | Source: AI-proposed teaching enhancement based on supplied PGF enrichment evidence | Insert from widgets/FA22GeneratingFunctionsWidget-002.html | Purpose: Convert between a probability table and a probability generating function.]

Student inputs outcomes \(x\) and probabilities \(P(X=x)\). The widget displays \(G_X(t)=\sum P(X=x)t^x\), checks that probabilities sum to 1, and warns if an outcome is not a non-negative integer. Boundary label: PGF enrichment, not confirmed CCEA core from supplied sources.

[INTERACTIVE PLACEHOLDER: FA22GeneratingFunctionsWidget-003 | Source: AI-proposed teaching enhancement based on ordinary A-Level Maths bridge + CCEA coefficient extraction | Insert from widgets/FA22GeneratingFunctionsWidget-003.html | Purpose: Target coefficients in binomial expansions without expanding the full expression.]

Student inputs \(n\), \(a\), \(b\), and requested \(r\) for \((a+bt)^n\). The widget displays

\[
[t^r](a+bt)^n={}^nC_ra^{n-r}b^r.
\]

# 11. Worked Examples

## Worked Example 1: Core CCEA coefficient extraction

Find

\[
[t^4](2+3t)^6.
\]

Use the binomial theorem:

\[
(2+3t)^6=\sum_{r=0}^{6}{}^6C_r(2)^{6-r}(3t)^r.
\]

We need \(t^4\), so take \(r=4\). The \(t^4\) term is

\[
{}^6C_4(2)^{6-4}(3t)^4={}^6C_4(2)^2(3t)^4.
\]

Now

\[
{}^6C_4=15,
\]

\[
2^2=4,
\]

and

\[
(3t)^4=3^4t^4=81t^4.
\]

So the coefficient is

\[
15\cdot4\cdot81=4860.
\]

Final answer:

\[
\boxed{4860}
\]

## Worked Example 2: Core CCEA coefficient shift

Find

\[
[t^9]\left(t^3(1+2t)^8\right).
\]

The outside \(t^3\) means \(t^3\cdot t^6=t^9\), so we need

\[
[t^6](1+2t)^8.
\]

Use the binomial theorem:

\[
(1+2t)^8=\sum_{r=0}^{8}{}^8C_r(1)^{8-r}(2t)^r.
\]

The \(t^6\) term occurs when \(r=6\):

\[
{}^8C_6(1)^{8-6}(2t)^6={}^8C_6(1)^2(2t)^6.
\]

Now

\[
{}^8C_6=28,
\]

\[
(2t)^6=64t^6.
\]

So the coefficient is

\[
28\cdot64=1792.
\]

Final answer:

\[
\boxed{1792}
\]

## Worked Example 3: Optional PGF enrichment, probability table to PGF

A random variable \(X\) has distribution

| \(x\) | 0 | 2 | 4 |
|---|---:|---:|---:|
| \(P(X=x)\) | \(0.25\) | \(0.5\) | \(0.25\) |

Write down \(G_X(t)\).

The probability generating function is

\[
G_X(t)=\sum_xP(X=x)t^x.
\]

Substitute:

\[
G_X(t)=0.25t^0+0.5t^2+0.25t^4.
\]

Since \(t^0=1\),

\[
\boxed{G_X(t)=0.25+0.5t^2+0.25t^4}
\]

## Worked Example 4: Optional PGF enrichment, PGF to table

Given

\[
G_Y(t)=\frac{1}{10}t+\frac{1}{5}t^2+\frac{7}{10}t^4,
\]

read off the probability distribution.

The powers are \(1\), \(2\), and \(4\), so

| \(y\) | 1 | 2 | 4 |
|---|---:|---:|---:|
| \(P(Y=y)\) | \(\frac{1}{10}\) | \(\frac{1}{5}\) | \(\frac{7}{10}\) |

Check:

\[
\frac{1}{10}+\frac{1}{5}+\frac{7}{10}=\frac{10}{10}=1.
\]

## Worked Example 5: Optional PGF enrichment, finding a constant

Given

\[
G_X(t)=k(1+t)^2,
\]

use \(G_X(1)=1\):

\[
k(1+1)^2=1,
\]

\[
4k=1,
\]

\[
k=\frac14.
\]

Then

\[
G_X(t)=\frac14(1+t)^2=\frac14+\frac12t+\frac14t^2.
\]

So

| \(x\) | 0 | 1 | 2 |
|---|---:|---:|---:|
| \(P(X=x)\) | \(\frac14\) | \(\frac12\) | \(\frac14\) |

## Worked Example 6: Optional PGF enrichment, sum of independent random variables

Let

\[
G_X(t)=\frac12+\frac12t,
\]

and

\[
G_Y(t)=\frac13+\frac12t+\frac16t^2.
\]

For independent \(X\) and \(Y\),

\[
G_{X+Y}(t)=G_X(t)G_Y(t).
\]

So

\[
G_{X+Y}(t)=\left(\frac12+\frac12t\right)\left(\frac13+\frac12t+\frac16t^2\right).
\]

Multiplying:

\[
G_{X+Y}(t)=\frac16+\frac14t+\frac{1}{12}t^2+\frac16t+\frac14t^2+\frac{1}{12}t^3.
\]

Collecting like terms:

\[
G_{X+Y}(t)=\frac16+\frac{5}{12}t+\frac13t^2+\frac{1}{12}t^3.
\]

# 12. Common Mistakes and Exam Traps

| Trap | Why it is wrong | Safer method |
|---|---|---|
| Treating the power as the stored value | The stored value is the coefficient | Use \([t^r]G(t)\). |
| Treating a missing power as coefficient \(1\) | Missing term means coefficient \(0\) | Write missing terms explicitly if needed. |
| Expanding a full polynomial when only one coefficient is needed | Wastes time and invites errors | Use the binomial theorem to target the required power. |
| Forgetting outside powers like \(t^3(1+2t)^8\) | The outside power shifts the target | Solve \(3+r=\text{target power}\). |
| Confusing \(t\) with a numerical variable | \(t\) is usually a dummy variable | Use it as a bookkeeping symbol. |
| Using PGF properties as confirmed CCEA core | The supplied CCEA map confirms “generating functions”, not PGFs specifically | Label PGF work as enrichment unless CCEA evidence confirms it. |
| Swapping outcomes and probabilities | Outcomes are powers, probabilities are coefficients | Build \(P(X=x)t^x\). |
| Using negative outcomes in a standard PGF | PGFs use non-negative integer powers | Restrict to non-negative integer outcomes. |
| Multiplying PGFs for non-independent variables | The product rule for sums needs independence | Check independence is stated. |

# 13. Practice Questions

## Core CCEA-aligned questions

1. Let \(G(t)=6-4t+9t^2+3t^5\). Find \([t^0]G(t)\), \([t^1]G(t)\), \([t^3]G(t)\), and \([t^5]G(t)\).
2. Find \([t^3](1+4t)^7\).
3. Find \([t^8]\left(t^2(3-t)^6\right)\).
4. Find \([t^5]\left((1+t)^4(1+2t)^3\right)\).
5. Without expanding all of \((2-5t)^8\), find \([t^2](2-5t)^8\).
6. Explain why Further Maths generating-function questions often prefer coefficient extraction.

## Optional PGF enrichment questions

7. A random variable \(X\) has distribution

| \(x\) | 0 | 1 | 3 |
|---|---:|---:|---:|
| \(P(X=x)\) | \(\frac15\) | \(\frac12\) | \(\frac{3}{10}\) |

Write down \(G_X(t)\), and verify \(G_X(1)=1\).

8. A random variable \(Y\) has PGF

\[
G_Y(t)=\frac{2}{7}+\frac{3}{7}t^2+\frac{2}{7}t^5.
\]

Write down the probability distribution of \(Y\).

9. A random variable \(X\) has PGF

\[
G_X(t)=k(1+2t)^3.
\]

Find \(k\), then find \(P(X=2)\).

10. Independent random variables \(X\) and \(Y\) have PGFs

\[
G_X(t)=\frac13+\frac23t,
\]

and

\[
G_Y(t)=\frac14+\frac12t+\frac14t^2.
\]

Find the PGF of \(Z=X+Y\).

# 14. Worked Solutions

## Solution 1

Given

\[
G(t)=6-4t+9t^2+3t^5.
\]

\[
[t^0]G(t)=6,
\]

\[
[t^1]G(t)=-4,
\]

\[
[t^3]G(t)=0,
\]

because there is no \(t^3\) term, and

\[
[t^5]G(t)=3.
\]

## Solution 2

\[
(1+4t)^7=\sum_{r=0}^{7}{}^7C_r(1)^{7-r}(4t)^r.
\]

For \(t^3\), take \(r=3\):

\[
{}^7C_3(1)^4(4t)^3.
\]

Now \({}^7C_3=35\) and \((4t)^3=64t^3\), so

\[
[t^3](1+4t)^7=35\cdot64=2240.
\]

## Solution 3

To find

\[
[t^8]\left(t^2(3-t)^6\right),
\]

we need \([t^6](3-t)^6\). The \(t^6\) term is

\[
{}^6C_6(3)^0(-t)^6=t^6.
\]

So the coefficient is

\[
\boxed{1}.
\]

## Solution 4

Possible powers giving \(t^5\) are \((2,3)\), \((3,2)\), and \((4,1)\). Thus

\[
[t^5]\left((1+t)^4(1+2t)^3\right)
=
[t^2](1+t)^4[t^3](1+2t)^3
+
[t^3](1+t)^4[t^2](1+2t)^3
+
[t^4](1+t)^4[t^1](1+2t)^3.
\]

Now

\[
[t^2](1+t)^4=6,\quad [t^3](1+t)^4=4,\quad [t^4](1+t)^4=1,
\]

and

\[
[t^3](1+2t)^3=8,\quad [t^2](1+2t)^3=12,\quad [t^1](1+2t)^3=6.
\]

So

\[
[t^5]=6\cdot8+4\cdot12+1\cdot6=48+48+6=102.
\]

## Solution 5

\[
(2-5t)^8=\sum_{r=0}^{8}{}^8C_r(2)^{8-r}(-5t)^r.
\]

For \(t^2\), take \(r=2\):

\[
{}^8C_2(2)^6(-5t)^2.
\]

Now \({}^8C_2=28\), \(2^6=64\), and \((-5t)^2=25t^2\), so

\[
[t^2](2-5t)^8=28\cdot64\cdot25=44800.
\]

## Solution 6

Full expansion is often unnecessary when the question asks for one coefficient. For example, \([t^6](1+3t)^{20}\) can be found directly from the \(r=6\) binomial term:

\[
{}^{20}C_6(1)^{14}(3t)^6.
\]

Generating functions turn expansion into targeted coefficient hunting.

## Solution 7

\[
G_X(t)=\frac15t^0+\frac12t^1+\frac{3}{10}t^3=\frac15+\frac12t+\frac{3}{10}t^3.
\]

Then

\[
G_X(1)=\frac15+\frac12+\frac{3}{10}=\frac{2}{10}+\frac{5}{10}+\frac{3}{10}=1.
\]

## Solution 8

Given

\[
G_Y(t)=\frac{2}{7}+\frac{3}{7}t^2+\frac{2}{7}t^5,
\]

the distribution is

| \(y\) | 0 | 2 | 5 |
|---|---:|---:|---:|
| \(P(Y=y)\) | \(\frac27\) | \(\frac37\) | \(\frac27\) |

## Solution 9

Use \(G_X(1)=1\):

\[
k(1+2)^3=1.
\]

So

\[
27k=1,
\]

\[
k=\frac{1}{27}.
\]

Now

\[
G_X(t)=\frac{1}{27}(1+2t)^3.
\]

The coefficient of \(t^2\) in \((1+2t)^3\) is

\[
{}^3C_2(1)^1(2t)^2=3\cdot4t^2=12t^2.
\]

So

\[
P(X=2)=\frac{12}{27}=\frac49.
\]

## Solution 10

\[
G_Z(t)=\left(\frac13+\frac23t\right)\left(\frac14+\frac12t+\frac14t^2\right).
\]

Multiply:

\[
G_Z(t)=\frac{1}{12}+\frac16t+\frac{1}{12}t^2+\frac16t+\frac13t^2+\frac16t^3.
\]

Collect terms:

\[
G_Z(t)=\frac{1}{12}+\frac13t+\frac{5}{12}t^2+\frac16t^3.
\]

# 15. Exam Technique Notes

## 15.1 CCEA core technique

1. Define the generating function clearly.
2. Identify what coefficient is required.
3. Use \([t^r]G(t)\).
4. Manipulate the expression algebraically.
5. Extract the required coefficient.
6. Interpret the coefficient in the context of the problem.

## 15.2 When using binomial expansion

For

\[
(a+bt)^n,
\]

the general term is

\[
{}^nC_ra^{n-r}(bt)^r.
\]

Since \((bt)^r=b^rt^r\), the coefficient of \(t^r\) is

\[
{}^nC_ra^{n-r}b^r.
\]

## 15.3 When there is a power shift

For

\[
t^mF(t),
\]

to find

\[
[t^r]t^mF(t),
\]

you need

\[
[t^{r-m}]F(t).
\]

## 15.4 PGF enrichment technique

For optional PGF work:

\[
G_X(t)=\sum_xP(X=x)t^x,
\]

\[
G_X(1)=1,
\]

\[
G_X(t)=E(t^X),
\]

\[
E(X)=G'_X(1),
\]

\[
\operatorname{Var}(X)=G''_X(1)+G'_X(1)-[G'_X(1)]^2,
\]

and for independent sums,

\[
G_{X+Y}(t)=G_X(t)G_Y(t).
\]

## 15.5 Boundary technique

In the portal, label PGF content as:

```text
Optional enrichment: Probability generating functions.
```

Do not label PGF statistics formulae as CCEA core unless CCEA evidence confirms them.

# 16. Syllabus Gap Check

## 16.1 LO coverage table

| LO ID | Official topic requirement | Coverage in this lesson | Evidence strength | Status |
|---|---|---|---|---|
| `FA22-GENFUNC-LO001` | demonstrate understanding of the meaning of a generating function | Strong coverage of coefficient encoding and \([t^r]\) extraction | CCEA specification map + conceptually supported by PGF evidence | Covered |
| `FA22-GENFUNC-LO002` | formulate a generating function to solve simple summation problems | Only general foundations included | CCEA-specific examples missing | Partially covered |
| `FA22-GENFUNC-LO003` | use combinatorial arguments and elementary generating functions to prove simple formulae involving, for example, binomial coefficients | Binomial coefficient extraction included, but full CCEA-style proof evidence missing | CCEA-specific examples missing | Partially covered |

## 16.2 Evidence coverage table

| Evidence source | Covered? | Notes |
|---|---:|---|
| CCEA Further Maths specification map | Yes | Used for topic identity and LO boundary. |
| Further Maths README module map | Yes | Used for metadata and output rules. |
| Evidence checklist | Yes | Used for missing/off-spec logging. |
| Ordinary A-Level Maths bridge sources | Yes | Used for bridge section and warnings. |
| PGF PDF definition | Yes | Used in enrichment lane. |
| PGF PDF examples | Yes | Used in enrichment worked examples. |
| Teacher transcript | Yes | Used for warnings about \(t\), powers, coefficients, \(G(1)=1\), independence and coding. |
| Screenshot PDF | Partially | Visuals were inspected through rendered image snippets only; no full text parsing. |

## 16.3 Bridge coverage table

| Bridge area | Covered? | Where |
|---|---:|---|
| Binomial expansion | Yes | Sections 5, 8, 11, 14 |
| Probability tables | Yes | PGF enrichment examples |
| Differentiation | Yes | PGF enrichment theory |
| Series | Yes | Poisson and geometric PGF enrichment |
| Exact fraction arithmetic | Yes | Worked examples and solutions |

## 16.4 Off-Spec Content Found but Excluded

| Content | Excluded from core because |
|---|---|
| Full PGF statistics chapter | Not listed as a CCEA topic in the supplied specification map. |
| Negative binomial PGF | Negative binomial was not confirmed in the supplied CCEA map. |
| PGF variance formula | Useful enrichment, but not confirmed under `FA22-GENFUNC`. |
| PGF linear coding | Useful enrichment, but not confirmed under `FA22-GENFUNC`. |
| Multiplying PGFs for sums of independent variables | Useful enrichment, but not confirmed under `FA22-GENFUNC`. |

## 16.5 Weak evidence warnings

- The core CCEA topic is “Generating functions,” but the uploaded lesson-specific evidence is “Probability Generating Functions.”
- This lesson therefore cannot honestly present PGFs as the main CCEA examinable topic.
- Core CCEA summation examples and combinatorial proof examples are missing.
- Screenshot PDF text was not parsed, so visual details are preserved only where visible in rendered pages.

## 16.6 Missing Evidence Log

| Missing evidence | Why it matters |
|---|---|
| CCEA textbook or teacher examples for simple summation problems | Needed for full `FA22-GENFUNC-LO002` coverage. |
| CCEA examples proving binomial coefficient formulae using generating functions | Needed for full `FA22-GENFUNC-LO003` coverage. |
| CCEA confirmation that PGFs are on-spec | Needed before moving PGF content from enrichment to core. |

# 17. Recommended Enhancements Not in the Evidence

These are AI-proposed enhancements, not evidence-backed content.

## 17.1 Recommended diagrams

1. A clean coefficient filing-cabinet diagram.
2. A target coefficient map for \([t^9]t^3F(t)\).
3. A PGF enrichment diagram showing outcome table to polynomial.
4. A boundary badge separating CCEA core generating functions from optional PGF enrichment.

## 17.2 Recommended animations

1. Animate \(t^3\) shifting a coefficient target.
2. Animate multiplication of two generating functions: powers add, coefficients combine.
3. Animate \(G_X(1)\): all powers become \(1\), so coefficients sum.

## 17.3 Recommended widgets

1. Coefficient extraction checker.
2. Binomial coefficient targeter.
3. PGF table converter.
4. PGF \(G(1)=1\) validator.
5. Independent-sum PGF multiplier, clearly labelled optional.

## 17.4 Recommended extra examples

1. CCEA core summation example using \(1+t+t^2+\cdots+t^n\).
2. CCEA core combinatorial identity example using \((1+t)^n\).
3. CCEA core coefficient proof example involving \({}^nC_r\).

These should only be added after CCEA-specific evidence is supplied.

# 18. Supplementary Sources Used

## Project Sources used

- CCEA GCE Further Mathematics Specification Map.
- Further Maths README module map.
- Further Maths Evidence Drop Checklist.
- CCEA GCE Mathematics Specification Map.
- Ordinary A-Level Maths Bridge Spec Extracts.
- Further Maths Portal Build Knowledge Evidence.

## Lesson-specific evidence used

- `FS1-Chp7-ProbabilityGeneratingFunctions.pdf`.
- `Chapter_7_Probability_Generating_Functions_📊_(Further_Statistics_1)_screenshots.pdf`.
- `transcripts.md`.

## Bridge sources used

Ordinary A-Level Maths bridge material was used only to explain prerequisite ideas: binomial expansion, probability tables, discrete random variables, differentiation and series. It does not override the CCEA Further Mathematics topic boundary.

## Cross-board source notes

The PGF evidence appears to be from Further Statistics 1 / Pearson / DrFrost-style material. It is useful and mathematically coherent, but it is not treated as CCEA core unless the CCEA Further Mathematics specification confirms the same content.

## Evidence limitations

- The screenshot PDF had no parsed text.
- Some screenshot visual details were visible only through rendered image previews.
- CCEA-specific examples for `FA22-GENFUNC-LO002` and `FA22-GENFUNC-LO003` were not supplied.
- PGF content is therefore enrichment, not the confirmed core of this lesson.

# 19. Final Student Checklist

## Prerequisite confidence checklist

You should be able to:

- [ ] expand \((a+bt)^n\) using the binomial theorem;
- [ ] calculate \({}^nC_r\);
- [ ] identify coefficients of powers;
- [ ] work with exact fractions;
- [ ] understand probability tables;
- [ ] differentiate powers of \(t\);
- [ ] recognise simple series expansions if doing PGF enrichment.

## Core Further Maths method checklist

You should be able to:

- [ ] explain what a generating function is;
- [ ] write a sequence as \(G(t)=a_0+a_1t+a_2t^2+\cdots\);
- [ ] use coefficient notation \([t^r]G(t)\);
- [ ] identify missing powers as coefficient \(0\);
- [ ] handle outside shifts such as \(t^mF(t)\);
- [ ] extract coefficients from binomial expressions without expanding everything;
- [ ] explain why coefficients encode the answer.

## Optional PGF enrichment checklist

You should be able to:

- [ ] write \(G_X(t)=\sum_xP(X=x)t^x\);
- [ ] explain that \(t\) is a dummy variable;
- [ ] explain that powers are outcomes;
- [ ] explain that coefficients are probabilities;
- [ ] verify \(G_X(1)=1\);
- [ ] convert a probability table into a PGF;
- [ ] convert a PGF back into a probability distribution;
- [ ] use \(E(X)=G'_X(1)\) where PGF enrichment is being studied;
- [ ] keep PGF results labelled as enrichment until CCEA evidence confirms otherwise.

## Exam technique checklist

You should be able to:

- [ ] state the coefficient you are extracting before doing algebra;
- [ ] avoid expanding unnecessary terms;
- [ ] use exact values unless decimals are requested;
- [ ] write final answers in the original context;
- [ ] flag enrichment content separately from CCEA core;
- [ ] avoid confusing ordinary generating functions with probability generating functions.

## Diagram and visual understanding checklist

You should be able to explain:

- [ ] what each coefficient represents;
- [ ] what each power of \(t\) represents;
- [ ] how a table becomes a polynomial;
- [ ] how a polynomial becomes a table;
- [ ] how coefficient extraction avoids unnecessary expansion;
- [ ] why multiplying generating functions makes powers add.
