# AS1 Vectors

## Title and Metadata

| Field | Value |
|---|---|
| Course | CCEA GCE Mathematics |
| Unit code | `AS1` |
| Unit name | `AS 1 Pure Mathematics` |
| Topic code | `AS1-VEC` |
| Topic name | `Vectors` |
| Topic slug | `vectors` |
| Topic Pascal | `Vectors` |
| Topic ID | `AS1Vectors` |
| Lesson file | `AS1_vectors_lesson.md` |
| Learning outcome IDs | `AS1-VEC-LO001`, `AS1-VEC-LO002`, `AS1-VEC-LO003`, `AS1-VEC-LO004`, `AS1-VEC-LO005` |
| Core evidence | CCEA specification map; uploaded vectors PDF; uploaded teacher transcript; screenshots PDF used as supporting visual evidence only |
| Asset status | Mermaid, SVG, TikZ and widget assets included in subfolders |

---

## Evidence Map

| Evidence | Lesson use |
|---|---|
| CCEA Mathematics specification map | Authority for AS1 Vectors identity, LO IDs and syllabus boundary. |
| `P1-Chp11-Vectors.pdf` | Core supporting evidence where aligned to CCEA AS1 Vectors: definitions, diagrams, examples, vector basics, component form, magnitude, unit vectors, position vectors, geometric proofs, speed/velocity and bearings. |
| `Chapter_11_Vectors_🚀_(Pure_Year_1)_Transcript.md` | Teacher explanations, notation warnings, route-selection advice and proof wording. |
| `Chapter_11_Vectors_🚀_(Pure_Year_1)_Screenshots.pdf` | Supporting visual evidence for slide layout and opening vector basics. No uninspected visual details are claimed. |
| Project README/module map and evidence checklist | File structure, phase workflow, missing-evidence logging and off-spec logging rules. |

---

## Specification Alignment

| LO ID | Lesson coverage |
|---|---|
| `AS1-VEC-LO001` | Use vectors in two dimensions, including column form and the unit vectors \(\mathbf{i}\) and \(\mathbf{j}\). |
| `AS1-VEC-LO002` | Calculate magnitude and direction of a vector; convert between component and magnitude/direction interpretations. |
| `AS1-VEC-LO003` | Add, subtract and scale vectors; understand geometric interpretations; prove parallelism using scalar multiples. |
| `AS1-VEC-LO004` | Use position vectors from the origin and from coordinates. |
| `AS1-VEC-LO005` | Calculate distance between points represented by position vectors using vector differences and magnitude. |

---

## Learning Objectives

By the end of this lesson, you should be able to:

1. Explain the difference between a coordinate and a vector.
2. Use column vectors and \(\mathbf{i},\mathbf{j}\) notation fluently.
3. Add, subtract and scale vectors.
4. Recognise that parallel vectors are scalar multiples.
5. Calculate magnitudes and unit vectors.
6. Find the direction of a vector using trigonometry.
7. Use position vectors to find displacement vectors.
8. Calculate distances between points represented by position vectors.
9. Solve geometric vector problems by choosing routes.
10. Write proof conclusions clearly, especially using the phrase **is a multiple of**.

---

## Prerequisite Recap

This lesson uses only general mathematical skills and earlier A-Level-style algebraic fluency. No GCSE source is used as authority.

| Skill | Why it matters for vectors |
|---|---|
| Directed numbers | Negative components mean movement in the opposite coordinate direction. |
| Pythagoras | Magnitude is found from a right-angled component triangle. |
| Trigonometry | Direction angles and bearings use sine, cosine and tangent. |
| Algebraic simplification | Expressions such as \(\frac14(-\mathbf{a}+\mathbf{b})+\frac12\mathbf{a}\) must be simplified carefully. |
| Fractions and ratios | Points dividing line segments use fractions of vectors. |
| Coordinates | Position vectors connect points to the origin. |

---

## Big Picture Explanation

A coordinate tells you **where** something is. A vector tells you **how to move**.

A point such as \((3,2)\) is a location. A vector such as

\[
\begin{pmatrix}3\\2\end{pmatrix}
\]

is a displacement: move \(3\) in the \(x\)-direction and \(2\) in the \(y\)-direction.

A vector has two properties:

\[
\text{magnitude}
\]

and

\[
\text{direction}.
\]

Magnitude means length. If the vector is

\[
\begin{pmatrix}x\\y\end{pmatrix},
\]

then its length is

\[
\sqrt{x^2+y^2}.
\]

Vectors are also a bridge to Mechanics: displacement, velocity and forces all rely on vector thinking. This topic is compact, but it is a little compass with a suspiciously large amount of influence.

---

## Key Definitions and Notation

### Vector

A **vector** represents a displacement. It has magnitude and direction.

If \(P\) and \(Q\) are points, then

\[
\overrightarrow{PQ}
\]

is the vector from \(P\) to \(Q\).

### Same vector

If two vectors have the same magnitude and the same direction, they represent the same vector even if they are drawn in different places.

This is a common trap: the vector is not different just because it occurs somewhere else on the page.

### Opposite vector

\[
\overrightarrow{AB}=-\overrightarrow{BA}
\]

The two vectors are equal in magnitude and parallel, but in opposite directions.

### Zero vector

The zero vector represents no movement:

\[
\mathbf{0}=\begin{pmatrix}0\\0\end{pmatrix}.
\]

Also,

\[
\overrightarrow{PQ}+\overrightarrow{QP}=\mathbf{0}.
\]

### Resultant vector

The result of adding vectors is called the **resultant vector**.

The triangle law says:

\[
\overrightarrow{AB}+\overrightarrow{BC}=\overrightarrow{AC}.
\]

### Scalar

A **scalar** is an ordinary number used to scale a vector.

If \(\lambda\) is a scalar, then

\[
\lambda\mathbf{a}
\]

is a scalar multiple of \(\mathbf{a}\).

If \(\lambda>0\), the vector keeps the same direction. If \(\lambda<0\), the vector reverses direction. If \(\lambda=0\), the result is the zero vector.

### Parallel vectors

Any vector parallel to \(\mathbf{a}\) can be written as

\[
\lambda\mathbf{a},
\]

where \(\lambda\) is a scalar.

To prove that two vectors are parallel, show that one is a scalar multiple of the other.

### Unit vector

A **unit vector** is a vector whose magnitude is \(1\).

