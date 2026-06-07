# FAS1 Vectors Lesson

# 1. Lesson Title and Metadata

| Field | Value |
|---|---|
| Date generated | 2026-06-04 |
| Course | CCEA GCE Further Mathematics |
| Unit | FAS1: Further AS 1 Pure Mathematics |
| Applied section | Pure, not applied |
| Topic code | FAS1-VEC |
| Topic name | Vectors |
| Topic slug | vectors |
| Topic Pascal | Vectors |
| Topic ID | FAS1Vectors |
| Lesson file name | FAS1_vectors_lesson.md |
| LO IDs | FAS1-VEC-LO001, FAS1-VEC-LO002, FAS1-VEC-LO003, FAS1-VEC-LO004, FAS1-VEC-LO005, FAS1-VEC-LO006, FAS1-VEC-LO007, FAS1-VEC-LO008, FAS1-VEC-LO009, FAS1-VEC-LO010, FAS1-VEC-LO011, FAS1-VEC-LO012 |
| Bridge tags | ordinary_vectors, coordinate_geometry, magnitude_direction, position_vectors, dot_product_recap, determinants_bridge |
| Topic tags | vectors_3d, scalar_product, vector_product, cross_product, triple_scalar_product, lines_3d, planes, skew_lines, distances, areas, volumes |

This lesson is written for a first-time independent Further Mathematics student. It is CCEA-boundary controlled. Cross-board lesson evidence from `FP1-Chp1-Vectors.pdf`, `transcripts.md`, and `screenshots.pdf` is used only where the CCEA FAS1-VEC specification confirms the content is on-spec.

# 2. Evidence Map

| Source | Use in lesson | Limitation |
|---|---|---|
| `CCEA_GCE_Further_Mathematics_Specification_Map.md` | Determines FAS1-VEC learning outcomes and boundary | Highest authority |
| `Further_Maths_README_module_map.md` | Confirms topic identity and lesson-pack workflow | Project authority |
| `Further_Maths_EVIDENCE_DROP_CHECKLIST.md` | Controls evidence priority and off-spec logging | Project authority |
| `Ordinary_A_Level_Maths_Bridge_Spec_Extracts.md` | Ordinary A-Level Mathematics bridge only | Does not override Further Maths |
| `CCEA_GCE_Mathematics_Specification_Map.md` | Ordinary AS1 vector bridge only | Bridge context only |
| `FP1-Chp1-Vectors.pdf` | Main readable lesson evidence for cross product, areas, volumes, lines, planes, intersections and distances | Cross-board source, used only where on-spec |
| `transcripts.md` | Teacher explanations, right-hand rule, screw analogy, quick method, warnings and worked examples | Informal speech is converted into clean lesson prose |
| `screenshots.pdf` | Visual support for slide sequence, handwritten sign table and determinant/quick-column method | Image-only, partly unclear, no hidden detail claimed |

# 3. Specification Alignment

| LO ID | Official CCEA Further Maths outcome | Lesson coverage |
|---|---|---|
| FAS1-VEC-LO001 | use vectors in three dimensions, including \(\mathbf{i}\), \(\mathbf{j}\) and \(\mathbf{k}\) unit vectors | 3D vectors, unit vectors, direction cosines and the \(\mathbf i,\mathbf j,\mathbf k\) sign cycle |
| FAS1-VEC-LO002 | demonstrate understanding of and use the vector and Cartesian forms of an equation of a straight line in 3D | \(\mathbf r=\mathbf a+\lambda\mathbf b\), Cartesian line form and \((\mathbf r-\mathbf a)\times\mathbf b=\mathbf0\) |
| FAS1-VEC-LO003 | demonstrate understanding of and use the vector and Cartesian forms of the equation of a plane | Parametric, normal and Cartesian plane forms |
| FAS1-VEC-LO004 | calculate the scalar product and use it to express the equation of a plane, and to calculate the angle between two lines, the angle between two planes and the angle between a line and a plane | Scalar product recap, normal form of plane and angle formulae |
| FAS1-VEC-LO005 | check whether vectors are perpendicular by using the scalar product | Dot-product checks throughout |
| FAS1-VEC-LO006 | find the intersection of two lines or a line and a plane | Simultaneous vector equations and substitution into plane equations |
| FAS1-VEC-LO007 | demonstrate understanding of and work with skew lines | Definition and shortest-distance formula |
| FAS1-VEC-LO008 | calculate the perpendicular distance between two lines, from a point to a line and from a point to a plane | Point-plane, point-line and skew-line distance formulae |
| FAS1-VEC-LO009 | find the equation of the line of intersection of two planes | Direction \(\mathbf n_1\times\mathbf n_2\) and a point satisfying both planes |
| FAS1-VEC-LO010 | calculate the vector product of two vectors, including link to a \(3\times3\) determinant | Component, determinant and quick-column methods |
| FAS1-VEC-LO011 | demonstrate understanding of and use the properties of the vector product | Non-commutativity, perpendicularity, zero product and sign cycle |
| FAS1-VEC-LO012 | interpret \(\lVert\mathbf a\times\mathbf b\rVert\) as an area and \(\mathbf a\cdot(\mathbf b\times\mathbf c)\) as a volume | Triangle/parallelogram areas and parallelepiped/tetrahedron volumes |

# 4. Learning Objectives

By the end of this lesson, you should be able to calculate vector products, explain their direction using the right-hand rule, use determinant and component methods, find areas and volumes, write equations of 3D lines and planes, solve intersection problems, and calculate distances involving points, lines, planes and skew lines.

# 5. Explicit Prerequisite Recap

You need GCSE Pythagoras, trigonometry, triangle area \(\frac12ab\sin C\), prism and pyramid volume, and simultaneous equations. From ordinary A-Level Mathematics, you should know two-dimensional vectors, position vectors, magnitudes, directions and coordinate geometry.

