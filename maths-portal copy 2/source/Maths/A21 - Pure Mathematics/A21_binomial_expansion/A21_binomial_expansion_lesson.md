# A21 Binomial Expansion Lesson

## Title and Metadata

| Field | Value |
|---|---|
| Course | CCEA GCE Mathematics |
| Unit code | A21 |
| Unit name | A2 1 Pure Mathematics |
| Topic code | A21-SS |
| Official topic area | Sequences and series |
| Lesson topic | Binomial Expansion |
| Topic slug | binomial_expansion |
| Topic Pascal | BinomialExpansion |
| Topic ID | A21BinomialExpansion |
| Lesson file | A21_binomial_expansion_lesson.md |
| Core LO | A21-SS-LO008 |
| Supporting LOs | A21-SS-LO002, A21-SS-LO007, A21-AF-LO008 |
| Prerequisite LOs | AS1-SS-LO001, AS1-SS-LO002 |

---

## Evidence Map

| Evidence | Lesson use |
|---|---|
| CCEA specification map | Unit, topic, LO IDs and syllabus boundary. |
| Project module map | Metadata format and file naming. |
| Project evidence checklist | Evidence hierarchy, missing evidence log and visual placeholder rules. |
| Chapter 4 Binomial Expansion transcript | Main teacher explanation, step-by-step methods, warnings and exam habits. |
| P2 Chapter 4 Binomial Expansion reveal-block PDF | Slide formulae, worked examples, common errors and exercise references. |
| Screenshot PDF | Visual-only reference; no parsed text used as core evidence. |

---

## Specification Alignment

### Core alignment

**A21-SS-LO008:** demonstrate understanding of and use the expansion of  
\[
(a+bx)^n
\]
for any rational \(n\), including its use for approximation and knowledge that the expansion is valid for  
\[
\left|\frac{bx}{a}\right|<1.
\]

This lesson covers:

- expanding \((1+x)^n\) where \(n\) is negative or fractional;
- recognising that these expansions are usually infinite;
- finding the first few terms only;
- rewriting \((a+bx)^n\) into the form \(a^n(1+\frac{b}{a}x)^n\);
- stating the validity condition;
- using a truncated expansion as an approximation;
- checking whether a substitution is valid;
- using partial fractions before applying binomial expansion.

### Supporting alignment

**A21-SS-LO002:** convergence and divergence are used to explain why infinite binomial expansions are valid only for certain values of \(x\).

**A21-SS-LO007:** the condition \(|r|<1\) for convergent geometric series supports the idea that higher powers must get smaller for an infinite expansion to be useful.

**A21-AF-LO008:** partial fractions are used to split rational functions into pieces that can each be expanded.

---

## Learning Objectives

By the end of this lesson, you should be able to:

1. Write the binomial expansion formula for \((1+x)^n\) when \(n\) is rational.
2. Use the coefficient pattern
   \[
   n,\quad \frac{n(n-1)}{2!},\quad \frac{n(n-1)(n-2)}{3!},\quad \ldots
   \]
   without needing Pascal's triangle.
3. Expand expressions such as
   \[
   (1+x)^{-1},\quad (1-3x)^{1/2},\quad (1+4x)^{-2}.
   \]
4. Rewrite expressions such as
   \[
   (4+x)^{1/2}
   \]
   into a form beginning with \(1+\cdots\).
5. State the values of \(x\) for which an expansion is valid.
6. Use truncated binomial expansions for approximation.
7. Use partial fractions before binomial expansion when a rational expression cannot be expanded directly.

---

## Prerequisite Recap: A-Level Knowledge Only

This lesson assumes you already know the AS binomial expansion for positive integer powers.

For example:

\[
(1+x)^5=1+5x+10x^2+10x^3+5x^4+x^5.
\]

Here the coefficients are taken from Pascal's triangle:

\[
1,\quad 5,\quad 10,\quad 10,\quad 5,\quad 1.
\]

Another example:

\[
(1+2x)^4=1+4(2x)+6(2x)^2+4(2x)^3+(2x)^4.
\]

Now simplify each term:

\[
4(2x)=8x,
\]

\[
6(2x)^2=6\cdot 4x^2=24x^2,
\]

\[
4(2x)^3=4\cdot 8x^3=32x^3,
\]

\[
(2x)^4=16x^4.
\]

So:

\[
(1+2x)^4=1+8x+24x^2+32x^3+16x^4.
\]

A third example:

\[
(1-3x)^3=1+3(-3x)+3(-3x)^2+(-3x)^3.
\]

Now simplify:

\[
3(-3x)=-9x,
\]

\[
(-3x)^2=9x^2,
\]

\[
3(-3x)^2=27x^2,
\]

\[
(-3x)^3=-27x^3.
\]

Therefore:

\[
(1-3x)^3=1-9x+27x^2-27x^3.
\]

The important habit is this:

\[
(-3x)^2\neq -3x^2.
\]

You must square the whole bracket:

\[
(-3x)^2=(-3x)(-3x)=9x^2.
\]

---

## Big Picture Explanation

In AS, binomial expansion was finite because \(n\) was a positive integer. For example, \((1+x)^5\) eventually stops at \(x^5\).

In A2, the exponent \(n\) can be any rational number, so it can be negative or fractional:

\[
(1+x)^{-1},\qquad (1+x)^{1/2},\qquad (1+x)^{-3/2}.
\]

These expansions usually do **not** stop. They continue forever:

\[
1+\cdots+\cdots+\cdots+\cdots
\]

That means the question normally asks for the first few terms only, for example first four terms, up to \(x^2\), or up to \(x^3\).

Because the expansion is infinite, it only works when the terms are getting smaller in the right way. This is why validity conditions such as \(|x|<1\) or \(\left|\frac{x}{4}\right|<1\) become part of the answer.

---

## Key Definitions and Notation

### Rational exponent

A rational exponent is an exponent that can be written as a fraction:

\[
n\in\mathbb{Q}.
\]

Examples include:

\[
\frac12,\quad -1,\quad -\frac13,\quad \frac32.
\]

### Factorial notation

\[
3! = 3\cdot 2\cdot 1=6,
\]

\[
4! = 4\cdot 3\cdot 2\cdot 1=24.
\]

### Binomial coefficient pattern

For the binomial expansion, the coefficients can be written as:

\[
\binom{n}{1}=n,
\]

\[
\binom{n}{2}=\frac{n(n-1)}{2!},
\]

\[
\binom{n}{3}=\frac{n(n-1)(n-2)}{3!},
\]

