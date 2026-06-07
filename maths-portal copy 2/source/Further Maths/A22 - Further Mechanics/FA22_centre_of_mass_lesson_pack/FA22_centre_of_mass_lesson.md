# FA22 Centre of Mass

## 1. Lesson Title and Metadata

| Field | Value |
|---|---|
| Date generated | 2026-06-04 |
| Course | CCEA GCE Further Mathematics |
| Unit | FA22 – Further A2 2 Applied Mathematics |
| Applied section | Section A: Mechanics 1 |
| Topic code | FA22-COM |
| Topic name | Centre of mass |
| Topic slug | centre_of_mass |
| Topic Pascal | CentreOfMass |
| Topic ID | FA22CentreOfMass |
| Lesson file name | FA22_centre_of_mass_lesson.md |
| Core LO IDs | FA22-COM-LO001, FA22-COM-LO002, FA22-COM-LO003, FA22-COM-LO004, FA22-COM-LO005 |
| Bridge tags | A22 Moments; AS2 Forces and Newton’s laws; AS1 Vectors; ordinary coordinate geometry; static equilibrium |
| Topic tags | centre of mass; resultant weight; particles; rods; laminae; composite laminae; suspended laminae; moments; symmetry; frameworks as wires/rods |

This lesson is a CCEA Further Mathematics lesson for **FA22 Centre of mass**. The uploaded lesson source is labelled **Further Mechanics 2: Centres of Mass of Plane Figures**, and the transcript says the chapter only looks at **2D** centre-of-mass situations, with calculus and 3D centre of mass pushed into a later chapter. This maps to **FA22-COM**, not the later **FA22-FCOM Further centre of mass** topic.

The word **framework** in this lesson means a **wire/rod framework for centre of mass**, not CCEA’s separate topic on **light pin-jointed frameworks**.

### Learning Outcome IDs Preserved

- `FA22-COM-LO001`
- `FA22-COM-LO002`
- `FA22-COM-LO003`
- `FA22-COM-LO004`
- `FA22-COM-LO005`

### Boundary Statement

This lesson teaches centre of mass for **systems of particles, rods/wires, standard laminae, composite laminae and suspended laminae**. It does **not** teach calculus derivations, 3D solid bodies, variable density functions, or pin-jointed framework force analysis.

---

## 2. Evidence Map

| Evidence source | Used in lesson? | Role |
|---|---:|---|
| CCEA Further Mathematics specification map | Yes | Core authority for `FA22-COM` and LO IDs. |
| Further Maths module map | Yes | Topic mapping and bridge hints. |
| Further Maths evidence checklist | Yes | Preservation rules, evidence limitations and asset planning. |
| Ordinary A-Level Maths bridge extracts | Yes | Bridge only: moments, vectors, forces, equilibrium. |
| CCEA ordinary Mathematics specification map | Yes | Bridge only: ordinary vectors, forces and moments. |
| `FM2-Chp2-Centres of Mass.pdf` | Yes | Core lesson evidence where on-spec: definitions, formulae, worked examples and diagrams. |
| `transcripts.md` | Yes | Core lesson evidence where on-spec: teacher explanation, warnings and worked-example reasoning. |
| `Chapter_2_Centres_of_Mass_🚗_(Further_Mechanics_2)_screenshots.pdf` | Partially | Visual evidence only. No parsed text was available, so only visible inspected details are claimed. |

### Visual Evidence Limitation

Diagram evidence is partially unclear here. The description below preserves the visible/readable details only. No uninspected visual detail is claimed.

The screenshot PDF is image-based and contains 150 pages. The first rendered pages show the title slide, chair-balancing diagrams, the body/particle/rod/lamina definition table, and the beginning of the particles-on-a-line section. Since the screenshot PDF has no parsed text, the readable PDF and transcript are the main evidence sources for exact wording and formulae.

---

## 3. Specification Alignment

| LO ID | Official wording | Lesson coverage | Evidence source | Boundary |
|---|---|---|---|---|
| `FA22-COM-LO001` | demonstrate understanding of the concept of centre of mass | Defines centre of mass as the single point through which the resultant weight is modelled to act. Explains balancing, collective weight and equilibrium. | CCEA spec map; lesson PDF definitions; transcript intro | No angular acceleration modelling. |
| `FA22-COM-LO002` | find the centre of mass of systems of particles at fixed points and rods, including use of symmetry but excluding use of calculus or variable density problems | Covers particles on a line, particles in a plane, rods/wires and wire frameworks. Uses \(\sum m_i x_i=\bar{x}\sum m_i\) and \(\sum m_i\mathbf r_i=\bar{\mathbf r}\sum m_i\). | Lesson PDF particles pages; transcript videos 1, 2 and 5 | No calculus or variable density functions. |
| `FA22-COM-LO003` | find the centre of mass of rectangular, triangular and circular laminae | Covers rectangles, triangles, symmetry, medians, \(\frac23\) along median, \(\frac13\) from base, circular sectors. | Lesson PDF standard laminae pages; transcript video 3 | Formulae quoted without proof. |
| `FA22-COM-LO004` | find the centre of mass of a composite lamina | Covers splitting into components, mass proportional to area, table method, holes as negative mass, componentwise differing density. | Lesson PDF composite pages; transcript videos 4 and 8 | Component densities allowed; variable density functions excluded. |
| `FA22-COM-LO005` | solve problems involving suspended laminae | Covers freely suspended laminae, \(G\) vertically below pivot, angle questions, two-string suspension using moments. | Lesson PDF lamina equilibrium pages; transcript videos 6 and 7 | Pin-jointed framework force analysis excluded. |

---

## 4. Learning Objectives

### Core Further Maths Objectives

By the end of this lesson, you should be able to:

1. Explain what the centre of mass of a body means in the Further Mechanics model.
2. Distinguish between a particle, rod/beam/wire, lamina and body.
3. Use the moment-balance idea

\[
\sum_{i=1}^{n}m_i x_i=\bar{x}\sum_{i=1}^{n}m_i
\]

to find the centre of mass of particles on a straight line.

4. Extend the method to particles in a plane using

\[
\sum_{i=1}^{n}m_i
\begin{pmatrix}x_i\\y_i\end{pmatrix}
=
\begin{pmatrix}\bar{x}\\\bar{y}\end{pmatrix}
\sum_{i=1}^{n}m_i.
\]

5. Use symmetry to locate the centre of mass of uniform laminae.
6. Find the centre of mass of a triangular lamina using medians, averaged coordinates or the one-third-from-base method.
7. Use standard circular arc and sector centre-of-mass results where they are supplied or allowed.
8. Find the centre of mass of a composite lamina by splitting it into simple parts.
9. Deal with holes by treating the removed part as a negative mass.
10. Find the centre of mass of wire/rod frameworks by using length instead of area.
11. Solve suspended lamina problems by using the fact that \(G\) lies vertically below the point of suspension.
12. Solve two-string suspension problems using moments and vertical equilibrium.

### Bridge Objectives

You should also be able to connect this lesson to ordinary A-Level Maths by:

1. Recognising centre-of-mass equations as moment equations in disguise.
2. Using column vectors without forgetting their physical meaning.
3. Choosing an origin sensibly.
4. Using right-angled trigonometry to find angles in suspended-lamina problems.
5. Taking moments about a point that removes an unwanted tension.

### Exam Technique Objectives

You should be able to:

1. State clearly whether you are using mass, area, length, or mass per unit area/length.
2. Label \(G\), \(\bar{x}\), \(\bar{y}\), masses and distances.
3. Keep units attached to final answers.
4. Avoid using degrees where the formula needs radians.
5. Avoid treating wire frameworks as laminae.
6. Avoid treating a hole as a positive mass.
7. Avoid rotating complicated diagrams when a pivot-to-\(G\) line is enough.

