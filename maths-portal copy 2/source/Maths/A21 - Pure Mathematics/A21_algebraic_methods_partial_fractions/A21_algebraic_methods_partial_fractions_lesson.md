# A21 Algebraic Methods: Partial Fractions

## Title and Metadata

| Field | Value |
|---|---|
| Course | CCEA GCE Mathematics |
| Unit | A21: A2 1 Pure Mathematics |
| Topic code | A21-AF |
| Topic area | Algebra and functions |
| Lesson | Algebraic Methods: Partial Fractions |
| Lesson file | `A21_algebraic_methods_partial_fractions_lesson.md` |
| Core LO IDs | A21-AF-LO001, A21-AF-LO008 |
| Forward link | A21-INT-LO005 |
| Status | Complete lesson pack |

## Evidence Map

| Evidence source | Used for |
|---|---|
| CCEA specification map | Unit, topic code, official LO IDs, syllabus boundary |
| README module map | Metadata and lesson file structure |
| Evidence checklist | Missing evidence, visual placeholder and off-spec logging |
| Dr Frost P2 Chapter 1 PDF | Slide-level examples and warnings |
| Chapter 1b transcript | Main explanatory sequence and worked-method detail |
| Screenshots PDF | Visual placeholder planning only, because no parsed text is available |

## Specification Alignment

### A21-AF-LO001

**Official learning outcome:** simplify rational expressions, including by factorising and cancelling, and algebraic division.

This lesson covers this through:

- factorising denominators before simplifying algebraic fractions;
- cancelling only common factors, not terms;
- using quotient and remainder form;
- recognising improper algebraic fractions;
- doing algebraic division before partial fractions when needed.

### A21-AF-LO008

**Official learning outcome:** decompose rational functions into partial fractions, with denominators not more complicated than squared linear terms.

This lesson covers this through:

- distinct linear factors;
- repeated squared linear factors;
- improper rational functions with linear-factor denominators;
- substitution method;
- comparing coefficients;
- one-identity method for improper partial fractions.

## Learning Objectives

By the end of the lesson, the student should be able to:

1. simplify algebraic fractions safely by factorising and cancelling common factors;
2. explain why cancelling terms is illegal unless a common factor divides the whole numerator and denominator;
3. decompose a proper rational function with distinct linear factors into partial fractions;
4. choose useful substitution values that make brackets disappear;
5. use comparing coefficients when substitution alone is not enough;
6. set up partial fractions with a repeated squared linear factor;
7. recognise an improper algebraic fraction by comparing degrees;
8. use algebraic division or a single identity before completing improper partial fractions.

## Prerequisite Recap

No GCSE source is used as authority here. The prerequisite recap is included only because the A-Level evidence itself begins by revising fraction operations.

### Fraction operations used in this lesson

If the denominators already match, only the numerators combine:

\[
\frac{a}{b}+\frac{c}{b}
=
\frac{a+c}{b}
\]

\[
\frac{a}{b}-\frac{c}{b}
=
\frac{a-c}{b}
\]

If the denominators do not match, use a common denominator:

\[
\frac{a}{b}+\frac{c}{d}
=
\frac{ad+bc}{bd}
\]

\[
\frac{a}{b}-\frac{c}{d}
=
\frac{ad-bc}{bd}
\]

For multiplication:

\[
\frac{a}{b}\times\frac{c}{d}
=
\frac{ac}{bd}
\]

For division, multiply by the reciprocal:

\[
\frac{a}{b}\div\frac{c}{d}
=
\frac{a}{b}\times\frac{d}{c}
=
\frac{ad}{bc}
\]

### The cancellation rule

Cancellation means **dividing the numerator and denominator by the same common factor**.

So:

\[
\frac{ab}{bc}
=
\frac{a}{c}
\]

because both numerator and denominator have a common factor \(b\).

But:

\[
\frac{ac+ab}{b}
\ne ac+a
\]

because \(b\) does not divide every term in the numerator as a common factor of the whole numerator.

A numerical check shows the danger:

\[
\frac{3\cdot 2+3\cdot 4}{4}
=
\frac{6+12}{4}
=
\frac{18}{4}
=
\frac{9}{2}
\]

