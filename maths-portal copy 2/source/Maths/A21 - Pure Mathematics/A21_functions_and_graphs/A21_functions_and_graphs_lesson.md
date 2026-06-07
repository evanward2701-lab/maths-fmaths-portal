# A21 Functions and Graphs

## Title and Metadata

| Field | Value |
|---|---|
| Course | CCEA GCE Mathematics |
| Unit | A2 1 Pure Mathematics |
| Unit code | `A21` |
| Topic code | `A21-AF` |
| Topic name | Algebra and functions |
| Lesson focus | Functions and Graphs |
| Topic slug | `functions_and_graphs` |
| Topic Pascal | `FunctionsAndGraphs` |
| Topic ID | `A21FunctionsAndGraphs` |
| Lesson file | `A21_functions_and_graphs_lesson.md` |
| Core LO IDs | `A21-AF-LO002`, `A21-AF-LO003`, `A21-AF-LO004`, `A21-AF-LO005`, `A21-AF-LO006`, `A21-AF-LO007` |
| Adjacent but not core | `A21-AF-LO001`, `A21-AF-LO008`, `A21-AF-LO009` |
| Tags | `#A21`, `#AlgebraFunctions`, `#Functions`, `#DomainRange`, `#CompositeFunctions`, `#InverseFunctions`, `#Modulus`, `#TransformGraphs` |

---

## Evidence Map

| Evidence source | Used for | Status |
|---|---|---|
| CCEA GCE Mathematics Specification Map | Unit, topic code, LO IDs and official boundaries | Core authority |
| Project README Module Map | Metadata rules, file naming and phase structure | Project authority |
| Project Evidence Drop Checklist | Missing evidence and off-spec logging format | Project authority |
| Chapter 2 Functions and Graphs transcript | Teacher explanations, warnings and worked-example flow | Core lesson evidence where on-spec |
| P2 Chapter 2 Functions and Graphs PDF | Slide definitions, example statements, diagrams and worked solutions | Core lesson evidence where on-spec |
| Screenshots PDF | Visual reference only | Visual-only, not fully parsed |
| Edexcel/Pearson/MAT/SMC labels inside evidence | Potential enrichment or cross-board examples | Controlled by CCEA boundary |

---

## Specification Alignment

| LO ID | Lesson coverage |
|---|---|
| `A21-AF-LO002` | Definition of mapping and function; vertical ray test; why a mapping may fail to be a function. |
| `A21-AF-LO003` | Domain and range; finite domains; restricted intervals; ranges of common functions; range by completing the square. |
| `A21-AF-LO004` | Composite functions; notation `gf(x)=g(f(x))`; `fg(x)=f(g(x))`; repeated functions. |
| `A21-AF-LO005` | Inverse functions; one-to-one condition; inverse notation; rearranging; inverse graphs as reflections in `y=x`. |
| `A21-AF-LO006` | Modulus definition; sketching `y=|x|`, `y=|ax+b|`; solving modulus equations and inequalities. |
| `A21-AF-LO007` | Combined transformations of `y=f(x)`; effect of inside/outside changes; `y=|f(x)|`; `y=f(|x|)`. |

---

## Learning Objectives

By the end of this lesson, the student should be able to:

1. Explain the modulus function as a non-negative numerical value.
2. Sketch `y=|x|`, `y=|ax+b|`, `y=|f(x)|` and `y=f(|x|)`.
3. Solve modulus equations and inequalities using a sketch plus algebra.
4. Distinguish between a mapping and a function.
5. Use the terms domain and range correctly.
6. Decide whether a function is one-to-one or many-to-one.
7. Form and simplify composite functions such as `fg(x)`, `gf(x)` and `f^2(x)`.
8. Find inverse functions algebraically.
9. Sketch inverse functions and state their domains/ranges.
10. Apply combined graph transformations carefully, especially when transformations affect `x`-values oppositely.

> Tiny warning bell: notation is not decoration. The difference between `fg(x)`, `f(g(x))`, `f^{-1}(x)`, `|f(x)|` and `f(|x|)` is the whole game.

---

## Prerequisite Recap

This lesson relies on earlier A-Level skills only:

- Straight-line sketching, especially gradient and intercept.
- Solving simultaneous equations by finding intersections.
- Solving linear and quadratic equations.
- Completing the square.
- Sketching common graphs such as `y=x`, `y=x^2`, `y=1/x`, `y=e^x`, and `y=ln x`.
- Basic graph transformations: `y=af(x)`, `y=f(x)+a`, `y=f(x+a)`, `y=f(ax)`.
- Interval notation and inequality notation.
- Recognising graph intersections as solutions to equations.

No GCSE source is used as evidence here. Earlier school ideas may be familiar, but this pack is built from A-Level evidence and the CCEA A21 boundary.

---

## Big Picture Explanation

Functions are mathematical machines with rules. This chapter is about learning how those machines behave when we restrict inputs, combine functions, reverse functions, fold negative outputs upwards using modulus, transform graphs, and solve equations by reading intersections.

A function question often looks algebraic, but there is usually a graph hiding in the rafters. The best solutions come when the algebra and sketch are made to agree.

---

## Key Definitions and Notation

### Modulus

The modulus of a number `a`, written `|a|`, is its **non-negative numerical value**.

Examples:

```math
|6|=6
```

```math
|-7.1|=7.1
```

The modulus is useful for expressing a **difference** as a positive value. If `b<a`, then `b-a` is negative, but the size of the difference is:

```math
|b-a|.
```

The modulus gives the **magnitude** or **size** of a value.

### Mapping

A **mapping** maps one set of numbers to another. A mapping can be arbitrary, or it can have a rule such as:

```math
x\mapsto 2x.
```

In a general mapping, one input may map to multiple outputs, multiple inputs may map to one output, and not every possible input necessarily needs a mapped output.

### Domain

The **domain** is the set of possible inputs. For graphs and functions, the domain is usually the set of allowed `x`-values.

### Range

The **range** is the set of possible outputs. For graphs and functions, the range is usually the set of possible `y`-values, written in terms of `f(x)`, `g(x)`, etc.

Important notation warning:

- `x` belongs to the domain.
- `f(x)` belongs to the range.

So a range should be written using `f(x)`, not `x`, unless you are explicitly describing output values as `y`-values.

### Function

A **function** is a mapping such that every element of the domain is mapped to **exactly one** element of the range.

That means one input cannot produce two outputs, one input cannot produce no output, but multiple inputs may produce the same output.

### Vertical Ray Test

A graph represents a function if a vertical line or vertical ray never hits the graph more than once. If a vertical ray hits the curve multiple times, then one input gives multiple outputs, so it is **not** a function.

