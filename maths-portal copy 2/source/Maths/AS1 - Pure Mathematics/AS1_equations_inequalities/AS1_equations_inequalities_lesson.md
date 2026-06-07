# AS1 Equations and Inequalities

## Title and Metadata

| Field | Value |
|---|---|
| Course | CCEA GCE Mathematics |
| Unit code | `AS1` |
| Unit name | `AS 1 Pure Mathematics` |
| Official topic area | Algebra and functions |
| Topic code | `AS1-AF` |
| Lesson topic name | Equations and Inequalities |
| topic_slug | `equations_inequalities` |
| topic_pascal | `EquationsInequalities` |
| topic_id | `AS1EquationsInequalities` |
| lesson_file | `AS1_equations_inequalities_lesson.md` |
| Core LO IDs | `AS1-AF-LO004`, `AS1-AF-LO007`, `AS1-AF-LO009`, `AS1-AF-LO014`, `AS1-AF-LO015` |
| Supporting LO IDs | `AS1-AF-LO003`, `AS1-AF-LO006`, `AS1-AF-LO012` |
| Excluded/not covered LO ID | `AS1-AF-LO008` |
| Tags | `#AS1`, `#AlgebraFunctions`, `#SimultaneousEquations`, `#Inequalities`, `#Discriminant`, `#SetNotation`, `#SketchGraph` |

---

## Evidence Map

| Evidence | Used for |
|---|---|
| CCEA GCE Mathematics Specification Map | Unit, topic code, LO IDs, syllabus boundaries |
| README Module Map | Metadata conventions, lesson file naming, phase structure |
| Source Evidence Drop Checklist | Missing evidence log, off-spec log, visual placeholder format |
| DrFrost/Pearson `P1 Chapter 3: Equations and Inequalities` PDF | Slide content, examples, diagrams, warnings, exercise references |
| Teacher transcript for Chapter 3 | Explanatory flow, method selection, warnings, calculator notes |
| Screenshots PDF | Visual confirmation only; no uninspected screenshot-specific detail is claimed |

---

## Specification Alignment

| LO ID | Official learning outcome | Lesson section |
|---|---|---|
| `AS1-AF-LO004` | demonstrate understanding of and use the discriminant of a quadratic function, including the condition for real and repeated roots | Discriminant and intersections |
| `AS1-AF-LO007` | solve simultaneous equations in two variables by elimination and by substitution, including one linear and one quadratic equation | Simultaneous equations sections |
| `AS1-AF-LO009` | solve linear and quadratic inequalities in a single variable and interpret such inequalities graphically, including inequalities with brackets and fractions | Linear, quadratic and fractional inequalities |
| `AS1-AF-LO014` | interpret the algebraic solution of equations graphically | Graph intersections and inequality graphs |
| `AS1-AF-LO015` | use intersection points of graphs to solve equations | Simultaneous equations using graphs |
| `AS1-AF-LO003` | work with quadratic functions and their graphs | Supporting graph sketches |
| `AS1-AF-LO006` | solve quadratic equations, including quadratic equations in a function of the unknown | Supporting algebra in simultaneous equations and inequalities |
| `AS1-AF-LO012` | sketch curves defined by simple equations, including polynomials | Supporting sketches for inequalities |

---

## Learning Objectives

By the end of this lesson, you should be able to:

1. Understand that the solution to an equation or inequality is a **solution set**, not just “an answer”.
2. Solve simultaneous equations in two variables by elimination.
3. Solve simultaneous equations in two variables by substitution.
4. Solve one linear and one quadratic equation simultaneously.
5. Interpret simultaneous equations as graph intersections.
6. Use the discriminant \(b^2-4ac\) to decide whether graphs meet twice, once or not at all.
7. Use set-builder notation for solution sets.
8. Solve linear inequalities and write solutions in set notation.
9. Solve quadratic inequalities using the “factorise, sketch, reason” method.
10. Solve simple fractional inequalities by converting safely to a quadratic inequality.
11. Interpret inequalities graphically.
12. Recognise which parts of the supplied evidence are CCEA core and which are optional enrichment.

---

## Prerequisite Recap

No GCSE source evidence is used in this lesson. The following are prerequisite mathematical skills assumed from earlier algebra work or general A-Level readiness:

| Skill | Needed for |
|---|---|
| Expanding brackets | Substitution into quadratics |
| Factorising quadratics | Solving non-linear simultaneous equations and quadratic inequalities |
| Rearranging equations | Making \(x\) or \(y\) the subject |
| Sketching simple quadratic graphs | Quadratic inequalities and graph intersections |
| Understanding \(<,\le,>,\ge\) | Inequality solution sets |
| Substituting values into equations | Checking solution pairs |
| Knowing the discriminant \(b^2-4ac\) | Deciding the number of intersections |

---

## Big Picture Explanation

This chapter turns equations and inequalities into a map of possible values.

A single equation can have one solution, several solutions, infinitely many solutions or no real solutions. An inequality usually opens the gate wider: instead of one value, it often gives an interval or a region.

The main idea is:

\[
\text{equations and inequalities describe sets of values.}
\]

For simultaneous equations, each solution is usually a pair:

\[
(x,y).
\]

For graph questions, each equation describes a curve or line. The solution to two simultaneous equations is where the graphs meet.

For inequalities, the graph becomes a signpost. We ask:

\[
\text{Where is the expression positive, negative, above another graph or below another graph?}
\]

The algebra is the engine. The graph is the dashboard.

---

## Key Definitions and Notation

### Solution set

The **solution set** is the set of all values that make an equation or inequality true.

Examples:

| Type | Example | Solution idea |
|---|---|---|
| A single value | \(2x+1=5\) | One value of \(x\) works |
| Multiple values | \(x^2+3x+2=0\) | Usually two values may work |
| Infinitely many values | \(x>3\) | All real numbers greater than \(3\) work |
| No real values | \(x^2=-1\) | No real \(x\) works |
| Every value | An identity | Every allowed value works |

### Empty set

\[
\varnothing
\]

means the set with no elements.

### Real numbers

\[
\mathbb{R}
\]

means the set of real numbers.

### Integers

\[
\mathbb{Z}
\]

means the set of integers:

\[
\dots,-3,-2,-1,0,1,2,3,\dots
\]

### Natural numbers

\[
\mathbb{N}
\]

means the set of positive whole numbers, using the convention in the supplied lesson evidence:

\[
1,2,3,4,\dots
\]

### Is a member of

\[
x\in A
\]