The illegal cancellation would give:

\[
3\cdot 2+3=9
\]

which is not equal to \(\frac92\). The transcript explicitly warns that cancelling only works when everything required is being divided as a common factor, not when a student snips a term out of a sum.

## Big Picture Explanation

Partial fractions are algebraic unpacking. A rational function that looks like one complicated fraction can often be rewritten as a sum of simpler fractions.

That matters because later in A2 Pure, especially in integration, smaller fractions are easier to differentiate, integrate, transform, or analyse. The transcript describes partial fractions as a skill or tool that helps access later mathematics, especially functions, differentiation and integration.

The core CCEA boundary is precise:

\[
\text{denominators not more complicated than squared linear terms.}
\]

So this lesson stays inside:

\[
(x-a)(x-b), \qquad (x-a)^2(x-b), \qquad (x-a)^2
\]

and does not make cubed repeated factors or irreducible quadratics part of the required core.

## Key Definitions and Notation

### Rational expression

A rational expression is a fraction where the numerator and denominator are algebraic expressions, usually polynomials:

\[
\frac{P(x)}{Q(x)}
\]

where \(Q(x)\ne 0\).

### Proper algebraic fraction

An algebraic fraction is **proper** when:

\[
\deg(\text{numerator}) < \deg(\text{denominator})
\]

Example:

\[
\frac{6x-2}{(x-3)(x+1)}
\]

The numerator has degree \(1\). The denominator has degree \(2\). So it is proper.

### Improper algebraic fraction

An algebraic fraction is **improper** when:

\[
\deg(\text{numerator}) \geq \deg(\text{denominator})
\]

The slide evidence states that an algebraic fraction is improper if the degree of the numerator is at least the degree of the denominator, and that a fraction is still improper when the degrees are the same.

Example:

\[
\frac{3x^2-3x-2}{(x-1)(x-2)}
\]

The numerator has degree \(2\). The denominator also has degree \(2\). So this is improper.

### Identity symbol

The symbol

\[
\equiv
\]

means **identically equal** or **equivalent for all allowed values of \(x\)**.

For example:

\[
3x+4\equiv ax+b
\]

means:

\[
a=3,\qquad b=4
\]

The PDF slide notes that \(\equiv\) indicates both sides are equal for all values of \(x\).

### Partial fractions

If the denominator is a product of linear terms, it can be split into partial fractions where each denominator is a single linear term:

\[
\frac{6x-2}{(x-3)(x+1)}
\equiv
\frac{A}{x-3}+\frac{B}{x+1}
\]

The constants \(A\) and \(B\) are found using substitution, comparing coefficients, or a mixture of both.

## Core Theory

## 1. Algebraic fractions before partial fractions

Partial fractions depend on the ability to combine and simplify algebraic fractions. This is the bridge-skill inside A-Level algebra.

### Example: simplify an algebraic fraction expression

Express as a single fraction in its simplest form:

\[
\frac{3x+5}{x^2+x-12}-\frac{2}{x-3}
\]

First factorise:

\[
x^2+x-12=(x-3)(x+4)
\]

So:

\[
\frac{3x+5}{x^2+x-12}-\frac{2}{x-3}
=
\frac{3x+5}{(x-3)(x+4)}-\frac{2}{x-3}
\]

The second fraction needs denominator \((x-3)(x+4)\), so multiply top and bottom by \(x+4\):

\[
\frac{2}{x-3}
=
\frac{2(x+4)}{(x-3)(x+4)}
\]

Now subtract:

\[
\frac{3x+5}{(x-3)(x+4)}
-
\frac{2(x+4)}{(x-3)(x+4)}
=
\frac{3x+5-2(x+4)}{(x-3)(x+4)}
\]

Expand the numerator carefully:

\[
3x+5-2(x+4)
=
3x+5-2x-8
\]

\[
=
x-3
\]

So:

\[
\frac{3x+5-2(x+4)}{(x-3)(x+4)}
=
\frac{x-3}{(x-3)(x+4)}
\]

Now cancel the common factor \(x-3\):

\[
\frac{x-3}{(x-3)(x+4)}
=
\frac{1}{x+4}
\]

