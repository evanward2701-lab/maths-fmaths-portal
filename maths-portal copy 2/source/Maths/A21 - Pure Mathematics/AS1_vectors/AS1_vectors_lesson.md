# AS1 Vectors

## Title and Metadata

| Field | Value |
|---|---|
| Course | CCEA GCE Mathematics |
| Unit code | AS1 |
| Unit name | AS 1 Pure Mathematics |
| Topic code | AS1-VEC |
| Topic name | Vectors |
| Topic slug | vectors |
| Topic Pascal | Vectors |
| Topic ID | AS1Vectors |
| Lesson file | AS1_vectors_lesson.md |
| Learning outcome IDs | AS1-VEC-LO001, AS1-VEC-LO002, AS1-VEC-LO003, AS1-VEC-LO004, AS1-VEC-LO005 |
| Boundary note | Core lesson is 2D vectors only. Uploaded Pure Year 2 3D vectors evidence is logged as enrichment / off-spec support. |

---

## Evidence Map

| Evidence | Role | Used for |
|---|---|---|
| CCEA GCE Mathematics Specification Map | Core authority | Unit, topic, LO IDs, syllabus boundary |
| README / Module Map | Project structure | Metadata format, placeholders, lesson section order |
| Evidence Drop Checklist | Quality control | Missing evidence and off-spec logs |
| Pure Year 2 Vectors transcript | Supporting evidence only | Transferable vector language: magnitude, unit vector, vector difference, scalar multiples |
| P2 Chapter 12 Vectors PDF | Supporting evidence only | Visual ideas and off-spec risks |
| Screenshot PDF | Visual evidence only | Broad visual confirmation; not fully inspected |

No GCSE source has been used as evidence, because the task requested A-Level evidence only.

---

## Specification Alignment

| LO ID | Official focus | Core lesson section |
|---|---|---|
| AS1-VEC-LO001 | use vectors in two dimensions, including \(\mathbf{i}\) and \(\mathbf{j}\) unit vectors | Key Definitions and Notation; Core Theory 1 |
| AS1-VEC-LO002 | calculate magnitude and direction; convert between component and magnitude/direction form | Core Theory 2, 3 and 4; Worked Examples 3 and 4 |
| AS1-VEC-LO003 | vector addition, scalar multiplication and geometrical interpretations | Core Theory 5; Worked Example 5; visual assets |
| AS1-VEC-LO004 | position vectors | Core Theory 6; Worked Examples 6 and 8 |
| AS1-VEC-LO005 | distance between two points represented by position vectors | Core Theory 7; Worked Examples 6 and 7 |

---

## Learning Objectives

By the end of this lesson, you should be able to:

1. write two-dimensional vectors in column form and in \(\mathbf{i},\mathbf{j}\) form;
2. calculate the magnitude and direction of a two-dimensional vector;
3. find a unit vector in the direction of a given vector;
4. add, subtract and multiply vectors by scalars;
5. understand vector addition geometrically using triangle and parallelogram interpretations;
6. use position vectors to find vectors between points;
7. calculate the distance between two points represented by position vectors;
8. avoid common sign, notation and direction-angle errors.

---

## Prerequisite Recap

This recap uses A-Level mathematical prerequisites only, not GCSE source material.

| Skill | Why it matters here |
|---|---|
| Directed numbers | Vector components may be positive or negative. |
| Expanding brackets | Needed in unknown-distance vector equations. |
| Solving quadratics | Can appear when a distance is given and a coordinate is unknown. |
| Pythagoras | Used to find vector magnitude and distance. |
| Trigonometry | Used to convert between component form and magnitude/direction form. |
| Coordinate geometry | Position vectors connect points to vectors. |

---

## Big Picture Explanation

A vector has **size** and **direction**. A scalar has size only.

A scalar is a single number such as

\[
5,\quad -2,\quad 12.7.
\]

A vector is more like a movement instruction. For example,

\[
\begin{pmatrix}
3\\
4
\end{pmatrix}
\]

means move 3 units in the horizontal \(\mathbf{i}\) direction and 4 units in the vertical \(\mathbf{j}\) direction.

In CCEA AS1, vectors are two-dimensional. The uploaded Pure Year 2 evidence extends the ideas into 3D, but this lesson keeps the CCEA core in 2D.

---

## Key Definitions and Notation

### Vector

A **vector** has both magnitude and direction.

Examples:

\[
\begin{pmatrix}
2\\
5
\end{pmatrix},
\quad
3\mathbf{i}-4\mathbf{j},
\quad
\overrightarrow{AB}.
\]

### Scalar

A **scalar** has magnitude only.

Examples:

\[
3,\quad -7,\quad 2.5.
\]

### Column vector

A two-dimensional column vector is written as

\[
\begin{pmatrix}
x\\
y
\end{pmatrix}.
\]

The top number gives the horizontal component. The bottom number gives the vertical component.