### One-to-one and Many-to-one

A function is **one-to-one** if each output has exactly one input.

A function is **many-to-one** if different inputs can produce the same output.

Example:

```math
f(x)=x^2
```

is many-to-one on `x in R`, since:

```math
f(2)=4
```

and

```math
f(-2)=4.
```

A horizontal ray test can help decide whether a function is one-to-one or many-to-one.

### Composite Function

Sometimes we apply one function after another. These combined functions are called **composite functions**.

```math
gf(x)=g(f(x)).
```

This means apply `f` first, then apply `g`.

### Inverse Function

An inverse function `f^{-1}` reverses the original function `f`.

If:

```math
f(4)=2,
```

then:

```math
f^{-1}(2)=4.
```

For an inverse function to exist as a function, the original function must be **one-to-one**. If the original function is many-to-one, then the inverse mapping would be one-to-many, which is not a function.

### Graph of an Inverse Function

The graphs of `y=f(x)` and `y=f^{-1}(x)` are reflections of each other in the line:

```math
y=x.
```

Also, the domain of `f` is the range of `f^{-1}`, and the range of `f` is the domain of `f^{-1}`.

---

## Core Theory

### A. The Modulus Function

The modulus function makes an expression non-negative.

```math
|a| =
\begin{cases}
a, & a\ge 0,\\
-a, & a<0.
\end{cases}
```

Examples:

```math
|6|=6
```

because `6` is already positive.

```math
|-7.1|=7.1
```

because the modulus takes the positive magnitude.

### B. Evaluating a Modulus Function

Suppose:

```math
f(x)=|2x-3|+1.
```

This means:

1. take the input `x`;
2. multiply by `2`;
3. subtract `3`;
4. make the result non-negative;
5. add `1`.

#### Example: Find `f(5)`

```math
f(5)=|2(5)-3|+1
```

```math
=|10-3|+1
```

```math
=|7|+1
```

```math
=7+1
```

```math
=8.
```

#### Example: Find `f(-2)`

```math
f(-2)=|2(-2)-3|+1
```

```math
=|-4-3|+1
```

```math
=|-7|+1
```

```math
=7+1
```

```math
=8.
```

#### Example: Find `f(1)`

```math
f(1)=|2(1)-3|+1
```

```math
=|2-3|+1
```

```math
=|-1|+1
```

```math
=1+1
```

```math
=2.
```

Important observation: `f(5)=8` and `f(-2)=8`. Different inputs can give the same output. That is allowed for a function.

### C. The Graph of `y=|x|`

Use a table of values:

| `x` | `-2` | `-1` | `0` | `1` | `2` |
|---|---:|---:|---:|---:|---:|
| `y=|x|` | `2` | `1` | `0` | `1` | `2` |

The graph passes through:

```math
(-2,2),\quad (-1,1),\quad (0,0),\quad (1,1),\quad (2,2).
```

It is a V-shaped graph with vertex `(0,0)`. The graph `y=x` would normally have negative `y`-values for `x<0`; the modulus function reflects that negative part upwards.

[VISUAL PLACEHOLDER: A21FunctionsAndGraphsSVG-001 | Source: P2 Chapter 2 slide page 6 + transcript section 1 | Insert from svg/A21FunctionsAndGraphsSVG-001.svg | Purpose: Show the table and V-shaped graph of `y=|x|`.]

### D. Sketching `y=|ax+b|`

To sketch:

```math
y=|ax+b|,
```

first sketch:

```math
y=ax+b,
```

then reflect upwards any section below the `x`-axis.

General method:

1. Sketch the non-modulus graph `y=ax+b`, usually as a dotted line.
2. Keep the part above the `x`-axis.
3. Reflect the part below the `x`-axis upwards.
4. Label important points, especially intercepts and the vertex.

### E. Example: Sketch `y=|2x-3|`

First sketch:

```math
y=2x-3.
```

This line has positive gradient `2`, crosses the `y`-axis at `-3`, and crosses the `x`-axis where:

```math
2x-3=0
```

```math
2x=3
```

```math
x=\frac32.
```

So the line crosses the `x`-axis at:

```math
\left(\frac32,0\right).
```

Now reflect the part below the `x`-axis upwards.

The reflected part is:

```math
y=-(2x-3)
```

```math
y=-2x+3
```

or:

```math
y=3-2x.
```

So the graph of `y=|2x-3|` is made of two pieces:

```math
y=
\begin{cases}
3-2x, & x<\frac32,\\
2x-3, & x\ge \frac32.
\end{cases}
```

[VISUAL PLACEHOLDER: A21FunctionsAndGraphsSVG-002 | Source: P2 Chapter 2 slide page 7 + transcript section 1 | Insert from svg/A21FunctionsAndGraphsSVG-002.svg | Purpose: Show `y=2x-3` as a dotted line and `y=|2x-3|` as the reflected V-shape.]

### F. Solving `|2x-3|=5`

Always start with a sketch. The equation:

```math
|2x-3|=5
```

means the graph `y=|2x-3|` intersects the horizontal line `y=5`.

#### Intersection with the unreflected branch

```math
2x-3=5
```

```math
2x=8
```

```math
x=4.
```

#### Intersection with the reflected branch

```math
3-2x=5
```

```math
-2x=2
```

```math
x=-1.
```

Therefore:

```math
\boxed{x=-1\text{ or }x=4.}
```

### G. Why the Sketch Matters

It is tempting to always solve both `ax+b=c` and `-(ax+b)=c`. But sometimes one algebraic solution is not a real intersection for the graph and line. The sketch tells you which branch actually intersects.

### H. Solving `|3x-5|=2-1/2x`

We solve:

```math
|3x-5|=2-\frac12x.
```

The graph `y=|3x-5|` is formed from `y=3x-5` and its reflected branch `y=5-3x`.

#### Intersection with `y=3x-5`

```math
3x-5=2-\frac12x
```

```math
3x=7-\frac12x
```

```math
3x+\frac12x=7
```

```math
\frac72x=7
```

```math
x=2.
```

#### Intersection with `y=5-3x`

```math
5-3x=2-\frac12x
```

```math
3-3x=-\frac12x
```

```math
3=\frac52x
```

```math
x=\frac65.
```

Therefore:

```math
\boxed{x=\frac65\text{ or }x=2.}
```

### I. Solving `|3x-5|>2-1/2x`

Use the graph from the previous example. We want:

```math
|3x-5|>2-\frac12x.
```

That means `y=|3x-5|` must be above `y=2-1/2x`.

The critical values are:

```math
x=\frac65
```

and:

```math
x=2.
```