Final answer:

\[
\boxed{\frac{1}{x+4}}
\]

Important: the subtraction applies to the whole expression \(2(x+4)\), not just the first term. The transcript highlights this as a common place where students lose the sign on the second term.

## 2. Simple partial fractions with distinct linear factors

### General form

If the denominator has two distinct linear factors:

\[
\frac{px+q}{(x-a)(x-b)}
\]

then write:

\[
\frac{px+q}{(x-a)(x-b)}
\equiv
\frac{A}{x-a}
+
\frac{B}{x-b}
\]

Then multiply through by the full denominator:

\[
px+q
\equiv
A(x-b)+B(x-a)
\]

Now find \(A\) and \(B\).

### Worked Example 1: substitution method

Express in partial fractions:

\[
\frac{6x-2}{(x-3)(x+1)}
\]

Start with the template:

\[
\frac{6x-2}{(x-3)(x+1)}
\equiv
\frac{A}{x-3}+\frac{B}{x+1}
\]

Multiply both sides by \((x-3)(x+1)\):

\[
6x-2
\equiv
A(x+1)+B(x-3)
\]

Choose \(x=3\), because this makes \(x-3=0\):

\[
6(3)-2
=
A(3+1)+B(3-3)
\]

\[
18-2
=
4A+B(0)
\]

\[
16=4A
\]

\[
A=4
\]

Choose \(x=-1\), because this makes \(x+1=0\):

\[
6(-1)-2
=
A(-1+1)+B(-1-3)
\]

\[
-6-2
=
A(0)+B(-4)
\]

\[
-8=-4B
\]

\[
B=2
\]

Therefore:

\[
\frac{6x-2}{(x-3)(x+1)}
\equiv
\frac{4}{x-3}
+
\frac{2}{x+1}
\]

Final answer:

\[
\boxed{
\frac{6x-2}{(x-3)(x+1)}
\equiv
\frac{4}{x-3}
+
\frac{2}{x+1}
}
\]

The PDF shows the same example using substitution and comparing coefficients.

### Worked Example 2: comparing coefficients

Use the same identity:

\[
6x-2
\equiv
A(x+1)+B(x-3)
\]

Expand the right-hand side:

\[
A(x+1)+B(x-3)
=
Ax+A+Bx-3B
\]

Collect like terms:

\[
Ax+Bx+A-3B
=
(A+B)x+(A-3B)
\]

So:

\[
6x-2
\equiv
(A+B)x+(A-3B)
\]

Compare coefficients of \(x\):

\[
A+B=6
\]

Compare constant terms:

\[
A-3B=-2
\]

Solve simultaneously.

From:

\[
A+B=6
\]

\[
A=6-B
\]

Substitute into:

\[
A-3B=-2
\]

\[
(6-B)-3B=-2
\]

\[
6-4B=-2
\]

\[
-4B=-8
\]

\[
B=2
\]

Then:

\[
A+B=6
\]

\[
A+2=6
\]

\[
A=4
\]

So:

\[
\boxed{
\frac{6x-2}{(x-3)(x+1)}
\equiv
\frac{4}{x-3}
+
\frac{2}{x+1}
}
\]

## 3. Repeated linear factors

A repeated linear factor is a factor such as:

\[
(x+1)^2
\]

The transcript explains that if a repeated factor appears, writing the same denominator twice is not enough:

\[
\frac{2x+1}{(x+1)^2}
\not\equiv
\frac{A}{x+1}+\frac{B}{x+1}
\]

because the right-hand side would combine to:

\[
\frac{A+B}{x+1}
\]

and the denominator would not be squared.

Instead, use both the non-squared and squared versions:

\[
\frac{2x+1}{(x+1)^2}
\equiv
\frac{A}{x+1}
+
\frac{B}{(x+1)^2}
\]

The transcript states the key twist: for a repeated linear factor, use both the linear version and the quadratic version of the factor.

### General repeated-factor template

For:

\[
\frac{P(x)}{(x-a)^2(x-b)}
\]

write:

\[
\frac{P(x)}{(x-a)^2(x-b)}
\equiv
\frac{A}{x-a}
+
\frac{B}{(x-a)^2}
+
\frac{C}{x-b}
\]