---

## 5. Explicit Prerequisite Recap

### GCSE Foundations

You should already be comfortable with coordinates, positive and negative numbers, midpoints, areas of rectangles/triangles/sectors, right-angled trigonometry, rearranging equations and simultaneous equations.

### Ordinary AS/A2 Mathematics Foundations

You should already have met position vectors and column vectors, resolving horizontal and vertical components, force diagrams and weight \(mg\), equilibrium, moments, and the idea that a model can simplify reality.

### A-Level Maths Bridge: What You Already Know and What Further Maths Changes

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| AS1 Vectors | Coordinates and position vectors can be written as column vectors. | A point mass at \((x_i,y_i)\) can be handled using \(m_i\begin{pmatrix}x_i\\y_i\end{pmatrix}\). | Do not treat the vector equation as pure algebra only; it represents a physical balance of moments. |
| AS2 Forces and Newton’s laws | Weight acts vertically downwards; diagrams show forces and components. | A whole body can be modelled as though its weight acts through one point \(G\). | This is a model. It is useful, but over-simplistic for angular acceleration. |
| A22 Moments | A moment is force multiplied by perpendicular distance. | The centre of mass is found by replacing many weights with one resultant weight at \(G\). | Since each weight is \(m_i g\), the \(g\) cancels. Work with mass unless force is required. |
| A22 Static equilibrium | A body at rest has balanced forces and balanced moments. | A freely suspended lamina rests with \(G\) vertically below the pivot or point of suspension. | If \(G\) is not vertically below the pivot, there is a turning moment. |
| Coordinate geometry | You can choose an origin and measure distances from axes or lines. | Composite lamina questions often become easy if the bottom-left corner is chosen as the origin. | A poor origin choice can make the algebra unnecessarily swampy. |

In ordinary A-Level Maths, this idea appeared as **moments and equilibrium**: forces caused turning effects depending on their perpendicular distances from a point.

In Further Maths, the same idea becomes a way of replacing a spread-out body with a single equivalent particle at \(G\), the centre of mass.

The key upgrade is that we now find that point \(G\) for **particles, laminae, rods, wire frameworks and suspended objects**.

The danger is that old mechanics habits can become too blunt: you must track whether the “mass” you are using comes from an actual mass, an area, a length, a density, or a negative mass representing a hole.

---

## 6. Big Picture Explanation

Centre of mass is the “single-point weight model” for an extended object.

In reality, a body is made from many tiny pieces of matter. Each tiny piece has its own weight acting vertically downwards. In this lesson, we replace all those individual weights by **one resultant weight** acting through one point: the **centre of mass**, usually labelled \(G\).

That single point matters because it tells us where an object balances and how it rests in equilibrium. If a body is suspended from a point, it settles with its centre of mass vertically below the suspension point. If the line of action of the weight is not beneath the support, the body has a turning tendency.

### The One Idea That Runs Through the Whole Topic

\[
\text{sum of moments of individual weights}
=
\text{moment of total weight acting at the centre of mass}.
\]

Because each weight is \(m_i g\), every term contains \(g\). Unless the question specifically requires forces, we usually work with **masses**, not weights:

\[
\sum_{i=1}^{n}m_i x_i
=
\bar{x}\sum_{i=1}^{n}m_i.
\]

For a plane problem:

\[
\sum_{i=1}^{n}m_i
\begin{pmatrix}x_i\\y_i\end{pmatrix}
=
\begin{pmatrix}\bar{x}\\\bar{y}\end{pmatrix}
\sum_{i=1}^{n}m_i.
\]

Particles, loaded plates, laminae, composite shapes, frameworks and suspended laminae all use this same balance idea, just wearing different hats.

### Modelling Context and Assumptions

| Object | Model used |
|---|---|
| Particle | Mass has no dimension and acts at a point. |
| Rod, beam or wire | One-dimensional body; length matters, thickness is ignored. |
| Lamina | Two-dimensional body; thickness is negligible compared with length and width. |
| Uniform lamina | Mass is evenly spread through area. |
| Uniform rod/wire | Mass is evenly spread through length. |
| Body | Any fixed amount of matter. |

A force acting through the centre of mass causes linear acceleration but not angular acceleration in this model. To study angular acceleration properly, you would need to consider the positions of individual particles of mass, which is not part of this lesson.

---

## 7. Key Definitions and Notation

### Body

A **body** is any fixed amount of matter.

### Particle

A **particle** is a mass with no dimension. All its mass is modelled as acting at one point.

### Rod, Beam or Wire

A **rod**, **beam** or **wire** is a one-dimensional body. For a uniform rod, beam or wire, the mass is spread evenly along its length. If the object is straight and uniform, its centre of mass is at its midpoint.

### Lamina

A **lamina** is a two-dimensional body. It can model a piece of paper, card or a metal sheet where thickness is very small compared with the other two dimensions.

### Uniform Lamina

A **uniform lamina** has its mass evenly spread throughout its area. If there is one line of symmetry, the centre of mass lies on that line. If there are two lines of symmetry, the centre of mass lies at their intersection.

### Centre of Mass

The **centre of mass** of a body is the position of the resultant of the weights of the individual particles making up the body. It is the point where we model the body’s whole weight as acting.

We usually label the centre of mass by \(G\). If the coordinates of \(G\) are needed, we write

\[
G=(\bar{x},\bar{y}).
\]

The symbols \(\bar{x}\) and \(\bar{y}\) are pronounced “\(x\)-bar” and “\(y\)-bar”. The bar notation should remind you of an average, but it is a **mass-weighted average**.

### Mass-Weighted Average

For particles with masses \(m_1,m_2,\dots,m_n\) at positions \(x_1,x_2,\dots,x_n\) on a line:

\[
\bar{x}=
\frac{\sum_{i=1}^{n}m_i x_i}{\sum_{i=1}^{n}m_i}.
\]

### Position Vector

For a particle at \((x_i,y_i)\):

\[
\mathbf r_i=\begin{pmatrix}x_i\\y_i\end{pmatrix},
\qquad
\bar{\mathbf r}=\begin{pmatrix}\bar{x}\\\bar{y}\end{pmatrix}.
\]

The vector form is

\[
\sum_{i=1}^{n}m_i\mathbf r_i
=
\bar{\mathbf r}\sum_{i=1}^{n}m_i.
\]

### Mass per Unit Area and Length

For a uniform lamina, if \(\rho\) is mass per unit area:

\[
\text{mass of component}=\rho\times\text{area}.
\]

For a uniform rod, wire or framework, if \(\lambda\) is mass per unit length:

\[
\text{mass of component}=\lambda\times\text{length}.
\]

Common density factors cancel only when they are common to every component.

### Hole or Removed Part

A hole in a lamina is treated as a **negative mass**.

### Suspended Lamina

If a lamina is suspended freely from a point, then in equilibrium its centre of mass lies vertically below the point of suspension.

---

## 8. Core Theory

### 8.1 The Centre-of-Mass Model

\[
\text{many weights at many positions}
\quad\rightsquigarrow\quad
\text{one resultant weight acting through }G.
\]

**Bridge Note:** In ordinary A-Level Maths, a particle’s weight \(mg\) was usually drawn as a single downward force. Here, Further Maths extends this by finding where the single downward force should act for an object that is not actually a particle.

### 8.2 Why \(g\) Cancels

Suppose particles have masses \(m_1,m_2,\dots,m_n\) and lie on a line with coordinates \(x_1,x_2,\dots,x_n\). Their weights are \(m_1g,m_2g,\dots,m_ng\). Taking moments about an origin gives:

\[
m_1g x_1+m_2g x_2+\cdots+m_ng x_n
=
\bar{x}(m_1+m_2+\cdots+m_n)g.
\]

