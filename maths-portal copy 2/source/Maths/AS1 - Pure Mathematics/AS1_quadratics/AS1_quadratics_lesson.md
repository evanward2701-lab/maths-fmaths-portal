# AS1 Quadratics

## CCEA GCE Mathematics: AS 1 Pure Mathematics

### Lesson Metadata

| Field | Value |
|---|---|
| unit_code | AS1 |
| unit_name | AS 1 Pure Mathematics |
| topic_code | AS1-AF |
| official topic area | Algebra and functions |
| lesson topic | Quadratics |
| topic_slug | quadratics |
| topic_pascal | Quadratics |
| topic_id | AS1Quadratics |
| lesson_file | AS1_quadratics_lesson.md |
| core LO IDs | AS1-AF-LO003, AS1-AF-LO004, AS1-AF-LO005, AS1-AF-LO006 |
| supporting LO IDs | AS1-AF-LO012, AS1-AF-LO014 |
| tags | `#AS1`, `#AlgebraFunctions`, `#Quadratics`, `#SolveEquation`, `#SketchGraph`, `#Discriminant`, `#CompletingTheSquare` |

---

## Evidence Map

| Evidence | Used for |
|---|---|
| CCEA GCE Mathematics Specification Map | Official topic, LO IDs, boundaries |
| Project README/module map | Naming conventions and phase structure |
| Source evidence checklist | Missing evidence and off-spec logging |
| `P1-Chp2-Quadratics_RevealBlocksRemoved.pdf` | Slide structure, examples, visual prompts |
| `Chapter_2_Quadratics_🤖_(Pure_Year_1)_Transcript.md` | Teacher explanation, warnings, worked methods |
| `Chapter_2_Quadratics_🤖_(Pure_Year_1)_Screenshots.pdf` | Visual annotation sequence for solving `x^2+5x=6` |

The lesson evidence covers solving quadratic equations, completing the square, quadratics as functions, quadratic graphs, the discriminant and modelling with quadratics.

---

## Specification Alignment

| LO ID | Lesson section |
|---|---|
| AS1-AF-LO003 | Quadratic functions, roots, range/domain language, graph features |
| AS1-AF-LO004 | Discriminant, repeated roots, no real roots, two distinct real roots |
| AS1-AF-LO005 | Completing the square, turning points, maxima/minima |
| AS1-AF-LO006 | Solving quadratic equations, including quadratics in a function of the unknown |
| AS1-AF-LO012 | Sketching quadratic graphs as polynomial curves |
| AS1-AF-LO014 | Interpreting roots and algebraic solutions graphically |

---

## Learning Objectives

By the end of this lesson, you should be able to:

1. Recognise a quadratic equation or quadratic function.
2. Solve quadratic equations by factorisation, the quadratic formula and completing the square.
3. Solve quadratic equations “in disguise” using substitution or direct factorisation.
4. Complete the square for expressions such as `x^2+bx+c` and `ax^2+bx+c`.
5. Use completed square form to find turning points and maximum/minimum values.
6. Use `f(x)`, domain, range and roots correctly in quadratic contexts.
7. Sketch quadratic graphs using roots, y-intercept, turning point and line of symmetry.
8. Use the discriminant `b^2-4ac` to decide whether a quadratic has no real roots, equal roots or two distinct real roots.
9. Interpret quadratic models in context.

---

## Prerequisite Recap: A-Level Working Skills Only

This lesson does **not** use GCSE sources as evidence. The prior skills below are only assumed working skills needed to access the A-Level content.

| Skill | Needed because |
|---|---|
| Expanding brackets | Required before rearranging quadratics into `ax^2+bx+c=0` |
| Factorising quadratics | Required for solving by factorisation |
| Rearranging equations | Required for isolating squared expressions and solving models |
| Surds and square roots | Required for `±sqrt(k)`, exact solutions and formula work |
| Basic graph sketching | Required for roots, intercepts and turning points |
| Substitution | Required for quadratics in disguise, such as equations in `sqrt(x)` |

---

## Big Picture Explanation

A quadratic is a mathematical shape-shifter. It appears as an equation to solve, a function to interpret, a graph to sketch, and a model for real situations.

The lesson evidence gives several contexts where quadratic relationships arise:

- summations and quadratic sequences;
- projectile motion, where a path under gravity is parabolic;
- probability-style products involving two expressions in the same variable;
- modelling height, distance, profit or other changing quantities.

The core reason quadratics matter is that they connect algebra and graphs. A line has one direction of travel; a quadratic bends. That bend creates roots, turning points, maximum or minimum values, and model interpretations.

---

## Key Definitions and Notation

### Quadratic expression

A quadratic expression in `x` is an expression where the highest power of `x` is `2`, usually written as

\[
ax^2+bx+c
\]

where `a`, `b`, and `c` are constants and

\[
a\ne 0.
\]

If `a=0`, then the `x^2` term disappears and the expression is no longer quadratic.

### Quadratic equation

A quadratic equation is an equation that can be written in the form

\[
ax^2+bx+c=0,\qquad a\ne0.
\]

A quadratic equation is an equation of degree 2, because the highest power present is the squared term.

### Root / solution

A root of an equation is a value that makes the equation true.

For a function `f(x)`, a root is a value of `x` such that

\[
f(x)=0.
\]

### Completed square form

Completing the square means rewriting a quadratic in one of these forms:

\[
(x+a)^2+b
\]

or

\[
a(x+b)^2+c.
\]

The reason this is useful is that `x` appears only once in the completed-square expression, which makes it easier to solve or interpret.

### Discriminant

For

\[
ax^2+bx+c=0,
\]

the discriminant is

\[
b^2-4ac.
\]

It is the part inside the square root in the quadratic formula, and it tells us the root type:

\[
b^2-4ac>0 \Rightarrow \text{two distinct real roots},
\]

\[
b^2-4ac=0 \Rightarrow \text{equal roots},
\]

\[
b^2-4ac<0 \Rightarrow \text{no real roots}.
\]

---

## Visual Asset Integration

[VISUAL PLACEHOLDER: AS1QuadraticsSVG-001 | Source: CCEA AS1-AF specification map + quadratics chapter overview | Insert from svg/AS1QuadraticsSVG-001.svg | Purpose: Show the six-part structure of the quadratics lesson: solving, completing the square, functions, graphs, discriminant and modelling.]

[VISUAL PLACEHOLDER: AS1QuadraticsSVG-002 | Source: Lesson PDF pages 6–8 and transcript video 1 | Insert from svg/AS1QuadraticsSVG-002.svg | Purpose: Compare the three algebraic solving routes: factorisation, quadratic formula and completing the square.]

[INTERACTIVE PLACEHOLDER: AS1QuadraticsWidget-001 | Source: CCEA AS1-AF-LO006 + lesson evidence on method choice | Insert from widgets/AS1QuadraticsWidget-001.html | Purpose: Let the student classify a quadratic equation by best solving method.]

---

# Core Theory Part A – Solving Quadratic Equations

## A1. The standard form

Before solving by factorisation or the quadratic formula, aim to write the equation as

\[
ax^2+bx+c=0.
\]

The slide example begins with

\[
x^2+5x=6.
\]

Move everything to one side:

\[
x^2+5x-6=0.
\]

Now it is in standard form:

\[
a=1,\qquad b=5,\qquad c=-6.
\]

## A2. Solving by factorisation

Start with

\[
x^2+5x=6.
\]

Move all terms to one side:

\[
x^2+5x-6=0.
\]

Find two numbers that multiply to `-6` and add to `5`. These are `6` and `-1`, so

\[
x^2+5x-6=(x+6)(x-1).
\]

Therefore

\[
(x+6)(x-1)=0.
\]

If the product of two factors is `0`, then at least one factor must be `0`. So

\[
x+6=0
\]

or

\[
x-1=0.
\]

Solving each equation gives

\[
x=-6
\]

or

\[
x=1.
\]

So the solutions are

\[
\boxed{x=-6 \text{ or } x=1.}
\]

## A3. Solving by the quadratic formula

For

\[
ax^2+bx+c=0,
\]

the quadratic formula is

\[
x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}.
\]

Using the same equation,

\[
x^2+5x-6=0,
\]

we identify

\[
a=1,\qquad b=5,\qquad c=-6.
\]

Substitute into the formula:

\[
x=\frac{-5\pm\sqrt{5^2-4(1)(-6)}}{2(1)}.
\]

Now simplify inside the square root:

\[
5^2=25,
\]

and

\[
-4(1)(-6)=+24.
\]

So

\[
x=\frac{-5\pm\sqrt{25+24}}{2}.
\]

\[
x=\frac{-5\pm\sqrt{49}}{2}.
\]

\[
x=\frac{-5\pm7}{2}.
\]

This gives two solutions:

\[
x=\frac{-5+7}{2}=\frac{2}{2}=1,
\]

or

\[
x=\frac{-5-7}{2}=\frac{-12}{2}=-6.
\]

Therefore

\[
\boxed{x=1 \text{ or } x=-6.}
\]

## A4. Solving without expanding when the unknown appears once

If the unknown appears only once, expanding can create needless algebra fog.

Example:

\[
(x-1)^2=5.
\]

Since `x` appears only in the bracket `x-1`, take the square root of both sides:

\[
x-1=\pm\sqrt{5}.
\]

Add `1` to both sides:

\[
x=1\pm\sqrt{5}.
\]