By observing the sketch, the modulus graph is above the line outside the interval:

```math
\boxed{x<\frac65\text{ or }x>2.}
```

In set notation:

```math
\boxed{\{x:x<\frac65\}\cup\{x:x>2\}.}
```

[VISUAL PLACEHOLDER: A21FunctionsAndGraphsSVG-003 | Source: P2 Chapter 2 slide page 7 + transcript section 1 | Insert from svg/A21FunctionsAndGraphsSVG-003.svg | Purpose: Show intersections and inequality regions for `|3x-5|>2-1/2x`.]

### J. A One-Solution Modulus Equation

Solve:

```math
|x+1|=2x+5.
```

A sketch shows that the line `y=2x+5` intersects only the reflected branch of `y=|x+1|`.

The reflected branch is:

```math
y=-(x+1)
```

```math
y=-x-1.
```

So solve:

```math
-x-1=2x+5
```

```math
-1=3x+5
```

```math
-6=3x
```

```math
x=-2.
```

Therefore:

```math
\boxed{x=-2.}
```

### K. A Modulus Inequality with Two Critical Values

Solve:

```math
|4x-1|<2x.
```

Find the critical values.

Unreflected branch:

```math
4x-1=2x
```

```math
2x=1
```

```math
x=\frac12.
```

Reflected branch:

```math
-(4x-1)=2x
```

```math
1-4x=2x
```

```math
1=6x
```

```math
x=\frac16.
```

The graph `y=|4x-1|` is below `y=2x` between the intersections, so:

```math
\boxed{\frac16<x<\frac12.}
```

### L. Tricky Modulus Parameter Question

Suppose:

```math
|6-x|=\frac12x+k
```

has exactly one solution. Find `k`, and state the solution.

Sketch:

```math
y=|6-x|.
```

The unmodded line is:

```math
y=6-x.
```

This has `y`-intercept `6`, `x`-intercept `6`, and after applying modulus the graph has vertex:

```math
(6,0).
```

The line:

```math
y=\frac12x+k
```

has gradient `1/2`. For exactly one solution, it must pass through the vertex `(6,0)`.

Substitute `x=6`, `y=0`:

```math
0=\frac12(6)+k
```

```math
0=3+k
```

```math
k=-3.
```

So:

```math
\boxed{k=-3.}
```

The solution of the equation is the `x`-coordinate of the single intersection:

```math
\boxed{x=6.}
```

If asked for no solutions, the line must be below this threshold:

```math
\boxed{k<-3.}
```

[VISUAL PLACEHOLDER: A21FunctionsAndGraphsSVG-004 | Source: Transcript section 3 | Insert from svg/A21FunctionsAndGraphsSVG-004.svg | Purpose: Show why exactly one solution occurs when the line passes through the vertex of `y=|6-x|`.]

---

## Mappings, Functions, Domain and Range

### M. What is a Mapping?

A mapping sends inputs to outputs.

Example of a rule-based mapping:

```math
x\mapsto 2x.
```

A mapping may allow one input to map to multiple outputs, multiple inputs to map to one output, and some possible inputs not to map at all.

### N. What is a Function?

A function is a mapping such that every element of the domain maps to exactly one element of the range.

Notation examples:

```math
f(x)=2x+1
```

or:

```math
f:x\mapsto 2x+1.
```

### O. Function or Not a Function?

#### Example 1: `f(x)=2^x`, `x in R`

For every real input `x`, there is exactly one output. So this is a function.

#### Example 2: `f(x)=±sqrt(x)`, domain `x≥0`

For:

```math
x=4,
```

we get:

```math
f(4)=2
```

and:

```math
f(4)=-2.
```

One input gives two outputs, so it is **not** a function.

#### Example 3: `f(x)=sqrt(x)`, domain `x in R`

If the domain is all real numbers, then `x=-1` is included in the domain. But `sqrt(-1)` is not a real output. So not every input maps to an output. With domain `R`, this is not a real-valued function.

### P. One-to-One and Many-to-One

A function may be many-to-one.

Example:

```math
f(x)=x^2.
```

Then:

```math
f(2)=2^2=4
```

and:

```math
f(-2)=(-2)^2=4.
```

Different inputs give the same output. This is still a function because each input gives exactly one output.

A one-to-one function has each output paired with exactly one input. Example: `f(x)=2x+1` is one-to-one on `R`.

[VISUAL PLACEHOLDER: A21FunctionsAndGraphsMER-001 | Source: P2 Chapter 2 slides pages 10-12 + transcript section 4 | Insert from mermaid/A21FunctionsAndGraphsMER-001.md | Purpose: Mapping diagram comparing a general mapping, a function, a one-to-one function and a many-to-one function.]

### Q. Finding Ranges

The range is the possible set of output values. Use a graph or graph knowledge to reason about the range. Substituting endpoints alone may miss a turning point.

#### Example: Finite Domain

Let:

```math
f(x)=3x-2,
```

with domain:

```math
\{1,2,3,4\}.
```

Evaluate each allowed input:

```math
f(1)=3(1)-2=1
```

```math
f(2)=3(2)-2=6-2=4
```

```math
f(3)=3(3)-2=9-2=7
```

```math
f(4)=3(4)-2=12-2=10
```

Therefore the range is:

```math
\boxed{\{1,4,7,10\}.}
```

The function is one-to-one on this domain.

#### Example: Quadratic Domain

Let:

```math
g(x)=x^2,
```

with domain:

```math
\{x\in\mathbb R:-5\le x\le5\}.
```

The graph is a parabola with minimum:

```math
g(0)=0.
```

At the endpoints:

```math
g(-5)=(-5)^2=25
```

and:

```math
g(5)=5^2=25.
```

Therefore:

```math
\boxed{0\le g(x)\le25.}
```

This function is many-to-one on this domain.

#### Example: Reciprocal Domain

Let:

```math
h(x)=\frac1x,
```

with domain:

```math
\{x\in\mathbb R:0<x\le3\}.
```

At:

```math
x=3,
```

```math
h(3)=\frac13.
```

As `x` approaches `0` from the right, `1/x` increases without bound. So:

```math
\boxed{h(x)\ge \frac13.}
```

The output `1/3` is included because `x=3` is included.

### R. Range of a Restricted Quadratic

Let:

```math
g(x)=x^2-4x+1,
```

with:

```math
x\in\mathbb R,\qquad 0\le x\le5.
```

Complete the square:

```math
g(x)=x^2-4x+1
```

```math
=(x-2)^2-4+1
```

```math
=(x-2)^2-3.
```

The minimum occurs when `x=2`. Then:

```math
g(2)=(2-2)^2-3
```