### Unit vectors \(\mathbf{i}\) and \(\mathbf{j}\)

In two dimensions,

\[
\mathbf{i}
=
\begin{pmatrix}
1\\
0
\end{pmatrix},
\qquad
\mathbf{j}
=
\begin{pmatrix}
0\\
1
\end{pmatrix}.
\]

So

\[
\begin{pmatrix}
x\\
y
\end{pmatrix}
=
x\mathbf{i}+y\mathbf{j}.
\]

For example,

\[
\begin{pmatrix}
8\\
-2
\end{pmatrix}
=
8\mathbf{i}-2\mathbf{j}.
\]

### Magnitude

The magnitude of a vector \(\mathbf{a}\) is written

\[
|\mathbf{a}|.
\]

It means the length of the vector. If

\[
\mathbf{a}
=
\begin{pmatrix}
x\\
y
\end{pmatrix},
\]

then

\[
|\mathbf{a}|=
\sqrt{x^2+y^2}.
\]

### Unit vector

A **unit vector** has magnitude 1. The unit vector in the direction of \(\mathbf{a}\) is

\[
\hat{\mathbf{a}}=
\frac{\mathbf{a}}{|\mathbf{a}|}.
\]

### Position vector

If \(A\) is a point, then the position vector of \(A\) is the vector from the origin \(O\) to \(A\):

\[
\overrightarrow{OA}.
\]

If

\[
A(x,y),
\]

then

\[
\overrightarrow{OA}=
\begin{pmatrix}
x\\
y
\end{pmatrix}.
\]

---

## Core Theory

### 1. Converting between column form and \(\mathbf{i},\mathbf{j}\) form

Because

\[
\mathbf{i}
=
\begin{pmatrix}
1\\
0
\end{pmatrix},
\qquad
\mathbf{j}
=
\begin{pmatrix}
0\\
1
\end{pmatrix},
\]

we have

\[
x\mathbf{i}
=
x
\begin{pmatrix}
1\\
0
\end{pmatrix}
=
\begin{pmatrix}
x\\
0
\end{pmatrix}
\]

and

\[
y\mathbf{j}
=
y
\begin{pmatrix}
0\\
1
\end{pmatrix}
=
\begin{pmatrix}
0\\
y
\end{pmatrix}.
\]

Adding these gives

\[
x\mathbf{i}+y\mathbf{j}
=
\begin{pmatrix}
x\\
0
\end{pmatrix}
+
\begin{pmatrix}
0\\
y
\end{pmatrix}
=
\begin{pmatrix}
x\\
y
\end{pmatrix}.
\]

Therefore

\[
\boxed{
\begin{pmatrix}
x\\
y
\end{pmatrix}=x\mathbf{i}+y\mathbf{j}
}
\]

and

\[
\boxed{x\mathbf{i}+y\mathbf{j}=\begin{pmatrix}x\\y\end{pmatrix}.}
\]

---

### 2. Magnitude of a two-dimensional vector

Let

\[
\mathbf{a}
=
\begin{pmatrix}
x\\
y
\end{pmatrix}.
\]

This forms a right-angled triangle with horizontal side \(x\), vertical side \(y\), and hypotenuse \(|\mathbf{a}|\).

By Pythagoras,

\[
|\mathbf{a}|^2=x^2+y^2.
\]

Taking the positive square root, because length is non-negative,

\[
\boxed{|\mathbf{a}|=\sqrt{x^2+y^2}.}
\]

Example:

\[
\left|
\begin{pmatrix}
3\\
4
\end{pmatrix}
\right|
=
\sqrt{3^2+4^2}
=
\sqrt{9+16}
=
\sqrt{25}
=
5.
\]

---

### 3. Direction of a vector

For

\[
\mathbf{a}
=
\begin{pmatrix}
x\\
y
\end{pmatrix},
\]

the direction angle \(\theta\) is usually measured from the positive \(x\)-axis.

If the vector is in the first quadrant, then

\[
\tan\theta=\frac{y}{x}.
\]

So

\[
\theta=\tan^{-1}\left(\frac{y}{x}\right).
\]

However, you must check the quadrant. A vector with a negative \(x\)-component or negative \(y\)-component may not have the direction angle given directly by the calculator’s first answer.

You can also use

\[
\cos\theta=\frac{x}{|\mathbf{a}|}
\]

and

\[
\sin\theta=\frac{y}{|\mathbf{a}|}.
\]

---

### 4. Unit vectors

A unit vector in the direction of \(\mathbf{a}\) is found by dividing the vector by its magnitude.

Let

\[
\mathbf{a}
=
\begin{pmatrix}
x\\
y
\end{pmatrix}.
\]

Then

\[
|\mathbf{a}|=\sqrt{x^2+y^2}.
\]

So