CCEA requires denominators no more complicated than squared linear terms, so this squared repeated-factor case is core. Cubed repeated factors are not core here.

### Worked Example 3: repeated linear factor

Split into partial fractions:

\[
\frac{11x^2+14x+5}{(x+1)^2(2x+1)}
\]

Set up the repeated-factor template:

\[
\frac{11x^2+14x+5}{(x+1)^2(2x+1)}
\equiv
\frac{A}{x+1}
+
\frac{B}{(x+1)^2}
+
\frac{C}{2x+1}
\]

Multiply through by the full denominator \((x+1)^2(2x+1)\):

\[
11x^2+14x+5
\equiv
A(x+1)(2x+1)+B(2x+1)+C(x+1)^2
\]

Use \(x=-1\), because it makes \(x+1=0\):

\[
11(-1)^2+14(-1)+5
=
A(0)(-1)+B(2(-1)+1)+C(0)^2
\]

\[
11-14+5
=
0+B(-1)+0
\]

\[
2=-B
\]

\[
B=-2
\]

Use \(x=-\frac12\), because it makes \(2x+1=0\):

\[
11\left(-\frac12\right)^2
+
14\left(-\frac12\right)
+
5
=
A\left(\frac12\right)(0)
+
B(0)
+
C\left(\frac12\right)^2
\]

\[
11\cdot\frac14-7+5
=
\frac14 C
\]

\[
\frac{11}{4}-2
=
\frac14 C
\]

\[
\frac{11}{4}-\frac{8}{4}
=
\frac14 C
\]

\[
\frac34
=
\frac14 C
\]

\[
C=3
\]

Now compare the coefficient of \(x^2\).

First expand only the parts needed for the \(x^2\) coefficient:

\[
A(x+1)(2x+1)
=
A(2x^2+3x+1)
\]

so it contributes \(2A\) to the \(x^2\) coefficient.

\[
B(2x+1)
\]

contributes no \(x^2\) term.

\[
C(x+1)^2
=
C(x^2+2x+1)
\]

contributes \(C\) to the \(x^2\) coefficient.

Therefore:

\[
11=2A+C
\]

Substitute \(C=3\):

\[
11=2A+3
\]

\[
8=2A
\]

\[
A=4
\]

So:

\[
\boxed{
\frac{11x^2+14x+5}{(x+1)^2(2x+1)}
\equiv
\frac{4}{x+1}
-
\frac{2}{(x+1)^2}
+
\frac{3}{2x+1}
}
\]

The PDF repeated-factor slide uses this structure and explains that the problem is resolved by having the factor both squared and non-squared.

## 4. Improper algebraic fractions

An algebraic fraction is improper when:

\[
\deg(\text{numerator})\geq \deg(\text{denominator})
\]

If a fraction is improper, do algebraic division first.

The transcript gives the exam-useful rule:

\[
\text{If it is improper, do algebraic division. If it is not improper, just do partial fractions.}
\]

It also notes that this becomes especially important later because integration questions may not tell you that partial fractions are needed.

### Quotient and remainder form

Just as:

\[
7\div 3=2\text{ remainder }1
\]

we can write:

\[
\frac{7}{3}=2+\frac13
\]

Similarly:

\[
\frac{f(x)}{d(x)}
=
q(x)+\frac{r(x)}{d(x)}
\]

where:

- \(d(x)\) is the divisor;
- \(q(x)\) is the quotient;
- \(r(x)\) is the remainder.

### Worked Example 4: quotient and remainder

Write:

\[
\frac{x^2+5x-9}{x+2}
\]

in the form:

\[
Ax+B+\frac{C}{x+2}
\]

Divide \(x^2+5x-9\) by \(x+2\).

First term:

\[
\frac{x^2}{x}=x
\]

Multiply:

\[
x(x+2)=x^2+2x
\]

Subtract:

\[
(x^2+5x-9)-(x^2+2x)
=
3x-9
\]

Next term:

\[
\frac{3x}{x}=3
\]

Multiply:

\[
3(x+2)=3x+6
\]

