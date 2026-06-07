# FAS1 Matrices: Transformations, Determinants and Invariant Lines

# 1. Lesson Title and Metadata

```yaml
date_generated: 2026-06-04
course: CCEA GCE Further Mathematics
unit_code: FAS1
unit_name: Further AS 1 Pure Mathematics
applied_section: Pure
topic_code: FAS1-MAT
topic_name: "Matrices: Transformations, Determinants and Invariant Lines"
topic_slug: matrices_invariant_lines
topic_pascal: MatricesInvariantLines
topic_id: FAS1MatricesInvariantLines
lesson_file: FAS1_matrices_invariant_lines_lesson.md
lesson_status: Written file
```

## Target LO IDs

```text
FAS1-MAT-LO003
FAS1-MAT-LO004
FAS1-MAT-LO006
FAS1-MAT-LO007
FAS1-MAT-LO008
FAS1-MAT-LO009
FAS1-MAT-LO010
```

## Bridge tags

```text
#AS1VectorsBridge
#AS1GraphTransformationsBridge
#AS1SimultaneousEquationsBridge
#GCSECoordinateGeometryBridge
```

## Topic tags

```text
#FAS1
#MAT
#Matrices
#LinearTransformations
#InvariantLines
#InvariantPoints
#Determinants
#SingularMatrices
#ExamTechnique
```

## Boundary Statement

This is a **CCEA FAS1 Matrices lesson** on matrix transformations, determinants and invariant lines. The uploaded FP2 eigenvalue/eigenvector material is not treated as CCEA core content. The transcript's geometric intuition that certain lines can remain lines under a transformation is useful background, but the eigenvalue method itself is excluded from the core lesson. The transcript directly defines eigenvectors through \(A\mathbf{x}=\lambda\mathbf{x}\) and the characteristic equation \(\det(A-\lambda I)=0\), which are logged as off-spec for this CCEA lesson.

---

# 2. Evidence Map

| Source | Used in this lesson? | Use type |
|---|---:|---|
| CCEA GCE Further Mathematics Specification Map | Yes | Core authority for `FAS1-MAT` learning outcomes. |
| Further Maths README module map | Yes | Metadata and workflow authority. |
| Further Maths Evidence Drop Checklist | Yes | Evidence QA and off-spec control. |
| CCEA GCE Mathematics Specification Map | Yes | Ordinary A-Level bridge only. |
| Ordinary A-Level Maths Bridge Extracts | Yes | Bridge framing only. |
| `transcripts.md` | Partly | Off-spec evidence plus invariant-line intuition. |
| `Chapter_5_Matrix_Algebra_♾️_(Further_Pure_2)_screenshots.pdf` | Partly | Visual evidence logged; no unseen details claimed. |
| Cross-board FP2 examples | No core use | Excluded from core; optional enrichment only. |

## Visual Evidence Limitation

The screenshot PDF did not provide extractable text through the file parser. The visible preview shows a cross-board FP2 matrix algebra chapter, with Bicen Maths logo transformation diagrams labelled by eigenvalues/eigenvectors. No uninspected page detail is claimed.

---

# 3. Specification Alignment

| LO ID | Official wording | Lesson coverage | Evidence source | Boundary note | Ordinary A-Level Maths bridge |
|---|---|---|---|---|---|
| `FAS1-MAT-LO003` | demonstrate understanding of and use zero and identity matrices | Identity matrix \(I\) and zero vector/matrix notation used in transformation context. | CCEA Further Maths Specification Map | Core. No eigenvalue characteristic equation use. | AS1 algebra and vectors. |
| `FAS1-MAT-LO004` | use matrices to represent linear transformations in 2D | Matrix maps \(\begin{pmatrix}x\\y\end{pmatrix}\) to \(\begin{pmatrix}x'\\y'\end{pmatrix}\). | CCEA Further Maths Specification Map | Core. | AS1 vectors and graph transformations. |
| `FAS1-MAT-LO006` | find invariant points and lines for a linear transformation in 2D | Direct CCEA method using transformed coordinates and line conditions. | CCEA Further Maths Specification Map | Core. Eigenvalue shortcut excluded. | AS1 simultaneous equations and straight lines. |
| `FAS1-MAT-LO007` | calculate determinants of \(2\times2\) and \(3\times3\) matrices | \(2\times2\) determinant used in transformation interpretation. | CCEA Further Maths Specification Map | Core for \(2\times2\) here; \(3\times3\) determinant not the lesson focus. | AS1 algebra. |
| `FAS1-MAT-LO008` | interpret the determinant of a \(2\times2\) matrix as the scale factor of a linear transformation | Determinant as signed area scale factor. | CCEA Further Maths Specification Map | Core. | AS1 graph transformations and GCSE area. |
| `FAS1-MAT-LO009` | demonstrate understanding of the implication of the zero value of the determinant of a simple \(2\times2\) transformation matrix | Zero determinant collapses area and usually maps the plane onto a line or lower-dimensional set. | CCEA Further Maths Specification Map | Core. | AS1 transformations and simultaneous equations. |
| `FAS1-MAT-LO010` | demonstrate understanding of and use singular and non-singular matrices | Singular if determinant \(0\); non-singular if determinant non-zero. | CCEA Further Maths Specification Map | Core support. | AS1 equation-solving logic. |

---

# 4. Learning Objectives

## Core Further Maths Objectives

By the end of this lesson, you should be able to:

1. Represent a 2D linear transformation using a matrix  
   \[
   A=
   \begin{pmatrix}
   a & b\\
   c & d
   \end{pmatrix}.
   \]

2. Apply \(A\) to a general point/vector  
   \[
   \mathbf{x}=
   \begin{pmatrix}
   x\\
   y
   \end{pmatrix}
   \]
   and obtain
   \[
   A\mathbf{x}
   =
   \begin{pmatrix}
   ax+by\\
   cx+dy
   \end{pmatrix}.
   \]

3. Find invariant points by solving  
   \[
   A\begin{pmatrix}x\\y\end{pmatrix}
   =
   \begin{pmatrix}x\\y\end{pmatrix}.
   \]

4. Find invariant lines by requiring that the image of every point on a line still lies on the same line.

5. Calculate the determinant  
   \[
   \det A=ad-bc
   \]
   and interpret it as the area scale factor of the transformation.

6. Explain what \(\det A=0\) implies for a simple \(2\times2\) transformation.

## Bridge Objectives

You should connect this lesson to AS1 vector notation, straight-line equations, simultaneous equations and GCSE coordinate geometry.

## Exam Technique Objectives

You should be able to use exact algebra, distinguish invariant points from invariant lines, state final invariant lines as Cartesian equations, interpret determinant sign and determinant zero, and avoid importing off-spec eigenvalue methods unless a question explicitly defines them.

---

# 5. Explicit Prerequisite Recap

## GCSE foundations

You should already be comfortable with coordinates \((x,y)\), equations of straight lines, substitution, simultaneous equations, area scale factor language, expanding and simplifying expressions.