Factor out \(g\):

\[
g(m_1x_1+m_2x_2+\cdots+m_nx_n)
=
\bar{x}g(m_1+m_2+\cdots+m_n).
\]

Divide by \(g\):

\[
m_1x_1+m_2x_2+\cdots+m_nx_n
=
\bar{x}(m_1+m_2+\cdots+m_n).
\]

Using sigma notation:

\[
\sum_{i=1}^{n}m_i x_i=\bar{x}\sum_{i=1}^{n}m_i.
\]

**Bridge Note:** This is still ordinary moments, but the algebra looks like weighted averaging.

### 8.3 Particles on a Straight Line

For \(n\) particles on a line:

\[
\sum_{i=1}^{n}m_i x_i=\bar{x}\sum_{i=1}^{n}m_i,
\qquad
\bar{x}=\frac{\sum m_i x_i}{\sum m_i}.
\]

If a particle lies to the left of the origin, its coordinate is negative and must stay negative.

### 8.4 Particles in a Plane

For particles in a plane, apply the same idea in \(x\) and \(y\):

\[
\bar{x}=\frac{\sum m_i x_i}{\sum m_i},
\qquad
\bar{y}=\frac{\sum m_i y_i}{\sum m_i}.
\]

Together:

\[
\sum m_i
\begin{pmatrix}x_i\\y_i\end{pmatrix}
=
\begin{pmatrix}\bar{x}\\\bar{y}\end{pmatrix}\sum m_i.
\]

**Bridge Note:** In ordinary A-Level vectors, \(\begin{pmatrix}x\\y\end{pmatrix}\) located a point. Here, multiplying by \(m\) turns that point into a mass-weighted point.

### 8.5 Choosing an Origin

Sometimes coordinates are not given. Choose an origin that makes component centres easy to write down. The bottom-left corner usually works for rectangles and grid diagrams.

### 8.6 Loaded Light Plates

A **light** plate has negligible mass. If a light plate has particles attached, ignore the plate and use only the particle masses.

For a light rectangle \(ABCD\), choosing \(A=(0,0)\) with \(AB=20\) and \(AD=50\) gives:

\[
A=(0,0),\quad B=(20,0),\quad C=(20,50),\quad D=(0,50).
\]

With masses \(2,3,5,5\) kg at \(A,B,C,D\):

\[
2\binom00+3\binom{20}0+5\binom{20}{50}+5\binom0{50}
=15\binom{\bar{x}}{\bar{y}}.
\]

Thus

\[
\binom{160}{500}=15\binom{\bar{x}}{\bar{y}},
\qquad
G=\left(\frac{32}{3},\frac{100}{3}\right).
\]

Distance from \(AD\) is \(\frac{32}{3}\) cm and distance from \(AB\) is \(\frac{100}{3}\) cm.

### 8.7 Standard Uniform Laminae

For a uniform lamina:

\[
\text{mass}\propto\text{area}.
\]

If a uniform lamina has a line of symmetry, \(G\) lies on that line. If it has two lines of symmetry, \(G\) lies at their intersection.

### 8.8 Triangular Laminae

For a uniform triangular lamina, the centre of mass is the centroid.

Methods:

1. **Single median:** \(G\) lies \(\frac23\) of the way along a median from a vertex, so \(AG:GM=2:1\).
2. **Intersecting medians:** \(G\) is where medians intersect.
3. **Averaging coordinates:**

\[
G=\left(\frac{x_1+x_2+x_3}{3},\frac{y_1+y_2+y_3}{3}\right).
\]

4. **One-third from the base:** \(G\) lies on a line parallel to the base and \(\frac13\) of the perpendicular height from the base.
5. **Symmetry:** for isosceles/equilateral triangles, use symmetry first.

### 8.9 Circular Sectors as Uniform Laminae

For a uniform sector of radius \(r\) and angle at the centre \(2\alpha\):

\[
d=\frac{2r\sin\alpha}{3\alpha}
\]

from the centre, along the axis of symmetry. The angle \(\alpha\) must be in radians.

### 8.10 Circular Arcs as Wires or Rods

A circular arc is not a lamina. It is a bent rod or wire. For a uniform circular arc of radius \(r\) and angle \(2\alpha\):

\[
d=\frac{r\sin\alpha}{\alpha}
\]

from the centre. Again \(\alpha\) must be in radians.

Do not confuse arcs and sectors.

### 8.11 Composite Laminae

A composite lamina is made from simpler laminae joined together or from a larger lamina with a part removed.

Method:

1. Split the lamina into standard components.
2. Find each component’s centre of mass.
3. Find each component’s mass or mass ratio.
4. Treat each component as a particle at its own centre of mass.
5. Use

\[
\sum m_i\mathbf r_i=\bar{\mathbf r}\sum m_i.
\]

For a uniform lamina, areas can be used as mass ratios.

### 8.12 Composite Laminae with Holes

If a hole is cut out of a lamina, treat the removed part as a negative mass:

\[
M_1\mathbf r_1-M_2\mathbf r_2=(M_1-M_2)\bar{\mathbf r}.
\]

### 8.13 Frameworks, Wires and Rods

In this lesson, a **framework** means a wire/rod shape for centre-of-mass calculation. It does not mean a pin-jointed truss with member forces.

For a uniform framework:

\[
\text{mass}\propto\text{length}.
\]

A straight uniform rod’s centre of mass is at its midpoint. For an arc, use the arc formula and arc length. Diagrams can mislead: a lamina uses **area**, a framework uses **length**.

### 8.14 Non-Uniform Composite Figures

If component \(i\) has area \(A_i\) and mass per unit area \(\rho_i\):

\[
m_i=\rho_i A_i.
\]

If component \(i\) is a wire of length \(L_i\) and mass per unit length \(\lambda_i\):

\[
m_i=\lambda_i L_i.
\]

Do not cancel density factors unless they are common.

### 8.15 Suspended Laminae

When a lamina is suspended freely from a point, \(G\) comes to rest vertically below the suspension point. If \(G\) is not vertically below the suspension point, the weight has a non-zero perpendicular distance from the point and creates a turning moment.

### 8.16 Two-String Suspension

If a body is suspended by two vertical strings:

\[
T_1+T_2=Mg.
\]

Take moments about the point where one tension acts to eliminate that tension. If taking moments about \(F\):

\[
T_A d_A=Mg\,d_G,
\qquad
T_A=\frac{Mg\,d_G}{d_A}.
\]

---

## 9. Visual Asset Integration

[VISUAL PLACEHOLDER: FA22CentreOfMassMermaid-001 | Source: CCEA `FA22-COM` specification boundary + uploaded lesson evidence | Insert from mermaid/FA22CentreOfMassMermaid-001.md | Purpose: Show the whole lesson flow from the centre-of-mass model to particles, laminae, composites, frameworks and suspended laminae.]

[VISUAL PLACEHOLDER: FA22CentreOfMassBridgeMermaid-001 | Source: Ordinary A-Level Maths bridge + Further Maths specification | Insert from mermaid/FA22CentreOfMassBridgeMermaid-001.md | Purpose: Compare prior ordinary Maths method with Further Maths extension.]

[VISUAL PLACEHOLDER: FA22CentreOfMassSVG-001 | Source: `FM2-Chp2-Centres of Mass.pdf`, definitions slide | Insert from svg/FA22CentreOfMassSVG-001.svg | Purpose: Show the difference between particle, rod/beam/wire, lamina and body.]

[VISUAL PLACEHOLDER: FA22CentreOfMassSVG-002 | Source: Screenshot PDF title/intro pages + transcript intro | Insert from svg/FA22CentreOfMassSVG-002.svg | Purpose: Introduce the balancing-point idea using a chair/person line-of-action diagram.]