### A-Level Maths Bridge: What You Already Know and What Further Maths Changes

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| CCEA AS1 Vectors bridge context | Vectors in two dimensions using \(\mathbf i,\mathbf j\), magnitude, direction and position vectors | Vectors now live in three dimensions using \(\mathbf i,\mathbf j,\mathbf k\), with normals, planes and cross products | Forgetting the zero \(\mathbf k\)-component can change the result |
| CCEA AS1 Coordinate Geometry bridge context | Lines, intersections and perpendicularity in the coordinate plane | Vector equations describe 3D lines and planes | A 2D gradient does not describe a 3D plane |
| GCSE/ordinary trig and geometry | \(\frac12ab\sin C\), prism volume and pyramid volume | \(\lVert\mathbf a\times\mathbf b\rVert\) becomes area; \(\mathbf a\cdot(\mathbf b\times\mathbf c)\) becomes volume | Vectors for area/volume must usually be from the same vertex |
| Determinant skill | Expanding determinants | Cross product and scalar triple product use determinant structures | The middle determinant sign is a major trap |

In ordinary A-Level Maths, vectors mainly described displacement, magnitude and direction. In Further Maths, the same idea becomes a 3D construction toolkit. The key upgrade is that the cross product creates a vector perpendicular to two others. The danger is that ordinary multiplication habits become risky because \(\mathbf a\times\mathbf b\neq\mathbf b\times\mathbf a\).

# 6. Big Picture Explanation

This topic exists because three-dimensional geometry becomes slow if every question is solved by raw simultaneous equations. The cross product turns two directions into a normal direction:

\[
\mathbf a,\mathbf b\quad\longmapsto\quad \mathbf a\times\mathbf b.
\]

Once a perpendicular direction is available, it can be used to find normals to planes, directions of lines of intersection, shortest distances between skew lines, areas of parallelograms, and volumes of solids.

# 7. Key Definitions and Notation

A 3D vector may be written as

\[
\mathbf a=a_1\mathbf i+a_2\mathbf j+a_3\mathbf k=
\begin{pmatrix}a_1\\a_2\\a_3\end{pmatrix}.
\]

Its magnitude is

\[
|\mathbf a|=\sqrt{a_1^2+a_2^2+a_3^2}.
\]

A unit vector in the direction of \(\mathbf a\ne\mathbf0\) is

\[
\hat{\mathbf a}=\frac{\mathbf a}{|\mathbf a|}.
\]

The scalar product is

\[
\mathbf a\cdot\mathbf b=|\mathbf a||\mathbf b|\cos\theta.
\]

The vector product is

\[
\boxed{\mathbf a\times\mathbf b=|\mathbf a||\mathbf b|\sin\theta\,\hat{\mathbf n}},
\]

where \(\hat{\mathbf n}\) is a unit vector perpendicular to both \(\mathbf a\) and \(\mathbf b\).

A line through point \(\mathbf a\), direction \(\mathbf b\), is

\[
\mathbf r=\mathbf a+\lambda\mathbf b.
\]

A plane through point \(\mathbf a\), normal \(\mathbf n\), is

\[
\mathbf r\cdot\mathbf n=\mathbf a\cdot\mathbf n=p.
\]

The scalar triple product is

\[
\mathbf a\cdot(\mathbf b\times\mathbf c).
\]

# 8. Core Theory

## 8.1 Dot product versus cross product

The dot product outputs a scalar. The cross product outputs a vector. Dot product is normally the better tool for angles; cross product is the better tool for perpendicular vectors, areas, normals and volume.

The vector \(\mathbf a\times\mathbf b\) is perpendicular to both input vectors, so

\[
\mathbf a\cdot(\mathbf a\times\mathbf b)=0,\qquad
\mathbf b\cdot(\mathbf a\times\mathbf b)=0.
\]

The cross product is not commutative:

\[
\boxed{\mathbf b\times\mathbf a=-\mathbf a\times\mathbf b.}
\]

## 8.2 Unit-vector sign cycle

Parallel unit vectors cross to zero:

\[
\mathbf i\times\mathbf i=\mathbf j\times\mathbf j=\mathbf k\times\mathbf k=\mathbf0.
\]

The positive cycle is

\[
\boxed{\mathbf i\times\mathbf j=\mathbf k,\qquad
\mathbf j\times\mathbf k=\mathbf i,\qquad
\mathbf k\times\mathbf i=\mathbf j.}
\]

Reversing the order reverses the sign:

\[
\boxed{\mathbf j\times\mathbf i=-\mathbf k,\qquad
\mathbf k\times\mathbf j=-\mathbf i,\qquad
\mathbf i\times\mathbf k=-\mathbf j.}
\]

## 8.3 Component formula for the cross product

Let

\[
\mathbf a=\begin{pmatrix}a_1\\a_2\\a_3\end{pmatrix},\qquad
\mathbf b=\begin{pmatrix}b_1\\b_2\\b_3\end{pmatrix}.
\]

Then

\[
\boxed{
\mathbf a\times\mathbf b=
\begin{pmatrix}
a_2b_3-a_3b_2\\
a_3b_1-a_1b_3\\
a_1b_2-a_2b_1
\end{pmatrix}.}
\]

This comes from expanding

\[
(a_1\mathbf i+a_2\mathbf j+a_3\mathbf k)\times(b_1\mathbf i+b_2\mathbf j+b_3\mathbf k)
\]

and replacing each \(\mathbf i,\mathbf j,\mathbf k\) product using the sign cycle.

## 8.4 Determinant form

\[
\boxed{
\mathbf a\times\mathbf b=
\begin{vmatrix}
\mathbf i&\mathbf j&\mathbf k\\
a_1&a_2&a_3\\
b_1&b_2&b_3
\end{vmatrix}.}
\]

Expanding along the top row gives

\[
\mathbf i\begin{vmatrix}a_2&a_3\\b_2&b_3\end{vmatrix}
-\mathbf j\begin{vmatrix}a_1&a_3\\b_1&b_3\end{vmatrix}
+\mathbf k\begin{vmatrix}a_1&a_2\\b_1&b_2\end{vmatrix}.
\]