\[
\hat{\mathbf{a}}
=
\frac{\mathbf{a}}{|\mathbf{a}|}
=
\frac{1}{\sqrt{x^2+y^2}}
\begin{pmatrix}
x\\
y
\end{pmatrix}.
\]

This gives

\[
\boxed{
\hat{\mathbf{a}}
=
\begin{pmatrix}
\dfrac{x}{\sqrt{x^2+y^2}}\\[6pt]
\dfrac{y}{\sqrt{x^2+y^2}}
\end{pmatrix}.
}
\]

Check that its length is 1:

\[
|\hat{\mathbf{a}}|
=
\sqrt{
\left(\frac{x}{\sqrt{x^2+y^2}}\right)^2
+
\left(\frac{y}{\sqrt{x^2+y^2}}\right)^2
}.
\]

Squaring each component gives

\[
|\hat{\mathbf{a}}|
=
\sqrt{
\frac{x^2}{x^2+y^2}
+
\frac{y^2}{x^2+y^2}
}.
\]

Using the common denominator,

\[
|\hat{\mathbf{a}}|
=
\sqrt{\frac{x^2+y^2}{x^2+y^2}}.
\]

So

\[
|\hat{\mathbf{a}}|=\sqrt{1}=1.
\]

---

### 5. Vector addition, subtraction and scalar multiplication

Let

\[
\mathbf{a}=\begin{pmatrix}a_1\\a_2\end{pmatrix},
\qquad
\mathbf{b}=\begin{pmatrix}b_1\\b_2\end{pmatrix}.
\]

Then

\[
\mathbf{a}+\mathbf{b}
=
\begin{pmatrix}
a_1+b_1\\
a_2+b_2
\end{pmatrix}.
\]

Also,

\[
\mathbf{a}-\mathbf{b}
=
\begin{pmatrix}
a_1-b_1\\
a_2-b_2
\end{pmatrix}.
\]

For a scalar \(k\),

\[
k\mathbf{a}
=
k
\begin{pmatrix}
a_1\\
a_2
\end{pmatrix}
=
\begin{pmatrix}
ka_1\\
ka_2
\end{pmatrix}.
\]

The geometry:

- \(\mathbf{a}+\mathbf{b}\) means follow \(\mathbf{a}\), then follow \(\mathbf{b}\);
- \(2\mathbf{a}\) points in the same direction as \(\mathbf{a}\), but is twice as long;
- \(-\mathbf{a}\) has the same magnitude as \(\mathbf{a}\), but points in the opposite direction.

---

### 6. Position vectors and vectors between points

Suppose

\[
A(x_1,y_1)\quad \text{and} \quad B(x_2,y_2).
\]

Then

\[
\overrightarrow{OA}=\begin{pmatrix}x_1\\y_1\end{pmatrix},
\qquad
\overrightarrow{OB}=\begin{pmatrix}x_2\\y_2\end{pmatrix}.
\]

To find \(\overrightarrow{AB}\), use

\[
\overrightarrow{AB}=\overrightarrow{OB}-\overrightarrow{OA}.
\]

So

\[
\overrightarrow{AB}
=
\begin{pmatrix}
x_2\\
y_2
\end{pmatrix}
-
\begin{pmatrix}
x_1\\
y_1
\end{pmatrix}.
\]

Subtract component by component:

\[
\boxed{
\overrightarrow{AB}
=
\begin{pmatrix}
x_2-x_1\\
y_2-y_1
\end{pmatrix}.
}
\]

A quick memory hook:

\[
\boxed{\overrightarrow{AB}=B-A}
\]

meaning second point minus first point.

---

### 7. Distance between two points

The distance between \(A(x_1,y_1)\) and \(B(x_2,y_2)\) is the magnitude of \(\overrightarrow{AB}\).

Since

\[
\overrightarrow{AB}
=
\begin{pmatrix}
x_2-x_1\\
y_2-y_1
\end{pmatrix},
\]

we have

\[
|\overrightarrow{AB}|=
\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}.
\]

Therefore

\[
\boxed{AB=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}.}
\]

Because the coordinate differences are squared, the final distance is the same whichever direction you subtract in. But the vector \(\overrightarrow{AB}\) itself is directional, so its signs matter.

---

## Visual Asset Integration

[VISUAL PLACEHOLDER: AS1VectorsSVG-001 | Source: CCEA AS1-VEC outcomes + lesson evidence | Insert from svg/AS1VectorsSVG-001.svg | Purpose: Show a 2D vector as horizontal and vertical components on coordinate axes.]

[VISUAL PLACEHOLDER: AS1VectorsSVG-002 | Source: CCEA AS1-VEC-LO003 | Insert from svg/AS1VectorsSVG-002.svg | Purpose: Show triangle and parallelogram laws of vector addition.]