So

\[
\boxed{x=1+\sqrt{5} \text{ or } x=1-\sqrt{5}.}
\]

The `±` is essential because

\[
2^2=4
\]

and also

\[
(-2)^2=4.
\]

So from

\[
x^2=4,
\]

we get

\[
x=\pm2.
\]

## A5. Quadratics “in disguise”

Some equations are quadratic, but not directly in `x`. The evidence calls these “quadratics in disguise” or “pseudo quadratics”.

Example:

\[
x-6\sqrt{x}+8=0.
\]

This is quadratic in `sqrt(x)`, because `x=(sqrt(x))^2`.

Let

\[
y=\sqrt{x}.
\]

Then

\[
y^2=x.
\]

Substitute into the equation:

\[
x-6\sqrt{x}+8=0
\]

becomes

\[
y^2-6y+8=0.
\]

Factorise:

\[
y^2-6y+8=(y-2)(y-4).
\]

So

\[
(y-2)(y-4)=0.
\]

Therefore

\[
y=2 \quad \text{or} \quad y=4.
\]

Now return to `x`. Since

\[
y=\sqrt{x},
\]

we have

\[
\sqrt{x}=2
\]

or

\[
\sqrt{x}=4.
\]

Square both sides in each case:

\[
x=2^2=4,
\]

or

\[
x=4^2=16.
\]

Therefore

\[
\boxed{x=4 \text{ or } x=16.}
\]

The same example can be factorised directly as

\[
(\sqrt{x}-2)(\sqrt{x}-4)=0,
\]

which gives the same answers.

## A6. Worked Example: Solve `(x+3)^2=x+5` by factorisation

Start with

\[
(x+3)^2=x+5.
\]

Expand the left-hand side:

\[
(x+3)^2=(x+3)(x+3).
\]

\[
(x+3)(x+3)=x^2+3x+3x+9.
\]

\[
(x+3)^2=x^2+6x+9.
\]

So the equation becomes

\[
x^2+6x+9=x+5.
\]

Move everything to one side:

\[
x^2+6x+9-x-5=0.
\]

Collect like terms:

\[
x^2+5x+4=0.
\]

Factorise:

\[
x^2+5x+4=(x+4)(x+1).
\]

So

\[
(x+4)(x+1)=0.
\]

Therefore

\[
x=-4
\]

or

\[
x=-1.
\]

\[
\boxed{x=-4 \text{ or } x=-1.}
\]

## A7. Worked Example: Solve `(2x+1)^2=5`

Start with

\[
(2x+1)^2=5.
\]

The subject `x` appears only once, inside `2x+1`, so do not expand.

Take the square root of both sides:

\[
2x+1=\pm\sqrt{5}.
\]

Subtract `1`:

\[
2x=-1\pm\sqrt{5}.
\]

Divide by `2`:

\[
x=\frac{-1\pm\sqrt{5}}{2}.
\]

Equivalently,

\[
x=-\frac12\pm\frac{\sqrt5}{2}.
\]

## A8. Worked Example: Solve `sqrt(x+3)=x-3`

Start with

\[
\sqrt{x+3}=x-3.
\]

Square both sides:

\[
\left(\sqrt{x+3}\right)^2=(x-3)^2.
\]

So

\[
x+3=(x-3)^2.
\]

Expand the right-hand side carefully:

\[
(x-3)^2=(x-3)(x-3)=x^2-3x-3x+9=x^2-6x+9.
\]

Therefore

\[
x+3=x^2-6x+9.
\]

Move all terms to one side:

\[
0=x^2-6x+9-x-3.
\]

\[
0=x^2-7x+6.
\]

So

\[
x^2-7x+6=0.
\]

Factorise:

\[
x^2-7x+6=(x-6)(x-1).
\]

Thus

\[
(x-6)(x-1)=0.
\]

So

\[
x=6 \quad \text{or} \quad x=1.
\]

Now check both in the original equation, because squaring both sides can introduce false solutions.

Check `x=1`:

Left-hand side:

\[
\sqrt{1+3}=\sqrt4=2.
\]

Right-hand side:

\[
1-3=-2.
\]

Since

\[
2\ne -2,
\]

`x=1` is not a solution.

Check `x=6`:

Left-hand side:

\[
\sqrt{6+3}=\sqrt9=3.
\]

Right-hand side:

\[
6-3=3.
\]

Since

\[
3=3,
\]

`x=6` works.

Therefore

\[
\boxed{x=6.}
\]

## A9. Worked Example: Solve `2x+sqrt(x)-1=0`

Start with

\[
2x+\sqrt{x}-1=0.
\]

Let

\[
y=\sqrt{x}.
\]

Then

\[
y^2=x.
\]

Substitute into the equation:

\[
2y^2+y-1=0.
\]

Factorise:

\[
2y^2+y-1=(2y-1)(y+1).
\]

So

\[
(2y-1)(y+1)=0.
\]

Therefore

\[
2y-1=0
\]

or

\[
y+1=0.
\]

Solve each:

\[
y=\frac12
\]

or

\[
y=-1.
\]

Return to `x`:

\[
\sqrt{x}=\frac12
\]

or

\[
\sqrt{x}=-1.
\]

For the first solution:

\[
x=\left(\frac12\right)^2=\frac14.
\]

For the second:

\[
\sqrt{x}=-1
\]

has no real solution, because the principal square root cannot be negative.

Therefore

\[
\boxed{x=\frac14.}
\]

---

## Common Mistakes and Exam Traps So Far

| Trap | Safer habit |
|---|---|
| Forgetting to make the quadratic equal to zero before factorising | First aim for `ax^2+bx+c=0` |
| Treating `(x-3)^2` as `x^2-9` | Expand as `(x-3)(x-3)` |
| Forgetting the `±` when square-rooting | From `u^2=k`, write `u=±sqrt(k)` |
| Expanding when the subject appears only once | Use inverse operations first |
| Accepting false solutions after squaring | Substitute answers into the original equation |
| Keeping `sqrt(x)=-1` as a valid real solution | Remember the principal square root is not negative |
| Using a calculator solver as the method when algebra is requested | Use it to check, not to replace required working |

---

# Core Theory Part B – Completing the Square

## B1. What completing the square means

Completing the square means rewriting a quadratic so that `x` appears inside a squared bracket, usually in one of these forms:

\[
(x+a)^2+b
\]

or

\[
a(x+b)^2+c.
\]

The main reason for doing this is that once the quadratic is written this way, `x` appears only once, which makes the expression easier to solve, sketch, and interpret.

## B2. The key expansion pattern

Start by expanding:

\[
(x+9)^2=(x+9)(x+9)=x^2+9x+9x+81=x^2+18x+81.
\]

Now expand:

\[
(x-5)^2=(x-5)(x-5)=x^2-5x-5x+25=x^2-10x+25.
\]

Notice the pattern:

\[
(x+a)^2=x^2+2ax+a^2.
\]

So the number inside the bracket is **half the coefficient of `x`**.

For example:

\[
(x+6)^2=x^2+12x+36.
\]

Therefore, if we want to rewrite

\[
x^2+12x,
\]

we begin with

\[
(x+6)^2.
\]

But this has created an extra `+36`, because

\[
(x+6)^2=x^2+12x+36.
\]

So we subtract `36`:

\[
x^2+12x=(x+6)^2-36.
\]

Check:

\[
(x+6)^2-36=x^2+12x+36-36=x^2+12x.
\]

So

\[
\boxed{x^2+12x=(x+6)^2-36.}
\]

## B3. Completing the square when the coefficient of `x^2` is `1`

### Example 1

Write

\[
x^2+8x
\]

in completed square form.

Half the coefficient of `x`:

\[
\frac{8}{2}=4.
\]

Start with

\[
(x+4)^2.
\]

Expand mentally:

\[
(x+4)^2=x^2+8x+16.
\]

We only wanted `x^2+8x`, so subtract `16`:

\[
x^2+8x=(x+4)^2-16.
\]

### Example 2

Write

\[
x^2-2x
\]

in completed square form.

Half the coefficient of `x`:

\[
\frac{-2}{2}=-1.
\]

Start with

\[
(x-1)^2.
\]

Expand:

\[
(x-1)^2=x^2-2x+1.
\]

Subtract `1`:

\[
x^2-2x=(x-1)^2-1.
\]

Even when the number in the bracket is negative, the number you subtract is still positive because

\[
(-1)^2=1.
\]

### Example 3

Write

\[
x^2-6x+7
\]

in completed square form.

First complete the square on

\[
x^2-6x.
\]

Half the coefficient of `x`:

\[
\frac{-6}{2}=-3.
\]

So

\[
x^2-6x=(x-3)^2-9.
\]

Now include the `+7`:

\[
x^2-6x+7=(x-3)^2-9+7.
\]

Simplify:

\[
x^2-6x+7=(x-3)^2-2.
\]

Check by expanding:

\[
(x-3)^2-2=x^2-6x+9-2=x^2-6x+7.
\]

## B4. Completing the square when the coefficient of `x^2` is not `1`

When the coefficient of `x^2` is not `1`, factor it out from the `x^2` and `x` terms first.

### Worked Example 10: Express `2x^2+12x+7` in the form `a(x+b)^2+c`

Start with

\[
2x^2+12x+7.
\]

Factor out `2` from the `x^2` and `x` terms:

\[
2x^2+12x+7=2(x^2+6x)+7.
\]