The middle term is negative. Keep that sign visible until the final column vector is written.

## 8.5 Worked example: \(\mathbf a=2\mathbf i-3\mathbf j\), \(\mathbf b=4\mathbf i+\mathbf j-\mathbf k\)

Write

\[
\mathbf a=\begin{pmatrix}2\\-3\\0\end{pmatrix},\qquad
\mathbf b=\begin{pmatrix}4\\1\\-1\end{pmatrix}.
\]

Then

\[
\mathbf a\times\mathbf b=
\begin{pmatrix}
(-3)(-1)-0(1)\\
0(4)-2(-1)\\
2(1)-(-3)(4)
\end{pmatrix}
=
\begin{pmatrix}3\\2\\14\end{pmatrix}.
\]

Check:

\[
\begin{pmatrix}2\\-3\\0\end{pmatrix}\cdot\begin{pmatrix}3\\2\\14\end{pmatrix}=6-6+0=0,
\]

and

\[
\begin{pmatrix}4\\1\\-1\end{pmatrix}\cdot\begin{pmatrix}3\\2\\14\end{pmatrix}=12+2-14=0.
\]

So the vector is perpendicular to both original vectors.

## 8.6 Unit vector perpendicular to two vectors

For

\[
\mathbf a=\begin{pmatrix}4\\3\\2\end{pmatrix},\qquad
\mathbf b=\begin{pmatrix}8\\3\\3\end{pmatrix},
\]

calculate

\[
\mathbf a\times\mathbf b=
\begin{pmatrix}3\\4\\-12\end{pmatrix}.
\]

Its magnitude is

\[
\sqrt{3^2+4^2+(-12)^2}=13.
\]

So a unit vector perpendicular to both is

\[
\boxed{\frac1{13}\begin{pmatrix}3\\4\\-12\end{pmatrix}.}
\]

The opposite vector is also valid.

## 8.7 Cross product magnitude and sine

Taking magnitudes of

\[
\mathbf a\times\mathbf b=|\mathbf a||\mathbf b|\sin\theta\,\hat{\mathbf n}
\]

gives

\[
|\mathbf a\times\mathbf b|=|\mathbf a||\mathbf b|\sin\theta,
\]

so

\[
\sin\theta=\frac{|\mathbf a\times\mathbf b|}{|\mathbf a||\mathbf b|}.
\]

Use this with caution because sine is ambiguous: \(\sin\theta=\sin(180^\circ-\theta)\). Dot product is usually better when the actual angle is wanted.

## 8.8 Area of a triangle and parallelogram

Since

\[
|\mathbf a\times\mathbf b|=|\mathbf a||\mathbf b|\sin\theta,
\]

and the ordinary triangle formula is

\[
A=\frac12ab\sin C,
\]

we get

\[
\boxed{A_{\triangle}=\frac12|\mathbf a\times\mathbf b|.}
\]

A parallelogram is two congruent triangles, so

\[
\boxed{A_{\text{parallelogram}}=|\mathbf a\times\mathbf b|.}
\]

If points \(A,B,C\) have position vectors \(\mathbf a,\mathbf b,\mathbf c\), then

\[
\boxed{A_{ABC}=\frac12| (\mathbf b-\mathbf a)\times(\mathbf c-\mathbf a)|.}
\]

## 8.9 Worked area examples

For triangle \(OAB\), where

\[
\overrightarrow{OA}=\begin{pmatrix}1\\-1\\0\end{pmatrix},\qquad
\overrightarrow{OB}=\begin{pmatrix}3\\4\\-6\end{pmatrix},
\]

\[
\overrightarrow{OA}\times\overrightarrow{OB}=\begin{pmatrix}6\\6\\7\end{pmatrix},
\]

so

\[
A=\frac12\sqrt{6^2+6^2+7^2}=\frac12\sqrt{121}=\boxed{\frac{11}{2}}.
\]

For parallelogram \(ABCD\), with

\[
\overrightarrow{AB}=\begin{pmatrix}4\\3\\-2\end{pmatrix},\qquad
\overrightarrow{AD}=\begin{pmatrix}12\\6\\-5\end{pmatrix},
\]

\[
\overrightarrow{AB}\times\overrightarrow{AD}=\begin{pmatrix}-3\\-4\\-12\end{pmatrix},
\]

and

\[
A=\sqrt{9+16+144}=\boxed{13}.
\]

## 8.10 Scalar triple product

The scalar triple product is

\[
\boxed{\mathbf a\cdot(\mathbf b\times\mathbf c).}
\]

It can be written as

\[
\boxed{
\mathbf a\cdot(\mathbf b\times\mathbf c)=
\begin{vmatrix}
a_1&a_2&a_3\\
b_1&b_2&b_3\\
c_1&c_2&c_3
\end{vmatrix}.}
\]

Cyclic reordering keeps the same value:

\[
\mathbf a\cdot(\mathbf b\times\mathbf c)=\mathbf b\cdot(\mathbf c\times\mathbf a)=\mathbf c\cdot(\mathbf a\times\mathbf b).
\]

Reversing order changes the sign.

## 8.11 Volumes

The volume of a parallelepiped is

\[
\boxed{V=|\mathbf a\cdot(\mathbf b\times\mathbf c)|.}
\]

The volume of a tetrahedron is

\[
\boxed{V=\frac16|\mathbf a\cdot(\mathbf b\times\mathbf c)|.}
\]

The factor \(\frac16\) comes from \(\frac12\) for the triangular base and \(\frac13\) for the pyramid volume.

The vectors must all come from the same vertex. If four points are given, choose one point and subtract it from the other three.

### Worked parallelepiped volume

For

\[
\mathbf a=\begin{pmatrix}2\\0\\3\end{pmatrix},\quad
\mathbf b=\begin{pmatrix}1\\4\\3\end{pmatrix},\quad
\mathbf c=\begin{pmatrix}-2\\1\\7\end{pmatrix},
\]

