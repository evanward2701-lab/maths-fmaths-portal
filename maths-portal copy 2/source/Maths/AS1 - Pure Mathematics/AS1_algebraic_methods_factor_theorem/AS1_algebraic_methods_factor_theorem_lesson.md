# AS1 Algebraic Methods: Algebraic Fractions, Polynomial Division and Factor Theorem

## Title and Metadata

| Field | Value |
|---|---|
| Course | CCEA GCE Mathematics |
| Unit code | AS1 |
| Unit name | AS 1 Pure Mathematics |
| Topic code | AS1-AF |
| Official topic area | Algebra and functions |
| Lesson topic | Algebraic Methods: Algebraic Fractions, Polynomial Division and Factor Theorem |
| Topic slug | algebraic_methods_factor_theorem |
| Topic Pascal | AlgebraicMethodsFactorTheorem |
| Topic ID | AS1AlgebraicMethodsFactorTheorem |
| Lesson file | AS1_algebraic_methods_factor_theorem_lesson.md |
| Learning outcome IDs | AS1-AF-LO010, AS1-AF-LO011 |
| Core tags | #AS1 #AlgebraFunctions #PolynomialDivision #FactorTheorem #RemainderTheorem |

## Evidence Map

| Evidence | Used for |
|---|---|
| CCEA GCE Mathematics Specification Map | Unit identity, LO IDs and syllabus boundary. |
| README Module Map | Lesson structure, topic metadata conventions and phase workflow. |
| Evidence Drop Checklist | Missing evidence, off-spec logs and visual placeholder rules. |
| `P1-Chp7-AlgebraicMethods_RevealBlocksRemoved.pdf` | Slide examples, warnings and visual sequence for algebraic fractions, division and factor theorem. |
| `Chapter_7a_Algebraic_Methods,_Factor_Theorem_🤖_(Pure_Year_1)_Transcript.md` | Detailed explanations, worked algebra steps, warnings, notation and exam technique. |
| `Chapter_7a_Algebraic_Methods,_Factor_Theorem_🤖_(Pure_Year_1)_Screenshots.pdf` | Visual support only for board-work sequencing and placeholder planning. |

## Specification Alignment

### AS1-AF-LO010

**Official learning outcome:** manipulate polynomials algebraically, including expanding brackets and collecting like terms, factorisation and simple algebraic division.

This lesson covers this through:

- simplifying algebraic fractions by factorising and cancelling common factors;
- recognising difference of two squares;
- polynomial long division by linear expressions;
- writing answers in quotient plus remainder form;
- checking division by expanding.

### AS1-AF-LO011

**Official learning outcome:** use the remainder and factor theorems.

This lesson covers this through:

- substituting into \(f(x)\) to find remainders;
- using \(f(a)=0\) to prove \(x-a\) is a factor;
- using a known factor to divide a cubic;
- fully factorising cubic expressions;
- finding unknown coefficients when a factor is given.

## Learning Objectives

By the end of this lesson, you should be able to:

1. simplify algebraic fractions by factorising the numerator and denominator;
2. avoid invalid cancellation by checking whether a factor belongs to every term or to a whole bracket;
3. divide a polynomial by a linear expression using algebraic long division;
4. identify the dividend, divisor, quotient and remainder;
5. use the remainder theorem in the CCEA sense;
6. use the factor theorem to show that a linear expression is a factor;
7. fully factorise cubic expressions using a found factor;
8. find unknown coefficients using a given factor;
9. write clear final statements that earn the communication mark.

## Prerequisite Recap

This lesson assumes the following algebra tools are already available.

| Prior skill | Why it matters here |
|---|---|
| Expanding brackets | Used to check answers after factorising or division. |
| Factorising quadratics | Used to simplify fractions and factorise the remaining quadratic after cubic division. |
| Difference of two squares | Used for expressions such as \(x^2-1\) and \(4-x^2\). |
| Substitution into expressions | Used for \(f(2)\), \(f(-3)\), \(g(-2)\), etc. |
| Negative arithmetic | Essential when subtracting rows in polynomial division. |
| Function notation | Needed for clear factor theorem solutions. |

No GCSE source is being used as evidence here. These are prerequisite skills only.

## Big Picture Explanation

This lesson is about turning awkward algebra into usable algebra.

A polynomial such as

\[
2x^3+x^2-18x-9
\]

is not very revealing in expanded form. It hides its roots, factors and graph behaviour. Once we find a factor, for example \(x-3\), we can rewrite it as

\[
2x^3+x^2-18x-9=(x-3)(2x^2+7x+3),
\]

and then factorise further:

\[
2x^3+x^2-18x-9=(x-3)(2x+1)(x+3).
\]

That factorised form reveals structure: factors, roots and possible graph intersections.

## Key Definitions and Notation

### Polynomial

A polynomial is an expression made from powers of \(x\) with coefficients, such as

\[
3x^3+0x^2-2x+4.
\]

Writing the missing term \(0x^2\) is often useful in polynomial division because it keeps the powers in order.

### Dividend, divisor, quotient and remainder

In a division,

\[
\text{dividend} \div \text{divisor}=\text{quotient with possible remainder}.
\]

For example,

\[
11\div4=2\text{ remainder }3.
\]

- The **dividend** is the thing being divided.
- The **divisor** is the thing we divide by.
- The **quotient** is the main answer.
- The **remainder** is the part left over.

For polynomial division, if

\[
P(x)\div D(x)=Q(x)\text{ remainder }R(x),
\]

then

\[
P(x)=D(x)Q(x)+R(x).
\]

### Factor

A factor divides exactly with no remainder.

So \(x-a\) is a factor of \(f(x)\) means

\[
f(x)=(x-a)Q(x)
\]

for some quotient polynomial \(Q(x)\).

### Remainder theorem

For CCEA AS1, the remainder theorem is on-spec.

If a polynomial \(f(x)\) is divided by \(x-a\), then the remainder is

\[
f(a).
\]

### Factor theorem

If \(f(x)\) is a polynomial, then:

\[
f(a)=0 \iff x-a \text{ is a factor of } f(x).
\]

Be careful with signs:

- \(x-2\) corresponds to \(a=2\), so test \(f(2)\).
- \(x+3=x-(-3)\), so test \(f(-3)\).
- \(2x+1=0\) gives \(x=-\frac12\), so test \(f\!\left(-\frac12\right)\).

## Visual Asset Integration