If \(\mathbf{a}\) is a non-zero vector, then the unit vector in the same direction is

\[
\hat{\mathbf{a}}=\frac{\mathbf{a}}{|\mathbf{a}|}.
\]

### \(\mathbf{i}\) and \(\mathbf{j}\)

The unit vector in the positive \(x\)-direction is

\[
\mathbf{i}=\begin{pmatrix}1\\0\end{pmatrix}.
\]

The unit vector in the positive \(y\)-direction is

\[
\mathbf{j}=\begin{pmatrix}0\\1\end{pmatrix}.
\]

Therefore,

\[
\begin{pmatrix}4\\3\end{pmatrix}
=4\begin{pmatrix}1\\0\end{pmatrix}+3\begin{pmatrix}0\\1\end{pmatrix}
=4\mathbf{i}+3\mathbf{j}.
\]

### Position vector

The **position vector** of a point \(A\) is the vector from the origin \(O\) to \(A\):

\[
\overrightarrow{OA}.
\]

If \(A=(3,2)\), then

\[
\overrightarrow{OA}=\begin{pmatrix}3\\2\end{pmatrix}.
\]

---

## Core Theory

### 1. Vector addition

Using the triangle law,

\[
\overrightarrow{AB}+\overrightarrow{BC}=\overrightarrow{AC}.
\]

If

\[
\mathbf{a}=\begin{pmatrix}3\\-2\end{pmatrix},
\qquad
\mathbf{b}=\begin{pmatrix}0\\-1\end{pmatrix},
\]

then

\[
\mathbf{a}+\mathbf{b}
=\begin{pmatrix}3\\-2\end{pmatrix}+\begin{pmatrix}0\\-1\end{pmatrix}
=\begin{pmatrix}3+0\\-2+(-1)\end{pmatrix}
=\begin{pmatrix}3\\-3\end{pmatrix}.
\]

### 2. Vector subtraction

Vector subtraction is defined using addition and negation:

\[
\mathbf{a}-\mathbf{b}=\mathbf{a}+(-\mathbf{b}).
\]

If

\[
\mathbf{b}=\begin{pmatrix}2\\-5\end{pmatrix},
\]

then

\[
-\mathbf{b}=-\begin{pmatrix}2\\-5\end{pmatrix}=\begin{pmatrix}-2\\5\end{pmatrix}.
\]

If

\[
\mathbf{a}=\begin{pmatrix}7\\1\end{pmatrix},
\]

then

\[
\mathbf{a}-\mathbf{b}
=\begin{pmatrix}7\\1\end{pmatrix}-\begin{pmatrix}2\\-5\end{pmatrix}
=\begin{pmatrix}7-2\\1-(-5)\end{pmatrix}
=\begin{pmatrix}5\\6\end{pmatrix}.
\]

### 3. Scalar multiplication

If

\[
\mathbf{a}=\begin{pmatrix}3\\-2\end{pmatrix},
\]

then

\[
2\mathbf{a}=2\begin{pmatrix}3\\-2\end{pmatrix}=\begin{pmatrix}6\\-4\end{pmatrix}.
\]

The direction is the same as \(\mathbf{a}\), but the magnitude is doubled.

If

\[
-\frac12\mathbf{a}=-\frac12\begin{pmatrix}3\\-2\end{pmatrix}=\begin{pmatrix}-\frac32\\1\end{pmatrix},
\]

then the negative sign reverses direction and the factor \(\frac12\) halves the magnitude.

### 4. Showing vectors are parallel

Two non-zero vectors are parallel if one is a scalar multiple of the other.

Show that

\[
2\mathbf{a}+4\mathbf{b}
\]

and

\[
3\mathbf{a}+6\mathbf{b}
\]

are parallel.

First factor each vector:

\[
2\mathbf{a}+4\mathbf{b}=2(\mathbf{a}+2\mathbf{b}),
\]

and

\[
3\mathbf{a}+6\mathbf{b}=3(\mathbf{a}+2\mathbf{b}).
\]

Directly,

\[
3\mathbf{a}+6\mathbf{b}=\frac32(2\mathbf{a}+4\mathbf{b}).
\]

Therefore one vector is a scalar multiple of the other, so the vectors are parallel.

### 5. Component form and \(\mathbf{i},\mathbf{j}\) form

A vector in column form

\[
\begin{pmatrix}x\\y\end{pmatrix}
\]

means \(x\) units in the \(x\)-direction and \(y\) units in the \(y\)-direction.

Using \(\mathbf{i}\) and \(\mathbf{j}\),

\[
\begin{pmatrix}x\\y\end{pmatrix}=x\mathbf{i}+y\mathbf{j}.
\]

Examples:

\[
\begin{pmatrix}4\\3\end{pmatrix}=4\mathbf{i}+3\mathbf{j},
\]

and

\[
5\mathbf{i}-\mathbf{j}=\begin{pmatrix}5\\-1\end{pmatrix}.
\]

### 6. Magnitude of a vector

The magnitude of a vector is its length.

If

\[
\mathbf{a}=\begin{pmatrix}x\\y\end{pmatrix},
\]

then

\[
|\mathbf{a}|=\sqrt{x^2+y^2}.
\]

For example,

\[
\mathbf{a}=\begin{pmatrix}3\\4\end{pmatrix}.
\]

Then

\[
|\mathbf{a}|=\sqrt{3^2+4^2}=\sqrt{9+16}=\sqrt{25}=5.
\]

### 7. Unit vectors

If

\[
\mathbf{a}=\begin{pmatrix}3\\4\end{pmatrix},
\]

then \(|\mathbf{a}|=5\). To make a vector of length \(1\) in the same direction, divide by its magnitude:

\[
\hat{\mathbf{a}}=\frac{\mathbf{a}}{|\mathbf{a}|}
=\frac15\begin{pmatrix}3\\4\end{pmatrix}
=\begin{pmatrix}\frac35\\\frac45\end{pmatrix}.
\]

Check:

\[
|\hat{\mathbf{a}}|
=\sqrt{\left(\frac35\right)^2+\left(\frac45\right)^2}
=\sqrt{\frac9{25}+\frac{16}{25}}
=\sqrt{1}=1.
\]

### 8. Direction of a vector

If

\[
\mathbf{a}=\begin{pmatrix}4\\5\end{pmatrix},
\]

