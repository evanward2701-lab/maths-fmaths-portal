# AS1 Algebraic Methods: Proof

## Title and Metadata

| Field | Value |
|---|---|
| Course | CCEA GCE Mathematics |
| Unit code | AS1 |
| Unit name | AS 1 Pure Mathematics |
| Topic code | AS1-AF, with overarching Proof and Reasoning |
| Topic name | Algebraic Methods: Proof |
| Topic slug | `algebraic_methods_proof` |
| Topic Pascal | `AlgebraicMethodsProof` |
| Topic ID | `AS1AlgebraicMethodsProof` |
| Lesson file | `AS1_algebraic_methods_proof_lesson.md` |
| Supporting LO IDs | AS1-AF-LO002, AS1-AF-LO005, AS1-AF-LO006, AS1-AF-LO010, AS1-SS-LO001 |
| Core proof methods | Proof by deduction, proof by exhaustion, disproof by counterexample |
| Excluded from AS1 core | Proof by contradiction |

## Evidence Map

| Evidence | Lesson use |
|---|---|
| CCEA GCE Mathematics Specification Map | Unit identity, AS1 Pure placement, supporting LO IDs and proof/reasoning theme. |
| Project README/module map | Metadata, phase order and file naming. |
| Project Evidence Drop Checklist | Missing evidence, off-spec log and visual placeholder rules. |
| Teacher transcript: Chapter 7b Algebraic Methods, Proof | Core lesson content, worked examples, warnings and exam technique. |
| Screenshot PDF: Chapter 7b Algebraic Methods, Proof | Visual evidence for proof-type cards and proof-by-deduction board sequence. |

## Specification Alignment

| Lesson content | CCEA alignment |
|---|---|
| General proof structure: assumptions, algebra, conclusion | Overarching proof and reasoning theme |
| Writing `2k`, `2k+1`, `2k-1`, `3k`, `3k±1` | AS1 algebraic manipulation |
| Expanding and collecting expressions | AS1-AF-LO010 |
| Completing the square to prove positivity | AS1-AF-LO005 |
| Solving the quadratic from the right-triangle proof | AS1-AF-LO006 |
| Surd counterexample `sqrt(12) * sqrt(3) = sqrt(36) = 6` | AS1-AF-LO002 |
| Cubic expansion in exhaustion examples | AS1-SS-LO001 |

## Learning Objectives

By the end of this lesson, you should be able to:

1. recognise proof by deduction, proof by exhaustion and disproof by counterexample;
2. choose algebraic forms for even, odd and consecutive integers;
3. prove statements about parity, divisibility and multiples;
4. split integers into exhaustive cases, such as even/odd or `3k`, `3k+1`, `3k-1`;
5. disprove a universal statement using one valid counterexample;
6. write a final conclusion sentence that answers the exact statement;
7. avoid the trap of assuming the result you are trying to prove.

## Prerequisite Recap

No GCSE source is used here. These are simply prior mathematical skills needed to follow the A-Level evidence.

| Skill | Needed for |
|---|---|
| Expanding brackets | Every algebraic proof |
| Factorising | Showing multiples and solving equations |
| Difference of two squares | `n^3-n=n(n-1)(n+1)` |
| Completing the square | Positivity proofs |
| Surd manipulation | Irrational-number counterexamples |
| Pythagoras' theorem | Consecutive integer right-triangle proof |
| Binomial expansion for small powers | Cubing `3n+1`, `3n-1`, `2n+1` |

## Big Picture Explanation

Proof is where mathematics stops being a calculator trail and starts becoming a courtroom drama. The answer is not just “true”; you must show why it is forced to be true.

The evidence for this lesson separates the Year 1 proof toolkit into three core moves:

- **proof by deduction**: start from known facts and move logically to the conclusion;
- **proof by exhaustion**: split the problem into every possible case and prove each case;
- **disproof by counterexample**: find one legal example that breaks the statement.

The transcript also mentions **proof by contradiction**, but treats it as an A2 topic. It is therefore not part of the AS1 core lesson.

## Key Definitions and Notation

### Proof by deduction

A proof by deduction starts from facts you are allowed to use and reaches the required conclusion through valid algebraic or logical steps.

You must not begin by assuming the conclusion.

### Proof by exhaustion

A proof by exhaustion breaks the statement into all possible smaller cases and proves each case. This is also called **case analysis**.

Common exhaustive splits:

\[
n \text{ is even} \quad \text{or} \quad n \text{ is odd}.
\]

Another useful split is:

\[
n=3k,\qquad n=3k+1,\qquad n=3k-1.
\]

These cover every integer because every integer is either a multiple of `3`, one more than a multiple of `3`, or one less than a multiple of `3`.