[VISUAL PLACEHOLDER: AS1AlgebraicMethodsSVG-001 | Source: Dr Frost PDF page 4 + teacher transcript | Insert from svg/AS1AlgebraicMethodsSVG-001.svg | Purpose: Show how algebraic fractions are simplified by factorising first, then cancelling common factors.]

[VISUAL PLACEHOLDER: AS1AlgebraicMethodsSVG-002 | Source: Dr Frost PDF pages 7-11 + teacher transcript | Insert from svg/AS1AlgebraicMethodsSVG-002.svg | Purpose: Show the polynomial long division layout with powers of \(x\) kept in columns.]

[VISUAL PLACEHOLDER: AS1AlgebraicMethodsMER-001 | Source: CCEA specification map + teacher transcript | Insert from mermaid/AS1AlgebraicMethodsMER-001.md | Purpose: Decision flow for using factor theorem, remainder theorem or polynomial division.]

[VISUAL PLACEHOLDER: AS1AlgebraicMethodsTikZ-001 | Source: Teacher transcript + Dr Frost PDF | Insert from tikz/AS1AlgebraicMethodsTikZ-001.tex | Purpose: Clean printable long division example.]

[VISUAL PLACEHOLDER: AS1AlgebraicMethodsTikZ-002 | Source: CCEA specification map + teacher transcript | Insert from tikz/AS1AlgebraicMethodsTikZ-002.tex | Purpose: Printable decision card for remainder theorem and factor theorem. This is an AI-proposed teaching enhancement.]

[INTERACTIVE PLACEHOLDER: AS1AlgebraicMethodsWidget-001 | Source: Teacher transcript calculator/table-mode discussion | Insert from widgets/AS1AlgebraicMethodsWidget-001.html | Purpose: Let the student test integer values of \(x\) and see when \(f(x)=0\), supporting factor theorem searches.]

[INTERACTIVE PLACEHOLDER: AS1AlgebraicMethodsWidget-002 | Source: CCEA specification map + teacher transcript | Insert from widgets/AS1AlgebraicMethodsWidget-002.html | Purpose: Remainder theorem substitution checker.]

## Core Theory A: Simplifying Algebraic Fractions

### A1. The central idea

You can simplify ordinary fractions by dividing the numerator and denominator by a common factor.

The same is true for algebraic fractions, but the key word is **factor**.

You may cancel common factors. You may not cancel random terms.

The battle plan is:

\[
\text{factorise first} \quad \rightarrow \quad \text{identify common factors} \quad \rightarrow \quad \text{cancel common factors}.
\]

### A2. Example: dividing every term by \(x\)

Simplify

\[
\frac{7x^4-2x^3+6x}{x}.
\]

Because every term in the numerator is being divided by \(x\), split the fraction into separate terms:

\[
\frac{7x^4-2x^3+6x}{x}
=
\frac{7x^4}{x}
-
\frac{2x^3}{x}
+
\frac{6x}{x}.
\]

Now simplify each term:

\[
\frac{7x^4}{x}=7x^3,
\]

\[
\frac{2x^3}{x}=2x^2,
\]

\[
\frac{6x}{x}=6.
\]

Therefore

\[
\frac{7x^4-2x^3+6x}{x}=7x^3-2x^2+6.
\]

Alternative factorisation method:

\[
7x^4-2x^3+6x=x(7x^3-2x^2+6).
\]

So

\[
\frac{7x^4-2x^3+6x}{x}
=
\frac{x(7x^3-2x^2+6)}{x}
=
7x^3-2x^2+6.
\]

### A3. Warning: only cancel through every term

Compare with

\[
\frac{7x^4-2x^3+6}{x}.
\]

The final term \(6\) does not contain a factor of \(x\), so:

\[
\frac{7x^4-2x^3+6}{x}
=
\frac{7x^4}{x}-\frac{2x^3}{x}+\frac6x
=
7x^3-2x^2+\frac6x.
\]

You cannot cancel \(x\) through the whole numerator unless every term has a factor of \(x\).

### A4. Example: difference of two squares

Simplify

\[
\frac{x^2-1}{x^2+x}.
\]

First factorise the numerator:

\[
x^2-1=(x+1)(x-1).
\]

Then factorise the denominator:

\[
x^2+x=x(x+1).
\]

So

\[
\frac{x^2-1}{x^2+x}
=
\frac{(x+1)(x-1)}{x(x+1)}.
\]

Cancel the common factor \(x+1\):

\[
\frac{(x+1)(x-1)}{x(x+1)}=\frac{x-1}{x}.
\]

Therefore

\[
\boxed{\frac{x^2-1}{x^2+x}=\frac{x-1}{x}}.
\]

### A5. What simplification really means

The two expressions

\[
\frac{x^2-1}{x^2+x}
\quad\text{and}\quad
\frac{x-1}{x}
\]

look different, but they give the same value for allowed values of \(x\).

The original denominator is

\[
x^2+x=x(x+1),
\]

so the original expression is undefined when

\[
x=0 \quad \text{or} \quad x=-1.
\]

The simplified form still carries those original restrictions.

### A6. Example: use the denominator as a clue

Simplify

\[
\frac{x^2+3x+2}{x+1}.
\]

Factorise the numerator:

\[
x^2+3x+2=(x+1)(x+2).
\]

So

\[
\frac{x^2+3x+2}{x+1}
=
\frac{(x+1)(x+2)}{x+1}
=x+2.
\]

Do not write \(\frac{x+2}{1}\) as your final answer. The evidence warning is: do not leave \(1\) in the denominator.

### A7. Example: factorise the easier quadratic first

Simplify

\[
\frac{2x^2+11x+12}{x^2+9x+20}.
\]

The denominator is easier because the coefficient of \(x^2\) is \(1\):

\[
x^2+9x+20=(x+5)(x+4).
\]

Now factorise the numerator:

\[
2x^2+11x+12=(2x+3)(x+4).
\]

Check by expanding:

\[
(2x+3)(x+4)=2x^2+8x+3x+12=2x^2+11x+12.
\]

So

\[
\frac{2x^2+11x+12}{x^2+9x+20}
=
\frac{(2x+3)(x+4)}{(x+5)(x+4)}
=
\frac{2x+3}{x+5}.
\]

### A8. Example: when factors look similar but not identical

Simplify

\[
\frac{4-x^2}{x^2+2x-8}.
\]

First factorise the numerator using difference of two squares:

\[
4-x^2=2^2-x^2=(2-x)(2+x).
\]