## Ordinary AS/A2 Mathematics foundations

You should already know that a vector such as  
\[
\begin{pmatrix}
x\\
y
\end{pmatrix}
\]
can represent a position from the origin or a displacement in the plane.

Scalar multiplication stretches a vector:

\[
k
\begin{pmatrix}
x\\
y
\end{pmatrix}
=
\begin{pmatrix}
kx\\
ky
\end{pmatrix}.
\]

A matrix transformation is more powerful. It can change the two components in a mixed way:

\[
\begin{pmatrix}
a & b\\
c & d
\end{pmatrix}
\begin{pmatrix}
x\\
y
\end{pmatrix}
=
\begin{pmatrix}
ax+by\\
cx+dy
\end{pmatrix}.
\]

The \(x\)-coordinate after transformation can depend on both \(x\) and \(y\). The \(y\)-coordinate after transformation can also depend on both \(x\) and \(y\).

## A-Level Maths Bridge: What You Already Know and What Further Maths Changes

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| AS1 vectors | Vectors in two dimensions, component notation, magnitude, direction, unit vectors and scalar multiples. | A matrix acts on a vector and can change direction, scale, orientation and area. | Do not assume every transformed vector stays parallel to itself. |
| AS1 graph transformations | Stretches and translations of graphs such as \(y=f(x)\). | A matrix transformation acts on the whole coordinate plane. | A matrix can shear, rotate, reflect or collapse the plane, not just stretch a graph vertically or horizontally. |
| AS1 simultaneous equations | Solving linked equations by elimination or substitution. | Invariant points and lines require solving algebraic conditions produced by the transformation. | Solving for one point is not the same as proving a whole line is invariant. |
| AS1 straight lines | Equations such as \(y=mx+c\), gradients and intercepts. | A line is invariant if its transformed points still satisfy the same line equation. | A line can be invariant even when individual points on it move. |
| GCSE coordinate geometry | Coordinates, gradients, basic area and transformations. | Determinants describe area scaling under a matrix transformation. | A negative determinant is not a “negative area”; it signals orientation reversal as well as scale. |

In ordinary A-Level Maths, this idea appeared as vectors, graph transformations and simultaneous equations.  
In Further Maths, the same idea becomes a transformation of the whole plane using a matrix.  
The key upgrade is that one compact object, a matrix, controls the movement of every point.  
The danger is treating “line unchanged” and “points unchanged” as the same thing.

---

# 6. Big Picture Explanation

A \(2\times2\) matrix is a rule for transforming the plane.

If

\[
A=
\begin{pmatrix}
a & b\\
c & d
\end{pmatrix},
\]

then the point or position vector

\[
\begin{pmatrix}
x\\
y
\end{pmatrix}
\]

is sent to

\[
A
\begin{pmatrix}
x\\
y
\end{pmatrix}
=
\begin{pmatrix}
ax+by\\
cx+dy
\end{pmatrix}.
\]

So the original point \((x,y)\) becomes the image point \((x',y')\), where

\[
x'=ax+by,
\]

and

\[
y'=cx+dy.
\]

A point is invariant if it does not move:

\[
A
\begin{pmatrix}
x\\
y
\end{pmatrix}
=
\begin{pmatrix}
x\\
y
\end{pmatrix}.
\]

A line is invariant if every point on the line is transformed to another point still on that same line.

Important:

\[
\text{invariant line} \neq \text{line of invariant points}.
\]

For

\[
A=
\begin{pmatrix}
a & b\\
c & d
\end{pmatrix},
\]

the determinant is

\[
\det A=ad-bc.
\]

For a \(2\times2\) linear transformation, \(|\det A|\) is the area scale factor. If \(\det A=0\), area collapses to zero, so the transformation is singular.

---

# 7. Key Definitions and Notation

## 7.1 Matrix

A **matrix** is a rectangular array of numbers. In this lesson, the main object is a \(2\times2\) matrix:

\[
A=
\begin{pmatrix}
a & b\\
c & d
\end{pmatrix}.
\]

## 7.2 Column vector

A **column vector** in two dimensions is written as

\[
\mathbf{x}
=
\begin{pmatrix}
x\\
y
\end{pmatrix}.
\]

The zero vector is

\[
\mathbf{0}
=
\begin{pmatrix}
0\\
0
\end{pmatrix}.
\]

## 7.3 Linear transformation in 2D

A \(2\times2\) matrix can represent a **linear transformation** in the plane:

\[
\begin{pmatrix}
x'\\
y'
\end{pmatrix}
=
\begin{pmatrix}
ax+by\\
cx+dy
\end{pmatrix}.
\]

The prime notation \(x'\), \(y'\) means “after the transformation”.

## 7.4 Identity matrix

The \(2\times2\) identity matrix is

\[
I=
\begin{pmatrix}
1 & 0\\
0 & 1
\end{pmatrix}.
\]

It leaves every vector unchanged:

\[
I
\begin{pmatrix}
x\\
y
\end{pmatrix}
=
\begin{pmatrix}
x\\
y
\end{pmatrix}.
\]

## 7.5 Zero matrix

The \(2\times2\) zero matrix is

\[
O=
\begin{pmatrix}
0 & 0\\
0 & 0
\end{pmatrix}.
\]

It sends every point to the origin.

## 7.6 Invariant point

A point is an **invariant point** if it stays fixed under the transformation:

\[
A
\begin{pmatrix}
x\\
y
\end{pmatrix}
=
\begin{pmatrix}
x\\
y
\end{pmatrix}.
\]

Equating components gives:

\[
ax+by=x,
\]

\[
cx+dy=y.
\]

## 7.7 Invariant line

A line is an **invariant line** if every point on the line is transformed to another point on the same line. This does **not** necessarily mean every point on the line stays fixed.

## 7.8 Line of invariant points

A **line of invariant points** is stronger than an invariant line. For a line of invariant points, every point on the line is fixed.

\[
\text{line invariant}
\quad\not\Rightarrow\quad
\text{points invariant}.
\]

## 7.9 Determinant

For

\[
A=
\begin{pmatrix}
a & b\\
c & d
\end{pmatrix},
\]

the determinant is

\[
\det A=ad-bc.
\]

## 7.10 Singular and non-singular matrix

A square matrix \(A\) is **singular** if

\[
\det A=0.
\]

A square matrix \(A\) is **non-singular** if

\[
\det A\neq 0.
\]

---

# 8. Core Theory

## 8.1 Applying a matrix transformation

Let

\[
A=
\begin{pmatrix}
a & b\\
c & d
\end{pmatrix}
\]

and

\[
\mathbf{x}=
\begin{pmatrix}x\\y\end{pmatrix}.
\]

Then

\[
A\mathbf{x}
=
\begin{pmatrix}
a & b\\
c & d
\end{pmatrix}
\begin{pmatrix}
x\\
y
\end{pmatrix}
=
\begin{pmatrix}
ax+by\\
cx+dy
\end{pmatrix}.
\]