Complete the square inside the bracket.

Half the coefficient of `x`:

\[
\frac{6}{2}=3.
\]

So

\[
x^2+6x=(x+3)^2-9.
\]

Substitute this into the expression:

\[
2(x^2+6x)+7=2\left((x+3)^2-9\right)+7.
\]

Expand the outer bracket:

\[
=2(x+3)^2-18+7.
\]

Simplify:

\[
=2(x+3)^2-11.
\]

Therefore

\[
\boxed{2x^2+12x+7=2(x+3)^2-11.}
\]

### Worked Example 11: Express `5-3x^2+6x` in the form `a-b(x+c)^2`

First rewrite in descending powers of `x`:

\[
5-3x^2+6x=-3x^2+6x+5.
\]

Factor out `-3` from the `x^2` and `x` terms:

\[
-3x^2+6x+5=-3(x^2-2x)+5.
\]

Complete the square inside the bracket.

Half the coefficient of `x`:

\[
\frac{-2}{2}=-1.
\]

So

\[
x^2-2x=(x-1)^2-1.
\]

Substitute:

\[
-3(x^2-2x)+5=-3\left((x-1)^2-1\right)+5.
\]

Expand:

\[
=-3(x-1)^2+3+5.
\]

Simplify:

\[
=8-3(x-1)^2.
\]

Therefore

\[
\boxed{5-3x^2+6x=8-3(x-1)^2.}
\]

This form immediately tells us the expression has a maximum value of `8`, since the squared term is being subtracted.

## B5. Student Practice: Complete the square

### Question 1

Express

\[
3x^2-18x+4
\]

in completed square form.

### Solution

Start with

\[
3x^2-18x+4.
\]

Factor out `3` from the `x^2` and `x` terms:

\[
3x^2-18x+4=3(x^2-6x)+4.
\]

Complete the square inside the bracket:

\[
x^2-6x=(x-3)^2-9.
\]

Substitute:

\[
3(x^2-6x)+4=3\left((x-3)^2-9\right)+4.
\]

Expand:

\[
=3(x-3)^2-27+4.
\]

Simplify:

\[
=3(x-3)^2-23.
\]

So

\[
\boxed{3x^2-18x+4=3(x-3)^2-23.}
\]

### Question 2

Express

\[
20x-5x^2+3
\]

in the form

\[
a-b(x+c)^2.
\]

### Solution

Rewrite in descending powers of `x`:

\[
20x-5x^2+3=-5x^2+20x+3.
\]

Factor out `-5` from the `x^2` and `x` terms:

\[
-5x^2+20x+3=-5(x^2-4x)+3.
\]

Complete the square:

\[
x^2-4x=(x-2)^2-4.
\]

Substitute:

\[
-5(x^2-4x)+3=-5\left((x-2)^2-4\right)+3.
\]

Expand:

\[
=-5(x-2)^2+20+3.
\]

Simplify:

\[
=23-5(x-2)^2.
\]

So

\[
\boxed{20x-5x^2+3=23-5(x-2)^2.}
\]

## B6. Critical distinction: expressions versus equations

When completing the square for an **expression**, such as

\[
3x^2-18x+4,
\]

you cannot simply divide every term by `3`, because that would change the expression.

For example,

\[
3x^2-18x+4
\]

is not the same as

\[
x^2-6x+\frac43.
\]

The second expression is one third of the first, not a rearranged version of it.

But for an **equation**, such as

\[
3x^2-18x+4=0,
\]

you may divide both sides by `3`, because doing the same operation to both sides preserves the solutions.

---

# Core Theory Part C – Solving by Completing the Square

## C1. Why completed square form helps with solving

Suppose we have

\[
(x+4)^2-7=0.
\]

This is easier to solve than an expanded quadratic because the unknown appears only once.

Add `7` to both sides:

\[
(x+4)^2=7.
\]

Square root both sides:

\[
x+4=\pm\sqrt7.
\]

Subtract `4`:

\[
x=-4\pm\sqrt7.
\]

So

\[
\boxed{x=-4+\sqrt7 \text{ or } x=-4-\sqrt7.}
\]

## C2. Worked Example 12: Solve `3x^2-18x+4=0` by completing the square

Start with

\[
3x^2-18x+4=0.
\]

Because this is an equation, divide both sides by `3`:

\[
\frac{3x^2-18x+4}{3}=\frac{0}{3}.
\]

So

\[
x^2-6x+\frac43=0.
\]

Complete the square on `x^2-6x`:

\[
x^2-6x=(x-3)^2-9.
\]

Substitute:

\[
(x-3)^2-9+\frac43=0.
\]

Combine the constants:

\[
-9+\frac43=-\frac{27}{3}+\frac43=-\frac{23}{3}.
\]

So

\[
(x-3)^2-\frac{23}{3}=0.
\]

Add `23/3` to both sides:

\[
(x-3)^2=\frac{23}{3}.
\]

Square root both sides:

\[
x-3=\pm\sqrt{\frac{23}{3}}.
\]

Add `3`:

\[
x=3\pm\sqrt{\frac{23}{3}}.
\]

Therefore

\[
\boxed{x=3+\sqrt{\frac{23}{3}} \text{ or } x=3-\sqrt{\frac{23}{3}}.}
\]

## C3. Deriving the quadratic formula by completing the square

Start with the general quadratic equation:

\[
ax^2+bx+c=0.
\]

Assume

\[
a\ne0.
\]

Divide every term by `a`:

\[
x^2+\frac{b}{a}x+\frac{c}{a}=0.
\]

Complete the square on

\[
x^2+\frac{b}{a}x.
\]

Half the coefficient of `x`:

\[
\frac12\cdot\frac{b}{a}=\frac{b}{2a}.
\]

So

\[
x^2+\frac{b}{a}x=\left(x+\frac{b}{2a}\right)^2-\left(\frac{b}{2a}\right)^2.
\]

Since

\[
\left(\frac{b}{2a}\right)^2=\frac{b^2}{4a^2},
\]

we have

\[
x^2+\frac{b}{a}x=\left(x+\frac{b}{2a}\right)^2-\frac{b^2}{4a^2}.
\]

Substitute into the equation:

\[
\left(x+\frac{b}{2a}\right)^2-\frac{b^2}{4a^2}+\frac{c}{a}=0.
\]

Move the constant terms to the other side:

\[
\left(x+\frac{b}{2a}\right)^2=\frac{b^2}{4a^2}-\frac{c}{a}.
\]

Make a common denominator of `4a^2`.

For

\[
\frac{c}{a},
\]

multiply numerator and denominator by `4a`:

\[
\frac{c}{a}=\frac{4ac}{4a^2}.
\]

So

\[
\left(x+\frac{b}{2a}\right)^2=\frac{b^2}{4a^2}-\frac{4ac}{4a^2}.
\]

Combine:

\[
\left(x+\frac{b}{2a}\right)^2=\frac{b^2-4ac}{4a^2}.
\]

Square root both sides:

\[
x+\frac{b}{2a}=\pm\sqrt{\frac{b^2-4ac}{4a^2}}.
\]

Split the square root:

\[
x+\frac{b}{2a}=\pm\frac{\sqrt{b^2-4ac}}{2a}.
\]

Subtract `b/(2a)`:

\[
x=-\frac{b}{2a}\pm\frac{\sqrt{b^2-4ac}}{2a}.
\]

Use the common denominator `2a`:

\[
x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}.
\]

Therefore

\[
\boxed{x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}.}
\]

---

# Core Theory Part D – Quadratics as Functions

## D1. What a function is

A function is a rule that maps inputs to outputs.

If

\[
f(x)=x^2-3x,
\]

then `f` is the name of the function, `x` is the input, and `x^2-3x` is the output rule.

## D2. Domain, range and roots

The **domain** is the set of possible inputs.

The **range** is the set of possible outputs.

The **roots** or **zeroes** of a function are the values of `x` for which

\[
f(x)=0.
\]

In this quadratics chapter, the key function-language move is:

\[
\text{Find the roots of } f(x)
\]

means

\[
\text{solve } f(x)=0.
\]

## D3. Worked Example 13: Function notation and roots

Let

\[
f(x)=x^2-3x
\]

and

\[
g(x)=x+5,\qquad x\in\mathbb{R}.
\]

### Part (a): Find `f(-4)`

Substitute

\[
x=-4
\]

into

\[
f(x)=x^2-3x.
\]

\[
f(-4)=(-4)^2-3(-4).
\]

Calculate:

\[
(-4)^2=16
\]

and

\[
-3(-4)=12.
\]

So

\[
f(-4)=16+12=28.
\]

### Part (b): Find the values of `x` for which `f(x)=g(x)`

Set the two output expressions equal:

\[
x^2-3x=x+5.
\]

Move everything to one side:

\[
x^2-3x-x-5=0.
\]

Collect like terms:

\[
x^2-4x-5=0.
\]

Factorise:

\[
x^2-4x-5=(x-5)(x+1).
\]

So

\[
(x-5)(x+1)=0.
\]

Therefore

\[
x=5 \quad \text{or} \quad x=-1.
\]

These are the input values where the two functions have the same output.

### Part (c): Find the roots of `f(x)`

Roots mean

\[
f(x)=0.
\]

So solve:

\[
x^2-3x=0.
\]

Factorise:

\[
x(x-3)=0.
\]

Therefore