Now factorise the denominator:

\[
x^2+2x-8=(x+4)(x-2).
\]

So

\[
\frac{4-x^2}{x^2+2x-8}
=
\frac{(2-x)(2+x)}{(x+4)(x-2)}.
\]

At first glance, \(2-x\) and \(x-2\) are not the same. But

\[
2-x=-(x-2).
\]

Show this carefully:

\[
-(x-2)=-x+2=2-x.
\]

Therefore

\[
(2-x)(2+x)=-(x-2)(2+x).
\]

So

\[
\frac{(2-x)(2+x)}{(x+4)(x-2)}
=
\frac{-(x-2)(2+x)}{(x+4)(x-2)}
=-\frac{2+x}{x+4}.
\]

Since \(2+x=x+2\), this can be written as

\[
\boxed{-\frac{x+2}{x+4}}.
\]

### A9. Sign warning: the negative applies to the whole numerator

The expression

\[
-\frac{x+2}{x+4}
\]

means

\[
\frac{-(x+2)}{x+4}=\frac{-x-2}{x+4}.
\]

It is not the same as

\[
\frac{-x+2}{x+4}.
\]

If you write the negative in the numerator, use brackets:

\[
\frac{-(x+2)}{x+4}.
\]

Safe equivalent forms include:

\[
-\frac{x+2}{x+4},\qquad \frac{-(x+2)}{x+4},\qquad \frac{-x-2}{x+4}.
\]

## Core Theory B: Polynomial Long Division by Linear Expressions

### B1. Why long division appears here

Polynomial division is the algebra version of ordinary long division. With numbers, we repeatedly:

1. divide;
2. multiply;
3. subtract;
4. bring down the next part.

With polynomials, we do the same thing, but instead of place-value columns, we use powers of \(x\):

\[
x^3,\quad x^2,\quad x,\quad \text{constant}.
\]

The evidence phrase to keep in your head is:

\[
\boxed{\text{divide, multiply, subtract, bring down}}.
\]

### B2. The CCEA boundary

For this lesson, algebraic division is by a **linear expression only**, such as

\[
x+5,\quad x-4,\quad 2x-1,\quad 5x+3.
\]

Division by quadratic expressions is not treated as required AS1 core content in this lesson.

### B3. Main example: divide \(6x^3+28x^2-7x+15\) by \(x+5\)

We want to divide

\[
6x^3+28x^2-7x+15
\]

by

\[
x+5.
\]

#### Step 1: divide

Look only at the highest-power term of the divisor. The divisor is \(x+5\), so the highest-power term is \(x\).

\[
\frac{6x^3}{x}=6x^2.
\]

#### Step 2: multiply

Multiply \(6x^2\) by the whole divisor:

\[
6x^2(x+5)=6x^3+30x^2.
\]

#### Step 3: subtract

Subtract this from the first part of the dividend:

\[
(6x^3+28x^2)-(6x^3+30x^2).
\]

Work term by term:

\[
6x^3-6x^3=0,
\]

\[
28x^2-30x^2=-2x^2.
\]

#### Step 4: bring down

Bring down the next term, \(-7x\):

\[
-2x^2-7x.
\]

Now repeat.

#### Step 5: divide again

\[
\frac{-2x^2}{x}=-2x.
\]

#### Step 6: multiply again

\[
-2x(x+5)=-2x^2-10x.
\]

#### Step 7: subtract again

\[
(-2x^2-7x)-(-2x^2-10x).
\]

Be careful:

\[
-2x^2-(-2x^2)=0,
\]

\[
-7x-(-10x)=-7x+10x=3x.
\]

#### Step 8: bring down

Bring down \(+15\):

\[
3x+15.
\]

#### Step 9: divide again

\[
\frac{3x}{x}=3.
\]

#### Step 10: multiply again

\[
3(x+5)=3x+15.
\]

#### Step 11: subtract again

\[
(3x+15)-(3x+15)=0.
\]

So the remainder is \(0\). Therefore

\[
\frac{6x^3+28x^2-7x+15}{x+5}=6x^2-2x+3.
\]

Final answer:

\[
\boxed{6x^2-2x+3}.
\]

Because the remainder is zero, we can also write

\[
6x^3+28x^2-7x+15=(x+5)(6x^2-2x+3).
\]

### B4. Check by expanding

Expand

\[
(x+5)(6x^2-2x+3).
\]

First multiply by \(x\):

\[
x(6x^2-2x+3)=6x^3-2x^2+3x.
\]

Then multiply by \(5\):

\[
5(6x^2-2x+3)=30x^2-10x+15.
\]

Add:

\[
6x^3-2x^2+3x+30x^2-10x+15.
\]

Collect like terms:

\[
6x^3+28x^2-7x+15.
\]

This matches the original dividend, so the division is correct.

## Core Theory C: Missing Terms and Remainders

### C1. Missing terms must be written with zero coefficients

If a polynomial skips a power of \(x\), write in the missing term with coefficient \(0\).

For example,

\[
3x^3-2x+4
\]

has no \(x^2\) term. So write it as

\[
3x^3+0x^2-2x+4.
\]

This keeps the columns in the correct positions:

\[
x^3,\quad x^2,\quad x,\quad \text{constant}.
\]

### C2. Example: find the remainder when \(3x^3-2x+4\) is divided by \(x-1\)

We divide

\[
3x^3+0x^2-2x+4
\]

by

\[
x-1.
\]

#### Step 1: divide

\[
\frac{3x^3}{x}=3x^2.
\]

#### Step 2: multiply

\[
3x^2(x-1)=3x^3-3x^2.
\]

#### Step 3: subtract

\[
(3x^3+0x^2)-(3x^3-3x^2).
\]

Term by term:

\[
3x^3-3x^3=0,
\]

\[
0x^2-(-3x^2)=3x^2.
\]

Bring down \(-2x\):

\[
3x^2-2x.
\]

#### Step 4: divide again

\[
\frac{3x^2}{x}=3x.
\]

#### Step 5: multiply again

\[
3x(x-1)=3x^2-3x.
\]

#### Step 6: subtract again

\[
(3x^2-2x)-(3x^2-3x).
\]

Term by term:

\[
3x^2-3x^2=0,
\]

\[
-2x-(-3x)=-2x+3x=x.
\]

Bring down \(+4\):

\[
x+4.
\]

#### Step 7: divide again

\[
\frac{x}{x}=1.
\]