So the transformation sends

\[
(x,y)\mapsto(ax+by,\;cx+dy).
\]

**Bridge Note:** In ordinary A-Level Maths, a vector represented a direction or position. Here, Further Maths extends this by using a matrix as a rule which transforms every vector in the plane.

## 8.2 How to read a transformation matrix from basis vectors

The standard basis vectors are

\[
\mathbf{i}=\begin{pmatrix}1\\0\end{pmatrix},
\qquad
\mathbf{j}=\begin{pmatrix}0\\1\end{pmatrix}.
\]

If

\[
A=\begin{pmatrix}a&b\\c&d\end{pmatrix},
\]

then

\[
A\mathbf{i}=\begin{pmatrix}a\\c\end{pmatrix},
\qquad
A\mathbf{j}=\begin{pmatrix}b\\d\end{pmatrix}.
\]

So the first column is where \(\mathbf{i}\) goes and the second column is where \(\mathbf{j}\) goes.

**Exam trap:** The first row is not where \(\mathbf{i}\) goes. The first **column** is where \(\mathbf{i}\) goes.

## 8.3 Invariant points: direct method

A point is invariant if it maps to itself:

\[
A
\begin{pmatrix}
x\\y
\end{pmatrix}
=
\begin{pmatrix}
x\\y
\end{pmatrix}.
\]

Substitute the general transformation:

\[
\begin{pmatrix}
ax+by\\
cx+dy
\end{pmatrix}
=
\begin{pmatrix}
x\\y
\end{pmatrix}.
\]

Equate corresponding components:

\[
ax+by=x,
\]

\[
cx+dy=y.
\]

Bring all terms to the left:

\[
(a-1)x+by=0,
\]

\[
cx+(d-1)y=0.
\]

For any \(2\times2\) linear transformation, the origin is always invariant:

\[
A\begin{pmatrix}0\\0\end{pmatrix}=\begin{pmatrix}0\\0\end{pmatrix}.
\]

## 8.4 Example: invariant points forming a line

Let

\[
A=\begin{pmatrix}2&1\\3&4\end{pmatrix}.
\]

Find the invariant points.

\[
\begin{pmatrix}2&1\\3&4\end{pmatrix}
\begin{pmatrix}x\\y\end{pmatrix}
=
\begin{pmatrix}x\\y\end{pmatrix}.
\]

Multiply:

\[
\begin{pmatrix}2x+y\\3x+4y\end{pmatrix}
=
\begin{pmatrix}x\\y\end{pmatrix}.
\]

Equate components:

\[
2x+y=x,
\]

\[
3x+4y=y.
\]

From the first equation:

\[
x+y=0,
\]

so

\[
y=-x.
\]

From the second equation:

\[
3x+3y=0,
\]

so again

\[
y=-x.
\]

Therefore every point on

\[
\boxed{y=-x}
\]

is invariant.

Check with a general point on the line:

\[
\begin{pmatrix}x\\-x\end{pmatrix}.
\]

\[
\begin{pmatrix}2&1\\3&4\end{pmatrix}
\begin{pmatrix}x\\-x\end{pmatrix}
=
\begin{pmatrix}2x-x\\3x-4x\end{pmatrix}
=
\begin{pmatrix}x\\-x\end{pmatrix}.
\]

## 8.5 Invariant lines: the direct CCEA-safe method

A general line through the origin has equation

\[
y=mx.
\]

A general point on it is

\[
\begin{pmatrix}x\\mx\end{pmatrix}.
\]

Apply

\[
A=\begin{pmatrix}a&b\\c&d\end{pmatrix}.
\]

Then

\[
A\begin{pmatrix}x\\mx\end{pmatrix}
=
\begin{pmatrix}ax+bmx\\cx+dmx\end{pmatrix}
=
\begin{pmatrix}x(a+bm)\\x(c+dm)\end{pmatrix}.
\]

So

\[
x'=x(a+bm),
\qquad
 y'=x(c+dm).
\]

For the line to be invariant, the image point must satisfy the same equation:

\[
y'=mx'.
\]

Substitute:

\[
x(c+dm)=m[x(a+bm)].
\]

For \(x\neq0\):

\[
c+dm=m(a+bm).
\]

Expand:

\[
c+dm=am+bm^2.
\]

Bring all terms to one side:

\[
bm^2+(a-d)m-c=0.
\]

So the gradients \(m\) of invariant lines through the origin satisfy

\[
\boxed{bm^2+(a-d)m-c=0.}
\]

## 8.6 Special case: vertical invariant line

The method using \(y=mx\) does not include the vertical line \(x=0\). Check it separately.

A general point on \(x=0\) is

\[
\begin{pmatrix}0\\y\end{pmatrix}.
\]

\[
A\begin{pmatrix}0\\y\end{pmatrix}
=
\begin{pmatrix}by\\dy\end{pmatrix}.
\]

For this to stay on \(x=0\), we need

\[
by=0
\]

for every \(y\), so

\[
\boxed{x=0\text{ is invariant if }b=0.}
\]

## 8.7 Invariant line versus line of invariant points

An invariant line means:

\[
(x,y)\in L \Rightarrow (x',y')\in L.
\]

A line of invariant points means:

\[
A\begin{pmatrix}x\\y\end{pmatrix}=\begin{pmatrix}x\\y\end{pmatrix}
\]

for every point on the line.

## 8.8 Example: finding invariant lines using \(y=mx\)

Let

\[
A=\begin{pmatrix}2&1\\3&0\end{pmatrix}.
\]

A general point on \(y=mx\) is

\[
\begin{pmatrix}x\\mx\end{pmatrix}.
\]

Apply \(A\):

\[
A\begin{pmatrix}x\\mx\end{pmatrix}
=
\begin{pmatrix}2x+mx\\3x\end{pmatrix}.
\]

So

\[
x'=x(2+m),
\qquad
 y'=3x.
\]

For invariance:

\[
3x=m[x(2+m)].
\]

For \(x\neq0\):

\[
3=m(2+m).
\]

Expand:

\[
3=2m+m^2.
\]

So

\[
m^2+2m-3=0.
\]

Factorise:

\[
(m+3)(m-1)=0.
\]

Therefore

\[
m=-3\quad\text{or}\quad m=1.
\]

The invariant lines are

\[
\boxed{y=-3x}
\]

and

\[
\boxed{y=x}.
\]

Check \(x=0\). Here \(b=1\neq0\), so \(x=0\) is not invariant.

## 8.9 Determinant as area scale factor

For

\[
A=\begin{pmatrix}a&b\\c&d\end{pmatrix},
\]

\[
\det A=ad-bc.
\]

For a \(2\times2\) matrix transformation, \(|\det A|\) is the area scale factor.

- positive determinant: orientation preserved;
- negative determinant: orientation reversed;
- zero determinant: area collapsed to zero.

## 8.10 Why the determinant measures area scale factor

The unit square has side vectors