\[
\binom{n}{4}=\frac{n(n-1)(n-2)(n-3)}{4!}.
\]

The pattern is:

- each new numerator factor subtracts one more from \(n\);
- the denominator is the matching factorial;
- the number of numerator factors matches the lower number in the choose notation.

### Important calculator warning

For positive integer \(n\), your calculator may evaluate \(\binom{n}{r}\) directly.

But when the top value is negative or fractional, for example \(\binom{-1}{2}\) or \(\binom{0.5}{2}\), you should calculate using the formula pattern rather than relying on a calculator choose function.

---

## Core Theory

### 1. The A2 binomial expansion formula

For rational \(n\),

\[
(1+x)^n=1+nx+\frac{n(n-1)}{2!}x^2+\frac{n(n-1)(n-2)}{3!}x^3+\cdots.
\]

More generally, if the expression is \((1+u)^n\), then replace every \(x\) in the formula by \(u\):

\[
(1+u)^n=1+nu+\frac{n(n-1)}{2!}u^2+\frac{n(n-1)(n-2)}{3!}u^3+\cdots.
\]

This is one of the most important moves in the chapter.

For example, in \((1-3x)^{1/2}\), the small part is not \(x\). It is \(u=-3x\). So every power must apply to the whole expression \(-3x\): \((-3x)^2\), \((-3x)^3\), and so on.

### 2. Why the expansion is infinite

When \(n\) is a positive integer, eventually one of the numerator factors becomes zero. For example, if \(n=3\), then a later coefficient contains \(n-3=0\). So the expansion stops.

But if \(n=-1\) or \(n=\frac12\), the coefficient pattern does not naturally hit zero. So the expansion continues forever.

This is why you will often see answers with ellipses:

\[
1-x+x^2-x^3+\cdots.
\]

### 3. Validity for \((1+x)^n\)

For an infinite binomial expansion, \((1+x)^n\) is valid when

\[
|x|<1.
\]

This means

\[
-1<x<1.
\]

The endpoints are not included.

### 4. Validity for \((1+u)^n\)

If the expansion is \((1+u)^n\), then the condition is

\[
|u|<1.
\]

For example:

\[
(1-3x)^{1/2}
\]

has \(u=-3x\). So the expansion is valid when

\[
|-3x|<1.
\]

Since \(|-3x|=3|x|\), we get

\[
3|x|<1.
\]

Divide both sides by \(3\):

\[
|x|<\frac13.
\]

Therefore:

\[
-\frac13<x<\frac13.
\]

### 5. Validity for \((a+bx)^n\)

The formula wants the expression to begin with \(1+\cdots\), so rewrite:

\[
(a+bx)^n=\left[a\left(1+\frac{bx}{a}\right)\right]^n.
\]

Now apply the power to both factors:

\[
(a+bx)^n=a^n\left(1+\frac{bx}{a}\right)^n.
\]

The expansion is valid when:

\[
\left|\frac{bx}{a}\right|<1.
\]

This is exactly the CCEA A21 condition for this learning outcome.

---

## Visual Asset Integration

[VISUAL PLACEHOLDER: A21BinomialExpansionSVG-001 | Source: lesson slide recap + transcript | Insert from svg/A21BinomialExpansionSVG-001.svg | Purpose: Show Pascal triangle coefficients and the shift from finite AS expansion to infinite A2 expansion.]

[VISUAL PLACEHOLDER: A21BinomialExpansionSVG-002 | Source: validity explanation in slide PDF and transcript | Insert from svg/A21BinomialExpansionSVG-002.svg | Purpose: Show the number-line interval \(-1<x<1\) and why endpoints are excluded.]

[VISUAL PLACEHOLDER: A21BinomialExpansionSVG-003 | Source: \((a+bx)^n\) slide example | Insert from svg/A21BinomialExpansionSVG-003.svg | Purpose: Show the factorisation route from \((a+bx)^n\) to \(a^n(1+\frac{b}{a}x)^n\).]

[VISUAL PLACEHOLDER: A21BinomialExpansionSVG-004 | Source: partial fractions example | Insert from svg/A21BinomialExpansionSVG-004.svg | Purpose: Show the workflow from rational expression to partial fractions to separate binomial expansions.]

[INTERACTIVE PLACEHOLDER: A21BinomialExpansionWidget-001 | Source: validity and approximation evidence | Insert from widgets/A21BinomialExpansionWidget-001.html | Purpose: Let the student change \(x\), compare exact and approximate values, and see when the approximation stops behaving.]

[INTERACTIVE PLACEHOLDER: A21BinomialExpansionWidget-002 | Source: validity examples | Insert from widgets/A21BinomialExpansionWidget-002.html | Purpose: Let the student practise finding validity conditions for \((a+bx)^n\).]

---

## Worked Examples

### Worked Example 1: Expanding \(\frac{1}{1+x}\)

Find the first four terms of

\[
\frac{1}{1+x}.
\]

First rewrite using an index:

\[
\frac{1}{1+x}=(1+x)^{-1}.
\]

Here \(n=-1\). Use

\[
(1+x)^n=1+nx+\frac{n(n-1)}{2!}x^2+\frac{n(n-1)(n-2)}{3!}x^3+\cdots.
\]

Substitute \(n=-1\):

\[
(1+x)^{-1}=1+(-1)x+\frac{(-1)(-1-1)}{2!}x^2+\frac{(-1)(-1-1)(-1-2)}{3!}x^3+\cdots.
\]

Simplify the brackets:

\[
-1-1=-2,
\]

\[
-1-2=-3.
\]

So:

\[
(1+x)^{-1}=1-x+\frac{(-1)(-2)}{2!}x^2+\frac{(-1)(-2)(-3)}{3!}x^3+\cdots.
\]

For \(x^2\):

\[
\frac{(-1)(-2)}{2!}=\frac{2}{2}=1.
\]

For \(x^3\):

\[
\frac{(-1)(-2)(-3)}{3!}=\frac{-6}{6}=-1.
\]

Therefore:

\[
\frac{1}{1+x}=1-x+x^2-x^3+\cdots.
\]

The first four terms are:

\[
\boxed{1-x+x^2-x^3}.
\]

Validity:

\[
|x|<1,
\]

so

\[
\boxed{-1<x<1}.
\]

---

### Worked Example 2: Expanding \(\sqrt{1-3x}\)

Find the first four terms of

\[
\sqrt{1-3x}=(1-3x)^{1/2}.
\]

Here

\[
n=\frac12,\qquad u=-3x.
\]