Subtract:

\[
(3x-9)-(3x+6)
=
-15
\]

So the quotient is:

\[
x+3
\]

and the remainder is:

\[
-15
\]

Therefore:

\[
\frac{x^2+5x-9}{x+2}
=
x+3-\frac{15}{x+2}
\]

So:

\[
\boxed{A=1,\quad B=3,\quad C=-15}
\]

## 5. Improper partial fractions

There are two methods:

1. algebraic division first, then partial fractions;
2. one identity containing the quotient and the partial fractions together.

Both are on-spec when they stay within the squared-linear-factor boundary.

### Worked Example 5: improper partial fractions by algebraic division

Split into partial fractions:

\[
\frac{3x^2-3x-2}{(x-1)(x-2)}
\]

First expand the denominator:

\[
(x-1)(x-2)
=
x^2-3x+2
\]

So:

\[
\frac{3x^2-3x-2}{(x-1)(x-2)}
=
\frac{3x^2-3x-2}{x^2-3x+2}
\]

This is improper because both numerator and denominator have degree \(2\).

Divide:

\[
3x^2-3x-2
\div
(x^2-3x+2)
\]

First term:

\[
\frac{3x^2}{x^2}=3
\]

Multiply:

\[
3(x^2-3x+2)
=
3x^2-9x+6
\]

Subtract:

\[
(3x^2-3x-2)-(3x^2-9x+6)
\]

\[
=
3x^2-3x-2-3x^2+9x-6
\]

\[
=
6x-8
\]

So:

\[
\frac{3x^2-3x-2}{x^2-3x+2}
=
3+\frac{6x-8}{x^2-3x+2}
\]

Return the denominator to factorised form:

\[
3+\frac{6x-8}{(x-1)(x-2)}
\]

Now split:

\[
\frac{6x-8}{(x-1)(x-2)}
\equiv
\frac{A}{x-1}
+
\frac{B}{x-2}
\]

Multiply through:

\[
6x-8
\equiv
A(x-2)+B(x-1)
\]

Use \(x=2\):

\[
6(2)-8
=
A(0)+B(1)
\]

\[
12-8=B
\]

\[
B=4
\]

Use \(x=1\):

\[
6(1)-8
=
A(1-2)+B(0)
\]

\[
-2=-A
\]

\[
A=2
\]

Therefore:

\[
\frac{6x-8}{(x-1)(x-2)}
\equiv
\frac{2}{x-1}
+
\frac{4}{x-2}
\]

So the full answer is:

\[
\boxed{
\frac{3x^2-3x-2}{(x-1)(x-2)}
\equiv
3+
\frac{2}{x-1}
+
\frac{4}{x-2}
}
\]

The transcript and PDF both present this example, with algebraic division producing \(3+\frac{6x-8}{(x-1)(x-2)}\), followed by partial fractions.

### Worked Example 6: improper partial fractions using one identity

Use the same fraction:

\[
\frac{3x^2-3x-2}{(x-1)(x-2)}
\]

Because the numerator and denominator have the same degree, the quotient part is a constant.

So write:

\[
\frac{3x^2-3x-2}{(x-1)(x-2)}
\equiv
A+\frac{B}{x-1}+\frac{C}{x-2}
\]

Multiply through by \((x-1)(x-2)\):

\[
3x^2-3x-2
\equiv
A(x-1)(x-2)+B(x-2)+C(x-1)
\]

Compare coefficients of \(x^2\).

Since:

\[
(x-1)(x-2)=x^2-3x+2
\]

the only \(x^2\) term on the right comes from:

\[
A(x-1)(x-2)
\]

So:

\[
A=3
\]

Use \(x=1\):

\[
3(1)^2-3(1)-2
=
A(0)(-1)+B(1-2)+C(0)
\]

\[
3-3-2
=
-B
\]

\[
-2=-B
\]

\[
B=2
\]

Use \(x=2\):

\[
3(2)^2-3(2)-2
=
A(1)(0)+B(0)+C(1)
\]

\[
12-6-2=C
\]

\[
4=C
\]

Therefore:

\[
\boxed{
\frac{3x^2-3x-2}{(x-1)(x-2)}
\equiv
3+\frac{2}{x-1}+\frac{4}{x-2}
}
\]

The transcript notes that this one identity method is often efficient and that mark schemes may present it as the standard method.

## Visual Asset Integration

[VISUAL PLACEHOLDER: A21AlgebraicMethodsPartialFractionsMermaid-001 | Source: CCEA specification map + transcript | Insert from mermaid/A21AlgebraicMethodsPartialFractionsMermaid-001.md | Purpose: Flowchart for choosing between proper partial fractions, repeated linear factors and improper fractions.]

[VISUAL PLACEHOLDER: A21AlgebraicMethodsPartialFractionsSVG-001 | Source: transcript and PDF slide examples | Insert from svg/A21AlgebraicMethodsPartialFractionsSVG-001.svg | Purpose: Partial-fractions template table for distinct, repeated and improper cases.]

[VISUAL PLACEHOLDER: A21AlgebraicMethodsPartialFractionsSVG-002 | Source: transcript warning on illegal cancellation | Insert from svg/A21AlgebraicMethodsPartialFractionsSVG-002.svg | Purpose: Show legal cancellation by common factor versus illegal cancellation inside a sum.]

[VISUAL PLACEHOLDER: A21AlgebraicMethodsPartialFractionsTikZ-001 | Source: transcript and PDF improper fraction examples | Insert from tikz/A21AlgebraicMethodsPartialFractionsTikZ-001.tex | Purpose: Algebraic division layout for quotient and remainder.]

[INTERACTIVE PLACEHOLDER: A21AlgebraicMethodsPartialFractionsWidget-001 | Source: transcript methods for substitution and comparing coefficients | Insert from widgets/A21AlgebraicMethodsPartialFractionsWidget-001.html | Purpose: Let students choose substitution values and compare coefficients for partial fractions.]

## Guided Practice

### Question 1

Express in partial fractions:

\[
\frac{5x+7}{(x+2)(x-1)}
\]

### Question 2

Express in partial fractions:

\[
\frac{8x+3}{(x-2)^2(x+1)}
\]

### Question 3

Express in partial fractions:

\[
\frac{2x^2+x+5}{(x+1)(x-3)}
\]

## Common Mistakes and Exam Traps

### Trap 1: Cancelling terms instead of factors

Wrong:

\[
\frac{x^2+x}{x}
=
x^2+1
\]

Correct:

\[
\frac{x^2+x}{x}
=
\frac{x(x+1)}{x}
=
x+1
\]

Cancellation is division by a common factor.

### Trap 2: Forgetting brackets after a subtraction

Wrong:

\[
3x+5-2(x+4)
=
3x+5-2x+8
\]

Correct:

\[
3x+5-2(x+4)
=
3x+5-2x-8
\]

### Trap 3: Missing the repeated-factor template

Wrong:

\[
\frac{P(x)}{(x+1)^2(2x+1)}
\equiv
\frac{A}{(x+1)^2}
+
\frac{B}{2x+1}
\]

Correct:

\[
\frac{P(x)}{(x+1)^2(2x+1)}
\equiv
\frac{A}{x+1}
+
\frac{B}{(x+1)^2}
+
\frac{C}{2x+1}
\]

### Trap 4: Forgetting to check whether the fraction is improper

If:

\[
\deg(\text{numerator})\geq \deg(\text{denominator})
\]

then you must include a quotient part.

For example:

\[
\frac{3x^2-3x-2}{(x-1)(x-2)}
\]

cannot be written only as:

\[
\frac{A}{x-1}+\frac{B}{x-2}
\]

because it is improper.

It needs:

\[
A+\frac{B}{x-1}+\frac{C}{x-2}
\]

or algebraic division first.

## Exam Technique Notes

1. **Always factorise the denominator first.**  
   It often reveals the intended partial-fractions structure.

2. **Check the degrees before doing anything else.**  
   If the fraction is improper, divide first or include the quotient in one identity.

3. **Use substitution values that make factors zero.**  
   For \(x-3\), use \(x=3\).  
   For \(x+1\), use \(x=-1\).  
   For \(2x+1\), use \(x=-\frac12\).