\[
\mathbf{i}=\begin{pmatrix}1\\0\end{pmatrix},
\qquad
\mathbf{j}=\begin{pmatrix}0\\1\end{pmatrix}.
\]

Under \(A\), these become

\[
A\mathbf{i}=\begin{pmatrix}a\\c\end{pmatrix},
\qquad
A\mathbf{j}=\begin{pmatrix}b\\d\end{pmatrix}.
\]

The unit square becomes a parallelogram with adjacent side vectors

\[
\begin{pmatrix}a\\c\end{pmatrix}
\quad\text{and}\quad
\begin{pmatrix}b\\d\end{pmatrix}.
\]

The signed area of this parallelogram is

\[
ad-bc.
\]

Therefore the area scale factor is

\[
|\det A|=|ad-bc|.
\]

## 8.11 Example: determinant as area scale factor

Let

\[
A=\begin{pmatrix}3&1\\2&4\end{pmatrix}.
\]

\[
\det A=3\cdot4-1\cdot2=12-2=10.
\]

So areas are enlarged by scale factor \(10\). Since \(\det A>0\), orientation is preserved.

## 8.12 Example: negative determinant

Let

\[
B=\begin{pmatrix}1&3\\2&0\end{pmatrix}.
\]

\[
\det B=1\cdot0-3\cdot2=0-6=-6.
\]

So areas are enlarged by scale factor \(6\), and orientation is reversed.

Do not say the area scale factor is \(-6\). Area scale factors are not negative.

## 8.13 Example: zero determinant and singular transformation

Let

\[
C=\begin{pmatrix}2&4\\1&2\end{pmatrix}.
\]

\[
\det C=2\cdot2-4\cdot1=4-4=0.
\]

Therefore \(C\) is singular.

Now

\[
C\begin{pmatrix}x\\y\end{pmatrix}
=
\begin{pmatrix}2x+4y\\x+2y\end{pmatrix}.
\]

The first component is twice the second component:

\[
2x+4y=2(x+2y).
\]

So every image point satisfies

\[
x'=2y',
\]

equivalently

\[
y'=\frac12x'.
\]

The whole plane has collapsed onto

\[
\boxed{y=\frac12x}.
\]

## 8.14 How to find invariant lines without using off-spec eigenvalues

The uploaded transcript's invariant-line example uses eigenvalues and eigenvectors. For this CCEA lesson, use the direct transformation method instead:

1. Let the line be \(y=mx\).
2. Use a general point \(\begin{pmatrix}x\\mx\end{pmatrix}\).
3. Transform it.
4. Force the image point to satisfy \(y'=mx'\).
5. Solve for \(m\).
6. Check \(x=0\) separately if needed.

---

# 9. Visual Asset Integration

[VISUAL PLACEHOLDER: FAS1MatricesInvariantLinesMermaid-001 | Source: CCEA FAS1-MAT specification boundary | Insert from mermaid/FAS1MatricesInvariantLinesMermaid-001.md | Purpose: Show the decision flow from matrix transformation to invariant point, invariant line and determinant interpretation.]

[VISUAL PLACEHOLDER: FAS1MatricesInvariantLinesSVG-001 | Source: CCEA FAS1-MAT specification boundary + AI-proposed teaching visual | Insert from svg/FAS1MatricesInvariantLinesSVG-001.svg | Purpose: Show the unit square transformed into a parallelogram, with side vectors \(A\mathbf{i}\) and \(A\mathbf{j}\), and label the determinant \(ad-bc\) as signed area scale factor.]