\[
x=0 \quad \text{or} \quad x=3.
\]

### Part (d): Find the roots of `g(x)`

Roots mean

\[
g(x)=0.
\]

So

\[
x+5=0.
\]

Subtract `5`:

\[
x=-5.
\]

---

# Core Theory Part E – Minimum and Maximum Values from Completed Square Form

## E1. The big idea

For any real number `u`,

\[
u^2\ge0.
\]

This means a squared bracket is always zero or positive.

So if

\[
f(x)=(x+a)^2+b,
\]

then the smallest possible value of the squared bracket is

\[
0.
\]

This happens when

\[
x+a=0.
\]

So

\[
x=-a.
\]

Therefore the minimum value of

\[
f(x)=(x+a)^2+b
\]

is

\[
b,
\]

and it occurs when

\[
x=-a.
\]

## E2. Worked Example 14: Find a minimum value

Determine the minimum value of

\[
f(x)=x^2-6x+2,
\]

and state the value of `x` for which this minimum occurs.

Complete the square:

\[
f(x)=x^2-6x+2.
\]

Half the coefficient of `x`:

\[
\frac{-6}{2}=-3.
\]

So

\[
x^2-6x=(x-3)^2-9.
\]

Substitute:

\[
f(x)=(x-3)^2-9+2.
\]

Simplify:

\[
f(x)=(x-3)^2-7.
\]

Now use the fact that

\[
(x-3)^2\ge0.
\]

The smallest possible value of

\[
(x-3)^2
\]

is

\[
0.
\]

This occurs when

\[
x-3=0.
\]

So

\[
x=3.
\]

When `x=3`,

\[
f(x)=0-7=-7.
\]

Therefore the minimum value is

\[
\boxed{-7}
\]

and it occurs when

\[
\boxed{x=3.}
\]

## E3. Worked Example 15: Minimum value with a coefficient

Find the minimum value of

\[
f(x)=2x^2+12x-5,
\]

and state the value of `x` for which it occurs.

Start with

\[
f(x)=2x^2+12x-5.
\]

Factor out `2` from the `x^2` and `x` terms:

\[
f(x)=2(x^2+6x)-5.
\]

Complete the square inside the bracket:

\[
x^2+6x=(x+3)^2-9.
\]

Substitute:

\[
f(x)=2\left((x+3)^2-9\right)-5.
\]

Expand:

\[
f(x)=2(x+3)^2-18-5.
\]

Simplify:

\[
f(x)=2(x+3)^2-23.
\]

Now

\[
(x+3)^2\ge0.
\]

So

\[
2(x+3)^2\ge0.
\]

The smallest value happens when

\[
(x+3)^2=0.
\]

That occurs when

\[
x+3=0.
\]

So

\[
x=-3.
\]

Then

\[
f(x)=0-23=-23.
\]

Therefore the minimum value is

\[
\boxed{-23}
\]

and it occurs when

\[
\boxed{x=-3.}
\]

## E4. Worked Example 16: Roots after function notation

Find the roots of

\[
f(x)=2x^2+3x+1.
\]

Roots mean solve

\[
f(x)=0.
\]

So

\[
2x^2+3x+1=0.
\]

Factorise:

\[
2x^2+3x+1=(2x+1)(x+1).
\]

So

\[
(2x+1)(x+1)=0.
\]

Therefore

\[
2x+1=0
\]

or

\[
x+1=0.
\]

Solve the first:

\[
2x=-1
\]

\[
x=-\frac12.
\]

Solve the second:

\[
x=-1.
\]

Therefore the roots are

\[
\boxed{x=-\frac12 \text{ or } x=-1.}
\]

## E5. Worked Example 17: Roots of a disguised quadratic function

Find the roots of

\[
f(x)=x^4-x^2-6.
\]

Roots mean solve

\[
x^4-x^2-6=0.
\]

This is quadratic in `x^2`. Factorise directly:

\[
x^4-x^2-6=(x^2-3)(x^2+2).
\]

So

\[
(x^2-3)(x^2+2)=0.
\]

Therefore

\[
x^2-3=0
\]

or

\[
x^2+2=0.
\]

From

\[
x^2-3=0,
\]

we get

\[
x^2=3.
\]

So

\[
x=\pm\sqrt3.
\]

From

\[
x^2+2=0,
\]

we get

\[
x^2=-2.
\]

There are no real solutions to

\[
x^2=-2,
\]

because a square cannot be negative in the real number system.

Therefore the real roots are

\[
\boxed{x=\pm\sqrt3.}
\]

[VISUAL PLACEHOLDER: AS1QuadraticsSVG-003 | Source: Lesson PDF pages 10–12 + CCEA AS1-AF-LO005 | Insert from svg/AS1QuadraticsSVG-003.svg | Purpose: Show the algebraic “complete the square” transformation from `x^2+bx+c` to `(x+a)^2+k`.]

[VISUAL PLACEHOLDER: AS1QuadraticsSVG-004 | Source: Transcript videos 5–6 + CCEA AS1-AF-LO003 and AS1-AF-LO005 | Insert from svg/AS1QuadraticsSVG-004.svg | Purpose: Show how completed square form reveals the minimum point of a quadratic.]

[INTERACTIVE PLACEHOLDER: AS1QuadraticsWidget-002 | Source: CCEA AS1-AF-LO005 + maxima/minima evidence | Insert from widgets/AS1QuadraticsWidget-002.html | Purpose: Let the student drag sliders in `a(x+b)^2+c` and observe the turning point and minimum or maximum value.]

---

# Core Theory Part F – Sketching Quadratic Graphs

## F1. What a sketch means

A **sketch** is not a perfectly scaled drawing.

For a graph sketch:

- draw and label the axes;
- show the general shape correctly;
- do **not** put a full scale on the axes unless required;
- label important coordinates such as intercepts, roots and turning points.

For quadratics, the main features are:

| Feature | Meaning |
|---|---|
| Shape | Whether the graph is U-shaped or upside-down U-shaped |
| Roots | Where the graph crosses or touches the x-axis |
| y-intercept | Where the graph crosses the y-axis |
| Turning point | The minimum or maximum point |
| Line of symmetry | The vertical line through the turning point |

## F2. Shape of a quadratic graph

A quadratic has the form

\[
y=ax^2+bx+c.
\]

The sign of `a` controls the broad shape.

If

\[
a>0,
\]

then the graph is U-shaped and has a **minimum** turning point.

If

\[
a<0,
\]

then the graph is upside-down U-shaped and has a **maximum** turning point.

## F3. Worked Example 18: Sketch `y=x^2+4x-5`

Sketch

\[
y=x^2+4x-5,
\]

indicating the turning point and any intercepts with the axes.

### Step 1: Decide the shape

The coefficient of `x^2` is

\[
a=1.
\]

Since

\[
a>0,
\]

the graph is U-shaped and has a minimum.

### Step 2: Find the x-intercepts, also called roots

Set

\[
y=0.
\]

So

\[
x^2+4x-5=0.
\]

Factorise:

\[
x^2+4x-5=(x+5)(x-1).
\]

Therefore

\[
(x+5)(x-1)=0.
\]

So

\[
x=-5
\]

or

\[
x=1.
\]

So the x-intercepts are

\[
\boxed{(-5,0)\text{ and }(1,0).}
\]

### Step 3: Find the y-intercept

The y-intercept occurs when

\[
x=0.
\]

Substitute into the equation:

\[
y=0^2+4(0)-5=-5.
\]

So the y-intercept is

\[
\boxed{(0,-5).}
\]

### Step 4: Find the turning point

Complete the square:

\[
y=x^2+4x-5.
\]

Half the coefficient of `x`:

\[
\frac{4}{2}=2.
\]

So

\[
x^2+4x=(x+2)^2-4.
\]

Therefore

\[
y=(x+2)^2-4-5=(x+2)^2-9.
\]

Since

\[
(x+2)^2\ge0,
\]

the minimum value is `-9`, and it occurs when

\[
x+2=0.
\]

So

\[
x=-2.
\]

The turning point is

\[
\boxed{(-2,-9).}
\]

### Step 5: State the line of symmetry

The line of symmetry passes through the turning point, so

\[
\boxed{x=-2.}
\]

This also lies halfway between the roots:

\[
\frac{-5+1}{2}=\frac{-4}{2}=-2.
\]

[VISUAL PLACEHOLDER: AS1QuadraticsSVG-005 | Source: Lesson PDF chapter overview + transcript video 7 | Insert from svg/AS1QuadraticsSVG-005.svg | Purpose: Sketch `y=x^2+4x-5`, labelling roots, y-intercept, turning point and line of symmetry.]

---

# Core Theory Part G – Finding the Equation of a Quadratic Graph

## G1. Three useful forms of a quadratic

### Form 1: General form

Use

\[
y=ax^2+bx+c
\]

when you are given three coordinates and no special root or turning-point structure is obvious.

### Form 2: Root form

If you know the roots are

\[
x=r_1
\]

and

\[
x=r_2,
\]

then use

\[
y=a(x-r_1)(x-r_2).
\]

The extra `a` is needed because many quadratics can share the same roots but be stretched, compressed, or reflected.

### Form 3: Completed square / turning point form

If you know the turning point is

\[
(h,k),
\]

then use

\[
y=a(x-h)^2+k.
\]

This is the form to reach for when the question gives a maximum or minimum point.

## G2. Worked Example 19: Find a quadratic from roots and shape

