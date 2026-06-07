# 1. Lesson Title and Metadata

# Simplex Algorithm and Tableau for Two-Variable Linear Programming

## Metadata

| Field | Value |
|---|---|
| Date generated | 2026-06-04 |
| Course | CCEA GCE Further Mathematics |
| Unit | FA22: Further A2 2 Applied Mathematics |
| Applied section | Section D: Discrete and Decision Mathematics |
| Specification topic code | FA22-ALGGRAPH |
| Specification topic name | Algorithms on graphs |
| Lesson topic name | Simplex Algorithm and Tableau for Two-Variable Linear Programming |
| Topic slug | simplex_algorithm_tableau |
| Topic Pascal | SimplexAlgorithmTableau |
| Topic ID | FA22SimplexAlgorithmTableau |
| Lesson file name | FA22_simplex_algorithm_tableau_lesson.md |
| Further Maths LO IDs | FA22-ALGGRAPH-LO003 |
| Core CCEA boundary | Two-variable linear programming problems solved using the simplex algorithm and tableau |
| Bridge tags | ordinary inequalities; simultaneous equations; graphical feasible regions; optimisation language |
| Topic tags | #FA22 #ALGGRAPH #Decision #Simplex #Tableau #LinearProgramming #SectionD |

## Learning outcome identity

This lesson is built around:

\[
\boxed{\text{FA22-ALGGRAPH-LO003}}
\]

Official wording:

\[
\boxed{\text{Use the simplex algorithm and tableau to solve two-variable linear programming problems.}}
\]

## Boundary warning

This lesson deliberately focuses on **two-variable** simplex tableau problems, because that is the CCEA boundary for this learning outcome.

Material in the uploaded Decision 1 evidence on:

- three or more decision variables;
- integer solutions;
- two-stage simplex;
- Big-M method;
- artificial variables;
- general \(n\)-variable simplex;

is logged as useful enrichment but is **not** taught as core CCEA content here.

# 2. Evidence Map

## 2.1 Project Sources Used

| Source | Role in this lesson |
|---|---|
| `CCEA_GCE_Further_Mathematics_Specification_Map.md` | Primary authority for unit, topic code, LO ID and syllabus boundary. |
| `Further_Maths_README_module_map.md` | Confirms `FA22-ALGGRAPH` belongs to Section D: Discrete and Decision Mathematics and has a limited ordinary Maths bridge. |
| `Further_Maths_EVIDENCE_DROP_CHECKLIST.md` | General evidence-status reference. |
| `Ordinary_A_Level_Maths_Bridge_Spec_Extracts.md` | Ordinary Maths bridge only. |
| `CCEA_GCE_Mathematics_Specification_Map.md` | Ordinary Maths bridge only. |

## 2.2 Lesson-Specific Evidence Used

| Evidence | Evidence type | Use |
|---|---|---|
| `Decision Maths 1 chapter 7 Simplex Algorithm updated may 22B.pdf` | Slide/PDF evidence | Used for formulating LPs, slack variables, simplex method explanation, tableau algorithm, pivot rules, theta values and worked examples. |
| `Chapter_7_Simplex_Algorithm_💻_(Decision_1)_screenshots.pdf` | Screenshot visual evidence | Used for visible slide structure, graph/table visual planning, and teacher annotations where readable. Text was not automatically parsed. |
| `transcripts.md` | Teacher transcript | Used for conceptual phrasing, warnings, and explanation of why the tableau steps work. |

## 2.3 Evidence Limitations

The screenshot PDF is image-only. The visible early pages showed the chapter title, geometric motivation, linear-programming formulation, the Andy tablet example, and slack-variable annotations. Because the full screenshot PDF was not manually inspected page-by-page, no uninspected diagram detail is claimed.

Diagram evidence is partially unclear here. The description below preserves the visible/readable details only. No uninspected visual detail is claimed.

# 3. Specification Alignment

| LO ID | Official wording | Lesson coverage | Evidence source | Syllabus boundary | Ordinary A-Level Maths bridge |
|---|---|---|---|---|---|
| FA22-ALGGRAPH-LO003 | Use the simplex algorithm and tableau to solve two-variable linear programming problems | The lesson teaches: formulate a two-variable LP; introduce slack variables; construct a tableau; identify basic variables; choose pivot column; calculate \(\theta\) values; choose pivot row; perform row operations; repeat until optimal; read off the solution. | CCEA Further Maths spec map; Decision 1 PDF; transcript; screenshot evidence | Core examples and generated practice use two decision variables \(x,y\). Slack variables may be added, but extra decision variables are not core. | Builds on inequalities, simultaneous equations, graph interpretation, and optimisation language. |

## 3.1 What is definitely on-spec

The following are taught as core:

\[
\begin{aligned}
&\text{linear objective functions in two variables, such as } P=ax+by,\\
&\text{linear constraints in two variables, such as } ax+by\leq c,\\
&\text{non-negativity constraints } x\geq0,\ y\geq0,\\
&\text{slack variables for converting inequalities into equations,}\\
&\text{simplex tableau construction and pivoting,}\\
&\text{reading the optimum from the final tableau.}
\end{aligned}
\]

## 3.2 What is not taught as core

The following are not core in this lesson:

\[
\begin{aligned}
&\text{three-variable simplex tableaux,}\\
&\text{four-variable linear programming formulation,}\\
&\text{integer simplex,}\\
&\text{two-stage simplex,}\\
&\text{Big-M method,}\\
&\text{artificial variables,}\\
&\text{general } n\text{-variable simplex.}
\end{aligned}
\]

# 4. Learning Objectives

## 4.1 Core Further Maths objectives

By the end of this lesson, you should be able to:

1. State what a two-variable linear programming problem is.
2. Define decision variables \(x\) and \(y\) clearly in context.
3. Write an objective function such as

\[
P=ax+by.
\]

4. Write constraints in the form

\[
ax+by\leq c,\qquad x\geq0,\qquad y\geq0.
\]

5. Introduce slack variables to convert inequalities into equations.
6. Build an initial simplex tableau.
7. Identify basic variables and non-basic variables.
8. Select a pivot column using the most negative entry in the objective row.
9. Calculate \(\theta\) values using

\[
\theta=\frac{\text{value entry}}{\text{positive pivot-column entry}}.
\]

10. Select the pivot row using the smallest positive \(\theta\).
11. Perform row operations so the pivot column contains one \(1\) and otherwise zeros.
12. Repeat the process until there are no negative entries in the objective row.
13. Read the optimal values of \(x,y\) and the objective value \(P\) from the final tableau.
14. Interpret the solution in the original context.

## 4.2 Bridge objectives

You should also be able to explain:

1. How ordinary graphical linear programming becomes simplex tableau.
2. Why vertices matter.
3. Why a slack variable measures unused capacity.
4. Why row operations in the tableau are controlled elimination steps.
5. Why the objective row tells us whether the value can still be improved.

## 4.3 Exam technique objectives

You should be able to:

1. Define variables in context, not just by letters.
2. Include non-negativity constraints.
3. Label the pivot column, pivot row and pivot.
4. Show \(\theta\) values clearly.
5. Avoid using a zero or negative \(\theta\) as the pivot-row choice.
6. Stop only when the objective row has no negative entries.
7. Read non-basic variables as zero.
8. Give the final answer in a sentence.

# 5. Explicit Prerequisite Recap

## 5.1 GCSE foundations

You should already be comfortable with:

- solving linear equations;
- substituting values into formulae;
- rearranging formulae;
- working with inequalities;
- reading tables;
- plotting straight lines;
- interpreting intersections of lines.

For example, if

\[
5x+7y\leq70,
\]

then the boundary line is

\[
5x+7y=70.
\]

The feasible side is the side satisfying the inequality.

## 5.2 Ordinary A-Level Maths foundations

You should already know how to:

- solve simultaneous linear equations;
- interpret straight-line graphs;
- use inequalities to describe regions;
- understand the language of maximising and minimising;
- carry out algebraic elimination accurately.

For example, solving

\[
\begin{cases}
5x+7y=70,\\
10x+3y=60
\end{cases}
\]

gives the intersection of two boundary lines. In ordinary graphical linear programming, that intersection is a vertex of the feasible region.

## 5.3 Previous Further Mathematics foundations

From earlier Further Mathematics Decision work, it helps if you are comfortable with:

- algorithmic step-by-step procedures;
- tables as a way of encoding information;
- precise notation;
- interpreting what a calculation means in context.

## 5.4 A-Level Maths Bridge: What You Already Know and What Further Maths Changes

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| Ordinary algebra and inequalities | Solve and rearrange inequalities | Inequalities become resource constraints in a linear programming problem | Do not forget the non-negativity constraints \(x\geq0,\ y\geq0\). |
| Ordinary coordinate geometry | Lines can intersect and enclose regions | The feasible region is explored through its vertices | A tableau hides the graph, so you must keep the geometric meaning alive in your head. |
| Ordinary simultaneous equations | Use elimination to remove variables | Tableau row operations are organised elimination steps | One arithmetic slip can corrupt the tableau. Keep fractions exact. |
| Ordinary optimisation language | Maximise or minimise a quantity | Simplex improves the objective function vertex by vertex | The “best direction” is read from the objective row after standardising it, not guessed from the original wording. |

In ordinary A-Level Maths, this idea appeared as graphing straight lines, shading inequalities and testing vertices.

In Further Maths, the same idea becomes an algorithm: instead of drawing the feasible region and reading vertices from a graph, the simplex tableau lets you move algebraically from one vertex to the next.

The key upgrade is that the tableau packages the constraints, slack variables and objective function into one machine-like calculation.

The danger is that the table can become a number swamp. Every entry means something. The pivot column says what variable we are increasing. The pivot row says which constraint we hit first. The value column tells us the current size of each basic variable.

# 6. Big Picture Explanation

## 6.1 Why simplex exists

In graphical linear programming, you draw a feasible region and test the vertices.

For a two-variable problem, this is visual:

\[
x \text{ on the horizontal axis},\qquad y \text{ on the vertical axis}.
\]

A typical objective function might be

\[
P=3x+2y.
\]

A typical set of constraints might be

\[
5x+7y\leq70,
\]

\[
10x+3y\leq60,
\]

\[
x\geq0,\qquad y\geq0.
\]

The best value of \(P\) occurs at a vertex of the feasible region, provided the feasible region is bounded in the improving direction.

The simplex algorithm is a vertex-hunter. It starts at a basic feasible solution, usually the origin, then moves along an edge to a neighbouring vertex where the objective function improves. It keeps doing this until no adjacent move improves the objective function.

## 6.2 Why CCEA still asks for tableau when the problem is two-variable

Even though CCEA specifies two-variable linear programming here, the simplex tableau is valuable because it tests whether you understand:

- objective functions;
- constraints;
- slack variables;
- feasible solutions;
- row operations;
- algorithmic decision-making;
- interpretation of a final optimum.

The graph tells the story. The tableau does the arithmetic.

## 6.3 The geometric idea

Suppose we have

\[
5x+7y+r=70.
\]

The slack variable \(r\) measures how much unused capacity remains in the first constraint.

If

\[
5x+7y=70,
\]

then

\[
r=0.
\]

So the boundary line

\[
5x+7y=70
\]

is also the line where

\[
r=0.
\]

Likewise, if

\[
10x+3y+s=60,
\]

then the boundary line

\[
10x+3y=60
\]

is also the line where

\[
s=0.
\]

At a vertex in a two-variable problem with two slack variables, two of the four variables

\[
x,\quad y,\quad r,\quad s
\]

are zero.

That is the quiet clockwork inside the tableau.

## 6.4 What the student should watch for

The main things to watch are:

