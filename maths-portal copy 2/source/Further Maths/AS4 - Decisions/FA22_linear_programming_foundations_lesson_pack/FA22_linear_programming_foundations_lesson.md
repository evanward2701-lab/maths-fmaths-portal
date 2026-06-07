# FA22 Linear Programming Foundations for the Simplex Algorithm

# 1. Lesson Title and Metadata

| Metadata field | Value |
|---|---|
| Date generated | 2026-06-04 |
| Course | CCEA GCE Further Mathematics |
| Unit | `FA22`: Further A2 2 Applied Mathematics |
| Applied section | Section D: Discrete and Decision Mathematics |
| Topic code | `FA22-ALGGRAPH` |
| Official topic name | Algorithms on graphs |
| Lesson topic name | Linear Programming Foundations for the Simplex Algorithm |
| Topic slug | `linear_programming_foundations` |
| Topic Pascal | `LinearProgrammingFoundations` |
| Topic ID | `FA22LinearProgrammingFoundations` |
| Lesson file | `FA22_linear_programming_foundations_lesson.md` |
| Core LO IDs | `FA22-ALGGRAPH-LO003` |
| Official LO wording | use the simplex algorithm and tableau to solve two-variable linear programming problems |
| Coverage note | This lesson builds the two-variable linear programming foundation. It does not yet teach simplex tableau because the supplied evidence is Chapter 6 graphical LP, while simplex is identified as Chapter 7 in the evidence. |
| Bridge tags | `#AS1Inequalities`, `#AS1CoordinateGeometry`, `#StraightLineGraphs`, `#SimultaneousEquations`, `#OptimisationLanguage` |
| Topic tags | `#FA22`, `#ALGGRAPH`, `#Decision`, `#LinearProgramming`, `#SimplexPreparation`, `#FeasibleRegion`, `#ObjectiveFunction`, `#IntegerSolutions` |

# 2. Evidence Map

| Source | Type | Role in this lesson | Status |
|---|---|---|---|
| `CCEA_GCE_Further_Mathematics_Specification_Map.md` | Project source | Unit, topic code, official LO boundary | Used |
| `Further_Maths_README_module_map.md` | Project source | Module map and topic context | Used |
| `Further_Maths_EVIDENCE_DROP_CHECKLIST.md` | Project source | Evidence limitations, phase structure and asset planning | Used |
| `Ordinary_A_Level_Maths_Bridge_Spec_Extracts.md` | Bridge source | Ordinary Maths inequalities, straight lines and simultaneous equations | Bridge only |
| `CCEA_GCE_Mathematics_Specification_Map.md` | Bridge source | Ordinary Maths specification context | Bridge only |
| `Decision Maths 1 chapter 6 Linear Programming.pdf` | Lesson PDF/slides | LP definition, formulation, feasible regions, sliding ruler, vertex testing | Used as lesson-specific evidence |
| `Chapter_6_Linear_Programming_💻_(Decision_1)_screenshots.pdf` | Visual screenshots | Slide visuals and diagram prompts | Partially accessible; no uninspected visual detail claimed |
| `transcripts.md` | Teacher transcript | Teacher phrasing, warnings, examples and common traps | Used as major evidence |

The supplied lesson evidence is cross-board Decision 1 style evidence. It is used only where it supports the CCEA Further Mathematics two-variable linear programming foundation confirmed by `FA22-ALGGRAPH-LO003`. The CCEA endpoint is simplex algorithm and tableau, which remains a separate missing evidence requirement.

# 3. Specification Alignment

| LO ID | Official wording | Lesson coverage | Evidence source | Boundary |
|---|---|---|---|---|
| `FA22-ALGGRAPH-LO003` | use the simplex algorithm and tableau to solve two-variable linear programming problems | Decision variables, objective functions, linear constraints, non-negativity, feasible solutions, feasible regions, graphical optimisation, vertex testing and integer checks | CCEA map plus Chapter 6 PDF/transcript | Partial only. Simplex tableau is not taught in this lesson. |

This lesson is a foundation lesson. It prepares the language and geometry needed before the simplex tableau lesson, but it does not claim full CCEA LO coverage.

# 4. Learning Objectives

## Core Further Maths objectives

By the end of this lesson, the student should be able to:

1. Define a linear programming problem as optimisation under linear constraints.
2. Identify and define decision variables in context.
3. Construct an objective function to maximise or minimise.
4. Translate resource, ratio, percentage and demand conditions into inequalities.
5. Include non-negativity constraints where appropriate.
6. Simplify decimal or fractional constraints into integer-coefficient inequalities.
7. Interpret feasible solutions, feasible regions and optimal solutions.
8. Draw or describe the feasible region for two-variable constraints.
9. Use objective lines and the sliding ruler idea to locate an optimum.
10. Use vertex testing to compare objective values at vertices.
11. Check nearby integer points when the context requires whole-number answers.
12. Recognise that the official CCEA endpoint is simplex algorithm and tableau.

## Bridge objectives

The student should connect this lesson to ordinary A-Level Maths by using:

- straight line equations;
- intercepts;
- inequality shading;
- simultaneous equations;
- substitution;
- ratio and percentage algebra.

## Exam technique objectives

The student should learn to state variables clearly, use “Maximise” or “Minimise”, write “subject to”, split double inequalities, watch “at least twice as many” traps, distinguish solid and dotted boundaries, use exact vertices, and interpret final answers in context.