A quadratic has roots

\[
x=-1
\]

and

\[
x=\frac72,
\]

and it is upside-down. Find an equation with integer coefficients.

Because the roots are known, use root form:

\[
y=a(x+1)\left(x-\frac72\right).
\]

Since the graph is upside-down, choose a negative value of `a`. To clear the fraction, choose

\[
a=-2.
\]

Then

\[
y=-2(x+1)\left(x-\frac72\right).
\]

Expand the brackets first:

\[
(x+1)\left(x-\frac72\right)=x^2-\frac72x+x-\frac72.
\]

Combine the `x`-terms:

\[
-\frac72x+x=-\frac72x+\frac22x=-\frac52x.
\]

So

\[
(x+1)\left(x-\frac72\right)=x^2-\frac52x-\frac72.
\]

Now multiply by `-2`:

\[
y=-2\left(x^2-\frac52x-\frac72\right)=-2x^2+5x+7.
\]

Therefore one suitable equation is

\[
\boxed{y=-2x^2+5x+7.}
\]

## G3. Worked Example 20: Find a quadratic from three points

Find the equation of the quadratic passing through

\[
(3,0),\qquad (0,10),\qquad (-3,0).
\]

Use the general form

\[
y=ax^2+bx+c.
\]

### Use the point `(0,10)`

Substitute

\[
x=0,\qquad y=10.
\]

\[
10=a(0)^2+b(0)+c.
\]

\[
10=c.
\]

So

\[
c=10.
\]

The equation is now

\[
y=ax^2+bx+10.
\]

### Use the point `(3,0)`

Substitute

\[
x=3,\qquad y=0.
\]

\[
0=a(3)^2+b(3)+10.
\]

\[
0=9a+3b+10.
\]

So

\[
9a+3b=-10.
\]

### Use the point `(-3,0)`

Substitute

\[
x=-3,\qquad y=0.
\]

\[
0=a(-3)^2+b(-3)+10.
\]

\[
0=9a-3b+10.
\]

So

\[
9a-3b=-10.
\]

Now solve the simultaneous equations:

\[
9a+3b=-10
\]

\[
9a-3b=-10.
\]

Add the two equations:

\[
(9a+3b)+(9a-3b)=-10+(-10).
\]

\[
18a=-20.
\]

\[
a=-\frac{20}{18}=-\frac{10}{9}.
\]

Now substitute into

\[
9a+3b=-10.
\]

\[
9\left(-\frac{10}{9}\right)+3b=-10.
\]

\[
-10+3b=-10.
\]

Add `10` to both sides:

\[
3b=0.
\]

\[
b=0.
\]

So

\[
a=-\frac{10}{9},\qquad b=0,\qquad c=10.
\]

Therefore

\[
\boxed{y=-\frac{10}{9}x^2+10.}
\]

---

# Core Theory Part H – The Discriminant

## H1. Why the discriminant works

For

\[
ax^2+bx+c=0,
\]

the quadratic formula is

\[
x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}.
\]

The discriminant is

\[
\boxed{b^2-4ac.}
\]

It is the expression inside the square root.

## H2. Discriminant cases

| Discriminant | Root type | Graph meaning |
|---|---|---|
| `b^2-4ac>0` | Two distinct real roots | Graph crosses the x-axis twice |
| `b^2-4ac=0` | One repeated real root | Graph touches the x-axis |
| `b^2-4ac<0` | No real roots | Graph does not meet the x-axis |

[VISUAL PLACEHOLDER: AS1QuadraticsSVG-006 | Source: CCEA AS1-AF-LO004 + transcript video 9 | Insert from svg/AS1QuadraticsSVG-006.svg | Purpose: Show the three graph cases for discriminant `>0`, `=0`, and `<0`.]

## H3. Worked Example 21: Use the discriminant to classify roots

For each equation, calculate

\[
b^2-4ac
\]

and state the number of real roots.

### Example 21(a)

\[
x^2+3x+4=0.
\]

Here

\[
a=1,\qquad b=3,\qquad c=4.
\]

Calculate:

\[
b^2-4ac=3^2-4(1)(4)=9-16=-7.
\]

Since

\[
-7<0,
\]

there are no real roots.

### Example 21(b)

\[
x^2+4x+1=0.
\]

Here

\[
a=1,\qquad b=4,\qquad c=1.
\]

Calculate:

\[
b^2-4ac=4^2-4(1)(1)=16-4=12.
\]

Since

\[
12>0,
\]

there are two distinct real roots.

### Example 21(c)

\[
x^2+4x+4=0.
\]

Here

\[
a=1,\qquad b=4,\qquad c=4.
\]

Calculate:

\[
b^2-4ac=4^2-4(1)(4)=16-16=0.
\]

Since

\[
b^2-4ac=0,
\]

there is one repeated real root.

### Example 21(d)

\[
-3x^2+x-4=0.
\]

Here

\[
a=-3,\qquad b=1,\qquad c=-4.
\]

Calculate:

\[
b^2-4ac=1^2-4(-3)(-4).
\]

Work through the signs carefully:

\[
-4(-3)(-4)=12(-4)=-48.
\]

So

\[
b^2-4ac=1-48=-47.
\]

Since

\[
-47<0,
\]

there are no real roots.

## H4. Worked Example 22: Equal roots with a parameter

The equation

\[
x^2+2px+3p+4=0
\]

has equal roots, where `p` is a positive constant. Find `p`, then solve the equation.

### Step 1: Use the equal roots condition

Equal roots mean

\[
b^2-4ac=0.
\]

For

\[
x^2+2px+3p+4=0,
\]

we have

\[
a=1,\qquad b=2p,\qquad c=3p+4.
\]

So

\[
(2p)^2-4(1)(3p+4)=0.
\]

Now expand:

\[
(2p)^2=4p^2.
\]

\[
4(1)(3p+4)=12p+16.
\]

So

\[
4p^2-(12p+16)=0.
\]

\[
4p^2-12p-16=0.
\]

Divide by `4`:

\[
p^2-3p-4=0.
\]

Factorise:

\[
p^2-3p-4=(p-4)(p+1).
\]

So

\[
(p-4)(p+1)=0.
\]

Therefore

\[
p=4
\]

or

\[
p=-1.
\]

But the question says `p` is positive, so

\[
\boxed{p=4.}
\]

### Step 2: Solve the equation when `p=4`

Substitute

\[
p=4
\]

into

\[
x^2+2px+3p+4=0.
\]

\[
x^2+2(4)x+3(4)+4=0.
\]

\[
x^2+8x+12+4=0.
\]

\[
x^2+8x+16=0.
\]

Factorise:

\[
x^2+8x+16=(x+4)^2.
\]

So

\[
(x+4)^2=0.
\]

Therefore

\[
x+4=0.
\]

\[
\boxed{x=-4.}
\]

Since the roots are equal, this is a repeated root.

## H5. Worked Example 23: Range of `k` for two distinct real roots

Find the range of values of `k` for which

\[
x^2+4x+k=0
\]

has two distinct real roots.

For two distinct real roots,

\[
b^2-4ac>0.
\]

Here

\[
a=1,\qquad b=4,\qquad c=k.
\]

So

\[
4^2-4(1)(k)>0.
\]

\[
16-4k>0.
\]

Subtract `16` from both sides:

\[
-4k>-16.
\]

Divide by `-4`. Since we divide by a negative number, reverse the inequality sign:

\[
k<4.
\]

Therefore

\[
\boxed{k<4.}
\]

---

# Core Theory Part I – Modelling with Quadratics

## I1. Why quadratics model real situations

Quadratic relationships appear in summations, projectile motion and probability contexts where a product of two expressions involving the same variable occurs.

In modelling questions, you must interpret symbols. The letters may not be `x` and `y`. For example:

\[
h(t)
\]

might mean height after `t` seconds.

## I2. Worked Example 24: Spear height model

A spear is thrown over level ground from the top of a tower. Its height `h` metres above the ground after `t` seconds is modelled by

\[
h(t)=12.25+14.7t-4.9t^2,\qquad t\ge0.
\]

### Part (a): Interpret the constant term `12.25`

The constant term is the value of `h(t)` when

\[
t=0.
\]

Substitute:

\[
h(0)=12.25+14.7(0)-4.9(0)^2=12.25.
\]

So `12.25` represents the starting height of the spear above the ground.

\[
\boxed{12.25\text{ m is the height from which the spear is thrown.}}
\]

### Part (b): Find when the spear hits the ground

The spear hits the ground when

\[
h(t)=0.
\]

So solve

\[
12.25+14.7t-4.9t^2=0.
\]

Rewrite in descending powers of `t`:

\[
-4.9t^2+14.7t+12.25=0.
\]

Using the quadratic formula with

\[
a=-4.9,\qquad b=14.7,\qquad c=12.25,
\]

\[
t=\frac{-14.7\pm\sqrt{14.7^2-4(-4.9)(12.25)}}{2(-4.9)}.
\]

Calculate the discriminant:

\[
14.7^2=216.09.
\]

\[
-4(-4.9)(12.25)=+240.1.
\]

So

\[
t=\frac{-14.7\pm\sqrt{216.09+240.1}}{-9.8}.
\]

\[
t=\frac{-14.7\pm\sqrt{456.19}}{-9.8}.
\]

This gives approximately

\[
t=3.68
\]

or

\[
t=-0.68.
\]

But the model states