```math
=0^2-3
```

```math
=-3.
```

Check the endpoints.

At `x=0`:

```math
g(0)=0^2-4(0)+1=1.
```

At `x=5`:

```math
g(5)=5^2-4(5)+1
```

```math
=25-20+1
```

```math
=6.
```

The range is therefore:

```math
\boxed{-3\le g(x)\le6.}
```

Warning: if you only substitute the endpoints `0` and `5`, you would get `1` and `6`, missing the minimum `-3`. This is a classic range trap.

[VISUAL PLACEHOLDER: A21FunctionsAndGraphsSVG-005 | Source: P2 Chapter 2 slide page 15 + transcript section 5 | Insert from svg/A21FunctionsAndGraphsSVG-005.svg | Purpose: Show restricted quadratic range using turning point and endpoint values.]

### S. Piecewise Functions

A piecewise function is defined in parts.

Example:

```math
f:x\mapsto
\begin{cases}
5-2x, & x<1,\\
x^2+3, & x\ge1.
\end{cases}
```

For `x<1`, use `y=5-2x`. For `x>=1`, use `y=x^2+3`.

At `x=1`, the first branch is not included and the second branch is included. Use an unfilled circle for a point that is not included, and a filled circle for a point that is included.

The range from the graph is:

```math
\boxed{f(x)>3.}
```

The value `3` is not included.

#### Solving `f(x)=19`

Use both pieces.

For `x>=1`:

```math
x^2+3=19
```

```math
x^2=16
```

```math
x=\pm4.
```

But this branch only applies when `x>=1`, so `x=4`.

For `x<1`:

```math
5-2x=19
```

```math
-2x=14
```

```math
x=-7.
```

This satisfies `x<1`, so:

```math
\boxed{x=-7\text{ or }x=4.}
```

[VISUAL PLACEHOLDER: A21FunctionsAndGraphsSVG-006 | Source: P2 Chapter 2 slide page 14 | Insert from svg/A21FunctionsAndGraphsSVG-006.svg | Purpose: Show piecewise graph with filled/unfilled endpoints and range `f(x)>3`.]

### T. Summary of Common Ranges

Use a sketch for each.

| Function | Domain | Range |
|---|---|---|
| `f(x)=x^2` | `x in R` | `f(x) >= 0` |
| `f(x)=1/x` | `x in R, x != 0` | `f(x) != 0` |
| `f(x)=ln x` | `x>0` | `f(x) in R` |
| `f(x)=e^x` | `x in R` | `f(x)>0` |

For:

```math
f(x)=x^2+2x+9,
```

complete the square:

```math
x^2+2x+9=(x+1)^2-1+9
```

```math
=(x+1)^2+8.
```

Since `(x+1)^2 >= 0`:

```math
\boxed{f(x)\ge8.}
```

For:

```math
f(x)=x^2,\qquad -1\le x\le4,
```

minimum:

```math
f(0)=0.
```

Endpoint values:

```math
f(-1)=1,\qquad f(4)=16.
```

Therefore:

```math
\boxed{0\le f(x)\le16.}
```

---

## Composite Functions

### U. Meaning of Composite Functions

If `f` and `g` are functions, then:

```math
gf(x)=g(f(x)).
```

This means apply `f` first, then apply `g`.

Similarly:

```math
fg(x)=f(g(x)).
```

This means apply `g` first, then apply `f`.

### V. Example: Composite Functions

Let:

```math
f(x)=x^2+1
```

and:

```math
g(x)=4x-2.
```

#### Find `fg(2)`

```math
fg(2)=f(g(2)).
```

First find `g(2)`:

```math
g(2)=4(2)-2
```

```math
=8-2
```

```math
=6.
```

Now apply `f`:

```math
f(g(2))=f(6)
```

```math
=6^2+1
```

```math
=36+1
```

```math
=37.
```

So:

```math
\boxed{fg(2)=37.}
```

#### Find `fg(x)`

```math
fg(x)=f(g(x)).
```

Since `g(x)=4x-2`, substitute `4x-2` into `f`:

```math
f(g(x))=f(4x-2)
```

```math
=(4x-2)^2+1.
```

Expand:

```math
(4x-2)^2=(4x-2)(4x-2)
```

```math
=16x^2-8x-8x+4
```

```math
=16x^2-16x+4.
```

Therefore:

```math
fg(x)=16x^2-16x+4+1
```

```math
\boxed{fg(x)=16x^2-16x+5.}
```

#### Find `gf(x)`

```math
gf(x)=g(f(x)).
```

Since `f(x)=x^2+1`, substitute `x^2+1` into `g`:

```math
g(f(x))=g(x^2+1)
```

```math
=4(x^2+1)-2
```

```math
=4x^2+4-2
```

```math
\boxed{gf(x)=4x^2+2.}
```

#### Find `f^2(x)`

The notation `f^2(x)` means:

```math
ff(x)=f(f(x)).
```

So:

```math
f^2(x)=f(x^2+1)
```

```math
=(x^2+1)^2+1.
```

```math
\boxed{f^2(x)=(x^2+1)^2+1.}
```

#### Solve `gf(x)=38`

We already found:

```math
gf(x)=4x^2+2.
```

So:

```math
4x^2+2=38
```

```math
4x^2=36
```

```math
x^2=9
```

```math
x=\pm3.
```

Therefore:

```math
\boxed{x=-3\text{ or }x=3.}
```

[VISUAL PLACEHOLDER: A21FunctionsAndGraphsMER-002 | Source: P2 Chapter 2 slides pages 19-20 + transcript section 8 | Insert from mermaid/A21FunctionsAndGraphsMER-002.md | Purpose: Function-machine chain showing `x -> f(x) -> g(f(x))`.]

### W. Composite Function with Modulus

Let:

```math
f:x\mapsto |2x-8|
```

and:

```math
g:x\mapsto \frac{x+1}{2}.
```

#### Find `fg(3)`

```math
fg(3)=f(g(3)).
```

First:

```math
g(3)=\frac{3+1}{2}
```

```math
=\frac42
```

```math
=2.
```

Then:

```math
f(2)=|2(2)-8|
```

```math
=|4-8|
```

```math
=|-4|
```

```math
=4.
```

So:

```math
\boxed{fg(3)=4.}
```

#### Find `fg(x)`

```math
fg(x)=f(g(x)).
```

Substitute `g(x)=(x+1)/2`:

```math
fg(x)=f\left(\frac{x+1}{2}\right)
```

```math
=\left|2\left(\frac{x+1}{2}\right)-8\right|
```

```math
=\left|x+1-8\right|
```

```math
=\boxed{|x-7|.}
```