Use

\[
(1+u)^n=1+nu+\frac{n(n-1)}{2!}u^2+\frac{n(n-1)(n-2)}{3!}u^3+\cdots.
\]

Substitute:

\[
(1-3x)^{1/2}=1+\frac12(-3x)+\frac{\frac12(\frac12-1)}{2!}(-3x)^2+\frac{\frac12(\frac12-1)(\frac12-2)}{3!}(-3x)^3+\cdots.
\]

Simplify:

\[
\frac12-1=-\frac12,\qquad \frac12-2=-\frac32.
\]

So:

\[
(1-3x)^{1/2}=1+\frac12(-3x)+\frac{\frac12(-\frac12)}{2!}(-3x)^2+\frac{\frac12(-\frac12)(-\frac32)}{3!}(-3x)^3+\cdots.
\]

First-order term:

\[
\frac12(-3x)=-\frac32x.
\]

Second-order coefficient:

\[
\frac{\frac12(-\frac12)}{2!}=\frac{-\frac14}{2}=-\frac18.
\]

Since

\[
(-3x)^2=9x^2,
\]

the second-order term is

\[
-\frac18\cdot 9x^2=-\frac98x^2.
\]

Third-order coefficient:

\[
\frac{\frac12(-\frac12)(-\frac32)}{3!}=\frac{\frac38}{6}=\frac{1}{16}.
\]

Since

\[
(-3x)^3=-27x^3,
\]

the third-order term is

\[
\frac{1}{16}(-27x^3)=-\frac{27}{16}x^3.
\]

Therefore:

\[
\sqrt{1-3x}=1-\frac32x-\frac98x^2-\frac{27}{16}x^3+\cdots.
\]

The first four terms are:

\[
\boxed{1-\frac32x-\frac98x^2-\frac{27}{16}x^3}.
\]

Validity:

\[
|-3x|<1\quad\Rightarrow\quad |x|<\frac13.
\]

---

### Worked Example 3: Expanding \((1+4x)^{-2}\)

Find the binomial expansion of

\[
\frac{1}{(1+4x)^2}
\]

up to and including the term in \(x^3\). State the values of \(x\) for which the expansion is valid.

Rewrite:

\[
\frac{1}{(1+4x)^2}=(1+4x)^{-2}.
\]

Here:

\[
n=-2,\qquad u=4x.
\]

Substitute into the formula:

\[
(1+4x)^{-2}=1+(-2)(4x)+\frac{(-2)(-3)}{2!}(4x)^2+\frac{(-2)(-3)(-4)}{3!}(4x)^3+\cdots.
\]

Simplify each term:

\[
(-2)(4x)=-8x,
\]

\[
\frac{(-2)(-3)}{2!}=\frac{6}{2}=3,
\]

\[
(4x)^2=16x^2,
\]

so

\[
3(16x^2)=48x^2.
\]

Next:

\[
\frac{(-2)(-3)(-4)}{3!}=\frac{-24}{6}=-4,
\]

\[
(4x)^3=64x^3,
\]

so

\[
-4(64x^3)=-256x^3.
\]

Therefore:

\[
(1+4x)^{-2}=1-8x+48x^2-256x^3+\cdots.
\]

Validity:

\[
|4x|<1\quad\Rightarrow\quad \boxed{|x|<\frac14}.
\]

---

### Worked Example 4: Dealing with \((a+bx)^n\)

Find the first four terms in the binomial expansion of

\[
\sqrt{4+x}.
\]

State the values of \(x\) for which the expansion is valid.

We want the expression in the form \((1+u)^n\). At the moment:

\[
\sqrt{4+x}=(4+x)^{1/2}.
\]

The constant term is not \(1\), so factor out \(4\):

\[
4+x=4\left(1+\frac{x}{4}\right).
\]

Therefore:

\[
(4+x)^{1/2}=\left[4\left(1+\frac{x}{4}\right)\right]^{1/2}.
\]

Apply the power to each factor:

\[
(4+x)^{1/2}=4^{1/2}\left(1+\frac{x}{4}\right)^{1/2}.
\]

Since \(4^{1/2}=2\),

\[
(4+x)^{1/2}=2\left(1+\frac{x}{4}\right)^{1/2}.
\]

Now expand the bracket with \(n=\frac12\) and \(u=\frac{x}{4}\):

\[
\left(1+\frac{x}{4}\right)^{1/2}=1+\frac12\left(\frac{x}{4}\right)+\frac{\frac12(-\frac12)}{2!}\left(\frac{x}{4}\right)^2+\frac{\frac12(-\frac12)(-\frac32)}{3!}\left(\frac{x}{4}\right)^3+\cdots.
\]

First-order term:

\[
\frac12\left(\frac{x}{4}\right)=\frac{x}{8}.
\]

Second-order term:

\[
\frac{\frac12(-\frac12)}{2!}\left(\frac{x}{4}\right)^2=-\frac18\cdot\frac{x^2}{16}=-\frac{x^2}{128}.
\]

Third-order term:

\[
\frac{\frac12(-\frac12)(-\frac32)}{3!}\left(\frac{x}{4}\right)^3=\frac{1}{16}\cdot\frac{x^3}{64}=\frac{x^3}{1024}.
\]

Thus:

\[
\left(1+\frac{x}{4}\right)^{1/2}=1+\frac{x}{8}-\frac{x^2}{128}+\frac{x^3}{1024}+\cdots.
\]

Multiply everything by \(2\):

\[
(4+x)^{1/2}=2+\frac{x}{4}-\frac{x^2}{64}+\frac{x^3}{512}+\cdots.
\]

The first four terms are:

\[
\boxed{2+\frac14x-\frac{1}{64}x^2+\frac{1}{512}x^3}.
\]

Validity:

\[
\left|\frac{x}{4}\right|<1\quad\Rightarrow\quad \boxed{|x|<4}.
\]

---

### Worked Example 5: Quickfire First Step for Non-1 Constants

The first algebraic move is the whole game here. Before expanding, pull out the constant so that the bracket begins with \(1\).

#### Example 5A

\[
(2+x)^{-3}=\left[2\left(1+\frac{x}{2}\right)\right]^{-3}=2^{-3}\left(1+\frac{x}{2}\right)^{-3}=\frac18\left(1+\frac{x}{2}\right)^{-3}.
\]

Validity:

\[
\left|\frac{x}{2}\right|<1\quad\Rightarrow\quad |x|<2.
\]

#### Example 5B