1. Are the constraints in the right form?
2. Have slack variables been added correctly?
3. Is the objective function written in standard tableau form?
4. Did you choose the most negative objective-row entry?
5. Did you calculate \(\theta\) values only where the pivot-column entry is positive?
6. Did you choose the smallest positive \(\theta\)?
7. Did your row operations create a pivot-column pattern of one \(1\) and zeros?
8. Did you stop only when there were no negative entries in the objective row?
9. Did you read non-basic variables as zero?
10. Did you interpret the answer in the original context?

# 7. Key Definitions and Notation

## 7.1 Linear programming problem

A **linear programming problem** is an optimisation problem where:

- the objective function is linear;
- the constraints are linear inequalities or equations;
- the variables usually have non-negativity constraints.

For this CCEA lesson, the decision variables are restricted to two variables, usually

\[
x,\qquad y.
\]

A typical maximisation problem is:

\[
\text{Maximise } P=ax+by
\]

subject to

\[
\alpha x+\beta y\leq c,
\]

\[
\gamma x+\delta y\leq d,
\]

\[
x\geq0,\qquad y\geq0.
\]

## 7.2 Decision variables

The **decision variables** are the variables whose values we choose.

For example:

\[
x=\text{number of units of product A},
\]

\[
y=\text{number of units of product B}.
\]

Teacher warning preserved from the transcript:

Do not merely write “let \(x\) be A and \(y\) be B”. Say what is being counted or measured. For example, write:

\[
x=\text{the number of product A made per day},
\]

not just:

\[
x=\text{product A}.
\]

## 7.3 Objective function

The **objective function** is the quantity being maximised or minimised.

For example:

\[
P=3x+2y.
\]

In a simplex tableau for a maximisation problem, write this in standard form as

\[
P-3x-2y=0.
\]

This is why the objective row contains negative coefficients for \(x\) and \(y\).

## 7.4 Constraints

A **constraint** is a restriction on the decision variables.

For example:

\[
5x+7y\leq70.
\]

This might mean that a resource with total capacity \(70\) is used up by \(5\) units for every \(x\) and \(7\) units for every \(y\).

## 7.5 Non-negativity constraints

In this topic, decision variables and slack variables must not be negative.

For decision variables:

\[
x\geq0,\qquad y\geq0.
\]

For slack variables:

\[
r\geq0,\qquad s\geq0.
\]

So the full non-negativity condition is often:

\[
x,y,r,s\geq0.
\]

## 7.6 Slack variable

A **slack variable** measures unused capacity.

If

\[
5x+7y\leq70,
\]

then introduce a slack variable \(r\geq0\):

\[
5x+7y+r=70.
\]

If \(5x+7y=52\), then

\[
52+r=70,
\]

so

\[
r=18.
\]

The unused capacity is \(18\).

If \(5x+7y=70\), then

\[
70+r=70,
\]

so

\[
r=0.
\]

There is no unused capacity.

## 7.7 Basic variable

A **basic variable** is a variable currently read from the value column of the tableau.

In the initial tableau for

\[
5x+7y+r=70,
\]

\[
10x+3y+s=60,
\]

the basic variables are usually

\[
r,\quad s,\quad P.
\]

This is because at the origin,

\[
x=0,\qquad y=0.
\]

Then

\[
r=70,\qquad s=60,\qquad P=0.
\]

## 7.8 Non-basic variable

A **non-basic variable** is a variable not listed in the basic-variable column.

Non-basic variables have value zero.

At the initial origin tableau, \(x\) and \(y\) are non-basic, so

\[
x=0,\qquad y=0.
\]

## 7.9 Pivot column

The **pivot column** is chosen from the objective row.

For a maximisation problem in standard form, choose the column with the most negative entry in the objective row.

This is because increasing that variable increases the objective function most quickly.

## 7.10 Theta value

A **theta value** is used to decide which constraint is hit first as we move to the next vertex.

For each constraint row with a positive pivot-column entry,

\[
\theta=\frac{\text{value entry}}{\text{pivot-column entry}}.
\]

The pivot row is the row with the smallest positive \(\theta\).

## 7.11 Pivot row

The **pivot row** is the row selected using the smallest positive \(\theta\).

It tells us which basic variable leaves the basis.

## 7.12 Pivot

The **pivot** is the entry where the pivot column and pivot row meet.

The pivot is divided into its row to make it equal to \(1\).

Then row operations are used to make every other entry in the pivot column equal to \(0\).

## 7.13 Optimal tableau

A maximisation tableau is **optimal** when there are no negative entries left in the objective row.

At that point, no variable can be increased to improve \(P\).

# 8. Core Theory

## 8.1 The CCEA simplex problem type

The core CCEA problem in this lesson has this shape:

\[
\text{Maximise }P=ax+by
\]

subject to

\[
\alpha x+\beta y\leq c,
\]

\[
\gamma x+\delta y\leq d,
\]

\[
x\geq0,\qquad y\geq0.
\]

The coefficients \(a,b,\alpha,\beta,\gamma,\delta,c,d\) are constants supplied by the question.

The variables \(x,y\) are decision variables.

The goal is to find the values of \(x\) and \(y\) that give the largest possible value of \(P\), while satisfying every constraint.

**Bridge Note:** In ordinary A-Level Maths, you may have solved inequalities by graphing them. Here, Further Maths turns the graph method into a table algorithm. The vertices are still the heroes, but they now wear row-operation armour.

## 8.2 Step 1: Convert inequalities into equations using slack variables

Suppose the constraints are

\[
5x+7y\leq70,
\]

\[
10x+3y\leq60.
\]

Introduce a slack variable \(r\) for the first constraint:

\[
5x+7y+r=70.
\]

Introduce a different slack variable \(s\) for the second constraint:

\[
10x+3y+s=60.
\]

The non-negativity conditions are

\[
x,y,r,s\geq0.
\]

Why do we add a slack variable?

Because if

\[
5x+7y<70,
\]

then there is spare capacity. The slack variable fills the gap so the expression becomes exactly \(70\).

For example, if

\[
5x+7y=40,
\]

then

\[
40+r=70,
\]

so

\[
r=30.
\]

If

\[
5x+7y=70,
\]

then

\[
70+r=70,
\]

so

\[
r=0.
\]

The boundary line is the place where the slack variable is zero.

## 8.3 Step 2: Put the objective function into standard form

If

\[
P=3x+2y,
\]

then for the tableau write

\[
P-3x-2y=0.
\]

This produces the objective row coefficients:

\[
-3,\quad -2,\quad 0,\quad 0,\quad 0.
\]

The first \(0\) is for \(r\), the second \(0\) is for \(s\), and the final \(0\) is the value column.

## 8.4 Step 3: Build the initial tableau

Using

\[
5x+7y+r=70,
\]

\[
10x+3y+s=60,
\]

\[
P-3x-2y=0,
\]

create the tableau.

The column order is:

\[
x,\quad y,\quad r,\quad s,\quad \text{Value}.
\]

The initial basic variables are:

\[
r,\quad s,\quad P.
\]

So the initial tableau is:

| Basic variable | \(x\) | \(y\) | \(r\) | \(s\) | Value |
|---|---:|---:|---:|---:|---:|
| \(r\) | \(5\) | \(7\) | \(1\) | \(0\) | \(70\) |
| \(s\) | \(10\) | \(3\) | \(0\) | \(1\) | \(60\) |
| \(P\) | \(-3\) | \(-2\) | \(0\) | \(0\) | \(0\) |

At this stage, the non-basic variables are

\[
x=0,\qquad y=0.
\]

Reading the constraint rows:

\[
r=70,\qquad s=60.
\]

Reading the objective row:

\[
P=0.
\]

This is the origin solution:

\[
(x,y)=(0,0).
\]

## 8.5 Step 4: Choose the pivot column

Look along the objective row:

\[
-3,\quad -2,\quad 0,\quad 0.
\]

The most negative entry is

\[
-3.
\]

This is in the \(x\)-column.

So the pivot column is the \(x\)-column.

Why?

Because

\[
P-3x-2y=0
\]

can be rearranged to

\[
P=3x+2y.
\]

Increasing \(x\) increases \(P\) by \(3\) per unit, while increasing \(y\) increases \(P\) by \(2\) per unit. So the tableau chooses \(x\) first.

**Bridge Note:** In ordinary Maths, you might inspect \(P=3x+2y\) directly. In the tableau, you inspect \(P-3x-2y=0\), so the “best” improving direction appears as the most negative coefficient.

## 8.6 Step 5: Calculate theta values

For each constraint row, calculate

\[
\theta=\frac{\text{value entry}}{\text{entry in pivot column}}.
\]

The pivot column is the \(x\)-column.

For the \(r\)-row:

\[
\theta=\frac{70}{5}=14.
\]

For the \(s\)-row:

\[
\theta=\frac{60}{10}=6.
\]

So the theta values are:

| Basic variable | Pivot-column entry | Value | \(\theta\) |
|---|---:|---:|---:|
| \(r\) | \(5\) | \(70\) | \(70\div5=14\) |
| \(s\) | \(10\) | \(60\) | \(60\div10=6\) |

Choose the smallest positive \(\theta\):

\[
6<14.
\]

So the pivot row is the \(s\)-row.

The pivot is the entry where the \(x\)-column and \(s\)-row meet:

\[
\boxed{10}.
\]

## 8.7 Why the smallest positive theta matters

As \(x\) increases from \(0\), one constraint will be reached first.

From the first constraint, if \(y=0\) and \(r=0\):

\[
5x+7(0)+0=70,
\]

\[
5x=70,
\]

\[
x=14.
\]

From the second constraint, if \(y=0\) and \(s=0\):

\[
10x+3(0)+0=60,
\]

\[
10x=60,
\]

\[
x=6.
\]

So the second constraint is reached first.

That is why the pivot row is the row with the smaller positive theta value.

If we ignored this and moved all the way to \(x=14\), then the second constraint would be broken. In geometric language, we would leave the feasible region. In tableau language, the wrong pivot row poisons the calculation.

## 8.8 Step 6: Divide the pivot row by the pivot

The pivot row is:

\[
[10,\ 3,\ 0,\ 1,\ 60].
\]

The pivot is \(10\).

Divide the whole row by \(10\):

\[
\left[1,\ \frac{3}{10},\ 0,\ \frac{1}{10},\ 6\right].
\]

The basic variable changes from \(s\) to \(x\), because \(x\) has entered the basis.

So the new pivot row is:

| Basic variable | \(x\) | \(y\) | \(r\) | \(s\) | Value |
|---|---:|---:|---:|---:|---:|
| \(x\) | \(1\) | \(\frac{3}{10}\) | \(0\) | \(\frac{1}{10}\) | \(6\) |

## 8.9 Step 7: Use row operations to eliminate the pivot-column variable from the other rows

The pivot column is the \(x\)-column.

We need the \(x\)-column to become:

\[
\begin{bmatrix}
0\\
1\\
0
\end{bmatrix}.
\]

The pivot row already has \(1\) in the \(x\)-column.

Now eliminate \(x\) from the other rows.

### 8.9.1 Eliminate \(x\) from the \(r\)-row

Original \(r\)-row:

\[
[5,\ 7,\ 1,\ 0,\ 70].
\]

New pivot row:

\[
\left[1,\ \frac{3}{10},\ 0,\ \frac{1}{10},\ 6\right].
\]

Use:

\[
R_r \leftarrow R_r-5R_x.
\]

Calculate every entry.

For the \(x\)-entry:

\[
5-5(1)=5-5=0.
\]

For the \(y\)-entry:

\[
7-5\left(\frac{3}{10}\right)
=
7-\frac{15}{10}
=
7-\frac{3}{2}
=
\frac{14}{2}-\frac{3}{2}
=
\frac{11}{2}.
\]

For the \(r\)-entry:

\[
1-5(0)=1.
\]

For the \(s\)-entry:

\[
0-5\left(\frac{1}{10}\right)
=
-\frac{5}{10}
=
-\frac{1}{2}.
\]

For the value entry:

\[
70-5(6)=70-30=40.
\]

So the new row is:

\[
\left[0,\ \frac{11}{2},\ 1,\ -\frac{1}{2},\ 40\right].
\]

### 8.9.2 Eliminate \(x\) from the objective row

Original objective row:

\[
[-3,\ -2,\ 0,\ 0,\ 0].
\]

New pivot row:

\[
\left[1,\ \frac{3}{10},\ 0,\ \frac{1}{10},\ 6\right].
\]

Use:

\[
R_P\leftarrow R_P+3R_x.
\]

For the \(x\)-entry:

\[
-3+3(1)=0.
\]

For the \(y\)-entry:

\[
-2+3\left(\frac{3}{10}\right)
=
-2+\frac{9}{10}
=
-\frac{20}{10}+\frac{9}{10}
=
-\frac{11}{10}.
\]

For the \(r\)-entry:

\[
0+3(0)=0.
\]

For the \(s\)-entry:

\[
0+3\left(\frac{1}{10}\right)
=
\frac{3}{10}.
\]

For the value entry:

\[
0+3(6)=18.
\]

So the new objective row is:

\[
\left[0,\ -\frac{11}{10},\ 0,\ \frac{3}{10},\ 18\right].
\]

## 8.10 The tableau after the first pivot

| Basic variable | \(x\) | \(y\) | \(r\) | \(s\) | Value |
|---|---:|---:|---:|---:|---:|
| \(r\) | \(0\) | \(\frac{11}{2}\) | \(1\) | \(-\frac{1}{2}\) | \(40\) |
| \(x\) | \(1\) | \(\frac{3}{10}\) | \(0\) | \(\frac{1}{10}\) | \(6\) |
| \(P\) | \(0\) | \(-\frac{11}{10}\) | \(0\) | \(\frac{3}{10}\) | \(18\) |

The basic variables are now:

\[
r,\quad x,\quad P.
\]

The non-basic variables are:

\[
y=0,\qquad s=0.
\]

Reading the value column:

\[
r=40,\qquad x=6,\qquad P=18.
\]

So the current vertex is:

\[
(x,y)=(6,0).
\]

The current objective value is:

\[
P=18.
\]

## 8.11 Step 8: Check whether the tableau is optimal

Look along the objective row:

\[
0,\quad -\frac{11}{10},\quad 0,\quad \frac{3}{10}.
\]

There is still a negative entry:

\[
-\frac{11}{10}.
\]

So the tableau is not optimal.

The pivot column is now the \(y\)-column.

## 8.12 Step 9: Calculate new theta values

Use the \(y\)-column.

For the \(r\)-row:

\[
\theta=\frac{40}{\frac{11}{2}}
=
40\div\frac{11}{2}
=
40\times\frac{2}{11}
=
\frac{80}{11}.
\]

For the \(x\)-row:

\[
\theta=\frac{6}{\frac{3}{10}}
=
6\div\frac{3}{10}
=
6\times\frac{10}{3}
=
20.
\]

Compare:

\[
\frac{80}{11}\approx 7.27,
\]

\[
20=20.
\]

The smallest positive theta is

\[
\frac{80}{11}.
\]

So the pivot row is the \(r\)-row.

The pivot is

\[
\boxed{\frac{11}{2}}.
\]

## 8.13 Step 10: Divide the pivot row by the pivot

The pivot row is:

\[
\left[0,\ \frac{11}{2},\ 1,\ -\frac{1}{2},\ 40\right].
\]

Divide by \(\frac{11}{2}\), which is the same as multiplying by \(\frac{2}{11}\).

For the \(x\)-entry:

\[
0\times\frac{2}{11}=0.
\]

For the \(y\)-entry:

\[
\frac{11}{2}\times\frac{2}{11}=1.
\]

For the \(r\)-entry:

\[
1\times\frac{2}{11}=\frac{2}{11}.
\]

For the \(s\)-entry:

\[
-\frac{1}{2}\times\frac{2}{11}=-\frac{1}{11}.
\]

For the value entry:

\[
40\times\frac{2}{11}=\frac{80}{11}.
\]

The basic variable changes from \(r\) to \(y\).

So the new pivot row is:

\[
\left[0,\ 1,\ \frac{2}{11},\ -\frac{1}{11},\ \frac{80}{11}\right].
\]

## 8.14 Step 11: Eliminate \(y\) from the other rows

The pivot column is now the \(y\)-column.

We need it to become:

\[
\begin{bmatrix}
1\\
0\\
0
\end{bmatrix}.
\]

The pivot row already has \(1\) in the \(y\)-column.

Now eliminate \(y\) from the \(x\)-row and objective row.

### 8.14.1 Eliminate \(y\) from the \(x\)-row

Current \(x\)-row:

\[
\left[1,\ \frac{3}{10},\ 0,\ \frac{1}{10},\ 6\right].
\]

Pivot row:

\[
\left[0,\ 1,\ \frac{2}{11},\ -\frac{1}{11},\ \frac{80}{11}\right].
\]

Use:

\[
R_x\leftarrow R_x-\frac{3}{10}R_y.
\]

For the \(x\)-entry:

\[
1-\frac{3}{10}(0)=1.
\]

For the \(y\)-entry:

\[
\frac{3}{10}-\frac{3}{10}(1)=0.
\]

For the \(r\)-entry:

\[
0-\frac{3}{10}\left(\frac{2}{11}\right)
=
-\frac{6}{110}
=
-\frac{3}{55}.
\]

For the \(s\)-entry:

\[
\frac{1}{10}-\frac{3}{10}\left(-\frac{1}{11}\right)
=
\frac{1}{10}+\frac{3}{110}
=
\frac{11}{110}+\frac{3}{110}
=
\frac{14}{110}
=
\frac{7}{55}.
\]

For the value entry:

\[
6-\frac{3}{10}\left(\frac{80}{11}\right)
=
6-\frac{240}{110}
=
6-\frac{24}{11}
=
\frac{66}{11}-\frac{24}{11}
=
\frac{42}{11}.
\]

So the new \(x\)-row is:

\[
\left[1,\ 0,\ -\frac{3}{55},\ \frac{7}{55},\ \frac{42}{11}\right].
\]

### 8.14.2 Eliminate \(y\) from the objective row

Current objective row:

\[
\left[0,\ -\frac{11}{10},\ 0,\ \frac{3}{10},\ 18\right].
\]

Pivot row:

\[
\left[0,\ 1,\ \frac{2}{11},\ -\frac{1}{11},\ \frac{80}{11}\right].
\]

Use:

\[
R_P\leftarrow R_P+\frac{11}{10}R_y.
\]

For the \(x\)-entry:

\[
0+\frac{11}{10}(0)=0.
\]

For the \(y\)-entry:

\[
-\frac{11}{10}+\frac{11}{10}(1)=0.
\]

For the \(r\)-entry:

\[
0+\frac{11}{10}\left(\frac{2}{11}\right)
=
\frac{2}{10}
=
\frac{1}{5}.
\]

For the \(s\)-entry:

\[
\frac{3}{10}+\frac{11}{10}\left(-\frac{1}{11}\right)
=
\frac{3}{10}-\frac{1}{10}
=
\frac{2}{10}
=
\frac{1}{5}.
\]

For the value entry:

\[
18+\frac{11}{10}\left(\frac{80}{11}\right)
=
18+\frac{80}{10}
=
18+8
=
26.
\]

So the new objective row is:

\[
\left[0,\ 0,\ \frac{1}{5},\ \frac{1}{5},\ 26\right].
\]

## 8.15 Final tableau

| Basic variable | \(x\) | \(y\) | \(r\) | \(s\) | Value |
|---|---:|---:|---:|---:|---:|
| \(y\) | \(0\) | \(1\) | \(\frac{2}{11}\) | \(-\frac{1}{11}\) | \(\frac{80}{11}\) |
| \(x\) | \(1\) | \(0\) | \(-\frac{3}{55}\) | \(\frac{7}{55}\) | \(\frac{42}{11}\) |
| \(P\) | \(0\) | \(0\) | \(\frac{1}{5}\) | \(\frac{1}{5}\) | \(26\) |

The objective row contains no negative entries.

Therefore the tableau is optimal.

The basic variables are:

\[
y,\quad x,\quad P.
\]

The non-basic variables are:

\[
r=0,\qquad s=0.
\]

Read from the value column:

\[
y=\frac{80}{11},
\]

\[
x=\frac{42}{11},
\]

\[
P=26.
\]

So the optimal solution is:

\[
\boxed{x=\frac{42}{11},\qquad y=\frac{80}{11},\qquad P=26.}
\]

## 8.16 Interpretation

The maximum value of the objective function is

\[
\boxed{26}.
\]

It occurs when

\[
\boxed{x=\frac{42}{11},\qquad y=\frac{80}{11}.}
\]

Because

\[
r=0,\qquad s=0,
\]

both resource constraints are exactly at capacity.

Check this in the original constraints.

First constraint:

\[
5x+7y
=
5\left(\frac{42}{11}\right)+7\left(\frac{80}{11}\right)
=
\frac{210}{11}+\frac{560}{11}
=
\frac{770}{11}
=
70.
\]

Second constraint:

\[
10x+3y
=
10\left(\frac{42}{11}\right)+3\left(\frac{80}{11}\right)
=
\frac{420}{11}+\frac{240}{11}
=
\frac{660}{11}
=
60.
\]

Objective function:

\[
P=3x+2y
=
3\left(\frac{42}{11}\right)+2\left(\frac{80}{11}\right)
=
\frac{126}{11}+\frac{160}{11}
=
\frac{286}{11}
=
26.
\]

Everything checks.

The tableau’s final answer matches the original linear programming problem.

## 8.17 The full algorithm in compact form

For a two-variable maximisation problem:

1. Define \(x\) and \(y\) clearly.
2. Write the objective function.
3. Write the constraints.
4. Add slack variables to convert \(\leq\) inequalities into equations.
5. Write the objective in standard form.
6. Create the initial tableau.
7. Find the most negative entry in the objective row.
8. This gives the pivot column.
9. Calculate \(\theta\) for each constraint row:

\[
\theta=\frac{\text{value}}{\text{positive entry in pivot column}}.
\]

10. Choose the smallest positive \(\theta\).
11. This gives the pivot row.
12. The pivot is the entry where pivot row and pivot column meet.
13. Divide the pivot row by the pivot.
14. Replace the basic variable in that row with the pivot-column variable.
15. Use row operations to make all other pivot-column entries zero.
16. Repeat until the objective row has no negative entries.
17. Read the non-zero values from the basic-variable and value columns.
18. Set non-basic variables equal to zero.
19. State the optimal solution in context.

## 8.18 Minimise problems: cautious two-variable extension

Some linear programming questions ask for a minimum.

A common tableau method is to define a new objective function that is the negative of the original objective.

Suppose the original problem is:

\[
\text{Minimise } C=3x-y.
\]

Define

\[
P=-C.
\]

Then

\[
P=-(3x-y),
\]

so

\[
P=-3x+y.
\]

Maximise \(P\) using the usual simplex tableau method.

If the maximum value of \(P\) is \(P_{\max}\), then the minimum value of \(C\) is

\[
C_{\min}=-P_{\max}.
\]

This method is included here only for two-variable tableau problems. It is not a doorway into off-spec multi-variable simplex methods.

## 8.19 Why the final objective row proves optimality

At a stage of the tableau, the objective row can be rearranged to express \(P\) in terms of the non-basic variables.

If a non-basic variable has a negative coefficient in the tableau objective row, increasing that variable can increase \(P\).