[VISUAL PLACEHOLDER: FA22CentreOfMassSVG-003 | Source: `FM2-Chp2-Centres of Mass.pdf`, particles on a line example | Insert from svg/FA22CentreOfMassSVG-003.svg | Purpose: Show the worked example of three particles at \(x=3,4,6\) and the centre of mass at \(x=4.4\).]

[VISUAL PLACEHOLDER: FA22CentreOfMassSVG-004 | Source: `FM2-Chp2-Centres of Mass.pdf`, particles in a plane example | Insert from svg/FA22CentreOfMassSVG-004.svg | Purpose: Show weighted points in the coordinate plane and the centre of mass calculation using a column-vector equation.]

[VISUAL PLACEHOLDER: FA22CentreOfMassSVG-005 | Source: `FM2-Chp2-Centres of Mass.pdf`, loaded rectangular plate example | Insert from svg/FA22CentreOfMassSVG-005.svg | Purpose: Show the origin choice and distances from \(AD\) and \(AB\) in the loaded-plate example.]

[VISUAL PLACEHOLDER: FA22CentreOfMassSVG-006 | Source: `FM2-Chp2-Centres of Mass.pdf`, standard uniform laminae slide | Insert from svg/FA22CentreOfMassSVG-006.svg | Purpose: Show how symmetry locates the centre of mass for circles, rectangles and regular polygons.]

[VISUAL PLACEHOLDER: FA22CentreOfMassSVG-007 | Source: `FM2-Chp2-Centres of Mass.pdf`, triangle slides | Insert from svg/FA22CentreOfMassSVG-007.svg | Purpose: Compare triangular lamina methods: median, intersecting medians, coordinate average and one-third-from-base.]

[VISUAL PLACEHOLDER: FA22CentreOfMassSVG-008 | Source: `FM2-Chp2-Centres of Mass.pdf`, sector and arc slides | Insert from svg/FA22CentreOfMassSVG-008.svg | Purpose: Prevent confusion between a sector lamina and a circular arc wire.]

[VISUAL PLACEHOLDER: FA22CentreOfMassSVG-009 | Source: `FM2-Chp2-Centres of Mass.pdf`, composite shapes and holes | Insert from svg/FA22CentreOfMassSVG-009.svg | Purpose: Show two valid approaches to the same L-shaped lamina: split into positive parts or use a large rectangle with a negative hole.]

[VISUAL PLACEHOLDER: FA22CentreOfMassSVG-010 | Source: `FM2-Chp2-Centres of Mass.pdf`, frameworks slide | Insert from svg/FA22CentreOfMassSVG-010.svg | Purpose: Show how a wire framework is split into straight rods and an arc, using length rather than area.]

[VISUAL PLACEHOLDER: FA22CentreOfMassSVG-011 | Source: Transcript video 6 and lesson PDF equilibrium section | Insert from svg/FA22CentreOfMassSVG-011.svg | Purpose: Show why \(G\) must lie vertically below a point of suspension.]

[VISUAL PLACEHOLDER: FA22CentreOfMassTikZ-001 | Source: `FM2-Chp2-Centres of Mass.pdf`, particles on a line example | Insert from tikz/FA22CentreOfMassTikZ-001.tex | Purpose: Create a precise printable mathematical diagram for the \(2,5,3\text{ kg}\) particle system.]

[VISUAL PLACEHOLDER: FA22CentreOfMassTikZ-002 | Source: `FM2-Chp2-Centres of Mass.pdf`, triangle method slides | Insert from tikz/FA22CentreOfMassTikZ-002.tex | Purpose: Show exact geometric relationship \(AG:GM=2:1\) and the one-third-from-base rule.]

[VISUAL PLACEHOLDER: FA22CentreOfMassTikZ-003 | Source: `FM2-Chp2-Centres of Mass.pdf`, composite lamina example | Insert from tikz/FA22CentreOfMassTikZ-003.tex | Purpose: Show the L-shaped lamina on a coordinate grid with component centres.]

[VISUAL PLACEHOLDER: FA22CentreOfMassTikZ-004 | Source: Transcript video 7, two-string suspension | Insert from tikz/FA22CentreOfMassTikZ-004.tex | Purpose: Show vertical tensions, weight through \(G\), and moment distances.]

---

## 10. Interactive Learning Widgets

[INTERACTIVE PLACEHOLDER: FA22CentreOfMassWidget-001 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FA22CentreOfMassWidget-001.html | Purpose: Let students calculate the centre of mass of particles on a line or in a plane using the exact weighted-average method.]

[INTERACTIVE PLACEHOLDER: FA22CentreOfMassWidget-002 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FA22CentreOfMassWidget-002.html | Purpose: Help students build the component table for composite laminae, holes and frameworks.]

[INTERACTIVE PLACEHOLDER: FA22CentreOfMassWidget-003 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FA22CentreOfMassWidget-003.html | Purpose: Let students see why the line from suspension point to \(G\) becomes vertical in equilibrium.]

[INTERACTIVE PLACEHOLDER: FA22CentreOfMassWidget-004 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FA22CentreOfMassWidget-004.html | Purpose: Prevent the two common circular-shape errors: using degrees and confusing arcs with sectors.]

---

## 11. Worked Examples

### Worked Example 1: Centre of Mass of Particles on a Line

A system of three particles with masses \(2\text{ kg}\), \(5\text{ kg}\) and \(3\text{ kg}\) are placed along the \(x\)-axis at \((3,0),(4,0),(6,0)\). Find the centre of mass.

\[
2(3)+5(4)+3(6)=\bar{x}(2+5+3).
\]

\[
6+20+18=10\bar{x}.
\]

\[
44=10\bar{x},\qquad \bar{x}=4.4.
\]

\[
\boxed{G=(4.4,0)}
\]

### Worked Example 2: Unknown Masses on a Line

Particles \(P,Q,R\) lie on the \(x\)-axis. \(P\) has mass \(3.5\text{ kg}\) at \((1,0)\), \(Q\) has mass \(m_1\) at \((-2,0)\), \(R\) has mass \(m_2\) at \((3,0)\). The centre of mass is \((0.3,0)\) and total mass is \(10\text{ kg}\).

\[
3.5(1)+m_1(-2)+m_2(3)=10(0.3).
\]

\[
3.5-2m_1+3m_2=3.
\]

\[
2m_1-3m_2=0.5.
\]

Total mass gives:

\[
3.5+m_1+m_2=10,
\qquad
m_1+m_2=6.5.
\]

So \(m_1=6.5-m_2\). Substitute:

\[
2(6.5-m_2)-3m_2=0.5.
\]

\[
13-5m_2=0.5,
\qquad
-5m_2=-12.5,
\qquad
m_2=2.5.
\]

\[
m_1=6.5-2.5=4.
\]

\[
\boxed{m_1=4\text{ kg},\qquad m_2=2.5\text{ kg}}
\]

### Worked Example 3: Centre of Mass of Particles in a Plane

Find the centre of mass of \(2\text{ kg}\) at \((1,2)\), \(3\text{ kg}\) at \((3,1)\), and \(5\text{ kg}\) at \((4,3)\).

\[
2\binom12+3\binom31+5\binom43=10\binom{\bar{x}}{\bar{y}}.
\]

\[
\binom24+\binom93+\binom{20}{15}=\binom{31}{22}.
\]

\[
\binom{31}{22}=10\binom{\bar{x}}{\bar{y}}.
\]

\[
\binom{\bar{x}}{\bar{y}}=\binom{3.1}{2.2}.
\]

\[
\boxed{G=(3.1,2.2)}
\]

### Worked Example 4: Particles in a Plane with Negative Coordinates

Particles have masses and coordinates:

\[
4\text{ kg at }(-1,3),\quad
2\text{ kg at }(-2,-4),\quad
8\text{ kg at }(4,0),\quad
6\text{ kg at }(1,-3).
\]