means “\(x\) is a member of the set \(A\).”

For example:

\[
x\in\mathbb{R}
\]

means “\(x\) is a real number.”

### Intersection

\[
A\cap B
\]

means values in \(A\) and in \(B\).

Example:

\[
\{1,2,3\}\cap\{3,4,5\}=\{3\}.
\]

### Union

\[
A\cup B
\]

means values in \(A\) or in \(B\).

Example:

\[
\{1,2,3\}\cup\{3,4,5\}=\{1,2,3,4,5\}.
\]

The value \(3\) is not written twice because sets do not contain duplicates.

### Set-builder notation

A set can be written as:

\[
\{ \text{expression}:\text{condition} \}.
\]

The colon means “such that”.

Example:

\[
\{x:x>5\}
\]

means “the set of all \(x\) such that \(x>5\).”

### Discriminant

For a quadratic equation

\[
ax^2+bx+c=0,
\]

the discriminant is

\[
b^2-4ac.
\]

| Discriminant | Meaning for roots | Meaning for intersections |
|---:|---|---|
| \(b^2-4ac>0\) | Two distinct real roots | Two intersection points |
| \(b^2-4ac=0\) | One repeated real root | One tangent/intersection point |
| \(b^2-4ac<0\) | No real roots | No real intersection points |

---

## Core Theory

## 1. Solution Sets

Do not think of the solution to an equation or inequality as only an “answer”. Think of it as a **set of values**.

For example:

\[
2x+1=5
\]

has one solution:

\[
2x=4
\]

\[
x=2.
\]

So the solution set is:

\[
\{2\}.
\]

This is a set with one value.

A quadratic such as

\[
x^2+3x+2=0
\]

may have two values:

\[
x^2+3x+2=(x+1)(x+2).
\]

So:

\[
(x+1)(x+2)=0
\]

\[
x+1=0 \quad \text{or} \quad x+2=0
\]

\[
x=-1 \quad \text{or} \quad x=-2.
\]

The solution set is:

\[
\{-1,-2\}.
\]

An inequality such as

\[
x>3
\]

has infinitely many solutions:

\[
\{x:x>3\}.
\]

An equation such as

\[
x^2=-1
\]

has no real solutions, so its real solution set is:

\[
\varnothing.
\]

---

## 2. Solution Sets for Simultaneous Equations

For simultaneous equations, each solution is an assignment to more than one variable.

Example:

\[
x+y=9
\]

\[
x-y=1.
\]

Add the equations:

\[
(x+y)+(x-y)=9+1
\]

\[
2x=10
\]

\[
x=5.
\]

Substitute into

\[
x+y=9.
\]

\[
5+y=9
\]

\[
y=4.
\]

The solution is not “\(x=5\)” and “\(y=4\)” as two separate solutions. It is one paired solution:

\[
(x,y)=(5,4).
\]

So the solution set is:

\[
\{(5,4)\}.
\]

A simultaneous system can have:

| Situation | Example | Solution-set idea |
|---|---|---|
| One solution | Two non-parallel lines | One ordered pair |
| Two solutions | A line and a circle, or a line and a parabola | Two ordered pairs |
| No solutions | Parallel lines | \(\varnothing\) |
| Infinitely many solutions | Same line written twice | Infinitely many ordered pairs |

---

## 3. Solving Linear Simultaneous Equations by Elimination

### Worked Example 1

Solve:

\[
3x+y=8
\]

\[
2x-3y=9.
\]

For linear simultaneous equations, elimination is usually efficient.

We want the \(y\)-terms to cancel.

Multiply the first equation by \(3\):

\[
3(3x+y)=3(8)
\]

\[
9x+3y=24.
\]

Keep the second equation unchanged:

\[
2x-3y=9.
\]

Now add:

\[
(9x+3y)+(2x-3y)=24+9
\]

\[
11x=33.
\]

Divide by \(11\):

\[
x=3.
\]

Substitute \(x=3\) into the original first equation:

\[
3x+y=8
\]

\[
3(3)+y=8
\]

\[
9+y=8
\]

\[
y=-1.
\]

So the solution is:

\[
(x,y)=(3,-1).
\]

In set notation:

\[
\{(3,-1)\}.
\]

---

## 4. Solving a Linear and Non-Linear Simultaneous System by Substitution

### Worked Example 2

Solve:

\[
x+2y=3
\]

\[
x^2+3xy=10.
\]

The second equation is not linear because it contains \(x^2\) and \(xy\). Elimination is not the natural tool here.

Start with the linear equation:

\[
x+2y=3.
\]

Make \(x\) the subject:

\[
x=3-2y.
\]

Substitute this into:

\[
x^2+3xy=10.
\]

Replace every \(x\) with \(3-2y\):

\[
(3-2y)^2+3(3-2y)y=10.
\]

Expand the square:

\[
(3-2y)^2=9-12y+4y^2.
\]

Expand the product:

\[
3(3-2y)y=3y(3-2y).
\]

\[
3y(3-2y)=9y-6y^2.
\]

So:

\[
9-12y+4y^2+9y-6y^2=10.
\]

Collect like terms:

\[
4y^2-6y^2=-2y^2
\]

\[
-12y+9y=-3y.
\]

Therefore:

\[
9-3y-2y^2=10.
\]

Subtract \(10\) from both sides:

\[
9-3y-2y^2-10=0
\]

\[
-2y^2-3y-1=0.
\]

Multiply by \(-1\):

\[
2y^2+3y+1=0.
\]

Factorise:

\[
2y^2+3y+1=(2y+1)(y+1).
\]

So:

\[
(2y+1)(y+1)=0.
\]

Hence:

\[
2y+1=0 \quad \text{or} \quad y+1=0.
\]

\[
y=-\frac12 \quad \text{or} \quad y=-1.
\]

Now use:

\[
x=3-2y.
\]

If

\[
y=-\frac12,
\]

then

\[
x=3-2\left(-\frac12\right)
\]

\[
x=3+1
\]

\[
x=4.
\]

So one solution is:

\[
(x,y)=\left(4,-\frac12\right).
\]

If

\[
y=-1,
\]

then

\[
x=3-2(-1)
\]

\[
x=3+2
\]

\[
x=5.
\]

So the other solution is:

\[
(x,y)=(5,-1).
\]

Final solution set:

\[
\left\{\left(4,-\frac12\right),(5,-1)\right\}.
\]

---

## 5. Test Your Understanding: Linear Plus Quadratic

Solve:

\[
3x^2+y^2=21
\]