\[
t\ge0.
\]

So the negative value is not meaningful in this context.

Therefore

\[
\boxed{t=3.68\text{ seconds, approximately}.}
\]

### Part (c): Write `h(t)` in completed square form

Start with

\[
h(t)=12.25+14.7t-4.9t^2.
\]

Rewrite in descending powers:

\[
h(t)=-4.9t^2+14.7t+12.25.
\]

Factor out `-4.9` from the `t^2` and `t` terms:

\[
h(t)=-4.9(t^2-3t)+12.25.
\]

Complete the square inside the bracket.

Half of `-3` is

\[
-\frac32=-1.5.
\]

So

\[
t^2-3t=(t-1.5)^2-(1.5)^2.
\]

Since

\[
(1.5)^2=2.25,
\]

we have

\[
t^2-3t=(t-1.5)^2-2.25.
\]

Substitute:

\[
h(t)=-4.9\left((t-1.5)^2-2.25\right)+12.25.
\]

Expand:

\[
h(t)=-4.9(t-1.5)^2+4.9(2.25)+12.25.
\]

Calculate:

\[
4.9(2.25)=11.025.
\]

So

\[
h(t)=-4.9(t-1.5)^2+11.025+12.25.
\]

\[
h(t)=-4.9(t-1.5)^2+23.275.
\]

Usually write the constant first:

\[
\boxed{h(t)=23.275-4.9(t-1.5)^2.}
\]

### Part (d): Find the maximum height and when it occurs

From

\[
h(t)=23.275-4.9(t-1.5)^2,
\]

we know

\[
(t-1.5)^2\ge0.
\]

So

\[
-4.9(t-1.5)^2\le0.
\]

This means the greatest possible value of `h(t)` occurs when

\[
(t-1.5)^2=0.
\]

So

\[
t-1.5=0.
\]

\[
t=1.5.
\]

At this time,

\[
h(t)=23.275-4.9(0)^2=23.275.
\]

Therefore the maximum height is

\[
\boxed{23.275\text{ m}}
\]

and it occurs at

\[
\boxed{t=1.5\text{ s}.}
\]

## I3. Worked Example 25: Tennis ball quadratic model from turning point information

A tennis ball is thrown from a point `1` metre above the ground. It reaches its maximum vertical height after travelling a horizontal distance of `5` metres. It is at a vertical height of `6` metres after travelling a horizontal distance of `9` metres.

Let `x` be horizontal distance in metres and `y` be vertical height in metres.

Find `y` in terms of `x`.

Since we know the horizontal coordinate of the turning point, use

\[
y=a(x-5)^2+C.
\]

We do not yet know `a` or `C`.

### Use the point `(9,6)`

Substitute

\[
x=9,\qquad y=6.
\]

\[
6=a(9-5)^2+C.
\]

\[
6=a(4)^2+C.
\]

\[
6=16a+C.
\]

So

\[
16a+C=6.
\]

### Use the point `(0,1)`

Substitute

\[
x=0,\qquad y=1.
\]

\[
1=a(0-5)^2+C.
\]

\[
1=a(-5)^2+C.
\]

\[
1=25a+C.
\]

So

\[
25a+C=1.
\]

Now solve the simultaneous equations:

\[
16a+C=6
\]

\[
25a+C=1.
\]

Subtract the first equation from the second:

\[
(25a+C)-(16a+C)=1-6.
\]

\[
9a=-5.
\]

\[
a=-\frac59.
\]

Substitute into

\[
16a+C=6.
\]

\[
16\left(-\frac59\right)+C=6.
\]

\[
-\frac{80}{9}+C=6.
\]

Write `6` as ninths:

\[
6=\frac{54}{9}.
\]

So

\[
C=\frac{54}{9}+\frac{80}{9}=\frac{134}{9}.
\]

Therefore

\[
\boxed{y=-\frac59(x-5)^2+\frac{134}{9}.}
\]

This negative `a`-value makes sense because the ball’s path is upside-down U-shaped.

### Find when the ball reaches the ground

The ball reaches the ground when

\[
y=0.
\]

So solve

\[
0=-\frac59(x-5)^2+\frac{134}{9}.
\]

Move the squared term to the other side:

\[
\frac59(x-5)^2=\frac{134}{9}.
\]

Multiply both sides by `9`:

\[
5(x-5)^2=134.
\]

Divide by `5`:

\[
(x-5)^2=\frac{134}{5}.
\]

Square root both sides:

\[
x-5=\pm\sqrt{\frac{134}{5}}.
\]

Add `5`:

\[
x=5\pm\sqrt{\frac{134}{5}}.
\]

Now

\[
\sqrt{\frac{134}{5}}\approx5.18.
\]

So

\[
x\approx5+5.18=10.18
\]

or

\[
x\approx5-5.18=-0.18.
\]

The negative horizontal distance is not meaningful for the forward path described in the question, so

\[
\boxed{x\approx10.18\text{ m}.}
\]

[VISUAL PLACEHOLDER: AS1QuadraticsSVG-007 | Source: Transcript modelling example: tennis ball path | Insert from svg/AS1QuadraticsSVG-007.svg | Purpose: Show a projectile-style quadratic with starting point `(0,1)`, point `(9,6)`, turning line `x=5`, and ground intersection.]

## I4. Worked Example 26: Profit model in completed square form

Suppose a company’s annual profit `P`, in thousands of pounds, is modelled by

\[
P=100-6.25(x-9)^2,
\]

where `x` is the selling price in pounds.

### Find the maximum possible annual profit and the selling price that gives it

Since

\[
(x-9)^2\ge0,
\]

we know

\[
-6.25(x-9)^2\le0.
\]

So the greatest value of

\[
100-6.25(x-9)^2
\]

happens when

\[
(x-9)^2=0.
\]

That occurs when

\[
x-9=0.
\]

\[
x=9.
\]

Then

\[
P=100-6.25(0)^2=100.
\]

Since `P` is in thousands of pounds,

\[
\boxed{\text{maximum annual profit }=£100{,}000}
\]

and it occurs when

\[
\boxed{x=£9.}
\]

[VISUAL PLACEHOLDER: AS1QuadraticsSVG-008 | Source: CCEA AS1-AF-LO004 + discriminant examples | Insert from svg/AS1QuadraticsSVG-008.svg | Purpose: Display discriminant sign table with graph interpretation.]

[VISUAL PLACEHOLDER: AS1QuadraticsSVG-009 | Source: Spear model transcript example | Insert from svg/AS1QuadraticsSVG-009.svg | Purpose: Show `h(t)=23.275-4.9(t-1.5)^2` as a height-time parabola with maximum labelled.]

[INTERACTIVE PLACEHOLDER: AS1QuadraticsWidget-003 | Source: CCEA AS1-AF-LO004 + discriminant lesson evidence | Insert from widgets/AS1QuadraticsWidget-003.html | Purpose: Let the student vary `a`, `b`, and `c`, observe `b^2-4ac`, and see the number of real roots.]

[INTERACTIVE PLACEHOLDER: AS1QuadraticsWidget-004 | Source: Quadratic modelling examples | Insert from widgets/AS1QuadraticsWidget-004.html | Purpose: Let the student adjust a projectile model and read off starting height, maximum height, time/distance at maximum, and ground intersection.]

---

## Common Mistakes and Exam Traps Continued

| Trap | Why it loses marks | Safer exam habit |
|---|---|---|
| Drawing a fully scaled graph when asked for a sketch | Wastes time and may distract from key features | Sketch shape, roots, intercepts and turning point |
| Forgetting the y-intercept | A graph sketch often needs all intercepts | Set `x=0` |
| Calling roots “y-values” | Roots are x-values where y=0 | Write roots as `x=...` or points `(x,0)` |
| Using `a(x+h)^2+k` for turning point `(h,k)` | Sign is reversed inside the bracket | Use `a(x-h)^2+k` |
| Missing the extra `a` in root form | Roots alone do not determine one unique quadratic | Use `y=a(x-r1)(x-r2)` |
| Discriminant sign confusion | Root count becomes wrong | Memorise: `>0` two, `=0` repeated, `<0` none |
| Forgetting to reverse an inequality after dividing by a negative | Gives the wrong parameter range | Circle the negative divisor before dividing |
| Keeping negative time or distance in a model | May be algebraically valid but contextually impossible | Check the domain, such as `t>=0` or `x>=0` |
| Treating `P=100` as £100 instead of £100,000 | Units are part of the answer | Read whether profit is in pounds, thousands, metres, seconds, etc. |

---

## Exam Technique Notes

1. For graph sketching, build the sketch from features:
   \[
   \text{shape} \rightarrow \text{roots} \rightarrow y\text{-intercept} \rightarrow \text{turning point}.
   \]
2. For roots, set `y=0` or `f(x)=0`.
3. For y-intercepts, set `x=0`.
4. For turning points, complete the square.
5. For equal roots, use `b^2-4ac=0`.
6. For two distinct real roots, use `b^2-4ac>0`.
7. For no real roots, use `b^2-4ac<0`.
8. For modelling, always interpret the answer in context.

---

# Guided Practice

## Practice Questions

### Q1. Solve by factorisation

Solve

\[
x^2+7x+12=0.
\]

### Q2. Solve without expanding

Solve

\[
(3x-2)^2=11.
\]

### Q3. Solve a disguised quadratic

Solve

\[
x-5\sqrt{x}+6=0.
\]