Total mass is \(20\). Then

\[
4\binom{-1}{3}+2\binom{-2}{-4}+8\binom40+6\binom1{-3}
=20\binom{\bar{x}}{\bar{y}}.
\]

\[
\binom{-4}{12}+\binom{-4}{-8}+\binom{32}{0}+\binom{6}{-18}
=\binom{30}{-14}.
\]

\[
\binom{\bar{x}}{\bar{y}}=\binom{30/20}{-14/20}=\binom{1.5}{-0.7}.
\]

\[
\boxed{G=(1.5,-0.7)}
\]

### Worked Example 5: Loaded Light Rectangular Plate

A light rectangle has \(AB=20\text{ cm}\), \(AD=50\text{ cm}\). Masses \(2,3,5,5\) kg are attached at \(A,B,C,D\). Choose \(A=(0,0)\). Then:

\[
2\binom00+3\binom{20}0+5\binom{20}{50}+5\binom0{50}=15\binom{\bar{x}}{\bar{y}}.
\]

\[
\binom{160}{500}=15\binom{\bar{x}}{\bar{y}}.
\]

\[
G=\left(\frac{32}{3},\frac{100}{3}\right).
\]

Distance from \(AD\): \(\frac{32}{3}\text{ cm}\). Distance from \(AB\): \(\frac{100}{3}\text{ cm}\).

### Worked Example 6: Unknown \(\lambda\) and \(k\)

Particles of masses \(3m,5m,\lambda m\) are at \((4,0),(0,-3),(4,2)\). The centre of mass is \((2,k)\).

Using \(x\)-coordinates:

\[
3m(4)+5m(0)+\lambda m(4)=2(8+\lambda)m.
\]

\[
12+4\lambda=16+2\lambda,
\qquad
2\lambda=4,
\qquad
\lambda=2.
\]

Using \(y\)-coordinates:

\[
3m(0)+5m(-3)+2m(2)=10mk.
\]

\[
-15m+4m=10mk,
\qquad
-11m=10mk,
\qquad
k=-\frac{11}{10}=-1.1.
\]

### Worked Example 7: Triangle by Averaging Coordinates

For vertices \((3,5),(2,-4),(7,2)\):

\[
G=\left(\frac{3+2+7}{3},\frac{5-4+2}{3}\right)=(4,1).
\]

### Worked Example 8: Right-Angled Triangle Using One-Third Rule

If \(BC=12\), \(AB=10\), and the coordinates in the evidence give the lower-left reference values \(-7\) and \(-4\), then:

\[
\bar{x}=-7+\frac{12}{3}=-3,
\qquad
\bar{y}=-4+\frac{10}{3}=-\frac23.
\]

\[
\boxed{G=\left(-3,-\frac23\right)}
\]

### Worked Example 9: Circular Sector Lamina

A sector has radius \(9\text{ cm}\) and angle \(100^\circ\). Since \(2\alpha=100^\circ\):

\[
\alpha=50^\circ=\frac{5\pi}{18}.
\]

\[
d=\frac{2r\sin\alpha}{3\alpha}
=\frac{2(9)\sin(5\pi/18)}{3(5\pi/18)}
=5.27\text{ cm to 3 s.f.}
\]

### Worked Example 10: Circular Arc Wire

A pole of length \(3\text{ m}\) is bent into an arc of a circle of radius \(3\text{ m}\). If the arc angle is \(2\alpha\), then:

\[
3=3(2\alpha),
\qquad
\alpha=0.5.
\]

\[
d=\frac{r\sin\alpha}{\alpha}=\frac{3\sin(0.5)}{0.5}=2.87655\ldots
\]

Distance from pole:

\[
3-2.87655\ldots=0.12345\text{ m to 5 d.p.}
\]

### Worked Example 11: Composite Lamina by Splitting

For components \((2,4)\) of area \(4\), and \((4,2)\) of area \(12\):

\[
4\binom24+12\binom42=16\binom{\bar{x}}{\bar{y}}.
\]

\[
\binom{8}{16}+\binom{48}{24}=\binom{56}{40}=16\binom{\bar{x}}{\bar{y}}.
\]

\[
G=(3.5,2.5).
\]

### Worked Example 12: Composite Lamina Using a Negative Hole

Large rectangle: centre \((4,3)\), area \(24\). Removed rectangle: centre \((5,4)\), area \(8\). Then:

\[
24\binom43-8\binom54=16\binom{\bar{x}}{\bar{y}}.
\]

\[
\binom{96}{72}-\binom{40}{32}=\binom{56}{40}=16\binom{\bar{x}}{\bar{y}}.
\]

\[
\boxed{G=(3.5,2.5)}
\]

### Worked Example 13: Composite Rectangle and Triangle

Rectangle area \(32\), centre distance \(4\) from \(PT\). Triangle area \(6\), centre distance \(9\) from \(PT\). By symmetry distance from \(PQ\) is \(2\text{ cm}\).

\[
32(4)+6(9)=38\bar{x}.
\]

\[
128+54=38\bar{x},
\qquad
182=38\bar{x},
\qquad
\bar{x}=\frac{91}{19}.
\]

\[
\boxed{\text{Distance from }PT=\frac{91}{19}\text{ cm},\quad \text{distance from }PQ=2\text{ cm}}
\]

### Worked Example 14: Subtracting a Rectangular Hole

Large rectangle area \(32\), centre \((4,2)\). Removed rectangle area \(12\), centre \((5,3)\). Remaining area \(20\).

\[
32\binom42-12\binom53=20\binom{\bar{x}}{\bar{y}}.
\]

\[
\binom{128}{64}-\binom{60}{36}=\binom{68}{28}=20\binom{\bar{x}}{\bar{y}}.
\]

\[
G=(3.4,1.4).
\]

### Worked Example 15: Uniform Wire Framework with an Arc

Components:

- vertical rod: centre \((3,4)\), length \(2\);
- horizontal rod: centre \((4,3)\), length \(2\);
- arc: centre \(\left(3-\frac{4\sqrt2}{3},3-\frac{4\sqrt2}{3}\right)\), length \(3\).

\[
2\binom34+2\binom43+3\binom{3-4\sqrt2/3}{3-4\sqrt2/3}=7\binom{\bar{x}}{\bar{y}}.
\]

\[
\binom68+\binom86+\binom{9-4\sqrt2}{9-4\sqrt2}
=inom{23-4\sqrt2}{23-4\sqrt2}.
\]

\[
\boxed{G=\left(\frac{23-4\sqrt2}{7},\frac{23-4\sqrt2}{7}\right)}
\]

### Worked Example 16: Non-Uniform Framework

If the straight rods have mass per unit length \(2\lambda\) and the arc has \(\lambda\), masses are \(4\lambda,4\lambda,3\lambda\):

\[
4\lambda\binom34+4\lambda\binom43+3\lambda\binom{3-4\sqrt2/3}{3-4\sqrt2/3}=11\lambda\binom{\bar{x}}{\bar{y}}.
\]

\[
\boxed{G=\left(\frac{37-4\sqrt2}{11},\frac{37-4\sqrt2}{11}\right)}
\]

### Worked Example 17: Suspended Lamina from One Point

If the right triangle from suspension point to \(G\) gives equal perpendicular distances \(2.5\) and \(2.5\):

\[
\tan\theta=\frac{2.5}{2.5}=1,
\qquad
\theta=45^\circ.
\]

### Worked Example 18: Suspended Lamina After Adding a Mass

Original lamina mass \(20\) kg, centre \((3.4,1.4)\). Add \(5\) kg at \((8,0)\):

\[
20\binom{3.4}{1.4}+5\binom80=25\binom{\bar{x}}{\bar{y}}.
\]

