# 1. Lesson Title and Metadata

## Lesson Title

FA22 Further Centre of Mass: Calculus, Composite Bodies, Suspended Bodies, Sliding and Toppling

## Metadata

| Field | Value |
|---|---|
| Date generated | 2026-06-04 |
| Course | CCEA GCE Further Mathematics |
| Unit | FA22: Further A2 2 Applied Mathematics |
| Applied section | Section B: Mechanics 2 |
| Topic code | FA22-FCOM |
| Topic name | Further centre of mass |
| Topic slug | further_centre_of_mass |
| Topic Pascal | FurtherCentreOfMass |
| Topic ID | FA22FurtherCentreOfMass |
| Lesson file name | FA22_further_centre_of_mass_lesson.md |
| LO IDs | FA22-FCOM-LO001; FA22-FCOM-LO002; FA22-FCOM-LO003; FA22-FCOM-LO004 |
| Bridge tags | A22 Moments; FA22 Centre of Mass; A21 Integration; AS2 Forces and Friction; A21 Volumes of Revolution |
| Topic tags | Centre of mass; laminae; solids; calculus; volumes of revolution; composite bodies; suspended bodies; sliding; toppling; moments; friction; normal reaction |

## Learning Outcome Identity

This lesson is for the CCEA Further Mathematics topic `FA22-FCOM`, **Further centre of mass**.

The lesson-specific evidence is titled **Further Centres of Mass** and comes from a Further Mechanics 2 chapter. The supplied transcript describes the chapter as an A2 Further Mechanics topic that extends centres of mass using calculus, 3D solids, non-uniform bodies, equilibrium, toppling and sliding. The transcript also warns that the topic is integration-heavy and uses integration from ordinary Pure/Core Pure, volumes of revolution, forces and friction, polar coordinates and moments as prerequisites.

## Important Authority Note

The supplied slide PDF contains Pearson/Edexcel-style material and explicitly refers to “The Specification (from Edexcel)”. This lesson does **not** use Edexcel as syllabus authority. CCEA `FA22-FCOM` is the syllabus authority. The Pearson/Edexcel material is used only as lesson-specific mathematical evidence where it matches the CCEA `FA22-FCOM` boundary.

---

# 2. Evidence Map

## 2.1 Project Sources Used

| Source | Use |
|---|---|
| `CCEA_GCE_Further_Mathematics_Specification_Map.md` | Determines `FA22-FCOM`, Section B: Mechanics 2, LO IDs and syllabus boundaries. |
| `Further_Maths_README_module_map.md` | Confirms bridge route: A22 Moments; FA22 Centre of Mass; A21 Integration for continuous bodies. |
| `Further_Maths_EVIDENCE_DROP_CHECKLIST.md` | Structures evidence intake, missing evidence, off-spec log and visual asset planning. |
| `Ordinary_A_Level_Maths_Bridge_Spec_Extracts.md` | Provides ordinary CCEA A-Level Maths bridge context only. |
| `Further Maths Portal Build – Knowledge Evidence.txt` | General portal build context only. |

## 2.2 Lesson-Specific Evidence Used

| Evidence | Type | Use |
|---|---|---|
| `transcripts.md` | Teacher transcript | Main explanation source for calculus derivations, warnings, worked-example flow, density comments, suspended-body reasoning, sliding/toppling reasoning. |
| `FM2-Chp3-FurtherCentresOfMass-Final.pdf` | Slide/PDF evidence | Formulae, diagrams, worked examples, exercise structure and standard result reminders. |
| `Chapter_3_Further_Centres_of_Mass_(A2)_🚗_(Further_Mechanics_2)_screenshots.pdf` | Screenshot visual evidence | Visual confirmation of chapter overview, formula boards and diagram layouts. |

## 2.3 Evidence Summary by Mathematical Subtopic

| Subtopic | Evidence used | Core CCEA status |
|---|---|---|
| Moment concept for centre of mass | Transcript and slide recap | Core |
| Lamina strip formulae | Transcript and slide formulae | Core |
| Between-curves laminae | Transcript worked example | Core |
| Standard laminae via calculus | Transcript and slide examples | Core where calculus is needed; proof depth controlled by CCEA boundary |
| Polar integration for sector/arc | Transcript and slide evidence | Optional enrichment unless question demands |
| Volumes of revolution for solids | Transcript and slide evidence | Core |
| Standard solid cone and solid hemisphere proofs | Transcript and slide evidence | Core proof boundary |
| Composite solids and densities | Transcript and slide examples | Core |
| Suspended bodies | Transcript and slide evidence | Core |
| Sliding/toppling | Transcript and slide evidence | Core |
| Banked corners | Project map only | Excluded from this lesson, belongs to `FA22-FCM` |

## 2.4 Visual Evidence Notes

The screenshot PDF did not provide parsed searchable text. Visual details are preserved only where visible/readable. No uninspected visual detail is claimed.

---

# 3. Specification Alignment

| LO ID | Official wording | Lesson coverage | Evidence source | Syllabus boundary | Ordinary A-Level Maths bridge |
|---|---|---|---|---|---|
| FA22-FCOM-LO001 | find the centre of mass of laminae and solids, including the use of calculus | Sections 7, 8, 11 and 14 derive and apply centre-of-mass formulae for laminae and solids. | CCEA spec map; transcript; slide PDF | Include calculus. Proof of standard results for solid cone and solid hemisphere only may be required. | A21 Integration and A21 Volumes of Revolution become mass/moment integrals. |
| FA22-FCOM-LO002 | find the centre of mass of composite bodies | Composite body mass-moment tables, density ratios and removed-solid/frustum methods. | CCEA spec map; transcript; slide PDF | Include composite bodies. Use density/mass ratios carefully. | A22 Moments becomes weighted average of component mass moments. |
| FA22-FCOM-LO003 | solve problems involving suspended bodies | Vertical through centre of mass, pivot diagrams and angle-finding. | CCEA spec map; transcript; slide PDF | Include suspended 3D bodies using clear 2D elevations. | A22 moments and trigonometry. |
| FA22-FCOM-LO004 | solve sliding and toppling problems | Friction threshold, normal reaction location, line of weight and footprint tests. | CCEA spec map; transcript; slide PDF | Include sliding and toppling. Do not merge with banked-corner topic unless explicitly a banked-corner question. | AS2/A2 friction and equilibrium become rigid-body stability tests. |

---

# 4. Learning Objectives

## 4.1 Core Further Mathematics Objectives

By the end of this lesson, you should be able to:

1. Explain centre of mass using moments of mass.
2. Derive the centre-of-mass formulae for a uniform lamina bounded by \(y=f(x)\), the \(x\)-axis and \(x=a,\ x=b\).
3. Adapt lamina formulae for regions between two curves \(y_1\) and \(y_2\).
4. Use volumes of revolution to find centres of mass of 3D solids.
5. Prove the standard centre-of-mass results for a solid cone and a solid hemisphere where required.
6. Use standard centre-of-mass results for common laminae and solids.
7. Find the centre of mass of composite bodies using mass-ratio and moment equations.
8. Handle density ratios and variable density/mass functions when supplied in a question.
9. Solve suspended-body problems using the fact that the centre of mass lies vertically below the suspension point in equilibrium.
10. Solve sliding and toppling problems using force equilibrium, friction limits and the line of action of weight.

## 4.2 Bridge Objectives

You should be able to connect this Further Mechanics topic to ordinary A-Level Maths by recognising that:

1. A moment of a force from ordinary Mechanics becomes a moment of a mass in centre-of-mass calculations.
2. Area under a curve becomes mass for a uniform lamina.
3. Volume of revolution becomes mass for a uniform solid.
4. Friction and normal reaction from ordinary Mechanics are not enough by themselves once the body has dimensions.
5. Integration limits now have physical meaning: they define the body being modelled.

## 4.3 Exam Technique Objectives

You should be able to:

1. Define \(M\), \(\bar{x}\), \(\bar{y}\), density and all limits before using formulae.
2. Show integration steps rather than relying on calculator-only values when calculus is requested.
3. Use exact fractions unless a real-world context or question wording asks for decimals.
4. State where the answer is measured from: base, vertex, diameter, centre, plane face, top, or pivot.
5. Draw large, clean diagrams for suspended-body and toppling questions.
6. Check whether sliding happens before toppling, and whether toppling happens before sliding.

---

# 5. Explicit Prerequisite Recap

## 5.1 GCSE Foundations

You need area of triangles, rectangles, sectors and circles; volume formulae where given or known; line equations; graph intercepts; curve sketching; similar triangles; trigonometry; exact fractions and algebraic simplification.

## 5.2 Ordinary AS/A2 Mathematics Foundations

You need integration of powers of \(x\), definite integrals, area under a curve, area between curves, volumes of revolution, resolving forces, friction and limiting equilibrium, moments, and interpreting a physical model from a diagram.

## 5.3 Previous Further Mathematics Foundations

You may also use FA22 Centre of Mass, especially particle systems, rods, standard laminae, composite laminae and suspended laminae; Further Pure calculus where integration is more demanding; and polar coordinates if attempting sector/arc derivations as enrichment.