### Disproof by counterexample

To prove a universal statement true, you may need to prove every possible case.

To disprove a universal statement, one counterexample is enough.

A counterexample must satisfy the conditions of the statement but make the conclusion false.

### Integer notation

\[
n\in\mathbb Z
\]

means `n` is an integer.

Integers include:

\[
\ldots,-3,-2,-1,0,1,2,3,\ldots
\]

### Natural number notation

\[
n\in\mathbb N
\]

means `n` is a natural number. In the transcript, natural numbers are described as positive integers, with a note that some mathematicians include `0` and some do not. Read the question carefully.

### Even numbers

An even integer can be written as:

\[
2k,\qquad k\in\mathbb Z.
\]

### Odd numbers

An odd integer can be written as:

\[
2k+1,\qquad k\in\mathbb Z,
\]

or

\[
2k-1,\qquad k\in\mathbb Z.
\]

### Consecutive integers

Consecutive integers are next to each other:

\[
n,\quad n+1.
\]

Three consecutive integers may be written as:

\[
x,\quad x+1,\quad x+2,
\]

or

\[
x-1,\quad x,\quad x+1.
\]

### Consecutive odd integers

Two consecutive odd integers may be written as:

\[
2n-1,\quad 2n+1,
\]

or

\[
2n+1,\quad 2n+3.
\]

The first version is often neater because the middle terms cancel.

### Factor

If `a` is a factor of `b`, then:

\[
b=na,\qquad n\in\mathbb Z.
\]

### Rational number

A rational number can be written as:

\[
\frac ab,
\]

where `a,b` are integers, `b != 0`, and the fraction is in lowest terms.

Examples:

\[
\frac12,\quad \frac13,\quad 17=\frac{17}{1},\quad -12=\frac{-12}{1},\quad 0.\overline4=\frac49.
\]

### Irrational number

An irrational number cannot be written as a fraction of two integers.

Examples from the evidence include:

\[
\pi,\quad e,\quad \sqrt2,\quad 3+\pi,\quad \frac{1+\sqrt2}{3}.
\]

## Core Theory

### 1. How to write a deduction proof

A deduction proof usually follows this structure:

1. Define a general object.
2. State any restrictions, such as `n in Z`.
3. Perform algebra from the starting expression.
4. Rewrite the result in the required form.
5. Write a final sentence.

Example target forms:

| What you want to prove | Algebraic target form |
|---|---|
| Even | `2(integer)` |
| Odd | `2(integer)+1` |
| Multiple of `8` | `8(integer)` |
| Two more than a multiple of `8` | `8(integer)+2` |
| Positive | `>0` |
| Non-negative | `>=0` |

### 2. The trivial inequality

For any real expression `A`,

\[
A^2\geq0.
\]

This is why completing the square is such a useful proof tool. For example:

\[
x^2+4x+5=(x+2)^2+1.
\]

Since

\[
(x+2)^2\geq0,
\]

then

\[
(x+2)^2+1\geq1,
\]

so

\[
x^2+4x+5\geq1>0.
\]

### 3. How to write a proof by exhaustion

A proof by exhaustion needs all possible cases. If you split into even and odd integers, you must prove both:

\[
n=2k
\]

and

\[
n=2k+1.
\]

Then you need a conclusion:

\[
\text{Therefore the statement is true for all integers }n.
\]

The sneaky part: exhaustion does not always mean even and odd. For questions involving multiples of `3`, it is often better to use:

\[
n=3k,\qquad n=3k+1,\qquad n=3k-1.
\]

### 4. How to disprove a statement

Suppose a statement says:

\[
\text{For all integers }n,\quad P(n)\text{ is true}.
\]

To disprove it, find one `n` such that `P(n)` is false.

You do not need to test every value. You need one legal value that breaks the rule.

## Visual Asset Integration

[VISUAL PLACEHOLDER: AS1AlgebraicMethodsProofSVG-001 | Source: CCEA proof/reasoning theme + transcript overview | Insert from svg/AS1AlgebraicMethodsProofSVG-001.svg | Purpose: Show the decision tree for deduction, exhaustion and counterexample.]

[VISUAL PLACEHOLDER: AS1AlgebraicMethodsProofSVG-002 | Source: Teacher transcript notation section | Insert from svg/AS1AlgebraicMethodsProofSVG-002.svg | Purpose: Show algebraic forms for even, odd, consecutive and modulo-3 integer cases.]

[VISUAL PLACEHOLDER: AS1AlgebraicMethodsProofSVG-003 | Source: Transcript right-triangle proof | Insert from svg/AS1AlgebraicMethodsProofSVG-003.svg | Purpose: Show a right-angled triangle with side lengths `x`, `x+1`, `x+2`.]