\[
\binom{68}{28}+\binom{40}{0}=\binom{108}{28}.
\]

\[
G=(4.32,1.12).
\]

Suspending from \(A\):

\[
\theta=\tan^{-1}\left(\frac{1.12}{4.32}\right)=14.5^\circ.
\]

### Worked Example 19: Two-String Suspension

If a lamina of mass \(M\) is suspended by vertical strings at \(A\) and \(F\), and the weight acts through \(G\), taking moments about \(F\) gives:

\[
T_A d_A=Mg\,d_G,
\qquad
T_A=\frac{Mg\,d_G}{d_A}.
\]

Then vertical equilibrium gives:

\[
T_F=Mg-T_A.
\]

### Worked Example 20: Two Vertical Ropes

If \(G\) is horizontally \(\frac{49}{26}a\) from \(A\), and \(AB=5a\), take moments about \(A\):

\[
Mg\left(\frac{49}{26}a\right)=T_B(5a).
\]

Cancel \(a\):

\[
T_B=\frac{49}{130}Mg.
\]

Vertical equilibrium gives:

\[
T_A=Mg-\frac{49}{130}Mg=\frac{81}{130}Mg.
\]

### Worked Example 21: Non-Uniform Folded Cardboard Lamina

Components:

- rectangle: area/mass ratio \(8\), centre \((1,2)\);
- square: area/mass ratio \(4\), centre \((3,1)\);
- folded triangle: geometric area \(2\), double thickness, mass ratio \(4\), centre \(\left(\frac83,\frac23\right)\).

\[
8\binom12+4\binom31+4\binom{8/3}{2/3}=16\binom{\bar{x}}{\bar{y}}.
\]

\[
\binom8{16}+\binom{12}{4}+\binom{32/3}{8/3}
=\binom{92/3}{68/3}.
\]

\[
\bar{x}=\frac{92/3}{16}=\frac{23}{12},
\qquad
\bar{y}=\frac{68/3}{16}=\frac{17}{12}.
\]

\[
\boxed{G=\left(\frac{23}{12},\frac{17}{12}\right)}
\]

### Worked Example 22: Symmetric Lamina for Two-String Tension

If the centre of mass is \(1\text{ cm}\) from the first string and \(4\text{ cm}\) from the second, taking moments about the first string gives:

\[
Mg(1)=T_2(4),
\qquad
T_2=\frac14Mg.
\]

Vertical equilibrium:

\[
T_1+T_2=Mg,
\qquad
T_1=\frac34Mg.
\]

---

## 12. Common Mistakes and Exam Traps

### Mistaking Centre of Mass for Ordinary Average

Centre of mass is a **mass-weighted average**:

\[
\bar{x}=\frac{\sum m_i x_i}{\sum m_i}.
\]

Do not average coordinates unless a special result justifies it, such as the centroid of a uniform triangular lamina.

### Forgetting Negative Coordinates

If a particle is at \(x=-2\), its contribution is \(m(-2)=-2m\), not \(2m\).

### Using Weight \(mg\) Everywhere When Mass Is Enough

Mass is enough for coordinates because \(g\) cancels. But \(g\) must return for forces, weights and tensions.

### Confusing \(2\alpha\) with \(\alpha\)

The formula uses \(\alpha\), where the full angle is \(2\alpha\). If the full angle is \(100^\circ\), then \(\alpha=50^\circ\), then convert to radians.

### Using Degrees in Formulae That Need Radians

Sector and arc formulae require radians.

### Confusing Arcs and Sectors

| Wording | Object type | Use |
|---|---|---|
| sector, board, lamina, sheet, plate | 2D lamina | Area and sector formula |
| arc, bent rod, wire, pole, framework | 1D object | Length and arc formula |

### Using Area for a Framework

A framework, wire or rod is one-dimensional: use length. A lamina is two-dimensional: use area.

### Treating a Hole as Positive Mass

A hole is removed material, so it must be negative.

### Cancelling Density When It Is Not Common

Different density or thickness factors must be included.

### Forgetting That a Folded Part May Count Twice

If a card is folded over, overlapped regions can have double thickness and double mass contribution.

### Choosing an Awkward Origin

The bottom-left corner usually works for rectangles and grids. The centre of a circle usually works for arcs and sectors.

### Not Answering the Actual Distance Asked

If the question asks for distance from \(AD\), give the horizontal distance from \(AD\), not merely the coordinate pair.

### Losing Units

Coordinates need cm/m/units; tensions and weights need newtons or symbolic multiples of \(Mg\).

### Using the Wrong Triangle Angle in Suspended Laminae

State whether \(\theta\) is the angle with the vertical or the horizontal.

### Taking Moments About a Bad Point in Two-String Problems

Choose a moment centre that removes one unknown tension.

### Thinking \(G\) Must Lie Inside the Material

The centre of mass can lie outside the material, especially for arcs, concave laminae and frameworks.

### Using Solid 3D Formulae in This 2D Lesson

Solid hemisphere, hemispherical shell, cone and conical shell results are excluded from this lesson core.

### Treating Calculus Derivations as Required Here

Standard results may be quoted where allowed; calculus derivations and variable-density functions are excluded from `FA22-COM` core.

---

## 13. Practice Questions

These are AI-generated practice questions based on the uploaded evidence and CCEA `FA22-COM` boundary. They are **not** past-paper questions and are **not** textbook questions.

1. Particles of masses \(1\text{ kg}\), \(4\text{ kg}\) and \(5\text{ kg}\) are placed at \(x=2,3,8\). Find \(G\).
2. Particles of masses \(3\text{ kg}\), \(2\text{ kg}\), \(5\text{ kg}\) are placed at \((-1,0),(2,0),(6,0)\). Find \(G\).
3. Particles of masses \(2\text{ kg}\), \(3\text{ kg}\), \(1\text{ kg}\) are placed at \((1,4),(5,2),(-3,0)\). Find \(G\).
4. Particles of masses \(2\text{ kg}\), \(m\text{ kg}\), \(6\text{ kg}\) are placed at \(x=1,4,7\). If \(\bar{x}=5\), find \(m\).
5. A uniform triangular lamina has vertices \((2,1),(8,1),(5,7)\). Find \(G\).
6. Explain why \(\sum m_i x_i=\bar{x}\sum m_i\) is a moments equation and why \(g\) cancels.
7. A light rectangle has \(AB=12\text{ cm}\), \(AD=8\text{ cm}\). Masses \(1,2,3,4\) kg are attached at \(A,B,C,D\). Choose \(A\) as origin and find distances from \(AD\) and \(AB\).
8. Explain why a freely suspended lamina has \(G\) vertically below the suspension point.
9. A uniform right-angled triangular lamina has vertices \((0,0),(9,0),(0,6)\). Find \(G\).
10. A uniform sector has radius \(12\text{ cm}\) and angle \(120^\circ\). Find its centre of mass distance from the centre.
11. A uniform wire is bent into a circular arc of radius \(4\text{ m}\), angle \(90^\circ\). Find the distance of \(G\) from the centre.
12. A uniform lamina is formed from rectangles: area \(18\), centre \((3,2)\); area \(12\), centre \((7,4)\). Find \(G\).
13. A rectangle of area \(60\), centre \((5,3)\), has a hole of area \(12\), centre \((8,4)\), removed. Find \(G\).
14. Piece \(A\): area \(10\), centre \((2,1)\), density \(\rho\). Piece \(B\): area \(6\), centre \((5,4)\), density \(3\rho\). Find \(G\).
15. A uniform wire framework has rods from \((0,0)\) to \((6,0)\), and from \((6,0)\) to \((6,8)\). Find \(G\).
16. A non-uniform wire framework has rod \(AB\), length \(6\), centre \((3,0)\), density \(\lambda\), and rod \(BC\), length \(8\), centre \((6,4)\), density \(2\lambda\). Find \(G\).
17. A lamina has centre \(G=(4,3)\) relative to \(A=(0,0)\). Suspended from \(A\), find the angle \(AG\) makes with the vertical.
18. A lamina of mass \(M\) is suspended by vertical strings at \(A\) and \(B\), \(AB=10a\), and \(G\) is \(3a\) from \(A\). Find tensions.
19. A lamina of mass \(12\text{ kg}\) has centre \((2,3)\). A particle of mass \(4\text{ kg}\) is attached at \((6,-1)\). Find new \(G\).
20. A rectangle with vertices \((0,0),(10,0),(10,6),(0,6)\), area \(60\), centre \((5,3)\), has a rectangular hole of area \(12\), centre \((8,4)\), removed. Find \(G\), then the angle from the origin to \(G\) with the vertical when suspended from the origin.