### Q4. Complete the square

Write

\[
x^2+10x-3
\]

in completed square form.

### Q5. Complete the square with a coefficient

Write

\[
4x^2-16x+9
\]

in the form

\[
a(x+b)^2+c.
\]

### Q6. Solve by completing the square

Solve

\[
2x^2+8x-5=0
\]

by completing the square.

### Q7. Function roots

Let

\[
f(x)=2x^2-5x-3.
\]

Find the roots of `f(x)`.

### Q8. Minimum value

Find the minimum value of

\[
f(x)=3x^2+18x+11
\]

and state the value of `x` for which it occurs.

### Q9. Sketching information

For

\[
y=x^2-2x-8,
\]

find:

1. the x-intercepts;
2. the y-intercept;
3. the turning point;
4. the line of symmetry.

### Q10. Discriminant classification

For

\[
3x^2-5x+7=0,
\]

use the discriminant to state the number of real roots.

### Q11. Parameter discriminant

Find the range of values of `k` for which

\[
x^2+6x+k=0
\]

has two distinct real roots.

### Q12. Modelling with a quadratic

A ball’s height `h` metres after `t` seconds is modelled by

\[
h(t)=1+8t-4t^2,\qquad t\ge0.
\]

1. Interpret the constant term.
2. Find when the ball hits the ground.
3. Write `h(t)` in completed square form.
4. State the maximum height and when it occurs.

---

# Full Worked Solutions

## Solution to Q1

Solve

\[
x^2+7x+12=0.
\]

Find two numbers that multiply to `12` and add to `7`. These are `3` and `4`.

So

\[
x^2+7x+12=(x+3)(x+4).
\]

Therefore

\[
(x+3)(x+4)=0.
\]

So

\[
x=-3 \quad \text{or} \quad x=-4.
\]

## Solution to Q2

Solve

\[
(3x-2)^2=11.
\]

The unknown appears only once, so do not expand.

Square root both sides:

\[
3x-2=\pm\sqrt{11}.
\]

Add `2`:

\[
3x=2\pm\sqrt{11}.
\]

Divide by `3`:

\[
x=\frac{2\pm\sqrt{11}}{3}.
\]

## Solution to Q3

Solve

\[
x-5\sqrt{x}+6=0.
\]

Let

\[
y=\sqrt{x}.
\]

Then

\[
y^2=x.
\]

Substitute:

\[
y^2-5y+6=0.
\]

Factorise:

\[
y^2-5y+6=(y-2)(y-3).
\]

So

\[
y=2 \quad \text{or} \quad y=3.
\]

Return to `x`:

\[
\sqrt{x}=2 \quad \text{or} \quad \sqrt{x}=3.
\]

Square both sides:

\[
x=4 \quad \text{or} \quad x=9.
\]

## Solution to Q4

Write

\[
x^2+10x-3
\]

in completed square form.

Half the coefficient of `x`:

\[
\frac{10}{2}=5.
\]

So

\[
x^2+10x=(x+5)^2-25.
\]

Now include the `-3`:

\[
x^2+10x-3=(x+5)^2-25-3.
\]

\[
x^2+10x-3=(x+5)^2-28.
\]

## Solution to Q5

Write

\[
4x^2-16x+9
\]

in the form

\[
a(x+b)^2+c.
\]

Factor out `4` from the `x^2` and `x` terms:

\[
4x^2-16x+9=4(x^2-4x)+9.
\]

Complete the square inside the bracket:

\[
x^2-4x=(x-2)^2-4.
\]

Substitute:

\[
4(x^2-4x)+9=4\left((x-2)^2-4\right)+9.
\]

Expand:

\[
=4(x-2)^2-16+9.
\]

Simplify:

\[
=4(x-2)^2-7.
\]

## Solution to Q6

Solve

\[
2x^2+8x-5=0
\]

by completing the square.

Because this is an equation, divide both sides by `2`:

\[
x^2+4x-\frac52=0.
\]

Complete the square:

\[
x^2+4x=(x+2)^2-4.
\]

So

\[
(x+2)^2-4-\frac52=0.
\]

Combine constants:

\[
-4-\frac52=-\frac{8}{2}-\frac52=-\frac{13}{2}.
\]

So

\[
(x+2)^2-\frac{13}{2}=0.
\]

Add `13/2` to both sides:

\[
(x+2)^2=\frac{13}{2}.
\]

Square root both sides:

\[
x+2=\pm\sqrt{\frac{13}{2}}.
\]

Subtract `2`:

\[
x=-2\pm\sqrt{\frac{13}{2}}.
\]

## Solution to Q7

Let

\[
f(x)=2x^2-5x-3.
\]

Roots mean

\[
f(x)=0.
\]

So

\[
2x^2-5x-3=0.
\]

Factorise:

\[
2x^2-5x-3=(2x+1)(x-3).
\]

So

\[
(2x+1)(x-3)=0.
\]

Therefore

\[
x=-\frac12 \quad \text{or} \quad x=3.
\]

## Solution to Q8

Find the minimum value of

\[
f(x)=3x^2+18x+11.
\]

Factor out `3` from the `x^2` and `x` terms:

\[
f(x)=3(x^2+6x)+11.
\]

Complete the square:

\[
x^2+6x=(x+3)^2-9.
\]

Substitute:

\[
f(x)=3\left((x+3)^2-9\right)+11.
\]

Expand:

\[
f(x)=3(x+3)^2-27+11.
\]

Simplify:

\[
f(x)=3(x+3)^2-16.
\]

Since

\[
(x+3)^2\ge0,
\]

the smallest value of

\[
3(x+3)^2
\]

is `0`. This occurs when

\[
x+3=0.
\]

So

\[
x=-3.
\]

The minimum value is therefore `-16`.

## Solution to Q9

For

\[
y=x^2-2x-8,
\]

### 1. x-intercepts

Set

\[
y=0.
\]

\[
x^2-2x-8=0.
\]

Factorise:

\[
x^2-2x-8=(x-4)(x+2).
\]

So

\[
x=4 \quad \text{or} \quad x=-2.
\]

The x-intercepts are

\[
(4,0) \quad \text{and} \quad (-2,0).
\]

### 2. y-intercept

Set

\[
x=0.
\]

\[
y=0^2-2(0)-8=-8.
\]

So the y-intercept is

\[
(0,-8).
\]

### 3. Turning point

Complete the square:

\[
y=x^2-2x-8.
\]

\[
x^2-2x=(x-1)^2-1.
\]

So

\[
y=(x-1)^2-1-8.
\]

\[
y=(x-1)^2-9.
\]

Since

\[
(x-1)^2\ge0,
\]

the minimum value is `-9` and it occurs when

\[
x-1=0.
\]

So

\[
x=1.
\]

The turning point is

\[
(1,-9).
\]

### 4. Line of symmetry

The line of symmetry passes through the turning point:

\[
x=1.
\]

Also check using the roots:

\[
\frac{4+(-2)}{2}=\frac{2}{2}=1.
\]

## Solution to Q10

For

\[
3x^2-5x+7=0,
\]

identify

\[
a=3,\qquad b=-5,\qquad c=7.
\]

The discriminant is

\[
b^2-4ac.
\]

Substitute:

\[
(-5)^2-4(3)(7).
\]

Calculate:

\[
(-5)^2=25.
\]

\[
4(3)(7)=84.
\]

So

\[
b^2-4ac=25-84=-59.
\]

Since

\[
-59<0,
\]

there are no real roots.

## Solution to Q11

Find the range of `k` for which

\[
x^2+6x+k=0
\]

has two distinct real roots.

For two distinct real roots,

\[
b^2-4ac>0.
\]

Here

\[
a=1,\qquad b=6,\qquad c=k.
\]

Substitute:

\[
6^2-4(1)(k)>0.
\]

\[
36-4k>0.
\]

Subtract `36`:

\[
-4k>-36.
\]

Divide by `-4`, reversing the inequality sign:

\[
k<9.
\]

## Solution to Q12

A ball’s height is modelled by

\[
h(t)=1+8t-4t^2,\qquad t\ge0.
\]

### 1. Interpret the constant term

The constant term is the height when

\[
t=0.
\]

\[
h(0)=1+8(0)-4(0)^2=1.
\]

So the ball starts `1 m` above the ground.

### 2. Find when the ball hits the ground

The ball hits the ground when

\[
h(t)=0.
\]

So solve

\[
1+8t-4t^2=0.
\]

Rewrite:

\[
-4t^2+8t+1=0.
\]

Use the quadratic formula with

\[
a=-4,\qquad b=8,\qquad c=1.
\]

\[
t=\frac{-8\pm\sqrt{8^2-4(-4)(1)}}{2(-4)}.
\]

Simplify inside the root:

\[
8^2=64.
\]

\[
-4(-4)(1)=16.
\]

So

\[
t=\frac{-8\pm\sqrt{64+16}}{-8}.
\]

\[
t=\frac{-8\pm\sqrt{80}}{-8}.
\]

Since

\[
\sqrt{80}=\sqrt{16\cdot5}=4\sqrt5,
\]

\[
t=\frac{-8\pm4\sqrt5}{-8}.
\]

Divide numerator and denominator by `-4`:

\[
t=\frac{2\mp\sqrt5}{2}.
\]

So the two algebraic values are

\[
t=\frac{2+\sqrt5}{2}
\]

or