# 5. Explicit Prerequisite Recap

## GCSE foundations

You need substitution, rearranging, expanding brackets, collecting like terms, fractions, percentages, ratio, coordinates, straight-line plotting and inequality shading.

## Ordinary AS/A2 Mathematics foundations

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| AS1 Algebra and Functions | Solve and manipulate inequalities | Use many inequalities at once to model decisions | One correct inequality is not enough; all constraints must hold |
| AS1 Coordinate Geometry | Equations of straight lines, gradients and intercepts | Each constraint becomes a boundary line | The inequality sign decides the feasible side |
| AS1 Simultaneous Equations | Solve two equations in two unknowns | Intersections become vertices of feasible regions | Rounded vertices may change the objective value |
| Ordinary graph interpretation | Shade regions and read coordinates | The feasible region represents all allowed decisions | Graphing software may shade the accepted side, while the evidence convention shades rejected regions |
| Ordinary optimisation language | Maximise or minimise a quantity | Optimise only subject to constraints | The largest coefficient alone does not choose the best point |

### A-Level Maths Bridge: What You Already Know and What Further Maths Changes

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| Inequalities | Interpret and solve linear inequalities | Combine several inequalities into one feasible region | One bad inequality can move or destroy the feasible region |
| Straight line graphs | Draw lines from gradients, intercepts or equations | Use lines as constraint boundaries | Forgetting which side is allowed gives the wrong model |
| Simultaneous equations | Find where two lines meet | Find vertices of a feasible polygon | Do not round exact intersections too early |
| Substitution | Put values into a formula | Evaluate objective functions at vertices | Pick maximum or minimum according to the question |

In ordinary A-Level Maths, this idea appeared as graphing straight lines, solving inequalities and finding intersections. In Further Maths, the same idea becomes a decision model: the lines are not just lines, they are boundaries of what is allowed. The key upgrade is that the graph becomes a map of possible decisions. The danger is treating the problem like a normal graphing question; in linear programming, a point matters only if it satisfies every constraint and optimises the objective.

# 6. Big Picture Explanation

Linear programming is an optimisation technique. It involves making the most, or the least, of something when subject to linear constraints. In the supplied evidence, the opening slides describe constrained problems in two independent variables and separate graphical linear programming from the later simplex algorithm. For CCEA Further Mathematics, this lesson is the launchpad for `FA22-ALGGRAPH-LO003`.

A typical two-variable linear programme looks like

\[
\begin{aligned}
\text{Maximise or minimise } & P=ax+by,\\
\text{subject to } & \text{linear constraints in }x\text{ and }y,\\
&x\ge 0,\quad y\ge 0.
\end{aligned}
\]

The big shift is from “which values solve this?” to “which allowed values are best?” A feasible point is allowed; an optimal point is best. Graphical linear programming helps students see why simplex later moves algebraically through candidate vertices.

For applied modelling, assume the decision variables are measurable, resource usage rates are constant, the objective and constraints are linear, values are fixed during the problem, and unlisted constraints are ignored. Fractional values are allowed unless the context requires integers.

# 7. Key Definitions and Notation

## Linear programming

A linear programming problem is an optimisation problem in which a linear objective function is maximised or minimised subject to linear constraints.

## Decision variables

Decision variables are the quantities chosen by the model. For example,

\[
x=\text{number of lemon drizzle cakes},\qquad y=\text{number of carrot cakes}.
\]

A good definition includes the quantity, object and time period or unit if relevant.

## Objective function

The objective function is the quantity to maximise or minimise. Typical notation is

\[
P=\text{profit or revenue},\qquad C=\text{cost}.
\]

For cakes sold at £4.50 and £5.00,

\[
P=4.5x+5y.
\]

## Constraints

A constraint is a condition restricting the decision variables. Resource constraints often have the form

\[
r_Ax+r_By\le R.
\]

Demand constraints often use \(\ge\). Capacity or budget constraints often use \(\le\).

## Non-negativity constraints

Usually

\[
x\ge0,\qquad y\ge0,
\]

because negative quantities such as cakes, litres or containers are impossible. If stronger bounds such as \(x\ge200\) and \(y\ge80\) are already present, non-negativity is implied.

## Feasible solution

A feasible solution is a set of values satisfying every constraint.

## Feasible region

The feasible region is the set of all feasible solutions. The evidence convention is to shade rejected regions and leave the feasible region unshaded.

## Optimal solution

An optimal solution is a feasible solution giving the best value of the objective function.

## Boundary line

The boundary line of

\[
2x+3y\le80
\]

is

\[
2x+3y=80.
\]

Use solid boundary lines for \(\le,\ge\), and dotted boundary lines for \(<,>\).

## Integer solution

An integer solution requires decision variables to be whole numbers. This is needed when the context involves indivisible objects.

# 8. Core Theory

## 8.1 Formulating a linear programme

Use this structure:

1. Define decision variables.
2. Decide whether to maximise or minimise.
3. Write the objective function.
4. Translate each condition into a constraint.
5. Add non-negativity constraints.
6. Simplify coefficients if appropriate.
7. State the full model clearly.

A clean final model uses the language:

\[
\begin{aligned}
\text{Maximise/Minimise }&\text{objective},\\
\text{subject to }&\text{constraints}.
\end{aligned}
\]

**Bridge Note:** In ordinary A-Level Maths, you often solve one inequality at a time. Here, Further Maths combines several inequalities into one decision model.