[VISUAL PLACEHOLDER: AS1VectorsSVG-003 | Source: CCEA AS1-VEC-LO004 and AS1-VEC-LO005 | Insert from svg/AS1VectorsSVG-003.svg | Purpose: Show position vectors \(\overrightarrow{OA}\), \(\overrightarrow{OB}\) and the vector \(\overrightarrow{AB}=\overrightarrow{OB}-\overrightarrow{OA}\).]

[INTERACTIVE PLACEHOLDER: AS1VectorsWidget-001 | Source: CCEA AS1-VEC-LO002 | Insert from widgets/AS1VectorsWidget-001.html | Purpose: Let the student change \(x,y\) components and see magnitude, direction and unit vector update.]

---

## Worked Examples

### Worked Example 1 – Convert column form to \(\mathbf{i},\mathbf{j}\) form

Write

\[
\begin{pmatrix}
8\\
-2
\end{pmatrix}
\]

in \(\mathbf{i},\mathbf{j}\) notation.

We use

\[
\begin{pmatrix}
x\\
y
\end{pmatrix}=x\mathbf{i}+y\mathbf{j}.
\]

Here,

\[
x=8
\]

and

\[
y=-2.
\]

So

\[
\begin{pmatrix}
8\\
-2
\end{pmatrix}
=
8\mathbf{i}+(-2)\mathbf{j}.
\]

Therefore

\[
\boxed{\begin{pmatrix}8\\-2\end{pmatrix}=8\mathbf{i}-2\mathbf{j}.}
\]

---

### Worked Example 2 – Convert \(\mathbf{i},\mathbf{j}\) form to column form

Write

\[
-7\mathbf{i}+3\mathbf{j}
\]

as a column vector.

Since

\[
x\mathbf{i}+y\mathbf{j}=\begin{pmatrix}x\\y\end{pmatrix},
\]

we identify

\[
x=-7
\]

and

\[
y=3.
\]

So

\[
\boxed{-7\mathbf{i}+3\mathbf{j}=\begin{pmatrix}-7\\3\end{pmatrix}.}
\]

---

### Worked Example 3 – Magnitude and direction

Find the magnitude and direction of

\[
\mathbf{a}=\begin{pmatrix}3\\4\end{pmatrix}.
\]

First find the magnitude:

\[
|\mathbf{a}|=\sqrt{3^2+4^2}.
\]

Square each component:

\[
|\mathbf{a}|=\sqrt{9+16}.
\]

Add:

\[
|\mathbf{a}|=\sqrt{25}.
\]

So

\[
\boxed{|\mathbf{a}|=5.}
\]

Now find the direction angle \(\theta\), measured from the positive \(x\)-axis. Since the vector is in the first quadrant,

\[
\tan\theta=\frac{4}{3}.
\]

Therefore

\[
\theta=\tan^{-1}\left(\frac{4}{3}\right).
\]

Using a calculator,

\[
\theta=53.130102\ldots^\circ.
\]

To one decimal place,

\[
\boxed{\theta=53.1^\circ.}
\]

Final answer:

\[
\boxed{|\mathbf{a}|=5,\quad \theta=53.1^\circ.}
\]

---

### Worked Example 4 – Unit vector

Find the unit vector in the direction of

\[
\mathbf{a}=2\mathbf{i}-\mathbf{j}.
\]

First write the vector in column form:

\[
\mathbf{a}=\begin{pmatrix}2\\-1\end{pmatrix}.
\]

Find the magnitude:

\[
|\mathbf{a}|=\sqrt{2^2+(-1)^2}.
\]

Square the components:

\[
|\mathbf{a}|=\sqrt{4+1}.
\]

So

\[
|\mathbf{a}|=\sqrt{5}.
\]

The unit vector is

\[
\hat{\mathbf{a}}=\frac{\mathbf{a}}{|\mathbf{a}|}.
\]

Substitute:

\[
\hat{\mathbf{a}}
=
\frac{1}{\sqrt{5}}
\begin{pmatrix}
2\\
-1
\end{pmatrix}.
\]

So

\[
\boxed{
\hat{\mathbf{a}}
=
\begin{pmatrix}
\dfrac{2}{\sqrt{5}}\\[6pt]
-\dfrac{1}{\sqrt{5}}
\end{pmatrix}
}
\]

or equivalently

\[
\boxed{\hat{\mathbf{a}}=\frac{1}{\sqrt{5}}(2\mathbf{i}-\mathbf{j}).}
\]

---

### Worked Example 5 – Vector operations

Let

\[
\mathbf{a}=\begin{pmatrix}2\\3\end{pmatrix}
\quad \text{and} \quad
\mathbf{b}=\begin{pmatrix}0\\-1\end{pmatrix}.
\]

Find

\[
3\mathbf{a}+2\mathbf{b}.
\]

First calculate \(3\mathbf{a}\):

\[
3\mathbf{a}=3\begin{pmatrix}2\\3\end{pmatrix}.
\]

Multiply each component by 3:

\[
3\mathbf{a}=\begin{pmatrix}6\\9\end{pmatrix}.
\]