#### Step 8: multiply again

\[
1(x-1)=x-1.
\]

#### Step 9: subtract again

\[
(x+4)-(x-1).
\]

Term by term:

\[
x-x=0,
\]

\[
4-(-1)=5.
\]

So the remainder is

\[
\boxed{5}.
\]

The quotient is

\[
3x^2+3x+1.
\]

So

\[
\frac{3x^3-2x+4}{x-1}=3x^2+3x+1+\frac{5}{x-1}.
\]

Equivalently,

\[
3x^3-2x+4=(x-1)(3x^2+3x+1)+5.
\]

### C3. Quotient plus remainder form

If \(P(x)\div D(x)\) gives quotient \(Q(x)\) and remainder \(R\), then

\[
\frac{P(x)}{D(x)}=Q(x)+\frac{R}{D(x)}.
\]

For example,

\[
\frac{3x^3-2x+4}{x-1}=3x^2+3x+1+\frac{5}{x-1}.
\]

## Core Theory D: Dividing When the Remainder Is Negative

### D1. Example: find the remainder when \(2x^3-5x^2-16x+10\) is divided by \(x-4\)

We divide

\[
2x^3-5x^2-16x+10
\]

by

\[
x-4.
\]

#### Step 1: divide

\[
\frac{2x^3}{x}=2x^2.
\]

#### Step 2: multiply

\[
2x^2(x-4)=2x^3-8x^2.
\]

#### Step 3: subtract

\[
(2x^3-5x^2)-(2x^3-8x^2).
\]

\[
2x^3-2x^3=0,
\]

\[
-5x^2-(-8x^2)=-5x^2+8x^2=3x^2.
\]

Bring down \(-16x\):

\[
3x^2-16x.
\]

#### Step 4: divide again

\[
\frac{3x^2}{x}=3x.
\]

#### Step 5: multiply again

\[
3x(x-4)=3x^2-12x.
\]

#### Step 6: subtract again

\[
(3x^2-16x)-(3x^2-12x).
\]

\[
3x^2-3x^2=0,
\]

\[
-16x-(-12x)=-16x+12x=-4x.
\]

Bring down \(+10\):

\[
-4x+10.
\]

#### Step 7: divide again

\[
\frac{-4x}{x}=-4.
\]

#### Step 8: multiply again

\[
-4(x-4)=-4x+16.
\]

#### Step 9: subtract again

\[
(-4x+10)-(-4x+16).
\]

\[
-4x-(-4x)=0,
\]

\[
10-16=-6.
\]

So the remainder is

\[
\boxed{-6}.
\]

The quotient is

\[
2x^2+3x-4.
\]

So

\[
\frac{2x^3-5x^2-16x+10}{x-4}=2x^2+3x-4-\frac6{x-4}.
\]

Equivalently,

\[
2x^3-5x^2-16x+10=(x-4)(2x^2+3x-4)-6.
\]

## Core Theory E: Division by \(2x-1\)

### E1. Example: divide \(8x^3-1\) by \(2x-1\)

First include missing terms:

\[
8x^3-1=8x^3+0x^2+0x-1.
\]

Divide by

\[
2x-1.
\]

#### Step 1: divide

The highest-power term of the divisor is \(2x\).

\[
\frac{8x^3}{2x}=4x^2.
\]

#### Step 2: multiply

\[
4x^2(2x-1)=8x^3-4x^2.
\]

#### Step 3: subtract

\[
(8x^3+0x^2)-(8x^3-4x^2).
\]

\[
8x^3-8x^3=0,
\]

\[
0x^2-(-4x^2)=4x^2.
\]

Bring down \(+0x\):

\[
4x^2+0x.
\]

#### Step 4: divide again

\[
\frac{4x^2}{2x}=2x.
\]

#### Step 5: multiply again

\[
2x(2x-1)=4x^2-2x.
\]

#### Step 6: subtract again

\[
(4x^2+0x)-(4x^2-2x).
\]

\[
4x^2-4x^2=0,
\]

\[
0x-(-2x)=2x.
\]

Bring down \(-1\):

\[
2x-1.
\]

#### Step 7: divide again

\[
\frac{2x}{2x}=1.
\]

#### Step 8: multiply again

\[
1(2x-1)=2x-1.
\]

#### Step 9: subtract again

\[
(2x-1)-(2x-1)=0.
\]

So the remainder is \(0\). Therefore

\[
\frac{8x^3-1}{2x-1}=4x^2+2x+1.
\]

Final answer:

\[
\boxed{4x^2+2x+1}.
\]

Since the remainder is zero,

\[
8x^3-1=(2x-1)(4x^2+2x+1).
\]

### E2. Off-spec enrichment note: difference of two cubes

The evidence mentions the identity

\[
x^3-y^3=(x-y)(x^2+xy+y^2),
\]

but it also states that this is **not in the A Level syllabus** for that source. Therefore, this identity is not treated as required core content here.

For this lesson, the on-spec method is polynomial division by the linear divisor.

## Core Theory F: The Remainder Theorem

### F1. Statement

For CCEA AS1, the remainder theorem is core content.

If a polynomial \(f(x)\) is divided by

\[
x-a,
\]

then the remainder is

\[
f(a).
\]

So:

\[
\boxed{\text{Remainder when }f(x)\text{ is divided by }x-a=f(a)}.
\]

### F2. Why this works

Suppose dividing \(f(x)\) by \(x-a\) gives quotient \(Q(x)\) and remainder \(R\). Then

\[
f(x)=(x-a)Q(x)+R.
\]

Now substitute \(x=a\):

\[
f(a)=(a-a)Q(a)+R.
\]

Since

\[
a-a=0,
\]

we get

\[
f(a)=0\cdot Q(a)+R.
\]

So

\[
f(a)=R.
\]

Therefore the remainder is

\[
\boxed{f(a)}.
\]

### F3. Example using the remainder theorem

Find the remainder when

\[
f(x)=3x^3-2x+4
\]

is divided by

\[
x-1.
\]

Here

\[
x-1=x-a,
\]

so

\[
a=1.
\]

By the remainder theorem, the remainder is

\[
f(1).
\]

Calculate:

\[
f(1)=3(1)^3-2(1)+4.
\]

Now simplify:

\[
f(1)=3-2+4=5.
\]

Therefore the remainder is

\[
\boxed{5}.
\]

This matches the long division result.

### F4. Linear divisors not written as \(x-a\)