[VISUAL PLACEHOLDER: AS1AlgebraicMethodsProofSVG-004 | Source: Screenshot PDF pages 1-3 | Insert from svg/AS1AlgebraicMethodsProofSVG-004.svg | Purpose: Recreate the four proof-type cards while grey-labeling proof by contradiction as A2/future context.]

[INTERACTIVE PLACEHOLDER: AS1AlgebraicMethodsProofWidget-001 | Source: Teacher transcript proof method decisions | Insert from widgets/AS1AlgebraicMethodsProofWidget-001.html | Purpose: Let the student choose a statement type and receive a suggested proof method.]

## Worked Examples

### Worked Example 1: Prove that the product of two odd numbers is odd

Let the two odd numbers be:

\[
2m+1
\]

and

\[
2n+1,
\]

where

\[
m,n\in\mathbb Z.
\]

Their product is:

\[
(2m+1)(2n+1).
\]

Expand:

\[
(2m+1)(2n+1)=2m(2n+1)+1(2n+1).
\]

\[
=4mn+2m+2n+1.
\]

Now factor `2` from the first three terms:

\[
4mn+2m+2n+1=2(2mn+m+n)+1.
\]

Since

\[
2mn+m+n\in\mathbb Z,
\]

so the product has the form:

\[
2(\text{integer})+1.
\]

Therefore the product of two odd numbers is odd.

### Worked Example 2: Prove that the difference between the squares of two consecutive integers is equal to their sum

Let the consecutive integers be:

\[
n
\]

and

\[
n+1,
\]

where

\[
n\in\mathbb Z.
\]

The difference between their squares is:

\[
(n+1)^2-n^2.
\]

Expand:

\[
(n+1)^2-n^2=(n^2+2n+1)-n^2.
\]

Cancel `n^2`:

\[
n^2+2n+1-n^2=2n+1.
\]

The sum of the two integers is:

\[
n+(n+1)=2n+1.
\]

Therefore:

\[
(n+1)^2-n^2=n+(n+1).
\]

### Worked Example 3: Prove that `x^2+4x+5` is positive for all values of `x`

Complete the square:

\[
x^2+4x+5=(x+2)^2-4+5.
\]

\[
=(x+2)^2+1.
\]

For every real `x`,

\[
(x+2)^2\geq0.
\]

Therefore:

\[
(x+2)^2+1\geq1.
\]

So:

\[
x^2+4x+5\geq1.
\]

Since

\[
1>0,
\]

we have:

\[
x^2+4x+5>0.
\]

Therefore `x^2+4x+5` is positive for all real values of `x`.

### Worked Example 4: Sum of squares of consecutive odd numbers

Let the consecutive odd numbers be:

\[
2n-1
\]

and

\[
2n+1,
\]

where

\[
n\in\mathbb Z.
\]

The sum of their squares is:

\[
(2n-1)^2+(2n+1)^2.
\]

Expand:

\[
(2n-1)^2=4n^2-4n+1.
\]

\[
(2n+1)^2=4n^2+4n+1.
\]

Add:

\[
(2n-1)^2+(2n+1)^2=(4n^2-4n+1)+(4n^2+4n+1).
\]

\[
=8n^2+2.
\]

This has the form:

\[
8(\text{integer})+2.
\]

Therefore the sum of the squares of two consecutive odd numbers is two more than a multiple of eight.

### Worked Example 5: Consecutive integer sides of a right-angled triangle

Prove that if three consecutive integers are the sides of a right-angled triangle, they must be `3,4,5`.

Do not begin by checking:

\[
3^2+4^2=5^2.
\]

That verifies the answer after the fact, but it does not prove these are the only possible side lengths.

Let the three consecutive integer side lengths be:

\[
x,\quad x+1,\quad x+2.
\]

The longest side is:

\[
x+2,
\]

so this must be the hypotenuse.

Using Pythagoras' theorem:

\[
x^2+(x+1)^2=(x+2)^2.
\]

Expand:

\[
x^2+(x^2+2x+1)=x^2+4x+4.
\]

Collect the left-hand side:

\[
2x^2+2x+1=x^2+4x+4.
\]

Subtract `x^2+4x+4` from both sides:

\[
2x^2+2x+1-(x^2+4x+4)=0.
\]

\[
2x^2+2x+1-x^2-4x-4=0.
\]

\[
x^2-2x-3=0.
\]

Factorise:

\[
x^2-2x-3=(x-3)(x+1).
\]

So:

\[
(x-3)(x+1)=0.
\]

Therefore:

\[
x=3
\]

or

\[
x=-1.
\]

Since `x` is a side length, it cannot be negative. Therefore:

\[
x=3.
\]

The side lengths are:

\[
x=3,\qquad x+1=4,\qquad x+2=5.
\]

Therefore the three consecutive integer side lengths must be:

\[
3,\quad4,\quad5.
\]

### Worked Example 6: Prove that `n^2+n` is even for all integers `n`

We use proof by exhaustion. Every integer is either even or odd.

#### Case 1: `n` is even

Let:

\[
n=2k,
\]

where

\[
k\in\mathbb Z.
\]

Then:

\[
n^2+n=(2k)^2+2k.
\]

\[
=4k^2+2k.
\]

Factor out `2`:

\[
4k^2+2k=2(2k^2+k).
\]

Since

\[
2k^2+k\in\mathbb Z,
\]

`n^2+n` is even when `n` is even.

#### Case 2: `n` is odd

Let:

\[
n=2k+1,
\]

where

\[
k\in\mathbb Z.
\]

Then:

\[
n^2+n=(2k+1)^2+(2k+1).
\]

Expand:

\[
(2k+1)^2=4k^2+4k+1.
\]

So:

\[
n^2+n=4k^2+4k+1+2k+1.
\]

Collect like terms:

\[
=4k^2+6k+2.
\]

Factor out `2`:

\[
4k^2+6k+2=2(2k^2+3k+1).
\]

Since

\[
2k^2+3k+1\in\mathbb Z,
\]

`n^2+n` is even when `n` is odd.

Since every integer is either even or odd, and the statement is true in both cases,

\[
n^2+n
\]

is even for all integers `n`.

### Worked Example 7: Prove that `n^2+2` is not divisible by `4`

We prove this by exhaustion using even and odd cases.

#### Case 1: `n` is even

Let:

\[
n=2k,
\]

where

\[
k\in\mathbb Z.
\]

Then:

\[
n^2+2=(2k)^2+2=4k^2+2.
\]

This is:

\[
4(k^2)+2.
\]

So it is two more than a multiple of `4`. Therefore it is not divisible by `4`.

#### Case 2: `n` is odd

Let:

\[
n=2k+1,
\]

where

\[
k\in\mathbb Z.
\]

Then:

\[
n^2+2=(2k+1)^2+2.
\]

Expand:

\[
(2k+1)^2=4k^2+4k+1.
\]

So:

\[
n^2+2=4k^2+4k+1+2=4k^2+4k+3.
\]

Factor `4` from the first two terms:

\[
4k^2+4k+3=4(k^2+k)+3.
\]

So it is three more than a multiple of `4`. Therefore it is not divisible by `4`.

Since every integer is either even or odd, `n^2+2` is not divisible by `4`.

### Worked Example 8: Harder proof by exhaustion with cube numbers

Prove that all cube numbers are either:

\[
\text{a multiple of }9,
\]

or

\[
\text{one more than a multiple of }9,
\]

or

\[
\text{one less than a multiple of }9.
\]

This is proof by exhaustion. Even and odd cases are not helpful, because cubing `2n` gives:

\[
(2n)^3=8n^3,
\]

which tells us about multiples of `8`, not multiples of `9`.

Instead, split all integers into:

\[
3n,\quad 3n+1,\quad 3n-1.
\]

#### Case 1: multiples of `3`

Let the integer be:

\[
3n,
\]

where

\[
n\in\mathbb Z.
\]

Cube it:

\[
(3n)^3=27n^3.
\]

Rewrite `27` as `9*3`:

\[
27n^3=9(3n^3).
\]

So this is a multiple of `9`.

#### Case 2: one more than a multiple of `3`

Let the integer be:

\[
3n+1.
\]

Cube it:

\[
(3n+1)^3.
\]

Using the binomial expansion:

\[
(a+b)^3=a^3+3a^2b+3ab^2+b^3.
\]

Here:

\[
a=3n,\qquad b=1.
\]

So:

\[
(3n+1)^3=(3n)^3+3(3n)^2(1)+3(3n)(1)^2+1^3.
\]

\[
=27n^3+3(9n^2)+9n+1.
\]

\[
=27n^3+27n^2+9n+1.
\]

Factor `9` from the first three terms:

\[
=9(3n^3+3n^2+n)+1.
\]

This is one more than a multiple of `9`.

#### Case 3: one less than a multiple of `3`

Let the integer be:

\[
3n-1.
\]

Cube it:

\[
(3n-1)^3.
\]

Using:

\[
(a-b)^3=a^3-3a^2b+3ab^2-b^3,
\]

with

\[
a=3n,\qquad b=1,
\]

we get:

\[
(3n-1)^3=(3n)^3-3(3n)^2(1)+3(3n)(1)^2-1^3.
\]

\[
=27n^3-27n^2+9n-1.
\]

Factor `9` from the first three terms:

\[
=9(3n^3-3n^2+n)-1.
\]

This is one less than a multiple of `9`.

Since all integers are covered by the three cases `3n`, `3n+1`, and `3n-1`, all cube numbers are either a multiple of `9`, one more than a multiple of `9`, or one less than a multiple of `9`.

### Worked Example 9: Disprove `n^2-n+41` is prime for all integers

To disprove it, one counterexample is enough.

Try:

\[
n=41.
\]

Then:

\[
n^2-n+41=41^2-41+41.
\]

The `-41` and `+41` cancel:

\[
41^2-41+41=41^2.
\]

But:

\[
41^2=41\cdot41.
\]

So `41^2` has `41` as a factor and is not prime.

Therefore the statement is false.

### Worked Example 10: Disprove “for every prime `p`, `2p+1` is prime”

We need a prime `p` such that:

\[
2p+1
\]

is not prime.

Try:

\[
p=7.
\]

Since `7` is prime, this is a legal test value.

Now calculate:

\[
2p+1=2(7)+1=14+1=15.
\]

But:

\[
15=3\cdot5,
\]

so `15` is not prime.

Therefore the statement is false.

### Worked Example 11: Disprove an irrational-number statement

Statement: If `m` and `n` are irrational numbers and `m != n`, then `mn` is also irrational. Disprove this statement.

Choose:

\[
m=\sqrt{12}
\]

and

\[
n=\sqrt3.
\]

Both are irrational and:

\[
\sqrt{12}\neq\sqrt3.
\]

Now multiply:

\[
mn=\sqrt{12}\cdot\sqrt3=\sqrt{12\cdot3}=\sqrt{36}=6.
\]

Since:

\[
6=\frac61,
\]

`6` is rational.

Therefore the statement is false.

### Worked Example 12: Always, sometimes or never true

Question: If I add `3` to a number and square the sum, the result is greater than the square of the original number. State whether this is always true, sometimes true or never true, giving a reason.

Let the original number be:

\[
x.
\]

Adding `3` and squaring gives:

\[
(x+3)^2.
\]

The square of the original number is:

\[
x^2.
\]

We investigate:

\[
(x+3)^2>x^2.
\]

Expand:

\[
x^2+6x+9>x^2.
\]

Subtract `x^2` from both sides:

\[
6x+9>0.
\]

Subtract `9`:

\[
6x>-9.
\]

Divide by `6`:

\[
x>-\frac96.
\]

Simplify:

\[
x>-\frac32.
\]

So the statement is true when:

\[
x>-\frac32.
\]

It is false when:

\[
x\leq-\frac32.
\]

For example, if:

\[
x=3,
\]

then:

\[
(x+3)^2=(3+3)^2=6^2=36
\]

and:

\[
x^2=3^2=9.
\]

Since:

\[
36>9,
\]

it is true for `x=3`.

If:

\[
x=-3,
\]

then:

\[
(x+3)^2=(-3+3)^2=0^2=0
\]

and:

\[
x^2=(-3)^2=9.
\]

Since `0>9` is false, the statement is false for `x=-3`.

Therefore the statement is sometimes true.

### Worked Example 13: Prove `sqrt(xy) <= (x+y)/2` for positive `x` and `y`

This is the corrected inequality supported by the evidence's factorisation.

Start with:

\[
\sqrt{xy}\leq\frac{x+y}{2}.
\]

Multiply both sides by `2`. Since `2>0`, the inequality direction stays the same:

\[
2\sqrt{xy}\leq x+y.
\]

Rearrange:

\[
0\leq x-2\sqrt{xy}+y.
\]

Now:

\[
x=(\sqrt{x})^2
\]

and

\[
y=(\sqrt{y})^2.
\]

So:

\[
x-2\sqrt{xy}+y=(\sqrt{x})^2-2\sqrt{x}\sqrt{y}+(\sqrt{y})^2.
\]

Factorise:

\[
(\sqrt{x})^2-2\sqrt{x}\sqrt{y}+(\sqrt{y})^2=(\sqrt{x}-\sqrt{y})^2.
\]

Since anything squared is non-negative:

\[
(\sqrt{x}-\sqrt{y})^2\geq0.
\]

So:

\[
x-2\sqrt{xy}+y\geq0.
\]

Hence:

\[
x+y\geq2\sqrt{xy}.
\]

Divide by `2`:

\[
\frac{x+y}{2}\geq\sqrt{xy}.
\]

Therefore:

\[
\sqrt{xy}\leq\frac{x+y}{2}.
\]

### Worked Example 14: Counterexample when `x` and `y` are both negative

Let:

\[
x=-2
\]

and

\[
y=-2.
\]

Then:

\[
xy=(-2)(-2)=4.
\]

So:

\[
\sqrt{xy}=\sqrt4=2.
\]

Now:

\[
\frac{x+y}{2}=\frac{-2+(-2)}{2}=\frac{-4}{2}=-2.
\]

The claimed inequality would say:

\[
2\leq -2,
\]

which is false.

Therefore `x=-2`, `y=-2` is a counterexample.

### Worked Example 15: Use a calculator table to find a counterexample

Show that the statement is false:

\[
n^2-n-1 \text{ is prime for }3\leq n\leq10.
\]

When:

\[
n=8,
\]

we get:

\[
n^2-n-1=8^2-8-1=64-8-1=56-1=55.
\]

But:

\[
55=5\cdot11,
\]

so `55` is not prime.

Therefore the statement is false.

### Worked Example 16: Difference between the cube and square of an odd number

Let the odd number be:

\[
2n+1,
\]

where:

\[
n\in\mathbb Z.
\]

The difference between the cube and the square is:

\[
(2n+1)^3-(2n+1)^2.
\]

First expand the cube:

\[
(2n+1)^3=(2n)^3+3(2n)^2(1)+3(2n)(1)^2+1^3.
\]

\[
=8n^3+3(4n^2)+6n+1.
\]

\[
=8n^3+12n^2+6n+1.
\]

Now expand the square:

\[
(2n+1)^2=4n^2+4n+1.
\]

Subtract:

\[
(2n+1)^3-(2n+1)^2=(8n^3+12n^2+6n+1)-(4n^2+4n+1).
\]

Remove the brackets carefully:

\[
=8n^3+12n^2+6n+1-4n^2-4n-1.
\]

Collect like terms:

\[
=8n^3+8n^2+2n.
\]

Factor out `2`:

\[
8n^3+8n^2+2n=2(4n^3+4n^2+n).
\]

Since:

\[
4n^3+4n^2+n\in\mathbb Z,
\]

the expression is even.

### Worked Example 17: Difference between squares of consecutive odd integers is a multiple of `8`

Let the consecutive odd integers be:

\[
2k+1
\]

and

\[
2k+3,
\]

where:

\[
k\in\mathbb Z.
\]

The larger square minus the smaller square is:

\[
(2k+3)^2-(2k+1)^2.
\]

Expand:

\[
(2k+3)^2=4k^2+12k+9.
\]

\[
(2k+1)^2=4k^2+4k+1.
\]

Subtract:

\[
(2k+3)^2-(2k+1)^2=(4k^2+12k+9)-(4k^2+4k+1).
\]

Remove brackets:

\[
=4k^2+12k+9-4k^2-4k-1.
\]

Collect like terms:

\[
=(4k^2-4k^2)+(12k-4k)+(9-1)=8k+8.
\]

Factor out `8`:

\[
8k+8=8(k+1).
\]

Since:

\[
k+1\in\mathbb Z,
\]

the expression is a multiple of `8`.

### Worked Example 18: Prove that `n^3-n` is divisible by `6`

Start by factorising:

\[
n^3-n=n(n^2-1).
\]

Use difference of two squares:

\[
n^2-1=(n-1)(n+1).
\]

So:

\[
n^3-n=n(n-1)(n+1).
\]

Rewrite in order:

\[
n^3-n=(n-1)n(n+1).
\]

These are three consecutive integers.

In any three consecutive integers:

- at least one is divisible by `2`;
- exactly one is divisible by `3`.

Therefore the product is divisible by both `2` and `3`.

Since:

\[
6=2\cdot3,
\]

`n^3-n` is divisible by `6`.

### Worked Example 19: Prove `n(n^2+1)` is even for all natural numbers

We use proof by exhaustion.

#### Case 1: `n` is even

Let:

\[
n=2k,
\]

where:

\[
k\in\mathbb Z.
\]

Then:

\[
n(n^2+1)=2k((2k)^2+1)=2k(4k^2+1).
\]

Expand:

\[
=8k^3+2k.
\]

Factor out `2`:

\[
8k^3+2k=2(4k^3+k).
\]

So `n(n^2+1)` is even when `n` is even.

#### Case 2: `n` is odd

Let:

\[
n=2k+1,
\]

where:

\[
k\in\mathbb Z.
\]

Then:

\[
n(n^2+1)=(2k+1)((2k+1)^2+1).
\]

Expand inside the bracket:

\[
(2k+1)^2=4k^2+4k+1.
\]

So:

\[
(2k+1)^2+1=4k^2+4k+1+1=4k^2+4k+2.
\]

Factor out `2`:

\[
4k^2+4k+2=2(2k^2+2k+1).
\]

Therefore:

\[
n(n^2+1)=(2k+1)\cdot2(2k^2+2k+1).
\]