---

## 14. Worked Solutions

### Solution 1

\[
1(2)+4(3)+5(8)=10\bar{x},
\quad
2+12+40=10\bar{x},
\quad
\bar{x}=5.4.
\]

\[
\boxed{G=(5.4,0)}
\]

### Solution 2

\[
3(-1)+2(2)+5(6)=10\bar{x},
\quad
-3+4+30=10\bar{x},
\quad
\bar{x}=3.1.
\]

\[
\boxed{G=(3.1,0)}
\]

### Solution 3

\[
2\binom14+3\binom52+1\binom{-3}{0}=6\binom{\bar{x}}{\bar{y}}.
\]

\[
\binom28+\binom{15}{6}+\binom{-3}{0}=\binom{14}{14}.
\]

\[
\boxed{G=\left(\frac73,\frac73\right)}
\]

### Solution 4

\[
2(1)+4m+6(7)=5(2+m+6).
\]

\[
44+4m=40+5m,
\qquad
m=4.
\]

### Solution 5

\[
G=\left(\frac{2+8+5}{3},\frac{1+1+7}{3}\right)=(5,3).
\]

### Solution 6

Each particle has weight \(m_i g\). The moment of that weight about the origin is \(m_i g x_i\). The resultant weight is \(g\sum m_i\) acting at \(\bar{x}\), so:

\[
\sum m_i g x_i=\bar{x}g\sum m_i.
\]

Divide by \(g\):

\[
\sum m_i x_i=\bar{x}\sum m_i.
\]

### Solution 7

With \(A=(0,0)\):

\[
A=(0,0),\quad B=(12,0),\quad C=(12,8),\quad D=(0,8).
\]

\[
1\binom00+2\binom{12}0+3\binom{12}8+4\binom08=10\binom{\bar{x}}{\bar{y}}.
\]

\[
\binom{60}{56}=10\binom{\bar{x}}{\bar{y}}.
\]

\[
\bar{x}=6,
\qquad
\bar{y}=5.6.
\]

Distance from \(AD\): \(6\text{ cm}\). Distance from \(AB\): \(5.6\text{ cm}\).

### Solution 8

The weight acts through \(G\). If \(G\) is not vertically below the suspension point, the weight has a non-zero perpendicular distance from the suspension point, so there is a moment and the lamina turns. In equilibrium, the line of action of the weight passes through the suspension point, so \(G\) is vertically below it.

### Solution 9

\[
G=\left(\frac{0+9+0}{3},\frac{0+0+6}{3}\right)=(3,2).
\]

### Solution 10

\[
2\alpha=120^\circ,
\qquad
\alpha=60^\circ=\frac{\pi}{3}.
\]

\[
d=\frac{2(12)\sin(\pi/3)}{3(\pi/3)}
=\frac{24(\sqrt3/2)}{\pi}
=\frac{12\sqrt3}{\pi}=6.62\text{ cm to 3 s.f.}
\]

### Solution 11

\[
2\alpha=90^\circ,
\qquad
\alpha=45^\circ=\frac{\pi}{4}.
\]

\[
d=\frac{4\sin(\pi/4)}{\pi/4}
=\frac{4(\sqrt2/2)}{\pi/4}
=\frac{8\sqrt2}{\pi}=3.60\text{ m to 3 s.f.}
\]

### Solution 12

\[
18\binom32+12\binom74=30\binom{\bar{x}}{\bar{y}}.
\]

\[
\binom{54}{36}+\binom{84}{48}=\binom{138}{84}.
\]

\[
G=\left(\frac{138}{30},\frac{84}{30}\right)=\left(\frac{23}{5},\frac{14}{5}\right).
\]

### Solution 13

\[
60\binom53-12\binom84=48\binom{\bar{x}}{\bar{y}}.
\]

\[
\binom{300}{180}-\binom{96}{48}=\binom{204}{132}.
\]

\[
G=\left(\frac{204}{48},\frac{132}{48}\right)=\left(\frac{17}{4},\frac{11}{4}\right).
\]

### Solution 14

Masses are \(10\rho\) and \(18\rho\):

\[
10\rho\binom21+18\rho\binom54=28\rho\binom{\bar{x}}{\bar{y}}.
\]

\[
\binom{20\rho}{10\rho}+\binom{90\rho}{72\rho}=\binom{110\rho}{82\rho}.
\]

\[
G=\left(\frac{55}{14},\frac{41}{14}\right).
\]

### Solution 15

Rod centres are \((3,0)\) and \((6,4)\), lengths \(6\) and \(8\):

\[
6\binom30+8\binom64=14\binom{\bar{x}}{\bar{y}}.
\]

\[
\binom{18}{0}+\binom{48}{32}=\binom{66}{32}.
\]

\[
G=\left(\frac{33}{7},\frac{16}{7}\right).
\]

### Solution 16

Masses are \(6\lambda\) and \(16\lambda\):

\[
6\lambda\binom30+16\lambda\binom64=22\lambda\binom{\bar{x}}{\bar{y}}.
\]

\[
G=\left(\frac{57}{11},\frac{32}{11}\right).
\]

### Solution 17

Horizontal separation \(=4\), vertical separation \(=3\). Angle with vertical:

\[
\tan\theta=\frac{4}{3},
\qquad
\theta=\tan^{-1}\left(\frac43\right)=53.1^\circ.
\]

### Solution 18

Take moments about \(A\):

\[
T_B(10a)=Mg(3a).
\]

\[
T_B=\frac{3}{10}Mg.
\]

Vertical equilibrium:

\[
T_A+T_B=Mg,
\qquad
T_A=\frac{7}{10}Mg.
\]

### Solution 19

\[
12\binom23+4\binom6{-1}=16\binom{\bar{x}}{\bar{y}}.
\]

\[
\binom{24}{36}+\binom{24}{-4}=\binom{48}{32}.
\]

\[
\boxed{G=(3,2)}
\]

### Solution 20

Part a:

\[
60\binom53-12\binom84=48\binom{\bar{x}}{\bar{y}}.
\]

\[
\binom{300}{180}-\binom{96}{48}=\binom{204}{132}.
\]

\[
G=\left(\frac{17}{4},\frac{11}{4}\right).
\]

Part b:

\[
\tan\theta=\frac{17/4}{11/4}=\frac{17}{11}.
\]

\[
\theta=\tan^{-1}\left(\frac{17}{11}\right)=57.1^\circ.
\]

---

## 15. Exam Technique Notes

1. Identify the object type before calculating: particle, light plate, uniform lamina, composite lamina, hole, wire/rod/framework, or non-uniform componentwise object.
2. Use the universal equations:

\[
\sum m_i x_i=\bar{x}\sum m_i,
\qquad
\sum m_i\binom{x_i}{y_i}=\binom{\bar{x}}{\bar{y}}\sum m_i.
\]