\[
(9+2x)^{1/2}=\left[9\left(1+\frac{2x}{9}\right)\right]^{1/2}=3\left(1+\frac{2x}{9}\right)^{1/2}.
\]

Validity:

\[
\left|\frac{2x}{9}\right|<1\quad\Rightarrow\quad |x|<\frac92.
\]

#### Example 5C

\[
(8-x)^{1/3}=\left[8\left(1-\frac{x}{8}\right)\right]^{1/3}=2\left(1-\frac{x}{8}\right)^{1/3}.
\]

Validity:

\[
\left|-\frac{x}{8}\right|<1\quad\Rightarrow\quad |x|<8.
\]

#### Example 5D

\[
(5-2x)^{-3}=\left[5\left(1-\frac{2x}{5}\right)\right]^{-3}=\frac{1}{125}\left(1-\frac{2x}{5}\right)^{-3}.
\]

Validity:

\[
\left|-\frac{2x}{5}\right|<1\quad\Rightarrow\quad |x|<\frac52.
\]

#### Example 5E

\[
(16+3x)^{-1/2}=16^{-1/2}\left(1+\frac{3x}{16}\right)^{-1/2}=\frac14\left(1+\frac{3x}{16}\right)^{-1/2}.
\]

Validity:

\[
\left|\frac{3x}{16}\right|<1\quad\Rightarrow\quad |x|<\frac{16}{3}.
\]

---

### Worked Example 6: Finding a Missing Coefficient

Use the binomial expansion to show that

\[
(4+5x)^{1/2}\approx 2+\frac54x+kx^2.
\]

Find \(k\).

Factor out \(4\):

\[
(4+5x)^{1/2}=\left[4\left(1+\frac{5x}{4}\right)\right]^{1/2}=2\left(1+\frac54x\right)^{1/2}.
\]

Expand the bracket up to \(x^2\):

\[
\left(1+\frac54x\right)^{1/2}=1+\frac12\left(\frac54x\right)+\frac{\frac12(-\frac12)}{2}\left(\frac54x\right)^2+\cdots.
\]

First-order term:

\[
\frac12\left(\frac54x\right)=\frac58x.
\]

Second-order term:

\[
\frac{\frac12(-\frac12)}{2}\left(\frac54x\right)^2=-\frac18\cdot\frac{25}{16}x^2=-\frac{25}{128}x^2.
\]

So:

\[
\left(1+\frac54x\right)^{1/2}=1+\frac58x-\frac{25}{128}x^2+\cdots.
\]

Multiply by \(2\):

\[
(4+5x)^{1/2}=2+\frac54x-\frac{25}{64}x^2+\cdots.
\]

Compare with \(2+\frac54x+kx^2\). Therefore:

\[
\boxed{k=-\frac{25}{64}}.
\]

---

### Worked Example 7: Using an Expansion to Approximate \(\sqrt2\)

Use

\[
(4+5x)^{1/2}\approx 2+\frac54x-\frac{25}{64}x^2
\]

with \(x=\frac{1}{10}\) to find an approximate value for \(\sqrt2\) in the form \(\frac{p}{q}\). Explain why the approximation is valid.

Left-hand side:

\[
(4+5\cdot\frac{1}{10})^{1/2}=\left(4+\frac12\right)^{1/2}=\left(\frac92\right)^{1/2}=\sqrt{\frac92}=\frac{3}{\sqrt2}=\frac{3\sqrt2}{2}.
\]

Right-hand side:

\[
2+\frac54\left(\frac{1}{10}\right)-\frac{25}{64}\left(\frac{1}{10}\right)^2.
\]

Simplify:

\[
\frac54\cdot\frac{1}{10}=\frac18,
\]

\[
\frac{25}{64}\left(\frac{1}{10}\right)^2=\frac{25}{6400}=\frac{1}{256}.
\]

So:

\[
2+\frac18-\frac{1}{256}=\frac{512}{256}+\frac{32}{256}-\frac{1}{256}=\frac{543}{256}.
\]

Thus:

\[
\frac{3\sqrt2}{2}\approx\frac{543}{256}.
\]

Multiply both sides by \(2\):

\[
3\sqrt2\approx\frac{1086}{256}.
\]

Divide by \(3\):

\[
\sqrt2\approx\frac{1086}{768}=\frac{181}{128}.
\]

Therefore:

\[
\boxed{\sqrt2\approx \frac{181}{128}}.
\]

Validity:

\[
\left|\frac54x\right|<1\quad\Rightarrow\quad |x|<\frac45.
\]

Since \(\frac{1}{10}<\frac45\), the approximation is valid.

---

### Worked Example 8: Comparing Coefficients with a Constant \(k\)

The expansion of

\[
(2+kx)^{-4}
\]

begins

\[
\frac{1}{16}+ax+\frac{125}{32}x^2+\cdots,
\]

where \(k\) is a positive constant. Find \(a\). Determine, with a reason, whether the expansion is valid when \(x=\frac{1}{10}\).

Factor out \(2\):

\[
(2+kx)^{-4}=\left[2\left(1+\frac{kx}{2}\right)\right]^{-4}=\frac{1}{16}\left(1+\frac{kx}{2}\right)^{-4}.
\]

Expand:

\[
\left(1+\frac{kx}{2}\right)^{-4}=1+(-4)\left(\frac{kx}{2}\right)+\frac{(-4)(-5)}{2!}\left(\frac{kx}{2}\right)^2+\cdots.
\]

Simplify:

\[
(-4)\left(\frac{kx}{2}\right)=-2kx,
\]

\[
\frac{(-4)(-5)}{2!}=10,
\]

\[
10\left(\frac{kx}{2}\right)^2=10\cdot \frac{k^2x^2}{4}=\frac52k^2x^2.
\]

Therefore:

\[
(2+kx)^{-4}=\frac{1}{16}\left(1-2kx+\frac52k^2x^2+\cdots\right)
=\frac{1}{16}-\frac{k}{8}x+\frac{5k^2}{32}x^2+\cdots.
\]

Compare coefficients of \(x^2\):

\[
\frac{5k^2}{32}=\frac{125}{32}.
\]

Multiply by \(32\):

\[
5k^2=125.
\]

Divide by \(5\):

\[
k^2=25.
\]

Since \(k\) is positive:

\[
k=5.
\]

Then:

\[
a=-\frac{k}{8}=-\frac58.
\]

Validity:

\[
\left|\frac{kx}{2}\right|<1.
\]

With \(k=5\):

\[
\left|\frac{5x}{2}\right|<1\quad\Rightarrow\quad |x|<\frac25.
\]