#### Solve `fg(x)=x`

We need:

```math
|x-7|=x.
```

A sketch shows the intersection is with the reflected branch of `y=|x-7|`. The reflected branch is:

```math
y=-(x-7)
```

```math
y=-x+7.
```

So:

```math
-x+7=x
```

```math
7=2x
```

```math
x=\frac72.
```

Therefore:

```math
\boxed{x=\frac72.}
```

---

## Inverse Functions

### X. Why One-to-One is Required

An inverse reverses a function. If a function is many-to-one, then reversing it creates a one-to-many mapping. A one-to-many mapping is not a function. Therefore, an inverse function exists only when the original function is one-to-one on its stated domain.

Exam sentence to know:

> If the mapping was many-to-one, then the inverse mapping would be one-to-many, which is not a function.

### Y. Inverse Function by Reversing Operations

Let:

```math
f(x)=2x+1.
```

The original function multiplies by `2`, then adds `1`. To reverse: subtract `1`, then divide by `2`.

```math
f^{-1}(x)=\frac{x-1}{2}.
```

### Z. Inverse Function by Rearranging

The proper algebraic method is:

1. write `y=f(x)`;
2. swap `x` and `y`, or rearrange first and swap at the end;
3. make `y` the subject;
4. write the result as `f^{-1}(x)`.

#### Example: Find the inverse of `f(x)=3-4x`

Let:

```math
y=3-4x.
```

Subtract `3`:

```math
y-3=-4x.
```

Divide by `-4`:

```math
x=\frac{y-3}{-4}.
```

This can be written as:

```math
x=\frac{3-y}{4}.
```

Now swap `y` for `x` in inverse notation:

```math
\boxed{f^{-1}(x)=\frac{3-x}{4}.}
```

#### Example: Find the inverse of `f(x)=(x+2)/(2x-1)`, `x != 1/2`

Let:

```math
y=\frac{x+2}{2x-1}.
```

Multiply both sides by `2x-1`:

```math
y(2x-1)=x+2.
```

Expand:

```math
2xy-y=x+2.
```

Collect the `x`-terms on one side:

```math
2xy-x=y+2.
```

Factor out `x`:

```math
x(2y-1)=y+2.
```

Divide by `2y-1`:

```math
x=\frac{y+2}{2y-1}.
```

Replace `y` with `x`:

```math
\boxed{f^{-1}(x)=\frac{x+2}{2x-1}.}
```

This function is its own inverse.

### AA. Graphing an Inverse Function

The inverse swaps the input and output, so `y=f^{-1}(x)` is the reflection of `y=f(x)` in the line:

```math
y=x.
```

Important consequences:

- `x`-intercepts become `y`-intercepts;
- vertical asymptotes become horizontal asymptotes;
- the domain of `f` becomes the range of `f^{-1}`;
- the range of `f` becomes the domain of `f^{-1}`.

[VISUAL PLACEHOLDER: A21FunctionsAndGraphsSVG-007 | Source: P2 Chapter 2 slide page 26 + transcript section 9 | Insert from svg/A21FunctionsAndGraphsSVG-007.svg | Purpose: Show `y=f(x)`, `y=f^{-1}(x)`, and reflection in `y=x`.]

### AB. Square Root Inverse Example

Let:

```math
g(x)=\sqrt{x-2},\qquad x\ge2.
```

#### Find the range of `g`

Since a square root is always non-negative:

```math
\boxed{g(x)\ge0.}
```

#### Find `g^{-1}(x)`

Let:

```math
y=\sqrt{x-2}.
```

Square both sides:

```math
y^2=x-2.
```

Add `2`:

```math
x=y^2+2.
```

Swap `x` and `y`:

```math
\boxed{g^{-1}(x)=x^2+2.}
```

The domain of `g^{-1}` is the range of `g`:

```math
\boxed{x\ge0.}
```

The range of `g^{-1}` is the domain of `g`:

```math
\boxed{g^{-1}(x)\ge2.}
```

### AC. Restricted Quadratic Inverse Example

Let:

```math
f(x)=x^2-3,\qquad x\ge0.
```

The restriction `x>=0` is essential because without it the quadratic would be many-to-one.

#### Find `f^{-1}(x)`

Let:

```math
y=x^2-3.
```

Add `3`:

```math
y+3=x^2.
```

Since the original domain is `x>=0`, take the positive square root:

```math
x=\sqrt{y+3}.
```

Swap `x` and `y`:

```math
\boxed{f^{-1}(x)=\sqrt{x+3}.}
```

#### Solve `f(x)=f^{-1}(x)`

If a function equals its inverse, the intersection lies on `y=x`. So solve:

```math
f(x)=x.
```

That gives:

```math
x^2-3=x.
```

Rearrange:

```math
x^2-x-3=0.
```

Use the quadratic formula:

```math
x=\frac{-(-1)\pm\sqrt{(-1)^2-4(1)(-3)}}{2(1)}
```

```math
=\frac{1\pm\sqrt{1+12}}{2}
```

```math
=\frac{1\pm\sqrt{13}}{2}.
```

From the graph/domain, we need the positive solution:

```math
\boxed{x=\frac{1+\sqrt{13}}{2}.}
```

### AD. Exponential Inverse Example

Let:

```math
f(x)=e^x+2,\qquad x\in\mathbb R.
```

#### Find the inverse

Let:

```math
y=e^x+2.
```

Subtract `2`:

```math
y-2=e^x.
```

Take natural logarithms:

```math
\ln(y-2)=x.
```

Swap `x` and `y`:

```math
\boxed{f^{-1}(x)=\ln(x-2).}
```

#### Domain of the inverse

Since logarithms require positive input:

```math
x-2>0
```

```math
\boxed{x>2.}
```

This is also the range of the original function:

```math
f(x)>2.
```

---

## Transformations of Functions

### AE. Recap of Simple Transformations

| Transformation | Effect |
|---|---|
| `y=af(x)` | Multiply `y`-values by `a`. |
| `y=f(x)+a` | Add `a` to `y`-values. |
| `y=f(x+a)` | Translate left by `a`, since `x`-changes act oppositely. |
| `y=f(ax)` | Divide `x`-values by `a`, since `x`-changes act oppositely. |

Rule:

- Changes **outside** `f( )` affect `y`-values in the expected way.
- Changes **inside** `f( )` affect `x`-values in the opposite way.

### AF. Combining Transformations with Points

Suppose a graph `y=f(x)` contains points:

```math
A(2,-1)
```

and:

```math
B(6,4).
```

#### Transformation: `y=2f(x+2)`