## 5.4 A-Level Maths Bridge: What You Already Know and What Further Maths Changes

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| A21/A2 Pure Integration | \(\int_a^b y\,dx\) gives signed area under a graph. | \(\int_a^b y\,dx\) may represent the mass of a uniform lamina, up to a constant density factor. | Area signs and limits now affect a physical answer. Negative mass is a warning that the model or limits are wrong. |
| A21 Area Between Curves | Area is \(\int_a^b(\text{top}-\text{bottom})\,dx\). | Mass becomes \(\int_a^b(y_1-y_2)\,dx\), and the vertical coordinate of a strip uses the midpoint \(\frac12(y_1+y_2)\). | Using \(\frac12(y_1-y_2)\) for the strip’s centre is wrong. |
| A21 Volumes of Revolution | Rotating \(y=f(x)\) about an axis gives volume \(\pi\int_a^b y^2\,dx\). | Thin discs have mass proportional to \(\pi y^2\,dx\), and moment proportional to \(x\pi y^2\,dx\). | Dropping \(\pi\) is allowed only when explaining that it cancels in a ratio. |
| A22 Moments | Moment of force \(=\) force \(\times\) perpendicular distance. | Moment of mass \(=\) mass \(\times\) distance, because every weight contains the same factor \(g\), so \(g\) cancels. | Saying “moment always means force” is too narrow here. |
| AS2/A2 Forces and Friction | \(F\le \mu R\), with \(F=\mu R\) in limiting equilibrium. | Sliding is tested by friction, but toppling is tested by line of weight and footprint/contact edge. | A particle model hides the exact point where the normal reaction acts. Rigid bodies need dimensions. |

In ordinary A-Level Maths, this idea appeared as calculating areas, volumes, force moments and friction thresholds. In Further Maths, the same ideas become a machinery room for continuous mass: little strips, little discs and little components all contribute moments. The key upgrade is that integration is no longer just “area under a graph”; it becomes a sum of mass and moment contributions. The danger is that old shortcuts, especially treating the body as a particle, can erase the geometry that determines toppling.

---

# 6. Big Picture Explanation

Centre of mass is the point where a body’s mass can be treated as acting for the purpose of translational and rotational balance. In earlier centre-of-mass work, you mostly handled particles, rods and composite laminae by adding a finite list of pieces. This topic takes the same idea and stretches it into a continuous body.

The central idea is:

\[
\text{sum of moments of small masses}
=
\text{moment of total mass at the centre of mass}.
\]

For a finite set of particles:

\[
\sum m_i x_i = M\bar{x}, \qquad M=\sum m_i.
\]

For a lamina, there are infinitely many tiny strips. Integration becomes the adding machine:

\[
\sum \longrightarrow \int.
\]

For a solid of revolution, the tiny pieces become discs. For a composite body, the pieces may be standard bodies. For a suspended body, the centre of mass must lie vertically below the suspension point. For toppling, the line of action of the weight must stay within the body’s footprint. Once that line passes outside the contact face, the body turns.

For applied modelling:

- bodies are treated as rigid unless the question says otherwise;
- laminae are treated as thin plane bodies;
- uniform means constant mass per unit length, area or volume;
- non-uniform means density or mass per unit length/area/volume varies as stated;
- \(g\) usually cancels in centre-of-mass ratios;
- diagrams are not decorative here: they are the machinery.

---

# 7. Key Definitions and Notation

## 7.1 Centre of Mass

The **centre of mass** of a body is the point at which the whole mass of the body may be considered to act when taking moments for centre-of-mass calculations.

For particles of masses \(m_1,m_2,\ldots,m_n\) at \(x\)-coordinates \(x_1,x_2,\ldots,x_n\):

\[
\sum_{i=1}^{n} m_i x_i = M\bar{x},
\qquad
M=\sum_{i=1}^{n}m_i.
\]

Therefore:

\[
\bar{x}
=
\frac{\sum_{i=1}^{n}m_i x_i}{\sum_{i=1}^{n}m_i}.
\]

Similarly:

\[
\bar{y}
=
\frac{\sum_{i=1}^{n}m_i y_i}{\sum_{i=1}^{n}m_i},
\qquad
\bar{z}
=
\frac{\sum_{i=1}^{n}m_i z_i}{\sum_{i=1}^{n}m_i}.
\]

## 7.2 Moment of a Mass

In ordinary Mechanics:

\[
\text{moment of force}=\text{force}\times \text{perpendicular distance}.
\]

In centre-of-mass work:

\[
\text{moment of mass}=\text{mass}\times \text{distance}.
\]

This is valid because weight is \(mg\), and if every component is multiplied by the same gravitational field strength \(g\), that factor cancels from the centre-of-mass equation.

## 7.3 Lamina

A **lamina** is a thin plane body. A uniform lamina has constant mass per unit area. If mass per unit area is \(\rho\), then:

\[
dm=\rho\,dA.
\]

When \(\rho\) is constant, it often cancels from centre-of-mass ratios.

## 7.4 Uniform and Non-Uniform Bodies

A body is **uniform** if its density is constant. A body is **non-uniform** if its density or mass distribution varies, for example \(\rho(x)\) or \(\lambda(x)\). If a density function is supplied, it must be included inside the mass and moment integrals.

## 7.5 Standard Notation

| Symbol | Meaning |
|---|---|
| \(M\) | Total mass, or mass-ratio quantity proportional to mass |
| \(\bar{x},\bar{y},\bar{z}\) | Coordinates of centre of mass |
| \(y=f(x)\) | Boundary curve of a lamina or generating curve for a solid |
| \(a,b\) | Integration limits |
| \(dx\) | Infinitesimal width of a strip or disc |
| \(dm\) | Infinitesimal mass element |
| \(\rho\) | Density or mass per unit area/volume |
| \(\lambda\) | Density constant or mass-per-unit-length constant |
| \(R\) | Normal reaction force |
| \(F\) | Friction force |
| \(\mu\) | Coefficient of friction |
| \(W\) | Weight |
| \(g\) | Acceleration due to gravity |

---

# 8. Core Theory

## 8.1 The One Equation Under Everything

For any centre-of-mass calculation:

\[
\text{moment of total mass at centre of mass}
=
\text{sum of moments of all mass elements}.
\]

For continuous bodies:

\[
M\bar{x}=\int x\,dm,
\qquad
M\bar{y}=\int y\,dm.
\]

The entire topic is about choosing the correct \(dm\) and the correct distance.

**Bridge Note:** In ordinary A-Level Mechanics, moments were usually moments of forces. Here, Further Mechanics uses the same lever idea, but the quantity being distributed is mass. Since weight is \(mg\), the common factor \(g\) cancels.

## 8.2 Uniform Lamina Bounded by \(y=f(x)\), \(x=a\), \(x=b\) and the \(x\)-axis

Take a vertical strip of width \(dx\) and height \(y\).

\[
dA=y\,dx.
\]

If the lamina has constant mass per unit area \(\rho\):

\[
dm=\rho y\,dx.
\]

For mass-ratio working, \(\rho\) cancels, so:

\[
M=\int_a^b y\,dx.
\]

The strip is positioned at \(x\), so:

\[
M\bar{x}=\int_a^b xy\,dx.
\]

The centre of the strip is halfway up, at height \(\frac12y\), so:

\[
M\bar{y}=\frac12\int_a^b y^2\,dx.
\]

Therefore:

\[
\boxed{\bar{x}=\frac{\int_a^b xy\,dx}{\int_a^b y\,dx}}
\]

and:

\[
\boxed{\bar{y}=\frac{\int_a^b y^2\,dx}{2\int_a^b y\,dx}}.
\]

**Bridge Note:** In ordinary A-Level Maths, \(\int_a^b y\,dx\) gave an area. Here that same integral becomes the mass-ratio denominator. The numerator is not “another area”; it is a sum of moments.

## 8.3 Uniform Lamina Between Two Curves

Suppose a lamina is bounded between:

\[
y=y_1(x), \qquad y=y_2(x),
\]

for:

\[
a\le x\le b,
\qquad y_1(x)\ge y_2(x).
\]

The strip height is:

\[
y_1-y_2.
\]

So:

\[
M=\int_a^b(y_1-y_2)\,dx.
\]

For the \(x\)-coordinate:

\[
M\bar{x}=\int_a^b x(y_1-y_2)\,dx,
\]

so:

\[
\boxed{
\bar{x}
=
\frac{\int_a^b x(y_1-y_2)\,dx}
{\int_a^b(y_1-y_2)\,dx}}
\]

For the \(y\)-coordinate, the strip does not run from \(0\) to \(y\). It runs from \(y_2\) to \(y_1\). The vertical coordinate of the centre of the strip is:

\[
\frac{y_1+y_2}{2}.
\]

The moment about the \(x\)-axis is:

\[
M\bar{y}
=
\frac12\int_a^b (y_1+y_2)(y_1-y_2)\,dx.
\]

Since:

\[
(y_1+y_2)(y_1-y_2)=y_1^2-y_2^2,
\]