Since \(\frac{1}{10}<\frac25\), it is valid when \(x=\frac{1}{10}\).

---

### Worked Example 9: Combining Expansions

Use binomial expansion to show that:

\[
\left(\frac{1+x}{1-x}\right)^{1/2}\approx 1+x+\frac12x^2.
\]

First express the expression as a product:

\[
\left(\frac{1+x}{1-x}\right)^{1/2}=\frac{(1+x)^{1/2}}{(1-x)^{1/2}}=(1+x)^{1/2}(1-x)^{-1/2}.
\]

We only need terms up to \(x^2\).

First:

\[
(1+x)^{1/2}=1+\frac12x+\frac{\frac12(-\frac12)}{2!}x^2+\cdots=1+\frac12x-\frac18x^2+\cdots.
\]

Second:

\[
(1-x)^{-1/2}=1+\left(-\frac12\right)(-x)+\frac{\left(-\frac12\right)\left(-\frac32\right)}{2!}(-x)^2+\cdots.
\]

Simplify:

\[
(1-x)^{-1/2}=1+\frac12x+\frac38x^2+\cdots.
\]

Now multiply:

\[
(1+\frac12x-\frac18x^2)(1+\frac12x+\frac38x^2).
\]

Keep terms up to \(x^2\):

\[
1+\frac12x+\frac38x^2+\frac12x+\frac14x^2-\frac18x^2.
\]

Combine:

\[
\frac12x+\frac12x=x,
\]

\[
\frac38+\frac14-\frac18=\frac38+\frac28-\frac18=\frac48=\frac12.
\]

Therefore:

\[
\boxed{\left(\frac{1+x}{1-x}\right)^{1/2}\approx 1+x+\frac12x^2}.
\]

Validity for both factors gives \(|x|<1\).

---

### Worked Example 10: Combining Expansions and Checking an Invalid Substitution

Show that:

\[
\left(\frac{1+4x}{1-x}\right)^{1/2}\approx 1+\frac52x-\frac58x^2.
\]

Then explain why a student should not substitute \(x=\frac12\) to approximate \(\sqrt6\).

Rewrite:

\[
\left(\frac{1+4x}{1-x}\right)^{1/2}=(1+4x)^{1/2}(1-x)^{-1/2}.
\]

Expand:

\[
(1+4x)^{1/2}=1+\frac12(4x)+\frac{\frac12(-\frac12)}{2!}(4x)^2+\cdots=1+2x-2x^2+\cdots.
\]

Also:

\[
(1-x)^{-1/2}=1+\frac12x+\frac38x^2+\cdots.
\]

Multiply:

\[
(1+2x-2x^2)(1+\frac12x+\frac38x^2).
\]

Keep terms up to \(x^2\):

\[
1+\frac12x+\frac38x^2+2x+x^2-2x^2.
\]

Combine:

\[
\frac12x+2x=\frac52x,
\]

\[
\frac38+x^2-2x^2=\frac38+\frac88-\frac{16}{8}=-\frac58.
\]

Therefore:

\[
\boxed{\left(\frac{1+4x}{1-x}\right)^{1/2}\approx 1+\frac52x-\frac58x^2}.
\]

Validity:

For \((1+4x)^{1/2}\):

\[
|4x|<1\quad\Rightarrow\quad |x|<\frac14.
\]

For \((1-x)^{-1/2}\):

\[
|-x|<1\quad\Rightarrow\quad |x|<1.
\]

Both must be true, so the stricter condition is:

\[
|x|<\frac14.
\]

But \(\frac12>\frac14\), so \(x=\frac12\) is invalid.

---

### Worked Example 11: Valid Approximation to \(\sqrt6\)

Use

\[
\left(\frac{1+4x}{1-x}\right)^{1/2}\approx 1+\frac52x-\frac58x^2
\]

with \(x=\frac{1}{11}\) to approximate \(\sqrt6\).

Left-hand side:

\[
1+4x=1+\frac{4}{11}=\frac{15}{11},
\]

\[
1-x=1-\frac{1}{11}=\frac{10}{11}.
\]

So:

\[
\frac{1+4x}{1-x}=\frac{\frac{15}{11}}{\frac{10}{11}}=\frac{15}{11}\cdot\frac{11}{10}=\frac{15}{10}=\frac32.
\]

Thus:

\[
\left(\frac{1+4x}{1-x}\right)^{1/2}=\sqrt{\frac32}=\frac{\sqrt3}{\sqrt2}=\frac{\sqrt6}{2}.
\]

Right-hand side:

\[
1+\frac52\left(\frac{1}{11}\right)-\frac58\left(\frac{1}{11}\right)^2=1+\frac{5}{22}-\frac{5}{968}.
\]

Write over \(968\):

\[
1=\frac{968}{968},\qquad \frac{5}{22}=\frac{220}{968}.
\]

Therefore:

\[
1+\frac{5}{22}-\frac{5}{968}=\frac{968}{968}+\frac{220}{968}-\frac{5}{968}=\frac{1183}{968}.
\]

So:

\[
\frac{\sqrt6}{2}\approx\frac{1183}{968}.
\]

Multiply by \(2\):

\[
\sqrt6\approx\frac{2366}{968}=\frac{1183}{484}.
\]

Therefore:

\[
\boxed{\sqrt6\approx \frac{1183}{484}}.
\]

---

### Worked Example 12: Partial Fractions Before Binomial Expansion

Show that the cubic approximation of

\[
\frac{4-5x}{(1+x)(2-x)}
\]

is:

\[
2-\frac72x+\frac{11}{4}x^2-\frac{25}{8}x^3.
\]

First express the fraction using partial fractions:

\[
\frac{4-5x}{(1+x)(2-x)}=\frac{A}{1+x}+\frac{B}{2-x}.
\]

Multiply both sides by \((1+x)(2-x)\):

\[
4-5x=A(2-x)+B(1+x).
\]

Let \(x=2\):

\[
4-10=0+3B,
\]

so

\[
-6=3B\quad\Rightarrow\quad B=-2.
\]

Let \(x=-1\):

\[
4-5(-1)=A(3)+B(0),
\]

so

\[
9=3A\quad\Rightarrow\quad A=3.
\]

Therefore:

\[
\frac{4-5x}{(1+x)(2-x)}=\frac{3}{1+x}-\frac{2}{2-x}.
\]

Now expand each part.

First:

\[
\frac{3}{1+x}=3(1+x)^{-1}=3(1-x+x^2-x^3+\cdots).
\]