The `x+2` is inside the function, so subtract `2` from `x`-values. The outside multiplier `2` multiplies `y`-values by `2`.

For `A(2,-1)`:

```math
x:2\mapsto 2-2=0
```

```math
y:-1\mapsto 2(-1)=-2.
```

So:

```math
A\mapsto (0,-2).
```

For `B(6,4)`:

```math
x:6\mapsto 6-2=4
```

```math
y:4\mapsto 2(4)=8.
```

So:

```math
B\mapsto (4,8).
```

#### Transformation: `y=-f(2x)`

The `2x` is inside the function, so halve the `x`-values. The negative sign outside negates the `y`-values.

For `A(2,-1)`:

```math
x:2\mapsto 1
```

```math
y:-1\mapsto 1.
```

So:

```math
A\mapsto (1,1).
```

For `B(6,4)`:

```math
x:6\mapsto 3
```

```math
y:4\mapsto -4.
```

So:

```math
B\mapsto (3,-4).
```

#### Transformation: `y=|f(-x)|`

The `-x` inside the function negates `x`-values. The modulus outside makes negative `y`-values positive.

For `A(2,-1)`:

```math
x:2\mapsto -2
```

```math
y:-1\mapsto |-1|=1.
```

So:

```math
A\mapsto (-2,1).
```

For `B(6,4)`:

```math
x:6\mapsto -6
```

```math
y:4\mapsto |4|=4.
```

So:

```math
B\mapsto (-6,4).
```

[VISUAL PLACEHOLDER: A21FunctionsAndGraphsSVG-008 | Source: P2 Chapter 2 slides pages 35-36 | Insert from svg/A21FunctionsAndGraphsSVG-008.svg | Purpose: Show point mapping under `y=2f(x+2)`, `y=-f(2x)`, and `y=|f(-x)|`.]

### AG. Sketching `y=|f(x)|`

The modulus is outside the function:

```math
y=|f(x)|.
```

So it affects the output values.

Rule:

- keep parts of `y=f(x)` above the `x`-axis;
- reflect parts below the `x`-axis upwards;
- ensure the `x`-intercepts are indicated.

Example:

If:

```math
f(x)=(x-3)(x+1),
```

then the roots are `x=3` and `x=-1`. The graph of `y=f(x)` is below the `x`-axis between `-1` and `3`, so that part is reflected upwards for `y=|f(x)|`.

### AH. Sketching `y=f(|x|)`

The modulus is inside the function:

```math
y=f(|x|).
```

So it affects the input values.

For `x<0`, `|x|` turns negative `x`-values into positive ones before they enter `f`.

Rule:

1. keep the part of `y=f(x)` for `x>=0`;
2. discard the part for `x<0`;
3. reflect the `x>=0` part into the left side using symmetry in the `y`-axis.

This graph is always symmetrical about the `y`-axis.

[VISUAL PLACEHOLDER: A21FunctionsAndGraphsSVG-009 | Source: P2 Chapter 2 slide page 31 | Insert from svg/A21FunctionsAndGraphsSVG-009.svg | Purpose: Compare `y=f(x)`, `y=|f(x)|`, and `y=f(|x|)`.]

### AI. Solving a Transformed Modulus Problem

Let:

```math
f(x)=3|x-1|-2,\qquad x\in\mathbb R.
```

#### Sketch `y=f(x)`

Start with `y=|x|`. Apply transformations in stages:

1. `y=|x-1|`: translate `1` right.
2. `y=3|x-1|`: multiply `y`-values by `3`.
3. `y=3|x-1|-2`: translate `2` down.

The vertex is:

```math
(1,-2).
```

#### State the range

Since the minimum `y`-value is `-2`:

```math
\boxed{f(x)\ge -2.}
```

#### Solve `f(x)=1/2x+3`

We solve:

```math
3|x-1|-2=\frac12x+3.
```

Use the graph and solve on each branch.

Right branch: for `x>=1`, `|x-1|=x-1`.

```math
3(x-1)-2=\frac12x+3
```

```math
3x-3-2=\frac12x+3
```

```math
3x-5=\frac12x+3
```

```math
\frac52x-5=3
```

```math
\frac52x=8
```

```math
x=\frac{16}{5}.
```

This satisfies `x>=1`, so it is valid.

Left branch: for `x<1`, `|x-1|=-(x-1)=-x+1`.

```math
3(-x+1)-2=\frac12x+3
```

```math
-3x+3-2=\frac12x+3
```

```math
-3x+1=\frac12x+3
```

```math
-3x=\frac12x+2
```

```math
-\frac72x=2
```

```math
x=-\frac47.
```

This satisfies `x<1`, so it is valid.

Therefore:

```math
\boxed{x=-\frac47\text{ or }x=\frac{16}{5}.}
```

Exam warning: only the modulus part is negated. Do **not** negate the whole equation.

[VISUAL PLACEHOLDER: A21FunctionsAndGraphsSVG-010 | Source: P2 Chapter 2 slides pages 40-42 | Insert from svg/A21FunctionsAndGraphsSVG-010.svg | Purpose: Show staged transformation of `3|x-1|-2` and intersections with `y=1/2x+3`.]

---

## Visual Asset Integration

No diagrams, TikZ files or widgets are generated inside the lesson markdown itself. The placeholders above refer to the generated assets in this pack.

| Asset ID | Type | Purpose |
|---|---|---|
| `A21FunctionsAndGraphsSVG-001` | SVG | Graph of `y=|x|`. |
| `A21FunctionsAndGraphsSVG-002` | SVG | Sketching `y=|2x-3|`. |
| `A21FunctionsAndGraphsSVG-003` | SVG | Solving modulus inequality by intersections. |
| `A21FunctionsAndGraphsSVG-004` | SVG | One-solution parameter modulus graph. |
| `A21FunctionsAndGraphsSVG-005` | SVG | Restricted quadratic range. |
| `A21FunctionsAndGraphsSVG-006` | SVG | Piecewise function graph. |
| `A21FunctionsAndGraphsSVG-007` | SVG | Inverse graph reflection in `y=x`. |
| `A21FunctionsAndGraphsSVG-008` | SVG | Combined transformations of points. |
| `A21FunctionsAndGraphsSVG-009` | SVG | `y=|f(x)|` versus `y=f(|x|)`. |
| `A21FunctionsAndGraphsSVG-010` | SVG | Solving `3|x-1|-2=1/2x+3`. |
| `A21FunctionsAndGraphsMER-001` | Mermaid | Mapping/function comparison. |
| `A21FunctionsAndGraphsMER-002` | Mermaid | Composite function machine chain. |
| `A21FunctionsAndGraphsWID-001` | Widget | Interactive transformation explorer. |
| `A21FunctionsAndGraphsWID-002` | Widget | Domain/range checker. |