\[
V=\left|\begin{vmatrix}2&0&3\\1&4&3\\-2&1&7\end{vmatrix}\right|.
\]

Expanding along the first row:

\[
2\begin{vmatrix}4&3\\1&7\end{vmatrix}-0\begin{vmatrix}1&3\\-2&7\end{vmatrix}+3\begin{vmatrix}1&4\\-2&1\end{vmatrix}
=2(25)+3(9)=77.
\]

So

\[
\boxed{V=77}.
\]

### Worked tetrahedron volume

For vertices

\[
P=(1,2,3),\quad A=(2,0,4),\quad B=(-1,4,0),\quad C=(2,5,5),
\]

choose \(P\) as common vertex:

\[
\overrightarrow{PA}=\begin{pmatrix}1\\-2\\1\end{pmatrix},\quad
\overrightarrow{PB}=\begin{pmatrix}-2\\2\\-3\end{pmatrix},\quad
\overrightarrow{PC}=\begin{pmatrix}1\\3\\2\end{pmatrix}.
\]

\[
\overrightarrow{PB}\times\overrightarrow{PC}=\begin{pmatrix}13\\1\\-8\end{pmatrix}.
\]

Then

\[
\overrightarrow{PA}\cdot(\overrightarrow{PB}\times\overrightarrow{PC})=
\begin{pmatrix}1\\-2\\1\end{pmatrix}\cdot\begin{pmatrix}13\\1\\-8\end{pmatrix}=13-2-8=3.
\]

Thus

\[
V=\frac16|3|=\boxed{\frac12}.
\]

## 8.12 Direction cosines

For

\[
\mathbf a=\begin{pmatrix}x\\y\\z\end{pmatrix},
\]

with angles \(\alpha,\beta,\gamma\) to the positive \(x,y,z\) axes,

\[
\cos\alpha=\frac{x}{|\mathbf a|},\qquad
\cos\beta=\frac{y}{|\mathbf a|},\qquad
\cos\gamma=\frac{z}{|\mathbf a|}.
\]

Hence

\[
\hat{\mathbf a}=\begin{pmatrix}\cos\alpha\\\cos\beta\\\cos\gamma\end{pmatrix}
\]

and

\[
\boxed{\cos^2\alpha+\cos^2\beta+\cos^2\gamma=1.}
\]

If a component is negative, the corresponding direction cosine is negative.

## 8.13 Equations of lines

A line through \(\mathbf a\) with direction \(\mathbf b\) is

\[
\boxed{\mathbf r=\mathbf a+\lambda\mathbf b.}
\]

Since

\[
\mathbf r-\mathbf a=\lambda\mathbf b,
\]

\(\mathbf r-\mathbf a\) is parallel to \(\mathbf b\), and therefore

\[
\boxed{(\mathbf r-\mathbf a)\times\mathbf b=\mathbf0.}
\]

Equivalently,

\[
\boxed{\mathbf r\times\mathbf b=\mathbf a\times\mathbf b.}
\]

The Cartesian line form is

\[
\boxed{\frac{x-a_1}{b_1}=\frac{y-a_2}{b_2}=\frac{z-a_3}{b_3}.}
\]

Do not divide by zero. If a direction component is zero, that coordinate is fixed.

### Worked line example

Through \((1,2,-1)\) and \((3,-2,2)\):

\[
\mathbf a=\begin{pmatrix}1\\2\\-1\end{pmatrix},\qquad
\mathbf b=\begin{pmatrix}3\\-2\\2\end{pmatrix}-\begin{pmatrix}1\\2\\-1\end{pmatrix}=\begin{pmatrix}2\\-4\\3\end{pmatrix}.
\]

So

\[
\boxed{\mathbf r=\begin{pmatrix}1\\2\\-1\end{pmatrix}+\lambda\begin{pmatrix}2\\-4\\3\end{pmatrix}.}
\]

Cartesian form:

\[
\boxed{\frac{x-1}{2}=\frac{y-2}{-4}=\frac{z+1}{3}.}
\]

Cross-product form:

\[
\boxed{\left(\mathbf r-\begin{pmatrix}1\\2\\-1\end{pmatrix}\right)\times\begin{pmatrix}2\\-4\\3\end{pmatrix}=\mathbf0.}
\]

## 8.14 Equations of planes

A plane may be written in parametric form as

\[
\boxed{\mathbf r=\mathbf a+\lambda\mathbf b+\mu\mathbf c.}
\]

If \(\mathbf n\) is a normal vector, then

\[
(\mathbf r-\mathbf a)\cdot\mathbf n=0,
\]

so

\[
\boxed{\mathbf r\cdot\mathbf n=\mathbf a\cdot\mathbf n=p.}
\]

If two non-parallel vectors \(\mathbf b\) and \(\mathbf c\) lie in the plane, then a normal vector is

\[
\boxed{\mathbf n=\mathbf b\times\mathbf c.}
\]

### Worked plane through a line and a point

Let the line be

\[
\mathbf r=\begin{pmatrix}3\\5\\-2\end{pmatrix}+\lambda\begin{pmatrix}-1\\2\\-1\end{pmatrix},
\]

and the extra point be

\[
\mathbf a=\begin{pmatrix}4\\3\\1\end{pmatrix}.
\]

One vector in the plane is the line direction:

\[
\mathbf d=\begin{pmatrix}-1\\2\\-1\end{pmatrix}.
\]

Another is

\[
\begin{pmatrix}4\\3\\1\end{pmatrix}-\begin{pmatrix}3\\5\\-2\end{pmatrix}=\begin{pmatrix}1\\-2\\3\end{pmatrix}.
\]

The normal is

\[
\mathbf n=\begin{pmatrix}-1\\2\\-1\end{pmatrix}\times\begin{pmatrix}1\\-2\\3\end{pmatrix}=\begin{pmatrix}4\\2\\0\end{pmatrix}.
\]

Then

\[
p=\begin{pmatrix}4\\3\\1\end{pmatrix}\cdot\begin{pmatrix}4\\2\\0\end{pmatrix}=22.
\]