\[
y=x+1.
\]

Because \(y\) is already the subject, substitute \(y=x+1\) into the first equation.

\[
3x^2+(x+1)^2=21.
\]

Expand:

\[
(x+1)^2=x^2+2x+1.
\]

So:

\[
3x^2+x^2+2x+1=21.
\]

Collect like terms:

\[
4x^2+2x+1=21.
\]

Subtract \(21\):

\[
4x^2+2x+1-21=0
\]

\[
4x^2+2x-20=0.
\]

Divide by \(2\):

\[
2x^2+x-10=0.
\]

Factorise:

\[
2x^2+x-10=(2x+5)(x-2).
\]

So:

\[
(2x+5)(x-2)=0.
\]

Hence:

\[
2x+5=0 \quad \text{or} \quad x-2=0.
\]

\[
x=-\frac52 \quad \text{or} \quad x=2.
\]

Use:

\[
y=x+1.
\]

If

\[
x=-\frac52,
\]

then

\[
y=-\frac52+1
\]

\[
y=-\frac52+\frac22
\]

\[
y=-\frac32.
\]

So:

\[
(x,y)=\left(-\frac52,-\frac32\right).
\]

If

\[
x=2,
\]

then

\[
y=2+1=3.
\]

So:

\[
(x,y)=(2,3).
\]

Final solution set:

\[
\left\{\left(-\frac52,-\frac32\right),(2,3)\right\}.
\]

Important: keep the \(x\) and \(y\) values paired correctly.

---

## 6. Simultaneous Equations and Graphs

A graph of an equation is the set of all points satisfying that equation.

For example, the line

\[
y=2x+1
\]

contains every point \((x,y)\) where the \(y\)-value is exactly \(2x+1\).

The equation

\[
x+y=5
\]

also represents a set of points.

The simultaneous solution is the point that satisfies both equations at the same time.

That is the **point of intersection**.

### Mini Example

Solve:

\[
y=2x+1
\]

\[
x+y=5.
\]

Substitute \(y=2x+1\) into \(x+y=5\):

\[
x+(2x+1)=5.
\]

Simplify:

\[
3x+1=5.
\]

Subtract \(1\):

\[
3x=4.
\]

Divide by \(3\):

\[
x=\frac43.
\]

Now find \(y\):

\[
y=2x+1
\]

\[
y=2\left(\frac43\right)+1
\]

\[
y=\frac83+1
\]

\[
y=\frac83+\frac33
\]

\[
y=\frac{11}{3}.
\]

So the point of intersection is:

\[
\left(\frac43,\frac{11}{3}\right).
\]

---

## 7. Graph Intersections and the Discriminant

When a line and a quadratic are solved simultaneously, substitution usually creates a new quadratic equation.

This quadratic is not necessarily the original curve. It is the equation whose roots give the \(x\)-coordinates of the intersections.

### Worked Example 3: Two Intersections

On the same axes, consider:

\[
2x+y=3
\]

\[
y=x^2-3x+1.
\]

From the line:

\[
2x+y=3.
\]

Make \(y\) the subject:

\[
y=3-2x.
\]

Substitute into the quadratic equation:

\[
3-2x=x^2-3x+1.
\]

Bring all terms to one side:

\[
0=x^2-3x+1-3+2x.
\]

Simplify:

\[
0=x^2-x-2.
\]

So:

\[
x^2-x-2=0.
\]

This quadratic gives the \(x\)-coordinates of the intersection points.

Factorise:

\[
x^2-x-2=(x-2)(x+1).
\]

So:

\[
(x-2)(x+1)=0.
\]

\[
x=2 \quad \text{or} \quad x=-1.
\]

Use:

\[
y=3-2x.
\]

If \(x=2\), then

\[
y=3-2(2)=3-4=-1.
\]

So one point is:

\[
(2,-1).
\]

If \(x=-1\), then

\[
y=3-2(-1)=3+2=5.
\]

So the other point is:

\[
(-1,5).
\]

The graph intersection solutions are:

\[
(-1,5) \quad \text{and} \quad (2,-1).
\]

Now use the discriminant to show there are two intersections.

For:

\[
x^2-x-2=0,
\]

we have:

\[
a=1,\quad b=-1,\quad c=-2.
\]

The discriminant is:

\[
b^2-4ac.
\]

Substitute:

\[
(-1)^2-4(1)(-2)=1+8=9.
\]

Since:

\[
9>0,
\]

the quadratic has two distinct real roots. Therefore the original graphs have two distinct points of intersection.

---

### Worked Example 4: No Intersection

Consider:

\[
y=2x-2
\]

\[
y=x^2+4x+1.
\]

To find intersections, set the two expressions for \(y\) equal:

\[
x^2+4x+1=2x-2.
\]

Bring all terms to one side:

\[
x^2+4x+1-2x+2=0.
\]

Simplify:

\[
x^2+2x+3=0.
\]

Now use the discriminant.

Here:

\[
a=1,\quad b=2,\quad c=3.
\]

So:

\[
b^2-4ac=2^2-4(1)(3)=4-12=-8.
\]

Since:

\[
-8<0,
\]

there are no real roots.

Therefore there are no real points of intersection.

---

### Worked Example 5: Exactly One Intersection

The line

\[
y=2x+1
\]

meets the curve

\[
kx^2+2y+k-2=0
\]

at exactly one point.

Given that \(k\) is a positive constant:

1. Find \(k\).
2. Find the coordinates of the point of intersection.

Substitute:

\[
y=2x+1
\]

into:

\[
kx^2+2y+k-2=0.
\]

This gives:

\[
kx^2+2(2x+1)+k-2=0.
\]

Expand:

\[
kx^2+4x+2+k-2=0.
\]

Simplify:

\[
kx^2+4x+k=0.
\]

Since the line and curve meet at exactly one point, this quadratic has exactly one real solution.

So:

\[
b^2-4ac=0.
\]

For:

\[
kx^2+4x+k=0,
\]

we have:

\[
a=k,\quad b=4,\quad c=k.
\]

So:

\[
4^2-4(k)(k)=0.
\]

\[
16-4k^2=0.
\]

Move:

\[
16=4k^2.
\]

Divide by \(4\):

\[
4=k^2.
\]

So:

\[
k=\pm2.
\]

But \(k\) is positive, so:

\[
k=2.
\]

Now find the intersection point.

When \(k=2\), the quadratic equation becomes:

\[
2x^2+4x+2=0.
\]

Divide by \(2\):

\[
x^2+2x+1=0.
\]