then the vector moves \(4\) units across and \(5\) units up.

Let \(\theta\) be the angle between \(\mathbf{a}\) and the positive \(x\)-axis.

\[
\tan\theta=\frac{\text{opposite}}{\text{adjacent}}=\frac54.
\]

So

\[
\theta=\tan^{-1}\left(\frac54\right)=51.3^\circ
\]

to 3 significant figures.

### 9. Position vectors and vector differences

If

\[
A=(3,4),\qquad B=(11,2),
\]

then

\[
\overrightarrow{OA}=\begin{pmatrix}3\\4\end{pmatrix}=3\mathbf{i}+4\mathbf{j},
\]

and

\[
\overrightarrow{OB}=\begin{pmatrix}11\\2\end{pmatrix}=11\mathbf{i}+2\mathbf{j}.
\]

The vector from \(A\) to \(B\) is

\[
\overrightarrow{AB}=\overrightarrow{OB}-\overrightarrow{OA}.
\]

So

\[
\overrightarrow{AB}
=\begin{pmatrix}11\\2\end{pmatrix}-\begin{pmatrix}3\\4\end{pmatrix}
=\begin{pmatrix}11-3\\2-4\end{pmatrix}
=\begin{pmatrix}8\\-2\end{pmatrix}.
\]

Therefore,

\[
\overrightarrow{AB}=8\mathbf{i}-2\mathbf{j}.
\]

---

## Visual Asset Integration

[VISUAL PLACEHOLDER: AS1VectorsSVG-001 | Source: P1-Chp11-Vectors.pdf page 4 and screenshots PDF | Insert from svg/AS1VectorsSVG-001.svg | Purpose: Show that a vector is a displacement with magnitude and direction, and that equal vectors can appear in different locations.]

[VISUAL PLACEHOLDER: AS1VectorsSVG-002 | Source: P1-Chp11-Vectors.pdf page 4 | Insert from svg/AS1VectorsSVG-002.svg | Purpose: Illustrate triangle law \(\overrightarrow{AB}+\overrightarrow{BC}=\overrightarrow{AC}\).]

[VISUAL PLACEHOLDER: AS1VectorsSVG-003 | Source: P1-Chp11-Vectors.pdf page 10 | Insert from svg/AS1VectorsSVG-003.svg | Purpose: Show column vector components and \(\mathbf{i},\mathbf{j}\) basis vectors.]

[VISUAL PLACEHOLDER: AS1VectorsSVG-004 | Source: P1-Chp11-Vectors.pdf pages 13-14 | Insert from svg/AS1VectorsSVG-004.svg | Purpose: Show magnitude and unit-vector scaling using a right-angled triangle.]

[VISUAL PLACEHOLDER: AS1VectorsSVG-005 | Source: P1-Chp11-Vectors.pdf pages 16-18 | Insert from svg/AS1VectorsSVG-005.svg | Purpose: Show position vectors from the origin and vector difference \(\overrightarrow{AB}=\overrightarrow{OB}-\overrightarrow{OA}\).]

[VISUAL PLACEHOLDER: AS1VectorsSVG-006 | Source: P1-Chp11-Vectors.pdf pages 20-22 | Insert from svg/AS1VectorsSVG-006.svg | Purpose: Show geometric vector proof with scalar multiples and comparing coefficients.]

[INTERACTIVE PLACEHOLDER: AS1VectorsWidget-001 | Source: CCEA AS1-VEC-LO002 plus P1-Chp11-Vectors.pdf magnitude/unit-vector examples | Insert from widgets/AS1VectorsWidget-001.html | Purpose: Let students adjust vector components and see magnitude, unit vector and direction update.]

---

## Worked Examples

### Worked Example 1: Route vectors

Suppose the diagram gives:

\[
\overrightarrow{PQ}=\mathbf{a},\qquad
\overrightarrow{QS}=\mathbf{b},\qquad
\overrightarrow{SR}=\mathbf{c},\qquad
\overrightarrow{PT}=\mathbf{d}.
\]

#### (a) Find \(\overrightarrow{QT}\)

To travel from \(Q\) to \(T\), use the route

\[
Q\to P\to T.
\]

So

\[
\overrightarrow{QT}=\overrightarrow{QP}+\overrightarrow{PT}.
\]

Since

\[
\overrightarrow{QP}=-\overrightarrow{PQ}=-\mathbf{a},
\]

and

\[
\overrightarrow{PT}=\mathbf{d},
\]

we get

\[
\overrightarrow{QT}=-\mathbf{a}+\mathbf{d}=\mathbf{d}-\mathbf{a}.
\]

\[
\boxed{\overrightarrow{QT}=\mathbf{d}-\mathbf{a}}
\]

#### (b) Find \(\overrightarrow{PR}\)

Use the route

\[
P\to Q\to S\to R.
\]

\[
\overrightarrow{PR}=\overrightarrow{PQ}+\overrightarrow{QS}+\overrightarrow{SR}=\mathbf{a}+\mathbf{b}+\mathbf{c}.
\]

\[
\boxed{\overrightarrow{PR}=\mathbf{a}+\mathbf{b}+\mathbf{c}}
\]

#### (c) Find \(\overrightarrow{TS}\)

Use the route

\[
T\to P\to Q\to S.
\]

\[
\overrightarrow{TS}=\overrightarrow{TP}+\overrightarrow{PQ}+\overrightarrow{QS}=-\mathbf{d}+\mathbf{a}+\mathbf{b}.
\]

\[
\boxed{\overrightarrow{TS}=\mathbf{a}+\mathbf{b}-\mathbf{d}}
\]

#### (d) Find \(\overrightarrow{TR}\)

Use the route

\[
T\to P\to Q\to S\to R.
\]

\[
\overrightarrow{TR}=\overrightarrow{TP}+\overrightarrow{PQ}+\overrightarrow{QS}+\overrightarrow{SR}
=-\mathbf{d}+\mathbf{a}+\mathbf{b}+\mathbf{c}.
\]

\[
\boxed{\overrightarrow{TR}=\mathbf{a}+\mathbf{b}+\mathbf{c}-\mathbf{d}}
\]

---

### Worked Example 2: Vector expressions in a parallelogram

In parallelogram \(PQRS\),

\[
\overrightarrow{PQ}=\mathbf{a},\qquad \overrightarrow{PS}=\mathbf{b}.
\]