If all entries in the objective row are non-negative, increasing any non-basic variable would not increase \(P\). In the tableau language, no improving adjacent vertex remains.

That is why the stopping condition is:

\[
\boxed{\text{No negative entries in the objective row.}}
\]

## 8.20 The exam-critical meaning of zero slack

If a slack variable is zero, the corresponding constraint is exactly full.

For

\[
5x+7y+r=70,
\]

if

\[
r=0,
\]

then

\[
5x+7y=70.
\]

So the first resource is fully used.

For

\[
10x+3y+s=60,
\]

if

\[
s=0,
\]

then

\[
10x+3y=60.
\]

So the second resource is fully used.

In the final solution above,

\[
r=0,\qquad s=0.
\]

So both constraints are at capacity.

That is not just a number fact. It is the story of the optimum: the best solution is wedged exactly where both resource walls meet.

# 9. Visual Asset Integration

This section records every visual that should later be generated in Phase 2 to Phase 4.

## 9.1 Mermaid algorithm flowchart

[VISUAL PLACEHOLDER: FA22SimplexAlgorithmTableauMermaid-001 | Source: CCEA FA22-ALGGRAPH-LO003 + Decision 1 simplex tableau evidence + teacher transcript | Insert from mermaid/FA22SimplexAlgorithmTableauMermaid-001.md | Purpose: Show the full two-variable simplex tableau algorithm as a decision flow.]

**Description of visual:**  
A flowchart should show:

1. Start with a two-variable linear programming problem.
2. Define \(x\) and \(y\).
3. Write the objective function.
4. Add slack variables.
5. Build the initial tableau.
6. Check the objective row.
7. If no negative entries remain, stop.
8. Otherwise choose the most negative entry as the pivot column.
9. Calculate \(\theta\) values.
10. Choose the smallest positive \(\theta\) as the pivot row.
11. Divide by the pivot.
12. Use row operations to clear the pivot column.
13. Repeat.

The visual must include a warning node:

\[
\theta=\frac{\text{value}}{\text{positive pivot-column entry only}}.
\]

## 9.2 SVG feasible-region and vertex movement diagram

[VISUAL PLACEHOLDER: FA22SimplexAlgorithmTableauSVG-001 | Source: Uploaded two-variable graphical simplex evidence | Insert from svg/FA22SimplexAlgorithmTableauSVG-001.svg | Purpose: Show how simplex moves between vertices of the feasible region.]

**Description of visual:**  
The SVG should show a two-variable feasible region for:

\[
5x+7y\leq70,
\]

\[
10x+3y\leq60,
\]

\[
x\geq0,\qquad y\geq0.
\]

It should include:

- horizontal axis labelled \(x\);
- vertical axis labelled \(y\);
- boundary line \(5x+7y=70\);
- boundary line \(10x+3y=60\);
- feasible region shaded softly;
- vertices labelled:
  \[
  (0,0),\quad (6,0),\quad \left(\frac{42}{11},\frac{80}{11}\right),\quad (0,10);
  \]
- simplex route:
  \[
  (0,0)\rightarrow(6,0)\rightarrow\left(\frac{42}{11},\frac{80}{11}\right).
  \]
- annotation:
  \[
  r=0\text{ on }5x+7y=70,
  \]
  \[
  s=0\text{ on }10x+3y=60.
  \]

## 9.3 SVG annotated tableau

[VISUAL PLACEHOLDER: FA22SimplexAlgorithmTableauSVG-002 | Source: Uploaded tableau evidence | Insert from svg/FA22SimplexAlgorithmTableauSVG-002.svg | Purpose: Explain pivot column, theta values, pivot row and pivot in one annotated tableau.]

**Description of visual:**  
The SVG should show the initial tableau:

| Basic variable | \(x\) | \(y\) | \(r\) | \(s\) | Value | \(\theta\) |
|---|---:|---:|---:|---:|---:|---:|
| \(r\) | \(5\) | \(7\) | \(1\) | \(0\) | \(70\) | \(14\) |
| \(s\) | \(10\) | \(3\) | \(0\) | \(1\) | \(60\) | \(6\) |
| \(P\) | \(-3\) | \(-2\) | \(0\) | \(0\) | \(0\) | |

It should highlight:

- the \(x\)-column as pivot column because \(-3\) is the most negative objective-row entry;
- \(\theta=70/5=14\);
- \(\theta=60/10=6\);
- the \(s\)-row as pivot row because \(6\) is the smallest positive \(\theta\);
- pivot \(10\).

## 9.4 Bridge SVG: graphical method versus tableau method

[VISUAL PLACEHOLDER: FA22SimplexAlgorithmTableauBridgeSVG-001 | Source: Ordinary A-Level Maths bridge + Further Maths specification | Insert from svg/FA22SimplexAlgorithmTableauBridgeSVG-001.svg | Purpose: Compare prior ordinary Maths method with Further Maths extension.]

**Description of visual:**  
The SVG should have two columns.

Left column: **Ordinary A-Level Maths graphical method**

- draw constraints;
- shade feasible region;
- find vertices;
- test objective function.

Right column: **Further Maths simplex tableau method**

- add slack variables;
- build tableau;
- pivot from one vertex to the next;
- stop when objective row is optimal.

Between them, include the bridge statement:

\[
\text{Same vertices, different machinery.}
\]

## 9.5 TikZ precise feasible-region diagram

[VISUAL PLACEHOLDER: FA22SimplexAlgorithmTableauTikZ-001 | Source: Two-variable simplex example evidence | Insert from tikz/FA22SimplexAlgorithmTableauTikZ-001.tex | Purpose: Provide a mathematically precise graph for the worked example.]

**Description of visual:**  
The TikZ diagram should draw:

\[
5x+7y=70,
\]

\[
10x+3y=60,
\]

with axes and the feasible region.

Key points:

\[
(0,0),
\]

\[
(6,0),
\]

\[
\left(\frac{42}{11},\frac{80}{11}\right),
\]

\[
(0,10).
\]

The optimum for

\[
P=3x+2y
\]

should be marked at

\[
\left(\frac{42}{11},\frac{80}{11}\right).
\]

## 9.6 TikZ tableau template

[VISUAL PLACEHOLDER: FA22SimplexAlgorithmTableauTikZ-002 | Source: Uploaded tableau evidence | Insert from tikz/FA22SimplexAlgorithmTableauTikZ-002.tex | Purpose: Provide a clean tableau template that can be reused in examples.]

**Description of visual:**  
The TikZ asset should show a generic tableau layout:

| Basic variable | \(x\) | \(y\) | \(r\) | \(s\) | Value |
|---|---:|---:|---:|---:|---:|

It should include labels:

- objective row;
- constraint rows;
- value column;
- pivot column;
- pivot row;
- pivot element.

# 10. Interactive Learning Widgets

This section records interactive placeholders only.

## 10.1 Pivot trainer

[INTERACTIVE PLACEHOLDER: FA22SimplexAlgorithmTableauWidget-001 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FA22SimplexAlgorithmTableauWidget-001.html | Purpose: Train students to identify pivot column, theta values, pivot row and pivot.]

**Student inputs:**

- objective row values;
- constraint row values;
- value column entries.

**Widget displays:**

- most negative objective-row entry;
- pivot column;
- valid \(\theta\) values;
- smallest positive \(\theta\);
- pivot row;
- pivot element.

**Method reinforced:**

\[
\theta=\frac{\text{value}}{\text{positive pivot-column entry}}.
\]

**Errors checked:**

- choosing the largest negative rather than most negative entry;
- calculating \(\theta\) using the wrong column;
- using zero or negative pivot-column entries;
- choosing the largest \(\theta\) instead of the smallest positive \(\theta\);
- forgetting that the pivot row determines which basic variable leaves.

**Exactness rule:**  
The widget should preserve fractions exactly where possible.

## 10.2 Slack-variable converter

[INTERACTIVE PLACEHOLDER: FA22SimplexAlgorithmTableauWidget-002 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FA22SimplexAlgorithmTableauWidget-002.html | Purpose: Help students convert \(\leq\) constraints into equations using slack variables.]

**Student inputs:**

- coefficients \(a,b,c\) for a constraint \(ax+by\leq c\);
- slack-variable name, usually \(r\) or \(s\).

**Widget displays:**

\[
ax+by+r=c.
\]

It should also show:

\[
r=c-ax-by.
\]

**Method reinforced:**  
A slack variable measures unused capacity.

**Errors checked:**

- subtracting the slack variable instead of adding it for a \(\leq\) constraint;
- reusing the same slack variable for two different constraints;
- forgetting \(r\geq0\);
- using a slack variable for the objective row.

## 10.3 Tableau row-operation checker

[INTERACTIVE PLACEHOLDER: FA22SimplexAlgorithmTableauWidget-003 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FA22SimplexAlgorithmTableauWidget-003.html | Purpose: Let students practise one pivot operation at a time.]

**Student inputs:**

- current tableau;
- chosen pivot row;
- chosen pivot column;
- proposed new pivot row;
- proposed updated rows.

**Widget displays:**

- whether the pivot row has been divided correctly;
- whether the pivot column has become one \(1\) and otherwise zeros;
- exact corrected entries if an arithmetic slip is detected.

**Method reinforced:**

\[
R_{\text{new}}=R_{\text{old}}-kR_{\text{pivot}}
\]

or

\[
R_{\text{new}}=R_{\text{old}}+kR_{\text{pivot}}.
\]

**Errors checked:**

- dividing only part of the pivot row;
- changing the wrong basic variable;
- eliminating the pivot column incorrectly;
- decimal rounding where exact fractions should be used.

# 11. Worked Examples

## Worked Example 1: Converting inequalities into equations using slack variables

### Evidence source

Uploaded Decision 1 simplex evidence and teacher transcript.

### On-spec status

Core support skill for `FA22-ALGGRAPH-LO003`.

### Ordinary Maths idea used

An inequality such as

\[
x+3y+5z\leq23
\]

describes a quantity that is at most \(23\).

### Further Maths upgrade

The simplex tableau needs equations, so we introduce a slack variable.

For CCEA core two-variable work, use the same idea with two decision variables.

### Question

Rewrite

\[
4x+3y\leq24
\]

as an equation using a slack variable.

### Step-by-step solution

Because the left-hand side is less than or equal to \(24\), there may be spare capacity.

Let \(r\) be the slack variable.

Add \(r\) to the left-hand side:

\[
4x+3y+r=24.
\]

The slack variable must be non-negative:

\[
r\geq0.
\]

The full non-negativity constraints are:

\[
x,y,r\geq0.
\]

### Why this works

If

\[
4x+3y=20,
\]

then

\[
20+r=24,
\]

so

\[
r=4.
\]

The unused capacity is \(4\).

If

\[
4x+3y=24,
\]

then

\[
24+r=24,
\]

so

\[
r=0.
\]

There is no unused capacity.

### Final exam-style answer

\[
\boxed{4x+3y+r=24,\qquad x,y,r\geq0.}
\]

### Teaching note

Use a new slack variable for each separate inequality. Do not use \(r\) for every row.

---

## Worked Example 2: Graphical meaning of slack variables

### Evidence source

Uploaded Decision 1 simplex evidence on the lines representing slack variables equal to zero.

### On-spec status

Core conceptual support for `FA22-ALGGRAPH-LO003`.

### Ordinary Maths idea used

A line such as

\[
5x+7y=70
\]

is the boundary of the inequality

\[
5x+7y\leq70.
\]

### Further Maths upgrade

The boundary line is also the place where the slack variable is zero.

### Question

Consider

\[
5x+7y+r=70,
\]

\[
10x+3y+s=60,
\]

\[
x,y,r,s\geq0.
\]

Explain what \(r=0\) and \(s=0\) mean.

### Step-by-step solution

Start with the first equation:

\[
5x+7y+r=70.
\]