## 8.2 Cake example formulation

Let

\[
x=\text{number of lemon drizzle cakes},\qquad y=\text{number of carrot cakes}.
\]

Each lemon drizzle cake sells for £4.50 and each carrot cake sells for £5.00, so

\[
\text{Maximise }P=4.5x+5y.
\]

Eggs:

\[
x+2y\le24.
\]

Flour: convert grams to kilograms.

\[
250\text{ g}=0.25\text{ kg},\qquad 300\text{ g}=0.3\text{ kg}.
\]

Hence

\[
0.25x+0.3y\le4.
\]

Multiply by \(100\):

\[
25x+30y\le400.
\]

Divide by \(5\):

\[
5x+6y\le80.
\]

Sugar:

\[
200\text{ g}=0.2\text{ kg},\qquad 300\text{ g}=0.3\text{ kg},
\]

so

\[
0.2x+0.3y\le5.
\]

Multiply by \(10\):

\[
2x+3y\le50.
\]

Non-negativity:

\[
x,y\ge0.
\]

Final model:

\[
\boxed{\begin{aligned}
\text{Maximise }P&=4.5x+5y,\\
x+2y&\le24,\\
5x+6y&\le80,\\
2x+3y&\le50,\\
x,y&\ge0.
\end{aligned}}
\]

## 8.3 Language traps

“At least twice as many pocket diaries as desktop diaries” with

\[
x=\text{desktop diaries},\qquad y=\text{pocket diaries}
\]

means

\[
y\ge2x,
\]

not \(2y\ge x\). Test with numbers to check.

Double inequalities must be split:

\[
30<x\le50
\]

becomes

\[
x>30,\qquad x\le50.
\]

Percentage constraints use “part compared with percentage of total”. For example, if \(x\) is keyboards and total is \(x+y+z\), then more than \(20\%\) keyboards gives

\[
x>\frac15(x+y+z).
\]

Multiplying by \(5\):

\[
5x>x+y+z,
\]

so

\[
4x>y+z.
\]

For every \(2\) keyboards, at least \(3\) monitors gives

\[
x:z=2:3,
\]

so

\[
z=\frac32x,
\]

therefore

\[
2z\ge3x.
\]

## 8.4 Feasible regions

To draw a feasible region:

1. Replace each inequality with an equality to draw the boundary line.
2. Use intercepts or another method to plot the line.
3. Use a solid line for \(\le,\ge\) and a dotted line for \(<,>\).
4. Test a point such as \((0,0)\) to decide the allowed side.
5. Shade rejected regions if using the evidence convention.
6. The unshaded overlap is the feasible region.

Example:

\[
2x+3y\le80.
\]

Boundary:

\[
2x+3y=80.
\]

Set \(x=0\):

\[
3y=80,\quad y=\frac{80}{3},
\]

so one point is

\[
\left(0,\frac{80}{3}\right).
\]

Set \(y=0\):

\[
2x=80,\quad x=40,
\]

so another point is

\[
(40,0).
\]

Test \((0,0)\):

\[
2(0)+3(0)=0\le80,
\]

so the origin side is allowed.

## 8.5 Expressing a feasible region algebraically

If a feasible region is given, find the boundary equations and then decide inequality direction. For a line

\[
y=\frac12x+6
\]

with the feasible region below it,

\[
y\le\frac12x+6.
\]

Multiplying by \(2\):

\[
2y\le x+12.
\]

If a line is

\[
y=-x+14
\]

and the region is below it,

\[
y\le -x+14,
\]

so

\[
x+y\le14.
\]

## 8.6 Objective lines and sliding ruler method

For

\[
P=ax+by,
\]

make \(y\) the subject:

\[
by=P-ax,
\]

\[
y=-\frac{a}{b}x+\frac{P}{b}.
\]

Changing \(P\) changes the intercept but not the gradient. So objective lines are parallel.

For a maximum, slide the objective line in the direction of increasing objective value until the last feasible contact. For a minimum, use the first feasible contact. If an objective line is parallel to a feasible-region edge, a whole edge can be optimal.

## 8.7 Vertex testing

For a polygonal feasible region, test each vertex:

1. Find coordinates of each vertex.
2. Substitute into the objective function.
3. Compare values.
4. Choose the largest value for a maximum or the smallest for a minimum.

Example with

\[
C=140x+170y
\]

and vertices

\[
A=(0,25),\quad B=(6,7),\quad C=(11,2),\quad D=(13,1).
\]

At \(A\):

\[
C=140(0)+170(25)=4250.
\]

At \(B\):

\[
C=140(6)+170(7)=840+1190=2030.
\]

At \(C\):

\[
C=140(11)+170(2)=1540+340=1880.
\]

At \(D\):

\[
C=140(13)+170(1)=1820+170=1990.
\]

The minimum is \(1880\) at \((11,2)\).

## 8.8 Integer solutions

If the optimum is non-integer but the variables count whole objects, test nearby integer points. Do not round blindly. A rounded point may fail a constraint.

For example, with

\[
P=18x+25y
\]

and constraints

\[
x\ge0,\quad y\ge0,\quad x\le6,\quad y\le8,\quad 5x+3y\le38,
\]

near the fractional optimum \((3.6,6.8)\), test points such as \((3,6),(3,7),(4,6),(4,7),(2,8),(3,8)\). Reject infeasible points, then compare objective values.