Point \(N\) lies on \(SQ\) such that

\[
SN:NQ=3:2.
\]

#### (a) Find \(\overrightarrow{SQ}\)

Use the route

\[
S\to P\to Q.
\]

\[
\overrightarrow{SQ}=\overrightarrow{SP}+\overrightarrow{PQ}.
\]

Since

\[
\overrightarrow{SP}=-\overrightarrow{PS}=-\mathbf{b},
\]

and

\[
\overrightarrow{PQ}=\mathbf{a},
\]

we have

\[
\overrightarrow{SQ}=-\mathbf{b}+\mathbf{a}=\mathbf{a}-\mathbf{b}.
\]

\[
\boxed{\overrightarrow{SQ}=\mathbf{a}-\mathbf{b}}
\]

#### (b) Find \(\overrightarrow{NR}\)

Since

\[
SN:NQ=3:2,
\]

the whole line \(SQ\) is split into \(5\) parts. Hence

\[
\overrightarrow{NQ}=\frac25\overrightarrow{SQ}.
\]

Use the route

\[
N\to Q\to R.
\]

\[
\overrightarrow{NR}=\overrightarrow{NQ}+\overrightarrow{QR}.
\]

In a parallelogram,

\[
\overrightarrow{QR}=\overrightarrow{PS}=\mathbf{b}.
\]

Therefore

\[
\overrightarrow{NR}=\frac25\overrightarrow{SQ}+\mathbf{b}.
\]

Substitute \(\overrightarrow{SQ}=-\mathbf{b}+\mathbf{a}\):

\[
\overrightarrow{NR}=\frac25(-\mathbf{b}+\mathbf{a})+\mathbf{b}.
\]

Expand:

\[
\overrightarrow{NR}=-\frac25\mathbf{b}+\frac25\mathbf{a}+\mathbf{b}.
\]

Collect terms:

\[
\overrightarrow{NR}=\frac25\mathbf{a}+\left(-\frac25+1\right)\mathbf{b}
=\frac25\mathbf{a}+\frac35\mathbf{b}.
\]

\[
\boxed{\overrightarrow{NR}=\frac25\mathbf{a}+\frac35\mathbf{b}}
\]

Technique note: add the ratio to the diagram and write the route first.

---

### Worked Example 3: Point on a side of a triangle

In triangle \(OAB\),

\[
\overrightarrow{OA}=\mathbf{a},\qquad \overrightarrow{OB}=\mathbf{b}.
\]

Point \(P\) lies on \(AB\) such that

\[
AP:PB=3:1.
\]

Find \(\overrightarrow{OP}\).

First,

\[
\overrightarrow{AB}=\overrightarrow{AO}+\overrightarrow{OB}=-\mathbf{a}+\mathbf{b}.
\]

Since \(AP:PB=3:1\),

\[
\overrightarrow{AP}=\frac34\overrightarrow{AB}.
\]

Use the route

\[
O\to A\to P.
\]

\[
\overrightarrow{OP}=\overrightarrow{OA}+\overrightarrow{AP}.
\]

Substitute:

\[
\overrightarrow{OP}=\mathbf{a}+\frac34(-\mathbf{a}+\mathbf{b}).
\]

Expand:

\[
\overrightarrow{OP}=\mathbf{a}-\frac34\mathbf{a}+\frac34\mathbf{b}.
\]

Write \(\mathbf{a}=\frac44\mathbf{a}\):

\[
\overrightarrow{OP}=\frac44\mathbf{a}-\frac34\mathbf{a}+\frac34\mathbf{b}
=\frac14\mathbf{a}+\frac34\mathbf{b}.
\]

\[
\boxed{\overrightarrow{OP}=\frac14\mathbf{a}+\frac34\mathbf{b}}
\]

---

### Worked Example 4: \(\mathbf{i},\mathbf{j}\) notation

Given

\[
\mathbf{a}=3\mathbf{i},\qquad \mathbf{b}=\mathbf{i}+\mathbf{j},\qquad \mathbf{c}=\mathbf{i}-2\mathbf{j},
\]

answer the following.

#### (a) Write \(\mathbf{a}\) in vector form

\[
3\mathbf{i}=3\begin{pmatrix}1\\0\end{pmatrix}=\begin{pmatrix}3\\0\end{pmatrix}.
\]

\[
\boxed{\mathbf{a}=\begin{pmatrix}3\\0\end{pmatrix}}
\]

#### (b) Find \(\mathbf{b}+2\mathbf{c}\) in \(\mathbf{i},\mathbf{j}\) form

\[
\mathbf{b}+2\mathbf{c}=(\mathbf{i}+\mathbf{j})+2(\mathbf{i}-2\mathbf{j}).
\]

Expand:

\[
\mathbf{b}+2\mathbf{c}=\mathbf{i}+\mathbf{j}+2\mathbf{i}-4\mathbf{j}.
\]

Collect terms:

\[
\mathbf{b}+2\mathbf{c}=3\mathbf{i}-3\mathbf{j}.
\]

\[
\boxed{\mathbf{b}+2\mathbf{c}=3\mathbf{i}-3\mathbf{j}}
\]

---

### Worked Example 5: Find a scalar using parallel vectors

Given

\[
\mathbf{c}=3\mathbf{i}+4\mathbf{j},\qquad \mathbf{d}=\mathbf{i}-2\mathbf{j},
\]

find \(\lambda\) if

\[
\mathbf{c}+\lambda\mathbf{d}
\]

is parallel to

\[
\mathbf{i}+\mathbf{j}.
\]

Write in column form:

\[
\mathbf{c}=\begin{pmatrix}3\\4\end{pmatrix},\qquad
\mathbf{d}=\begin{pmatrix}1\\-2\end{pmatrix}.
\]

Then

\[
\mathbf{c}+\lambda\mathbf{d}
=\begin{pmatrix}3\\4\end{pmatrix}+\lambda\begin{pmatrix}1\\-2\end{pmatrix}
=\begin{pmatrix}3\\4\end{pmatrix}+\begin{pmatrix}\lambda\\-2\lambda\end{pmatrix}
=\begin{pmatrix}3+\lambda\\4-2\lambda\end{pmatrix}.
\]

Also

\[
\mathbf{i}+\mathbf{j}=\begin{pmatrix}1\\1\end{pmatrix}.
\]

Since the vectors are parallel,