If the divisor is

\[
2x+1,
\]

do not substitute \(1\). Instead, set the divisor equal to zero:

\[
2x+1=0.
\]

Solve:

\[
2x=-1,
\]

\[
x=-\frac12.
\]

So for a divisor or factor of \(2x+1\), use

\[
f\!\left(-\frac12\right).
\]

In general, for \(ax+b\), solve

\[
ax+b=0
\]

before substituting.

## Core Theory G: The Factor Theorem

### G1. Statement

If \(f(x)\) is a polynomial, then:

\[
\boxed{f(a)=0 \iff x-a \text{ is a factor of } f(x)}.
\]

This means:

- if \(f(a)=0\), then \(x-a\) is a factor;
- if \(x-a\) is a factor, then \(f(a)=0\).

### G2. Why the factor theorem follows from the remainder theorem

By the remainder theorem, when \(f(x)\) is divided by \(x-a\), the remainder is \(f(a)\).

If

\[
f(a)=0,
\]

then the remainder is zero. A zero remainder means \(x-a\) divides \(f(x)\) exactly. Therefore \(x-a\) is a factor of \(f(x)\).

### G3. Example: show that \(x-2\) is a factor of \(x^3+x^2-4x-4\)

Let

\[
f(x)=x^3+x^2-4x-4.
\]

To test whether \(x-2\) is a factor, use \(x-2=0\), so \(x=2\).

Now calculate \(f(2)\):

\[
f(2)=2^3+2^2-4(2)-4.
\]

Work through every term:

\[
2^3=8,
\]

\[
2^2=4,
\]

\[
-4(2)=-8.
\]

So

\[
f(2)=8+4-8-4=0.
\]

Therefore

\[
f(2)=0.
\]

By the factor theorem,

\[
\boxed{x-2 \text{ is a factor of } x^3+x^2-4x-4}.
\]

### G4. The final sentence matters

In exams, do not stop at

\[
f(2)=0.
\]

You should write:

\[
f(2)=0,\ \therefore \text{ by the factor theorem, }x-2\text{ is a factor of }f(x).
\]

## Core Theory H: Fully Factorising a Cubic

### H1. Battle plan

To fully factorise a cubic:

1. Define the polynomial: \(f(x)=\cdots\).
2. Try simple integer values: \(x=1,-1,2,-2,3,-3,\ldots\).
3. When you find \(f(a)=0\), conclude \(x-a\) is a factor.
4. Divide the cubic by \(x-a\).
5. Factorise the resulting quadratic.

### H2. Example: fully factorise \(2x^3+x^2-18x-9\)

Let

\[
f(x)=2x^3+x^2-18x-9.
\]

Try \(x=1\):

\[
f(1)=2(1)^3+(1)^2-18(1)-9=2+1-18-9=-24.
\]

So \(x-1\) is not a factor.

Try \(x=-1\):

\[
f(-1)=2(-1)^3+(-1)^2-18(-1)-9.
\]

\[
f(-1)=2(-1)+1+18-9=-2+1+18-9=8.
\]

So \(x+1\) is not a factor.

Try \(x=3\):

\[
f(3)=2(3)^3+(3)^2-18(3)-9.
\]

\[
f(3)=2(27)+9-54-9=54+9-54-9=0.
\]

Therefore, by the factor theorem,

\[
x-3
\]

is a factor.

Now divide \(2x^3+x^2-18x-9\) by \(x-3\).

First term:

\[
\frac{2x^3}{x}=2x^2.
\]

Multiply:

\[
2x^2(x-3)=2x^3-6x^2.
\]

Subtract:

\[
(2x^3+x^2)-(2x^3-6x^2)=7x^2.
\]

Bring down \(-18x\):

\[
7x^2-18x.
\]

Next term:

\[
\frac{7x^2}{x}=7x.
\]

Multiply:

\[
7x(x-3)=7x^2-21x.
\]

Subtract:

\[
(7x^2-18x)-(7x^2-21x)=3x.
\]

Bring down \(-9\):

\[
3x-9.
\]

Next term:

\[
\frac{3x}{x}=3.
\]

Multiply:

\[
3(x-3)=3x-9.
\]

Subtract:

\[
(3x-9)-(3x-9)=0.
\]

So

\[
2x^3+x^2-18x-9=(x-3)(2x^2+7x+3).
\]

Now factorise the quadratic:

\[
2x^2+7x+3.
\]

We need two factors whose product is \(2\cdot3=6\) and whose sum is \(7\). Those numbers are \(6\) and \(1\). So

\[
2x^2+7x+3=(2x+1)(x+3).
\]

Therefore

\[
\boxed{2x^3+x^2-18x-9=(x-3)(2x+1)(x+3)}.
\]

## Core Theory I: Finding Unknown Coefficients Using a Given Factor

### I1. The key idea

If a factor is given, choose the value of \(x\) that makes that factor equal zero. Then substitute that value into the polynomial and set the result equal to zero.

### I2. Example: \(2x+1\) is a factor of \(6x^3+ax^2+1\)

Given that \(2x+1\) is a factor of

\[
6x^3+ax^2+1,
\]

find \(a\).

Let

\[
f(x)=6x^3+ax^2+1.
\]

Since

\[
2x+1=0,
\]

we solve:

\[
2x=-1,
\]

\[
x=-\frac12.
\]

Because \(2x+1\) is a factor,

\[
f\!\left(-\frac12\right)=0.
\]

Now substitute:

\[
f\!\left(-\frac12\right)=6\left(-\frac12\right)^3+a\left(-\frac12\right)^2+1.
\]

Calculate each power:

\[
\left(-\frac12\right)^3=-\frac18,
\]

\[
\left(-\frac12\right)^2=\frac14.
\]

So

\[
f\!\left(-\frac12\right)=6\left(-\frac18\right)+a\left(\frac14\right)+1.
\]

Simplify:

\[
6\left(-\frac18\right)=-\frac68=-\frac34.
\]

Therefore

\[
-\frac34+\frac14a+1=0.
\]

Combine constants:

\[
-\frac34+1=\frac14.
\]

So

\[
\frac14+\frac14a=0.
\]

Subtract \(\frac14\) from both sides:

\[
\frac14a=-\frac14.
\]

Multiply both sides by \(4\):

\[
a=-1.
\]

Final answer:

\[
\boxed{a=-1}.
\]

### I3. Example: \(3x-1\) is a factor of \(3x^3+11x^2+ax+1\)