So:

\[
\frac{3}{1+x}=3-3x+3x^2-3x^3+\cdots.
\]

Next:

\[
\frac{2}{2-x}=2(2-x)^{-1}.
\]

Factor \(2\):

\[
2-x=2\left(1-\frac{x}{2}\right).
\]

So:

\[
2(2-x)^{-1}=2\cdot 2^{-1}\left(1-\frac{x}{2}\right)^{-1}=\left(1-\frac{x}{2}\right)^{-1}.
\]

Expand:

\[
\left(1-\frac{x}{2}\right)^{-1}=1+\frac{x}{2}+\frac{x^2}{4}+\frac{x^3}{8}+\cdots.
\]

Now subtract:

\[
\frac{4-5x}{(1+x)(2-x)}\approx (3-3x+3x^2-3x^3)-\left(1+\frac{x}{2}+\frac{x^2}{4}+\frac{x^3}{8}\right).
\]

Constants:

\[
3-1=2.
\]

Coefficient of \(x\):

\[
-3x-\frac{x}{2}=-\frac72x.
\]

Coefficient of \(x^2\):

\[
3x^2-\frac14x^2=\frac{11}{4}x^2.
\]

Coefficient of \(x^3\):

\[
-3x^3-\frac18x^3=-\frac{25}{8}x^3.
\]

Therefore:

\[
\boxed{\frac{4-5x}{(1+x)(2-x)}\approx 2-\frac72x+\frac{11}{4}x^2-\frac{25}{8}x^3}.
\]

Validity:

For \(3(1+x)^{-1}\), require \(|x|<1\).

For \(\left(1-\frac{x}{2}\right)^{-1}\), require \(\left|\frac{x}{2}\right|<1\), so \(|x|<2\).

Both must hold, so the stricter condition is:

\[
\boxed{|x|<1}.
\]

---

### Worked Example 13: Partial Fractions with a Polynomial Term

Expand:

\[
\frac{2x^2+5x-10}{(x-1)(x+2)}
\]

as far as the term in \(x^2\), using partial fractions.

First write:

\[
\frac{2x^2+5x-10}{(x-1)(x+2)}=A+\frac{B}{x-1}+\frac{C}{x+2}.
\]

Multiply through by \((x-1)(x+2)\):

\[
2x^2+5x-10=A(x-1)(x+2)+B(x+2)+C(x-1).
\]

Expand:

\[
(x-1)(x+2)=x^2+x-2.
\]

So:

\[
2x^2+5x-10=A(x^2+x-2)+B(x+2)+C(x-1).
\]

Expand the right-hand side:

\[
A(x^2+x-2)=Ax^2+Ax-2A,
\]

\[
B(x+2)=Bx+2B,
\]

\[
C(x-1)=Cx-C.
\]

Therefore:

\[
2x^2+5x-10=Ax^2+(A+B+C)x+(-2A+2B-C).
\]

Compare coefficients:

\[
A=2,
\]

\[
A+B+C=5\quad\Rightarrow\quad 2+B+C=5\quad\Rightarrow\quad B+C=3,
\]

\[
-2A+2B-C=-10\quad\Rightarrow\quad -4+2B-C=-10\quad\Rightarrow\quad 2B-C=-6.
\]

Solve:

\[
B+C=3,
\]

\[
2B-C=-6.
\]

Add the equations:

\[
3B=-3\quad\Rightarrow\quad B=-1.
\]

Then:

\[
-1+C=3\quad\Rightarrow\quad C=4.
\]

Thus:

\[
\frac{2x^2+5x-10}{(x-1)(x+2)}=2-\frac{1}{x-1}+\frac{4}{x+2}.
\]

Rewrite each part:

\[
-\frac{1}{x-1}=\frac{1}{1-x}=(1-x)^{-1}.
\]

Also:

\[
\frac{4}{x+2}=4(x+2)^{-1}=4\left[2\left(1+\frac{x}{2}\right)\right]^{-1}=2\left(1+\frac{x}{2}\right)^{-1}.
\]

Expand:

\[
(1-x)^{-1}=1+x+x^2+\cdots,
\]

\[
2\left(1+\frac{x}{2}\right)^{-1}=2\left(1-\frac{x}{2}+\frac{x^2}{4}+\cdots\right)=2-x+\frac{x^2}{2}+\cdots.
\]

Combine all parts:

\[
2+(1+x+x^2)+\left(2-x+\frac{x^2}{2}\right).
\]

Constants:

\[
2+1+2=5.
\]

\(x\)-terms:

\[
x-x=0.
\]

\(x^2\)-terms:

\[
x^2+\frac12x^2=\frac32x^2.
\]

Therefore:

\[
\boxed{\frac{2x^2+5x-10}{(x-1)(x+2)}\approx 5+\frac32x^2}.
\]

Validity:

\[
(1-x)^{-1}: |x|<1,
\]

\[
\left(1+\frac{x}{2}\right)^{-1}: |x|<2.
\]

So the stricter condition is:

\[
\boxed{|x|<1}.
\]

---

## Guided Practice

### Practice Question 1

Expand

\[
(1-2x)^{-1}
\]

up to and including the term in \(x^3\). State the values of \(x\) for which the expansion is valid.

### Practice Question 2

Find the first three terms in the expansion of:

\[
(9+2x)^{1/2}.
\]

State the values of \(x\) for which the expansion is valid.

### Practice Question 3

Find the first three terms in the expansion of:

\[
(16+3x)^{-1/2}.
\]

State the values of \(x\) for which the expansion is valid.

### Practice Question 4

Use binomial expansion to show that:

\[
\left(\frac{1+x}{1-x}\right)^{1/2}\approx 1+x+\frac12x^2.
\]

### Practice Question 5

Expand:

\[
\frac{2x^2+5x-10}{(x-1)(x+2)}
\]

as far as the term in \(x^2\).

---

## Common Mistakes and Exam Traps

### Trap 1: Forgetting to make the bracket begin with \(1\)

The formula is for \((1+x)^n\). So before expanding \((4+x)^{1/2}\), you must rewrite it as

\[
2\left(1+\frac{x}{4}\right)^{1/2}.
\]

### Trap 2: Forgetting the outside multiplier

For \((4+x)^{1/2}=2(1+\frac{x}{4})^{1/2}\), the expansion inside the bracket must be multiplied by \(2\).

### Trap 3: Squaring only part of the bracket

For \((1-3x)^{1/2}\), the formula gives terms involving \((-3x)^2\) and \((-3x)^3\). You must use