Now calculate \(2\mathbf{b}\):

\[
2\mathbf{b}=2\begin{pmatrix}0\\-1\end{pmatrix}.
\]

Multiply each component by 2:

\[
2\mathbf{b}=\begin{pmatrix}0\\-2\end{pmatrix}.
\]

Now add:

\[
3\mathbf{a}+2\mathbf{b}
=
\begin{pmatrix}6\\9\end{pmatrix}
+
\begin{pmatrix}0\\-2\end{pmatrix}.
\]

Add component by component:

\[
3\mathbf{a}+2\mathbf{b}
=
\begin{pmatrix}6+0\\9+(-2)\end{pmatrix}
=
\begin{pmatrix}6\\7\end{pmatrix}.
\]

Therefore

\[
\boxed{3\mathbf{a}+2\mathbf{b}=\begin{pmatrix}6\\7\end{pmatrix}.}
\]

---

### Worked Example 6 – Position vectors and distance

The points \(A\) and \(B\) have coordinates

\[
A(1,2)
\]

and

\[
B(4,0).
\]

Find \(\overrightarrow{AB}\) and the distance \(AB\).

The position vectors are

\[
\overrightarrow{OA}=\begin{pmatrix}1\\2\end{pmatrix}
\]

and

\[
\overrightarrow{OB}=\begin{pmatrix}4\\0\end{pmatrix}.
\]

Now

\[
\overrightarrow{AB}=\overrightarrow{OB}-\overrightarrow{OA}.
\]

Substitute:

\[
\overrightarrow{AB}
=
\begin{pmatrix}4\\0\end{pmatrix}
-
\begin{pmatrix}1\\2\end{pmatrix}.
\]

Subtract component by component:

\[
\overrightarrow{AB}
=
\begin{pmatrix}4-1\\0-2\end{pmatrix}
=
\begin{pmatrix}3\\-2\end{pmatrix}.
\]

Now find the distance:

\[
AB=|\overrightarrow{AB}|.
\]

So

\[
AB=\left|\begin{pmatrix}3\\-2\end{pmatrix}\right|.
\]

Use Pythagoras:

\[
AB=\sqrt{3^2+(-2)^2}.
\]

Square each component:

\[
AB=\sqrt{9+4}.
\]

Therefore

\[
\boxed{AB=\sqrt{13}.}
\]

Final answer:

\[
\boxed{\overrightarrow{AB}=\begin{pmatrix}3\\-2\end{pmatrix},\quad AB=\sqrt{13}.}
\]

---

### Worked Example 7 – Unknown coordinate from a distance

The coordinates of \(A\) and \(B\) are

\[
A(5,3)
\]

and

\[
B(1,k).
\]

Given that the distance from \(A\) to \(B\) is 5 units, find the possible values of \(k\).

Use the distance formula:

\[
AB=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}.
\]

Here,

\[
x_1=5,\quad y_1=3,
\]

and

\[
x_2=1,\quad y_2=k.
\]

So

\[
AB=\sqrt{(1-5)^2+(k-3)^2}.
\]

Simplify the \(x\)-difference:

\[
1-5=-4.
\]

Therefore

\[
AB=\sqrt{(-4)^2+(k-3)^2}.
\]

Since

\[
AB=5,
\]

we have

\[
\sqrt{(-4)^2+(k-3)^2}=5.
\]

Square both sides:

\[
(-4)^2+(k-3)^2=5^2.
\]

Calculate the squares:

\[
16+(k-3)^2=25.
\]

Subtract 16 from both sides:

\[
(k-3)^2=9.
\]

Now take square roots:

\[
k-3=\pm 3.
\]

So either

\[
k-3=3
\]

or

\[
k-3=-3.
\]

First case:

\[
k-3=3.
\]

Add 3 to both sides:

\[
k=6.
\]

Second case:

\[
k-3=-3.
\]

Add 3 to both sides:

\[
k=0.
\]

Therefore

\[
\boxed{k=0 \quad \text{or} \quad k=6.}
\]

---

### Worked Example 8 – Showing a triangle is isosceles using position vectors

The points \(O\), \(A\) and \(B\) are

\[
O(0,0),\quad A(4,2),\quad B(2,4).
\]

Show that triangle \(OAB\) is isosceles.

First find the length \(OA\).

Since

\[
\overrightarrow{OA}=\begin{pmatrix}4\\2\end{pmatrix},
\]

we have

\[
OA=\sqrt{4^2+2^2}.
\]

Square the components:

\[
OA=\sqrt{16+4}=\sqrt{20}.
\]

Now find the length \(OB\).

Since

\[
\overrightarrow{OB}=\begin{pmatrix}2\\4\end{pmatrix},
\]

we have

\[
OB=\sqrt{2^2+4^2}.
\]

Square the components:

\[
OB=\sqrt{4+16}=\sqrt{20}.
\]