[VISUAL PLACEHOLDER: FAS1MatricesInvariantLinesSVG-002 | Source: CCEA FAS1-MAT specification boundary + transcript visual intuition from uploaded FP2 evidence | Insert from svg/FAS1MatricesInvariantLinesSVG-002.svg | Purpose: Show a line \(y=mx\) through the origin, a point \(P\) on the line, and its image \(P'\) still on the same line.]

[VISUAL PLACEHOLDER: FAS1MatricesInvariantLinesBridgeSVG-001 | Source: Ordinary A-Level Maths bridge + Further Maths specification | Insert from svg/FAS1MatricesInvariantLinesBridgeSVG-001.svg | Purpose: Compare scalar multiplication of a vector in ordinary Maths with matrix transformation in Further Maths.]

[VISUAL PLACEHOLDER: FAS1MatricesInvariantLinesTikZ-001 | Source: CCEA FAS1-MAT specification boundary | Insert from tikz/FAS1MatricesInvariantLinesTikZ-001.tex | Purpose: Provide a precise coordinate diagram for the transformation \(A=\begin{pmatrix}2&1\\3&0\end{pmatrix}\), showing invariant lines \(y=x\) and \(y=-3x\).]

---

# 10. Interactive Learning Widgets

[INTERACTIVE PLACEHOLDER: FAS1MatricesInvariantLinesWidget-001 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FAS1MatricesInvariantLinesWidget-001.html | Purpose: Let the student enter a \(2\times2\) matrix and a gradient \(m\), then test whether \(y=mx\) is invariant.]

The widget displays \(x'=x(a+bm)\), \(y'=x(c+dm)\), and checks whether \(y'=mx'\).

[INTERACTIVE PLACEHOLDER: FAS1MatricesInvariantLinesWidget-002 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FAS1MatricesInvariantLinesWidget-002.html | Purpose: Let the student choose a point and see its image under a matrix transformation, with invariant points highlighted.]

The widget computes

\[
\begin{pmatrix}x'\\y'\end{pmatrix}
=
\begin{pmatrix}a&b\\c&d\end{pmatrix}
\begin{pmatrix}x\\y\end{pmatrix}.
\]

[INTERACTIVE PLACEHOLDER: FAS1MatricesInvariantLinesWidget-003 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FAS1MatricesInvariantLinesWidget-003.html | Purpose: Let the student enter a \(2\times2\) matrix and see determinant, area scale factor, orientation effect and singular/non-singular status.]

---

# 11. Worked Examples

## Worked Example 1: Applying a \(2\times2\) transformation to a point

**Question.** The transformation \(T\) is represented by

\[
A=\begin{pmatrix}2&-1\\3&4\end{pmatrix}.
\]

Find the image of \(P(5,-2)\).

Write

\[
\mathbf p=\begin{pmatrix}5\\-2\end{pmatrix}.
\]

Then

\[
A\mathbf p
=
\begin{pmatrix}2&-1\\3&4\end{pmatrix}
\begin{pmatrix}5\\-2\end{pmatrix}.
\]

First component:

\[
2(5)+(-1)(-2)=10+2=12.
\]

Second component:

\[
3(5)+4(-2)=15-8=7.
\]

Therefore

\[
A\mathbf p=\begin{pmatrix}12\\7\end{pmatrix}.
\]

So the image is

\[
\boxed{P'(12,7)}.
\]

## Worked Example 2: Finding invariant points

**Question.** The transformation \(T\) is represented by

\[
A=\begin{pmatrix}3&2\\-1&0\end{pmatrix}.
\]

Find the invariant points.

For an invariant point:

\[
\begin{pmatrix}3&2\\-1&0\end{pmatrix}
\begin{pmatrix}x\\y\end{pmatrix}
=
\begin{pmatrix}x\\y\end{pmatrix}.
\]

Multiply:

\[
\begin{pmatrix}3x+2y\\-x\end{pmatrix}
=
\begin{pmatrix}x\\y\end{pmatrix}.
\]

Equate components:

\[
3x+2y=x,
\]

\[
-x=y.
\]

From the second equation,

\[
y=-x.
\]

Substitute into the first equation:

\[
3x+2(-x)=x.
\]

\[
3x-2x=x.
\]

\[
x=x.
\]

This is always true once \(y=-x\). Therefore the invariant points form the line

\[
\boxed{y=-x}.
\]

Check:

\[
\begin{pmatrix}3&2\\-1&0\end{pmatrix}
\begin{pmatrix}x\\-x\end{pmatrix}
=
\begin{pmatrix}3x-2x\\-x\end{pmatrix}
=
\begin{pmatrix}x\\-x\end{pmatrix}.
\]

## Worked Example 3: Finding invariant lines through the origin

**Question.** The transformation \(T\) is represented by

\[
A=\begin{pmatrix}2&1\\3&0\end{pmatrix}.
\]

Find the invariant lines through the origin.

Let the line be \(y=mx\). A general point is

\[
\begin{pmatrix}x\\mx\end{pmatrix}.
\]

Transform:

\[
A\begin{pmatrix}x\\mx\end{pmatrix}
=
\begin{pmatrix}2x+mx\\3x\end{pmatrix}.
\]

So

\[
x'=x(2+m),
\qquad
 y'=3x.
\]

For invariance:

\[
y'=mx'.
\]

Therefore

\[
3x=m[x(2+m)].
\]

For \(x\neq0\):

\[
3=m(2+m).
\]

\[
3=2m+m^2.
\]

\[
m^2+2m-3=0.
\]

\[
(m+3)(m-1)=0.
\]

So

\[
m=-3\quad\text{or}\quad m=1.
\]

The invariant lines are

\[
\boxed{y=-3x}
\quad\text{and}\quad
\boxed{y=x}.
\]

Check \(x=0\): since \(b=1\neq0\), \(x=0\) is not invariant.

## Worked Example 4: A vertical invariant line

**Question.** The transformation \(T\) is represented by

\[
A=\begin{pmatrix}2&0\\1&3\end{pmatrix}.
\]

Show that \(x=0\) is invariant.

A general point on \(x=0\) is

\[
\begin{pmatrix}0\\y\end{pmatrix}.
\]

Apply the matrix:

\[
A\begin{pmatrix}0\\y\end{pmatrix}
=
\begin{pmatrix}2&0\\1&3\end{pmatrix}
\begin{pmatrix}0\\y\end{pmatrix}
=
\begin{pmatrix}0\\3y\end{pmatrix}.
\]

The image still has first coordinate \(0\), so it lies on \(x=0\). Therefore

\[
\boxed{x=0\text{ is invariant}.}
\]

It is not a line of invariant points except at the origin, because \((0,3y)=(0,y)\) requires \(3y=y\), hence \(y=0\).

## Worked Example 5: Determinant and area scale factor

**Question.**

\[
A=\begin{pmatrix}4&-2\\1&3\end{pmatrix}.
\]

\[
\det A=4(3)-(-2)(1)=12-(-2)=14.
\]

Thus the area scale factor is \(14\), and orientation is preserved.

\[
\boxed{\det A=14.}
\]

## Worked Example 6: Zero determinant and singular matrix

**Question.**

\[
A=\begin{pmatrix}6&-3\\4&-2\end{pmatrix}.
\]

\[
\det A=6(-2)-(-3)(4)=-12-(-12)=0.
\]

So \(A\) is singular.

Now

\[
A\begin{pmatrix}x\\y\end{pmatrix}
=
\begin{pmatrix}6x-3y\\4x-2y\end{pmatrix}.
\]

Let the image coordinates be \((X,Y)\):

\[
X=6x-3y=3(2x-y),
\]

\[
Y=4x-2y=2(2x-y).
\]

So

\[
\frac{X}{3}=\frac{Y}{2}.
\]

Cross-multiply:

\[
2X=3Y.
\]

Thus

\[
Y=\frac{2}{3}X.
\]

The plane is collapsed onto

\[
\boxed{y=\frac{2}{3}x}.
\]

## Worked Example 7: Full exam-style synthesis

**Question.**

\[
A=\begin{pmatrix}1&2\\2&1\end{pmatrix}.
\]

1. Find the invariant lines through the origin.  
2. Determine whether either invariant line is a line of invariant points.  
3. Calculate \(\det A\) and interpret its meaning.

Let \(y=mx\). A general point is \(\begin{pmatrix}x\\mx\end{pmatrix}\).

\[
A\begin{pmatrix}x\\mx\end{pmatrix}
=
\begin{pmatrix}x+2mx\\2x+mx\end{pmatrix}
=
\begin{pmatrix}x(1+2m)\\x(2+m)\end{pmatrix}.
\]

For invariance:

\[
x(2+m)=m[x(1+2m)].
\]

For \(x\neq0\):

\[
2+m=m(1+2m).
\]

\[
2+m=m+2m^2.
\]

\[
2=2m^2.
\]

\[
m^2=1.
\]

So \(m=1\) or \(m=-1\). The invariant lines are

\[
\boxed{y=x}
\quad\text{and}\quad
\boxed{y=-x}.
\]

Check whether \(y=x\) is a line of invariant points:

\[
A\begin{pmatrix}x\\x\end{pmatrix}
=
\begin{pmatrix}3x\\3x\end{pmatrix}.
\]

This is equal to \(\begin{pmatrix}x\\x\end{pmatrix}\) only when \(3x=x\), so \(x=0\). Thus only the origin is fixed.

Check whether \(y=-x\) is a line of invariant points:

\[
A\begin{pmatrix}x\\-x\end{pmatrix}
=
\begin{pmatrix}-x\\x\end{pmatrix}.
\]

This is equal to \(\begin{pmatrix}x\\-x\end{pmatrix}\) only when \(-x=x\), so \(x=0\). Thus only the origin is fixed.

Finally,

\[
\det A=1(1)-2(2)=1-4=-3.
\]

So the area scale factor is \(3\), and orientation is reversed.

---

# 12. Common Mistakes and Exam Traps

## 12.1 Confusing invariant lines with invariant points

An invariant line means points on it remain on it. It does not mean every point on it is fixed.

## 12.2 Forgetting to use a general point

For \(y=mx\), use

\[
\begin{pmatrix}x\\mx\end{pmatrix},
\]

not just one numerical point.

## 12.3 Setting \(A\mathbf{x}=\mathbf{x}\) when the question asks for invariant lines

\(A\mathbf{x}=\mathbf{x}\) finds invariant points, not all invariant lines.

## 12.4 Forgetting the vertical line \(x=0\)

The equation \(y=mx\) misses vertical lines. Check \(x=0\) separately.

## 12.5 Mixing up rows and columns

The image of \(\mathbf{i}\) is the first column of the matrix. The image of \(\mathbf{j}\) is the second column.

## 12.6 Determinant sign trap

If \(\det A=-5\), the area scale factor is \(5\), not \(-5\). The negative sign means orientation is reversed.

## 12.7 Determinant zero trap

\(\det A=0\) does not mean the transformation has no effect. It means area collapses to zero and the matrix is singular.

## 12.8 Off-spec method trap: eigenvalues and eigenvectors

Do not use \(\det(A-\lambda I)=0\) as the main CCEA method in this lesson. Use the direct transformation method.

## 12.9 Using decimals too early

Keep gradients exact, for example \(m=-\frac12\), rather than using unnecessary decimals.

## 12.10 Losing the final interpretation sentence

For determinant questions, write both the determinant and its interpretation.

---

# 13. Practice Questions

These are generated on-spec practice questions. They are not past-paper or textbook questions.

## 13.1 Basic fluency questions

### Question 1

\[
A=\begin{pmatrix}2&3\\-1&4\end{pmatrix}.
\]

Find the image of \(P(1,-2)\).

### Question 2

\[
B=\begin{pmatrix}5&1\\2&-3\end{pmatrix}.
\]

Calculate \(\det B\). State the area scale factor and whether orientation is preserved or reversed.

### Question 3

\[
C=\begin{pmatrix}1&0\\4&1\end{pmatrix}.
\]

Show that \(x=0\) is invariant.

## 13.2 Bridge questions

### Question 4

\[
3\begin{pmatrix}2\\-1\end{pmatrix}=\begin{pmatrix}6\\-3\end{pmatrix}.
\]

Now let

\[
A=\begin{pmatrix}3&0\\0&3\end{pmatrix}.
\]

Find \(A\begin{pmatrix}2\\-1\end{pmatrix}\). Explain why this matrix behaves like scalar multiplication by \(3\).

### Question 5

\[
A=\begin{pmatrix}1&2\\0&1\end{pmatrix}.
\]

Find the image of \(\begin{pmatrix}x\\y\end{pmatrix}\). Explain how the \(x\)-coordinate changes.

## 13.3 Standard exam-style questions

### Question 6

\[
A=\begin{pmatrix}2&1\\0&3\end{pmatrix}.
\]

Find all invariant points.

### Question 7

\[
A=\begin{pmatrix}0&2\\1&1\end{pmatrix}.
\]

Find the invariant lines through the origin.

### Question 8

\[
A=\begin{pmatrix}3&-1\\6&-2\end{pmatrix}.
\]

Show that \(A\) is singular and find the line onto which the plane is mapped.

## 13.4 Harder synthesis questions

### Question 9

\[
A=\begin{pmatrix}4&2\\-1&1\end{pmatrix}.
\]

Find the invariant lines, determine whether either line is a line of invariant points, and interpret \(\det A\).

### Question 10

\[
A=\begin{pmatrix}1&k\\0&2\end{pmatrix}.
\]

Find the image of a general point on \(x=0\), determine the value of \(k\) for which \(x=0\) is invariant, and for \(k=0\) find the invariant lines through the origin.

### Question 11

\[
A=\begin{pmatrix}p&2\\2&p\end{pmatrix}.
\]

Show that \(y=x\) and \(y=-x\) are invariant for every value of \(p\), then find the values of \(p\) for which \(A\) is singular.

---

# 14. Worked Solutions

## Solution 1

\[
A\begin{pmatrix}1\\-2\end{pmatrix}
=
\begin{pmatrix}2&3\\-1&4\end{pmatrix}
\begin{pmatrix}1\\-2\end{pmatrix}
=
\begin{pmatrix}2-6\\-1-8\end{pmatrix}
=
\begin{pmatrix}-4\\-9\end{pmatrix}.
\]

\[
\boxed{P'(-4,-9)}.
\]

## Solution 2

\[
\det B=5(-3)-1(2)=-15-2=-17.
\]

Area scale factor:

\[
|-17|=17.
\]

Since \(\det B<0\), orientation is reversed.

## Solution 3

A general point on \(x=0\) is \(\begin{pmatrix}0\\y\end{pmatrix}\).

\[
C\begin{pmatrix}0\\y\end{pmatrix}
=
\begin{pmatrix}1&0\\4&1\end{pmatrix}
\begin{pmatrix}0\\y\end{pmatrix}
=
\begin{pmatrix}0\\y\end{pmatrix}.
\]

So \(x=0\) is invariant and is a line of invariant points.

## Solution 4

\[
\begin{pmatrix}3&0\\0&3\end{pmatrix}
\begin{pmatrix}2\\-1\end{pmatrix}
=
\begin{pmatrix}6\\-3\end{pmatrix}.
\]

This is the same as scalar multiplication by \(3\), because

\[
\begin{pmatrix}3&0\\0&3\end{pmatrix}=3I.
\]

## Solution 5

\[
\begin{pmatrix}1&2\\0&1\end{pmatrix}
\begin{pmatrix}x\\y\end{pmatrix}
=
\begin{pmatrix}x+2y\\y\end{pmatrix}.
\]

Thus \(x'=x+2y\), and \(y'=y\). The \(y\)-coordinate is unchanged, while the \(x\)-coordinate increases by \(2y\).

## Solution 6

Invariant points satisfy

\[
\begin{pmatrix}2&1\\0&3\end{pmatrix}
\begin{pmatrix}x\\y\end{pmatrix}
=
\begin{pmatrix}x\\y\end{pmatrix}.
\]

So

\[
\begin{pmatrix}2x+y\\3y\end{pmatrix}
=
\begin{pmatrix}x\\y\end{pmatrix}.
\]

Hence

\[
2x+y=x,
\]

\[
3y=y.
\]

From \(3y=y\):

\[
2y=0,
\]

so \(y=0\). Then \(2x=x\), so \(x=0\). The only invariant point is \((0,0)\).

## Solution 7

Let \(y=mx\). Transform \(\begin{pmatrix}x\\mx\end{pmatrix}\):

\[
\begin{pmatrix}0&2\\1&1\end{pmatrix}
\begin{pmatrix}x\\mx\end{pmatrix}
=
\begin{pmatrix}2mx\\x+mx\end{pmatrix}.
\]

For invariance:

\[
x(1+m)=m(2mx).
\]

For \(x\neq0\):

\[
1+m=2m^2.
\]

\[
2m^2-m-1=0.
\]

\[
(2m+1)(m-1)=0.
\]

So \(m=-\frac12\) or \(m=1\). Since \(b=2\neq0\), \(x=0\) is not invariant.

\[
\boxed{y=x\quad\text{and}\quad y=-\frac12x}.
\]

## Solution 8

\[
\det A=3(-2)-(-1)(6)=-6-(-6)=0.
\]

So \(A\) is singular.

\[
A\begin{pmatrix}x\\y\end{pmatrix}
=
\begin{pmatrix}3x-y\\6x-2y\end{pmatrix}.
\]

Let \(X=3x-y\), \(Y=6x-2y\). Since

\[
Y=2(3x-y)=2X,
\]

the plane is mapped onto

\[
\boxed{y=2x}.
\]

## Solution 9

Let \(y=mx\).

\[
\begin{pmatrix}4&2\\-1&1\end{pmatrix}
\begin{pmatrix}x\\mx\end{pmatrix}
=
\begin{pmatrix}x(4+2m)\\x(-1+m)\end{pmatrix}.
\]

For invariance:

\[
-1+m=m(4+2m).
\]

\[
-1+m=4m+2m^2.
\]

\[
2m^2+3m+1=0.
\]

\[
(2m+1)(m+1)=0.
\]

So the invariant lines are

\[
\boxed{y=-\frac12x}
\quad\text{and}\quad
\boxed{y=-x}.
\]

Neither is a line of invariant points except at the origin:

\[
A\begin{pmatrix}x\\-x\end{pmatrix}=\begin{pmatrix}2x\\-2x\end{pmatrix},
\]

and

\[
A\begin{pmatrix}x\\-\frac12x\end{pmatrix}=\begin{pmatrix}3x\\-\frac32x\end{pmatrix}.
\]

Finally,

\[
\det A=4(1)-2(-1)=4+2=6.
\]

Areas are enlarged by scale factor \(6\), and orientation is preserved.

## Solution 10

A general point on \(x=0\) is \(\begin{pmatrix}0\\y\end{pmatrix}\).

\[
\begin{pmatrix}1&k\\0&2\end{pmatrix}
\begin{pmatrix}0\\y\end{pmatrix}
=
\begin{pmatrix}ky\\2y\end{pmatrix}.
\]

For \(x=0\) to be invariant, we need \(ky=0\) for every \(y\), so

\[
\boxed{k=0}.
\]

For \(k=0\),

\[
A=\begin{pmatrix}1&0\\0&2\end{pmatrix}.
\]

Let \(y=mx\):

\[
A\begin{pmatrix}x\\mx\end{pmatrix}=\begin{pmatrix}x\\2mx\end{pmatrix}.
\]

For invariance:

\[
2mx=mx.
\]

So \(m=0\), giving \(y=0\). Since \(b=0\), \(x=0\) is also invariant.

\[
\boxed{y=0\quad\text{and}\quad x=0}.
\]

## Solution 11

For \(y=x\):

\[
A\begin{pmatrix}x\\x\end{pmatrix}
=
\begin{pmatrix}p&2\\2&p\end{pmatrix}
\begin{pmatrix}x\\x\end{pmatrix}
=
\begin{pmatrix}(p+2)x\\(p+2)x\end{pmatrix}.
\]

The image still lies on \(y=x\).

For \(y=-x\):

\[
A\begin{pmatrix}x\\-x\end{pmatrix}
=
\begin{pmatrix}(p-2)x\\(2-p)x\end{pmatrix}
=
\begin{pmatrix}(p-2)x\\-(p-2)x\end{pmatrix}.
\]

The image still lies on \(y=-x\).

For singularity:

\[
\det A=p^2-4.
\]

Set

\[
p^2-4=0.
\]

\[
(p-2)(p+2)=0.
\]

So

\[
\boxed{p=2\text{ or }p=-2}.
\]

---

# 15. Exam Technique Notes

1. Write points as column vectors before multiplying.
2. For invariant points, use \(A\begin{pmatrix}x\\y\end{pmatrix}=\begin{pmatrix}x\\y\end{pmatrix}\).
3. For invariant lines through the origin, use \(y=mx\), transform \(\begin{pmatrix}x\\mx\end{pmatrix}\), then impose \(y'=mx'\).
4. Always check \(x=0\) separately.
5. Keep gradients exact.
6. Interpret determinant using full sentences.
7. Do not use \(\det(A-\lambda I)=0\) as the main CCEA method in this lesson.

---

# 16. Syllabus Gap Check

## 16.1 LO coverage table

| LO ID | Coverage in this lesson | Coverage status |
|---|---|---|
| `FAS1-MAT-LO003` | Identity and zero matrices defined; identity used conceptually as “unchanged”. | Covered |
| `FAS1-MAT-LO004` | Matrix transformation \(A\begin{pmatrix}x\\y\end{pmatrix}\) taught and practised. | Covered |
| `FAS1-MAT-LO006` | Invariant points and invariant lines taught with multiple examples. | Covered |
| `FAS1-MAT-LO007` | \(2\times2\) determinants calculated repeatedly. | Partly covered |
| `FAS1-MAT-LO008` | Determinant interpreted as area scale factor. | Covered |
| `FAS1-MAT-LO009` | Zero determinant interpreted as area collapse. | Covered |
| `FAS1-MAT-LO010` | Singular/non-singular matrices linked to determinant zero/non-zero. | Covered |

## 16.2 Evidence coverage table

| Evidence type | Status | Limitation |
|---|---|---|
| CCEA Further Maths specification map | Used as core boundary | Exact source text is project source rather than pasted in the user message. |
| Further Maths module map | Used for naming and workflow | No extra matrix examples supplied there. |
| Evidence checklist | Used for QA | No lesson-specific CCEA worked examples supplied. |
| Uploaded transcript | Used only for off-spec logging and visual intuition | FP2 eigenvalue content is not treated as CCEA core. |
| Screenshot PDF | Logged visually | No parsed text; visible pages show FP2 matrix algebra/eigenvalue material. |
| Ordinary Maths bridge | Used only as bridge context | Does not override Further Maths scope. |
| CCEA textbook/past-paper examples | Not supplied | All practice questions in this lesson are generated and labelled as generated. |

## 16.3 Bridge coverage table

| Bridge area | Used in lesson? | How |
|---|---:|---|
| Vectors | Yes | Column vectors and transformations. |
| Scalar multiplication | Yes | Compared with diagonal scalar matrix \(3I\). |
| Straight-line equations | Yes | \(y=mx\), \(x=0\), invariant line tests. |
| Simultaneous equations | Yes | Invariant points. |
| Graph transformations | Yes | Conceptual bridge to whole-plane transformations. |
| GCSE area | Yes | Determinant as area scale factor. |

## 16.4 Off-Spec Content Found but Excluded

The uploaded evidence contains FP2 material on eigenvalues, eigenvectors, characteristic equations, normalised eigenvectors, complex eigenvalues, \(3\times3\) eigenvalues and eigenvectors, diagonalising matrices, symmetric matrix diagonalisation and Cayley-Hamilton theorem.

This material is not taught as core in this CCEA FAS1 lesson.

## 16.5 Optional Enrichment Not Required by CCEA

| Enrichment item | Why it may be useful | Why it is not core here |
|---|---|---|
| Eigenvectors | Gives a more advanced way to describe invariant directions. | Not in the CCEA FAS1 matrix boundary used for this lesson. |
| Eigenvalues | Describes scaling along invariant directions. | Not required for CCEA invariant-line method here. |
| Characteristic equation | Finds eigenvalues algebraically. | Off-spec for this CCEA lesson. |
| Matrix visualiser | Helps visualise plane transformations. | External enrichment, not CCEA authority. |
| Diagonalisation | Powerful later linear algebra idea. | Not in lesson boundary. |
| Cayley-Hamilton theorem | Interesting theorem about square matrices. | Not in lesson boundary. |

## 16.6 Weak evidence warnings

- The screenshot PDF is image-only in the current tool context, so no full text extraction was available.
- The uploaded transcript is cross-board FP2 evidence, not CCEA specification evidence.
- No CCEA-specific worked examples were supplied for invariant lines.
- All practice questions are generated, not past-paper questions.

## 16.7 Missing evidence log

| Missing evidence | Impact |
|---|---|
| CCEA textbook worked examples for `FAS1-MAT-LO006` | Could improve board-style examples. |
| CCEA mark schemes for invariant-line questions | Could improve exact mark allocation and wording. |
| CCEA-specific teaching transcript | Would reduce reliance on generated examples. |
| Full visual extraction from the uploaded screenshot PDF | Would allow richer source-backed visual descriptions. |

---

# 17. Recommended Enhancements Not in the Evidence

These are AI-proposed enhancements. They are not claimed as evidence-backed CCEA diagrams.

## 17.1 Diagrams

1. A unit square and its transformed parallelogram, labelled with \(\mathbf{i},\mathbf{j},A\mathbf{i},A\mathbf{j}\).
2. An invariant-line diagram showing \(P\mapsto P'\), where \(P\neq P'\), but both lie on the same line.
3. A line of invariant points diagram showing \(P\mapsto P\).
4. A singular matrix diagram showing the plane collapsing onto a line.

## 17.2 Animations

1. Animate a grid under \(\begin{pmatrix}1&2\\0&1\end{pmatrix}\) to show shear.
2. Animate a grid under \(\begin{pmatrix}2&0\\0&2\end{pmatrix}\) to show scalar enlargement.
3. Animate a singular matrix collapsing the plane onto a line.

## 17.3 Widgets

1. Invariant-line tester using \(c+dm=m(a+bm)\).
2. Point image calculator showing \((x,y)\mapsto(ax+by,cx+dy)\).
3. Determinant area-scale checker.

## 17.4 Extra examples

1. A question where the only invariant point is the origin.
2. A question where a whole line is fixed point-by-point.
3. A question with exactly two invariant lines, neither fixed point-by-point.
4. A question where \(x=0\) is the only non-horizontal invariant line.
5. A question with determinant \(-1\), showing area preserved but orientation reversed.

## 17.5 Bridge visuals

1. Scalar multiplication versus matrix transformation.
2. Straight-line equation before and after transformation.
3. Simultaneous-equation solution types linked to invariant-point sets.

---

# 18. Supplementary Sources Used

## Project sources used

- CCEA GCE Further Mathematics Specification Map.
- Further Maths README module map.
- Further Maths Evidence Drop Checklist.
- Further Maths Portal Build Knowledge Evidence.
- Ordinary A-Level Maths Bridge Spec Extracts.
- CCEA GCE Mathematics Specification Map.

## Lesson-specific evidence used

- `transcripts.md`: used as cross-board FP2 evidence. It supplied eigenvalue/eigenvector explanations, characteristic-equation methods and invariant-line intuition. The off-spec methods were excluded from the CCEA core lesson.
- `Chapter_5_Matrix_Algebra_♾️_(Further_Pure_2)_screenshots.pdf`: used only as visual evidence of the uploaded FP2 chapter structure and transformation diagrams. The PDF was image-only in the current context, so no unseen diagram detail was claimed.

## Ordinary A-Level Maths bridge sources used

Ordinary A-Level Maths bridge sources were used only for vector notation, scalar multiples, straight-line equations, simultaneous equations, graph transformation intuition and area scale-factor intuition. They were not used as authority for Further Mathematics scope.

## Cross-board source notes

The uploaded FP2 transcript and screenshots are useful, but the source uses FP2/CP1 terminology and includes eigenvalues, eigenvectors, diagonalisation and Cayley-Hamilton. Those items were treated as cross-board/off-spec enrichment for this CCEA FAS1 lesson.

## Evidence limitations

- No CCEA lesson transcript was supplied.
- No CCEA textbook worked examples were supplied.
- No CCEA mark scheme extract was supplied.
- The screenshot PDF had no parsed text available in the current context.

---

# 19. Final Student Checklist

## 19.1 Prerequisite confidence checklist

- [ ] Write a point \((x,y)\) as a column vector \(\begin{pmatrix}x\\y\end{pmatrix}\).
- [ ] Multiply a \(2\times2\) matrix by a \(2\times1\) column vector.
- [ ] Solve simple simultaneous equations.
- [ ] Substitute \(y=mx\) into expressions.
- [ ] Factorise quadratics such as \(m^2+2m-3\).
- [ ] Use exact fractions instead of unnecessary decimals.

## 19.2 Further Maths method checklist

- [ ] Apply \(\begin{pmatrix}a&b\\c&d\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix}=\begin{pmatrix}ax+by\\cx+dy\end{pmatrix}\).
- [ ] Find invariant points using \(A\mathbf{x}=\mathbf{x}\).
- [ ] Find invariant lines through the origin using \(y=mx\).
- [ ] Transform \(\begin{pmatrix}x\\mx\end{pmatrix}\).
- [ ] Use the condition \(y'=mx'\).
- [ ] Check \(x=0\) separately.
- [ ] Distinguish between an invariant line and a line of invariant points.

## 19.3 Determinant checklist

- [ ] Calculate \(\det\begin{pmatrix}a&b\\c&d\end{pmatrix}=ad-bc\).
- [ ] Interpret \(|\det A|\) as the area scale factor.
- [ ] Explain that \(\det A<0\) reverses orientation.
- [ ] Explain that \(\det A=0\) means the matrix is singular.
- [ ] Recognise that determinant zero means area collapses to zero.

## 19.4 Exam technique checklist

- [ ] Show enough matrix multiplication working to earn method marks.
- [ ] Use line equations as final answers for invariant lines.
- [ ] Avoid claiming a whole line is fixed when it is only invariant.
- [ ] Avoid using off-spec eigenvalue methods in a CCEA FAS1 matrix question.
- [ ] Write determinant interpretation in a full sentence.
- [ ] Check signs carefully in \(ad-bc\).

## 19.5 Visual understanding checklist

- [ ] Explain how a matrix moves a point.
- [ ] Explain how a matrix moves a grid.
- [ ] Explain why an invariant line can contain moving points.
- [ ] Explain why a line of invariant points is stronger than an invariant line.
- [ ] Explain why \(\det A=0\) collapses a plane shape into zero area.