Factorise:

\[
(x+1)^2=0.
\]

So:

\[
x=-1.
\]

Use the line:

\[
y=2x+1.
\]

\[
y=2(-1)+1=-2+1=-1.
\]

Therefore the point of intersection is:

\[
(-1,-1).
\]

This is exactly one point, matching the condition in the question.

---

## 8. Set-Builder Notation

A set is a collection of values where:

1. The order does not matter.
2. There are no duplicates.

Example:

\[
A=\{1,4,6,7\}.
\]

### Intersection

\[
\{1,2,3\}\cap\{3,4,5\}=\{3\}.
\]

The only number in both sets is \(3\).

### Union

\[
\{1,2,3\}\cup\{3,4,5\}=\{1,2,3,4,5\}.
\]

The union contains values that are in either set. We do not repeat \(3\).

### Empty set

\[
\{1,2\}\cap\{3,4\}=\varnothing.
\]

There are no shared elements.

### Building sets without listing every value

Set-builder notation uses:

\[
\{\text{expression}:\text{condition}\}.
\]

The colon means “such that”.

Example:

\[
\{2x:x\in\mathbb{Z}\}.
\]

This means:

\[
\text{all numbers }2x\text{ such that }x\text{ is an integer.}
\]

If \(x\) is an integer, then \(2x\) is even.

So:

\[
\{2x:x\in\mathbb{Z}\}
\]

is the set of even numbers.

Using the evidence convention:

\[
\{2^x:x\in\mathbb{N}\}=\{2,4,8,16,32,\dots\}.
\]

This is the set of powers of \(2\).

### Common set-builder forms

All odd numbers:

\[
\{2x+1:x\in\mathbb{Z}\}.
\]

All real numbers greater than \(5\):

\[
\{x:x>5\}.
\]

Technically:

\[
\{x:x>5,\ x\in\mathbb{R}\},
\]

but the inequality \(x>5\) usually implies real numbers in this context.

All real numbers less than \(5\) or greater than \(7\):

\[
\{x:x<5\}\cup\{x:x>7\}.
\]

All real numbers between \(5\) and \(7\), inclusive:

\[
\{x:5\le x\le 7\}.
\]

Although this could be written using an intersection, the cleaner form is:

\[
\{x:5\le x\le 7\}.
\]

---

## 9. Linear Inequalities

Linear inequalities behave much like equations, except for one key trap:

> Multiplying or dividing both sides by a negative number reverses the inequality sign.

### Example 1

Solve:

\[
2x+1>5.
\]

Subtract \(1\):

\[
2x>4.
\]

Divide by \(2\):

\[
x>2.
\]

Solution set:

\[
\{x:x>2\}.
\]

---

### Example 2

Solve:

\[
-x\ge 2.
\]

Divide by \(-1\). Because we divide by a negative number, reverse the inequality:

\[
x\le -2.
\]

Solution set:

\[
\{x:x\le -2\}.
\]

Alternative method without dividing by a negative:

\[
-x\ge2.
\]

Add \(x\) to both sides:

\[
0\ge x+2.
\]

Subtract \(2\):

\[
-2\ge x.
\]

So:

\[
x\le -2.
\]

Same result.

---

### Example 3

Solve:

\[
3(x-5)\ge 5-2(x-8).
\]

Expand the left-hand side:

\[
3x-15.
\]

Expand the right-hand side:

\[
5-2(x-8)=5-2x+16.
\]

\[
5-2x+16=21-2x.
\]

So:

\[
3x-15\ge21-2x.
\]

Add \(2x\) to both sides:

\[
5x-15\ge21.
\]

Add \(15\):

\[
5x\ge36.
\]

Divide by \(5\):

\[
x\ge\frac{36}{5}.
\]

Since:

\[
\frac{36}{5}=7.2,
\]

the solution set is:

\[
\left\{x:x\ge\frac{36}{5}\right\}.
\]

---

### Combining Inequalities

If:

\[
x<3
\]

and

\[
2\le x<4,
\]

both must be true.

The overlap is:

\[
2\le x<3.
\]

So the combined solution set is:

\[
\{x:2\le x<3\}.
\]

---

### Three-Part Inequality Example

Solve:

\[
2x+1\le 5x\le 80.
\]

Think of it as two inequalities.

First:

\[
2x+1\le5x.
\]

Subtract \(2x\):

\[
1\le3x.
\]

Divide by \(3\):

\[
\frac13\le x.
\]

So:

\[
x\ge\frac13.
\]

Second:

\[
5x\le80.
\]

Divide by \(5\):

\[
x\le16.
\]

Combine:

\[
\frac13\le x\le16.
\]

Solution set:

\[
\left\{x:\frac13\le x\le16\right\}.
\]

---

## 10. Quadratic Inequalities

The safest method is:

1. Get \(0\) on one side.
2. Factorise or solve the quadratic equation.
3. Sketch the quadratic.
4. Reason from the graph.

Skipping the sketch is the classic trapdoor.

### Worked Example 6

Solve:

\[
x^2+2x-15>0.
\]

Step 1: \(0\) is already on one side.

Step 2: Factorise.

\[
x^2+2x-15=(x+5)(x-3).
\]

So:

\[
(x+5)(x-3)>0.
\]

The critical values are found by solving:

\[
(x+5)(x-3)=0.
\]

So:

\[
x+5=0 \quad \text{or} \quad x-3=0.
\]

\[
x=-5 \quad \text{or} \quad x=3.
\]

Step 3: Sketch.

The quadratic

\[
y=(x+5)(x-3)
\]

has positive \(x^2\), so it is a U-shaped parabola.

It crosses the \(x\)-axis at:

\[
x=-5
\]

and

\[
x=3.
\]

Step 4: Reason.

We need:

\[
y>0.
\]

That means the part of the graph above the \(x\)-axis.

For a positive quadratic, that happens outside the roots:

\[
x<-5 \quad \text{or} \quad x>3.
\]

Solution set:

\[
\{x:x<-5\}\cup\{x:x>3\}.
\]

---

### Worked Example 7

Solve:

\[
x^2+2x-15\le0.
\]

Factorise:

\[
x^2+2x-15=(x+5)(x-3).
\]

So:

\[
(x+5)(x-3)\le0.
\]

Critical values:

\[
x=-5,\quad x=3.
\]

The graph is U-shaped.

We need:

\[
y\le0.
\]

This means the graph is on or below the \(x\)-axis.

That occurs between the roots, including the roots:

\[
-5\le x\le3.
\]