\[
(-3x)^2=9x^2,
\]

not \(-3x^2\).

### Trap 4: Sign errors with negative brackets

\[
(-3x)^2=9x^2,
\]

but

\[
(-3x)^3=-27x^3.
\]

Even powers of a negative expression become positive. Odd powers remain negative.

### Trap 5: Dividing by \(3\) instead of \(3!\)

The third-order coefficient uses \(3!\), not \(3\). Since \(3!=6\), the coefficient is divided by \(6\).

### Trap 6: Losing the validity condition

A finished binomial expansion question often needs the expansion and the range of \(x\) for which it is valid.

### Trap 7: Using a substitution outside the valid range

If the expansion requires \(|x|<\frac14\), then \(x=\frac12\) is not allowed.

### Trap 8: In combined expansions, using the looser validity condition

For \((1+4x)^{1/2}(1-x)^{-1/2}\), the two conditions are \(|x|<\frac14\) and \(|x|<1\). Both must be true, so use the stricter one:

\[
|x|<\frac14.
\]

---

## Exam Technique Notes

### 1. First line habit

Always begin by identifying the form. For example:

\[
(8+5x)^{-1/3}=8^{-1/3}\left(1+\frac{5x}{8}\right)^{-1/3}=\frac12\left(1+\frac{5x}{8}\right)^{-1/3}.
\]

### 2. Write down \(n\) and \(u\)

For every expansion, write

\[
n=\cdots,\qquad u=\cdots.
\]

For \((1-3x)^{1/2}\), write

\[
n=\frac12,
\qquad
u=-3x.
\]

### 3. Know how many terms you need

If the question says “up to and including the term in \(x^3\)”, you need constant, \(x\), \(x^2\), and \(x^3\) terms.

### 4. In product expansions, ignore terms too high only after checking their powers

\[
x\cdot x=x^2
\]

must be kept if working to \(x^2\), but

\[
x\cdot x^2=x^3
\]

can be ignored.

### 5. For approximation questions, substitute into both sides

If the left-hand side becomes \(\frac{3\sqrt2}{2}\), you still need to rearrange to isolate \(\sqrt2\).

### 6. More accurate approximations come from smaller \(|x|\)

For binomial approximations, smaller values of \(|x|\) usually give better approximations because higher powers such as \(x^3,x^4,x^5\) become very small.

---

## Full Worked Solutions to Guided Practice

### Solution to Practice Question 1

Here \(n=-1\) and \(u=-2x\):

\[
(1-2x)^{-1}=1+(-1)(-2x)+\frac{(-1)(-2)}{2!}(-2x)^2+\frac{(-1)(-2)(-3)}{3!}(-2x)^3+\cdots.
\]

First-order term:

\[
(-1)(-2x)=2x.
\]

Second-order term:

\[
\frac{(-1)(-2)}{2!}(-2x)^2=1\cdot 4x^2=4x^2.
\]

Third-order term:

\[
\frac{(-1)(-2)(-3)}{3!}(-2x)^3=-1\cdot (-8x^3)=8x^3.
\]

Therefore:

\[
\boxed{(1-2x)^{-1}\approx 1+2x+4x^2+8x^3}.
\]

Validity:

\[
|-2x|<1\quad\Rightarrow\quad \boxed{|x|<\frac12}.
\]

### Solution to Practice Question 2

\[
(9+2x)^{1/2}=3\left(1+\frac{2x}{9}\right)^{1/2}.
\]

Expand:

\[
\left(1+\frac{2x}{9}\right)^{1/2}=1+\frac12\left(\frac{2x}{9}\right)+\frac{\frac12(-\frac12)}{2!}\left(\frac{2x}{9}\right)^2+\cdots.
\]

So:

\[
=1+\frac{x}{9}-\frac18\cdot\frac{4x^2}{81}+\cdots=1+\frac{x}{9}-\frac{x^2}{162}+\cdots.
\]

Multiply by \(3\):

\[
\boxed{(9+2x)^{1/2}\approx 3+\frac13x-\frac{1}{54}x^2}.
\]

Validity:

\[
\left|\frac{2x}{9}\right|<1\quad\Rightarrow\quad \boxed{|x|<\frac92}.
\]

### Solution to Practice Question 3

\[
(16+3x)^{-1/2}=\frac14\left(1+\frac{3x}{16}\right)^{-1/2}.
\]

Expand:

\[
\left(1+\frac{3x}{16}\right)^{-1/2}=1-\frac12\left(\frac{3x}{16}\right)+\frac{(-\frac12)(-\frac32)}{2!}\left(\frac{3x}{16}\right)^2+\cdots.
\]

So:

\[
=1-\frac{3x}{32}+\frac38\cdot\frac{9x^2}{256}+\cdots=1-\frac{3}{32}x+\frac{27}{2048}x^2+\cdots.
\]

Multiply by \(\frac14\):

\[
\boxed{(16+3x)^{-1/2}\approx \frac14-\frac{3}{128}x+\frac{27}{8192}x^2}.
\]

Validity:

\[
\left|\frac{3x}{16}\right|<1\quad\Rightarrow\quad \boxed{|x|<\frac{16}{3}}.
\]

### Solution to Practice Question 4

\[
\left(\frac{1+x}{1-x}\right)^{1/2}=(1+x)^{1/2}(1-x)^{-1/2}.
\]

Now:

\[
(1+x)^{1/2}=1+\frac12x-\frac18x^2+\cdots,
\]

and

\[
(1-x)^{-1/2}=1+\frac12x+\frac38x^2+\cdots.
\]

Multiply:

\[
\left(1+\frac12x-\frac18x^2\right)\left(1+\frac12x+\frac38x^2\right).
\]

Keep terms up to \(x^2\):

\[
1+\frac12x+\frac38x^2+\frac12x+\frac14x^2-\frac18x^2.
\]

Combine:

\[
\boxed{\left(\frac{1+x}{1-x}\right)^{1/2}\approx 1+x+\frac12x^2}.
\]

### Solution to Practice Question 5

As shown in Worked Example 13:

\[
\frac{2x^2+5x-10}{(x-1)(x+2)}=2-\frac{1}{x-1}+\frac{4}{x+2}.
\]

Rewrite:

\[
-\frac{1}{x-1}=(1-x)^{-1},
\]

\[
\frac{4}{x+2}=2\left(1+\frac{x}{2}\right)^{-1}.
\]

Then:

\[
2+(1+x+x^2)+\left(2-x+\frac{x^2}{2}\right)=5+\frac32x^2.
\]