\[
t=\frac{2-\sqrt5}{2}.
\]

Now

\[
\frac{2-\sqrt5}{2}<0,
\]

because

\[
\sqrt5>2.
\]

But the model says

\[
t\ge0.
\]

So reject the negative time.

Therefore

\[
\boxed{t=\frac{2+\sqrt5}{2}\text{ s}.}
\]

Approximately,

\[
t\approx2.12\text{ s}.
\]

### 3. Write `h(t)` in completed square form

Start with

\[
h(t)=1+8t-4t^2.
\]

Rewrite in descending powers:

\[
h(t)=-4t^2+8t+1.
\]

Factor out `-4` from the `t^2` and `t` terms:

\[
h(t)=-4(t^2-2t)+1.
\]

Complete the square:

\[
t^2-2t=(t-1)^2-1.
\]

Substitute:

\[
h(t)=-4\left((t-1)^2-1\right)+1.
\]

Expand:

\[
h(t)=-4(t-1)^2+4+1.
\]

\[
h(t)=5-4(t-1)^2.
\]

### 4. State the maximum height and when it occurs

Since

\[
(t-1)^2\ge0,
\]

we know

\[
-4(t-1)^2\le0.
\]

So the maximum occurs when

\[
(t-1)^2=0.
\]

That means

\[
t-1=0.
\]

\[
t=1.
\]

Then

\[
h(1)=5-4(0)^2=5.
\]

So the maximum height is

\[
\boxed{5\text{ m}}
\]

and it occurs when

\[
\boxed{t=1\text{ s}.}
\]

---

# Common CCEA-Style Wording

| Wording | What to do |
|---|---|
| “Solve the equation” | Find the value or values of the unknown |
| “Solve by factorisation” | Rearrange to `ax^2+bx+c=0`, factorise, set factors equal to zero |
| “Solve by completing the square” | Put into completed square form, then use inverse operations |
| “Write in the form `a(x+b)^2+c`” | Complete the square |
| “Find the roots of `f(x)`” | Solve `f(x)=0` |
| “Find the coordinates of the turning point” | Complete the square and read off `(h,k)` |
| “Sketch the graph” | Show shape, intercepts, roots, turning point and line of symmetry |
| “Has equal roots” | Use `b^2-4ac=0` |
| “Has two distinct real roots” | Use `b^2-4ac>0` |
| “Has no real roots” | Use `b^2-4ac<0` |
| “Interpret the constant term” | Substitute input `0`, then explain in context |
| “According to the model” | Answer using the equation and then interpret sensibly |

---

# Consolidated Exam Technique

## Method-choice guide

| Equation type | Preferred method |
|---|---|
| Factorises cleanly | Factorisation |
| Has awkward coefficients or surd roots | Quadratic formula |
| Asks “by completing the square” | Completing the square |
| Unknown appears once inside a squared bracket | Square root both sides |
| Involves `sqrt(x)`, `x^2`, `e^x`, `sin x`, etc. | Treat as quadratic in a function of the unknown |
| Asks about number of roots only | Discriminant |
| Asks for turning point or maximum/minimum | Completing the square |
| Gives roots of graph | Use `y=a(x-r1)(x-r2)` |
| Gives turning point | Use `y=a(x-h)^2+k` |
| Gives three points | Use `y=ax^2+bx+c` and simultaneous equations |

---

# Syllabus Gap Check

| LO ID | Coverage in this lesson | Status |
|---|---|---|
| AS1-AF-LO003 | Quadratic functions, roots, graph features, turning points, sketching | Covered |
| AS1-AF-LO004 | Discriminant, repeated roots, distinct real roots, no real roots, parameter inequalities | Covered |
| AS1-AF-LO005 | Completing the square for `x^2+bx+c` and `ax^2+bx+c`, turning points | Covered |
| AS1-AF-LO006 | Factorisation, formula, completing square, disguised quadratics | Covered |
| AS1-AF-LO012 | Sketching quadratic polynomial graphs | Supported |
| AS1-AF-LO014 | Interpreting algebraic roots graphically | Supported |

## Evidence limitations

| Limitation | Action taken |
|---|---|
| No pasted CCEA extract was provided in the user message | Pre-loaded CCEA specification map used |
| Topic-specific README/module map was not pasted | Project-wide README used; topic inferred from AS1-AF and quadratics evidence |
| Topic-specific evidence checklist was not pasted | Project-wide checklist used |
| Textbook exercises referenced in slides were not fully provided | Unseen textbook content not reproduced |
| Screenshot PDF has no parsed text | Used only as visual support, not as independent mathematical text |
| Dr Frost/Pearson source is not CCEA-specific | Used only where CCEA AS1-AF confirms the material is on-spec |

---

# Off-Spec Content Found but Excluded

| Evidence item | Decision |
|---|---|
| MAT/UKMT-style extension references | Optional enrichment only, not core CCEA requirement |
| Complex/imaginary solutions | Mentioned only to justify “no real roots”; not treated as AS1 core solving |
| Further Maths integration using completing the square | Excluded from core |
| General competition extension database links | Excluded from core |
| Riemann Zeta / Clay prize references from summary content | Excluded from core |

---

# Visual and Interactive Asset Plan

## SVG assets planned

| Asset ID | Purpose |
|---|---|
| AS1QuadraticsSVG-001 | Six-part quadratics chapter map |
| AS1QuadraticsSVG-002 | Method comparison for solving quadratics |
| AS1QuadraticsSVG-003 | Completing-the-square algebra transformation |
| AS1QuadraticsSVG-004 | Completed square form and turning point |
| AS1QuadraticsSVG-005 | Sketch of `y=x^2+4x-5` |
| AS1QuadraticsSVG-006 | Discriminant graph cases |
| AS1QuadraticsSVG-007 | Tennis ball projectile-style model |
| AS1QuadraticsSVG-008 | Discriminant sign table |
| AS1QuadraticsSVG-009 | Spear height-time model |

## Mermaid assets planned

| Asset ID | Purpose |
|---|---|
| AS1QuadraticsMermaid-001 | Solving-method decision flowchart |
| AS1QuadraticsMermaid-002 | Quadratic graph sketching checklist |
| AS1QuadraticsMermaid-003 | Discriminant decision tree |
| AS1QuadraticsMermaid-004 | Modelling workflow: equation, solve, interpret |

## TikZ assets planned

| Asset ID | Purpose |
|---|---|
| AS1QuadraticsTikZ-001 | Generic parabola with roots, intercept and turning point |
| AS1QuadraticsTikZ-002 | Three discriminant graph cases |
| AS1QuadraticsTikZ-003 | Projectile path diagram |
| AS1QuadraticsTikZ-004 | Completed square vertex form diagram |

## Widgets planned

| Asset ID | Purpose |
|---|---|
| AS1QuadraticsWidget-001 | Classify best solving method |
| AS1QuadraticsWidget-002 | Slider for `a(x+b)^2+c` and turning point |
| AS1QuadraticsWidget-003 | Discriminant explorer |
| AS1QuadraticsWidget-004 | Projectile model explorer |

---

# Supplementary Sources Used

| Source | Status |
|---|---|
| CCEA GCE Mathematics Specification Map | Core authority |
| Project README/module map | Project metadata and file conventions |
| Project evidence checklist | Evidence logging and placeholder rules |
| Dr Frost/Pearson quadratics lesson PDF | Lesson content support, controlled by CCEA boundary |
| Teacher transcript | Lesson content support, controlled by CCEA boundary |
| Screenshot PDF | Visual support only |

No external web sources were used.

---

# Final Student Checklist

## Solving

- [ ] I can put a quadratic into the form `ax^2+bx+c=0`.
- [ ] I can solve by factorisation.
- [ ] I can solve by the quadratic formula.
- [ ] I can solve by completing the square.
- [ ] I remember the `±` when square-rooting.
- [ ] I know when not to expand because the unknown appears only once.
- [ ] I can solve disguised quadratics such as equations in `sqrt(x)` or `x^2`.
- [ ] I check possible false solutions after squaring.

## Completing the square

- [ ] I can complete the square for `x^2+bx+c`.
- [ ] I can complete the square for `ax^2+bx+c`.
- [ ] I know the difference between handling expressions and equations.
- [ ] I can use completed square form to find a minimum or maximum value.
- [ ] I can state both the value and the `x`-value where it occurs.

## Functions and graphs

- [ ] I know that roots of `f(x)` mean values where `f(x)=0`.
- [ ] I can find x-intercepts by setting `y=0`.
- [ ] I can find the y-intercept by setting `x=0`.
- [ ] I can find the turning point by completing the square.
- [ ] I can sketch a quadratic with its main features labelled.
- [ ] I can find an equation from roots, a turning point or three points.

## Discriminant

- [ ] I know the discriminant is `b^2-4ac`.
- [ ] I know `b^2-4ac>0` means two distinct real roots.
- [ ] I know `b^2-4ac=0` means one repeated real root.
- [ ] I know `b^2-4ac<0` means no real roots.
- [ ] I can form and solve inequalities involving the discriminant.

## Modelling

- [ ] I can interpret `h(0)`, `P(0)`, or another constant term in context.
- [ ] I can solve `h(t)=0` or `P(x)=0` and reject impossible values.
- [ ] I can use completed square form to find a maximum height or maximum profit.
- [ ] I include correct units in final answers.
- [ ] I remember that a mathematical answer must make sense in the context.