Given that \(3x-1\) is a factor of

\[
3x^3+11x^2+ax+1,
\]

find \(a\).

Let

\[
f(x)=3x^3+11x^2+ax+1.
\]

Since

\[
3x-1=0,
\]

we solve:

\[
3x=1,
\]

\[
x=\frac13.
\]

Because \(3x-1\) is a factor,

\[
f\!\left(\frac13\right)=0.
\]

Substitute:

\[
f\!\left(\frac13\right)=3\left(\frac13\right)^3+11\left(\frac13\right)^2+a\left(\frac13\right)+1.
\]

Calculate powers:

\[
\left(\frac13\right)^3=\frac1{27},
\]

\[
\left(\frac13\right)^2=\frac19.
\]

So

\[
f\!\left(\frac13\right)=3\left(\frac1{27}\right)+11\left(\frac19\right)+\frac13a+1.
\]

Simplify:

\[
3\left(\frac1{27}\right)=\frac3{27}=\frac19,
\]

\[
11\left(\frac19\right)=\frac{11}{9}.
\]

So

\[
\frac19+\frac{11}{9}+\frac13a+1=0.
\]

Combine the first two fractions:

\[
\frac19+\frac{11}{9}=\frac{12}{9}=\frac43.
\]

Write \(1\) as thirds:

\[
1=\frac33.
\]

So

\[
\frac43+\frac33+\frac13a=0.
\]

\[
\frac73+\frac13a=0.
\]

Subtract \(\frac73\):

\[
\frac13a=-\frac73.
\]

Multiply by \(3\):

\[
a=-7.
\]

Final answer:

\[
\boxed{a=-7}.
\]

## Worked Examples

### Worked Example 1: simplify an algebraic fraction

Simplify

\[
\frac{x^2-1}{x^2+x}.
\]

Solution:

\[
x^2-1=(x+1)(x-1),
\]

\[
x^2+x=x(x+1).
\]

Therefore

\[
\frac{x^2-1}{x^2+x}=\frac{(x+1)(x-1)}{x(x+1)}=\frac{x-1}{x}.
\]

Final answer:

\[
\boxed{\frac{x-1}{x}}.
\]

### Worked Example 2: divide a polynomial

Divide

\[
6x^3+28x^2-7x+15
\]

by

\[
x+5.
\]

Solution:

\[
\frac{6x^3+28x^2-7x+15}{x+5}=6x^2-2x+3.
\]

Check:

\[
(x+5)(6x^2-2x+3)=6x^3+28x^2-7x+15.
\]

Final answer:

\[
\boxed{6x^2-2x+3}.
\]

### Worked Example 3: use the remainder theorem

Find the remainder when

\[
f(x)=2x^3-5x^2-16x+10
\]

is divided by \(x-4\).

Solution:

Since the divisor is \(x-4\), use \(x=4\).

\[
f(4)=2(4)^3-5(4)^2-16(4)+10.
\]

\[
f(4)=128-80-64+10=-6.
\]

Remainder:

\[
\boxed{-6}.
\]

### Worked Example 4: use the factor theorem

Show that \(x-2\) is a factor of

\[
x^3+x^2-4x-4.
\]

Solution:

Let

\[
f(x)=x^3+x^2-4x-4.
\]

Test \(x=2\):

\[
f(2)=2^3+2^2-4(2)-4=8+4-8-4=0.
\]

Therefore, by the factor theorem,

\[
\boxed{x-2\text{ is a factor of }x^3+x^2-4x-4}.
\]

## Guided Practice

Try these before reading the solutions.

### Algebraic Fractions

1. Simplify

\[
\frac{6x^3+9x^2}{3x}.
\]

2. Simplify

\[
\frac{x^2-9}{x^2+3x}.
\]

3. Simplify

\[
\frac{x^2+5x+6}{x+2}.
\]

4. Simplify

\[
\frac{3x^2+13x+14}{x^2+6x+8}.
\]

5. Simplify

\[
\frac{9-x^2}{x^2+x-6}.
\]

### Polynomial Division

6. Divide

\[
6x^3+28x^2-7x+15
\]

by \(x+5\).

7. Find the remainder when

\[
3x^3-2x+4
\]

is divided by \(x-1\).

8. Find the remainder when

\[
2x^3-5x^2-16x+10
\]

is divided by \(x-4\).

9. Divide

\[
8x^3-1
\]

by \(2x-1\).

10. Write

\[
\frac{3x^3-2x+4}{x-1}
\]

in quotient plus remainder form.

### Remainder and Factor Theorems

11. Use the factor theorem to show that \(x-2\) is a factor of

\[
x^3+x^2-4x-4.
\]

12. Fully factorise

\[
2x^3+x^2-18x-9.
\]

13. Given that \(2x+1\) is a factor of

\[
6x^3+ax^2+1,
\]

find \(a\).

14. Given that \(3x-1\) is a factor of

\[
3x^3+11x^2+ax+1,
\]

find \(a\).

15. Find the remainder when

\[
f(x)=4x^3-7x+2
\]

is divided by \(x+2\).

## Common Mistakes and Exam Traps

| Mistake | Why it loses marks | Safer method |
|---|---|---|
| Cancelling \(x\) from \(\frac{7x^4-2x^3+6}{x}\) | The \(6\) term does not contain \(x\). | Split into terms: \(7x^3-2x^2+\frac6x\). |
| Cancelling terms instead of factors | Terms joined by \(+\) or \(-\) are not individual cancellable factors. | Factorise first, then cancel whole common brackets. |
| Leaving \(\frac{x+2}{1}\) | It is not simplified final form. | Write \(x+2\). |
| Treating \(2-x\) as \(x-2\) | They differ by a factor of \(-1\). | Use \(2-x=-(x-2)\). |
| Forgetting missing terms | Columns shift and the division breaks. | Write \(0x^2\) or \(0x\) explicitly. |
| Dividing by the whole divisor at the divide step | Only the leading term is used at the divide step. | For \(x+5\), divide by \(x\). For \(2x-1\), divide by \(2x\). |
| Ignoring the constant in the multiply step | The whole divisor must be multiplied. | After finding \(6x^2\), multiply \(6x^2(x+5)\), not just \(6x^2\cdot x\). |
| Subtracting negatives incorrectly | This is a classic algebra error. | Write brackets: \(-7x-(-10x)=-7x+10x=3x\). |
| Saying \(x+3\) means test \(f(3)\) | Wrong sign. | \(x+3=x-(-3)\), so test \(f(-3)\). |
| Saying \(2x+1\) means test \(f(2)\) or \(f(1)\) | The factor is zero at \(x=-\frac12\). | Solve \(2x+1=0\). |
| Stopping at \(f(a)=0\) | The conclusion has not been stated. | Write: “Therefore, by the factor theorem, \(x-a\) is a factor.” |
| Treating a cross-board “not in spec” note as CCEA law | Specifications differ. | For CCEA, follow AS1-AF-LO011: remainder theorem is included. |