Now compare:

\[
OA=\sqrt{20}
\]

and

\[
OB=\sqrt{20}.
\]

Therefore

\[
OA=OB.
\]

Since two sides of triangle \(OAB\) are equal, triangle \(OAB\) is isosceles.

\[
\boxed{\triangle OAB \text{ is isosceles because } OA=OB.}
\]

---

## Guided Practice

### Question 1

Write \(4\mathbf{i}-9\mathbf{j}\) as a column vector.

### Question 2

Find the magnitude of \(\mathbf{a}=5\mathbf{i}-12\mathbf{j}\).

### Question 3

Find the unit vector in the direction of

\[
\mathbf{b}=\begin{pmatrix}-3\\4\end{pmatrix}.
\]

### Question 4

The points \(A\) and \(B\) have coordinates

\[
A(-2,5),\quad B(4,-3).
\]

Find:

1. \(\overrightarrow{AB}\);
2. the distance \(AB\).

### Question 5

The points \(P\) and \(Q\) have coordinates

\[
P(2,-1),\quad Q(k,5).
\]

Given that \(PQ=10\), find the possible values of \(k\).

---

## Common Mistakes and Exam Traps

### Mistake 1 – Confusing a vector with its magnitude

This is a vector:

\[
\begin{pmatrix}3\\-2\end{pmatrix}.
\]

This is its magnitude:

\[
\sqrt{3^2+(-2)^2}=\sqrt{13}.
\]

Do not write

\[
\begin{pmatrix}3\\-2\end{pmatrix}=\sqrt{13}.
\]

That would claim a vector is equal to a scalar, which is not correct.

### Mistake 2 – Getting \(\overrightarrow{AB}\) the wrong way round

The correct formula is

\[
\overrightarrow{AB}=\overrightarrow{OB}-\overrightarrow{OA}.
\]

That means

\[
\boxed{\overrightarrow{AB}=B-A.}
\]

It is second letter minus first letter.

### Mistake 3 – Losing brackets when squaring negatives

Correct:

\[
(-5)^2=25.
\]

Dangerous calculator input:

\[
-5^2=-25.
\]

When a negative component is being squared, write brackets:

\[
(-5)^2.
\]

### Mistake 4 – Forgetting the quadrant for direction angles

If

\[
\mathbf{a}=\begin{pmatrix}-3\\4\end{pmatrix},
\]

then the vector points left and up. The direction angle is in quadrant II, not quadrant I.

A calculator value from

\[
\tan^{-1}\left(\frac{4}{-3}\right)
\]

needs interpretation.

### Mistake 5 – Bringing in \(\mathbf{k}\) for CCEA AS1 core

In this CCEA AS1 lesson, vectors are two-dimensional:

\[
\mathbf{i},\mathbf{j}.
\]

The uploaded Year 2 evidence uses \(\mathbf{k}\) and 3D vectors. That is not treated as required CCEA AS1 core content here.

---

## Exam Technique Notes

### 1. Decide what the question wants

If the question asks for a **vector**, give a vector:

\[
\overrightarrow{AB}=\begin{pmatrix}3\\-2\end{pmatrix}.
\]

If the question asks for a **distance**, give a scalar:

\[
AB=\sqrt{13}.
\]

### 2. Keep exact values where possible

If the magnitude is \(\sqrt{13}\), do not round unless asked.

### 3. Use surd form for exact distances

\[
\sqrt{20}=2\sqrt{5}.
\]

Both may be acceptable, but simplified surd form is usually neater.

### 4. For \(\overrightarrow{AB}\), write the subtraction explicitly

A good exam line is:

\[
\overrightarrow{AB}=\overrightarrow{OB}-\overrightarrow{OA}.
\]

Then substitute the column vectors.

### 5. For unit vectors, always divide by the magnitude

\[
\hat{\mathbf{a}}=\frac{\mathbf{a}}{|\mathbf{a}|}.
\]

Do not divide by one component only.

---

## Full Worked Solutions to Guided Practice

### Solution 1

\[
4\mathbf{i}-9\mathbf{j}=\begin{pmatrix}4\\-9\end{pmatrix}.
\]

### Solution 2

\[
\mathbf{a}=5\mathbf{i}-12\mathbf{j}=\begin{pmatrix}5\\-12\end{pmatrix}.
\]

Then

\[
|\mathbf{a}|=\sqrt{5^2+(-12)^2}=\sqrt{25+144}=\sqrt{169}=13.
\]

So

\[
\boxed{|\mathbf{a}|=13.}
\]

### Solution 3

\[
\mathbf{b}=\begin{pmatrix}-3\\4\end{pmatrix}.
\]

First find the magnitude:

\[
|\mathbf{b}|=\sqrt{(-3)^2+4^2}=\sqrt{9+16}=\sqrt{25}=5.
\]

The unit vector is