3. Use symmetry before algebra.
4. For composite shapes, build a component table.
5. State the origin.
6. Holes need negative mass.
7. Keep exact values until the final line.
8. For sectors and arcs, check: sector or arc? full angle \(2\alpha\)? halved? radians?
9. For suspended laminae, find \(G\), draw the line from pivot to \(G\), and use the fact that this line is vertical in equilibrium.
10. For two-string problems, use vertical equilibrium and take moments about one string attachment point.

Useful phrases:

- “Since the lamina is uniform, mass is proportional to area.”
- “Since the framework is uniform, mass is proportional to length.”
- “Treat the removed part as negative mass.”
- “When freely suspended, \(G\) lies vertically below the point of suspension.”
- “Taking moments about \(A\) eliminates the tension at \(A\).”

---

## 16. Syllabus Gap Check

### LO Coverage Table

| LO ID | Covered? | Evidence coverage |
|---|---:|---|
| `FA22-COM-LO001` | Yes | Definitions, resultant weight, balancing, model limitations. |
| `FA22-COM-LO002` | Yes | Particles, rods, wires, arcs, frameworks, symmetry, no calculus derivations. |
| `FA22-COM-LO003` | Yes | Rectangle, triangle methods, circular sector, symmetry. |
| `FA22-COM-LO004` | Yes | Composite laminae, holes, area proportional to mass, componentwise density. |
| `FA22-COM-LO005` | Yes | Freely suspended laminae, \(G\) vertically below point, two-string moments. |

### Off-Spec Content Found but Excluded

| Content | Reason excluded from core |
|---|---|
| Calculus derivations of standard centre-of-mass formulae | Evidence says these are proved in the next chapter; `FA22-COM` excludes calculus/variable density problems. |
| Solid hemisphere, hemispherical shell, cone, conical shell | 3D/further centre-of-mass content, not this 2D lesson. |
| Angular acceleration of bodies | Mentioned as not covered; only used as model limitation. |
| Variable density functions | Excluded by CCEA LO wording. |
| Pin-jointed framework force analysis | Separate CCEA topic; not the same as wire framework centre of mass. |

### Optional Enrichment Not Required by CCEA

- proving the triangular lamina centre using integration;
- deriving the sector and arc formulae;
- extending centre of mass to 3D bodies;
- variable density centre-of-mass integrals;
- rotation and angular acceleration.

### Weak Evidence Warnings

- The screenshot PDF has no parsed text.
- Edexcel/Pearson examples in evidence are not CCEA exam questions.
- Two-string suspension examples are diagram-dependent, so generic forms are used where exact diagram distances were not fully available.
- Framework wording means wire/rod centre-of-mass object, not pin-jointed structural framework analysis.

---

## 17. Recommended Enhancements Not in the Evidence

AI-proposed enhancements aligned with `FA22-COM`:

- many-weights-to-one-weight diagram;
- object-type comparison visual;
- lamina vs framework comparison;
- hole as negative mass animation;
- suspended lamina before/after rotation diagram;
- two-string moment diagram;
- particle centre-of-mass calculator;
- composite lamina table builder;
- suspended lamina angle explorer;
- arc/sector formula checker.

These are proposed teaching enhancements, not original evidence-backed diagrams.

---

## 18. Supplementary Sources Used

### Project Sources Used

- CCEA Further Mathematics specification map: core topic boundary and LO IDs.
- Further Maths module map: topic identity and bridge mapping.
- Further Maths evidence checklist: evidence audit and phase structure.
- Further Maths portal build knowledge evidence: general portal build expectations.

### Lesson-Specific Evidence Used

- `FM2-Chp2-Centres of Mass.pdf`: main readable PDF evidence for definitions, formulae, diagrams and examples.
- `transcripts.md`: teacher explanation, warnings, example reasoning and spoken method notes.
- `Chapter_2_Centres_of_Mass_🚗_(Further_Mechanics_2)_screenshots.pdf`: visual-only evidence, used cautiously because no parsed text was available.

### Ordinary A-Level Maths Bridge Sources Used

Ordinary A-Level Maths sources were used only as bridge context for moments, equilibrium, forces and weight, position vectors, coordinate geometry and trigonometry. They do not override the CCEA Further Mathematics `FA22-COM` boundary.

### Cross-Board Sources Used

The uploaded evidence includes Pearson Further Mechanics 2 and Edexcel M2 references. These were used only where the CCEA `FA22-COM` boundary confirms the mathematical method is on-spec. They are not presented as CCEA questions.

### Final Evidence Boundary Statement

The core lesson is bounded by `FA22-COM`: centre of mass for particles, rods/wires, standard laminae, composite laminae and suspended laminae. Calculus derivations, variable density functions, 3D solid bodies and pin-jointed framework force analysis are excluded from the core lesson.

---

## 19. Final Student Checklist

### Prerequisite Confidence Checklist

- [ ] Use coordinates with negative values correctly.
- [ ] Use column vectors such as \(\begin{pmatrix}x\\y\end{pmatrix}\).
- [ ] Calculate areas of rectangles, triangles and sectors.
- [ ] Calculate midpoints of line segments.
- [ ] Use \(\tan^{-1}\) to find angles.
- [ ] Explain a moment as force multiplied by perpendicular distance.
- [ ] Use vertical equilibrium and moments.

### Further Maths Method Checklist

- [ ] Define centre of mass.
- [ ] Distinguish between particle, rod/wire, lamina and body.
- [ ] Use \(\sum m_i x_i=\bar{x}\sum m_i\).
- [ ] Use \(\sum m_i\binom{x_i}{y_i}=\binom{\bar{x}}{\bar{y}}\sum m_i\).
- [ ] Choose a sensible origin.
- [ ] Use symmetry.
- [ ] Find the centre of mass of a triangular lamina.
- [ ] Use sector and arc formulae with radians.
- [ ] Split composite laminae into components.
- [ ] Treat holes as negative mass.
- [ ] Use area for laminae and length for frameworks/wires.
- [ ] Include density/thickness multipliers when needed.
- [ ] Solve suspended-lamina and two-string problems.

### Exam Technique Checklist

- [ ] State the origin.
- [ ] Label \(G\), \(\bar{x}\), \(\bar{y}\).
- [ ] State whether you are using area, length or mass.
- [ ] Keep negative signs.
- [ ] Keep exact values until the final line.
- [ ] Convert degrees to radians for arc/sector formulae.
- [ ] Use \(\alpha\), not \(2\alpha\), in formulae.
- [ ] Include units.
- [ ] State that cross-board examples are not CCEA past-paper questions.
- [ ] For suspension, state that \(G\) lies vertically below the point of suspension.
- [ ] For two-string problems, take moments about a point that removes one tension.

### Bridge Checklist

- [ ] Explain how the centre-of-mass equation comes from moments.
- [ ] Explain why \(g\) cancels in coordinate calculations.
- [ ] Explain why \(g\) returns in tension and weight calculations.
- [ ] Connect column vectors to mass-weighted position vectors.
- [ ] Explain why a vertical line through \(G\) matters in suspended equilibrium.

### Diagram and Visual Understanding Checklist

- [ ] Particle-on-line diagram.
- [ ] Weighted particle plane diagram.
- [ ] Rectangle with masses at vertices.
- [ ] Triangle median diagram showing \(AG:GM=2:1\).
- [ ] One-third-from-base triangle diagram.
- [ ] Sector diagram with total angle \(2\alpha\).
- [ ] Arc diagram with \(G\) off the wire.
- [ ] Composite lamina split into rectangles/triangles.
- [ ] Lamina with a hole shown as negative mass.
- [ ] Wire framework split into rods/arcs.
- [ ] Suspended lamina with \(G\) vertically below the pivot.
- [ ] Two-string tension diagram with \(Mg\), \(T_A\) and \(T_B\).