## Exam Technique Notes

### When asked to “divide”

Show the long division process unless a shorter method is clearly accepted.

End with either:

\[
\boxed{\text{quotient}}
\]

if the remainder is zero, or

\[
\boxed{\text{quotient}+\frac{\text{remainder}}{\text{divisor}}}
\]

if writing the division as an algebraic expression.

### When asked to “find the remainder”

You can use polynomial division or the remainder theorem. For CCEA, the efficient method is usually:

\[
\text{remainder}=f(a)
\]

when dividing by \(x-a\).

### When asked to “show that \(x-a\) is a factor”

Use the factor theorem:

\[
f(a)=0.
\]

Then write the conclusion:

\[
\therefore x-a\text{ is a factor of }f(x).
\]

### When asked to “fully factorise”

Do not stop after finding one factor. You need:

\[
\text{cubic}=(\text{linear factor})(\text{quadratic})
\]

then factorise the quadratic if possible:

\[
(\text{linear})(\text{linear})(\text{linear}).
\]

### Calculator use

A calculator table can help test values such as

\[
x=-3,-2,-1,0,1,2,3.
\]

But the exam solution still needs the algebraic statement:

\[
f(a)=0,\quad \therefore x-a\text{ is a factor}.
\]

## Full Worked Solutions

### 1. Simplify \(\frac{6x^3+9x^2}{3x}\)

\[
\frac{6x^3+9x^2}{3x}=\frac{6x^3}{3x}+\frac{9x^2}{3x}=2x^2+3x.
\]

Final answer:

\[
\boxed{2x^2+3x}.
\]

### 2. Simplify \(\frac{x^2-9}{x^2+3x}\)

\[
x^2-9=(x-3)(x+3),
\]

\[
x^2+3x=x(x+3).
\]

So

\[
\frac{x^2-9}{x^2+3x}=\frac{(x-3)(x+3)}{x(x+3)}=\frac{x-3}{x}.
\]

Final answer:

\[
\boxed{\frac{x-3}{x}}.
\]

### 3. Simplify \(\frac{x^2+5x+6}{x+2}\)

\[
x^2+5x+6=(x+2)(x+3).
\]

So

\[
\frac{x^2+5x+6}{x+2}=\frac{(x+2)(x+3)}{x+2}=x+3.
\]

Final answer:

\[
\boxed{x+3}.
\]

### 4. Simplify \(\frac{3x^2+13x+14}{x^2+6x+8}\)

\[
x^2+6x+8=(x+2)(x+4).
\]

\[
3x^2+13x+14=(3x+7)(x+2).
\]

So

\[
\frac{3x^2+13x+14}{x^2+6x+8}=\frac{(3x+7)(x+2)}{(x+2)(x+4)}=\frac{3x+7}{x+4}.
\]

Final answer:

\[
\boxed{\frac{3x+7}{x+4}}.
\]

### 5. Simplify \(\frac{9-x^2}{x^2+x-6}\)

\[
9-x^2=(3-x)(3+x),
\]

\[
x^2+x-6=(x+3)(x-2).
\]

Since \(3+x=x+3\),

\[
\frac{9-x^2}{x^2+x-6}=\frac{(3-x)(x+3)}{(x+3)(x-2)}=\frac{3-x}{x-2}.
\]

Because \(3-x=-(x-3)\), another valid form is

\[
-\frac{x-3}{x-2}.
\]

Final answer:

\[
\boxed{\frac{3-x}{x-2}}.
\]

### 6. Divide \(6x^3+28x^2-7x+15\) by \(x+5\)

From Core Theory B:

\[
\boxed{6x^2-2x+3}.
\]

### 7. Find the remainder when \(3x^3-2x+4\) is divided by \(x-1\)

Let

\[
f(x)=3x^3-2x+4.
\]

Since the divisor is \(x-1\), use \(x=1\).

\[
f(1)=3(1)^3-2(1)+4=3-2+4=5.
\]

Remainder:

\[
\boxed{5}.
\]

### 8. Find the remainder when \(2x^3-5x^2-16x+10\) is divided by \(x-4\)

Let

\[
f(x)=2x^3-5x^2-16x+10.
\]

Since the divisor is \(x-4\), use \(x=4\).

\[
f(4)=2(4)^3-5(4)^2-16(4)+10.
\]

\[
f(4)=128-80-64+10=-6.
\]

Remainder:

\[
\boxed{-6}.
\]

### 9. Divide \(8x^3-1\) by \(2x-1\)

Write missing terms:

\[
8x^3-1=8x^3+0x^2+0x-1.
\]

From Core Theory E:

\[
\frac{8x^3-1}{2x-1}=4x^2+2x+1.
\]

Final answer:

\[
\boxed{4x^2+2x+1}.
\]

### 10. Write \(\frac{3x^3-2x+4}{x-1}\) in quotient plus remainder form

The quotient is \(3x^2+3x+1\) and the remainder is \(5\), so

\[
\boxed{\frac{3x^3-2x+4}{x-1}=3x^2+3x+1+\frac5{x-1}}.
\]

### 11. Show that \(x-2\) is a factor of \(x^3+x^2-4x-4\)

Let

\[
f(x)=x^3+x^2-4x-4.
\]

Test \(x=2\):

\[
f(2)=2^3+2^2-4(2)-4=8+4-8-4=0.
\]

Therefore, by the factor theorem,

\[
\boxed{x-2\text{ is a factor of }x^3+x^2-4x-4}.
\]

### 12. Fully factorise \(2x^3+x^2-18x-9\)

Let

\[
f(x)=2x^3+x^2-18x-9.
\]

Test \(x=3\):

\[
f(3)=2(3)^3+(3)^2-18(3)-9=54+9-54-9=0.
\]

Therefore, by the factor theorem, \(x-3\) is a factor.

Divide by \(x-3\):

\[
2x^3+x^2-18x-9=(x-3)(2x^2+7x+3).
\]