\[
\hat{\mathbf{b}}=\frac{\mathbf{b}}{|\mathbf{b}|}
=
\frac{1}{5}\begin{pmatrix}-3\\4\end{pmatrix}
=
\begin{pmatrix}-\dfrac{3}{5}\\[4pt]\dfrac{4}{5}\end{pmatrix}.
\]

So

\[
\boxed{\hat{\mathbf{b}}=\begin{pmatrix}-\dfrac{3}{5}\\[4pt]\dfrac{4}{5}\end{pmatrix}.}
\]

### Solution 4

The points are

\[
A(-2,5),\quad B(4,-3).
\]

The position vectors are

\[
\overrightarrow{OA}=\begin{pmatrix}-2\\5\end{pmatrix},
\qquad
\overrightarrow{OB}=\begin{pmatrix}4\\-3\end{pmatrix}.
\]

Now

\[
\overrightarrow{AB}=\overrightarrow{OB}-\overrightarrow{OA}.
\]

Substitute:

\[
\overrightarrow{AB}
=
\begin{pmatrix}4\\-3\end{pmatrix}
-
\begin{pmatrix}-2\\5\end{pmatrix}
=
\begin{pmatrix}4-(-2)\\-3-5\end{pmatrix}
=
\begin{pmatrix}6\\-8\end{pmatrix}.
\]

So

\[
\boxed{\overrightarrow{AB}=\begin{pmatrix}6\\-8\end{pmatrix}.}
\]

Now

\[
AB=|\overrightarrow{AB}|=\sqrt{6^2+(-8)^2}=\sqrt{36+64}=\sqrt{100}=10.
\]

Therefore

\[
\boxed{AB=10.}
\]

### Solution 5

The points are

\[
P(2,-1),\quad Q(k,5).
\]

Given \(PQ=10\), use the distance formula:

\[
PQ=\sqrt{(k-2)^2+(5-(-1))^2}.
\]

Simplify the \(y\)-difference:

\[
5-(-1)=6.
\]

So

\[
PQ=\sqrt{(k-2)^2+6^2}.
\]

Since \(PQ=10\),

\[
\sqrt{(k-2)^2+6^2}=10.
\]

Square both sides:

\[
(k-2)^2+6^2=10^2.
\]

Calculate the squares:

\[
(k-2)^2+36=100.
\]

Subtract 36 from both sides:

\[
(k-2)^2=64.
\]

Take square roots:

\[
k-2=\pm 8.
\]

So either

\[
k-2=8
\]

or

\[
k-2=-8.
\]

First case:

\[
k=10.
\]

Second case:

\[
k=-6.
\]

Therefore

\[
\boxed{k=10 \quad \text{or} \quad k=-6.}
\]

---

## Common CCEA-Style Wording

| Question wording | What to do |
|---|---|
| “Use vectors in two dimensions” | Work with \(\binom{x}{y}\), \(\mathbf{i}\), and \(\mathbf{j}\). |
| “Find the magnitude” | Use \(\sqrt{x^2+y^2}\). |
| “Find the direction” | Use trig and check the quadrant. |
| “Find the unit vector” | Divide the vector by its magnitude. |
| “The position vector of \(A\)” | Write \(\overrightarrow{OA}\). |
| “Find \(\overrightarrow{AB}\)” | Use \(\overrightarrow{OB}-\overrightarrow{OA}\). |
| “Find the distance between two points represented by position vectors” | Find the vector difference, then its magnitude. |

---

## Syllabus Gap Check

| LO ID | Covered? | Evidence limitation |
|---|---:|---|
| AS1-VEC-LO001 | Yes | CCEA spec is clear; uploaded evidence is mostly 3D, so examples are boundary-safe 2D constructions. |
| AS1-VEC-LO002 | Yes | Unit vector included; direction included. |
| AS1-VEC-LO003 | Yes | Algebraic operations included; geometry supported by visual assets. |
| AS1-VEC-LO004 | Yes | Position vectors included. |
| AS1-VEC-LO005 | Yes | Distance via vector difference included. |

### Off-spec content found but excluded from the core lesson

| Content | Source | Reason excluded |
|---|---|---|
| \(\mathbf{k}\) notation | Uploaded P2 / Pure Year 2 vectors evidence | CCEA AS1 vectors specify \(\mathbf{i},\mathbf{j}\) in two dimensions. |
| 3D vector magnitude \(\sqrt{x^2+y^2+z^2}\) | Uploaded P2 / Pure Year 2 vectors evidence | Not in supplied CCEA AS1 vector boundary. |
| Angles between 3D vectors and axes | Uploaded P2 / Pure Year 2 vectors evidence | Not in supplied CCEA AS1 vector boundary. |
| 3D geometric problems | Uploaded P2 / Pure Year 2 vectors evidence | Not in supplied CCEA AS1 vector boundary. |
| Dot product and vector equations of lines | Mentioned in uploaded evidence as boundary notes | Not included in supplied standard Mathematics vector boundary. |