Solution set:

\[
\{x:-5\le x\le3\}.
\]

The \(\le\) matters because the original inequality included equality.

---

### Worked Example 8

Solve:

\[
x^2+5x\ge -4.
\]

Get \(0\) on one side:

\[
x^2+5x+4\ge0.
\]

Factorise:

\[
x^2+5x+4=(x+4)(x+1).
\]

So:

\[
(x+4)(x+1)\ge0.
\]

Critical values:

\[
x=-4,\quad x=-1.
\]

The quadratic is U-shaped, so it is non-negative outside the roots.

Therefore:

\[
x\le -4 \quad \text{or} \quad x\ge -1.
\]

Solution set:

\[
\{x:x\le -4\}\cup\{x:x\ge -1\}.
\]

---

### Worked Example 9

Solve:

\[
x^2<9.
\]

Get \(0\) on one side:

\[
x^2-9<0.
\]

Factorise the difference of two squares:

\[
x^2-9=(x+3)(x-3).
\]

So:

\[
(x+3)(x-3)<0.
\]

Critical values:

\[
x=-3,\quad x=3.
\]

The graph is U-shaped.

We need it below the \(x\)-axis:

\[
-3<x<3.
\]

Solution set:

\[
\{x:-3<x<3\}.
\]

---

### Worked Example 10

Solve:

\[
2+x-x^2>0.
\]

It is often easier to work with a positive \(x^2\)-coefficient.

Start:

\[
2+x-x^2>0.
\]

Move everything to the other side:

\[
0>x^2-x-2.
\]

This is equivalent to:

\[
x^2-x-2<0.
\]

Factorise:

\[
x^2-x-2=(x-2)(x+1).
\]

So:

\[
(x-2)(x+1)<0.
\]

Critical values:

\[
x=2,\quad x=-1.
\]

The graph of \(y=(x-2)(x+1)\) is U-shaped.

We need:

\[
y<0.
\]

This occurs between the roots:

\[
-1<x<2.
\]

Solution set:

\[
\{x:-1<x<2\}.
\]

---

## 11. Inequalities Involving Division by \(x\)

This section has a boundary caution.

The CCEA specification includes inequalities with fractions where they are reducible to linear or quadratic inequalities. The supplied evidence also warns not to treat this as unlimited rational-inequality theory.

### Worked Example 11

Find the set of values for which:

\[
\frac6x>2,\quad x\ne0.
\]

The tempting move is to multiply both sides by \(x\):

\[
\frac6x>2
\]

\[
6>2x.
\]

But this is unsafe because \(x\) might be negative.

If \(x\) is negative, multiplying by \(x\) would reverse the inequality.

Instead, multiply both sides by \(x^2\), which is always positive for \(x\ne0\).

Start:

\[
\frac6x>2.
\]

Multiply both sides by \(x^2\):

\[
x^2\cdot\frac6x>2x^2.
\]

Simplify the left-hand side:

\[
6x>2x^2.
\]

Bring all terms to one side:

\[
0>2x^2-6x.
\]

So:

\[
2x^2-6x<0.
\]

Divide by \(2\):

\[
x^2-3x<0.
\]

Factorise:

\[
x(x-3)<0.
\]

Critical values:

\[
x=0,\quad x=3.
\]

The graph

\[
y=x(x-3)
\]

is U-shaped.

We need:

\[
y<0.
\]

That happens between the roots:

\[
0<x<3.
\]

Solution set:

\[
\{x:0<x<3\}.
\]

Check:

If \(x=-1\),

\[
\frac6{-1}=-6,
\]

and

\[
-6>2
\]

is false.

If \(x=4\),

\[
\frac64=1.5,
\]

and

\[
1.5>2
\]

is false.

If \(x=1\),

\[
\frac61=6,
\]

and

\[
6>2
\]

is true.

So:

\[
0<x<3
\]

is consistent.

---

## 12. Inequalities on Graphs

When solving:

\[
(x+5)(x-3)>0,
\]

we sketch:

\[
y=(x+5)(x-3)
\]

and look for where:

\[
y>0.
\]

That means the parts of the graph above the \(x\)-axis.

The same idea works when comparing two graphs.

### Worked Example 12

Let:

\[
L_1:y=12+4x
\]

and

\[
L_2:y=x^2.
\]

Find the intersection points, then solve:

\[
12+4x>x^2.
\]

Set the equations equal to find intersections:

\[
x^2=12+4x.
\]

Bring all terms to one side:

\[
x^2-4x-12=0.
\]

Factorise:

\[
x^2-4x-12=(x-6)(x+2).
\]

So:

\[
(x-6)(x+2)=0.
\]

Hence:

\[
x=6 \quad \text{or} \quad x=-2.
\]

Find corresponding \(y\)-values.

For \(x=6\):

\[
y=x^2=6^2=36.
\]

So one point is:

\[
(6,36).
\]

For \(x=-2\):

\[
y=x^2=(-2)^2=4.
\]

So the other point is:

\[
(-2,4).
\]

Now solve:

\[
12+4x>x^2.
\]

This means:

\[
L_1 \text{ is above } L_2.
\]

From the graph, the line is above the parabola between the intersection \(x\)-values.

Therefore:

\[
-2<x<6.
\]

Solution set:

\[
\{x:-2<x<6\}.
\]

---

## 13. Optional Enrichment: Two-Variable Inequality Regions

This appears in the supplied lesson evidence, but it is not treated as required CCEA core for this topic because the mapped CCEA inequality LO specifies inequalities in a single variable.

Still, it is a useful enrichment skill.

Sketch the region satisfying:

\[
2y+x<14
\]

\[
y\ge x^2-3x-4.
\]

First rewrite the line inequality:

\[
2y+x<14.
\]

Subtract \(x\):

\[
2y<14-x.
\]

Divide by \(2\):

\[
y<7-\frac{x}{2}.
\]

So this means shade below the line:

\[
y=7-\frac{x}{2}.
\]

For quick sketching, use intercepts.

If \(x=0\):

\[
2y+0=14
\]

\[
2y=14
\]

\[
y=7.
\]

So the \(y\)-intercept is:

\[
(0,7).
\]

If \(y=0\):

\[
2(0)+x=14
\]

\[
x=14.
\]

So the \(x\)-intercept is:

\[
(14,0).
\]

Now consider:

\[
y\ge x^2-3x-4.
\]

The boundary curve is:

\[
y=x^2-3x-4.
\]

Factorise the quadratic:

\[
x^2-3x-4=(x-4)(x+1).
\]

So the \(x\)-intercepts are:

\[
x=4
\]

and

\[
x=-1.
\]

The curve is U-shaped because the coefficient of \(x^2\) is positive.

The inequality

\[
y\ge x^2-3x-4
\]

means shade above the parabola.

So the required region is:

\[
\text{below } y=7-\frac{x}{2}
\]

and

\[
\text{above } y=x^2-3x-4.
\]

A test point can help. Use the origin:

\[
(0,0).
\]

For the line inequality:

\[
2y+x<14
\]

\[
2(0)+0<14
\]

\[
0<14,
\]

which is true.

For the quadratic inequality:

\[
y\ge x^2-3x-4
\]

\[
0\ge 0^2-3(0)-4
\]

\[
0\ge -4,
\]

which is true.

So the origin lies in the shaded region.

---

## Visual Asset Integration

[VISUAL PLACEHOLDER: AS1EquationsInequalitiesSVG-001 | Source: P1 Chapter 3 PDF pages on solution sets | Insert from svg/AS1EquationsInequalitiesSVG-001.svg | Purpose: Show the different possible sizes of a solution set: one value, multiple values, infinite values, empty set and all real values.]

[VISUAL PLACEHOLDER: AS1EquationsInequalitiesSVG-002 | Source: P1 Chapter 3 PDF simultaneous equations graph section | Insert from svg/AS1EquationsInequalitiesSVG-002.svg | Purpose: Show that the solution of two simultaneous equations is the point of intersection of their graphs.]

[VISUAL PLACEHOLDER: AS1EquationsInequalitiesSVG-003 | Source: P1 Chapter 3 PDF discriminant examples | Insert from svg/AS1EquationsInequalitiesSVG-003.svg | Purpose: Compare two intersections, one tangent intersection and no intersections using discriminant cases.]

[VISUAL PLACEHOLDER: AS1EquationsInequalitiesSVG-004 | Source: P1 Chapter 3 PDF quadratic inequalities section | Insert from svg/AS1EquationsInequalitiesSVG-004.svg | Purpose: Show the roots and sign regions for \(y=(x+5)(x-3)\).]

[VISUAL PLACEHOLDER: AS1EquationsInequalitiesSVG-005 | Source: P1 Chapter 3 PDF fractional inequality example | Insert from svg/AS1EquationsInequalitiesSVG-005.svg | Purpose: Show why multiplying by \(x^2\) is safe in \(\frac6x>2\), then display the sign chart for \(x(x-3)<0\).]

[VISUAL PLACEHOLDER: AS1EquationsInequalitiesSVG-006 | Source: P1 Chapter 3 PDF inequality region example | Insert from svg/AS1EquationsInequalitiesSVG-006.svg | Purpose: Optional enrichment diagram showing the region below a line and above a quadratic curve.]

[INTERACTIVE PLACEHOLDER: AS1EquationsInequalitiesWidget-001 | Source: CCEA AS1-AF-LO004 plus lesson discriminant examples | Insert from widgets/AS1EquationsInequalitiesWidget-001.html | Purpose: Let the student vary \(a,b,c\) and observe whether the discriminant gives two, one or no real roots.]

[INTERACTIVE PLACEHOLDER: AS1EquationsInequalitiesWidget-002 | Source: P1 Chapter 3 quadratic inequalities section | Insert from widgets/AS1EquationsInequalitiesWidget-002.html | Purpose: Let the student toggle \(>,\ge,<,\le\) and see the matching interval on a sign chart.]

[INTERACTIVE PLACEHOLDER: AS1EquationsInequalitiesWidget-003 | Source: P1 Chapter 3 set-builder notation section | Insert from widgets/AS1EquationsInequalitiesWidget-003.html | Purpose: Practise translating inequalities into set-builder notation.]

---

## Worked Examples Summary

| Example | Skill | Final answer |
|---|---|---|
| \(3x+y=8,\ 2x-3y=9\) | Linear simultaneous equations by elimination | \((3,-1)\) |
| \(x+2y=3,\ x^2+3xy=10\) | Linear plus non-linear simultaneous equations | \(\left(4,-\frac12\right),(5,-1)\) |
| \(3x^2+y^2=21,\ y=x+1\) | Substitution into quadratic | \(\left(-\frac52,-\frac32\right),(2,3)\) |
| \(2x+y=3,\ y=x^2-3x+1\) | Graph intersections and discriminant | \((-1,5),(2,-1)\) |
| \(y=2x-2,\ y=x^2+4x+1\) | Discriminant proves no intersection | No real intersection |
| \(y=2x+1,\ kx^2+2y+k-2=0\) | Tangency using discriminant | \(k=2,\ (-1,-1)\) |
| \(2x+1>5\) | Linear inequality | \(\{x:x>2\}\) |
| \(-x\ge2\) | Reverse sign when dividing by negative | \(\{x:x\le-2\}\) |
| \(x^2+2x-15>0\) | Quadratic inequality | \(\{x:x<-5\}\cup\{x:x>3\}\) |
| \(x^2+2x-15\le0\) | Quadratic inequality with equality | \(\{x:-5\le x\le3\}\) |
| \(\frac6x>2\) | Fractional inequality reducible to quadratic | \(\{x:0<x<3\}\) |
| \(12+4x>x^2\) | Inequality between graphs | \(\{x:-2<x<6\}\) |

---

## Guided Practice

### Question 1

Solve:

\[
x+y=11
\]

\[
xy=30.
\]

Write your answer as ordered pairs.

### Question 2

Find the points of intersection, if any, of:

\[
y=3x^2-2x+4
\]

and

\[
7x+y+3=0.
\]

Use algebra and the discriminant.

### Question 3

Solve:

\[
x^2-11x+24<0.
\]

Write your answer in set notation.

### Question 4

Solve:

\[
x^2+5x\ge -4.
\]

Write your answer in set notation.

### Question 5

Solve:

\[
\frac6x>2,\quad x\ne0.
\]

Explain why multiplying directly by \(x\) is unsafe.

### Question 6

Let:

\[
L_1:y=12+4x
\]

and

\[
L_2:y=x^2.
\]

Find the intersections and hence solve:

\[
12+4x>x^2.
\]

---

## Common Mistakes and Exam Traps

### Trap 1: Treating \(x\) and \(y\) as separate answers

For simultaneous equations, the solution is an ordered pair:

\[
(x,y).
\]

If you get:

\[
x=4,\quad y=-\frac12,
\]

write:

\[
\left(4,-\frac12\right),
\]

not two unrelated values.

### Trap 2: Pairing the wrong \(x\) and \(y\)

If a quadratic gives two possible \(y\)-values, substitute each one separately to find the matching \(x\).

Do not mix values from different solution branches.

### Trap 3: Dividing an inequality by a negative without reversing the sign

\[
-x\ge2
\]

does not become:

\[
x\ge -2.
\]

Correct:

\[
x\le -2.
\]

### Trap 4: Skipping the sketch for a quadratic inequality

For:

\[
(x+5)(x-3)>0,
\]

the roots alone are not the answer. You must decide whether the solution is inside or outside the roots.

Sketch and reason.

### Trap 5: Losing the strict/non-strict inequality

If the question says:

\[
>0,
\]

your endpoints are not included.

If the question says:

\[
\ge0,
\]

your endpoints are included.

### Trap 6: Multiplying \(\frac6x>2\) directly by \(x\)

You do not know whether \(x\) is positive or negative.

Instead, for this reducible example, multiply by \(x^2\), since \(x^2>0\) for \(x\ne0\).

### Trap 7: Applying the discriminant to the wrong quadratic

When combining a line and a curve, the discriminant is applied to the quadratic produced after substitution.

That quadratic represents the \(x\)-coordinates of intersections.

### Trap 8: Saying “the lines never meet” when one graph is not a line

Some evidence wording says “lines never meet”, but in examples one object may be a curve. Safer exam wording:

\[
\text{The graphs have no real points of intersection.}
\]

---

## Exam Technique

### For simultaneous equations

Use elimination when both equations are linear and coefficients can be made to match.

Use substitution when one equation is already written as \(y=\dots\) or \(x=\dots\), especially when one equation is non-linear.

### For graph intersection questions

1. Substitute or equate the expressions.
2. Rearrange into a quadratic.
3. Use factorisation if solving exactly.
4. Use the discriminant if the question asks about the number of intersections.
5. Interpret the roots as \(x\)-coordinates of intersections.
6. Substitute back to find \(y\)-coordinates.

### For discriminant questions

Use:

\[
b^2-4ac>0
\]

for two distinct intersections.

Use:

\[
b^2-4ac=0
\]

for exactly one intersection.

Use:

\[
b^2-4ac<0
\]

for no real intersections.

### For inequalities

Always ask:

\[
\text{What values make the statement true?}
\]

For quadratic inequalities:

1. Rearrange.
2. Factorise or solve.
3. Sketch.
4. Decide whether the required region is above or below the \(x\)-axis.
5. Match \(<,\le,>,\ge\) carefully.

### For set notation

Use:

\[
\{x:\text{condition}\}.
\]

Examples:

\[
\{x:x>2\}
\]

\[
\{x:-5\le x\le3\}
\]

\[
\{x:x<-5\}\cup\{x:x>3\}.
\]

---

## Full Worked Solutions to Guided Practice

### Solution 1

Solve:

\[
x+y=11
\]

\[
xy=30.
\]

From:

\[
x+y=11,
\]

make \(y\) the subject:

\[
y=11-x.
\]

Substitute into:

\[
xy=30.
\]

\[
x(11-x)=30.
\]

Expand:

\[
11x-x^2=30.
\]

Bring all terms to one side:

\[
0=x^2-11x+30.
\]

So:

\[
x^2-11x+30=0.
\]

Factorise:

\[
x^2-11x+30=(x-5)(x-6).
\]

So:

\[
(x-5)(x-6)=0.
\]

Hence:

\[
x=5 \quad \text{or} \quad x=6.
\]

If:

\[
x=5,
\]

then:

\[
y=11-5=6.
\]

So:

\[
(x,y)=(5,6).
\]

If:

\[
x=6,
\]

then:

\[
y=11-6=5.
\]

So:

\[
(x,y)=(6,5).
\]

Final answer:

\[
\{(5,6),(6,5)\}.
\]

---

### Solution 2

Find intersections of:

\[
y=3x^2-2x+4
\]

and:

\[
7x+y+3=0.
\]

First make \(y\) the subject in the line equation:

\[
7x+y+3=0.
\]

Subtract \(7x\) and \(3\):

\[
y=-7x-3.
\]

Set the two expressions for \(y\) equal:

\[
3x^2-2x+4=-7x-3.
\]

Bring all terms to one side:

\[
3x^2-2x+4+7x+3=0.
\]

Simplify:

\[
3x^2+5x+7=0.
\]

Use the discriminant.

Here:

\[
a=3,\quad b=5,\quad c=7.
\]

\[
b^2-4ac=5^2-4(3)(7).
\]

\[
=25-84.
\]

\[
=-59.
\]

Since:

\[
-59<0,
\]

there are no real roots.

Therefore the graphs have no real points of intersection.

Final answer:

\[
\varnothing
\]

for real intersection points.

---

### Solution 3

Solve:

\[
x^2-11x+24<0.
\]

Factorise:

\[
x^2-11x+24=(x-3)(x-8).
\]

So:

\[
(x-3)(x-8)<0.
\]

Critical values:

\[
x=3,\quad x=8.
\]

The quadratic is U-shaped.

We need the graph below the \(x\)-axis:

\[
3<x<8.
\]

Solution set:

\[
\{x:3<x<8\}.
\]

---

### Solution 4

Solve:

\[
x^2+5x\ge -4.
\]

Add \(4\) to both sides:

\[
x^2+5x+4\ge0.
\]

Factorise:

\[
x^2+5x+4=(x+4)(x+1).
\]

So:

\[
(x+4)(x+1)\ge0.
\]

Critical values:

\[
x=-4,\quad x=-1.
\]

The quadratic is U-shaped.

For:

\[
\ge0,
\]

we need the graph on or above the \(x\)-axis.

That happens outside the roots, including the roots:

\[
x\le -4 \quad \text{or} \quad x\ge -1.
\]

Solution set:

\[
\{x:x\le -4\}\cup\{x:x\ge -1\}.
\]

---

### Solution 5

Solve:

\[
\frac6x>2,\quad x\ne0.
\]

Do not multiply directly by \(x\), because \(x\) could be negative. Multiplying by a negative would reverse the inequality sign.

Instead multiply by \(x^2\), since:

\[
x^2>0
\]

for:

\[
x\ne0.
\]

\[
x^2\cdot \frac6x>2x^2.
\]

Simplify:

\[
6x>2x^2.
\]

Bring all terms to one side:

\[
0>2x^2-6x.
\]