Now factorise:

\[
2x^2+7x+3=(2x+1)(x+3).
\]

Therefore

\[
\boxed{2x^3+x^2-18x-9=(x-3)(2x+1)(x+3)}.
\]

### 13. Given \(2x+1\) is a factor of \(6x^3+ax^2+1\), find \(a\)

Let

\[
f(x)=6x^3+ax^2+1.
\]

Since

\[
2x+1=0,
\]

\[
x=-\frac12.
\]

Because \(2x+1\) is a factor,

\[
f\!\left(-\frac12\right)=0.
\]

\[
6\left(-\frac12\right)^3+a\left(-\frac12\right)^2+1=0.
\]

\[
6\left(-\frac18\right)+a\left(\frac14\right)+1=0.
\]

\[
-\frac34+\frac14a+1=0.
\]

\[
\frac14+\frac14a=0.
\]

\[
\frac14a=-\frac14.
\]

\[
a=-1.
\]

Final answer:

\[
\boxed{a=-1}.
\]

### 14. Given \(3x-1\) is a factor of \(3x^3+11x^2+ax+1\), find \(a\)

Let

\[
f(x)=3x^3+11x^2+ax+1.
\]

Since

\[
3x-1=0,
\]

\[
x=\frac13.
\]

Because \(3x-1\) is a factor,

\[
f\!\left(\frac13\right)=0.
\]

\[
3\left(\frac13\right)^3+11\left(\frac13\right)^2+a\left(\frac13\right)+1=0.
\]

\[
3\left(\frac1{27}\right)+11\left(\frac19\right)+\frac13a+1=0.
\]

\[
\frac19+\frac{11}{9}+\frac13a+1=0.
\]

\[
\frac{12}{9}+\frac13a+1=0.
\]

\[
\frac43+\frac13a+1=0.
\]

\[
\frac43+\frac33+\frac13a=0.
\]

\[
\frac73+\frac13a=0.
\]

\[
\frac13a=-\frac73.
\]

\[
a=-7.
\]

Final answer:

\[
\boxed{a=-7}.
\]

### 15. Find the remainder when \(f(x)=4x^3-7x+2\) is divided by \(x+2\)

Since

\[
x+2=x-(-2),
\]

use \(x=-2\).

\[
f(-2)=4(-2)^3-7(-2)+2.
\]

\[
(-2)^3=-8.
\]

So

\[
f(-2)=4(-8)+14+2=-32+14+2=-16.
\]

Remainder:

\[
\boxed{-16}.
\]

## Common CCEA-Style Wording

| Question wording | What to do |
|---|---|
| “Divide \(P(x)\) by \(x-a\)” | Use polynomial long division and give quotient, with remainder if needed. |
| “Find the remainder when \(P(x)\) is divided by \(x-a\)” | Use \(P(a)\). |
| “Show that \(x-a\) is a factor” | Show \(P(a)=0\), then state the factor theorem conclusion. |
| “Given that \(ax+b\) is a factor...” | Solve \(ax+b=0\), substitute that \(x\)-value, set equal to zero. |
| “Fully factorise” | Find one linear factor, divide, then factorise the remaining quadratic. |
| “Solve \(P(x)=0\)” after factorising | Set each factor equal to zero and solve. |

## Syllabus Gap Check

| LO ID | Covered? | Evidence-backed coverage |
|---|---|---|
| AS1-AF-LO010 | Yes | Expanding, factorisation, algebraic fractions and simple algebraic division by linear expressions. |
| AS1-AF-LO011 | Yes | Remainder theorem, factor theorem, cubic factorisation and unknown coefficients. |

### Excluded from core

| Item | Reason |
|---|---|
| Division by quadratic expressions | CCEA AS1 boundary for algebraic division is linear expression only. |
| Difference of two cubes identity as a required method | Evidence marks it as not required; long division provides an on-spec route. |
| MAT/extension examples | Useful enrichment but not core CCEA AS1 lesson content. |
| Proof by deduction chapter material | Belongs in a separate Chapter 7B proof lesson. |
| Cross-board “remainder theorem no longer in spec” warning | Not applicable to CCEA because AS1-AF-LO011 includes remainder theorem. |

## Visual and Interactive Asset Plan

| Asset ID | Type | Purpose | File |
|---|---|---|---|
| AS1AlgebraicMethodsMER-001 | Mermaid | Decision flow for simplifying, dividing, using remainder theorem and using factor theorem | mermaid/AS1AlgebraicMethodsMER-001.md |
| AS1AlgebraicMethodsSVG-001 | SVG | Algebraic fraction factorise-then-cancel flow | svg/AS1AlgebraicMethodsSVG-001.svg |
| AS1AlgebraicMethodsSVG-002 | SVG | Polynomial long division layout | svg/AS1AlgebraicMethodsSVG-002.svg |
| AS1AlgebraicMethodsTikZ-001 | TikZ | Printable polynomial long division diagram | tikz/AS1AlgebraicMethodsTikZ-001.tex |
| AS1AlgebraicMethodsTikZ-002 | TikZ | Remainder/factor theorem decision card | tikz/AS1AlgebraicMethodsTikZ-002.tex |
| AS1AlgebraicMethodsWidget-001 | HTML widget | Factor theorem value tester | widgets/AS1AlgebraicMethodsWidget-001.html |
| AS1AlgebraicMethodsWidget-002 | HTML widget | Remainder theorem substitution checker | widgets/AS1AlgebraicMethodsWidget-002.html |

## Supplementary Sources Used

No external web sources were used.

The Dr Frost lesson materials are treated as lesson evidence. Cross-board references inside those materials are used only where the CCEA specification confirms the mathematical skill is on-spec.

## Final Student Checklist

Before moving on, make sure you can:

- [ ] simplify algebraic fractions only after factorising;
- [ ] explain why terms cannot be cancelled unless they are common factors;
- [ ] handle \(2-x=-(x-2)\);
- [ ] set up polynomial long division with powers of \(x\) in columns;
- [ ] include missing terms such as \(0x^2\) and \(0x\);
- [ ] subtract negative terms safely;
- [ ] write quotient plus remainder form;
- [ ] use the remainder theorem to find remainders quickly;
- [ ] use the factor theorem to prove a factor;
- [ ] fully factorise a cubic after finding one factor;
- [ ] find unknown coefficients from a given factor;
- [ ] write the final factor theorem conclusion in words.