[INTERACTIVE PLACEHOLDER: A21FunctionsAndGraphsWID-001 | Source: CCEA A21-AF-LO007 + lesson evidence | Insert from widgets/A21FunctionsAndGraphsWID-001.html | Purpose: Let the student adjust transformations of `f(x)`, `|f(x)|`, and `f(|x|)`.]

[INTERACTIVE PLACEHOLDER: A21FunctionsAndGraphsWID-002 | Source: CCEA A21-AF-LO003 + lesson evidence | Insert from widgets/A21FunctionsAndGraphsWID-002.html | Purpose: Let the student test domains and ranges of standard and restricted functions.]

---

## Guided Practice

### Q1. Evaluate a modulus function

Let:

```math
f(x)=|3x+2|-4.
```

Find `f(2)`, `f(-3)`, and `f(-2/3)`.

### Q2. Sketch and solve

Sketch:

```math
y=|5-2x|.
```

Then solve:

```math
|5-2x|=3.
```

### Q3. Modulus inequality

Solve:

```math
|2x+1|<7.
```

### Q4. Range from a restricted quadratic

Let:

```math
f(x)=x^2-6x+5,\qquad 1\le x\le6.
```

Find the range of `f`.

### Q5. Function or not?

Decide whether each is a function.

1. `f(x)=sqrt(x)`, domain `x>=0`.
2. `g(x)=±sqrt(x)`, domain `x>=0`.
3. `h(x)=1/x`, domain `x in R`.

### Q6. Composite functions

Let:

```math
f(x)=2x-1
```

and:

```math
g(x)=x^2+3.
```

Find `fg(x)`, `gf(x)`, and `f^2(x)`.

### Q7. Inverse function

Let:

```math
f(x)=\frac{3x+2}{x-4},\qquad x\ne4.
```

Find `f^{-1}(x)`.

### Q8. Inverse graph/domain

Let:

```math
g(x)=\sqrt{x+1},\qquad x\ge -1.
```

Find the range of `g`, `g^{-1}(x)`, and the domain of `g^{-1}`.

### Q9. Transforming points

A graph `y=f(x)` contains points:

```math
A(4,-2),\qquad B(-6,3).
```

Find the image of each point under:

```math
y=-2f(x-1).
```

### Q10. `y=|f(x)|` and `y=f(|x|)`

Suppose `f(x)=(x-2)(x+4)`. Explain how to sketch `y=|f(x)|` and `y=f(|x|)`.

---

## Common Mistakes and Exam Traps

1. **Solving modulus equations without a sketch.** A modulus equation can have two solutions, one solution or no solutions.
2. **Negating the whole equation.** In `3|x-1|-2 = 1/2x+3`, the reflected branch uses `|x-1|=-(x-1)`, not the negative of the whole expression.
3. **Confusing `fg(x)` with `gf(x)`.** Usually `fg(x) != gf(x)`.
4. **Forgetting restricted domains.** A many-to-one function may need a restricted domain before an inverse exists.
5. **Range by endpoint substitution only.** Restricted quadratics may have a turning point inside the domain.
6. **Writing a range in terms of `x`.** Domain uses `x`; range should normally use `f(x)` or `y`.
7. **Treating `f^{-1}(x)` as `1/f(x)`.** Inverse function notation is not reciprocal notation.

---

## Exam Technique Notes

### Modulus equation checklist

1. Sketch the modulus graph.
2. Sketch the other side of the equation.
3. Count likely intersections.
4. Solve using the correct branch equations.
5. Reject any branch solution that does not match the sketch/branch domain.
6. For inequalities, use the graph to decide above/below regions.

### Domain/range checklist

1. Identify the domain first.
2. Sketch the graph or recall its shape.
3. Check endpoints if the domain is restricted.
4. Check turning points/asymptotes.
5. Write the range in terms of `f(x)`, `g(x)`, etc.
6. Use strict inequalities when the value is approached but not reached.

### Composite function checklist

For `fg(x)`, read it as `f(g(x))`. Identify the inner function, substitute it into the outer function, simplify carefully, and check domain restrictions if given.

### Inverse function checklist

1. Check the function is one-to-one on its domain.
2. Let `y=f(x)`.
3. Rearrange to make `x` the subject, or swap `x,y` first.
4. Write the final result as `f^{-1}(x)`.
5. State the domain of the inverse if asked.
6. Remember: domain and range swap.

---

## Full Worked Solutions to Guided Practice

### Solution to Q1

```math
f(x)=|3x+2|-4.
```

For `f(2)`:

```math
f(2)=|3(2)+2|-4=|8|-4=8-4=\boxed{4}.
```

For `f(-3)`:

```math
f(-3)=|3(-3)+2|-4=|-9+2|-4=|-7|-4=7-4=\boxed{3}.
```

For `f(-2/3)`:

```math
f\left(-\frac23\right)=\left|3\left(-\frac23\right)+2\right|-4=|-2+2|-4=|0|-4=\boxed{-4}.
```

### Solution to Q2

Sketch `y=|5-2x|`. Start with `y=5-2x`. This crosses the `x`-axis when:

```math
5-2x=0
```

```math
5=2x
```

```math
x=\frac52.
```

So the vertex is `(5/2,0)`.

To solve:

```math
|5-2x|=3,
```

solve both branches.

Branch 1:

```math
5-2x=3
```

```math
-2x=-2
```

```math
x=1.
```

Branch 2:

```math
-(5-2x)=3
```

```math
-5+2x=3
```

```math
2x=8
```

```math
x=4.
```

Therefore:

```math
\boxed{x=1\text{ or }x=4.}
```

### Solution to Q3

```math
|2x+1|<7.
```

This means:

```math
-7<2x+1<7.
```

Subtract `1` throughout:

```math
-8<2x<6.
```

Divide by `2`:

```math
\boxed{-4<x<3.}
```

### Solution to Q4

```math
f(x)=x^2-6x+5,\qquad 1\le x\le6.
```

Complete the square:

```math
x^2-6x+5=(x-3)^2-9+5
```

```math
=(x-3)^2-4.
```

Minimum occurs at `x=3`, which is inside the domain. So:

```math
f(3)=(3-3)^2-4=0-4=-4.
```

Check endpoints:

```math
f(1)=1^2-6(1)+5=1-6+5=0.
```

```math
f(6)=6^2-6(6)+5=36-36+5=5.
```

Therefore:

```math
\boxed{-4\le f(x)\le5.}
```

### Solution to Q5