4. **If substitution does not finish the problem, compare coefficients.**  
   This is especially useful with repeated factors.

5. **Use \(\equiv\), not just \(=\), when setting up identities.**  
   It signals that the equality is true for all allowed \(x\), so coefficients can be compared.

6. **Keep the quotient separate in improper cases.**  
   The quotient is not part of the partial fraction denominators.

## Full Worked Solutions

### Solution to Question 1

\[
\frac{5x+7}{(x+2)(x-1)}
\equiv
\frac{A}{x+2}+\frac{B}{x-1}
\]

Multiply through by \((x+2)(x-1)\):

\[
5x+7
\equiv
A(x-1)+B(x+2)
\]

Use \(x=1\):

\[
5(1)+7
=
A(0)+B(3)
\]

\[
12=3B
\]

\[
B=4
\]

Use \(x=-2\):

\[
5(-2)+7
=
A(-3)+B(0)
\]

\[
-10+7=-3A
\]

\[
-3=-3A
\]

\[
A=1
\]

Therefore:

\[
\boxed{
\frac{5x+7}{(x+2)(x-1)}
\equiv
\frac{1}{x+2}+\frac{4}{x-1}
}
\]

### Solution to Question 2

\[
\frac{8x+3}{(x-2)^2(x+1)}
\equiv
\frac{A}{x-2}
+
\frac{B}{(x-2)^2}
+
\frac{C}{x+1}
\]

Multiply through by \((x-2)^2(x+1)\):

\[
8x+3
\equiv
A(x-2)(x+1)+B(x+1)+C(x-2)^2
\]

Use \(x=2\):

\[
8(2)+3
=
A(0)(3)+B(3)+C(0)^2
\]

\[
19=3B
\]

\[
B=\frac{19}{3}
\]

Use \(x=-1\):

\[
8(-1)+3
=
A(-3)(0)+B(0)+C(-3)^2
\]

\[
-8+3=9C
\]

\[
-5=9C
\]

\[
C=-\frac59
\]

Now compare coefficients of \(x^2\).

Expand only the \(x^2\) parts:

\[
A(x-2)(x+1)=A(x^2-x-2)
\]

so it contributes \(A\) to the \(x^2\) coefficient.

\[
C(x-2)^2=C(x^2-4x+4)
\]

so it contributes \(C\) to the \(x^2\) coefficient.

The left-hand side \(8x+3\) has no \(x^2\) term, so its \(x^2\) coefficient is \(0\).

Thus:

\[
0=A+C
\]

\[
A=-C
\]

Since:

\[
C=-\frac59
\]

we get:

\[
A=\frac59
\]

Therefore:

\[
\boxed{
\frac{8x+3}{(x-2)^2(x+1)}
\equiv
\frac{\frac59}{x-2}
+
\frac{\frac{19}{3}}{(x-2)^2}
-
\frac{\frac59}{x+1}
}
\]

Equivalently:

\[
\boxed{
\frac{8x+3}{(x-2)^2(x+1)}
\equiv
\frac{5}{9(x-2)}
+
\frac{19}{3(x-2)^2}
-
\frac{5}{9(x+1)}
}
\]

### Solution to Question 3

\[
\frac{2x^2+x+5}{(x+1)(x-3)}
\]

First check the degree.

The numerator has degree \(2\). The denominator has degree \(2\), because:

\[
(x+1)(x-3)=x^2-2x-3
\]

So the fraction is improper.

Divide:

\[
2x^2+x+5
\div
(x^2-2x-3)
\]

First term:

\[
\frac{2x^2}{x^2}=2
\]

Multiply:

\[
2(x^2-2x-3)
=
2x^2-4x-6
\]

Subtract:

\[
(2x^2+x+5)-(2x^2-4x-6)
\]

\[
=
2x^2+x+5-2x^2+4x+6
\]

\[
=
5x+11
\]

So:

\[
\frac{2x^2+x+5}{(x+1)(x-3)}
=
2+\frac{5x+11}{(x+1)(x-3)}
\]

Now decompose:

\[
\frac{5x+11}{(x+1)(x-3)}
\equiv
\frac{A}{x+1}
+
\frac{B}{x-3}
\]