\[
\begin{pmatrix}3+\lambda\\4-2\lambda\end{pmatrix}
=k\begin{pmatrix}1\\1\end{pmatrix}
=\begin{pmatrix}k\\k\end{pmatrix}.
\]

So

\[
3+\lambda=k,
\]

and

\[
4-2\lambda=k.
\]

Therefore

\[
3+\lambda=4-2\lambda.
\]

Add \(2\lambda\):

\[
3+3\lambda=4.
\]

Subtract \(3\):

\[
3\lambda=1.
\]

Divide by \(3\):

\[
\boxed{\lambda=\frac13}.
\]

Check:

\[
3+\frac13=\frac{10}{3},
\]

and

\[
4-2\left(\frac13\right)=4-\frac23=\frac{12}{3}-\frac23=\frac{10}{3}.
\]

---

### Worked Example 6: Magnitude and unit vector

Convert

\[
\mathbf{a}=\begin{pmatrix}12\\-5\end{pmatrix}
\]

to a unit vector.

First find the magnitude:

\[
|\mathbf{a}|=\sqrt{12^2+(-5)^2}=\sqrt{144+25}=\sqrt{169}=13.
\]

Now divide by the magnitude:

\[
\hat{\mathbf{a}}=\frac{\mathbf{a}}{|\mathbf{a}|}
=\frac1{13}\begin{pmatrix}12\\-5\end{pmatrix}
=\begin{pmatrix}\frac{12}{13}\\-\frac{5}{13}\end{pmatrix}.
\]

\[
\boxed{\hat{\mathbf{a}}=\begin{pmatrix}\frac{12}{13}\\-\frac{5}{13}\end{pmatrix}}
\]

---

### Worked Example 7: Position vectors from coordinates

The points \(A\) and \(B\) have coordinates

\[
A=(3,4),\qquad B=(11,2).
\]

Find the position vectors and \(\overrightarrow{AB}\).

\[
\overrightarrow{OA}=3\mathbf{i}+4\mathbf{j}.
\]

\[
\overrightarrow{OB}=11\mathbf{i}+2\mathbf{j}.
\]

Now

\[
\overrightarrow{AB}=\overrightarrow{OB}-\overrightarrow{OA}.
\]

\[
\overrightarrow{AB}=(11\mathbf{i}+2\mathbf{j})-(3\mathbf{i}+4\mathbf{j}).
\]

Remove brackets:

\[
\overrightarrow{AB}=11\mathbf{i}+2\mathbf{j}-3\mathbf{i}-4\mathbf{j}.
\]

Collect:

\[
\overrightarrow{AB}=8\mathbf{i}-2\mathbf{j}.
\]

\[
\boxed{\overrightarrow{AB}=8\mathbf{i}-2\mathbf{j}}
\]

---

### Worked Example 8: Position vector and distance

Given

\[
\overrightarrow{OA}=5\mathbf{i}-2\mathbf{j},\qquad
\overrightarrow{AB}=3\mathbf{i}+4\mathbf{j},
\]

find \(\overrightarrow{OB}\) and \(|\overrightarrow{OB}|\).

Use the route \(O\to A\to B\):

\[
\overrightarrow{OB}=\overrightarrow{OA}+\overrightarrow{AB}.
\]

\[
\overrightarrow{OB}=(5\mathbf{i}-2\mathbf{j})+(3\mathbf{i}+4\mathbf{j})=8\mathbf{i}+2\mathbf{j}.
\]

In column form,

\[
\overrightarrow{OB}=\begin{pmatrix}8\\2\end{pmatrix}.
\]

Magnitude:

\[
|\overrightarrow{OB}|=\sqrt{8^2+2^2}=\sqrt{64+4}=\sqrt{68}.
\]

Simplify:

\[
\sqrt{68}=\sqrt{4\times17}=2\sqrt{17}.
\]

\[
\boxed{|\overrightarrow{OB}|=2\sqrt{17}}
\]

---

### Worked Example 9: Proving two vectors are parallel

In the evidence example,

\[
X \text{ is on } AB \text{ such that } AX:XB=3:1,
\]

and \(M\) is the midpoint of \(BC\). Show that \(XM\parallel OC\).

The evidence gives

\[
\overrightarrow{OC}=\mathbf{a}+\mathbf{b}.
\]

Now find \(\overrightarrow{XM}\). Since \(AX:XB=3:1\), \(XB\) is \(\frac14\) of \(AB\). The vector

\[
\overrightarrow{AB}=-\mathbf{a}+\mathbf{b}.
\]

Therefore

\[
\overrightarrow{XB}=\frac14(-\mathbf{a}+\mathbf{b}).
\]

Since \(M\) is the midpoint of \(BC\),

\[
\overrightarrow{BM}=\frac12\mathbf{a}.
\]

Use the route \(X\to B\to M\):

\[
\overrightarrow{XM}=\overrightarrow{XB}+\overrightarrow{BM}.
\]

Substitute:

\[
\overrightarrow{XM}=\frac14(-\mathbf{a}+\mathbf{b})+\frac12\mathbf{a}.
\]

Expand:

\[
\overrightarrow{XM}=-\frac14\mathbf{a}+\frac14\mathbf{b}+\frac12\mathbf{a}.
\]

Write \(\frac12\mathbf{a}=\frac24\mathbf{a}\):

\[
\overrightarrow{XM}=-\frac14\mathbf{a}+\frac24\mathbf{a}+\frac14\mathbf{b}
=\frac14\mathbf{a}+\frac14\mathbf{b}.
\]

Factor:

\[
\overrightarrow{XM}=\frac14(\mathbf{a}+\mathbf{b}).
\]

But

\[
\overrightarrow{OC}=\mathbf{a}+\mathbf{b}.
\]

So

\[
\overrightarrow{XM}=\frac14\overrightarrow{OC}.
\]

Therefore \(\overrightarrow{XM}\) is a scalar multiple of \(\overrightarrow{OC}\), so

\[
\boxed{XM\parallel OC}.
\]

---

### Worked Example 10: Comparing coefficients to prove diagonals bisect

In parallelogram \(OACB\),

\[
\overrightarrow{OA}=\mathbf{a},\qquad \overrightarrow{OB}=\mathbf{b}.
\]

The diagonals \(OC\) and \(AB\) intersect at \(X\). Prove that the diagonals bisect each other.