If

\[
r=0,
\]

then

\[
5x+7y+0=70.
\]

So

\[
5x+7y=70.
\]

Therefore \(r=0\) is the boundary line of the first constraint.

Now use the second equation:

\[
10x+3y+s=60.
\]

If

\[
s=0,
\]

then

\[
10x+3y+0=60.
\]

So

\[
10x+3y=60.
\]

Therefore \(s=0\) is the boundary line of the second constraint.

### Final exam-style answer

\[
\boxed{r=0\text{ means the constraint }5x+7y\leq70\text{ is exactly full.}}
\]

\[
\boxed{s=0\text{ means the constraint }10x+3y\leq60\text{ is exactly full.}}
\]

### Teaching note

At a vertex, two variables are often zero. These might be two decision variables, or one decision variable and one slack variable, or two slack variables.

---

## Worked Example 3: Solving a two-variable problem using a simplex tableau

### Evidence source

Uploaded Decision 1 PDF and teacher transcript. This example matches the two-variable simplex tableau boundary and is therefore core.

### On-spec status

Core example for `FA22-ALGGRAPH-LO003`.

### Ordinary Maths idea used

Graphical linear programming tests vertices.

### Further Maths upgrade

The tableau moves between vertices algebraically.

### Question

Maximise

\[
P=3x+4y
\]

subject to

\[
x+y\leq7,
\]

\[
2x+3y\leq18,
\]

\[
x,y\geq0.
\]

### Step 1: Introduce slack variables

For the first constraint, introduce \(r\):

\[
x+y+r=7.
\]

For the second constraint, introduce \(s\):

\[
2x+3y+s=18.
\]

So

\[
x,y,r,s\geq0.
\]

### Step 2: Write the objective in standard form

\[
P=3x+4y.
\]

Move all terms to one side:

\[
P-3x-4y=0.
\]

### Step 3: Initial tableau

| Basic variable | \(x\) | \(y\) | \(r\) | \(s\) | Value |
|---|---:|---:|---:|---:|---:|
| \(r\) | \(1\) | \(1\) | \(1\) | \(0\) | \(7\) |
| \(s\) | \(2\) | \(3\) | \(0\) | \(1\) | \(18\) |
| \(P\) | \(-3\) | \(-4\) | \(0\) | \(0\) | \(0\) |

The most negative entry in the objective row is

\[
-4.
\]

So the pivot column is the \(y\)-column.

### Step 4: Calculate theta values

For the \(r\)-row:

\[
\theta=\frac{7}{1}=7.
\]

For the \(s\)-row:

\[
\theta=\frac{18}{3}=6.
\]

The smallest positive theta is

\[
6.
\]

So the pivot row is the \(s\)-row.

The pivot is

\[
3.
\]

### Step 5: Divide the pivot row by \(3\)

The \(s\)-row is:

\[
[2,\ 3,\ 0,\ 1,\ 18].
\]

Divide by \(3\):

\[
\left[\frac{2}{3},\ 1,\ 0,\ \frac{1}{3},\ 6\right].
\]

The basic variable \(s\) is replaced by \(y\).

### Step 6: Eliminate \(y\) from other rows

#### Eliminate \(y\) from the \(r\)-row

Use:

\[
R_r\leftarrow R_r-R_y.
\]

Original \(r\)-row:

\[
[1,\ 1,\ 1,\ 0,\ 7].
\]

New \(y\)-row:

\[
\left[\frac{2}{3},\ 1,\ 0,\ \frac{1}{3},\ 6\right].
\]

Subtract:

\[
1-\frac{2}{3}=\frac{1}{3},
\]

\[
1-1=0,
\]

\[
1-0=1,
\]

\[
0-\frac{1}{3}=-\frac{1}{3},
\]

\[
7-6=1.
\]

New \(r\)-row:

\[
\left[\frac{1}{3},\ 0,\ 1,\ -\frac{1}{3},\ 1\right].
\]

#### Eliminate \(y\) from the objective row

Use:

\[
R_P\leftarrow R_P+4R_y.
\]

Original objective row:

\[
[-3,\ -4,\ 0,\ 0,\ 0].
\]

Four times the new \(y\)-row is:

\[
\left[\frac{8}{3},\ 4,\ 0,\ \frac{4}{3},\ 24\right].
\]

Add:

\[
-3+\frac{8}{3}
=
-\frac{9}{3}+\frac{8}{3}
=
-\frac{1}{3},
\]

\[
-4+4=0,
\]

\[
0+0=0,
\]

\[
0+\frac{4}{3}=\frac{4}{3},
\]

\[
0+24=24.
\]

New objective row:

\[
\left[-\frac{1}{3},\ 0,\ 0,\ \frac{4}{3},\ 24\right].
\]

### Step 7: Tableau after first pivot

| Basic variable | \(x\) | \(y\) | \(r\) | \(s\) | Value |
|---|---:|---:|---:|---:|---:|
| \(r\) | \(\frac{1}{3}\) | \(0\) | \(1\) | \(-\frac{1}{3}\) | \(1\) |
| \(y\) | \(\frac{2}{3}\) | \(1\) | \(0\) | \(\frac{1}{3}\) | \(6\) |
| \(P\) | \(-\frac{1}{3}\) | \(0\) | \(0\) | \(\frac{4}{3}\) | \(24\) |

The objective row still has a negative entry:

\[
-\frac{1}{3}.
\]

So pivot again. The pivot column is now the \(x\)-column.

### Step 8: New theta values

For the \(r\)-row:

\[
\theta=\frac{1}{\frac{1}{3}}=3.
\]

For the \(y\)-row:

\[
\theta=\frac{6}{\frac{2}{3}}
=
6\times\frac{3}{2}
=
9.
\]

The smallest positive theta is

\[
3.
\]

So the pivot row is the \(r\)-row.

The pivot is

\[
\frac{1}{3}.
\]

### Step 9: Divide the pivot row by \(\frac{1}{3}\)

The \(r\)-row is:

\[
\left[\frac{1}{3},\ 0,\ 1,\ -\frac{1}{3},\ 1\right].
\]

Divide by \(\frac{1}{3}\), which is the same as multiplying by \(3\):

\[
[1,\ 0,\ 3,\ -1,\ 3].
\]

The basic variable \(r\) is replaced by \(x\).

### Step 10: Eliminate \(x\) from other rows

#### Eliminate \(x\) from the \(y\)-row

Use:

\[
R_y\leftarrow R_y-\frac{2}{3}R_x.
\]

Current \(y\)-row:

\[
\left[\frac{2}{3},\ 1,\ 0,\ \frac{1}{3},\ 6\right].
\]

New \(x\)-row:

\[
[1,\ 0,\ 3,\ -1,\ 3].
\]

Subtract:

\[
\frac{2}{3}-\frac{2}{3}(1)=0,
\]

\[
1-\frac{2}{3}(0)=1,
\]

\[
0-\frac{2}{3}(3)=-2,
\]

\[
\frac{1}{3}-\frac{2}{3}(-1)
=
\frac{1}{3}+\frac{2}{3}
=
1,
\]

\[
6-\frac{2}{3}(3)=6-2=4.
\]

New \(y\)-row:

\[
[0,\ 1,\ -2,\ 1,\ 4].
\]

#### Eliminate \(x\) from the objective row

Use:

\[
R_P\leftarrow R_P+\frac{1}{3}R_x.
\]

Current objective row:

\[
\left[-\frac{1}{3},\ 0,\ 0,\ \frac{4}{3},\ 24\right].
\]

One third of the new \(x\)-row is:

\[
\left[\frac{1}{3},\ 0,\ 1,\ -\frac{1}{3},\ 1\right].
\]

Add:

\[
-\frac{1}{3}+\frac{1}{3}=0,
\]

\[
0+0=0,
\]

\[
0+1=1,
\]

\[
\frac{4}{3}-\frac{1}{3}=1,
\]

\[
24+1=25.
\]

New objective row:

\[
[0,\ 0,\ 1,\ 1,\ 25].
\]

### Step 11: Final tableau

| Basic variable | \(x\) | \(y\) | \(r\) | \(s\) | Value |
|---|---:|---:|---:|---:|---:|
| \(x\) | \(1\) | \(0\) | \(3\) | \(-1\) | \(3\) |
| \(y\) | \(0\) | \(1\) | \(-2\) | \(1\) | \(4\) |
| \(P\) | \(0\) | \(0\) | \(1\) | \(1\) | \(25\) |

There are no negative entries in the objective row.

So the tableau is optimal.

Read the solution:

\[
x=3,
\]

\[
y=4,
\]

\[
P=25.
\]

The non-basic variables are:

\[
r=0,\qquad s=0.
\]

### Final exam-style answer

\[
\boxed{P_{\max}=25\text{ when }x=3,\ y=4.}
\]

### Check

Original constraints:

\[
x+y=3+4=7,
\]

\[
2x+3y=2(3)+3(4)=6+12=18.
\]

Objective:

\[
P=3x+4y=3(3)+4(4)=9+16=25.
\]

### Teaching note

Because \(r=0\) and \(s=0\), both constraints are exactly at capacity.

# 12. Common Mistakes and Exam Traps

## 12.1 Defining variables too vaguely

Weak:

\[
x=\text{chairs},\qquad y=\text{tables}.
\]

Better:

\[
x=\text{the number of chairs produced per day},
\]

\[
y=\text{the number of tables produced per day}.
\]

The transcript evidence warns that mark schemes can be fussy about how constraints and variables are defined.

## 12.2 Forgetting non-negativity constraints

Always include:

\[
x\geq0,\qquad y\geq0.
\]

After adding slack variables, include:

\[
x,y,r,s\geq0.
\]

## 12.3 Using the same slack variable twice

Wrong:

\[
5x+7y+r=70,
\]

\[
10x+3y+r=60.
\]

Correct:

\[
5x+7y+r=70,
\]

\[
10x+3y+s=60.
\]

Each constraint gets its own slack variable.

## 12.4 Putting the objective row in the wrong form

If

\[
P=3x+4y,
\]

then the objective row should come from:

\[
P-3x-4y=0.
\]

So the entries under \(x\) and \(y\) are:

\[
-3,\quad -4.
\]

Do not write the bottom row as \(3,4,0,0,0\) unless a specific alternative tableau convention is being used and clearly explained.

## 12.5 Choosing the wrong pivot column

For a maximisation tableau in this convention, choose the **most negative** entry in the objective row.

If the objective row is:

\[
-3,\quad -4,\quad 0,\quad 0,
\]

then choose \(-4\), not \(-3\).

The pivot column is the \(y\)-column.

## 12.6 Calculating theta using the wrong entries

The rule is:

\[
\theta=\frac{\text{value entry}}{\text{pivot-column entry}}.
\]

Do not divide the pivot-column entry by the value.

Wrong:

\[
\theta=\frac{5}{70}.
\]

Correct:

\[
\theta=\frac{70}{5}.
\]

## 12.7 Using zero or negative pivot-column entries for theta

Only use rows where the pivot-column entry is positive.

If a pivot-column entry is \(0\), it cannot limit movement in that direction.

If a pivot-column entry is negative, it is not used for the smallest positive theta test.

## 12.8 Choosing the largest theta

The pivot row is chosen using the smallest positive theta.

The smallest positive theta tells you which constraint is reached first.

## 12.9 Dividing only part of the pivot row

If the pivot is \(3\), divide the entire pivot row by \(3\).

Wrong:

\[
[2,\ 3,\ 0,\ 1,\ 18]\rightarrow[2,\ 1,\ 0,\ 1,\ 18].
\]

Correct:

\[
[2,\ 3,\ 0,\ 1,\ 18]\rightarrow
\left[\frac{2}{3},\ 1,\ 0,\ \frac{1}{3},\ 6\right].
\]