So

\[
\boxed{\mathbf r\cdot\begin{pmatrix}4\\2\\0\end{pmatrix}=22}
\]

or

\[
\boxed{4x+2y=22.}
\]

## 8.15 Intersections

For two lines

\[
l_1:\mathbf r=\mathbf a+\lambda\mathbf b,\qquad
l_2:\mathbf r=\mathbf c+\mu\mathbf d,
\]

set

\[
\mathbf a+\lambda\mathbf b=\mathbf c+\mu\mathbf d
\]

and compare all three components.

For a line and plane, substitute

\[
\mathbf r=\mathbf a+\lambda\mathbf b
\]

into

\[
\mathbf r\cdot\mathbf n=p.
\]

For two planes

\[
\Pi_1:\mathbf r\cdot\mathbf n_1=p_1,\qquad
\Pi_2:\mathbf r\cdot\mathbf n_2=p_2,
\]

the direction of their intersection line is

\[
\boxed{\mathbf n_1\times\mathbf n_2.}
\]

Then find one point satisfying both plane equations.

## 8.16 Distances

Distance from point \(\mathbf s\) to plane \(\mathbf r\cdot\mathbf n=p\):

\[
\boxed{d=\frac{|\mathbf s\cdot\mathbf n-p|}{|\mathbf n|}.}
\]

Distance from point \(\mathbf s\) to line \(\mathbf r=\mathbf a+\lambda\mathbf b\):

\[
\boxed{d=\frac{|(\mathbf s-\mathbf a)\times\mathbf b|}{|\mathbf b|}.}
\]

For skew lines

\[
l_1:\mathbf r=\mathbf a+\lambda\mathbf b,
\qquad
l_2:\mathbf r=\mathbf c+\mu\mathbf d,
\]

the shortest distance is

\[
\boxed{d=\frac{|(\mathbf a-\mathbf c)\cdot(\mathbf b\times\mathbf d)|}{|\mathbf b\times\mathbf d|}.}
\]

Skew lines are not parallel and do not intersect.

### Worked skew-line example

For

\[
l_1:\mathbf r=\mathbf i+\lambda(\mathbf j+\mathbf k),
\]

and

\[
l_2:\mathbf r=-\mathbf i+3\mathbf j-\mathbf k+\mu(2\mathbf i-\mathbf j-\mathbf k),
\]

we have

\[
\mathbf a=\begin{pmatrix}1\\0\\0\end{pmatrix},\quad
\mathbf b=\begin{pmatrix}0\\1\\1\end{pmatrix},\quad
\mathbf c=\begin{pmatrix}-1\\3\\-1\end{pmatrix},\quad
\mathbf d=\begin{pmatrix}2\\-1\\-1\end{pmatrix}.
\]

Then

\[
\mathbf a-\mathbf c=\begin{pmatrix}2\\-3\\1\end{pmatrix},
\qquad
\mathbf b\times\mathbf d=\begin{pmatrix}0\\2\\-2\end{pmatrix}.
\]

The numerator is

\[
\left|\begin{pmatrix}2\\-3\\1\end{pmatrix}\cdot\begin{pmatrix}0\\2\\-2\end{pmatrix}\right|=|-8|=8.
\]

The denominator is

\[
\sqrt{0^2+2^2+(-2)^2}=\sqrt8=2\sqrt2.
\]

So

\[
\boxed{d=\frac8{2\sqrt2}=2\sqrt2.}
\]

## 8.17 Angles

Angle between two lines with direction vectors \(\mathbf b,\mathbf d\):

\[
\boxed{\cos\theta=\frac{|\mathbf b\cdot\mathbf d|}{|\mathbf b||\mathbf d|}}
\]

for the acute angle.

Angle between two planes with normals \(\mathbf n_1,\mathbf n_2\):

\[
\boxed{\cos\theta=\frac{|\mathbf n_1\cdot\mathbf n_2|}{|\mathbf n_1||\mathbf n_2|}.}
\]

Angle \(\phi\) between a line direction \(\mathbf b\) and a plane normal \(\mathbf n\):

\[
\boxed{\sin\phi=\frac{|\mathbf b\cdot\mathbf n|}{|\mathbf b||\mathbf n|}.}
\]

# 9. Visual Asset Integration

[VISUAL PLACEHOLDER: FAS1VectorsMermaid-001 | Source: Lesson PDF chapter overview, page route map and CCEA FAS1-VEC syllabus boundary | Insert from mermaid/FAS1VectorsMermaid-001.md | Purpose: Show how the topic descends from cross product to areas, triple scalar product, line equations and applications.]

[VISUAL PLACEHOLDER: FAS1VectorsBridgeSVG-001 | Source: Ordinary A-Level Maths bridge + Further Maths specification | Insert from svg/FAS1VectorsBridgeSVG-001.svg | Purpose: Compare prior ordinary Maths vector methods with Further Maths vector-product extensions.]

[VISUAL PLACEHOLDER: FAS1VectorsSVG-001 | Source: Lesson PDF Vector/Cross Product slide + teacher transcript + screenshot visual evidence | Insert from svg/FAS1VectorsSVG-001.svg | Purpose: Show why \(\mathbf a\times\mathbf b\) and \(\mathbf b\times\mathbf a\) point in opposite directions.]

[VISUAL PLACEHOLDER: FAS1VectorsTikZ-001 | Source: Lesson PDF important results slide + screenshot sign-cycle table | Insert from tikz/FAS1VectorsTikZ-001.tex | Purpose: Teach the \(\mathbf i,\mathbf j,\mathbf k\) cross-product sign cycle and zero results.]

[VISUAL PLACEHOLDER: FAS1VectorsSVG-002 | Source: Lesson PDF determinant method + screenshot quick column method | Insert from svg/FAS1VectorsSVG-002.svg | Purpose: Show the determinant expansion and highlight the negative middle component.]