## 8.9 Bridge to simplex

The simplex algorithm uses the same variables, objective function and constraints, but solves algebraically using a tableau. This lesson explains the geometry and modelling objects; a separate lesson must teach slack variables, pivoting, row operations and final tableau interpretation.

# 9. Visual Asset Integration

[VISUAL PLACEHOLDER: FA22LinearProgrammingFoundationsMermaid-001 | Source: CCEA FA22-ALGGRAPH boundary + supplied Chapter 6 linear programming evidence | Insert from mermaid/FA22LinearProgrammingFoundationsMermaid-001.md | Purpose: Show the flow from real-world context to decision variables, objective function, constraints, feasible region, optimal solution and later simplex tableau.]

[VISUAL PLACEHOLDER: FA22LinearProgrammingFoundationsSVG-001 | Source: Teacher transcript and screenshot PDF cake example | Insert from svg/FA22LinearProgrammingFoundationsSVG-001.svg | Purpose: Annotate the cake example with labels for decision variables, objective function, constraints and non-negativity.]

[VISUAL PLACEHOLDER: FA22LinearProgrammingFoundationsSVG-002 | Source: Chapter 6 PDF graphical methods page | Insert from svg/FA22LinearProgrammingFoundationsSVG-002.svg | Purpose: Show that the evidence convention shades rejected regions and leaves the feasible region unshaded.]

[VISUAL PLACEHOLDER: FA22LinearProgrammingFoundationsSVG-003 | Source: Chapter 6 PDF and transcript sliding ruler method | Insert from svg/FA22LinearProgrammingFoundationsSVG-003.svg | Purpose: Show a family of parallel objective lines moving across a feasible region to locate a maximum or minimum.]

[VISUAL PLACEHOLDER: FA22LinearProgrammingFoundationsSVG-004 | Source: Chapter 6 PDF vertex testing method | Insert from svg/FA22LinearProgrammingFoundationsSVG-004.svg | Purpose: Link a feasible-region graph to a vertex testing table.]

[VISUAL PLACEHOLDER: FA22LinearProgrammingFoundationsBridgeSVG-001 | Source: Ordinary A-Level Maths bridge + Further Maths specification | Insert from svg/FA22LinearProgrammingFoundationsBridgeSVG-001.svg | Purpose: Compare prior ordinary Maths method with Further Maths extension.]

[VISUAL PLACEHOLDER: FA22LinearProgrammingFoundationsTikZ-001 | Source: Chapter 6 graphical methods evidence | Insert from tikz/FA22LinearProgrammingFoundationsTikZ-001.tex | Purpose: Provide a precise mathematical feasible-region diagram with labelled lines and coordinates.]

[VISUAL PLACEHOLDER: FA22LinearProgrammingFoundationsTikZ-002 | Source: Teacher transcript integer-solution discussion | Insert from tikz/FA22LinearProgrammingFoundationsTikZ-002.tex | Purpose: Show nearby integer candidates around a non-integer optimum.]

# 10. Interactive Learning Widgets

[INTERACTIVE PLACEHOLDER: FA22LinearProgrammingFoundationsWidget-001 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FA22LinearProgrammingFoundationsWidget-001.html | Purpose: Practise translating English constraint phrases into inequalities.]

[INTERACTIVE PLACEHOLDER: FA22LinearProgrammingFoundationsWidget-002 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FA22LinearProgrammingFoundationsWidget-002.html | Purpose: Let students enter inequalities and see the rejected regions plus feasible region.]

[INTERACTIVE PLACEHOLDER: FA22LinearProgrammingFoundationsWidget-003 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FA22LinearProgrammingFoundationsWidget-003.html | Purpose: Build a vertex-testing table from a given objective function and vertex list.]

[INTERACTIVE PLACEHOLDER: FA22LinearProgrammingFoundationsWidget-004 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FA22LinearProgrammingFoundationsWidget-004.html | Purpose: Help students test nearby integer points around a fractional optimum.]

# 11. Worked Examples

## Worked Example 1: Cake Production Linear Programme

Let

\[
x=\text{number of lemon drizzle cakes made},\qquad y=\text{number of carrot cakes made}.
\]

Objective:

\[
\text{Maximise }P=4.5x+5y.
\]

Eggs:

\[
x+2y\le24.
\]

Flour:

\[
0.25x+0.3y\le4.
\]

Multiply by \(100\):

\[
25x+30y\le400.
\]

Divide by \(5\):

\[
5x+6y\le80.
\]

Sugar:

\[
0.2x+0.3y\le5.
\]

Multiply by \(10\):

\[
2x+3y\le50.
\]

Non-negativity:

\[
x,y\ge0.
\]

Final answer:

\[
\boxed{\begin{aligned}
\text{Maximise }P&=4.5x+5y,\\
x+2y&\le24,\\
5x+6y&\le80,\\
2x+3y&\le50,\\
x,y&\ge0.
\end{aligned}}
\]

## Worked Example 2: Diary Buying Linear Programme

Let

\[
x=\text{desktop diaries},\qquad y=\text{pocket diaries}.
\]

Costs:

\[
\text{Minimise }C=6x+3y.
\]

Minimum orders:

\[
x\ge200,
\]

\[
y\ge80.
\]

At least twice as many pocket diaries as desktop diaries:

\[
y\ge2x.
\]

Total at least \(400\):

\[
x+y\ge400.
\]

Final answer:

\[
\boxed{\begin{aligned}
\text{Minimise }C&=6x+3y,\\
x&\ge200,\\
y&\ge80,\\
y&\ge2x,\\
x+y&\ge400.
\end{aligned}}
\]

## Worked Example 3: Complex Constraint Language

Let \(x\) be keyboards, \(y\) mice and \(z\) monitors.

1. “Keyboards cannot be fewer than mice and monitors”:

\[
x\ge y+z.
\]

2. “At most twice as many monitors as mice”:

\[
z\le2y.
\]

3. “More than 20% and less than 60% must be keyboards”:

\[
x>\frac15(x+y+z),
\]

so

\[
5x>x+y+z,
\]

\[
4x>y+z.
\]

Also

\[
x<\frac35(x+y+z),
\]

so

\[
5x<3x+3y+3z,
\]

\[
2x<3y+3z.
\]

4. “For every 2 keyboards, at least 3 monitors”:

\[
2z\ge3x.
\]

## Worked Example 4: Syrup Blending

Let

\[
x=\text{litres of syrup A},\qquad y=\text{litres of syrup B}.
\]

Objective:

\[
\text{Minimise }C=0.5x+0.4y.
\]

Production and quantity:

\[
x\le40000,
\]

\[
y\le45000,
\]

\[
x+y\ge60000.
\]

Sugar below 25%:

\[
0.3x+0.2y<0.25(x+y).
\]

\[
0.3x+0.2y<0.25x+0.25y.
\]

\[
0.05x<0.05y.
\]

\[
x<y.
\]

Fruit at least 40%:

\[
0.5x+0.35y\ge0.4(x+y).
\]

\[
0.5x+0.35y\ge0.4x+0.4y.
\]

\[
0.1x\ge0.05y.
\]

\[
2x\ge y.
\]

Juice no more than 35%:

\[
0.2x+0.45y\le0.35(x+y).
\]

\[
0.2x+0.45y\le0.35x+0.35y.
\]

\[
0.1y\le0.15x.
\]

\[
2y\le3x.
\]

Final answer:

\[
\boxed{\begin{aligned}
\text{Minimise }C&=0.5x+0.4y,\\
x&\le40000,\\
y&\le45000,\\
x+y&\ge60000,\\
x&<y,\\
y&\le2x,\\
2y&\le3x,\\
x,y&\ge0.
\end{aligned}}
\]

## Worked Example 5: Stainless Steel Blending

Let

\[
x=\text{kg of type A},\qquad y=\text{kg of type B}.
\]

Objective:

\[
\text{Minimise }C=1.2x+y.
\]

Iron no more than 85%:

\[
0.82x+0.88y\le0.85(x+y).
\]

\[
0.82x+0.88y\le0.85x+0.85y.
\]

\[
0.03y\le0.03x.
\]

\[
y\le x.
\]

Chromium more than 15%:

\[
0.17x+0.115y>0.15(x+y).
\]

\[
0.17x+0.115y>0.15x+0.15y.
\]

\[
0.02x>0.035y.
\]

\[
x>1.75y.
\]

Carbon no more than 0.9%:

\[
0.01x+0.005y\le0.009(x+y).
\]

\[
0.01x+0.005y\le0.009x+0.009y.
\]

\[
0.001x\le0.004y.
\]

\[
\frac14x\le y.
\]

Other constraints:

\[
x+y\ge20000,\qquad x\le15000,\qquad y\le10000,\qquad x,y\ge0.
\]

Final answer:

\[
\boxed{\begin{aligned}
\text{Minimise }C&=1.2x+y,\\
y&\le x,\\
x&>1.75y,\\
\frac14x&\le y,\\
x+y&\ge20000,\\
x&\le15000,\\
y&\le10000,\\
x,y&\ge0.
\end{aligned}}
\]

## Worked Example 6: Graphing a Feasible Region

Storage-container constraints:

\[
x\ge2,
\]

\[
-x+24y\ge24,
\]

\[
7x+8y\le112,
\]

and budget

\[
20x+65y\le520.
\]

Divide the budget constraint by \(5\):

\[
4x+13y\le104.
\]

For \(-x+24y=24\), if \(x=0\), then \(y=1\). If \(x=24\), then

\[
-24+24y=24,
\]

\[
24y=48,
\]

\[
y=2.
\]

So draw through \((0,1)\) and \((24,2)\). Test \((0,0)\):

\[
0\ge24
\]

is false, so reject the origin side.

For \(7x+8y=112\), intercepts are \((0,14)\) and \((16,0)\). The origin satisfies \(\le\), so reject the opposite side.

For \(4x+13y=104\), intercepts are \((0,8)\) and \((26,0)\). The origin satisfies \(\le\), so reject the opposite side. The unshaded overlap is \(R\).

## Worked Example 7: Vertex Testing

For vertices

\[
(0,25),\quad(6,7),\quad(11,2),\quad(13,1)
\]

and

\[
C=140x+170y,
\]

we get

\[
C(0,25)=4250,
\]

\[
C(6,7)=2030,
\]

\[
C(11,2)=1880,
\]

\[
C(13,1)=1990.
\]

Minimum is \(1880\) at \((11,2)\).

## Worked Example 8: Integer Solutions

For candidates \((10,4),(11,4),(10,5),(11,5)\) with budget

\[
4x+13y\le104
\]

and capacity

\[
V=x+1.5y,
\]

check:

\[
(10,4):\quad 4(10)+13(4)=40+52=92\le104,
\]

\[
V=10+1.5(4)=16.
\]

\[
(11,4):\quad 4(11)+13(4)=44+52=96\le104,
\]

\[
V=11+1.5(4)=17.
\]

\[
(10,5):\quad 40+65=105>104,
\]

so reject. Similarly

\[
(11,5):\quad 44+65=109>104,
\]

so reject. The best feasible integer point is \((11,4)\).

# 12. Common Mistakes and Exam Traps

- Not defining decision variables clearly.
- Forgetting to state maximise or minimise.
- Confusing profit, revenue and cost.
- Not converting units, such as grams to kilograms.
- Leaving awkward decimal constraints when integer coefficients are expected.
- Reversing “at least twice as many”.
- Mishandling ratio constraints.
- Not splitting double inequalities.
- Treating “between” as one inequality.
- Forgetting non-negativity.
- Shading the wrong region.
- Forgetting solid and dotted line rules.
- Choosing a corner by eye instead of using objective lines or vertex testing.
- Forgetting a whole edge can be optimal.
- Rounding a non-integer optimum without checking feasibility.
- Giving the final answer without context.
- Treating graphical LP as full CCEA simplex coverage.

# 13. Practice Questions

The following are generated practice questions, not past-paper or textbook questions.

## Basic fluency

1. Let \(x\) be laptops, \(y\) tablets and \(z\) monitors. Translate:
   - at least \(40\) laptops;
   - no more than \(75\) tablets;
   - monitors more than twice laptops;
   - laptops cannot be fewer than tablets and monitors;
   - between \(25\%\) and \(60\%\) of all devices must be tablets;
   - for every \(3\) laptops, at least \(2\) monitors.

2. Rewrite with integer coefficients:

\[
0.2x+0.3y\le6,
\]

\[
0.75x+0.5y\ge12,
\]

\[
1.25x+0.4y<10,
\]

\[
\frac23x+\frac14y\le8.
\]

3. For

\[
\text{Maximise }P=12x+15y
\]

subject to

\[
2x+y\le100,
\]

\[
x+3y\le120,
\]

\[
x,y\ge0,
\]

identify decision variables, objective function, constraints, one feasible point and one infeasible point.

## Bridge questions

4. For \(3x+2y\le24\), find intercepts, boundary type and allowed side.
5. A region is below \(y=\frac23x+5\) and above \(y=-2x+18\). Write the constraints.
6. Solve for the vertex of \(2x+y=18\) and \(x+3y=24\).

## Standard exam-style questions

7. Formulate the sandwich/wrap café revenue problem with bread/wrap items, cheese and salad constraints.
8. Formulate the charity food parcel minimum-cost problem.
9. Formulate a juice blending minimum-cost problem.
10. Graph constraints \(x,y\ge0\), \(x+y\le10\), \(2x+y\le14\), \(x+3y\le18\), and find vertices.
11. Maximise \(P=5x+4y\) over the region in Question 10.

## Harder synthesis

12. Integer restriction: maximise \(P=18x+25y\) with \(x\le6\), \(y\le8\), \(5x+3y\le38\), \(x,y\ge0\), near \((18/5,34/5)\).
13. Objective-line gradient: if \(P=ax+by\) has gradient \(-4/5\), find \(a:b\) and an exact objective if \(P=260\) at \((10,6)\).
14. Show all points on \(x+2y=20\) have the same value for \(P=3x+6y\).
15. Formulate and solve the garden-planter resource problem.
16. Explain why this lesson is foundation for simplex but not full `FA22-ALGGRAPH-LO003` coverage.

# 14. Worked Solutions

## Solution 1

(a) \(x\ge40\).  
(b) \(y\le75\).  
(c) \(z>2x\).  
(d) \(x\ge y+z\).  
(e) Total \(x+y+z\). Lower bound:

\[
y\ge\frac14(x+y+z),
\]

so

\[
4y\ge x+y+z,
\]

\[
3y\ge x+z.
\]

Upper bound:

\[
y\le\frac35(x+y+z),
\]

so

\[
5y\le3x+3y+3z,
\]

\[
2y\le3x+3z.
\]

(f) \(x:z=3:2\), so \(3z=2x\); at least monitors gives \(3z\ge2x\).

## Solution 2

(a)

\[
0.2x+0.3y\le6\Rightarrow 2x+3y\le60.
\]

(b)

\[
0.75x+0.5y\ge12\Rightarrow \frac34x+\frac12y\ge12\Rightarrow 3x+2y\ge48.
\]

(c)

\[
1.25x+0.4y<10\Rightarrow \frac54x+\frac25y<10\Rightarrow 25x+8y<200.
\]

(d)

\[
\frac23x+\frac14y\le8\Rightarrow 8x+3y\le96.
\]

## Solution 3

Decision variables: \(x,y\). Objective: \(P=12x+15y\). Constraints: \(2x+y\le100\), \(x+3y\le120\), \(x,y\ge0\). A feasible point is \((10,10)\) because \(30\le100\) and \(40\le120\). An infeasible point is \((60,30)\) because \(2(60)+30=150>100\).

## Solution 4

Boundary:

\[
3x+2y=24.
\]

Set \(y=0\): \(3x=24\), so \(x=8\). Set \(x=0\): \(2y=24\), so \(y=12\). The boundary is solid. Test \((0,0)\):