Because \(OACB\) is a parallelogram,

\[
\overrightarrow{OC}=\mathbf{a}+\mathbf{b}.
\]

Let \(X\) be a fraction \(\lambda\) of the way along \(BA\) from \(B\) to \(A\). Use the route \(O\to B\to X\):

\[
\overrightarrow{OX}=\overrightarrow{OB}+\overrightarrow{BX}
=\mathbf{b}+\lambda\overrightarrow{BA}.
\]

Now

\[
\overrightarrow{BA}=-\mathbf{b}+\mathbf{a}.
\]

So

\[
\overrightarrow{OX}=\mathbf{b}+\lambda(-\mathbf{b}+\mathbf{a})
=\mathbf{b}-\lambda\mathbf{b}+\lambda\mathbf{a}
=\lambda\mathbf{a}+(1-\lambda)\mathbf{b}.
\]

Now express \(\overrightarrow{OX}\) using diagonal \(OC\). Let \(X\) be a fraction \(\mu\) of the way along \(OC\):

\[
\overrightarrow{OX}=\mu\overrightarrow{OC}=\mu(\mathbf{a}+\mathbf{b})=\mu\mathbf{a}+\mu\mathbf{b}.
\]

The two expressions are equal:

\[
\mu\mathbf{a}+\mu\mathbf{b}=\lambda\mathbf{a}+(1-\lambda)\mathbf{b}.
\]

Compare coefficients of non-parallel vectors \(\mathbf{a}\) and \(\mathbf{b}\):

\[
\mu=\lambda,
\]

and

\[
\mu=1-\lambda.
\]

Since \(\mu=\lambda\), substitute into \(\mu=1-\lambda\):

\[
\lambda=1-\lambda.
\]

Add \(\lambda\):

\[
2\lambda=1.
\]

Divide by \(2\):

\[
\lambda=\frac12.
\]

Therefore \(\mu=\frac12\), so \(X\) is halfway along both diagonals. Hence the diagonals bisect each other.

---

### Worked Example 11: Angle using vector lengths

Given

\[
\overrightarrow{AB}=3\mathbf{i}-2\mathbf{j},
\qquad
\overrightarrow{AC}=\mathbf{i}-5\mathbf{j},
\]

determine \(\angle BAC\).

First find the side lengths.

\[
|\overrightarrow{AB}|=\sqrt{3^2+(-2)^2}=\sqrt{9+4}=\sqrt{13}.
\]

\[
|\overrightarrow{AC}|=\sqrt{1^2+(-5)^2}=\sqrt{1+25}=\sqrt{26}.
\]

Find \(\overrightarrow{CB}\):

\[
\overrightarrow{CB}=\overrightarrow{AB}-\overrightarrow{AC}
=\begin{pmatrix}3\\-2\end{pmatrix}-\begin{pmatrix}1\\-5\end{pmatrix}
=\begin{pmatrix}2\\3\end{pmatrix}.
\]

So

\[
|\overrightarrow{CB}|=\sqrt{2^2+3^2}=\sqrt{13}.
\]

Use the cosine rule. The side opposite \(\angle BAC\) is \(BC\):

\[
BC^2=AB^2+AC^2-2(AB)(AC)\cos A.
\]

Substitute:

\[
(\sqrt{13})^2=(\sqrt{13})^2+(\sqrt{26})^2-2(\sqrt{13})(\sqrt{26})\cos A.
\]

Simplify:

\[
13=13+26-2\sqrt{338}\cos A.
\]

Since

\[
\sqrt{338}=\sqrt{169\times2}=13\sqrt2,
\]

we get

\[
13=39-26\sqrt2\cos A.
\]

Subtract \(39\):

\[
-26=-26\sqrt2\cos A.
\]

Divide by \(-26\):

\[
1=\sqrt2\cos A.
\]

So

\[
\cos A=\frac1{\sqrt2}.
\]

Therefore

\[
A=45^\circ.
\]

\[
\boxed{\angle BAC=45^\circ}
\]

---

### Worked Example 12: Speed from velocity

A ship has velocity

\[
12\mathbf{i}+5\mathbf{j}\ \text{km/h}.
\]

Find its speed.

Velocity is a vector quantity. Speed is the corresponding scalar magnitude.

\[
\text{speed}=|12\mathbf{i}+5\mathbf{j}|.
\]

Write the velocity as a column vector:

\[
12\mathbf{i}+5\mathbf{j}=\begin{pmatrix}12\\5\end{pmatrix}.
\]

Now find the magnitude:

\[
\left|\begin{pmatrix}12\\5\end{pmatrix}\right|=\sqrt{12^2+5^2}=\sqrt{144+25}=\sqrt{169}=13.
\]

\[
\boxed{\text{speed}=13\text{ km/h}}
\]

---

### Worked Example 13: Bearings and position vectors

A cadet leaves \(O\) and walks \(15\) km on a bearing of \(120^\circ\) to reach \(A\). Find the position vector of \(A\) relative to \(O\).

Use the convention:

- east is the positive \(\mathbf{i}\) direction;
- north is the positive \(\mathbf{j}\) direction;
- bearings are measured clockwise from north.

A bearing of \(120^\circ\) is \(30^\circ\) south of east.

East component:

\[
15\cos30^\circ.
\]

North component:

\[
-15\sin30^\circ.
\]

Therefore,

\[
\overrightarrow{OA}
=\begin{pmatrix}15\cos30^\circ\\-15\sin30^\circ\end{pmatrix}.
\]

Use exact values:

\[
\cos30^\circ=\frac{\sqrt3}{2},\qquad \sin30^\circ=\frac12.
\]

So

\[
\overrightarrow{OA}
=\begin{pmatrix}15\cdot\frac{\sqrt3}{2}\\-15\cdot\frac12\end{pmatrix}
=\begin{pmatrix}\frac{15\sqrt3}{2}\\-\frac{15}{2}\end{pmatrix}\text{ km}.
\]

To 3 significant figures,

\[
\overrightarrow{OA}\approx\begin{pmatrix}13.0\\-7.5\end{pmatrix}\text{ km}.
\]

Sign-convention warning: if \(\mathbf{i}\) is east and \(\mathbf{j}\) is north, south has a negative \(\mathbf{j}\) component.

---

## Guided Practice

### Practice 1: Basic vector routes

Given