Reorder:

\[
=2(2k+1)(2k^2+2k+1).
\]

This has the form:

\[
2(\text{integer}).
\]

So `n(n^2+1)` is even when `n` is odd.

Since every natural number is either even or odd, `n(n^2+1)` is even for all natural numbers.

### Worked Example 20: Square numbers and multiples of `3`

Prove that all square numbers are either a multiple of `3` or one more than a multiple of `3`.

We use proof by exhaustion with:

\[
n=3k,\qquad n=3k+1,\qquad n=3k+2.
\]

#### Case 1: `n=3k`

\[
n^2=(3k)^2=9k^2=3(3k^2).
\]

So `n^2` is a multiple of `3`.

#### Case 2: `n=3k+1`

\[
n^2=(3k+1)^2=9k^2+6k+1.
\]

Factor `3` from the first two terms:

\[
9k^2+6k+1=3(3k^2+2k)+1.
\]

So `n^2` is one more than a multiple of `3`.

#### Case 3: `n=3k+2`

\[
n^2=(3k+2)^2=9k^2+12k+4.
\]

Rewrite `4` as `3+1`:

\[
9k^2+12k+4=9k^2+12k+3+1.
\]

Factor `3` from the first three terms:

\[
=3(3k^2+4k+1)+1.
\]

So `n^2` is one more than a multiple of `3`.

Since all integers are covered by `3k`, `3k+1`, and `3k+2`, every square number is either a multiple of `3` or one more than a multiple of `3`.

## Guided Practice

### Practice Question 1

Prove that the sum of two even integers is even.

### Practice Question 2

Prove that the product of an even integer and an odd integer is even.

### Practice Question 3

Prove that the square of an odd integer is odd.

### Practice Question 4

Prove that:

\[
n^2-n
\]

is even for all integers `n`.

### Practice Question 5

Disprove the statement:

\[
\text{For every prime }p,\quad p+2\text{ is prime}.
\]

### Practice Question 6

State whether the following is always true, sometimes true or never true:

\[
x^2+1>x.
\]

Give a reason.

## Common Mistakes and Exam Traps

| Mistake | Why it costs marks | Safer habit |
|---|---|---|
| Starting with the conclusion | You assume what you are meant to prove | Start from definitions or the left-hand expression |
| Forgetting “where `k in Z`” | Your general form is less formal | State the integer condition early |
| Using the same letter for two different arbitrary odd numbers | You accidentally prove a special case | Use `2m+1` and `2n+1` for any two odd numbers |
| Splitting into even and odd when the question is about multiples of `3` or `9` | You may get irrelevant algebra | Match the cases to the number structure |
| Giving many examples to prove an “always” statement | Examples do not prove infinitely many cases | Use algebra or exhaustion |
| Giving a counterexample that violates the condition | It does not disprove the statement | Check the example satisfies the hypothesis |
| Omitting the final sentence | The proof may not explicitly answer the question | End with “Therefore...” or “Hence...” |
| Writing “sometimes true” with only one example | Sometimes true needs both true and false evidence | Give one true case and one false case, or solve algebraically |

## Exam Technique Notes

1. For “prove” questions, use general algebra. Examples alone are not enough.
2. For “disprove” questions, one counterexample is enough.
3. For “always, sometimes, never” questions, look for:
   - always true: proof for all values;
   - never true: proof that no value works;
   - sometimes true: one true case and one false case, or an algebraic range.
4. For divisibility, aim for the form:
   \[
   a(\text{integer}).
   \]
5. For positivity, try completing the square.
6. For exhaustion, ask: “Have I covered every possible case?”
7. For counterexamples over a finite range, a calculator table can help search, but the written proof still needs a clear counterexample.

## Full Worked Solutions to Guided Practice

### Solution 1

Let the two even integers be:

\[
2m
\]

and

\[
2n,
\]

where:

\[
m,n\in\mathbb Z.
\]

Their sum is:

\[
2m+2n.
\]

Factor out `2`:

\[
2m+2n=2(m+n).
\]

Since:

\[
m+n\in\mathbb Z,
\]

the sum is even.

### Solution 2

Let the even integer be:

\[
2m
\]

and the odd integer be:

\[
2n+1,
\]

where:

\[
m,n\in\mathbb Z.
\]

Their product is:

\[
2m(2n+1).
\]

\[
=2(m(2n+1)).
\]

Since:

\[
m(2n+1)\in\mathbb Z,
\]

the product is even.

### Solution 3

Let the odd integer be:

\[
2n+1,
\]

where:

\[
n\in\mathbb Z.
\]

Its square is:

\[
(2n+1)^2.
\]

Expand:

\[
(2n+1)^2=4n^2+4n+1.
\]

Factor `2` from the first two terms:

\[
4n^2+4n+1=2(2n^2+2n)+1.
\]

Since:

\[
2n^2+2n\in\mathbb Z,
\]

the square has the form:

\[
2(\text{integer})+1.
\]

Therefore the square of an odd integer is odd.

### Solution 4

\[
n^2-n=n(n-1).
\]

The integers `n-1` and `n` are consecutive. One of two consecutive integers is even.

Therefore:

\[
n(n-1)
\]

is even.

So:

\[
n^2-n
\]

is even for all integers `n`.

### Solution 5

Choose:

\[
p=2.
\]

Since `2` is prime, this is a legal value.

Then:

\[
p+2=2+2=4.
\]

But:

\[
4=2\cdot2,
\]

so `4` is not prime.

Therefore the statement is false.

### Solution 6

We investigate:

\[
x^2+1>x.
\]

Bring all terms to one side:

\[
x^2-x+1>0.
\]

Complete the square:

\[
x^2-x+1=\left(x-\frac12\right)^2-\frac14+1.
\]

\[
=\left(x-\frac12\right)^2+\frac34.
\]

Since:

\[
\left(x-\frac12\right)^2\geq0,
\]

we have:

\[
\left(x-\frac12\right)^2+\frac34\geq\frac34.
\]

Since:

\[
\frac34>0,
\]

\[
x^2-x+1>0
\]

for all real `x`.

Therefore:

\[
x^2+1>x
\]

is always true.

## Common CCEA-Style Wording

| Wording | What to do |
|---|---|
| “Prove that...” | Write a general argument, not just examples |
| “Disprove...” | Give one valid counterexample |
| “For all integers `n`” | Consider all `n in Z`, often using cases |
| “For `n in N`” | Work with natural numbers, usually positive integers unless stated otherwise |
| “Always, sometimes or never true” | Decide whether all, some or no values work |
| “Hence” | Use your previous result |
| “Show that” | Give enough working to justify the printed result |

## Syllabus Gap Check

| Item | Status |
|---|---|
| Proof by deduction | Covered |
| Proof by exhaustion | Covered |
| Disproof by counterexample | Covered |
| Proof by contradiction | Logged as A2/future context, excluded from AS1 core |
| AS1-AF-LO002 support | Covered through surd counterexample |
| AS1-AF-LO005 support | Covered through completing the square |
| AS1-AF-LO006 support | Covered through quadratic equation in triangle proof |
| AS1-AF-LO010 support | Covered throughout |
| AS1-SS-LO001 support | Covered through binomial expansion examples |
| Visual placeholders | Inserted |
| Widgets | Placeholder inserted only |
| Missing evidence | Logged |
| Off-spec material | Controlled |

## Visual and Interactive Asset Plan

| Asset ID | Type | Purpose | Phase |
|---|---|---|---|
| AS1AlgebraicMethodsProofSVG-001 | SVG | Proof method decision tree | Phase 3 |
| AS1AlgebraicMethodsProofSVG-002 | SVG | Integer forms and case splits | Phase 3 |
| AS1AlgebraicMethodsProofSVG-003 | SVG | Consecutive integer right-triangle diagram | Phase 3 |
| AS1AlgebraicMethodsProofSVG-004 | SVG | Proof-type overview cards with A2 contradiction labelled | Phase 3 |
| AS1AlgebraicMethodsProofWidget-001 | HTML widget | Interactive proof-method selector | Phase 5 |
| AS1AlgebraicMethodsProofMermaid-001 | Mermaid | Flowchart for proof choice | Phase 2 |
| AS1AlgebraicMethodsProofTikZ-001 | TikZ | Right-triangle proof diagram | Phase 4 |

## Supplementary Sources Used

No external web sources were used.

The lesson uses only:

- the pre-loaded CCEA Mathematics specification map;
- the pre-loaded project module map;
- the pre-loaded evidence checklist;
- the uploaded teacher transcript;
- the uploaded screenshots PDF.

The transcript's references to P1 textbook exercises and exam questions are treated as teacher-evidence provenance only, not as CCEA authority.

## Final Student Checklist

You are ready for this lesson when you can:

- write an even integer as `2k`;
- write an odd integer as `2k+1` or `2k-1`;
- explain why `2(integer)` is even;
- explain why `2(integer)+1` is odd;
- choose proof by deduction when algebra directly reaches the result;
- choose proof by exhaustion when all cases must be checked;
- split integers into even/odd cases;
- split integers into `3k`, `3k+1`, `3k-1` cases;
- find a counterexample to disprove a false universal statement;
- write a final sentence that matches the question exactly;
- avoid assuming the conclusion at the start of a proof.