## 12.10 Forgetting to change the basic variable

If the pivot column is \(y\) and the pivot row is currently \(s\), then \(y\) enters the basis and \(s\) leaves.

So the row label changes from \(s\) to \(y\).

## 12.11 Stopping too early

You stop only when the objective row has no negative entries.

If the objective row still contains

\[
-\frac{1}{3},
\]

then another pivot is needed.

## 12.12 Reading non-basic variables incorrectly

Variables not in the basic-variable column are zero.

If the final basic variables are

\[
x,\quad y,\quad P,
\]

then

\[
r=0,\qquad s=0.
\]

## 12.13 Rounding fractions too early

Keep exact fractions.

Use:

\[
\frac{80}{11}
\]

rather than

\[
7.27.
\]

Only use decimals if the question asks for decimals or a contextual interpretation requires rounding.

## 12.14 Confusing the graph with the tableau

The graph helps explain the method, but the simplex tableau is the required algorithmic method here.

You should understand both:

\[
\text{graph vertex movement}
\]

and

\[
\text{tableau pivoting}.
\]

# 13. Practice Questions

These are AI-generated on-spec practice questions. They are not past-paper or textbook questions.

## Question 1: Basic slack-variable fluency

Rewrite each inequality as an equation using a slack variable.

(a)

\[
4x+3y\leq24.
\]

(b)

\[
2x+5y\leq30.
\]

State the non-negativity constraints.

## Question 2: Bridge question

For the constraint

\[
6x+2y+r=36,
\]

explain what \(r=0\) means graphically and contextually.

## Question 3: Standard tableau question

Maximise

\[
P=5x+2y
\]

subject to

\[
2x+y\leq18,
\]

\[
x+2y\leq16,
\]

\[
x,y\geq0.
\]

Use a simplex tableau.

## Question 4: Full two-pivot tableau question

Maximise

\[
P=5x+4y
\]

subject to

\[
2x+y\leq16,
\]

\[
x+2y\leq14,
\]

\[
x,y\geq0.
\]

Use a simplex tableau.

## Question 5: Context and interpretation

A small workshop makes two products, \(A\) and \(B\).

Let

\[
x=\text{the number of units of product A made per day},
\]

\[
y=\text{the number of units of product B made per day}.
\]

The profit is

\[
P=4x+3y.
\]

Machine time gives the constraint

\[
2x+y\leq40.
\]

Labour time gives the constraint

\[
x+2y\leq50.
\]

Also,

\[
x,y\geq0.
\]

Use a simplex tableau to find the maximum profit and interpret the slack variables in your final answer.

# 14. Worked Solutions

## Solution 1

### Part (a)

Given:

\[
4x+3y\leq24.
\]

Introduce slack variable \(r\geq0\):

\[
4x+3y+r=24.
\]

### Part (b)

Given:

\[
2x+5y\leq30.
\]

Introduce slack variable \(s\geq0\):

\[
2x+5y+s=30.
\]

### Non-negativity constraints

\[
x,y,r,s\geq0.
\]

### Final answer

\[
\boxed{4x+3y+r=24,}
\]

\[
\boxed{2x+5y+s=30,}
\]

\[
\boxed{x,y,r,s\geq0.}
\]

---

## Solution 2

Given:

\[
6x+2y+r=36.
\]

If

\[
r=0,
\]

then

\[
6x+2y+0=36.
\]

So

\[
6x+2y=36.
\]

Graphically, \(r=0\) is the boundary line of the constraint

\[
6x+2y\leq36.
\]

Contextually, \(r=0\) means there is no spare capacity left in that constraint.

If \(6x+2y\) represents resource use and \(36\) represents the total available resource, then

\[
r=0
\]

means the full resource has been used.

### Final answer

\[
\boxed{r=0\text{ means }6x+2y=36,\text{ so the constraint is exactly at capacity.}}
\]

---

## Solution 3

Maximise

\[
P=5x+2y
\]

subject to

\[
2x+y\leq18,
\]

\[
x+2y\leq16,
\]

\[
x,y\geq0.
\]

### Step 1: Add slack variables

\[
2x+y+r=18,
\]

\[
x+2y+s=16,
\]

\[
x,y,r,s\geq0.
\]

### Step 2: Objective in standard form

\[
P=5x+2y.
\]

So

\[
P-5x-2y=0.
\]

### Step 3: Initial tableau

| Basic variable | \(x\) | \(y\) | \(r\) | \(s\) | Value |
|---|---:|---:|---:|---:|---:|
| \(r\) | \(2\) | \(1\) | \(1\) | \(0\) | \(18\) |
| \(s\) | \(1\) | \(2\) | \(0\) | \(1\) | \(16\) |
| \(P\) | \(-5\) | \(-2\) | \(0\) | \(0\) | \(0\) |

Most negative objective-row entry:

\[
-5.
\]

So the pivot column is the \(x\)-column.

### Step 4: Theta values

For the \(r\)-row:

\[
\theta=\frac{18}{2}=9.
\]

For the \(s\)-row:

\[
\theta=\frac{16}{1}=16.
\]

Smallest positive theta:

\[
9.
\]

So the pivot row is the \(r\)-row.

Pivot:

\[
2.
\]

### Step 5: Divide pivot row by \(2\)

\[
[2,\ 1,\ 1,\ 0,\ 18]\div2
=
\left[1,\ \frac{1}{2},\ \frac{1}{2},\ 0,\ 9\right].
\]

The basic variable \(r\) is replaced by \(x\).

### Step 6: Eliminate \(x\) from other rows

#### New \(x\)-row

\[
\left[1,\ \frac{1}{2},\ \frac{1}{2},\ 0,\ 9\right].
\]

#### Update \(s\)-row

Use:

\[
R_s\leftarrow R_s-R_x.
\]

\[
[1,\ 2,\ 0,\ 1,\ 16]
-
\left[1,\ \frac{1}{2},\ \frac{1}{2},\ 0,\ 9\right]
=
\left[0,\ \frac{3}{2},\ -\frac{1}{2},\ 1,\ 7\right].
\]

#### Update objective row

Use:

\[
R_P\leftarrow R_P+5R_x.
\]

\[
[-5,\ -2,\ 0,\ 0,\ 0]
+
5\left[1,\ \frac{1}{2},\ \frac{1}{2},\ 0,\ 9\right]
\]

\[
=
[-5,\ -2,\ 0,\ 0,\ 0]
+
\left[5,\ \frac{5}{2},\ \frac{5}{2},\ 0,\ 45\right].
\]

So

\[
R_P=
\left[0,\ \frac{1}{2},\ \frac{5}{2},\ 0,\ 45\right].
\]

### Step 7: New tableau

| Basic variable | \(x\) | \(y\) | \(r\) | \(s\) | Value |
|---|---:|---:|---:|---:|---:|
| \(x\) | \(1\) | \(\frac{1}{2}\) | \(\frac{1}{2}\) | \(0\) | \(9\) |
| \(s\) | \(0\) | \(\frac{3}{2}\) | \(-\frac{1}{2}\) | \(1\) | \(7\) |
| \(P\) | \(0\) | \(\frac{1}{2}\) | \(\frac{5}{2}\) | \(0\) | \(45\) |

The objective row has no negative entries.

So the tableau is optimal.

Read the solution:

\[
x=9,
\]

\[
s=7,
\]

\[
P=45.
\]

The non-basic variables are:

\[
y=0,\qquad r=0.
\]

### Final answer

\[
\boxed{P_{\max}=45\text{ when }x=9,\ y=0.}
\]

### Check

\[
2x+y=2(9)+0=18,
\]

so the first constraint is full and

\[
r=0.
\]

\[
x+2y=9+0=9.
\]

The second constraint has capacity \(16\), so

\[
s=16-9=7.
\]

Objective:

\[
P=5(9)+2(0)=45.
\]

---

## Solution 4

Maximise

\[
P=5x+4y
\]

subject to

\[
2x+y\leq16,
\]

\[
x+2y\leq14,
\]

\[
x,y\geq0.
\]

### Step 1: Add slack variables

\[
2x+y+r=16,
\]

\[
x+2y+s=14,
\]

\[
x,y,r,s\geq0.
\]

### Step 2: Objective in standard form

\[
P=5x+4y
\]

so

\[
P-5x-4y=0.
\]

### Step 3: Initial tableau

| Basic variable | \(x\) | \(y\) | \(r\) | \(s\) | Value |
|---|---:|---:|---:|---:|---:|
| \(r\) | \(2\) | \(1\) | \(1\) | \(0\) | \(16\) |
| \(s\) | \(1\) | \(2\) | \(0\) | \(1\) | \(14\) |
| \(P\) | \(-5\) | \(-4\) | \(0\) | \(0\) | \(0\) |

Most negative objective-row entry:

\[
-5.
\]

Pivot column: \(x\).

### Step 4: Theta values

For the \(r\)-row:

\[
\theta=\frac{16}{2}=8.
\]

For the \(s\)-row:

\[
\theta=\frac{14}{1}=14.
\]

Smallest positive theta:

\[
8.
\]

Pivot row: \(r\)-row.

Pivot:

\[
2.
\]

### Step 5: Divide pivot row by \(2\)

\[
[2,\ 1,\ 1,\ 0,\ 16]\div2
=
\left[1,\ \frac{1}{2},\ \frac{1}{2},\ 0,\ 8\right].
\]

The basic variable \(r\) is replaced by \(x\).

### Step 6: Eliminate \(x\)

#### New \(x\)-row

\[
\left[1,\ \frac{1}{2},\ \frac{1}{2},\ 0,\ 8\right].
\]

#### Update \(s\)-row

Use:

\[
R_s\leftarrow R_s-R_x.
\]

\[
[1,\ 2,\ 0,\ 1,\ 14]
-
\left[1,\ \frac{1}{2},\ \frac{1}{2},\ 0,\ 8\right]
=
\left[0,\ \frac{3}{2},\ -\frac{1}{2},\ 1,\ 6\right].
\]

#### Update objective row

Use:

\[
R_P\leftarrow R_P+5R_x.
\]

\[
[-5,\ -4,\ 0,\ 0,\ 0]
+
5\left[1,\ \frac{1}{2},\ \frac{1}{2},\ 0,\ 8\right]
\]

\[
=
[-5,\ -4,\ 0,\ 0,\ 0]
+
\left[5,\ \frac{5}{2},\ \frac{5}{2},\ 0,\ 40\right].
\]

So

\[
R_P=
\left[0,\ -\frac{3}{2},\ \frac{5}{2},\ 0,\ 40\right].
\]

### Step 7: Tableau after first pivot

| Basic variable | \(x\) | \(y\) | \(r\) | \(s\) | Value |
|---|---:|---:|---:|---:|---:|
| \(x\) | \(1\) | \(\frac{1}{2}\) | \(\frac{1}{2}\) | \(0\) | \(8\) |
| \(s\) | \(0\) | \(\frac{3}{2}\) | \(-\frac{1}{2}\) | \(1\) | \(6\) |
| \(P\) | \(0\) | \(-\frac{3}{2}\) | \(\frac{5}{2}\) | \(0\) | \(40\) |

There is still a negative entry in the objective row:

\[
-\frac{3}{2}.
\]

Pivot column: \(y\).

### Step 8: Theta values

For the \(x\)-row:

\[
\theta=\frac{8}{\frac{1}{2}}
=
8\times2
=
16.
\]

For the \(s\)-row:

\[
\theta=\frac{6}{\frac{3}{2}}
=
6\times\frac{2}{3}
=
4.
\]

Smallest positive theta:

\[
4.
\]

Pivot row: \(s\)-row.

Pivot:

\[
\frac{3}{2}.
\]

### Step 9: Divide pivot row by \(\frac{3}{2}\)