---

## Visual and Interactive Asset Plan

| Asset ID | Type | File | Purpose |
|---|---|---|---|
| AS1VectorsMermaid-001 | Mermaid | mermaid/AS1VectorsMermaid-001_vector_components.md | Flowchart for vector components |
| AS1VectorsMermaid-002 | Mermaid | mermaid/AS1VectorsMermaid-002_magnitude_direction.md | Flowchart for magnitude and direction |
| AS1VectorsMermaid-003 | Mermaid | mermaid/AS1VectorsMermaid-003_vector_operations.md | Flowchart for vector operations |
| AS1VectorsMermaid-004 | Mermaid | mermaid/AS1VectorsMermaid-004_position_vectors.md | Flowchart for position vectors and distance |
| AS1VectorsMermaid-005 | Mermaid | mermaid/AS1VectorsMermaid-005_unit_vector.md | Flowchart for unit vectors |
| AS1VectorsSVG-001 | SVG | svg/AS1VectorsSVG-001.svg | 2D vector components on coordinate axes |
| AS1VectorsSVG-002 | SVG | svg/AS1VectorsSVG-002.svg | Triangle and parallelogram laws |
| AS1VectorsSVG-003 | SVG | svg/AS1VectorsSVG-003.svg | Position vectors and vector difference |
| AS1VectorsSVG-004 | SVG | svg/AS1VectorsSVG-004.svg | Magnitude and direction triangle |
| AS1VectorsSVG-005 | SVG | svg/AS1VectorsSVG-005.svg | Unit vector process |
| AS1VectorsTikZ-001 | TikZ | tikz/AS1VectorsTikZ-001_vector_components.tex | Printable vector component diagram |
| AS1VectorsTikZ-002 | TikZ | tikz/AS1VectorsTikZ-002_magnitude_direction.tex | Printable magnitude and direction diagram |
| AS1VectorsTikZ-003 | TikZ | tikz/AS1VectorsTikZ-003_vector_addition.tex | Printable triangle law diagram |
| AS1VectorsTikZ-004 | TikZ | tikz/AS1VectorsTikZ-004_parallelogram_law.tex | Printable parallelogram law diagram |
| AS1VectorsTikZ-005 | TikZ | tikz/AS1VectorsTikZ-005_position_vectors.tex | Printable position vectors diagram |
| AS1VectorsTikZ-006 | TikZ | tikz/AS1VectorsTikZ-006_unit_vector.tex | Printable unit vector process diagram |
| AS1VectorsWidget-001 | HTML widget | widgets/AS1VectorsWidget-001.html | Interactive magnitude/direction/unit-vector explorer |
| AS1VectorsWidget-002 | HTML widget | widgets/AS1VectorsWidget-002.html | Interactive position vector/distance explorer |

---

## Supplementary Sources Used

The uploaded Pure Year 2 / P2 vectors transcript and slide PDF were used only as **controlled support** for general vector language such as magnitude, unit vector, vector difference, scalar multiples and the warning that some vector content belongs outside the standard course boundary.

They were **not** used to make 3D vectors, \(\mathbf{k}\) notation or axis-angle calculations part of the CCEA AS1 core lesson.

No GCSE sources were used.

---

## Final Student Checklist

You are ready for this lesson when you can:

- [ ] write \(\binom{x}{y}\) as \(x\mathbf{i}+y\mathbf{j}\);
- [ ] write \(x\mathbf{i}+y\mathbf{j}\) as \(\binom{x}{y}\);
- [ ] calculate \(|\mathbf{a}|\) using \(\sqrt{x^2+y^2}\);
- [ ] find the direction of a vector using trigonometry;
- [ ] find a unit vector using \(\hat{\mathbf{a}}=\dfrac{\mathbf{a}}{|\mathbf{a}|}\);
- [ ] add and subtract vectors component by component;
- [ ] multiply a vector by a scalar;
- [ ] use \(\overrightarrow{AB}=\overrightarrow{OB}-\overrightarrow{OA}\);
- [ ] calculate distance between two points using the magnitude of a vector difference;
- [ ] explain why \(\mathbf{k}\) and 3D vectors are not part of this CCEA AS1 core lesson.

---

## End-of-Pack Quality Check

| Check | Result |
|---|---|
| Unit prefix correct | Yes: AS1 |
| Topic identity complete | Yes: AS1-VEC, Vectors, AS1Vectors |
| LO IDs preserved exactly | Yes: AS1-VEC-LO001 to AS1-VEC-LO005 |
| On-spec evidence covered | Yes, within the supplied CCEA AS1 vectors boundary |
| Off-spec material excluded or marked | Yes |
| Placeholders match actual files | Yes |
| Manifest and source reference updated | Yes |
| Unresolved issues | None found beyond the logged evidence limitations |