\[
\overrightarrow{AB}=\mathbf{p},\qquad \overrightarrow{BC}=\mathbf{q},\qquad \overrightarrow{CD}=\mathbf{r},
\]

find \(\overrightarrow{AC}\), \(\overrightarrow{AD}\), \(\overrightarrow{DA}\), and \(\overrightarrow{BD}\).

### Practice 2: Component operations

Let

\[
\mathbf{a}=\begin{pmatrix}5\\-2\end{pmatrix},\qquad
\mathbf{b}=\begin{pmatrix}-1\\4\end{pmatrix}.
\]

Find \(\mathbf{a}+\mathbf{b}\), \(\mathbf{a}-\mathbf{b}\), \(3\mathbf{a}\), and \(2\mathbf{a}-\mathbf{b}\).

### Practice 3: \(\mathbf{i},\mathbf{j}\) notation

Given

\[
\mathbf{u}=4\mathbf{i}-3\mathbf{j},\qquad \mathbf{v}=-2\mathbf{i}+5\mathbf{j},
\]

find \(\mathbf{u}+2\mathbf{v}\) in \(\mathbf{i},\mathbf{j}\) form.

### Practice 4: Magnitude and unit vector

For

\[
\mathbf{a}=\begin{pmatrix}-8\\15\end{pmatrix},
\]

find \(|\mathbf{a}|\) and the unit vector in the direction of \(\mathbf{a}\).

### Practice 5: Position vectors

The points \(A\) and \(B\) have coordinates

\[
A=(-2,5),\qquad B=(4,-3).
\]

Find \(\overrightarrow{OA}\), \(\overrightarrow{OB}\), \(\overrightarrow{AB}\), and the distance \(AB\).

### Practice 6: Parallel vectors

Find \(k\) such that

\[
\begin{pmatrix}2+k\\7-2k\end{pmatrix}
\]

is parallel to

\[
\begin{pmatrix}3\\1\end{pmatrix}.
\]

### Practice 7: Geometric vector proof

Suppose

\[
\overrightarrow{OA}=\mathbf{a},\qquad \overrightarrow{OB}=\mathbf{b}.
\]

Point \(P\) lies on \(AB\) such that

\[
AP:PB=2:1.
\]

Find \(\overrightarrow{OP}\).

---

## Common Mistakes and Exam Traps

1. **Thinking vectors depend on location.** A vector is not tied to where it is drawn.
2. **Forgetting direction when reversing a vector.** \(\overrightarrow{AB}=-\overrightarrow{BA}\), not \(\overrightarrow{AB}=\overrightarrow{BA}\).
3. **Missing the route line.** Write routes such as \(\overrightarrow{NR}=\overrightarrow{NQ}+\overrightarrow{QR}\).
4. **Not adding ratios to the diagram.** For \(SN:NQ=3:2\), write the ratio on the diagram and use \(\overrightarrow{NQ}=\frac25\overrightarrow{SQ}\).
5. **Weak proof conclusion.** Finish with “therefore one vector is a multiple of the other, so the line segments are parallel.”
6. **Unit vector without dividing by magnitude.** Always use \(\hat{\mathbf{a}}=\frac{\mathbf{a}}{|\mathbf{a}|}\).
7. **Direction angles without a sketch.** Draw a component triangle.
8. **Bearings sign convention.** South is negative \(\mathbf{j}\) if north is positive \(\mathbf{j}\).
9. **Confusing speed and velocity.** Velocity is a vector; speed is a scalar.
10. **Writing \(s\) like \(5\).** Make handwritten scalars visibly distinct.

---

## Exam Technique

- Start vector geometry with a route.
- For position vectors, use destination minus start:
  \[
  \overrightarrow{AB}=\overrightarrow{OB}-\overrightarrow{OA}.
  \]
- For parallel proof, factor out the scalar.
- Use exact values unless decimals are requested.
- For direction questions, draw a component triangle.
- For bearings, draw north lines and measure clockwise from north.
- Include units for applied vector quantities.

---

## Full Worked Solutions to Guided Practice

### Solution 1

\[
\overrightarrow{AC}=\overrightarrow{AB}+\overrightarrow{BC}=\mathbf{p}+\mathbf{q}.
\]

\[
\overrightarrow{AD}=\overrightarrow{AB}+\overrightarrow{BC}+\overrightarrow{CD}=\mathbf{p}+\mathbf{q}+\mathbf{r}.
\]

\[
\overrightarrow{DA}=-\overrightarrow{AD}=-(\mathbf{p}+\mathbf{q}+\mathbf{r})=-\mathbf{p}-\mathbf{q}-\mathbf{r}.
\]

\[
\overrightarrow{BD}=\overrightarrow{BC}+\overrightarrow{CD}=\mathbf{q}+\mathbf{r}.
\]

### Solution 2

\[
\mathbf{a}+\mathbf{b}=\begin{pmatrix}5\\-2\end{pmatrix}+\begin{pmatrix}-1\\4\end{pmatrix}=\begin{pmatrix}4\\2\end{pmatrix}.
\]

\[
\mathbf{a}-\mathbf{b}=\begin{pmatrix}5\\-2\end{pmatrix}-\begin{pmatrix}-1\\4\end{pmatrix}=\begin{pmatrix}6\\-6\end{pmatrix}.
\]

\[
3\mathbf{a}=3\begin{pmatrix}5\\-2\end{pmatrix}=\begin{pmatrix}15\\-6\end{pmatrix}.
\]

\[
2\mathbf{a}-\mathbf{b}=2\begin{pmatrix}5\\-2\end{pmatrix}-\begin{pmatrix}-1\\4\end{pmatrix}=\begin{pmatrix}10\\-4\end{pmatrix}-\begin{pmatrix}-1\\4\end{pmatrix}=\begin{pmatrix}11\\-8\end{pmatrix}.
\]

### Solution 3

\[
\mathbf{u}+2\mathbf{v}=(4\mathbf{i}-3\mathbf{j})+2(-2\mathbf{i}+5\mathbf{j})
\]

\[
=4\mathbf{i}-3\mathbf{j}-4\mathbf{i}+10\mathbf{j}=7\mathbf{j}.
\]

### Solution 4

\[
|\mathbf{a}|=\sqrt{(-8)^2+15^2}=\sqrt{64+225}=\sqrt{289}=17.
\]