So:

\[
2x^2-6x<0.
\]

Divide by \(2\):

\[
x^2-3x<0.
\]

Factorise:

\[
x(x-3)<0.
\]

Critical values:

\[
x=0,\quad x=3.
\]

The U-shaped graph is below the \(x\)-axis between the roots:

\[
0<x<3.
\]

Final answer:

\[
\{x:0<x<3\}.
\]

---

### Solution 6

Let:

\[
L_1:y=12+4x
\]

and:

\[
L_2:y=x^2.
\]

Find intersections by setting:

\[
x^2=12+4x.
\]

Bring all terms to one side:

\[
x^2-4x-12=0.
\]

Factorise:

\[
x^2-4x-12=(x-6)(x+2).
\]

So:

\[
(x-6)(x+2)=0.
\]

Hence:

\[
x=6 \quad \text{or} \quad x=-2.
\]

Find \(y\)-values using:

\[
y=x^2.
\]

If:

\[
x=6,
\]

then:

\[
y=6^2=36.
\]

So one point is:

\[
(6,36).
\]

If:

\[
x=-2,
\]

then:

\[
y=(-2)^2=4.
\]

So the other point is:

\[
(-2,4).
\]

Now solve:

\[
12+4x>x^2.
\]

This means the line \(L_1\) is above the parabola \(L_2\).

This happens between the intersection \(x\)-values:

\[
-2<x<6.
\]

Solution set:

\[
\{x:-2<x<6\}.
\]

---

## Common CCEA-Style Wording

| Wording | What to do |
|---|---|
| “Solve the simultaneous equations” | Use elimination or substitution and give paired solutions. |
| “Find the points of intersection” | Solve simultaneously and give coordinates. |
| “Prove algebraically that the graphs do not meet” | Combine equations, form a quadratic, show \(b^2-4ac<0\). |
| “The line meets the curve at exactly one point” | Use \(b^2-4ac=0\). |
| “Find the range of values” | Form an inequality, often using the discriminant. |
| “Solve the inequality” | Give all values satisfying it, preferably in set notation. |
| “Interpret graphically” | Explain using roots, intersections, above/below the axis or above/below another graph. |

---

## Syllabus Gap Check

| LO ID | Status | Evidence coverage | Notes |
|---|---|---|---|
| `AS1-AF-LO004` | Covered | Discriminant examples for two, one and no intersections | Core. |
| `AS1-AF-LO007` | Covered | Linear and linear-quadratic simultaneous examples | Core. |
| `AS1-AF-LO009` | Covered | Linear, quadratic and reducible fractional inequalities | Core, with fractional boundary caution. |
| `AS1-AF-LO014` | Covered | Algebraic solutions interpreted as graph intersections | Core. |
| `AS1-AF-LO015` | Covered | Intersections used to solve equations and inequalities | Core. |
| `AS1-AF-LO003` | Partially covered | Quadratic graphs used but not a full quadratic graph chapter | Supporting only. |
| `AS1-AF-LO006` | Partially covered | Quadratic solving used as a method | Supporting only. |
| `AS1-AF-LO012` | Partially covered | Sketches used for inequalities | Supporting only. |
| `AS1-AF-LO008` | Not covered | No three-variable simultaneous equation evidence | Logged gap. |

---

## Visual and Interactive Asset Plan

| Asset ID | Type | Purpose | Phase |
|---|---|---|---|
| `AS1EquationsInequalitiesSVG-001` | SVG | Solution set types | Phase 3 |
| `AS1EquationsInequalitiesSVG-002` | SVG | Simultaneous equations as graph intersections | Phase 3 |
| `AS1EquationsInequalitiesSVG-003` | SVG | Discriminant cases for intersections | Phase 3 |
| `AS1EquationsInequalitiesSVG-004` | SVG | Quadratic inequality sign chart | Phase 3 |
| `AS1EquationsInequalitiesSVG-005` | SVG | Fractional inequality transformed into quadratic sign chart | Phase 3 |
| `AS1EquationsInequalitiesSVG-006` | SVG | Optional two-variable inequality region | Phase 3 |
| `AS1EquationsInequalitiesMermaid-001` | Mermaid | Method-choice flowchart: elimination, substitution, discriminant, sketch | Phase 2 |
| `AS1EquationsInequalitiesTikZ-001` | TikZ | Clean exam-style graph for line-parabola intersection | Phase 4 |
| `AS1EquationsInequalitiesTikZ-002` | TikZ | Clean sign chart for quadratic inequalities | Phase 4 |
| `AS1EquationsInequalitiesWidget-001` | HTML widget | Discriminant explorer | Phase 5 |
| `AS1EquationsInequalitiesWidget-002` | HTML widget | Quadratic inequality interval explorer | Phase 5 |
| `AS1EquationsInequalitiesWidget-003` | HTML widget | Set-builder notation translator | Phase 5 |

---

## Supplementary Sources Used

| Source | Status |
|---|---|
| DrFrost/Pearson PDF | Used as lesson evidence only where aligned to CCEA AS1-AF |
| Teacher transcript | Used for explanation, warnings and method choice |
| Screenshots PDF | Visual confirmation only |
| Pearson textbook page references | Mentioned by evidence but not independently available |
| Edexcel C1 question references | Not used as core due cross-board status and incomplete question text |
| STEP/MAT extension material | Excluded from core, optional enrichment only |

---

## Final Student Checklist

Before moving on, check that you can:

- [ ] Explain what a solution set is.
- [ ] Write a simple solution set in set-builder notation.
- [ ] Solve two linear simultaneous equations by elimination.
- [ ] Solve a linear and quadratic simultaneous system by substitution.
- [ ] Keep solution pairs correctly matched.
- [ ] Explain why graph intersections solve simultaneous equations.
- [ ] Form the quadratic produced by combining a line and a curve.
- [ ] Use \(b^2-4ac>0\), \(=0\), or \(<0\) to decide how many real intersections exist.
- [ ] Solve linear inequalities without losing the inequality direction.
- [ ] Reverse the inequality when multiplying or dividing by a negative number.
- [ ] Solve quadratic inequalities by factorising, sketching and reasoning.
- [ ] Decide whether endpoints are included from \(<,\le,>,\ge\).
- [ ] Solve \(\frac6x>2\) safely by multiplying by \(x^2\), not \(x\).
- [ ] Interpret \(12+4x>x^2\) as one graph being above another.
- [ ] Identify which two-variable inequality region work is optional enrichment rather than CCEA core for this lesson.