[VISUAL PLACEHOLDER: FAS1VectorsSVG-003 | Source: Lesson PDF area of triangle/parallelogram section | Insert from svg/FAS1VectorsSVG-003.svg | Purpose: Show \(|\mathbf a\times\mathbf b|\) as parallelogram area and \(\frac12|\mathbf a\times\mathbf b|\) as triangle area.]

[VISUAL PLACEHOLDER: FAS1VectorsTikZ-002 | Source: Lesson PDF volume of parallelepiped/tetrahedron section + teacher transcript | Insert from tikz/FAS1VectorsTikZ-002.tex | Purpose: Show parallelepiped and tetrahedron volume from three vectors from the same vertex.]

[VISUAL PLACEHOLDER: FAS1VectorsSVG-004 | Source: Lesson PDF vector equation of line section | Insert from svg/FAS1VectorsSVG-004.svg | Purpose: Show why \((\mathbf r-\mathbf a)\times\mathbf b=\mathbf0\) represents a line.]

[VISUAL PLACEHOLDER: FAS1VectorsTikZ-003 | Source: Lesson PDF plane examples | Insert from tikz/FAS1VectorsTikZ-003.tex | Purpose: Show how two vectors in a plane generate a normal vector through their cross product.]

[VISUAL PLACEHOLDER: FAS1VectorsTikZ-004 | Source: Lesson PDF line of intersection example + teacher transcript | Insert from tikz/FAS1VectorsTikZ-004.tex | Purpose: Show why the line of intersection of two planes has direction \(\mathbf n_1\times\mathbf n_2\).]

[VISUAL PLACEHOLDER: FAS1VectorsTikZ-005 | Source: Lesson PDF shortest distance section + teacher transcript | Insert from tikz/FAS1VectorsTikZ-005.tex | Purpose: Show the shortest-distance formula between two skew lines using projection onto \(\mathbf b\times\mathbf d\).]

[VISUAL PLACEHOLDER: FAS1VectorsSVG-005 | Source: Lesson PDF direction cosine note + CCEA FAS1-VEC 3D vector boundary | Insert from svg/FAS1VectorsSVG-005.svg | Purpose: Show \(\cos\alpha,\cos\beta,\cos\gamma\) as components of a unit vector.]

# 10. Interactive Learning Widgets

[INTERACTIVE PLACEHOLDER: FAS1VectorsWidget-001 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FAS1VectorsWidget-001.html | Purpose: Practise calculating \(\mathbf a\times\mathbf b\), expanding the determinant and checking perpendicularity.]

[INTERACTIVE PLACEHOLDER: FAS1VectorsWidget-002 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FAS1VectorsWidget-002.html | Purpose: Connect cross-product magnitude with area and scalar triple product with volume.]

[INTERACTIVE PLACEHOLDER: FAS1VectorsWidget-003 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FAS1VectorsWidget-003.html | Purpose: Help students choose between dot product, cross product, scalar triple product and simultaneous equations.]

[INTERACTIVE PLACEHOLDER: FAS1VectorsWidget-004 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FAS1VectorsWidget-004.html | Purpose: Practise direction cosines and the identity \(\cos^2\alpha+\cos^2\beta+\cos^2\gamma=1\).]

# 11. Worked Examples

The main evidence-backed worked examples are embedded in the theory sections above. They include:

1. calculating \(\mathbf a\times\mathbf b\) for \(2\mathbf i-3\mathbf j\) and \(4\mathbf i+\mathbf j-\mathbf k\);
2. finding a unit vector perpendicular to two vectors;
3. using \(|\mathbf a\times\mathbf b|\) to find the sine of an angle;
4. triangle and parallelogram area examples;
5. scalar triple product and volume examples;
6. equations of lines and planes;
7. line of intersection of two planes;
8. shortest distance between skew lines.

A cross-board worked snippet from the supplied lesson PDF gives

\[
\mathbf b=3\mathbf i-\mathbf j+\mathbf k,
\qquad
\mathbf c=2\mathbf i+\mathbf j-\mathbf k,
\]

so

\[
\mathbf b\times\mathbf c=
\begin{pmatrix}3\\-1\\1\end{pmatrix}\times\begin{pmatrix}2\\1\\-1\end{pmatrix}
=
\begin{pmatrix}0\\5\\5\end{pmatrix}.
\]

A cross-board area snippet gives

\[
\overrightarrow{AC}=3\mathbf i+6\mathbf j+2\mathbf k,
\qquad
\overrightarrow{BC}=-3\mathbf i+4\mathbf j+3\mathbf k,
\]

so

\[
\overrightarrow{AC}\times\overrightarrow{BC}=10\mathbf i-15\mathbf j+30\mathbf k,
\]

and

\[
A_{ABC}=\frac12\sqrt{10^2+(-15)^2+30^2}=\frac12\sqrt{1225}=17.5.
\]

# 12. Common Mistakes and Exam Traps

| Trap | Safe correction |
|---|---|
| Treating \(\mathbf a\times\mathbf b\) as commutative | Use \(\mathbf b\times\mathbf a=-\mathbf a\times\mathbf b\) |
| Losing the \(\mathbf j\)-component sign | Write \(+\mathbf i,-\mathbf j,+\mathbf k\) before simplifying |
| Forgetting zero components | Write all 3 components, including zeros |
| Using \(|\mathbf a\times\mathbf b|\) for triangle area | Use \(\frac12|\mathbf a\times\mathbf b|\) |
| Using \(\frac12|\mathbf a\times\mathbf b|\) for parallelogram area | Use \(|\mathbf a\times\mathbf b|\) |
| Forgetting \(\frac16\) for tetrahedron volume | Tetrahedron is one sixth of the parallelepiped volume |
| Using vectors from different vertices for volume | Choose one common vertex first |
| Forgetting modulus for volume/distance | Volumes and distances are non-negative |
| Treating a 3D line like a 2D gradient line | Use a point and direction vector |
| Confusing line-plane angle with line-normal angle | Use \(\sin\phi=\frac{|\mathbf b\cdot\mathbf n|}{|\mathbf b||\mathbf n|}\) |