we also have:

\[
\boxed{
\bar{y}
=
\frac{\frac12\int_a^b (y_1^2-y_2^2)\,dx}
{\int_a^b(y_1-y_2)\,dx}}
\]

**Warning:** \(\frac12(y_1-y_2)\) is half the height of the strip, not the vertical coordinate of the strip centre.

**Bridge Note:** Ordinary A-Level Maths taught top curve minus bottom curve for area. Further Mechanics keeps that for mass, but adds the strip midpoint.

## 8.4 Symmetry in Centre-of-Mass Problems

If a uniform body has a line of symmetry, the centre of mass lies on that line. If a uniform 3D body has a plane of symmetry, the centre of mass lies in that plane. Symmetry can find one coordinate, but usually not all coordinates.

Examples:

- uniform sphere: centre of mass at its centre;
- uniform cylinder: centre of mass halfway along its axis;
- uniform hemisphere: centre of mass on its axis of symmetry;
- sector of a circle: centre of mass on its axis of symmetry;
- semicircular lamina: centre of mass on its axis of symmetry.

## 8.5 Standard Lamina Results and Proof from Calculus

Some standard results may be quoted unless the question asks for proof. When a question says “show, using calculus”, the result must be derived.

For a right-angled triangular lamina with vertices \((0,0),(D,0),(D,H)\), the boundary line is:

\[
y=\frac{H}{D}x.
\]

The area/mass-ratio is:

\[
M=\int_0^D \frac{H}{D}x\,dx
=\frac{H}{D}\left[\frac12x^2\right]_0^D
=\frac{HD}{2}.
\]

The \(x\)-moment is:

\[
M\bar{x}=\int_0^D x\left(\frac{H}{D}x\right)\,dx
=\frac{H}{D}\left[\frac13x^3\right]_0^D
=\frac{HD^2}{3}.
\]

Therefore:

\[
\bar{x}=\frac{\frac{HD^2}{3}}{\frac{HD}{2}}
=\frac{HD^2}{3}\times\frac{2}{HD}
=\frac{2D}{3}.
\]

The \(y\)-moment is:

\[
M\bar{y}=\frac12\int_0^D\left(\frac{H}{D}x\right)^2\,dx
=\frac{H^2}{2D^2}\left[\frac13x^3\right]_0^D
=\frac{H^2D}{6}.
\]

Therefore:

\[
\bar{y}=\frac{\frac{H^2D}{6}}{\frac{HD}{2}}
=\frac{H^2D}{6}\times\frac{2}{HD}
=\frac{H}{3}.
\]

So:

\[
\boxed{(\bar{x},\bar{y})=\left(\frac{2D}{3},\frac{H}{3}\right)}.
\]

**Transcript warning preserved:** do **not** drop the \(\frac12\) in \(M\bar{y}=\frac12\int y^2\,dx\).

## 8.6 Optional Enrichment: Sector and Arc Proofs Using Polar Integration

This subsection is included because it appears in the supplied evidence and helps understanding. It is not treated as core CCEA proof requirement unless a question specifically asks for such a derivation.

For a uniform sector of radius \(R\) and angle \(2\alpha\), symmetry gives \(\bar{y}=0\), and:

\[
M=\frac12R^2(2\alpha)=R^2\alpha.
\]

A thin triangular slice has area:

\[
dA=\frac12R^2\,d\theta.
\]

The slice centre is \(\frac23R\) from \(O\), so its \(x\)-coordinate is:

\[
\frac23R\cos\theta.
\]

Thus:

\[
d(\text{moment})=\left(\frac23R\cos\theta\right)\left(\frac12R^2\,d\theta\right)=\frac13R^3\cos\theta\,d\theta.
\]

Integrating from \(-\alpha\) to \(\alpha\):

\[
M\bar{x}=\int_{-\alpha}^{\alpha}\frac13R^3\cos\theta\,d\theta
=\frac13R^3[\sin\theta]_{-\alpha}^{\alpha}
=\frac23R^3\sin\alpha.
\]

So:

\[
\boxed{\bar{x}=\frac{2R\sin\alpha}{3\alpha}}.
\]

For a uniform circular arc of radius \(R\) and angle \(2\alpha\):

\[
M=2R\alpha,
\qquad ds=R\,d\theta,
\qquad x=R\cos\theta.
\]

Then:

\[
M\bar{x}=\int_{-\alpha}^{\alpha}R^2\cos\theta\,d\theta=2R^2\sin\alpha,
\]

so:

\[
\boxed{\bar{x}=\frac{R\sin\alpha}{\alpha}}.
\]

## 8.7 Solids of Revolution: Centre of Mass Using Calculus

Consider a solid formed by rotating \(y=f(x)\) about the \(x\)-axis between \(x=a\) and \(x=b\). A thin disc has radius \(y\), width \(dx\), volume:

\[
dV=\pi y^2\,dx.
\]

If density is constant \(\rho\):

\[
dm=\rho\pi y^2\,dx.
\]

Thus:

\[
M=\rho\pi\int_a^b y^2\,dx.
\]

The disc is located at \(x\), so:

\[
M\bar{x}=\rho\pi\int_a^b xy^2\,dx.
\]

Therefore:

\[
\boxed{\bar{x}=\frac{\int_a^b xy^2\,dx}{\int_a^b y^2\,dx}}.
\]

For rotation about the \(x\)-axis, symmetry gives \(\bar{y}=0\) and \(\bar{z}=0\).

If the body is formed by rotating about the \(y\)-axis and using \(x\) as a function of \(y\), then:

\[
\boxed{\bar{y}=\frac{\int yx^2\,dy}{\int x^2\,dy}}.
\]

## 8.8 Proof of Standard Solid Result: Uniform Solid Cone

For a cone of height \(H\) and base radius \(R\), take the vertex at \(x=0\) and base at \(x=H\). The generating line is:

\[
y=\frac{R}{H}x.
\]

Then:

\[
y^2=\frac{R^2}{H^2}x^2.
\]

For a solid of revolution:

\[
\bar{x}=\frac{\int_0^H xy^2\,dx}{\int_0^H y^2\,dx}.
\]

Denominator:

\[
\int_0^H y^2\,dx=\frac{R^2}{H^2}\int_0^H x^2\,dx
=\frac{R^2}{H^2}\left[\frac13x^3\right]_0^H
=\frac{R^2H}{3}.
\]

Numerator:

\[
\int_0^H xy^2\,dx=\frac{R^2}{H^2}\int_0^H x^3\,dx
=\frac{R^2}{H^2}\left[\frac14x^4\right]_0^H
=\frac{R^2H^2}{4}.
\]

Therefore:

\[
\bar{x}=\frac{\frac{R^2H^2}{4}}{\frac{R^2H}{3}}
=\frac{R^2H^2}{4}\times\frac{3}{R^2H}
=\frac{3H}{4}.
\]

So the centre of mass is:

\[
\boxed{\frac{3H}{4}\text{ from the vertex}}
\]

or:

\[
\boxed{\frac{H}{4}\text{ from the base}}.
\]

## 8.9 Proof of Standard Solid Result: Uniform Solid Hemisphere

For a solid hemisphere of radius \(R\), take the flat circular face in the plane \(x=0\), and the curved surface extending to \(x=R\). The generating curve is:

\[
x^2+y^2=R^2,
\qquad y^2=R^2-x^2.
\]

Then:

\[
\bar{x}=\frac{\int_0^R x(R^2-x^2)\,dx}{\int_0^R (R^2-x^2)\,dx}.
\]

Denominator:

\[
\int_0^R(R^2-x^2)\,dx
=\left[R^2x-\frac13x^3\right]_0^R
=R^3-\frac13R^3
=\frac23R^3.
\]

Numerator:

\[
\int_0^R x(R^2-x^2)\,dx
=\int_0^R(R^2x-x^3)\,dx
=\left[\frac12R^2x^2-\frac14x^4\right]_0^R
=\frac12R^4-\frac14R^4
=\frac14R^4.
\]

Therefore:

\[
\bar{x}=\frac{\frac14R^4}{\frac23R^3}
=\frac14R^4\times\frac{3}{2R^3}
=\frac38R.
\]

So the centre of mass is:

\[
\boxed{\frac38R\text{ from the centre of the plane face}}
\]

along the axis of symmetry.

## 8.10 Standard 3D Results: How to Use Them Without Re-Proving Everything

| Body | Centre of mass location |
|---|---|
| Uniform solid sphere | At the centre |
| Uniform solid cylinder | Halfway along the axis |
| Uniform solid cone of height \(H\) | \(\frac{H}{4}\) from the base, or \(\frac{3H}{4}\) from the vertex |
| Uniform solid hemisphere of radius \(R\) | \(\frac38R\) from the centre of the plane face |
| Uniform hemispherical shell of radius \(R\) | \(\frac12R\) from the centre of the plane face |
| Uniform hollow right circular cone of height \(H\) | \(\frac13H\) from the base along the axis of symmetry |

## 8.11 Composite Bodies

A composite body is made from two or more simpler bodies. Use:

\[
\sum m_ix_i=M\bar{x}.
\]