\[
3(0)+2(0)=0\le24,
\]

so the origin side is allowed.

## Solution 5

Below

\[
y=\frac23x+5
\]

gives

\[
y\le\frac23x+5.
\]

Multiply by \(3\):

\[
3y\le2x+15.
\]

Above

\[
y=-2x+18
\]

gives

\[
y\ge-2x+18,
\]

so

\[
2x+y\ge18.
\]

## Solution 6

From

\[
2x+y=18,
\]

\[
y=18-2x.
\]

Substitute into

\[
x+3y=24:
\]

\[
x+3(18-2x)=24,
\]

\[
x+54-6x=24,
\]

\[
-5x=-30,
\]

\[
x=6.
\]

Then

\[
y=18-2(6)=6.
\]

Vertex:

\[
(6,6).
\]

## Solution 7

Let \(x\) be sandwiches and \(y\) wraps. Maximise

\[
R=3.20x+4.50y.
\]

Bread/wrap items:

\[
2x+y\le160.
\]

Cheese:

\[
30x+50y\le3600,
\]

so

\[
3x+5y\le360.
\]

Salad:

\[
x+2y\le120.
\]

Non-negativity:

\[
x,y\ge0.
\]

## Solution 8

Let \(x\) be standard parcels and \(y\) family parcels. Minimise

\[
C=8x+14y.
\]

Constraints:

\[
x\ge50,
\]

\[
y\ge30,
\]

\[
x+y\ge120,
\]

\[
x\ge2y.
\]

## Solution 9

Let \(x\) be litres of juice A and \(y\) litres of juice B. Minimise

\[
C=1.30x+1.10y.
\]

Total:

\[
x+y\ge1000.
\]

Orange:

\[
0.40x+0.20y\ge0.30(x+y)
\]

gives

\[
x\ge y.
\]

Apple:

\[
0.20x+0.50y\le0.35(x+y)
\]

also gives

\[
y\le x.
\]

Water:

\[
0.40x+0.30y\le0.38(x+y)
\]

gives

\[
x\le4y.
\]

Final model:

\[
\boxed{\begin{aligned}
\text{Minimise }C&=1.30x+1.10y,\\
x+y&\ge1000,\\
x&\ge y,\\
x&\le4y,\\
x,y&\ge0.
\end{aligned}}
\]

## Solution 10

For \(x+y=10\), intercepts are \((10,0)\) and \((0,10)\).  
For \(2x+y=14\), intercepts are \((7,0)\) and \((0,14)\).  
For \(x+3y=18\), intercepts are \((18,0)\) and \((0,6)\).

The vertices are

\[
(0,0),\quad (0,6),\quad \left(\frac{24}{5},\frac{22}{5}\right),\quad (7,0).
\]

## Solution 11

Evaluate \(P=5x+4y\):

\[
P(0,0)=0,
\]

\[
P(0,6)=24,
\]

\[
P\left(\frac{24}{5},\frac{22}{5}\right)=5\cdot\frac{24}{5}+4\cdot\frac{22}{5}=24+\frac{88}{5}=\frac{208}{5},
\]

\[
P(7,0)=35.
\]

Maximum is

\[
\frac{208}{5}
\]

at

\[
\left(\frac{24}{5},\frac{22}{5}\right).
\]

## Solution 12

Near \((3.6,6.8)\), test:

\[
(3,6):\quad 5(3)+3(6)=33\le38,
\]

\[
P=18(3)+25(6)=204.
\]

\[
(3,7):\quad 15+21=36\le38,
\]

\[
P=54+175=229.
\]

\[
(4,6):\quad 20+18=38\le38,
\]

\[
P=72+150=222.
\]

\[
(4,7):\quad 20+21=41>38,
\]

reject.

Check \((2,8)\):

\[
5(2)+3(8)=10+24=34\le38,
\]

\[
P=18(2)+25(8)=36+200=236.
\]

Check \((3,8)\):

\[
15+24=39>38,
\]

reject.

Best integer solution:

\[
\boxed{x=2,\quad y=8,\quad P=236.}
\]

## Solution 13

For

\[
P=ax+by,
\]

objective-line gradient is

\[
-\frac{a}{b}.
\]

Given gradient \(-\frac45\),

\[
a:b=4:5.
\]

Simplest objective:

\[
P=4x+5y.
\]

If \(P=260\) at \((10,6)\), write

\[
P=k(4x+5y).
\]

Then

\[
260=k(4(10)+5(6))=70k,
\]

so

\[
k=\frac{26}{7}.
\]

Thus

\[
P=\frac{26}{7}(4x+5y).
\]

## Solution 14

Since

\[
P=3x+6y=3(x+2y),
\]

and on the segment

\[
x+2y=20,
\]

we have

\[
P=3(20)=60.
\]

Every point on the segment gives the same objective value, so the optimum is a whole edge rather than a single point.

## Solution 15

Let \(x\) be small planters and \(y\) large planters. Maximise

\[
P=12x+30y.
\]

Constraints:

\[
2x+3y\le48,
\]

\[
x+4y\le40,
\]

\[
x+2y\le28,
\]

\[
x,y\ge0.
\]

Vertices are

\[
(0,0),\quad (0,10),\quad \left(\frac{72}{5},\frac{32}{5}\right),\quad (24,0).
\]

Objective values:

\[
P(0,0)=0,
\]

\[
P(0,10)=300,
\]