# 13. Practice Questions

These are generated practice questions, not past-paper or textbook questions.

1. Evaluate \(\mathbf i\times\mathbf j\), \(\mathbf j\times\mathbf i\), \(\mathbf j\times\mathbf k\), \(\mathbf k\times\mathbf j\), \(\mathbf i\times\mathbf k\), \(\mathbf k\times\mathbf k\).
2. For \(\mathbf a=(1,4,-2)^T\) and \(\mathbf b=(3,-1,5)^T\), find \(\mathbf a\times\mathbf b\) and check perpendicularity.
3. Find a unit vector perpendicular to \((2,-1,3)^T\) and \((1,4,-2)^T\).
4. Find the area of triangle \(ABC\), where \(A=(1,0,2)\), \(B=(4,1,-1)\), \(C=(2,5,3)\).
5. Find the area of parallelogram \(ABCD\), where \(A=(2,-1,0)\), \(B=(5,3,1)\), \(D=(1,2,4)\).
6. Find the volume of the tetrahedron with vertices \(P=(1,0,2)\), \(A=(3,1,0)\), \(B=(0,4,1)\), \(C=(2,2,5)\).
7. Find the volume of the parallelepiped with edge vectors \((1,2,0)^T\), \((3,-1,2)^T\), \((2,1,4)^T\).
8. Find the plane through \((1,2,-1)\), \((3,0,2)\), \((2,5,1)\).
9. Find where \(\mathbf r=(2,-1,0)^T+\lambda(1,3,-2)^T\) meets \(\mathbf r\cdot(2,-1,4)^T=7\).
10. Find the shortest distance between \(\mathbf r=(1,0,2)^T+\lambda(1,2,-1)^T\) and \(\mathbf r=(0,3,1)^T+\mu(2,-1,1)^T\).

# 14. Worked Solutions

## Solution 1

\[
\mathbf i\times\mathbf j=\mathbf k,
\quad
\mathbf j\times\mathbf i=-\mathbf k,
\quad
\mathbf j\times\mathbf k=\mathbf i,
\quad
\mathbf k\times\mathbf j=-\mathbf i,
\quad
\mathbf i\times\mathbf k=-\mathbf j,
\quad
\mathbf k\times\mathbf k=\mathbf0.
\]

## Solution 2

\[
\mathbf a\times\mathbf b=
\begin{pmatrix}4(5)-(-2)(-1)\\(-2)(3)-1(5)\\1(-1)-4(3)\end{pmatrix}
=
\begin{pmatrix}18\\-11\\-13\end{pmatrix}.
\]

Check:

\[
(1,4,-2)\cdot(18,-11,-13)=18-44+26=0,
\]

\[
(3,-1,5)\cdot(18,-11,-13)=54+11-65=0.
\]

## Solution 3

\[
\begin{pmatrix}2\\-1\\3\end{pmatrix}\times\begin{pmatrix}1\\4\\-2\end{pmatrix}
=
\begin{pmatrix}-10\\7\\9\end{pmatrix}.
\]

Magnitude:

\[
\sqrt{100+49+81}=\sqrt{230}.
\]

So the unit vectors are

\[
\boxed{\pm\frac1{\sqrt{230}}\begin{pmatrix}-10\\7\\9\end{pmatrix}.}
\]

## Solution 4

\[
\overrightarrow{AB}=\begin{pmatrix}3\\1\\-3\end{pmatrix},\qquad
\overrightarrow{AC}=\begin{pmatrix}1\\5\\1\end{pmatrix}.
\]

\[
\overrightarrow{AB}\times\overrightarrow{AC}=\begin{pmatrix}16\\-6\\14\end{pmatrix}.
\]

\[
A=\frac12\sqrt{16^2+(-6)^2+14^2}=\frac12\sqrt{488}=\boxed{\sqrt{122}}.
\]

## Solution 5

\[
\overrightarrow{AB}=\begin{pmatrix}3\\4\\1\end{pmatrix},\qquad
\overrightarrow{AD}=\begin{pmatrix}-1\\3\\4\end{pmatrix}.
\]

\[
\overrightarrow{AB}\times\overrightarrow{AD}=\begin{pmatrix}13\\-13\\13\end{pmatrix}.
\]

\[
A=\sqrt{13^2+(-13)^2+13^2}=\boxed{13\sqrt3}.
\]

## Solution 6

Use \(P\) as the common vertex:

\[
\overrightarrow{PA}=\begin{pmatrix}2\\1\\-2\end{pmatrix},\quad
\overrightarrow{PB}=\begin{pmatrix}-1\\4\\-1\end{pmatrix},\quad
\overrightarrow{PC}=\begin{pmatrix}1\\2\\3\end{pmatrix}.
\]

\[
\overrightarrow{PB}\times\overrightarrow{PC}=\begin{pmatrix}14\\2\\-6\end{pmatrix}.
\]

\[
\overrightarrow{PA}\cdot(\overrightarrow{PB}\times\overrightarrow{PC})=28+2+12=42.
\]

\[
V=\frac16|42|=\boxed7.
\]

## Solution 7

\[
\mathbf b\times\mathbf c=
\begin{pmatrix}3\\-1\\2\end{pmatrix}\times\begin{pmatrix}2\\1\\4\end{pmatrix}
=
\begin{pmatrix}-6\\-8\\5\end{pmatrix}.
\]

\[
\mathbf a\cdot(\mathbf b\times\mathbf c)=
\begin{pmatrix}1\\2\\0\end{pmatrix}\cdot\begin{pmatrix}-6\\-8\\5\end{pmatrix}=-22.
\]

\[
V=|-22|=\boxed{22}.
\]

## Solution 8

\[
\overrightarrow{AB}=\begin{pmatrix}2\\-2\\3\end{pmatrix},\qquad
\overrightarrow{AC}=\begin{pmatrix}1\\3\\2\end{pmatrix}.
\]