Therefore:

\[
\boxed{\frac{2x^2+5x-10}{(x-1)(x+2)}\approx 5+\frac32x^2}.
\]

---

## Common CCEA-Style Wording

### “Expand in ascending powers of \(x\)”

This means write terms in the order

\[
1,\quad x,\quad x^2,\quad x^3,\quad \ldots
\]

### “Up to and including the term in \(x^3\)”

Include all terms through \(x^3\): constant, \(x\), \(x^2\), and \(x^3\).

### “Show that”

You must show enough algebra to prove the given expression. A final answer alone is not enough.

### “Hence”

“Hence” means use what you have just found.

### “State the range of values”

Give the final interval clearly, for example \(|x|<1\) or \(-1<x<1\).

---

## Syllabus Gap Check

| Requirement | Status | Notes |
|---|---:|---|
| A21-SS-LO008: expansion of \((a+bx)^n\) for rational \(n\) | Covered | Includes fractional and negative powers. |
| Validity condition \(\left|\frac{bx}{a}\right|<1\) | Covered | Used repeatedly in constant-not-1 examples. |
| Approximation using truncated expansion | Covered | \(\sqrt2\) and \(\sqrt6\) examples included. |
| Infinite expansion and convergence warning | Covered | Uses validity logic and endpoint exclusion. |
| Combining binomial expansions | Covered | Product examples included. |
| Partial fractions before binomial expansion | Covered as supporting A21-AF content | Included because evidence uses it and CCEA includes partial fractions in A21 Algebra and Functions. |
| CCEA-specific past-paper questions | Missing | No CCEA paper extract supplied, so none invented. |
| Textbook exercise full questions | Missing | Only evidence-visible textbook references and examples used. |
| STEP/AEA extension material | Excluded from core | Logged as optional enrichment only. |

---

## Visual and Interactive Asset Plan

| Asset ID | Type | Phase | Purpose |
|---|---|---:|---|
| A21BinomialExpansionMermaid-001 | Mermaid | Phase 2 | AS finite expansion to A2 infinite rational expansion. |
| A21BinomialExpansionMermaid-002 | Mermaid | Phase 2 | Coefficient pattern. |
| A21BinomialExpansionMermaid-003 | Mermaid | Phase 2 | Validity decision flow. |
| A21BinomialExpansionMermaid-004 | Mermaid | Phase 2 | Constant-not-1 workflow. |
| A21BinomialExpansionMermaid-005 | Mermaid | Phase 2 | Combining expansions. |
| A21BinomialExpansionMermaid-006 | Mermaid | Phase 2 | Partial fractions workflow. |
| A21BinomialExpansionMermaid-007 | Mermaid | Phase 2 | Approximation workflow. |
| A21BinomialExpansionSVG-001 to 007 | SVG | Phase 3 | Printable/portal visual assets. |
| A21BinomialExpansionTikZ-001 to 006 | TikZ | Phase 4 | LaTeX printable diagrams. |
| A21BinomialExpansionWidget-001 | HTML widget | Phase 5 | Compare exact and approximate values. |
| A21BinomialExpansionWidget-002 | HTML widget | Phase 5 | Practise validity conditions. |

---

## Supplementary Sources Used

| Source | Status |
|---|---|
| CCEA GCE Mathematics specification map | Core authority for LO IDs and syllabus boundary. |
| Chapter 4 transcript | Core lesson evidence for methods, worked examples and warnings. |
| Reveal-block PDF | Core slide evidence for formulae, examples, common errors and exercise references. |
| Screenshot PDF | Visual-only support; not used for unverified text. |
| Edexcel C4 examples in evidence | Cross-board support only where the method matches CCEA A21 binomial expansion. |
| AEA 2006 and STEP I 2011 examples | Optional enrichment only, excluded from core requirement. |

---

## Final Student Checklist

### Formula and setup

- [ ] I can write the binomial expansion formula for \((1+x)^n\).
- [ ] I know that rational \(n\) includes negative and fractional powers.
- [ ] I know that negative or fractional powers usually give infinite expansions.
- [ ] I can identify \(n\) and \(u\) in \((1+u)^n\).

### Expanding brackets

- [ ] I can expand \((1-3x)^{1/2}\) without sign errors.
- [ ] I remember to square or cube the whole bracket, such as \((-3x)^2\).
- [ ] I divide by \(2!\), \(3!\), \(4!\), not just by \(2\), \(3\), \(4\).
- [ ] I stop at the requested power of \(x\).

### Constant not 1

- [ ] I can rewrite \((4+x)^{1/2}\) as \(2(1+\frac{x}{4})^{1/2}\).
- [ ] I can rewrite \((8+5x)^{-1/3}\) by pulling out \(8\).
- [ ] I remember to apply the power to the factor pulled out.
- [ ] I multiply the final expansion by the outside constant.

### Validity

- [ ] I know that \((1+x)^n\) is valid for \(|x|<1\).
- [ ] I know that \((1+u)^n\) is valid for \(|u|<1\).
- [ ] I can find validity for \((a+bx)^n\) using \(\left|\frac{bx}{a}\right|<1\).
- [ ] I use the stricter condition when combining expansions.
- [ ] I do not use invalid substitutions in approximation questions.

### Approximation

- [ ] I can substitute into both sides of an approximation.
- [ ] I can rearrange to isolate a required surd such as \(\sqrt2\) or \(\sqrt6\).
- [ ] I understand why smaller \(|x|\) values give better approximations.
- [ ] I can explain why an approximation is valid.

### Partial fractions

- [ ] I can decompose a rational function before expanding.
- [ ] I can expand each partial fraction separately.
- [ ] I can combine constants, \(x\)-terms, \(x^2\)-terms and \(x^3\)-terms carefully.
- [ ] I can find the overall validity range from all partial-fraction expansions.

---

## Final Quality Check Summary

| Check | Result |
|---|---|
| Unit prefix and topic identity are correct | Passed: A21, A2 1 Pure Mathematics, A21-SS, Binomial Expansion. |
| LO IDs are preserved exactly | Passed: A21-SS-LO008, A21-SS-LO002, A21-SS-LO007, A21-AF-LO008, AS1-SS-LO001, AS1-SS-LO002. |
| On-spec evidence is covered | Passed. |
| Off-spec material is excluded or marked | Passed. |
| Placeholders match actual files | Passed. |
| Manifest and source reference are updated | Passed. |
| Unresolved issues | No CCEA past-paper extract or full textbook extract supplied. |