The \(s\)-row is:

\[
\left[0,\ \frac{3}{2},\ -\frac{1}{2},\ 1,\ 6\right].
\]

Divide by \(\frac{3}{2}\), which is the same as multiplying by \(\frac{2}{3}\):

\[
0\times\frac{2}{3}=0,
\]

\[
\frac{3}{2}\times\frac{2}{3}=1,
\]

\[
-\frac{1}{2}\times\frac{2}{3}=-\frac{1}{3},
\]

\[
1\times\frac{2}{3}=\frac{2}{3},
\]

\[
6\times\frac{2}{3}=4.
\]

New \(y\)-row:

\[
\left[0,\ 1,\ -\frac{1}{3},\ \frac{2}{3},\ 4\right].
\]

The basic variable \(s\) is replaced by \(y\).

### Step 10: Eliminate \(y\)

#### Update \(x\)-row

Use:

\[
R_x\leftarrow R_x-\frac{1}{2}R_y.
\]

Current \(x\)-row:

\[
\left[1,\ \frac{1}{2},\ \frac{1}{2},\ 0,\ 8\right].
\]

Half of new \(y\)-row:

\[
\frac{1}{2}
\left[0,\ 1,\ -\frac{1}{3},\ \frac{2}{3},\ 4\right]
=
\left[0,\ \frac{1}{2},\ -\frac{1}{6},\ \frac{1}{3},\ 2\right].
\]

Subtract:

\[
\left[1,\ \frac{1}{2},\ \frac{1}{2},\ 0,\ 8\right]
-
\left[0,\ \frac{1}{2},\ -\frac{1}{6},\ \frac{1}{3},\ 2\right]
\]

\[
=
\left[1,\ 0,\ \frac{1}{2}+\frac{1}{6},\ -\frac{1}{3},\ 6\right].
\]

Now

\[
\frac{1}{2}+\frac{1}{6}
=
\frac{3}{6}+\frac{1}{6}
=
\frac{4}{6}
=
\frac{2}{3}.
\]

So

\[
R_x=
\left[1,\ 0,\ \frac{2}{3},\ -\frac{1}{3},\ 6\right].
\]

#### Update objective row

Use:

\[
R_P\leftarrow R_P+\frac{3}{2}R_y.
\]

Current objective row:

\[
\left[0,\ -\frac{3}{2},\ \frac{5}{2},\ 0,\ 40\right].
\]

Now

\[
\frac{3}{2}R_y
=
\frac{3}{2}
\left[0,\ 1,\ -\frac{1}{3},\ \frac{2}{3},\ 4\right].
\]

Calculate:

\[
0,
\]

\[
\frac{3}{2},
\]

\[
\frac{3}{2}\left(-\frac{1}{3}\right)=-\frac{1}{2},
\]

\[
\frac{3}{2}\left(\frac{2}{3}\right)=1,
\]

\[
\frac{3}{2}(4)=6.
\]

So

\[
\frac{3}{2}R_y
=
\left[0,\ \frac{3}{2},\ -\frac{1}{2},\ 1,\ 6\right].
\]

Add:

\[
\left[0,\ -\frac{3}{2},\ \frac{5}{2},\ 0,\ 40\right]
+
\left[0,\ \frac{3}{2},\ -\frac{1}{2},\ 1,\ 6\right]
\]

\[
=
[0,\ 0,\ 2,\ 1,\ 46].
\]

### Step 11: Final tableau

| Basic variable | \(x\) | \(y\) | \(r\) | \(s\) | Value |
|---|---:|---:|---:|---:|---:|
| \(x\) | \(1\) | \(0\) | \(\frac{2}{3}\) | \(-\frac{1}{3}\) | \(6\) |
| \(y\) | \(0\) | \(1\) | \(-\frac{1}{3}\) | \(\frac{2}{3}\) | \(4\) |
| \(P\) | \(0\) | \(0\) | \(2\) | \(1\) | \(46\) |

There are no negative entries in the objective row.

So the tableau is optimal.

Read:

\[
x=6,\qquad y=4,\qquad P=46.
\]

The non-basic variables are:

\[
r=0,\qquad s=0.
\]

### Final answer

\[
\boxed{P_{\max}=46\text{ when }x=6,\ y=4.}
\]

### Check

\[
2x+y=2(6)+4=12+4=16,
\]

\[
x+2y=6+2(4)=6+8=14,
\]

\[
P=5(6)+4(4)=30+16=46.
\]

---

## Solution 5

A small workshop makes two products, \(A\) and \(B\).

\[
x=\text{the number of units of product A made per day},
\]

\[
y=\text{the number of units of product B made per day}.
\]

Profit:

\[
P=4x+3y.
\]

Constraints:

\[
2x+y\leq40,
\]

\[
x+2y\leq50,
\]

\[
x,y\geq0.
\]

### Step 1: Add slack variables

Let \(r\) be the unused machine-time capacity.

\[
2x+y+r=40.
\]

Let \(s\) be the unused labour-time capacity.

\[
x+2y+s=50.
\]

So

\[
x,y,r,s\geq0.
\]

### Step 2: Objective in standard form

\[
P=4x+3y.
\]

So

\[
P-4x-3y=0.
\]

### Step 3: Initial tableau

| Basic variable | \(x\) | \(y\) | \(r\) | \(s\) | Value |
|---|---:|---:|---:|---:|---:|
| \(r\) | \(2\) | \(1\) | \(1\) | \(0\) | \(40\) |
| \(s\) | \(1\) | \(2\) | \(0\) | \(1\) | \(50\) |
| \(P\) | \(-4\) | \(-3\) | \(0\) | \(0\) | \(0\) |

Most negative objective-row entry:

\[
-4.
\]

Pivot column: \(x\).

### Step 4: Theta values

For the \(r\)-row:

\[
\theta=\frac{40}{2}=20.
\]

For the \(s\)-row:

\[
\theta=\frac{50}{1}=50.
\]

Smallest positive theta:

\[
20.
\]

Pivot row: \(r\)-row.

Pivot:

\[
2.
\]

### Step 5: Divide pivot row by \(2\)

\[
[2,\ 1,\ 1,\ 0,\ 40]\div2
=
\left[1,\ \frac{1}{2},\ \frac{1}{2},\ 0,\ 20\right].
\]

The basic variable \(r\) is replaced by \(x\).

### Step 6: Eliminate \(x\)

#### New \(x\)-row

\[
\left[1,\ \frac{1}{2},\ \frac{1}{2},\ 0,\ 20\right].
\]

#### Update \(s\)-row

Use:

\[
R_s\leftarrow R_s-R_x.
\]

\[
[1,\ 2,\ 0,\ 1,\ 50]
-
\left[1,\ \frac{1}{2},\ \frac{1}{2},\ 0,\ 20\right]
=
\left[0,\ \frac{3}{2},\ -\frac{1}{2},\ 1,\ 30\right].
\]

#### Update objective row

Use:

\[
R_P\leftarrow R_P+4R_x.
\]

\[
[-4,\ -3,\ 0,\ 0,\ 0]
+
4\left[1,\ \frac{1}{2},\ \frac{1}{2},\ 0,\ 20\right]
\]

\[
=
[-4,\ -3,\ 0,\ 0,\ 0]
+
[4,\ 2,\ 2,\ 0,\ 80].
\]

So

\[
R_P=[0,\ -1,\ 2,\ 0,\ 80].
\]

### Step 7: Tableau after first pivot

| Basic variable | \(x\) | \(y\) | \(r\) | \(s\) | Value |
|---|---:|---:|---:|---:|---:|
| \(x\) | \(1\) | \(\frac{1}{2}\) | \(\frac{1}{2}\) | \(0\) | \(20\) |
| \(s\) | \(0\) | \(\frac{3}{2}\) | \(-\frac{1}{2}\) | \(1\) | \(30\) |
| \(P\) | \(0\) | \(-1\) | \(2\) | \(0\) | \(80\) |

There is a negative entry in the objective row:

\[
-1.
\]

Pivot column: \(y\).

### Step 8: Theta values

For the \(x\)-row:

\[
\theta=\frac{20}{\frac{1}{2}}=40.
\]

For the \(s\)-row:

\[
\theta=\frac{30}{\frac{3}{2}}
=
30\times\frac{2}{3}
=
20.
\]

Smallest positive theta:

\[
20.
\]

Pivot row: \(s\)-row.

Pivot:

\[
\frac{3}{2}.
\]

### Step 9: Divide pivot row by \(\frac{3}{2}\)

\[
\left[0,\ \frac{3}{2},\ -\frac{1}{2},\ 1,\ 30\right]
\div
\frac{3}{2}.
\]

This is the same as multiplying by \(\frac{2}{3}\):

\[
0,
\]

\[
1,
\]

\[
-\frac{1}{2}\times\frac{2}{3}=-\frac{1}{3},
\]

\[
1\times\frac{2}{3}=\frac{2}{3},
\]

\[
30\times\frac{2}{3}=20.
\]

New \(y\)-row:

\[
\left[0,\ 1,\ -\frac{1}{3},\ \frac{2}{3},\ 20\right].
\]

The basic variable \(s\) is replaced by \(y\).

### Step 10: Eliminate \(y\)

#### Update \(x\)-row

Use:

\[
R_x\leftarrow R_x-\frac{1}{2}R_y.
\]

\[
\left[1,\ \frac{1}{2},\ \frac{1}{2},\ 0,\ 20\right]
-
\frac{1}{2}
\left[0,\ 1,\ -\frac{1}{3},\ \frac{2}{3},\ 20\right].
\]

Now

\[
\frac{1}{2}R_y
=
\left[0,\ \frac{1}{2},\ -\frac{1}{6},\ \frac{1}{3},\ 10\right].
\]

So

\[
R_x=
\left[1,\ 0,\ \frac{1}{2}+\frac{1}{6},\ -\frac{1}{3},\ 10\right].
\]

\[
\frac{1}{2}+\frac{1}{6}
=
\frac{3}{6}+\frac{1}{6}
=
\frac{4}{6}
=
\frac{2}{3}.
\]

So

\[
R_x=
\left[1,\ 0,\ \frac{2}{3},\ -\frac{1}{3},\ 10\right].
\]

#### Update objective row

Use:

\[
R_P\leftarrow R_P+R_y.
\]

\[
[0,\ -1,\ 2,\ 0,\ 80]
+
\left[0,\ 1,\ -\frac{1}{3},\ \frac{2}{3},\ 20\right]
\]

\[
=
\left[0,\ 0,\ \frac{5}{3},\ \frac{2}{3},\ 100\right].
\]

### Step 11: Final tableau

| Basic variable | \(x\) | \(y\) | \(r\) | \(s\) | Value |
|---|---:|---:|---:|---:|---:|
| \(x\) | \(1\) | \(0\) | \(\frac{2}{3}\) | \(-\frac{1}{3}\) | \(10\) |
| \(y\) | \(0\) | \(1\) | \(-\frac{1}{3}\) | \(\frac{2}{3}\) | \(20\) |
| \(P\) | \(0\) | \(0\) | \(\frac{5}{3}\) | \(\frac{2}{3}\) | \(100\) |

No negative entries remain in the objective row.

So the tableau is optimal.

Read:

\[
x=10,
\]

\[
y=20,
\]

\[
P=100.
\]

The non-basic variables are:

\[
r=0,\qquad s=0.
\]

### Interpretation

The workshop should make:

\[
\boxed{10\text{ units of product A per day}}
\]

and

\[
\boxed{20\text{ units of product B per day}}.
\]

The maximum profit is:

\[
\boxed{100}.
\]

Because

\[
r=0,\qquad s=0,
\]

both constraints are exactly at capacity.

Machine time check:

\[
2x+y=2(10)+20=40.
\]

Labour time check:

\[
x+2y=10+2(20)=50.
\]

So both machine time and labour time are fully used.

# 15. Exam Technique Notes

## 15.1 Always define the variables in context

A full variable definition should say what the variable counts or measures.

Good:

\[
x=\text{the number of units of product A made per day}.
\]

Weak:

\[
x=A.
\]

## 15.2 Write the objective function separately

Example:

\[
\text{Maximise }P=4x+3y.
\]

Do not bury the objective function among the constraints.

## 15.3 Include every constraint

A full linear programming formulation usually needs:

- resource constraints;
- non-negativity constraints;
- any extra contextual constraints.

For the CCEA simplex tableau core, the constraints should be two-variable linear constraints suitable for tableau work.

## 15.4 Add slack variables carefully

For

\[
ax+by\leq c,
\]

write

\[
ax+by+r=c.
\]

Use a different slack variable for each constraint.

## 15.5 Keep the objective row convention consistent

This lesson uses:

\[
P=ax+by
\]

becomes

\[
P-ax-by=0.
\]

So the objective row has entries:

\[
-a,\quad -b.
\]

## 15.6 Pivot-column selection

For maximisation using this convention:

\[
\boxed{\text{Choose the most negative entry in the objective row.}}
\]

If no negative entries remain, the tableau is optimal.

## 15.7 Pivot-row selection

Use:

\[
\theta=\frac{\text{value}}{\text{positive pivot-column entry}}.
\]

Choose the smallest positive \(\theta\).

Do not use rows with zero or negative pivot-column entries.

## 15.8 Show row operations

Write row operations clearly, for example:

\[
R_s\leftarrow R_s-R_x,
\]

\[
R_P\leftarrow R_P+5R_x.
\]

This helps the marker follow your arithmetic.

## 15.9 Read the final tableau correctly

If the final tableau has basic variables

\[
x,\quad y,\quad P,
\]

then read their values from the value column.

If \(r\) and \(s\) are not basic variables, then

\[
r=0,\qquad s=0.
\]

## 15.10 Interpret final answers

Do not finish with just:

\[
x=10,\quad y=20,\quad P=100.
\]

Write a sentence:

The maximum profit is \(100\), achieved by making \(10\) units of product \(A\) and \(20\) units of product \(B\) per day.

## 15.11 Exact values versus decimals

Use exact fractions unless the context demands rounding.

For example, write:

\[
x=\frac{42}{11},\qquad y=\frac{80}{11}.
\]

Only round if the problem asks for a practical integer interpretation, and do not assume integer solutions are part of the simplex method unless the question explicitly asks for that. Integer simplex is not core in this lesson.

# 16. Syllabus Gap Check

## 16.1 LO coverage table

| LO ID | Requirement | Covered? | Where covered |
|---|---|---:|---|
| FA22-ALGGRAPH-LO003 | Use the simplex algorithm | Yes | Sections 6, 8, 11, 14 |
| FA22-ALGGRAPH-LO003 | Use tableau | Yes | Sections 8, 11, 14 |
| FA22-ALGGRAPH-LO003 | Solve two-variable LP problems | Yes | Sections 8, 11, 13, 14 |
| FA22-ALGGRAPH-LO003 | Interpret optimal solution | Yes | Sections 8, 11, 14, 15 |

## 16.2 Evidence coverage table

| Evidence item | Used? | Notes |
|---|---:|---|
| CCEA Further Maths specification map | Yes | Sets the official boundary. |
| Further Maths module map | Yes | Confirms applied section and topic grouping. |
| Evidence checklist | Yes | Used for evidence-status awareness. |
| Decision 1 PDF | Yes | Used for simplex tableau method, slack variables, pivoting and examples. |
| Screenshot PDF | Partially | Used only where visible/readable. |
| Transcript | Yes | Used for conceptual warnings and teacher phrasing. |
| Ordinary A-Level Maths bridge extracts | Yes | Bridge only. |
| Cross-board or internet sources | No | Not needed for core lesson. |

## 16.3 Bridge coverage table

| Bridge concept | Covered? | Lesson location |
|---|---:|---|
| Inequalities as constraints | Yes | Sections 5, 6, 7, 8 |
| Graphical feasible regions | Yes | Sections 5, 6, 8, 9 |
| Vertices and optimisation | Yes | Sections 6, 8, 11 |
| Simultaneous-equation elimination | Yes | Sections 8, 11, 14 |
| Algebraic interpretation of row operations | Yes | Sections 8, 11, 15 |

## 16.4 Off-Spec Content Found but Excluded

The uploaded Decision 1 evidence contains material that goes beyond the CCEA `FA22-ALGGRAPH-LO003` boundary.

Excluded from core:

- simplex with three or more decision variables;
- four-variable formulation examples;
- integer solutions;
- two-stage simplex method;
- Big-M method;
- artificial variables;
- general \(n\)-variable simplex.

Reason for exclusion:

\[
\text{The CCEA LO specifies two-variable linear programming problems.}
\]

## 16.5 Optional Enrichment Not Required by CCEA

The following could be useful enrichment later, but is not required here:

- why simplex generalises beyond graphs;
- three-dimensional feasible polyhedra;
- full \(n\)-variable simplex;
- integer programming;
- two-stage simplex;
- Big-M method;
- artificial variables.

## 16.6 Weak evidence warnings

| Issue | Warning |
|---|---|
| Screenshot PDF is image-only | Only visible/readable screenshot details are used. |
| Uploaded Decision 1 evidence is not CCEA-specific | It is used only where it supports the CCEA two-variable simplex tableau LO. |
| No CCEA mark scheme supplied | Exam notes are method-based, not claimed as exact CCEA mark-scheme wording. |
| Some uploaded examples use more than two variables | These are excluded from core. |

## 16.7 Missing evidence log

| Missing item | Impact |
|---|---|
| CCEA past-paper examples for this exact LO | Generated practice is not labelled as past-paper. |
| Topic-specific CCEA mark scheme | No exact CCEA mark allocation is claimed. |
| Complete inspectable screenshot text | Visual evidence limitations are logged. |

# 17. Recommended Enhancements Not in the Evidence

These are AI-proposed teaching enhancements. They are not claimed as evidence-backed content.

## 17.1 Additional diagrams

1. A clean graph showing:
   \[
   r=0
   \]
   on one boundary and
   \[
   s=0
   \]
   on another boundary.

2. A “vertex passport” diagram showing which variables are zero at each vertex.

3. A tableau heatmap showing:
   - pivot column;
   - theta column;
   - pivot row;
   - pivot element.

## 17.2 Additional animations

1. Animated movement:
   \[
   (0,0)\rightarrow(6,0)\rightarrow\left(\frac{42}{11},\frac{80}{11}\right).
   \]

2. Animated row operation:
   - divide pivot row;
   - eliminate entries above and below pivot;
   - update basic-variable column.

## 17.3 Additional widgets

1. Pivot-column trainer.
2. Theta-value trainer.
3. Slack-variable meaning checker.
4. Final-tableau reader.
5. “Spot the invalid tableau step” diagnostic.

## 17.4 Extra examples

Useful extra example types:

- a one-pivot problem;
- a two-pivot problem;
- a problem where the optimum lies on an axis;
- a contextual problem requiring interpretation of zero and non-zero slack;
- a final-tableau reading question.

## 17.5 Bridge visuals

Recommended bridge visual:

\[
\text{ordinary graph method}\rightarrow\text{simplex tableau method}.
\]

The visual should make clear:

\[
\text{the tableau does not replace vertices; it navigates them algebraically.}
\]

# 18. Supplementary Sources Used

## 18.1 Project Sources

- `CCEA_GCE_Further_Mathematics_Specification_Map.md`
- `Further_Maths_README_module_map.md`
- `Further_Maths_EVIDENCE_DROP_CHECKLIST.md`
- `Ordinary_A_Level_Maths_Bridge_Spec_Extracts.md`
- `CCEA_GCE_Mathematics_Specification_Map.md`

## 18.2 Lesson-specific sources

- `Decision Maths 1 chapter 7 Simplex Algorithm updated may 22B.pdf`
- `Chapter_7_Simplex_Algorithm_💻_(Decision_1)_screenshots.pdf`
- `transcripts.md`

## 18.3 Ordinary A-Level Maths bridge sources

Ordinary Mathematics sources were used only for bridge context:

- inequalities;
- simultaneous equations;
- straight-line graph interpretation;
- optimisation language;
- feasible regions.

They do not override the Further Mathematics specification.

## 18.4 Cross-board source notes

The uploaded Decision 1 material appears to follow a broader Decision Mathematics route than the CCEA two-variable simplex tableau boundary.

Therefore, only the parts that match the CCEA LO are used as core.

## 18.5 Evidence boundary statement

The controlling authority is:

\[
\boxed{\text{FA22-ALGGRAPH-LO003: Use the simplex algorithm and tableau to solve two-variable linear programming problems.}}
\]

Everything outside that boundary is either excluded or marked as optional enrichment.

# 19. Final Student Checklist

## 19.1 Prerequisite confidence checklist

Before attempting exam questions, check that you can:

- [ ] solve simultaneous linear equations;
- [ ] rearrange formulae accurately;
- [ ] work with inequalities;
- [ ] understand a feasible region;
- [ ] identify a vertex of a feasible region;
- [ ] use exact fractions without rounding too early.

## 19.2 Further Maths method checklist

You should be able to:

- [ ] define \(x\) and \(y\) clearly in context;
- [ ] write the objective function;
- [ ] write all constraints;
- [ ] add a separate slack variable for each \(\leq\) constraint;
- [ ] write the objective in standard form;
- [ ] build the initial tableau;
- [ ] identify the most negative objective-row entry;
- [ ] choose the pivot column;
- [ ] calculate valid \(\theta\) values;
- [ ] choose the smallest positive \(\theta\);
- [ ] identify the pivot row;
- [ ] identify the pivot;
- [ ] divide the whole pivot row by the pivot;
- [ ] change the basic variable correctly;
- [ ] eliminate the pivot-column entries in the other rows;
- [ ] repeat until no negative objective-row entries remain;
- [ ] read the final values from the value column;
- [ ] set non-basic variables equal to zero.

## 19.3 Exam technique checklist

Before finishing a solution, ask:

- [ ] Have I included \(x,y\geq0\)?
- [ ] Have I included slack-variable non-negativity?
- [ ] Did I show my \(\theta\) values?
- [ ] Did I avoid zero or negative pivot-column entries in the theta test?
- [ ] Did I keep fractions exact?
- [ ] Did I show row operations clearly?
- [ ] Did I stop only when the objective row had no negative entries?
- [ ] Did I state the maximum value of \(P\)?
- [ ] Did I state the values of \(x\) and \(y\)?
- [ ] Did I interpret the answer in context?

## 19.4 Bridge checklist

You should understand that:

- [ ] ordinary graphical LP and simplex tableau both rely on vertices;
- [ ] slack variables measure unused capacity;
- [ ] \(r=0\) means the first constraint is full;
- [ ] \(s=0\) means the second constraint is full;
- [ ] row operations are structured elimination;
- [ ] the objective row tells you whether improvement is still possible.

## 19.5 Diagram and visual understanding checklist

You should be able to explain:

- [ ] why the simplex method starts at a feasible vertex;
- [ ] why the pivot column is a direction of improvement;
- [ ] why the pivot row tells you which boundary is reached first;
- [ ] why zero slack corresponds to a boundary line;
- [ ] why the final tableau proves optimality.

## Final lesson boundary reminder

This lesson covers:

\[
\boxed{\text{two-variable simplex algorithm and tableau problems only.}}
\]

The broader simplex machinery in the uploaded evidence is useful for curiosity, but it is not core CCEA `FA22-ALGGRAPH-LO003` content unless a separate enrichment lesson is requested.