\[
\overrightarrow{AB}\times\overrightarrow{AC}=\begin{pmatrix}-13\\-1\\8\end{pmatrix}.
\]

Use \(\mathbf n=(13,1,-8)^T\). Then

\[
p=(1,2,-1)\cdot(13,1,-8)=13+2+8=23.
\]

So

\[
\boxed{\mathbf r\cdot\begin{pmatrix}13\\1\\-8\end{pmatrix}=23}
\]

or

\[
\boxed{13x+y-8z=23.}
\]

## Solution 9

A general line point is

\[
\mathbf r=\begin{pmatrix}2+\lambda\\-1+3\lambda\\-2\lambda\end{pmatrix}.
\]

Substitute into the plane:

\[
2(2+\lambda)-(-1+3\lambda)+4(-2\lambda)=7.
\]

\[
4+2\lambda+1-3\lambda-8\lambda=7,
\]

\[
5-9\lambda=7,
\]

\[
\lambda=-\frac29.
\]

Point:

\[
\boxed{\left(\frac{16}{9},-\frac53,\frac49\right)}.
\]

## Solution 10

\[
\mathbf a-\mathbf c=\begin{pmatrix}1\\-3\\1\end{pmatrix},
\]

\[
\mathbf b\times\mathbf d=\begin{pmatrix}1\\2\\-1\end{pmatrix}\times\begin{pmatrix}2\\-1\\1\end{pmatrix}
=\begin{pmatrix}1\\-3\\-5\end{pmatrix}.
\]

\[
(\mathbf a-\mathbf c)\cdot(\mathbf b\times\mathbf d)=1+9-5=5.
\]

\[
|\mathbf b\times\mathbf d|=\sqrt{1+9+25}=\sqrt{35}.
\]

\[
\boxed{d=\frac5{\sqrt{35}}=\frac{\sqrt{35}}7.}
\]

# 15. Exam Technique Notes

Use the dot product for angles and perpendicularity checks. Use the cross product for perpendicular vectors, areas, normals and the direction of line of intersection of planes. Use the scalar triple product for volumes. Show determinant or component working before calculator checks. Keep exact values unless decimals are explicitly requested. Always substitute original points back into plane equations, because a single arithmetic slip can create a convincing wrong plane.

# 16. Syllabus Gap Check

All FAS1-VEC LO IDs are covered:

- FAS1-VEC-LO001: 3D vectors and \(\mathbf i,\mathbf j,\mathbf k\)
- FAS1-VEC-LO002: vector and Cartesian line equations
- FAS1-VEC-LO003: vector and Cartesian plane equations
- FAS1-VEC-LO004: scalar product, plane equation and angles
- FAS1-VEC-LO005: perpendicularity by scalar product
- FAS1-VEC-LO006: intersections of two lines and line-plane
- FAS1-VEC-LO007: skew lines
- FAS1-VEC-LO008: point-plane, point-line and line-line distances
- FAS1-VEC-LO009: line of intersection of two planes
- FAS1-VEC-LO010: vector product and \(3\times3\) determinant
- FAS1-VEC-LO011: properties of vector product
- FAS1-VEC-LO012: areas and volumes

### Off-Spec Content Found but Excluded

Vector triple products of the form \(\mathbf a\times(\mathbf b\times\mathbf c)\) are excluded from the core lesson. Cross-board labels such as FP1, FP3, Core Pure Year 1, Edexcel and Pearson are retained only in source-reference context and not used as CCEA topic identity.

### Missing Evidence Log

Official CCEA past-paper questions and mark schemes were not supplied. Textbook exercise pages referenced in the slides were not supplied. The screenshot PDF is image-only and partially unclear, so it supports visual planning only.

# 17. Recommended Enhancements Not in the Evidence

Recommended enhancements include the decision-tree Mermaid route map, right-hand rule SVG, determinant sign-trap SVG, area SVG, volume TikZ, plane-normal TikZ, skew-distance TikZ and four widgets for cross products, area/volume, method selection and direction cosines. These are AI-proposed teaching assets based on the lesson evidence.

# 18. Supplementary Sources Used

- `CCEA_GCE_Further_Mathematics_Specification_Map.md`
- `Further_Maths_README_module_map.md`
- `Further_Maths_EVIDENCE_DROP_CHECKLIST.md`
- `Further Maths Portal Build – Knowledge Evidence.txt`
- `CCEA_GCE_Mathematics_Specification_Map.md` as bridge context only
- `Ordinary_A_Level_Maths_Bridge_Spec_Extracts.md` as bridge context only
- `FP1-Chp1-Vectors.pdf` as cross-board lesson evidence where on-spec
- `transcripts.md` as teacher explanation evidence
- `screenshots.pdf` as partial visual evidence only

# 19. Final Student Checklist

- [ ] I can write vectors in \(\mathbf i,\mathbf j,\mathbf k\) and column form.
- [ ] I can calculate magnitudes and unit vectors.
- [ ] I can calculate \(\mathbf a\times\mathbf b\) using components or determinants.
- [ ] I remember \(\mathbf b\times\mathbf a=-\mathbf a\times\mathbf b\).
- [ ] I check cross products by dotting with both original vectors.
- [ ] I use \(\frac12|\mathbf a\times\mathbf b|\) for triangles.
- [ ] I use \(|\mathbf a\times\mathbf b|\) for parallelograms.
- [ ] I use \(|\mathbf a\cdot(\mathbf b\times\mathbf c)|\) for parallelepipeds.
- [ ] I use \(\frac16|\mathbf a\cdot(\mathbf b\times\mathbf c)|\) for tetrahedrons.
- [ ] I choose vectors from the same vertex for volume.
- [ ] I can write equations of lines and planes in vector and Cartesian forms.
- [ ] I can find intersections using simultaneous equations or substitution.
- [ ] I can calculate point-plane, point-line and skew-line distances.
- [ ] I can choose the correct angle formula for lines and planes.
- [ ] I keep ordinary A-Level Maths bridge ideas in their proper place and do not let them override CCEA Further Maths.