For removed pieces, use negative mass:

\[
M_Lx_L-M_Sx_S=(M_L-M_S)\bar{x}.
\]

Workflow:

1. Choose an origin.
2. Choose a positive direction.
3. Draw the axis of symmetry if there is one.
4. List each component.
5. Find its mass-ratio.
6. Find its centre-of-mass coordinate from the chosen origin.
7. Use a mass-moment table.
8. Add components, subtract holes.
9. Solve for \(\bar{x}\), \(\bar{y}\) or \(\bar{z}\).
10. State the answer with reference point and units.

| Component | Mass-ratio \(m\) | CoM coordinate \(x\) | Moment \(mx\) | Add/subtract |
|---|---:|---:|---:|---|
| Component 1 | \(m_1\) | \(x_1\) | \(m_1x_1\) | \(+\) |
| Component 2 | \(m_2\) | \(x_2\) | \(m_2x_2\) | \(+\) or \(-\) |
| Total | \(M\) | \(\bar{x}\) | \(M\bar{x}\) |  |

If two components have different densities, mass is not just volume:

\[
m=\rho V.
\]

Use \(m\propto \rho V\) in a mass-ratio table.

## 8.12 Non-Uniform Bodies

A non-uniform body has density that varies. Always start from:

\[
dm=\text{density}\times\text{small size element}.
\]

Then:

\[
M=\int dm,
\qquad
M\bar{x}=\int x\,dm.
\]

For a non-uniform solid of revolution where density is \(\rho(x)\):

\[
dm=\rho(x)\pi y^2\,dx.
\]

Then:

\[
\boxed{\bar{x}=\frac{\int_a^b x\rho(x)y^2\,dx}{\int_a^b \rho(x)y^2\,dx}}.
\]

For a non-uniform lamina under \(y=f(x)\):

\[
dm=\rho(x)y\,dx,
\]

so:

\[
\boxed{\bar{x}=\frac{\int_a^b x\rho(x)y\,dx}{\int_a^b \rho(x)y\,dx}},
\qquad
\boxed{\bar{y}=\frac{\frac12\int_a^b \rho(x)y^2\,dx}{\int_a^b \rho(x)y\,dx}}.
\]

## 8.13 Suspended Bodies

A suspended body in equilibrium has a crucial property:

\[
\boxed{\text{The centre of mass lies vertically below the point of suspension.}}
\]

This is because the body settles so that the line of action of its weight passes through the suspension point. If it did not, there would be a turning moment.

Method:

1. Draw a clean 2D cross-section.
2. Mark the suspension point \(P\).
3. Mark the centre of mass \(G\).
4. Draw the downward vertical line through \(P\).
5. Place \(G\) on that vertical line.
6. Use the geometry of the body to form a right-angled triangle.
7. Use trigonometry to find the requested angle or distance.

For a solid hemisphere of radius \(R\) suspended from a point on the rim of its base, with \(O\) the centre of the plane face and \(G\) the centre of mass:

\[
OG=\frac38R.
\]

If \(\theta\) is the angle between the axis and the downward vertical, a common setup gives:

\[
\tan\theta=\frac{R}{\frac38R}=\frac83,
\]

so:

\[
\theta=\tan^{-1}\left(\frac83\right).
\]

## 8.14 Bodies in Equilibrium Under Coplanar Forces

For a rigid body in equilibrium:

\[
\sum F_x=0,
\qquad
\sum F_y=0,
\qquad
\sum \text{moments}=0.
\]

The weight acts through the centre of mass \(G\):

\[
W=mg.
\]

For toppling, the key question is whether the vertical line through \(G\) passes inside the base of contact, through an edge, or outside.

## 8.15 Sliding on a Rough Plane

For a body on a rough inclined plane:

- \(R\) is the normal reaction;
- \(F\) is the friction force;
- \(\mu\) is the coefficient of friction;
- \(mg\) is the weight;
- \(\theta\) is the angle of the plane to the horizontal.

Resolve perpendicular to the plane:

\[
R=mg\cos\theta.
\]

The component of weight down the plane is:

\[
mg\sin\theta.
\]

At limiting sliding:

\[
F=\mu R.
\]

Thus:

\[
mg\sin\theta=\mu mg\cos\theta.
\]

Cancel \(mg\):

\[
\sin\theta=\mu\cos\theta.
\]

Divide by \(\cos\theta\):

\[
\boxed{\tan\theta=\mu}.
\]

**Rigid body warning:** this sliding condition alone does not decide whether the body topples first.

## 8.16 Toppling

A body topples when it starts to rotate about an edge or corner of its base of contact. At the point of toppling:

\[
\boxed{\text{the line of action of the weight passes through the edge of contact.}}
\]

For a rectangular block with half-width \(b\) and centre-of-mass height \(h\) above the base, the limiting toppling condition is:

\[
\boxed{\tan\theta=\frac{b}{h}}.
\]

Sliding/toppling workflow:

1. Find sliding condition using \(F\le \mu R\).
2. Find toppling condition using moment/geometry.
3. Compare thresholds.
4. State which happens first, or whether they happen simultaneously.

**Trap:** \(F=\mu R\) only at limiting sliding. If the body is just about to topple but not slide, friction may be less than its limiting value.

## 8.17 Core Theory Summary

| Situation | Mass element or mass-ratio | Moment equation |
|---|---|---|
| Particles | \(m_i\) | \(M\bar{x}=\sum m_ix_i\) |
| Lamina under \(y=f(x)\) | \(y\,dx\) | \(M\bar{x}=\int xy\,dx\), \(M\bar{y}=\frac12\int y^2\,dx\) |
| Lamina between \(y_1,y_2\) | \((y_1-y_2)\,dx\) | \(M\bar{x}=\int x(y_1-y_2)\,dx\), \(M\bar{y}=\frac12\int(y_1+y_2)(y_1-y_2)\,dx\) |
| Solid of revolution about \(x\)-axis | \(y^2\,dx\) up to constant factor | \(M\bar{x}=\int xy^2\,dx\) |
| Non-uniform solid of revolution | \(\rho(x)y^2\,dx\) up to constant factor | \(M\bar{x}=\int x\rho(x)y^2\,dx\) |
| Composite body | Component mass-ratios | \(M\bar{x}=\sum mx\) |
| Removed body | Negative component mass-ratio | \((M_1-M_2)\bar{x}=M_1x_1-M_2x_2\) |
| Suspended body | Standard/composite CoM | \(G\) vertically below suspension point |
| Sliding | Forces and friction | \(F\le \mu R\), with \(F=\mu R\) only at limiting sliding |
| Toppling | Weight line and base edge | Line of action of \(mg\) through edge at limiting toppling |

---

# 9. Visual Asset Integration

[VISUAL PLACEHOLDER: FA22FurtherCentreOfMassMermaid-001 | Source: CCEA FA22-FCOM specification boundary + teacher transcript overview | Insert from mermaid/FA22FurtherCentreOfMassMermaid-001.md | Purpose: Show how the topic grows from ordinary moments and integration into laminae, solids, composite bodies, suspended bodies, sliding and toppling.]

[VISUAL PLACEHOLDER: FA22FurtherCentreOfMassSVG-001 | Source: `FM2-Chp3-FurtherCentresOfMass-Final.pdf`, page 4, plus teacher transcript derivation | Insert from svg/FA22FurtherCentreOfMassSVG-001.svg | Purpose: Show the vertical strip model for a uniform lamina under \(y=f(x)\), with strip width \(dx\), height \(y\), and centre at \((x,\frac12y)\).]

[VISUAL PLACEHOLDER: FA22FurtherCentreOfMassSVG-002 | Source: Teacher transcript worked example with \(y_1=\sqrt{x}\), \(y_2=\frac12x\), plus screenshot visual evidence | Insert from svg/FA22FurtherCentreOfMassSVG-002.svg | Purpose: Teach why the mass strip is \(y_1-y_2\), but the vertical centre of the strip is \(\frac12(y_1+y_2)\).]

[VISUAL PLACEHOLDER: FA22FurtherCentreOfMassTikZ-001 | Source: `FM2-Chp3-FurtherCentresOfMass-Final.pdf`, page 14 | Insert from tikz/FA22FurtherCentreOfMassTikZ-001.tex | Purpose: Show a solid generated by rotating \(y=f(x)\) about the \(x\)-axis, divided into thin discs of width \(dx\).]

[VISUAL PLACEHOLDER: FA22FurtherCentreOfMassTikZ-002 | Source: Teacher transcript and slide PDF polar sector/arc examples | Insert from tikz/FA22FurtherCentreOfMassTikZ-002.tex | Purpose: Optional enrichment visual for sector and arc derivations using small angle \(d\theta\).]

[VISUAL PLACEHOLDER: FA22FurtherCentreOfMassSVG-003 | Source: CCEA FA22-FCOM boundary + supplied slide examples for cones, hemisphere and shell | Insert from svg/FA22FurtherCentreOfMassSVG-003.svg | Purpose: Compare standard 3D centre-of-mass results and reference points.]