Multiply through:

\[
5x+11
\equiv
A(x-3)+B(x+1)
\]

Use \(x=3\):

\[
5(3)+11
=
A(0)+B(4)
\]

\[
15+11=4B
\]

\[
26=4B
\]

\[
B=\frac{13}{2}
\]

Use \(x=-1\):

\[
5(-1)+11
=
A(-4)+B(0)
\]

\[
-5+11=-4A
\]

\[
6=-4A
\]

\[
A=-\frac32
\]

Therefore:

\[
\frac{5x+11}{(x+1)(x-3)}
\equiv
-\frac{3}{2(x+1)}
+
\frac{13}{2(x-3)}
\]

So:

\[
\boxed{
\frac{2x^2+x+5}{(x+1)(x-3)}
\equiv
2-\frac{3}{2(x+1)}
+
\frac{13}{2(x-3)}
}
\]

## Common CCEA-Style Wording

Expect wording such as:

- “Express as partial fractions.”
- “Decompose into partial fractions.”
- “Find the values of the constants \(A\), \(B\) and \(C\).”
- “Given that \(\cdots\equiv\cdots\), find the constants.”
- “Express as a quotient and a remainder.”
- “Hence integrate…” later in A21 Integration, but that is a forward link, not this lesson’s core.

## Syllabus Gap Check

| Requirement | Covered? | Evidence |
|---|---:|---|
| A21-AF-LO001 rational simplification | Yes | Algebraic fraction simplification and improper fraction division |
| A21-AF-LO001 algebraic division | Yes | Quotient and remainder examples |
| A21-AF-LO008 distinct linear factors | Yes | \(\frac{6x-2}{(x-3)(x+1)}\) |
| A21-AF-LO008 repeated squared linear factors | Yes | \(\frac{11x^2+14x+5}{(x+1)^2(2x+1)}\) |
| A21-AF-LO008 improper rational functions | Yes | \(\frac{3x^2-3x-2}{(x-1)(x-2)}\) |
| Denominators beyond squared linear terms | Excluded | Outside supplied CCEA boundary |
| Integration using partial fractions | Forward link only | A21-INT-LO005 |

## Visual and Interactive Asset Plan

| Asset ID | Type | Purpose |
|---|---|---|
| A21AlgebraicMethodsPartialFractionsMermaid-001 | Mermaid | Decision flowchart |
| A21AlgebraicMethodsPartialFractionsSVG-001 | SVG | Template table |
| A21AlgebraicMethodsPartialFractionsSVG-002 | SVG | Legal vs illegal cancellation |
| A21AlgebraicMethodsPartialFractionsTikZ-001 | TikZ | Algebraic division layout |
| A21AlgebraicMethodsPartialFractionsWidget-001 | HTML widget | Interactive constants finder |

## Supplementary Sources Used

The Dr Frost material is third-party and includes cross-board references, but its partial fractions content is used only where it matches the CCEA A21-AF boundary. Cross-board exam labels are not treated as CCEA exam authority.

## Final Student Checklist

Before leaving this lesson, the student should be able to say yes to each item:

- I can factorise denominators before simplifying algebraic fractions.
- I can explain why cancelling terms in a sum is illegal.
- I can set up partial fractions for two distinct linear factors.
- I can use substitution values that make brackets disappear.
- I can compare coefficients from an identity.
- I can set up repeated squared linear factors using both \((x-a)\) and \((x-a)^2\).
- I can identify an improper algebraic fraction using degrees.
- I can do algebraic division before partial fractions.
- I can use a single identity for an improper partial fraction.
- I know that cubed repeated factors and irreducible quadratic denominators are not core for this CCEA lesson boundary.

## Progress Manifest

| Item | Status |
|---|---|
| Phase 0 Evidence Intake and Plan | Complete |
| Phase 1 Main Lesson Markdown | Complete |
| Phase 2 Mermaid Diagrams | Complete |
| Phase 3 SVG Assets | Complete |
| Phase 4 TikZ Assets | Complete |
| Phase 5 Widgets | Complete |
| Phase 6 Manifest, Source Reference and Packaging | Complete |