\[
\hat{\mathbf{a}}=\frac1{17}\begin{pmatrix}-8\\15\end{pmatrix}=\begin{pmatrix}-\frac8{17}\\\frac{15}{17}\end{pmatrix}.
\]

### Solution 5

\[
\overrightarrow{OA}=\begin{pmatrix}-2\\5\end{pmatrix},
\qquad
\overrightarrow{OB}=\begin{pmatrix}4\\-3\end{pmatrix}.
\]

\[
\overrightarrow{AB}=\overrightarrow{OB}-\overrightarrow{OA}=\begin{pmatrix}4\\-3\end{pmatrix}-\begin{pmatrix}-2\\5\end{pmatrix}=\begin{pmatrix}6\\-8\end{pmatrix}.
\]

\[
AB=|\overrightarrow{AB}|=\sqrt{6^2+(-8)^2}=\sqrt{36+64}=10.
\]

### Solution 6

Let

\[
\begin{pmatrix}2+k\\7-2k\end{pmatrix}=\lambda\begin{pmatrix}3\\1\end{pmatrix}=\begin{pmatrix}3\lambda\\\lambda\end{pmatrix}.
\]

So

\[
2+k=3\lambda,
\]

and

\[
7-2k=\lambda.
\]

Substitute:

\[
2+k=3(7-2k).
\]

Expand:

\[
2+k=21-6k.
\]

Add \(6k\):

\[
2+7k=21.
\]

Subtract \(2\):

\[
7k=19.
\]

Divide by \(7\):

\[
\boxed{k=\frac{19}{7}}.
\]

### Solution 7

\[
\overrightarrow{AB}=\overrightarrow{OB}-\overrightarrow{OA}=\mathbf{b}-\mathbf{a}.
\]

Since \(AP:PB=2:1\),

\[
\overrightarrow{AP}=\frac23\overrightarrow{AB}.
\]

Use the route \(O\to A\to P\):

\[
\overrightarrow{OP}=\overrightarrow{OA}+\overrightarrow{AP}.
\]

Substitute:

\[
\overrightarrow{OP}=\mathbf{a}+\frac23(\mathbf{b}-\mathbf{a})
=\mathbf{a}+\frac23\mathbf{b}-\frac23\mathbf{a}.
\]

\[
\overrightarrow{OP}=\frac33\mathbf{a}-\frac23\mathbf{a}+\frac23\mathbf{b}
=\frac13\mathbf{a}+\frac23\mathbf{b}.
\]

\[
\boxed{\overrightarrow{OP}=\frac13\mathbf{a}+\frac23\mathbf{b}}
\]

---

## Syllabus Gap Check

| LO ID | Coverage status | Notes |
|---|---|---|
| `AS1-VEC-LO001` | Covered | 2D vectors, column form and \(\mathbf{i},\mathbf{j}\) form covered. |
| `AS1-VEC-LO002` | Covered | Magnitude, direction, unit vectors, bearings and speed from velocity covered. |
| `AS1-VEC-LO003` | Covered | Addition, subtraction, scalar multiplication, parallel vectors, geometric interpretation and proofs covered. |
| `AS1-VEC-LO004` | Covered | Position vectors from origin and coordinates covered. |
| `AS1-VEC-LO005` | Covered | Distance between two points using position-vector difference and magnitude covered. |

### Off-Spec Content Found but Excluded

| Evidence item | Decision |
|---|---|
| 3D vector cross product | Excluded from core. Logged as Further Maths / enrichment. |
| Vector multiplication | Excluded from core. |
| Set Cartesian product discussion | Excluded from core. |
| Casio vector-mode cross-product calculation | Excluded from core. |
| STEP 2010 extension | Excluded from core lesson. |
| Full Further Maths vector comments | Excluded from core. |

---

## Visual and Interactive Asset Plan

| Asset ID | Type | Source | Purpose |
|---|---|---|---|
| `AS1VectorsMermaid-001` to `AS1VectorsMermaid-010` | Mermaid | Lesson evidence and spec boundary | Concept maps and workflows for vector basics, triangle law, components, magnitude, position vectors, proofs and modelling. |
| `AS1VectorsSVG-001` to `AS1VectorsSVG-006` | SVG | Lesson evidence | Core visual diagrams for lesson pages. |
| `AS1VectorsTikZ-001` to `AS1VectorsTikZ-007` | TikZ | Lesson evidence | Printable mathematical diagrams. |
| `AS1VectorsWidget-001` | HTML/CSS/JS widget | AS1 vectors and magnitude evidence | Interactive vector explorer. |

---

## Supplementary Sources Used

| Source | Status |
|---|---|
| Uploaded DrFrost/Pearson-style vectors PDF | Used where aligned with AS1 Vectors; not treated as CCEA authority. |
| Uploaded teacher transcript | Used for explanations, warnings and worked-method preservation. |
| Edexcel GCSE examples inside uploaded evidence | Used only as on-spec method support. |
| STEP extension in PDF | Not used in core lesson. |
| Cross product / Further Maths comments | Not used in core lesson. |

---

## Final Student Checklist

| Skill | Yes/Not yet |
|---|---|
| I know that a vector has magnitude and direction. |  |
| I can explain why equal vectors can be drawn in different places. |  |
| I can use \(\overrightarrow{AB}=-\overrightarrow{BA}\). |  |
| I can add and subtract column vectors. |  |
| I can multiply a vector by a scalar. |  |
| I can prove vectors are parallel by showing one is a multiple of the other. |  |
| I can use \(\mathbf{i}\) and \(\mathbf{j}\) notation. |  |
| I can convert between column form and \(\mathbf{i},\mathbf{j}\) form. |  |
| I can calculate \(|\mathbf{a}|\) using Pythagoras. |  |
| I can find a unit vector using \(\hat{\mathbf{a}}=\frac{\mathbf{a}}{|\mathbf{a}|}\). |  |
| I can find a direction angle using trigonometry. |  |
| I can use position vectors from the origin. |  |
| I can use \(\overrightarrow{AB}=\overrightarrow{OB}-\overrightarrow{OA}\). |  |
| I can calculate distance between two points using vector magnitude. |  |
| I can solve geometric vector problems by choosing routes. |  |
| I can compare coefficients in non-parallel vector proofs. |  |
| I can distinguish velocity from speed. |  |
| I know to draw a big diagram for bearings. |  |
| I remember to include units where required. |  |