[VISUAL PLACEHOLDER: FA22FurtherCentreOfMassSVG-004 | Source: Teacher transcript composite-body approach + CCEA FA22-FCOM-LO002 | Insert from svg/FA22FurtherCentreOfMassSVG-004.svg | Purpose: Show how component mass ratios, centre coordinates and moments combine in a table.]

[VISUAL PLACEHOLDER: FA22FurtherCentreOfMassSVG-005 | Source: CCEA FA22-FCOM-LO003 + supplied lesson evidence on suspended bodies | Insert from svg/FA22FurtherCentreOfMassSVG-005.svg | Purpose: Show that in suspended equilibrium, the centre of mass lies vertically below the suspension point.]

[VISUAL PLACEHOLDER: FA22FurtherCentreOfMassSVG-006 | Source: CCEA FA22-FCOM-LO004 + teacher transcript sliding/toppling overview | Insert from svg/FA22FurtherCentreOfMassSVG-006.svg | Purpose: Compare sliding threshold and toppling threshold for a rigid body on a rough plane.]

[VISUAL PLACEHOLDER: FA22FurtherCentreOfMassBridgeSVG-001 | Source: Ordinary A-Level Maths bridge + Further Maths specification | Insert from svg/FA22FurtherCentreOfMassBridgeSVG-001.svg | Purpose: Compare prior ordinary Maths method with Further Maths extension.]

---

# 10. Interactive Learning Widgets

[INTERACTIVE PLACEHOLDER: FA22FurtherCentreOfMassWidget-001 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FA22FurtherCentreOfMassWidget-001.html | Purpose: Help students build \(M\), \(M\bar{x}\) and \(M\bar{y}\) expressions for laminae using strips.]

This widget lets the student choose one curve or two curves, define limits, and see the mass and moment expressions. It checks the common error of using \(\frac12(y_1-y_2)\) instead of \(\frac12(y_1+y_2)\) for between-curves vertical centre.

[INTERACTIVE PLACEHOLDER: FA22FurtherCentreOfMassWidget-002 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FA22FurtherCentreOfMassWidget-002.html | Purpose: Let students build a component table for composite bodies and calculate centre of mass using mass moments.]

This widget reinforces mass ratios, subtracting holes, density ratios and reference-point warnings.

[INTERACTIVE PLACEHOLDER: FA22FurtherCentreOfMassWidget-003 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FA22FurtherCentreOfMassWidget-003.html | Purpose: Compare sliding and toppling thresholds for a rigid body on a rough plane.]

This widget reinforces \(F\le\mu R\), \(F=\mu R\) only at limiting sliding, and the toppling condition where the line of action of weight reaches the edge.

---

# 11. Worked Examples

## 11.1 Worked Example 1: Lamina Under \(y=4-x^2\)

Find the centre of mass of the uniform lamina bounded by \(y=4-x^2\), the \(x\)-axis and the \(y\)-axis.

The positive \(x\)-intercept is found from:

\[
4-x^2=0
\quad\Rightarrow\quad
x^2=4
\quad\Rightarrow\quad
x=2.
\]

For \(0\le x\le2\):

\[
M=\int_0^2(4-x^2)\,dx
=\left[4x-\frac13x^3\right]_0^2
=8-\frac83
=\frac{16}{3}.
\]

\[
M\bar{x}=\int_0^2x(4-x^2)\,dx
=\int_0^2(4x-x^3)\,dx
=\left[2x^2-\frac14x^4\right]_0^2
=8-4=4.
\]

\[
\bar{x}=\frac{4}{16/3}=4\times\frac{3}{16}=\frac34.
\]

For \(\bar{y}\):

\[
M\bar{y}=\frac12\int_0^2(4-x^2)^2\,dx.
\]

Expand:

\[
(4-x^2)^2=16-8x^2+x^4.
\]

So:

\[
M\bar{y}=\frac12\left[16x-\frac83x^3+\frac15x^5\right]_0^2.
\]

Substitute \(x=2\):

\[
M\bar{y}=\frac12\left(32-\frac{64}{3}+\frac{32}{5}\right)
=\frac12\left(\frac{480-320+96}{15}\right)
=\frac{128}{15}.
\]

Then:

\[
\bar{y}=\frac{128/15}{16/3}=\frac{128}{15}\times\frac{3}{16}=\frac85.
\]

Final answer:

\[
\boxed{(\bar{x},\bar{y})=\left(\frac34,\frac85\right)}.
\]

Teaching warning: when integrating \(x^4\), use \(\frac15x^5\), not \(\frac15x^4\).

## 11.2 Worked Example 2: Lamina Between \(y=\sqrt{x}\) and \(y=\frac12x\)

Set the curves equal:

\[
\sqrt{x}=\frac12x.
\]

Squaring:

\[
x=\frac14x^2
\quad\Rightarrow\quad
x\left(\frac14x-1\right)=0.
\]

So:

\[
x=0,\quad x=4.
\]

Let:

\[
y_1=x^{1/2},\qquad y_2=\frac12x.
\]

Mass:

\[
M=\int_0^4\left(x^{1/2}-\frac12x\right)\,dx
=\left[\frac23x^{3/2}-\frac14x^2\right]_0^4
=\frac{16}{3}-4=\frac43.
\]

\(x\)-moment:

\[
M\bar{x}=\int_0^4x\left(x^{1/2}-\frac12x\right)\,dx
=\int_0^4\left(x^{3/2}-\frac12x^2\right)\,dx.
\]

\[
M\bar{x}=\left[\frac25x^{5/2}-\frac16x^3\right]_0^4
=\frac{64}{5}-\frac{32}{3}
=\frac{32}{15}.
\]

Therefore:

\[
\bar{x}=\frac{32/15}{4/3}=\frac85.
\]

For \(\bar{y}\):

\[
M\bar{y}=\frac12\int_0^4(y_1+y_2)(y_1-y_2)\,dx.
\]

Substitute:

\[
M\bar{y}=\frac12\int_0^4\left(x^{1/2}+\frac12x\right)\left(x^{1/2}-\frac12x\right)\,dx.
\]

Use difference of two squares:

\[
\left(x^{1/2}+\frac12x\right)\left(x^{1/2}-\frac12x\right)=x-\frac14x^2.
\]

Thus:

\[
M\bar{y}=\frac12\left[\frac12x^2-\frac1{12}x^3\right]_0^4
=\frac12\left(8-\frac{16}{3}\right)
=\frac43.
\]

So:

\[
\bar{y}=\frac{4/3}{4/3}=1.
\]

Final answer:

\[
\boxed{(\bar{x},\bar{y})=\left(\frac85,1\right)}.
\]

Teaching warning: the vertical coordinate of a strip is \(\frac12(y_1+y_2)\), not \(\frac12(y_1-y_2)\).

## 11.3 Worked Example 3: Uniform Triangular Lamina Using Calculus

For vertices \((0,0),(D,0),(D,H)\), the line is \(y=\frac{H}{D}x\). The result is:

\[
M=\frac{HD}{2},
\qquad
M\bar{x}=\frac{HD^2}{3},
\qquad
M\bar{y}=\frac{H^2D}{6}.
\]

Therefore:

\[
\bar{x}=\frac{HD^2/3}{HD/2}=\frac{2D}{3},
\qquad
\bar{y}=\frac{H^2D/6}{HD/2}=\frac{H}{3}.
\]

So:

\[
\boxed{(\bar{x},\bar{y})=\left(\frac{2D}{3},\frac{H}{3}\right)}.
\]

## 11.4 Worked Example 4: Uniform Semicircular Lamina

For a right semicircular lamina of radius \(R\), symmetry gives \(\bar{y}=0\). Its mass-ratio is:

\[
M=\frac12\pi R^2.
\]

Using \(x^2+y^2=R^2\), the upper half has:

\[
y=\sqrt{R^2-x^2}.
\]

The full vertical strip is twice the upper half, so:

\[
M\bar{x}=\int_0^R2x\sqrt{R^2-x^2}\,dx.
\]

Using \(u=R^2-x^2\), \(du=-2x\,dx\):

\[
M\bar{x}=\left[-\frac23(R^2-x^2)^{3/2}\right]_0^R
=0-\left(-\frac23R^3\right)=\frac23R^3.
\]

Thus:

\[
\bar{x}=\frac{\frac23R^3}{\frac12\pi R^2}=\frac{4R}{3\pi}.
\]

Final answer:

\[
\boxed{\bar{x}=\frac{4R}{3\pi},\quad \bar{y}=0}.
\]

## 11.5 Worked Example 5: Solid of Revolution Generated by \(y=x^2+1\)

For \(y=x^2+1\), \(0\le x\le3\), rotated about the \(x\)-axis:

\[
y^2=(x^2+1)^2=x^4+2x^2+1.
\]

Denominator:

\[
\int_0^3y^2\,dx=\int_0^3(x^4+2x^2+1)\,dx
=\left[\frac15x^5+\frac23x^3+x\right]_0^3
=\frac{348}{5}.
\]

Numerator:

\[
\int_0^3xy^2\,dx=\int_0^3(x^5+2x^3+x)\,dx
=\left[\frac16x^6+\frac12x^4+\frac12x^2\right]_0^3
=\frac{333}{2}.
\]

Therefore:

\[
\bar{x}=\frac{333/2}{348/5}=\frac{333}{2}\times\frac{5}{348}=\frac{555}{232}.
\]

Final answer:

\[
\boxed{(\bar{x},\bar{y})=\left(\frac{555}{232},0\right)}.
\]

## 11.6 Worked Example 6: Uniform Solid Cone Proof

See Section 8.8. The proof gives:

\[
\boxed{\bar{x}=\frac{3H}{4}\text{ from the vertex}=\frac{H}{4}\text{ from the base}}.
\]

## 11.7 Worked Example 7: Uniform Solid Hemisphere Proof

See Section 8.9. The proof gives:

\[
\boxed{\bar{x}=\frac38R\text{ from the centre of the plane face}}.
\]

## 11.8 Worked Example 8: Composite Body with Different Densities

A cone of height \(2R\), base radius \(R\), density \(4\rho\), is joined at its base to a solid hemisphere of radius \(2R\), density \(\rho\). Let the common base centre be \(O\), with the cone side positive.

Cone volume:

\[
V_c=\frac13\pi R^2(2R)=\frac23\pi R^3.
\]

Cone mass-ratio:

\[
m_c=4\rho V_c=\frac83\rho\pi R^3.
\]

Use \(m_c=\frac83\). Cone centre is \(\frac14(2R)=\frac{R}{2}\) from the base:

\[
x_c=\frac{R}{2}.
\]

Hemisphere volume:

\[
V_h=\frac23\pi(2R)^3=\frac{16}{3}\pi R^3.
\]

Use \(m_h=\frac{16}{3}\). Hemisphere centre is:

\[
\frac38(2R)=\frac{3R}{4}
\]

from its plane face, on the negative side:

\[
x_h=-\frac{3R}{4}.
\]

Total mass-ratio:

\[
M=\frac83+\frac{16}{3}=8.
\]

Moment sum:

\[
\frac83\cdot\frac{R}{2}+\frac{16}{3}\cdot\left(-\frac{3R}{4}\right)
=\frac{4R}{3}-4R
=-\frac{8R}{3}.
\]

Therefore:

\[
8\bar{x}=-\frac{8R}{3},
\qquad
\bar{x}=-\frac{R}{3}.
\]

So:

\[
\boxed{\frac{R}{3}\text{ into the hemisphere from }O}.
\]

## 11.9 Worked Example 9: Suspended Solid Hemisphere

For a solid hemisphere of radius \(R\) suspended from a point \(A\) on the rim of its plane face, let \(O\) be the centre of the plane face and \(G\) the centre of mass.

\[
OA=R,
\qquad
OG=\frac38R.
\]

In equilibrium, \(G\) lies vertically below \(A\). If \(\theta\) is the angle between the axis of symmetry and the downward vertical, then:

\[
\tan\theta=\frac{OA}{OG}=\frac{R}{\frac38R}=\frac83.
\]

So:

\[
\boxed{\theta=\tan^{-1}\left(\frac83\right)}.
\]

## 11.10 Worked Example 10: Sliding Before Toppling, or Toppling Before Sliding

For a uniform rectangular block of height \(2h\), base width \(2b\), coefficient of friction \(\mu\), on a plane inclined at \(\theta\):

Sliding threshold:

\[
R=mg\cos\theta,
\qquad
mg\sin\theta=\mu R.
\]

Thus:

\[
mg\sin\theta=\mu mg\cos\theta
\quad\Rightarrow\quad
\tan\theta=\mu.
\]

Toppling threshold:

\[
\tan\theta=\frac{b}{h}.
\]

Sliding first if:

\[
\mu<\frac{b}{h}.
\]

Toppling first if:

\[
\mu>\frac{b}{h}.
\]

Simultaneous if:

\[
\mu=\frac{b}{h}.
\]

---

# 12. Common Mistakes and Exam Traps

1. Forgetting the \(\frac12\) in \(M\bar{y}=\frac12\int y^2\,dx\).
2. Using \(\frac12(y_1-y_2)\) instead of \(\frac12(y_1+y_2)\) for a between-curves strip centre.
3. Using wrong integration limits.
4. Dropping \(\rho\) or \(\pi\) without explaining that they cancel.
5. Mixing up solid and shell results:
   - solid cone: \(\frac14H\) from base;
   - hollow cone: \(\frac13H\) from base;
   - solid hemisphere: \(\frac38R\) from plane face;
   - hemispherical shell: \(\frac12R\) from plane face.
6. Giving a distance without saying “from where”.
7. Treating a removed body as positive.
8. Assuming \(F=\mu R\) too early.
9. Confusing sliding and toppling.
10. Forgetting units.

---

# 13. Practice Questions

These are AI-generated on-spec practice questions. They are not past-paper questions and should not be labelled as textbook or CCEA questions.

## 13.1 Basic Fluency Questions

### Question 1: Lamina under one curve

A uniform lamina is bounded by:

\[
y=3x-x^2,
\]

the \(x\)-axis, and the lines:

\[
x=0,
\quad x=3.
\]

Find the coordinates of its centre of mass.

### Question 2: Lamina between two curves

A uniform lamina is bounded by:

\[
y=x
\]

and:

\[
y=x^2
\]

between their points of intersection. Find its centre of mass.

### Question 3: Solid of revolution

The region under:

\[
y=\sqrt{x}
\]

from \(x=0\) to \(x=4\) is rotated about the \(x\)-axis to form a uniform solid. Find the centre of mass.

## 13.2 Bridge Questions

### Question 4: Moment of mass bridge

A uniform lamina under \(y=f(x)\) between \(x=a\) and \(x=b\) is divided into vertical strips. Explain why:

\[
M\bar{x}=\int_a^bxy\,dx.
\]

Your answer must refer to area of a strip, mass of a strip, location of the strip, and why force/weight is not needed explicitly.

### Question 5: Between-curves midpoint warning

For a lamina between \(y_1=\sqrt{x}\) and \(y_2=\frac12x\), a student writes:

\[
M\bar{y}=\frac12\int_0^4(y_1-y_2)^2\,dx.
\]

Explain why this is wrong and write the correct expression for \(M\bar{y}\).

## 13.3 Standard Exam-Style Questions

### Question 6: Solid cone from first principles

A uniform solid right circular cone has height \(h\) and base radius \(r\). Use calculus to prove that its centre of mass lies \(\frac14h\) from the base.

### Question 7: Composite solid

A uniform solid cylinder of radius \(R\) and height \(4R\) is joined to a uniform solid cone of base radius \(R\) and height \(3R\). The base of the cone is attached to the top circular face of the cylinder, and the axes coincide. Find the distance of the centre of mass from the base of the cylinder.

### Question 8: Suspended body

A uniform solid hemisphere of radius \(R\) is suspended from a point on the rim of its plane face. Given that the centre of mass is \(\frac38R\) from the centre of the plane face, find the angle between the axis of symmetry and the downward vertical.

## 13.4 Harder Synthesis Questions

### Question 9: Non-uniform solid of revolution

A solid is formed by rotating \(y=x\) between \(x=0\) and \(x=a\) about the \(x\)-axis. The mass per unit volume at distance \(x\) from the origin is proportional to \(x\). Find the distance of the centre of mass from the origin.

### Question 10: Sliding and toppling comparison

A uniform rectangular block has height \(2h\) and base width \(2b\). It rests on a rough plane inclined at angle \(\theta\) to the horizontal. The coefficient of friction is \(\mu\). Show that sliding is limiting when \(\tan\theta=\mu\), toppling is limiting when \(\tan\theta=\frac{b}{h}\), and state the condition for toppling before sliding.

---

# 14. Worked Solutions

## 14.1 Solution to Question 1

For \(y=3x-x^2\), \(0\le x\le3\):

\[
M=\int_0^3(3x-x^2)\,dx
=\left[\frac32x^2-\frac13x^3\right]_0^3
=\frac{27}{2}-9=\frac92.
\]

\[
M\bar{x}=\int_0^3x(3x-x^2)\,dx
=\int_0^3(3x^2-x^3)\,dx
=\left[x^3-\frac14x^4\right]_0^3
=27-\frac{81}{4}=\frac{27}{4}.
\]

\[
\bar{x}=\frac{27/4}{9/2}=\frac32.
\]

For \(\bar{y}\):

\[
M\bar{y}=\frac12\int_0^3(3x-x^2)^2\,dx.
\]

Expand:

\[
(3x-x^2)^2=9x^2-6x^3+x^4.
\]

Then:

\[
M\bar{y}=\frac12\left[3x^3-\frac32x^4+\frac15x^5\right]_0^3
=\frac12\left(81-\frac{243}{2}+\frac{243}{5}\right).
\]

Use denominator \(10\):

\[
81-\frac{243}{2}+\frac{243}{5}
=\frac{810-1215+486}{10}=\frac{81}{10}.
\]

So:

\[
M\bar{y}=\frac{81}{20}.
\]