\[
P\left(\frac{72}{5},\frac{32}{5}\right)=12\cdot\frac{72}{5}+30\cdot\frac{32}{5}=\frac{864}{5}+192=\frac{1824}{5}=364.8,
\]

\[
P(24,0)=288.
\]

Continuous maximum:

\[
\boxed{£364.80\text{ at }x=14.4,\ y=6.4.}
\]

If planters must be whole objects, an integer check is required.

## Solution 16

This lesson prepares for simplex by teaching decision variables, objective functions, constraints, feasible regions and vertices. The missing CCEA skill is the simplex algorithm and tableau: slack variables, tableau setup, pivoting, row operations and reading the final solution. Graphical LP must therefore be labelled as foundation only, not full coverage of `FA22-ALGGRAPH-LO003`.

# 15. Exam Technique Notes

1. Define variables first.
2. Use correct units.
3. Write “Maximise” or “Minimise”.
4. Use “subject to” before constraints.
5. Split double inequalities.
6. Use solid boundaries for \(\le,\ge\) and dotted boundaries for \(<,>\).
7. Keep exact vertex coordinates where possible.
8. Test all relevant vertices.
9. Check integer feasibility when required.
10. Write the final answer in context.
11. Do not treat this as full simplex coverage.

# 16. Syllabus Gap Check

## LO coverage

| LO ID | Official wording | Covered? | Gap |
|---|---|---|---|
| `FA22-ALGGRAPH-LO003` | use the simplex algorithm and tableau to solve two-variable linear programming problems | Partially | Simplex algorithm and tableau are missing |

## Evidence coverage

| Lesson content | Evidence support | Judgement |
|---|---|---|
| LP definition | Chapter 6 PDF | Strong |
| Decision variables | Transcript | Strong |
| Objective function | PDF and transcript examples | Strong |
| Constraints | PDF and transcript examples | Strong |
| Feasible region | PDF graphical methods | Strong |
| Sliding ruler | PDF and transcript | Strong foundation |
| Vertex testing | PDF and transcript | Strong foundation |
| Integer checking | Transcript | Supporting evidence |
| Simplex tableau | Not supplied | Missing |

## Off-Spec Content Found but Excluded

| Content | Why excluded from core | Treatment |
|---|---|---|
| Higher-dimensional LP | CCEA LO is two-variable simplex tableau | Mentioned as enrichment only |
| Pearson/Edexcel exercise labels | Not CCEA authority | Used only as aligned foundation evidence |
| Three-variable examples | CCEA LO is two-variable | Used only for language training |
| Graphical LP as final endpoint | CCEA requires simplex tableau | Treated as foundation |
| Simplex algorithm details | Required but not evidenced | Not invented; logged as missing |

## Missing evidence

- Chapter 7 Simplex Algorithm PDF/transcript.
- Simplex tableau worked examples.
- CCEA past-paper questions and mark schemes.
- CCEA-specific LP formulation examples.
- Fully readable extraction of the screenshot PDF.

# 17. Recommended Enhancements Not in the Evidence

AI-proposed enhancements include: formulation flowcharts, feasible-region diagrams, objective-line animations, vertex testing visuals, integer lattice diagrams, a constraint translator widget, feasible-region builder, vertex-testing calculator and integer-candidate checker. These are teaching enhancements, not original evidence diagrams.

# 18. Supplementary Sources Used

## Project sources

- `CCEA_GCE_Further_Mathematics_Specification_Map.md`
- `Further_Maths_README_module_map.md`
- `Further_Maths_EVIDENCE_DROP_CHECKLIST.md`
- `Ordinary_A_Level_Maths_Bridge_Spec_Extracts.md`
- `CCEA_GCE_Mathematics_Specification_Map.md`

## Lesson-specific sources

- `Decision Maths 1 chapter 6 Linear Programming.pdf`
- `transcripts.md`
- `Chapter_6_Linear_Programming_💻_(Decision_1)_screenshots.pdf`

## Evidence boundary statement

This lesson is a foundation lesson for `FA22-ALGGRAPH-LO003`. It does not complete the LO because it does not teach simplex tableau setup, slack variables, pivot choices, row operations or final tableau interpretation.

# 19. Final Student Checklist

## Prerequisite confidence

- [ ] Rearrange linear equations.
- [ ] Convert decimals, fractions and percentages.
- [ ] Plot straight lines from intercepts.
- [ ] Solve simultaneous equations.
- [ ] Interpret inequalities on a coordinate grid.

## Further Maths method

- [ ] Define decision variables clearly.
- [ ] Write the objective function.
- [ ] State maximise or minimise.
- [ ] Translate resource, demand, ratio and percentage conditions into constraints.
- [ ] Add non-negativity constraints.
- [ ] Rewrite decimal constraints with integer coefficients.
- [ ] Identify feasible and infeasible points.
- [ ] Draw boundary lines and shade rejected regions.
- [ ] Use objective lines or vertex testing.
- [ ] Check integer points when necessary.

## Exam technique

- [ ] Use exact vertices where possible.
- [ ] Reject infeasible integer points.
- [ ] Interpret the final answer in context.
- [ ] State clearly whether the answer is continuous or integer-context.

## CCEA boundary

- [ ] This lesson supports `FA22-ALGGRAPH-LO003`.
- [ ] This lesson does not fully cover `FA22-ALGGRAPH-LO003`.
- [ ] A separate simplex tableau lesson is required.