1. `f(x)=sqrt(x)`, domain `x>=0`: every input gives exactly one non-negative output. **Function**.
2. `g(x)=±sqrt(x)`, domain `x>=0`: for `x=4`, outputs are `2` and `-2`. **Not a function**.
3. `h(x)=1/x`, domain `x in R`: the input `x=0` is in the stated domain, but `1/0` is undefined. **Not a function with this domain**. If the domain were `x in R, x != 0`, it would be a function.

### Solution to Q6

```math
f(x)=2x-1,\qquad g(x)=x^2+3.
```

`fg(x)=f(g(x))`:

```math
fg(x)=f(x^2+3)=2(x^2+3)-1=2x^2+6-1=\boxed{2x^2+5}.
```

`gf(x)=g(f(x))`:

```math
gf(x)=g(2x-1)=(2x-1)^2+3.
```

Expand:

```math
(2x-1)^2=(2x-1)(2x-1)=4x^2-2x-2x+1=4x^2-4x+1.
```

So:

```math
gf(x)=4x^2-4x+1+3=\boxed{4x^2-4x+4}.
```

`f^2(x)=f(f(x))`:

```math
f^2(x)=f(2x-1)=2(2x-1)-1=4x-2-1=\boxed{4x-3}.
```

### Solution to Q7

```math
f(x)=\frac{3x+2}{x-4}.
```

Let:

```math
y=\frac{3x+2}{x-4}.
```

Multiply both sides by `x-4`:

```math
y(x-4)=3x+2.
```

Expand:

```math
xy-4y=3x+2.
```

Collect `x`-terms:

```math
xy-3x=4y+2.
```

Factor:

```math
x(y-3)=4y+2.
```

Divide:

```math
x=\frac{4y+2}{y-3}.
```

Replace `y` by `x`:

```math
\boxed{f^{-1}(x)=\frac{4x+2}{x-3}.}
```

### Solution to Q8

```math
g(x)=\sqrt{x+1},\qquad x\ge -1.
```

A square root is non-negative, so:

```math
\boxed{g(x)\ge0.}
```

Let:

```math
y=\sqrt{x+1}.
```

Square both sides:

```math
y^2=x+1.
```

Subtract `1`:

```math
x=y^2-1.
```

Swap `x` and `y`:

```math
\boxed{g^{-1}(x)=x^2-1.}
```

The domain of `g^{-1}` is the range of `g`:

```math
\boxed{x\ge0.}
```

### Solution to Q9

Original points:

```math
A(4,-2),\qquad B(-6,3).
```

Transformation:

```math
y=-2f(x-1).
```

The `x-1` is inside the function, so add `1` to `x`-values. The outside multiplier `-2` multiplies `y`-values by `-2`.

For `A(4,-2)`:

```math
x:4\mapsto 4+1=5
```

```math
y:-2\mapsto -2(-2)=4.
```

So:

```math
\boxed{A\mapsto (5,4).}
```

For `B(-6,3)`:

```math
x:-6\mapsto -6+1=-5
```

```math
y:3\mapsto -2(3)=-6.
```

So:

```math
\boxed{B\mapsto (-5,-6).}
```

### Solution to Q10

```math
f(x)=(x-2)(x+4).
```

The roots are `x=2` and `x=-4`. The graph is an upward-opening quadratic.

For `y=|f(x)|`: the modulus is outside the function, so it affects `y`-values. Keep parts of `y=f(x)` above the `x`-axis. Reflect any part below the `x`-axis upwards. The roots `x=-4` and `x=2` remain on the `x`-axis. Since the quadratic is below the `x`-axis between the roots, the section `-4<x<2` is reflected upwards.

For `y=f(|x|)`: the modulus is inside the function, so it affects `x`-values. Keep the part of `y=f(x)` for `x>=0`, reflect that right-hand part into the left-hand side, and make the final graph symmetrical about the `y`-axis.

---

## Syllabus Gap Check

| LO ID | Covered? | Notes |
|---|---|---|
| `A21-AF-LO001` | Not in core lesson | Rational expressions and algebraic division are not part of this chapter evidence. |
| `A21-AF-LO002` | Yes | Mapping/function definition and vertical ray test included. |
| `A21-AF-LO003` | Yes | Domain and range included with restricted-domain examples. |
| `A21-AF-LO004` | Yes | Composite functions covered in detail. |
| `A21-AF-LO005` | Yes | Inverse functions and inverse graphs covered. |
| `A21-AF-LO006` | Yes | Modulus function, equations and inequalities covered. |
| `A21-AF-LO007` | Yes | Combined transformations and modulus transformations covered. |
| `A21-AF-LO008` | No | Partial fractions excluded for separate lesson. |
| `A21-AF-LO009` | Partial only | Functions in modelling is not strongly evidenced here. Only general modelling awareness is included. |

---

## Visual and Interactive Asset Plan

The pack includes Mermaid, SVG, TikZ and HTML widget assets in matching subfolders. Each Phase 1 placeholder has a corresponding Mermaid, SVG or widget file. TikZ files are supplementary print-quality versions of selected graphs.

---

## Supplementary Sources Used

The Dr Frost/Pearson Pure Year 2 lesson deck and transcript are used as lesson-specific evidence because their content aligns with the CCEA A21 Algebra and functions outcomes for functions, modulus, domain/range, composites, inverses and transformations.

Cross-board exam labels such as Edexcel C4, MAT and SMC appear in the evidence. They are not treated as CCEA core sources. Where a mathematical method aligns with CCEA A21-AF, it is used as supporting practice. Extension-only content is excluded from the required lesson.

---

## Final Student Checklist

Before moving on, make sure you can:

- [ ] Explain what `|a|` means.
- [ ] Sketch `y=|x|`.
- [ ] Sketch `y=|ax+b|` by reflecting the negative part upwards.
- [ ] Solve modulus equations using a sketch and branch equations.
- [ ] Solve modulus inequalities by identifying graph regions.
- [ ] Define a mapping.
- [ ] Define a function.
- [ ] Use the vertical ray test.
- [ ] Explain domain and range.
- [ ] Find the range of a function from a restricted domain.
- [ ] Complete the square to find a quadratic range.
- [ ] Explain one-to-one and many-to-one functions.
- [ ] Form `fg(x)`, `gf(x)` and `f^2(x)`.
- [ ] Find an inverse function algebraically.
- [ ] Explain why an inverse function needs the original function to be one-to-one.
- [ ] Sketch an inverse graph by reflecting in `y=x`.
- [ ] Apply combined graph transformations.
- [ ] Distinguish `y=|f(x)|` from `y=f(|x|)`.
- [ ] Avoid negating the whole equation when solving transformed modulus problems.