\[
\bar{y}=\frac{81/20}{9/2}=\frac9{10}.
\]

Final answer:

\[
\boxed{(\bar{x},\bar{y})=\left(\frac32,\frac9{10}\right)}.
\]

## 14.2 Solution to Question 2

Intersection points:

\[
x=x^2\Rightarrow x(x-1)=0\Rightarrow x=0,1.
\]

For \(0<x<1\), \(y_1=x\), \(y_2=x^2\).

\[
M=\int_0^1(x-x^2)\,dx
=\left[\frac12x^2-\frac13x^3\right]_0^1
=\frac12-\frac13=\frac16.
\]

\[
M\bar{x}=\int_0^1x(x-x^2)\,dx
=\int_0^1(x^2-x^3)\,dx
=\left[\frac13x^3-\frac14x^4\right]_0^1
=\frac13-\frac14=\frac1{12}.
\]

\[
\bar{x}=\frac{1/12}{1/6}=\frac12.
\]

\[
M\bar{y}=\frac12\int_0^1(x+x^2)(x-x^2)\,dx
=\frac12\int_0^1(x^2-x^4)\,dx.
\]

\[
M\bar{y}=\frac12\left[\frac13x^3-\frac15x^5\right]_0^1
=\frac12\left(\frac13-\frac15\right)
=\frac1{15}.
\]

\[
\bar{y}=\frac{1/15}{1/6}=\frac25.
\]

Final answer:

\[
\boxed{(\bar{x},\bar{y})=\left(\frac12,\frac25\right)}.
\]

## 14.3 Solution to Question 3

For \(y=\sqrt{x}\), \(y^2=x\). A solid of revolution about the \(x\)-axis has:

\[
\bar{x}=\frac{\int_0^4xy^2\,dx}{\int_0^4y^2\,dx}.
\]

Denominator:

\[
\int_0^4x\,dx=\left[\frac12x^2\right]_0^4=8.
\]

Numerator:

\[
\int_0^4x^2\,dx=\left[\frac13x^3\right]_0^4=\frac{64}{3}.
\]

Therefore:

\[
\bar{x}=\frac{64/3}{8}=\frac83.
\]

Final answer:

\[
\boxed{(\bar{x},\bar{y})=\left(\frac83,0\right)}.
\]

## 14.4 Solution to Question 4

A thin vertical strip has width \(dx\), height \(y\), and area:

\[
dA=y\,dx.
\]

For a uniform lamina with mass per unit area \(\rho\):

\[
dm=\rho y\,dx.
\]

The strip is located at horizontal distance \(x\), so its moment about the \(y\)-axis is:

\[
x\,dm=x\rho y\,dx.
\]

Summing all strips:

\[
M\bar{x}=\int_a^b\rho xy\,dx.
\]

In mass-ratio form, \(\rho\) cancels, so:

\[
\boxed{M\bar{x}=\int_a^bxy\,dx}.
\]

Weight is not needed explicitly because every weight would contain the common factor \(g\), which cancels.

## 14.5 Solution to Question 5

The height of the strip is \(y_1-y_2\), but the vertical coordinate of the centre of the strip is:

\[
\frac{y_1+y_2}{2}.
\]

Therefore:

\[
\boxed{M\bar{y}=\frac12\int_0^4(y_1+y_2)(y_1-y_2)\,dx}.
\]

For \(y_1=\sqrt{x}\), \(y_2=\frac12x\):

\[
\boxed{M\bar{y}=\frac12\int_0^4\left(\sqrt{x}+\frac12x\right)\left(\sqrt{x}-\frac12x\right)\,dx}.
\]

## 14.6 Solution to Question 6

With vertex at \(x=0\), base at \(x=h\), and generating line \(y=\frac{r}{h}x\):

\[
y^2=\frac{r^2}{h^2}x^2.
\]

Denominator:

\[
\int_0^hy^2\,dx=\frac{r^2}{h^2}\left[\frac13x^3\right]_0^h=\frac13r^2h.
\]

Numerator:

\[
\int_0^hxy^2\,dx=\frac{r^2}{h^2}\left[\frac14x^4\right]_0^h=\frac14r^2h^2.
\]

Therefore:

\[
\bar{x}=\frac{\frac14r^2h^2}{\frac13r^2h}=\frac34h
\]

from the vertex. Hence distance from the base is:

\[
h-\frac34h=\frac14h.
\]

## 14.7 Solution to Question 7

Let \(x=0\) at the base of the cylinder, upward positive.

Cylinder:

\[
V_c=\pi R^2(4R)=4\pi R^3,
\qquad x_c=2R.
\]

Moment:

\[
m_cx_c=4\pi R^3(2R)=8\pi R^4.
\]

Cone:

\[
V_k=\frac13\pi R^2(3R)=\pi R^3.
\]

The cone centre is \(\frac14(3R)=\frac{3R}{4}\) above its base, and the cone base is at \(x=4R\), so:

\[
x_k=4R+\frac{3R}{4}=\frac{19R}{4}.
\]

Moment:

\[
m_kx_k=\pi R^3\cdot\frac{19R}{4}=\frac{19}{4}\pi R^4.
\]

Total mass:

\[
M=5\pi R^3.
\]

Total moment:

\[
M\bar{x}=8\pi R^4+\frac{19}{4}\pi R^4=\frac{51}{4}\pi R^4.
\]

Therefore:

\[
\bar{x}=\frac{\frac{51}{4}\pi R^4}{5\pi R^3}=\frac{51R}{20}.
\]

## 14.8 Solution to Question 8

Let \(O\) be the centre of the plane face, \(A\) the suspension point, and \(G\) the centre of mass.

\[
OA=R,
\qquad OG=\frac38R.
\]

In equilibrium, \(G\) lies vertically below \(A\). If \(\theta\) is the angle between the axis and the downward vertical:

\[
\tan\theta=\frac{OA}{OG}=\frac{R}{\frac38R}=\frac83.
\]

Thus:

\[
\boxed{\theta=\tan^{-1}\left(\frac83\right)}.
\]

## 14.9 Solution to Question 9

Density is proportional to \(x\), so write \(\rho(x)=kx\). Since \(y=x\), \(y^2=x^2\). For a disc:

\[
dm=kx\pi y^2\,dx=k\pi x^3\,dx.
\]

Total mass:

\[
M=k\pi\int_0^a x^3\,dx=k\pi\left[\frac14x^4\right]_0^a=\frac14k\pi a^4.
\]

Moment:

\[
M\bar{x}=\int_0^a x\,dm=k\pi\int_0^a x^4\,dx=k\pi\left[\frac15x^5\right]_0^a=\frac15k\pi a^5.
\]

Therefore:

\[
\bar{x}=\frac{\frac15k\pi a^5}{\frac14k\pi a^4}=\frac45a.
\]

## 14.10 Solution to Question 10

Sliding:

\[
R=mg\cos\theta,
\qquad mg\sin\theta=\mu R.
\]

So:

\[
mg\sin\theta=\mu mg\cos\theta
\Rightarrow
\tan\theta=\mu.
\]

Toppling:

At limiting toppling, the line of action of weight passes through the downhill edge. The centre of mass is height \(h\) above the base and horizontal half-width \(b\) from the edge, so:

\[
\tan\theta=\frac{b}{h}.
\]

Toppling happens before sliding if:

\[
\frac{b}{h}<\mu.
\]

So:

\[
\boxed{\mu>\frac{b}{h}}.
\]

---

# 15. Exam Technique Notes

## 15.1 Start every question by identifying the body type

| Body type | First thought |
|---|---|
| Lamina under one curve | \(M=\int y\,dx\) |
| Lamina between two curves | \(M=\int(y_1-y_2)\,dx\) |
| Solid of revolution | \(M\propto\int y^2\,dx\) |
| Composite body | Mass-moment table |
| Suspended body | \(G\) vertically below suspension point |
| Sliding | \(F\le \mu R\) |
| Toppling | Weight line through edge at limiting case |

## 15.2 Define your origin and direction

For composite and 3D problems, write something like:

```text
Take x=0 at the base, with positive x vertically upwards.
```

## 15.3 Show enough integration

If the question says “using calculus” or “show”, do not jump straight from integral to answer. Show the antiderivative and substitution into limits.

## 15.4 Use exact values

Keep \(\frac85\) instead of \(1.6\), unless a decimal is requested.

## 15.5 Check plausibility

Check that the centre of mass lies in a plausible place. A cone’s centre is nearer its base than its vertex. A density increasing with \(x\) should pull \(\bar{x}\) towards larger \(x\).

## 15.6 Do not overuse formulae without checking reference points

Write:

\[
\frac14h\text{ from the base}
\]

not just \(\frac14h\).

## 15.7 In sliding/toppling questions, run two tests

Sliding test:

\[
F\le \mu R.
\]

Toppling test:

\[
\text{line of action of }mg\text{ through edge at limiting toppling.}
\]

Then compare.

---

# 16. Syllabus Gap Check

## 16.1 LO Coverage Table

| LO ID | Official wording | Covered? | Evidence strength | Notes |
|---|---|---:|---|---|
| FA22-FCOM-LO001 | find the centre of mass of laminae and solids, including the use of calculus | Yes | Strong | Laminae, between curves, solids of revolution, cone proof and hemisphere proof included. |
| FA22-FCOM-LO002 | find the centre of mass of composite bodies | Yes | Moderate-strong | Composite table method and density-ratio example included. |
| FA22-FCOM-LO003 | solve problems involving suspended bodies | Yes | Moderate | Suspended hemisphere example included; more CCEA-style examples would strengthen this. |
| FA22-FCOM-LO004 | solve sliding and toppling problems | Yes | Moderate | General block example included; more varied rigid body/sloped plane examples would strengthen this. |

## 16.2 Evidence Coverage Table

| Evidence area | Used? | Where |
|---|---:|---|
| Transcript chapter overview | Yes | Sections 1, 6, 8 |
| Lamina calculus derivation | Yes | Sections 8.2, 11.1, 11.2 |
| Between-curves warning | Yes | Sections 8.3, 11.2, 12.2 |
| Standard lamina proofs | Yes | Sections 8.5, 11.3, 11.4 |
| Polar sector/arc examples | Yes, enrichment only | Section 8.6 |
| Volumes of revolution | Yes | Sections 8.7, 11.5 |
| Solid cone proof | Yes | Sections 8.8, 11.6, 14.6 |
| Solid hemisphere proof | Yes | Sections 8.9, 11.7 |
| Composite/density bodies | Yes | Sections 8.11, 8.12, 11.8 |
| Suspended bodies | Yes | Sections 8.13, 11.9 |
| Sliding/toppling | Yes | Sections 8.15, 8.16, 11.10 |

## 16.3 Bridge Coverage Table

| Bridge area | Covered? | Sections |
|---|---:|---|
| Ordinary integration to mass integrals | Yes | 5, 8.2, 8.3 |
| Area between curves to strip mass | Yes | 8.3, 11.2 |
| Volumes of revolution to solid mass | Yes | 8.7, 11.5 |
| Moments of force to moments of mass | Yes | 5, 7, 14.4 |
| Friction to sliding | Yes | 8.15, 11.10, 14.10 |
| Rigid-body geometry to toppling | Yes | 8.16, 11.10, 14.10 |

## 16.4 Off-Spec Content Found but Excluded

| Content | Decision |
|---|---|
| Banked corners, overturning on banked tracks | Excluded from core because it belongs to `FA22-FCM`, not `FA22-FCOM`. |
| Edexcel specification wording | Not used as authority; only used as supporting evidence where aligned with CCEA. |
| Pearson exercise labels and page references | Not treated as CCEA content. |
| Full textbook examples not visible in supplied evidence | Not claimed or reproduced. |

## 16.5 Optional Enrichment Not Required by CCEA

| Enrichment | Why included |
|---|---|
| Sector proof using polar integration | Appears in supplied evidence and strengthens understanding of continuous mass elements. |
| Arc proof using polar integration | Appears in supplied evidence and reinforces \(d\theta\)-based mass elements. |
| Hemispherical shell proof by limiting process | Mentioned in evidence but not fully developed as a core proof. Standard result can be used if supplied/known. |
| Extra widget proposals | AI-proposed teaching enhancements, not evidence-backed lesson content. |

## 16.6 Weak Evidence Warnings

| Issue | Warning |
|---|---|
| Screenshot PDF text not parsed | Visual details are used only where visible. No hidden diagram details are claimed. |
| Some slide PDF pages truncated in parsed view | The lesson relies on visible parsed snippets, screenshots and transcript for those areas. |
| CCEA formula booklet not supplied | Standard result list is based on topic evidence and common Further Mechanics results; reference-point wording is emphasised. |
| Exact CCEA mark scheme phrasing not supplied | Exam technique notes are generated from mathematical requirements, not unseen mark schemes. |

---

# 17. Recommended Enhancements Not in the Evidence

The following are proposed enhancements for the portal. They are not evidence-backed claims and should be labelled as teaching enhancements:

- a strip detective diagram comparing \(y\,dx\), \(xy\,dx\), and \(\frac12y^2\,dx\);
- a between-curves midpoint visual;
- a standard solids reference card;
- a frustum-as-large-cone-minus-small-cone diagram;
- a suspended body cross-section;
- a sliding-versus-toppling threshold graph;
- animations for strips, solids of revolution, reaction shift and suspended-body rotation;
- widgets for lamina integrals, composite tables and sliding/toppling classification.

---

# 18. Supplementary Sources Used

## 18.1 Project Sources

| Source | Role |
|---|---|
| `CCEA_GCE_Further_Mathematics_Specification_Map.md` | Syllabus authority for `FA22-FCOM`. |
| `Further_Maths_README_module_map.md` | Topic mapping and bridge support. |
| `Further_Maths_EVIDENCE_DROP_CHECKLIST.md` | Evidence workflow and missing evidence structure. |
| `Ordinary_A_Level_Maths_Bridge_Spec_Extracts.md` | Ordinary A-Level Maths bridge context only. |
| `Further Maths Portal Build – Knowledge Evidence.txt` | General portal context. |

## 18.2 Lesson-Specific Sources

| Source | Role |
|---|---|
| `transcripts.md` | Main teacher explanation evidence for calculus derivations, examples, warnings and applied modelling comments. |
| `FM2-Chp3-FurtherCentresOfMass-Final.pdf` | Slide/PDF evidence for formulae, diagrams, examples and structure. |
| `Chapter_3_Further_Centres_of_Mass_(A2)_🚗_(Further_Mechanics_2)_screenshots.pdf` | Visual evidence where visible; no searchable text parsed. |

## 18.3 Ordinary A-Level Maths Sources

Ordinary A-Level Maths sources are used only as bridge context for integration, areas, volumes of revolution, moments, friction and trigonometry. They do not override the CCEA Further Mathematics specification.

## 18.4 Cross-Board Sources

The slide/PDF evidence includes Edexcel/Pearson-style material. It is used only where its mathematical content matches the CCEA `FA22-FCOM` boundary. Cross-board content is not used as syllabus authority.

## 18.5 Evidence Limitations

1. The screenshot PDF did not provide parsed searchable text.
2. The supplied PDF snippets were partially truncated in the conversation context.
3. The official CCEA formula booklet was not supplied.
4. Full textbook pages referenced in the slide deck were not supplied.
5. No CCEA mark schemes were supplied for this topic.

---

# 19. Final Student Checklist

## 19.1 Prerequisite Confidence Checklist

- [ ] integrate powers of \(x\);
- [ ] expand squared brackets such as \((4-x^2)^2\);
- [ ] find intersections of curves;
- [ ] find areas between curves;
- [ ] use volumes of revolution;
- [ ] take moments about a point;
- [ ] resolve forces on an inclined plane;
- [ ] use \(F\le\mu R\);
- [ ] use exact fractions confidently;
- [ ] sketch basic curves and label axes.

## 19.2 Further Centre-of-Mass Method Checklist

- [ ] write \(M\bar{x}=\sum mx\);
- [ ] replace sums with integrals for continuous bodies;
- [ ] derive \(M=\int y\,dx\) for a lamina;
- [ ] derive \(M\bar{x}=\int xy\,dx\);
- [ ] derive \(M\bar{y}=\frac12\int y^2\,dx\);
- [ ] adapt formulae for regions between curves;
- [ ] use \(M\propto\int y^2\,dx\) for solids of revolution;
- [ ] prove the solid cone result;
- [ ] prove the solid hemisphere result;
- [ ] use a component table for composite bodies;
- [ ] subtract removed bodies correctly;
- [ ] include density ratios when needed;
- [ ] identify when symmetry gives a coordinate.

## 19.3 Exam Technique Checklist

- [ ] define the origin;
- [ ] define the positive direction;
- [ ] write the correct limits;
- [ ] show integrals before evaluating;
- [ ] keep exact fractions;
- [ ] state “from the base”, “from the vertex” or “from the plane face”;
- [ ] draw a diagram for suspended bodies;
- [ ] draw a force diagram for sliding/toppling;
- [ ] check sliding and toppling separately;
- [ ] avoid \(F=\mu R\) unless limiting sliding is stated or proved.

## 19.4 Bridge Checklist

- [ ] ordinary area integration becomes mass integration;
- [ ] ordinary volume of revolution becomes solid mass modelling;
- [ ] ordinary moments of forces become moments of mass;
- [ ] ordinary friction is only one part of sliding/toppling;
- [ ] old formulae still work, but reference points matter more than ever.

## 19.5 Diagram and Visual Understanding Checklist

- [ ] explain what \(dx\) represents in a lamina strip;
- [ ] explain why the centre of a strip under \(y=f(x)\) is at height \(\frac12y\);
- [ ] explain why the centre of a strip between two curves is at \(\frac12(y_1+y_2)\);
- [ ] explain why a disc of revolution has volume \(\pi y^2\,dx\);
- [ ] explain why a suspended body has \(G\) vertically below the suspension point;
- [ ] explain why toppling occurs when the weight line passes through the edge.
