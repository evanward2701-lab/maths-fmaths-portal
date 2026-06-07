# FA22 Restitution: Elastic Collisions in Two Dimensions

## 1. Lesson Title and Metadata

| Field | Value |
|---|---|
| Date generated | 2026-06-05 |
| Course | CCEA GCE Further Mathematics |
| Unit | `FA22` – Further A2 2 Applied Mathematics |
| Applied section | Section B: Mechanics 2 |
| Topic code | `FA22-REST` |
| CCEA topic name | Restitution |
| Lesson topic name | Elastic Collisions in Two Dimensions |
| Topic slug | `restitution_elastic_collisions_in_two_dimensions` |
| Topic Pascal | `RestitutionElasticCollisionsInTwoDimensions` |
| Topic ID | `FA22RestitutionElasticCollisionsInTwoDimensions` |
| Lesson file | `FA22_restitution_elastic_collisions_in_two_dimensions_lesson.md` |
| LO IDs | `FA22-REST-LO001`, `FA22-REST-LO002` |
| Bridge tags | A22 Impulse and Momentum; AS2 Kinematics; AS/A2 vectors; trigonometry |
| Topic tags | `#FA22`, `#REST`, `#Mechanics2`, `#Restitution`, `#Collisions`, `#SmoothSpheres`, `#FixedPlane`, `#Impulse`, `#Momentum`, `#NewtonLawRestitution` |

This lesson belongs to `FA22 – Further A2 2 Applied Mathematics`, Section B: Mechanics 2, Topic `FA22-REST`, Restitution.

The official CCEA learning outcomes preserved in this lesson are:

```text
FA22-REST-LO001
FA22-REST-LO002
```

This lesson teaches Newton’s law of restitution and elastic collisions using two-dimensional component ideas. The core CCEA-safe content is Newton’s law of restitution, smooth sphere and fixed plane collisions, smooth sphere and smooth sphere collisions, impulse and momentum in the direction of impact, and smoothness causing no tangential impulse.

The uploaded evidence goes further into Edexcel/Pearson-style oblique two-dimensional collisions and scalar product shortcuts. These are used carefully as method support, but the CCEA boundary remains `FA22-REST`.

---

## 2. Evidence Map

| Source | Lesson use |
|---|---|
| CCEA Further Mathematics specification map | Governs `FA22-REST`, official LO IDs and boundary |
| Further Maths README module map | Confirms bridge route from A22 Impulse and Momentum and AS2 Kinematics |
| Ordinary A-Level Maths bridge extracts | Used only for prerequisite context |
| `FM1-Chp5-ObliqueCollisions.pdf` | Main lesson-specific PDF evidence |
| `Chapter_5_Elastic_Collisions_in_Two_Dimensions_🎯_(Further_Mechanics_1)_screenshots.pdf` | Visual evidence, including handwritten annotations |
| `transcripts.md` | Teacher explanation, warnings, diagram interpretations |
| Cross-board examples inside evidence | Used as worked-example-style evidence or enrichment, never labelled CCEA |

The lesson PDF begins by identifying the chapter as Elastic Collisions in Two Dimensions and introduces oblique impact with a fixed smooth surface and collisions between two spheres not travelling along the same straight line.

The same PDF states the key modelling condition: all the spheres and all the surfaces are always smooth.

The consequence-of-smoothness slide says that a smooth surface cannot apply a frictional force, so it can only apply a normal reaction force; hence the impulse is normal to the surface, and the component of momentum and velocity parallel to the surface is unchanged.

---

## 3. Specification Alignment

| LO ID | Official wording | Lesson coverage | Evidence source | Syllabus boundary | Bridge |
|---|---|---|---|---|---|
| `FA22-REST-LO001` | demonstrate understanding of and use Newton’s law of restitution | Defines \(e\), speed of separation / speed of approach, \(0\le e\le 1\), and applies restitution in the normal direction | CCEA spec map; lesson PDF; transcript | Core | A22 impulse and momentum |
| `FA22-REST-LO002` | solve problems involving direct elastic collisions between smooth spheres or between a smooth sphere and a fixed plane | Solves fixed-plane and sphere-sphere collisions by resolving into normal and tangential components | CCEA spec map; lesson PDF; transcript | Core with boundary caution for oblique 2D cross-board examples | AS2 kinematics, A22 impulse/momentum, vector components |

The phrase direct elastic collisions in the CCEA map is the controlling phrase. The lesson does not treat every cross-board oblique impact example as automatically core. Instead, it teaches the confirmed CCEA mechanics of restitution and shows how two-dimensional component resolution can reduce an oblique collision to the direct normal collision that CCEA explicitly requires.

---

## 4. Learning Objectives

### Core Further Maths objectives

By the end of this lesson, you should be able to:

1. State and use Newton’s law of restitution.
2. Explain why a smooth surface gives no tangential impulse.
3. Resolve a velocity into components parallel and perpendicular to a smooth surface.
4. Use the fact that the parallel component of velocity is unchanged in a smooth impact.
5. Use the coefficient of restitution \(e\) to connect the normal component before impact to the normal component after impact.
6. Solve fixed smooth plane collision problems using component equations.
7. Solve smooth sphere collision problems using the line of centres and common tangent.
8. Use conservation of momentum in the line of impact when two smooth spheres collide.
9. Calculate impulse using change in momentum.
10. Calculate loss of kinetic energy where required.

### Bridge objectives

You should also be able to connect this lesson to ordinary A-Level Mathematics by recognising that \(I=m(v-u)\) from impulse and momentum becomes vector-based when velocities are vectors, recognising that \(\frac12mv^2\) uses speed rather than vector velocity, using trigonometry to split velocities into components, using Pythagoras to rebuild a speed from perpendicular components, and using scalar product ideas to find components in arbitrary directions.

### Exam technique objectives

You should be able to draw a before-and-after collision diagram, label the direction of impulse clearly, decide which component is unchanged, decide where Newton’s law of restitution applies, avoid mixing up angle to wall, angle to normal, angle to line of centres and angle of deflection, and label cross-board-style practice as practice, not CCEA past-paper content.

---

## 5. Explicit Prerequisite Recap

### 5.1 GCSE foundations

| GCSE / early algebra skill | Why it matters here |
|---|---|
| Rearranging equations | Restitution equations often need to be solved simultaneously. |
| Pythagoras’ theorem | Used to rebuild speed from perpendicular velocity components. |
| Trigonometry in right-angled triangles | Used to split oblique velocities into parallel and perpendicular components. |
| Angles on straight lines and between lines | Used when interpreting angle of approach, angle of rebound and angle of deflection. |
| Exact values such as \(\sin 60^\circ=\frac{\sqrt3}{2}\), \(\cos60^\circ=\frac12\), \(\sin45^\circ=\cos45^\circ=\frac1{\sqrt2}\) | These appear naturally in collision diagrams. |

This topic is a geometry engine wearing mechanics clothing. The diagram is not a decoration; it is the gearbox.

### 5.2 Ordinary A-Level Mathematics foundations

| Ordinary A-Level idea | Prior version | Further Maths upgrade |
|---|---|---|
| Velocity | Usually one-dimensional or simple vector motion | Velocity is split into directions parallel and perpendicular to the surface or line of centres. |
| Momentum | \(p=mv\) in a chosen straight-line direction | Momentum is handled in the impact direction, and sometimes as a vector. |
| Impulse | \(I=m(v-u)\) | Impulse has a direction and may be written as a vector change in momentum. |
| Coefficient of restitution | \(e=\dfrac{\text{speed of separation}}{\text{speed of approach}}\) in 1D | The same law applies only along the normal / line of impact. |
| Kinetic energy | \(\frac12mv^2\) | \(v\) must be the speed, so with vectors you first find the magnitude. |

### A-Level Maths Bridge: What You Already Know and What Further Maths Changes

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| A22 Impulse and Momentum | Collisions in one dimension, impulse as change in momentum, and coefficient of restitution foundations | Collisions are now handled by choosing the correct impact direction and resolving velocities | A one-dimensional sign convention is not enough unless the chosen axis is the normal / line of centres |
| AS2 Kinematics | Velocity, speed, components and vector motion | Speed after collision may be found using Pythagoras from components | Do not use a vector where a scalar speed is required |
| AS/A2 Trigonometry | \(\sin\), \(\cos\), \(\tan\), exact angles, identities | Oblique collisions use component triangles, often with \(\sin^2\theta+\cos^2\theta=1\) | If the angle is measured from the wall rather than the normal, sine and cosine swap roles |
| AS/A2 Vectors | \(\mathbf{i}\), \(\mathbf{j}\), magnitude, scalar product | Scalar product can project a velocity onto a wall or impulse direction | Unit vectors may clutter the algebra; if both sides use the same direction vector, scale factors may cancel |
| Ordinary Mechanics modelling | Smooth contact means no friction | Smooth impact means no tangential impulse, so the parallel velocity component is unchanged | Forgetting the smooth assumption ruins the whole model |

In ordinary A-Level Maths, this idea appeared as one-dimensional collision algebra: choose a direction, write momentum and restitution equations, solve. In Further Maths, the same idea becomes a direction-choice problem. The key upgrade is that the collision only acts along one special direction, the normal to the surface or the line of centres. The danger is treating the whole velocity as if it were changed by \(e\). It is not. Only the normal component obeys the restitution law.

---

## 6. Big Picture Explanation

In ordinary one-dimensional collisions, everything happens on a single line. In two dimensions, an object can approach a wall or another sphere at an angle. At first glance, the collision looks like a storm of arrows. The rescue trick is to split the motion into two perpendicular directions:

\[
\text{parallel to the contact surface}
\]

and

\[
\text{perpendicular to the contact surface}.
\]

Only the perpendicular direction is affected by the normal impulse. The parallel direction glides through untouched.

### Modelling context

| Assumption | Meaning | Mathematical consequence |
|---|---|---|
| Smooth surface | No friction acts at contact | No impulse parallel to the surface |
| Smooth sphere | Contact force acts along the normal / line of centres | Tangential components are unchanged |
| Fixed plane | The wall or plane does not move | Only the sphere’s velocity changes |
| Instantaneous collision | The impact time is very small | Weight or other non-impulsive forces are ignored during impact |
| Coefficient of restitution \(e\) | Measures elasticity of impact | Normal speed of separation \(=e\) times normal speed of approach |
| \(0\le e\le1\) | Physical collision range in this model | \(e=1\) perfectly elastic, \(e=0\) no rebound in normal direction |

When you meet a collision question, ask: what is the contact surface or line of centres, which component is parallel, which component is perpendicular, which component is unchanged, which component obeys Newton’s law of restitution, and is the answer asking for velocity, speed, angle, impulse or kinetic energy?

---

## 7. Key Definitions and Notation

### Smooth surface

A smooth surface is a surface that exerts no frictional force during contact. Therefore, during impact:

\[
F_r=0.
\]

The reaction force acts normal to the surface.

### Normal direction

The normal direction is the direction perpendicular to the surface at the point of contact. For a fixed smooth plane:

\[
\text{normal direction} \perp \text{plane}.
\]

For two smooth spheres:

\[
\text{normal direction}=\text{line of centres at impact}.
\]

### Tangential / parallel direction

The tangential direction is parallel to the surfaces in contact. In the smooth model, no impulse acts in this direction, so the tangential component of velocity remains unchanged.

### Coefficient of restitution

The coefficient of restitution is denoted by \(e\), where

\[
0\le e\le 1.
\]

Newton’s law of restitution states:

\[
e=\frac{\text{speed of separation}}{\text{speed of approach}}.
\]

This must be applied along the line of impact only.

### Velocity notation

Use \(u\) for the speed before collision and \(v\) for the speed after collision.

For a wall collision diagram:

- \(\alpha\) = angle of approach measured to the wall or plane;
- \(\beta\) = angle of rebound measured to the wall or plane;
- \(u\cos\alpha\) = component parallel to the wall if \(\alpha\) is measured to the wall;
- \(u\sin\alpha\) = component perpendicular to the wall if \(\alpha\) is measured to the wall;
- \(v\cos\beta\) = component parallel after collision;
- \(v\sin\beta\) = component perpendicular after collision.

### Angle of deflection

The angle of deflection is the total angle through which the path of the sphere changes. In the standard fixed-wall diagram used in the evidence:

\[
\text{angle of deflection}=\alpha+\beta.
\]

Warning: this is diagram-dependent. In vector cases, the angle of deflection may be found more safely as the angle between the initial and final velocity vectors.

### Impulse

Impulse is change in momentum:

\[
\mathbf{I}=m\mathbf{v}-m\mathbf{u}=m(\mathbf{v}-\mathbf{u}).
\]

For a smooth wall or plane, impulse acts normal to the wall or plane. For two smooth spheres, impulse acts along the line of centres.

---

## 8. Core Theory

### 8.1 Smoothness: the tiny assumption that moves the whole mountain

The evidence gives the chain:

\[
\text{smooth surface}\Rightarrow\text{no frictional force}\Rightarrow\text{only normal reaction force}\Rightarrow\text{impulse normal to surface}\Rightarrow\text{change in momentum normal to surface}\Rightarrow\text{parallel component unchanged}.
\]

Let the velocity before impact be split into:

\[
u_{\parallel},\qquad u_{\perp}.
\]

Let the velocity after impact be split into:

\[
v_{\parallel},\qquad v_{\perp}.
\]

Because the surface is smooth,

\[
v_{\parallel}=u_{\parallel}.
\]

Because Newton’s law of restitution acts in the normal direction,

\[
v_{\perp}=e u_{\perp}
\]

in terms of magnitudes for a fixed plane collision.

**Bridge Note:** In ordinary A-Level Maths, you used restitution along a single straight line. Here, Further Maths extends this by splitting the velocity into a collision direction and a non-collision direction.

### 8.2 Fixed smooth plane: component equations

Suppose a smooth sphere approaches a fixed smooth plane with speed \(u\), making an angle \(\alpha\) with the plane. After collision, the sphere leaves with speed \(v\), making an angle \(\beta\) with the plane.

The components before impact are:

\[
u_{\parallel}=u\cos\alpha,
\qquad
u_{\perp}=u\sin\alpha.
\]

The components after impact are:

\[
v_{\parallel}=v\cos\beta,
\qquad
v_{\perp}=v\sin\beta.
\]

Since the surface is smooth:

\[
\boxed{v\cos\beta=u\cos\alpha}\tag{1}
\]

Using Newton’s law of restitution perpendicular to the surface:

\[
e=\frac{v\sin\beta}{u\sin\alpha}.
\]

Hence:

\[
\boxed{v\sin\beta=eu\sin\alpha}\tag{2}
\]

**Bridge Note:** In ordinary A-Level Maths, the restitution equation was often written immediately. Here, the trick is deciding which component belongs in the restitution equation.

### 8.3 Deriving \(\tan\beta=e\tan\alpha\)

Divide equation \((2)\) by equation \((1)\):

\[
\frac{v\sin\beta}{v\cos\beta}=\frac{eu\sin\alpha}{u\cos\alpha}.
\]

Cancel \(v\) and \(u\):

\[
\frac{\sin\beta}{\cos\beta}=e\frac{\sin\alpha}{\cos\alpha}.
\]

Use \(\tan\theta=\frac{\sin\theta}{\cos\theta}\):

\[
\boxed{\tan\beta=e\tan\alpha}.
\]

Since \(0\le e\le1\), for the usual acute collision angles:

\[
\beta\le\alpha.
\]

The rebound angle to the plane is no larger than the approach angle to the plane.

### 8.4 Finding speed without carrying \(\beta\)

Square and add the two component equations:

\[
v^2\cos^2\beta+v^2\sin^2\beta=u^2\cos^2\alpha+e^2u^2\sin^2\alpha.
\]

Factorise:

\[
v^2(\cos^2\beta+\sin^2\beta)=u^2\cos^2\alpha+e^2u^2\sin^2\alpha.
\]

Use \(\cos^2\beta+\sin^2\beta=1\):

\[
v^2=u^2\cos^2\alpha+e^2u^2\sin^2\alpha.
\]

Therefore:

\[
\boxed{v=u\sqrt{\cos^2\alpha+e^2\sin^2\alpha}}.
\]

This is not a formula you need to memorise. It is often safer to build it from the component triangle each time.

### 8.5 The x-and-y method

If a sphere approaches a fixed smooth plane with speed \(u\) at angle \(60^\circ\) to the plane and \(e=\frac14\), then:

\[
u_{\parallel}=u\cos60^\circ=\frac12u,
\]

\[
u_{\perp}=u\sin60^\circ=\frac{\sqrt3}{2}u.
\]

After collision:

\[
v_{\parallel}=\frac12u,
\]

\[
v_{\perp}=\frac14\cdot\frac{\sqrt3}{2}u=\frac{\sqrt3}{8}u.
\]

Then:

\[
v^2=\left(\frac12u\right)^2+\left(\frac{\sqrt3}{8}u\right)^2
=\frac14u^2+\frac{3}{64}u^2
=\frac{19}{64}u^2.
\]

So:

\[
\boxed{v=\frac{\sqrt{19}}{8}u}.
\]

The rebound angle \(\theta\) satisfies:

\[
\tan\theta=\frac{\frac{\sqrt3}{8}u}{\frac12u}=\frac{\sqrt3}{4}.
\]

So:

\[
\theta=\tan^{-1}\left(\frac{\sqrt3}{4}\right)\approx23.4^\circ.
\]

The angle of deflection in the standard diagram is:

\[
60^\circ+23.4^\circ=83.4^\circ.
\]

### 8.6 Quickfire vector examples for a horizontal wall

For a horizontal smooth wall, the horizontal component is parallel to the wall and unchanged; the vertical component is perpendicular to the wall and changes direction, with magnitude multiplied by \(e\).

\[
\begin{pmatrix}3\\-3\end{pmatrix},\ e=\frac13
\quad\Rightarrow\quad
\mathbf{v}=\begin{pmatrix}3\\1\end{pmatrix}.
\]

\[
\begin{pmatrix}1\\-1\end{pmatrix},\ e=1
\quad\Rightarrow\quad
\mathbf{v}=\begin{pmatrix}1\\1\end{pmatrix}.
\]

\[
\begin{pmatrix}7\\-6\end{pmatrix},\ e=\frac12
\quad\Rightarrow\quad
\mathbf{v}=\begin{pmatrix}7\\3\end{pmatrix}.
\]

\[
\begin{pmatrix}5\\-3\end{pmatrix},\ e=0
\quad\Rightarrow\quad
\mathbf{v}=\begin{pmatrix}5\\0\end{pmatrix}.
\]

When \(e=0\), the sphere does not rebound away from the surface. It continues with only the parallel component.

### 8.7 Impulse for a fixed smooth plane collision

For a fixed smooth plane, impulse acts normal to the plane.

Choose positive direction away from the plane. If the incoming normal component has magnitude \(u_\perp\), then:

\[
\text{initial normal velocity}=-u_\perp,
\qquad
\text{final normal velocity}=+eu_\perp.
\]

Impulse magnitude:

\[
I=m(eu_\perp-(-u_\perp))=m(1+e)u_\perp.
\]

So:

\[
\boxed{I=m(1+e)u_\perp}.
\]

### 8.8 Loss of kinetic energy

\[
K_{\text{before}}=\frac12mu^2,
\qquad
K_{\text{after}}=\frac12mv^2.
\]

Loss of kinetic energy:

\[
\Delta K=\frac12m(u^2-v^2).
\]

If velocities are vectors:

\[
\Delta K=\frac12m(|\mathbf{u}|^2-|\mathbf{v}|^2).
\]

### 8.9 Two smooth spheres: line of centres and common tangent

When two smooth spheres collide, the contact force acts along the line joining their centres at impact. This line is the line of centres. The direction perpendicular to this line is the common tangent direction.

For two smooth spheres:

- components parallel to the common tangent are unchanged;
- components along the line of centres are changed by impulse;
- conservation of momentum applies along the line of centres;
- Newton’s law of restitution applies along the line of centres.

Let sphere \(A\) have mass \(m_A\), initial line-of-centres velocity \(u_A\), and final line-of-centres velocity \(v_A\). Let sphere \(B\) have mass \(m_B\), initial line-of-centres velocity \(u_B\), and final line-of-centres velocity \(v_B\). Then:

\[
m_Au_A+m_Bu_B=m_Av_A+m_Bv_B.\tag{1}
\]

Newton’s law of restitution gives, for a usual approach/separation ordering:

\[
v_B-v_A=e(u_A-u_B).\tag{2}
\]

### 8.10 Scalar product method for angled walls

Boundary note: this is useful and evidence-backed, but treated here as an optional efficient method unless a CCEA question requires it.

Let:

\[
\mathbf{u}=\text{velocity before impact},\quad
\mathbf{v}=\text{velocity after impact},\quad
\mathbf{W}=\text{a vector parallel to the wall},\quad
\mathbf{I}=\text{a vector in the direction of impulse}.
\]

Since the wall is smooth:

\[
\boxed{\mathbf{u}\cdot\mathbf{W}=\mathbf{v}\cdot\mathbf{W}}.
\]

Since restitution acts along the impulse direction:

\[
\boxed{-e\mathbf{u}\cdot\mathbf{I}=\mathbf{v}\cdot\mathbf{I}}.
\]

If unit vectors are used, the equations measure exact scalar components. If both sides use the same non-unit direction vector, the common scale factor cancels.

### 8.11 Scalar product method for angled line of centres

For two spheres with an angled line of centres:

\[
\boxed{-e(\mathbf{u}_A-\mathbf{u}_B)\cdot\mathbf{I}=(\mathbf{v}_A-\mathbf{v}_B)\cdot\mathbf{I}}.
\]

For a vector \(\mathbf{W}\) in the common tangent direction:

\[
\boxed{(\mathbf{u}_A-\mathbf{u}_B)\cdot\mathbf{W}=(\mathbf{v}_A-\mathbf{v}_B)\cdot\mathbf{W}}.
\]

### 8.12 Modelling limitation: what if it is not smooth?

If surfaces are not smooth, friction acts during impact:

\[
F_r\ne0.
\]

The tangential component may change:

\[
v_{\parallel}\ne u_{\parallel}.
\]

This is outside the core smooth model for this lesson.

---

## 9. Visual Asset Integration

[VISUAL PLACEHOLDER: FA22RestitutionElasticCollisionsInTwoDimensionsMermaid-001 | Source: CCEA FA22-REST specification boundary + lesson evidence | Insert from mermaid/FA22RestitutionElasticCollisionsInTwoDimensionsMermaid-001.md | Purpose: Show the decision flow from “smooth impact” to “resolve components” to “apply Newton’s law of restitution”.]

[VISUAL PLACEHOLDER: FA22RestitutionElasticCollisionsInTwoDimensionsSVG-001 | Source: FM1-Chp5-ObliqueCollisions.pdf page 3 | Insert from svg/FA22RestitutionElasticCollisionsInTwoDimensionsSVG-001.svg | Purpose: Show the consequence of smoothness for a sphere on a smooth surface. The visual must show a sphere touching a horizontal smooth surface, a normal reaction arrow \(R\), a horizontal friction arrow labelled \(F_r=0\), no frictional impulse, impulse normal to the surface, and parallel component unchanged.]

[VISUAL PLACEHOLDER: FA22RestitutionElasticCollisionsInTwoDimensionsSVG-002 | Source: FM1-Chp5-ObliqueCollisions.pdf page 4 + transcript theory explanation | Insert from svg/FA22RestitutionElasticCollisionsInTwoDimensionsSVG-002.svg | Purpose: Show oblique impact with fixed smooth plane using \(u\), \(v\), \(\alpha\), \(\beta\), components and angle of deflection.]

[VISUAL PLACEHOLDER: FA22RestitutionElasticCollisionsInTwoDimensionsSVG-003 | Source: FM1-Chp5-ObliqueCollisions.pdf page 5 + transcript quickfire examples | Insert from svg/FA22RestitutionElasticCollisionsInTwoDimensionsSVG-003.svg | Purpose: Show quickfire vector wall collisions for a horizontal smooth surface.]

[VISUAL PLACEHOLDER: FA22RestitutionElasticCollisionsInTwoDimensionsSVG-004 | Source: Transcript two-sphere explanation + CCEA FA22-REST boundary | Insert from svg/FA22RestitutionElasticCollisionsInTwoDimensionsSVG-004.svg | Purpose: Show two smooth spheres with line of centres and common tangent.]

[VISUAL PLACEHOLDER: FA22RestitutionElasticCollisionsInTwoDimensionsBridgeSVG-001 | Source: Ordinary A-Level Maths bridge + CCEA FA22-REST specification | Insert from svg/FA22RestitutionElasticCollisionsInTwoDimensionsBridgeSVG-001.svg | Purpose: Compare prior ordinary Maths method with Further Maths extension.]

[VISUAL PLACEHOLDER: FA22RestitutionElasticCollisionsInTwoDimensionsTikZ-001 | Source: FM1-Chp5-ObliqueCollisions.pdf page 4 | Insert from tikz/FA22RestitutionElasticCollisionsInTwoDimensionsTikZ-001.tex | Purpose: Provide a precise mathematical diagram for fixed smooth plane oblique impact.]

[VISUAL PLACEHOLDER: FA22RestitutionElasticCollisionsInTwoDimensionsTikZ-002 | Source: Transcript two-sphere explanation + CCEA FA22-REST boundary | Insert from tikz/FA22RestitutionElasticCollisionsInTwoDimensionsTikZ-002.tex | Purpose: Provide a precise line-of-centres/common-tangent diagram for two smooth spheres.]

---

## 10. Interactive Learning Widgets

[INTERACTIVE PLACEHOLDER: FA22RestitutionElasticCollisionsInTwoDimensionsWidget-001 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FA22RestitutionElasticCollisionsInTwoDimensionsWidget-001.html | Purpose: Help the student practise fixed smooth plane oblique impacts by resolving components.]

The student inputs \(u\), \(\alpha\), and \(e\). The widget displays \(u_{\parallel}=u\cos\alpha\), \(u_{\perp}=u\sin\alpha\), \(v_{\parallel}=u_{\parallel}\), \(v_{\perp}=eu_{\perp}\), final speed, rebound angle, and standard deflection for the standard diagram. It checks invalid values of \(e\), angle range, and diagram warnings.

[INTERACTIVE PLACEHOLDER: FA22RestitutionElasticCollisionsInTwoDimensionsWidget-002 | Source: AI-proposed teaching enhancement based on scalar product evidence | Insert from widgets/FA22RestitutionElasticCollisionsInTwoDimensionsWidget-002.html | Purpose: Help the student practise wall collisions using vector projection and scalar products.]

The student inputs \(\mathbf{u}\), wall direction \(\mathbf{W}\), \(e\), and optional mass. The widget solves using \(\mathbf{u}\cdot\mathbf{W}=\mathbf{v}\cdot\mathbf{W}\) and \(-e\mathbf{u}\cdot\mathbf{I}=\mathbf{v}\cdot\mathbf{I}\).

---

## 11. Worked Examples

### Worked Example 1: Quickfire vector impacts with a horizontal smooth surface

For a horizontal smooth surface, the horizontal component is parallel and unchanged; the vertical component is perpendicular and rebounds upward with magnitude multiplied by \(e\).

#### Example 1A

\[
\mathbf{u}=\begin{pmatrix}3\\-3\end{pmatrix},\qquad e=\frac13.
\]

The horizontal component after impact is \(3\). The downward normal speed before impact is \(3\). The upward rebound speed is:

\[
\frac13\times3=1.
\]

Therefore:

\[
\boxed{\mathbf{v}=\begin{pmatrix}3\\1\end{pmatrix}}.
\]

#### Example 1B

\[
\mathbf{u}=\begin{pmatrix}1\\-1\end{pmatrix},\qquad e=1.
\]

The horizontal component is \(1\), and the vertical component rebounds with magnitude \(1\), so:

\[
\boxed{\mathbf{v}=\begin{pmatrix}1\\1\end{pmatrix}}.
\]

#### Example 1C

\[
\mathbf{u}=\begin{pmatrix}7\\-6\end{pmatrix},\qquad e=\frac12.
\]

The horizontal component is \(7\). The vertical component rebounds with magnitude \(\frac12\times6=3\), so:

\[
\boxed{\mathbf{v}=\begin{pmatrix}7\\3\end{pmatrix}}.
\]

#### Example 1D

\[
\mathbf{u}=\begin{pmatrix}5\\-3\end{pmatrix},\qquad e=0.
\]

The horizontal component is \(5\). The vertical rebound magnitude is \(0\times3=0\), so:

\[
\boxed{\mathbf{v}=\begin{pmatrix}5\\0\end{pmatrix}}.
\]

### Worked Example 2: Smooth sphere hitting a fixed smooth vertical wall at \(60^\circ\)

A smooth sphere moves with speed \(u\) and strikes a smooth fixed vertical wall at an angle of \(60^\circ\) to the wall. The coefficient of restitution is \(\frac14\). Find the speed immediately after collision and the angle of deflection.

Resolve incoming velocity:

\[
u_{\parallel}=u\cos60^\circ=\frac12u,
\qquad
u_{\perp}=u\sin60^\circ=\frac{\sqrt3}{2}u.
\]

After collision:

\[
v_{\parallel}=\frac12u,
\qquad
v_{\perp}=\frac14\cdot\frac{\sqrt3}{2}u=\frac{\sqrt3}{8}u.
\]

Speed after collision:

\[
v^2=\left(\frac12u\right)^2+\left(\frac{\sqrt3}{8}u\right)^2
=\frac14u^2+\frac{3}{64}u^2
=\frac{19}{64}u^2.
\]

Therefore:

\[
\boxed{v=\frac{\sqrt{19}}{8}u}.
\]

Let the rebound angle be \(\theta\):

\[
\tan\theta=\frac{\frac{\sqrt3}{8}u}{\frac12u}=\frac{\sqrt3}{4}.
\]

\[
\theta=\tan^{-1}\left(\frac{\sqrt3}{4}\right)\approx23.4^\circ.
\]

Angle of deflection:

\[
60^\circ+23.4^\circ=83.4^\circ.
\]

\[
\boxed{\text{angle of deflection}=83.4^\circ\text{ to 3 s.f.}}
\]

### Worked Example 3: Impulse and kinetic energy loss from vector velocities

A small smooth ball of mass \(0.5\text{ kg}\) moves with velocity \(\mathbf{u}=4\mathbf{i}-\mathbf{j}\). Immediately after impact with a smooth fixed wall, its velocity is \(\mathbf{v}=2\mathbf{i}+3\mathbf{j}\). Find the impulse, magnitude of impulse, and loss in kinetic energy.

\[
\mathbf{u}=\begin{pmatrix}4\\-1\end{pmatrix},\qquad
\mathbf{v}=\begin{pmatrix}2\\3\end{pmatrix}.
\]

\[
\mathbf{v}-\mathbf{u}=\begin{pmatrix}2-4\\3-(-1)\end{pmatrix}=\begin{pmatrix}-2\\4\end{pmatrix}.
\]

\[
\mathbf{I}=0.5\begin{pmatrix}-2\\4\end{pmatrix}=\begin{pmatrix}-1\\2\end{pmatrix}.
\]

\[
\boxed{\mathbf{I}=-\mathbf{i}+2\mathbf{j}\text{ Ns}}.
\]

Magnitude:

\[
|\mathbf{I}|=\sqrt{(-1)^2+2^2}=\sqrt5\text{ Ns}\approx2.24\text{ Ns}.
\]

Kinetic energy loss:

\[
|\mathbf{u}|^2=4^2+(-1)^2=17,
\qquad
|\mathbf{v}|^2=2^2+3^2=13.
\]

\[
\Delta K=\frac12(0.5)(17)-\frac12(0.5)(13)=\frac{17}{4}-\frac{13}{4}=1\text{ J}.
\]

### Worked Example 4: Scalar product method for an angled wall

A smooth sphere of mass \(m\) is moving with velocity \(\mathbf{u}=2\mathbf{i}+7\mathbf{j}\) when it collides with a smooth fixed vertical wall. After collision, \(\mathbf{v}=\mathbf{i}-3\mathbf{j}\). Find the impulse and coefficient of restitution.

Impulse:

\[
\mathbf{I}_{\text{impulse}}=m(\mathbf{v}-\mathbf{u})=m\left(\begin{pmatrix}1\\-3\end{pmatrix}-\begin{pmatrix}2\\7\end{pmatrix}\right)=m\begin{pmatrix}-1\\-10\end{pmatrix}.
\]

\[
\boxed{\mathbf{I}_{\text{impulse}}=-m\mathbf{i}-10m\mathbf{j}}.
\]

Choose impulse direction vector:

\[
\mathbf{I}=\begin{pmatrix}1\\10\end{pmatrix}.
\]

Use:

\[
-e\mathbf{u}\cdot\mathbf{I}=\mathbf{v}\cdot\mathbf{I}.
\]

\[
\mathbf{u}\cdot\mathbf{I}=2(1)+7(10)=72.
\]

\[
\mathbf{v}\cdot\mathbf{I}=1(1)+(-3)(10)=-29.
\]

So:

\[
-72e=-29.
\]

\[
\boxed{e=\frac{29}{72}}.
\]

### Worked Example 5: Fixed smooth wall containing \(y=x\)

A smooth ball moves with velocity \(\mathbf{u}=4\mathbf{i}+2\mathbf{j}\) and collides with a smooth fixed vertical wall containing the line \(y=x\). The coefficient of restitution is \(e=\frac13\). Find the velocity after impact.

A vector parallel to the wall is:

\[
\mathbf{W}=\begin{pmatrix}1\\1\end{pmatrix}.
\]

A perpendicular impulse-direction vector is:

\[
\mathbf{I}=\begin{pmatrix}1\\-1\end{pmatrix}.
\]

Let:

\[
\mathbf{v}=\begin{pmatrix}a\\b\end{pmatrix}.
\]

Wall-parallel component unchanged:

\[
\mathbf{u}\cdot\mathbf{W}=\mathbf{v}\cdot\mathbf{W}.
\]

\[
4+2=a+b.
\]

\[
a+b=6.\tag{1}
\]

Restitution in impulse direction:

\[
-e\mathbf{u}\cdot\mathbf{I}=\mathbf{v}\cdot\mathbf{I}.
\]

\[
\mathbf{u}\cdot\mathbf{I}=4-2=2,
\qquad
\mathbf{v}\cdot\mathbf{I}=a-b.
\]

\[
-\frac13(2)=a-b.
\]

\[
a-b=-\frac23.\tag{2}
\]

Add equations:

\[
(a+b)+(a-b)=6-\frac23.
\]

\[
2a=\frac{16}{3}.
\]

\[
a=\frac83.
\]

Then:

\[
b=6-\frac83=\frac{10}{3}.
\]

\[
\boxed{\mathbf{v}=\frac83\mathbf{i}+\frac{10}{3}\mathbf{j}}.
\]

### Worked Example 6: Two smooth spheres with line of centres parallel to \(\mathbf{j}\)

Sphere \(A\), mass \(5\text{ kg}\), has velocity \(2\mathbf{i}+3\mathbf{j}\). Sphere \(B\), mass \(3\text{ kg}\), has velocity \(4\mathbf{i}-2\mathbf{j}\). The spheres collide when their line of centres is parallel to \(\mathbf{j}\). The coefficient of restitution is \(e=\frac35\). Find the velocities after impact.

The line of centres is vertical, so the \(\mathbf{i}\)-components are unchanged:

\[
v_{Ax}=2,
\qquad
v_{Bx}=4.
\]

Let:

\[
\mathbf{v}_A=2\mathbf{i}+p\mathbf{j},
\qquad
\mathbf{v}_B=4\mathbf{i}+q\mathbf{j}.
\]

Conservation of vertical momentum:

\[
5(3)+3(-2)=5p+3q.
\]

\[
9=5p+3q.\tag{1}
\]

Restitution:

\[
q-p=e(3-(-2))=\frac35(5)=3.
\]

\[
q-p=3.\tag{2}
\]

From \((2)\), \(q=p+3\). Substitute:

\[
5p+3(p+3)=9.
\]

\[
8p+9=9.
\]

\[
p=0,
\qquad q=3.
\]

Therefore:

\[
\boxed{\mathbf{v}_A=2\mathbf{i}},
\qquad
\boxed{\mathbf{v}_B=4\mathbf{i}+3\mathbf{j}}.
\]

### Worked Example 7: Angle of deflection from velocity vectors

Let:

\[
\mathbf{u}=\begin{pmatrix}-6\\-4\end{pmatrix},
\qquad
\mathbf{v}=\begin{pmatrix}2\\-4\end{pmatrix}.
\]

The angle of deflection is the angle between the original and final velocity vectors:

\[
\cos\theta=\frac{\mathbf{u}\cdot\mathbf{v}}{|\mathbf{u}||\mathbf{v}|}.
\]

\[
\mathbf{u}\cdot\mathbf{v}=(-6)(2)+(-4)(-4)=-12+16=4.
\]

\[
|\mathbf{u}|=\sqrt{36+16}=\sqrt{52},
\qquad
|\mathbf{v}|=\sqrt{4+16}=\sqrt{20}.
\]

\[
\cos\theta=\frac{4}{\sqrt{52}\sqrt{20}}.
\]

\[
\theta=\cos^{-1}\left(\frac{4}{\sqrt{52}\sqrt{20}}\right)\approx82.9^\circ.
\]

\[
\boxed{\theta=82.9^\circ\text{ to 3 s.f.}}
\]

---

## 12. Common Mistakes and Exam Traps

### Multiplying the whole velocity by \(e\)

Wrong:

\[
\mathbf{v}=e\mathbf{u}.
\]

Correct:

\[
\text{normal component after}=e(\text{normal component before}),
\]

while:

\[
\text{parallel component after}=\text{parallel component before}.
\]

### Using restitution in the wrong direction

Newton’s law of restitution applies along the line of impact only. For a fixed plane, the line of impact is normal to the plane. For two spheres, it is the line of centres.

### Forgetting that a smooth surface has no friction

If the surface is smooth:

\[
F_r=0.
\]

So no tangential impulse acts.

### Confusing angle to the wall with angle to the normal

If the angle is measured to the wall:

\[
u_{\parallel}=u\cos\alpha,
\qquad
u_{\perp}=u\sin\alpha.
\]

If the angle is measured to the normal:

\[
u_{\perp}=u\cos\alpha,
\qquad
u_{\parallel}=u\sin\alpha.
\]

### Calling velocity “speed”

Speed is scalar:

\[
v=|\mathbf{v}|.
\]

Velocity is vector:

\[
\mathbf{v}=v_x\mathbf{i}+v_y\mathbf{j}.
\]

### Losing signs in impulse

Impulse is:

\[
\mathbf{I}=m(\mathbf{v}-\mathbf{u}).
\]

For two bodies, the impulses are equal in magnitude and opposite in direction.

### Forgetting mass in momentum equations

For two spheres:

\[
m_Au_A+m_Bu_B=m_Av_A+m_Bv_B.
\]

### Treating the wall as moving

A fixed wall does not have an unknown velocity. For a fixed smooth plane, use parallel component unchanged and normal component after \(=e\) times normal component before.

### Forgetting the CCEA boundary

The core CCEA topic is restitution, including direct elastic collisions between smooth spheres or between a smooth sphere and a fixed plane. Do not import rough surfaces, frictional impact equations, impulsive tensions in strings, or extra cross-board assumptions unless clearly marked.

### Over-memorising angle of deflection formulae

The standard oblique wall diagram may give:

\[
\text{deflection}=\alpha+\beta.
\]

But other diagrams may require a difference or the scalar product angle between velocity vectors.

---

## 13. Practice Questions

All questions in this section are generated practice questions. They are not labelled as CCEA past-paper questions.

### Basic fluency questions

1. A smooth ball strikes a horizontal smooth surface with velocity \(\begin{pmatrix}6\\-4\end{pmatrix}\) and \(e=\frac12\). Find the velocity immediately after impact.

2. A smooth ball strikes a horizontal smooth surface with velocity \(\begin{pmatrix}-5\\-8\end{pmatrix}\) and \(e=\frac34\). Find the velocity immediately after impact.

3. A smooth ball strikes a fixed smooth plane. Its component of velocity parallel to the plane is \(7\text{ m s}^{-1}\), and its component perpendicular to the plane before impact is \(12\text{ m s}^{-1}\) towards the plane. The coefficient of restitution is \(e=\frac13\). Find the speed immediately after impact.

4. A smooth ball strikes a fixed smooth plane with speed \(10\text{ m s}^{-1}\) at an angle of \(30^\circ\) to the plane. The coefficient of restitution is \(e=\frac25\). Find the speed immediately after impact.

### Bridge questions

5. Explain why the component of velocity parallel to a smooth fixed plane remains unchanged during impact.

6. A ball of mass \(0.4\text{ kg}\) has velocity \(3\mathbf{i}-4\mathbf{j}\) before impact and \(3\mathbf{i}+2\mathbf{j}\) after impact. Find the impulse on the ball.

7. For the velocities in Question 6, find the loss in kinetic energy.

### Standard exam-style questions

8. A smooth sphere moves on a smooth horizontal plane with speed \(u\). It strikes a smooth fixed vertical wall at an angle of \(45^\circ\) to the wall. The coefficient of restitution is \(e=\frac12\). Find the speed immediately after collision and the angle of deflection.

9. A smooth sphere of mass \(m\) moves with velocity \(5\mathbf{i}+2\mathbf{j}\) and collides with a smooth fixed wall. Immediately after collision its velocity is \(2\mathbf{i}+5\mathbf{j}\). Find the impulse and the coefficient of restitution using a scalar product method.

10. A smooth sphere \(A\), of mass \(2m\), has velocity \(3\mathbf{i}+4\mathbf{j}\). A smooth sphere \(B\), of mass \(m\), has velocity \(\mathbf{i}-2\mathbf{j}\). They collide when their line of centres is parallel to \(\mathbf{j}\). The coefficient of restitution is \(e=\frac12\). Find the velocities after collision.

### Harder synthesis questions

11. A smooth ball moves with velocity \(6\mathbf{i}+2\mathbf{j}\) and strikes a smooth fixed wall whose direction is parallel to \(\begin{pmatrix}2\\1\end{pmatrix}\). The coefficient of restitution is \(e=\frac14\). Use scalar products to find the velocity after impact.

12. A smooth sphere \(S\) moves on a smooth horizontal plane with speed \(u\) at an angle \(\alpha\) to a fixed smooth wall. Show that if the coefficient of restitution is \(e\), then the speed \(v\) immediately after impact satisfies

\[
v^2=u^2(\cos^2\alpha+e^2\sin^2\alpha),
\]

where \(\alpha\) is measured to the wall.

---

## 14. Worked Solutions

### Solution 1

Horizontal component unchanged: \(v_x=6\). Vertical rebound speed: \(\frac12\times4=2\). Therefore:

\[
\boxed{\mathbf{v}=\begin{pmatrix}6\\2\end{pmatrix}}.
\]

### Solution 2

Horizontal component unchanged: \(v_x=-5\). Vertical rebound speed: \(\frac34\times8=6\). Therefore:

\[
\boxed{\mathbf{v}=\begin{pmatrix}-5\\6\end{pmatrix}}.
\]

### Solution 3

\[
v_{\parallel}=7,
\qquad
v_{\perp}=\frac13\times12=4.
\]

\[
v^2=7^2+4^2=65.
\]

\[
\boxed{v=\sqrt{65}\text{ m s}^{-1}\approx8.06\text{ m s}^{-1}}.
\]

### Solution 4

\[
u_{\parallel}=10\cos30^\circ=5\sqrt3,
\qquad
u_{\perp}=10\sin30^\circ=5.
\]

\[
v_{\parallel}=5\sqrt3,
\qquad
v_{\perp}=\frac25\times5=2.
\]

\[
v^2=(5\sqrt3)^2+2^2=75+4=79.
\]

\[
\boxed{v=\sqrt{79}\text{ m s}^{-1}\approx8.89\text{ m s}^{-1}}.
\]

### Solution 5

A smooth fixed plane exerts no frictional force. Therefore it can only exert a normal reaction force. The impulse is normal to the plane. Since impulse equals change in momentum, there is no change in the momentum component parallel to the plane. Since mass is unchanged, the component of velocity parallel to the plane remains unchanged.

### Solution 6

\[
\mathbf{I}=m(\mathbf{v}-\mathbf{u})=0.4\left(\begin{pmatrix}3\\2\end{pmatrix}-\begin{pmatrix}3\\-4\end{pmatrix}\right)=0.4\begin{pmatrix}0\\6\end{pmatrix}=\begin{pmatrix}0\\2.4\end{pmatrix}.
\]

\[
\boxed{\mathbf{I}=2.4\mathbf{j}\text{ Ns}}.
\]

### Solution 7

\[
|\mathbf{u}|^2=3^2+(-4)^2=25,
\qquad
|\mathbf{v}|^2=3^2+2^2=13.
\]

\[
\Delta K=\frac12(0.4)(25)-\frac12(0.4)(13)=5-2.6=2.4.
\]

\[
\boxed{\Delta K=2.4\text{ J}}.
\]

### Solution 8

\[
u_{\parallel}=u\cos45^\circ=\frac{u}{\sqrt2},
\qquad
u_{\perp}=u\sin45^\circ=\frac{u}{\sqrt2}.
\]

\[
v_{\parallel}=\frac{u}{\sqrt2},
\qquad
v_{\perp}=\frac12\cdot\frac{u}{\sqrt2}=\frac{u}{2\sqrt2}.
\]

\[
v^2=\frac{u^2}{2}+\frac{u^2}{8}=\frac58u^2.
\]

\[
\boxed{v=\frac{\sqrt{10}}{4}u}.
\]

For the rebound angle \(\beta\):

\[
\tan\beta=e\tan45^\circ=\frac12.
\]

\[
\beta=\tan^{-1}\left(\frac12\right)\approx26.565^\circ.
\]

Deflection:

\[
45^\circ+26.565^\circ=71.565^\circ.
\]

\[
\boxed{71.6^\circ\text{ to 3 s.f.}}
\]

### Solution 9

\[
\mathbf{I}_{\text{impulse}}=m\left(\begin{pmatrix}2\\5\end{pmatrix}-\begin{pmatrix}5\\2\end{pmatrix}\right)=m\begin{pmatrix}-3\\3\end{pmatrix}.
\]

\[
\boxed{\mathbf{I}_{\text{impulse}}=-3m\mathbf{i}+3m\mathbf{j}}.
\]

Choose impulse direction vector:

\[
\mathbf{I}=\begin{pmatrix}-1\\1\end{pmatrix}.
\]

\[
\mathbf{u}\cdot\mathbf{I}=5(-1)+2(1)=-3,
\qquad
\mathbf{v}\cdot\mathbf{I}=2(-1)+5(1)=3.
\]

\[
-e(-3)=3.
\]

\[
\boxed{e=1}.
\]

### Solution 10

Line of centres parallel to \(\mathbf{j}\), so \(\mathbf{i}\)-components unchanged:

\[
\mathbf{v}_A=3\mathbf{i}+p\mathbf{j},
\qquad
\mathbf{v}_B=\mathbf{i}+q\mathbf{j}.
\]

Conservation of vertical momentum:

\[
(2m)(4)+m(-2)=2mp+mq.
\]

\[
6m=2mp+mq.
\]

\[
2p+q=6.\tag{1}
\]

Restitution:

\[
q-p=\frac12(4-(-2))=3.\tag{2}
\]

From \((2)\), \(q=p+3\). Substitute:

\[
2p+(p+3)=6.
\]

\[
3p=3.
\]

\[
p=1,
\qquad q=4.
\]

\[
\boxed{\mathbf{v}_A=3\mathbf{i}+\mathbf{j}},
\qquad
\boxed{\mathbf{v}_B=\mathbf{i}+4\mathbf{j}}.
\]

### Solution 11

Let \(\mathbf{v}=\begin{pmatrix}a\\b\end{pmatrix}\). Wall direction:

\[
\mathbf{W}=\begin{pmatrix}2\\1\end{pmatrix}.
\]

Choose normal direction:

\[
\mathbf{I}=\begin{pmatrix}1\\-2\end{pmatrix}.
\]

Wall-parallel component unchanged:

\[
\mathbf{u}\cdot\mathbf{W}=\mathbf{v}\cdot\mathbf{W}.
\]

\[
6(2)+2(1)=2a+b.
\]

\[
2a+b=14.\tag{1}
\]

Restitution:

\[
-e\mathbf{u}\cdot\mathbf{I}=\mathbf{v}\cdot\mathbf{I}.
\]

\[
\mathbf{u}\cdot\mathbf{I}=6(1)+2(-2)=2,
\qquad
\mathbf{v}\cdot\mathbf{I}=a-2b.
\]

\[
-\frac14(2)=a-2b.
\]

\[
a-2b=-\frac12.\tag{2}
\]

From \((1)\), \(b=14-2a\). Substitute into \((2)\):

\[
a-2(14-2a)=-\frac12.
\]

\[
5a-28=-\frac12.
\]

\[
5a=\frac{55}{2}.
\]

\[
a=\frac{11}{2}.
\]

\[
b=14-11=3.
\]

\[
\boxed{\mathbf{v}=\frac{11}{2}\mathbf{i}+3\mathbf{j}}.
\]

### Solution 12

Since \(\alpha\) is measured to the wall:

\[
u_{\parallel}=u\cos\alpha,
\qquad
u_{\perp}=u\sin\alpha.
\]

After collision:

\[
v_{\parallel}=u\cos\alpha,
\qquad
v_{\perp}=eu\sin\alpha.
\]

Therefore:

\[
v^2=v_{\parallel}^2+v_{\perp}^2=(u\cos\alpha)^2+(eu\sin\alpha)^2.
\]

\[
v^2=u^2\cos^2\alpha+e^2u^2\sin^2\alpha.
\]

Factorise:

\[
\boxed{v^2=u^2(\cos^2\alpha+e^2\sin^2\alpha)}.
\]

---

## 15. Exam Technique Notes

1. Draw the impact geometry before algebra.
2. Mark the normal and tangent/parallel directions.
3. For a fixed smooth plane, write \(v_{\parallel}=u_{\parallel}\) and \(v_{\perp}=eu_{\perp}\).
4. For two smooth spheres, write tangential components unchanged, then use PCLM and NLR along the line of centres.
5. Use \((1)^2+(2)^2\) when finding speed and division of equations when finding angle.
6. If asked for velocity, give vector or components. If asked for speed, give magnitude.
7. Use \(\mathbf{I}=m(\mathbf{v}-\mathbf{u})\) for impulse.
8. For scalar product method, use \(\mathbf{u}\cdot\mathbf{W}=\mathbf{v}\cdot\mathbf{W}\) and \(-e\mathbf{u}\cdot\mathbf{I}=\mathbf{v}\cdot\mathbf{I}\).
9. Angle of deflection is diagram-dependent. Do not blindly memorise \(\alpha+\beta\).
10. If asked what modelling assumption ensures parallel momentum is unchanged, state: the wall/surface is smooth, so no frictional impulse acts parallel to the surface.

---

## 16. Syllabus Gap Check

### LO coverage table

| LO ID | Official wording | Lesson coverage status | Evidence / notes |
|---|---|---:|---|
| `FA22-REST-LO001` | demonstrate understanding of and use Newton’s law of restitution | Fully covered | Defined \(e\), used speed of separation over speed of approach, applied along normal / line of centres |
| `FA22-REST-LO002` | solve problems involving direct elastic collisions between smooth spheres or between a smooth sphere and a fixed plane | Covered with boundary control | Fixed plane collisions, smooth sphere collisions, line of centres, common tangent, impulse and velocity components |

### Evidence coverage table

| Evidence item | Used in core lesson? | Where used |
|---|---:|---|
| Smoothness consequence: no friction, normal reaction, normal impulse | Yes | Sections 7, 8, 12, 15 |
| Fixed smooth surface component equations | Yes | Sections 8, 11, 14 |
| \(u\cos\alpha=v\cos\beta\), \(eu\sin\alpha=v\sin\beta\) | Yes | Sections 8 and 11 |
| Angle of deflection \(\alpha+\beta\) for standard diagram | Yes, with warning | Sections 7, 11, 12, 15 |
| Quickfire vector wall examples | Yes | Sections 8 and 11 |
| \(x,y\)-component method | Yes | Sections 8 and 11 |
| Impulse as \(m(\mathbf{v}-\mathbf{u})\) | Yes | Sections 8, 11, 14, 15 |
| Scalar product wall method | Boundary-risk / optional | Sections 8, 11, 14, 15 |
| Two smooth spheres: line of centres and common tangent | Yes | Sections 8, 11, 14 |
| Successive collisions with multiple walls | Enrichment only | Mentioned in boundary log, not taught as core |
| Cross-board Edexcel/Pearson examples | Used cautiously | Worked-example style, not labelled CCEA |

### Off-Spec Content Found but Excluded

| Content found | Exclusion decision | Reason |
|---|---|---|
| Impulsive tensions in strings | Excluded from core | Not within this FA22-REST lesson boundary |
| Rough-surface collision modelling | Excluded from core | Smooth surfaces are assumed in supplied lesson evidence and CCEA restitution boundary |
| Pearson exercise assignment pages | Excluded as required tasks | Cross-board textbook source, not CCEA authority |
| Edexcel M4 past-paper labels | Excluded as CCEA labels | Cross-board source, useful only as enrichment style |
| Successive impacts with two walls | Not taught as core | Boundary-risk extension beyond core direct collision methods |

### Missing Evidence Log

| Missing evidence | Consequence |
|---|---|
| CCEA-specific past-paper restitution question | Practice questions are generated, not labelled as past-paper |
| CCEA-specific mark scheme for this lesson | Mark allocation language is not claimed |
| Fully parsed screenshot PDF | Later visual details are not claimed unless directly inspected |
| Complete textbook extract text for all referenced exercises | Pearson exercise details are not used as official lesson authority |

---

## 17. Recommended Enhancements Not in the Evidence

These are AI-proposed teaching enhancements, not evidence-backed content unless they directly restate supplied evidence.

- Normal-versus-tangent overlay diagram.
- Fixed wall component triangle with angle-to-wall and angle-to-normal versions.
- Two-sphere collision diagram with line of centres rotating.
- Impulse direction mini-diagram.
- Angle of deflection gallery.
- Coefficient-of-restitution slider.
- Drag-the-normal widget.
- Two-sphere line-of-centres solver.
- Mistake detector.

---

## 18. Supplementary Sources Used

### Project sources used

| Source | Role |
|---|---|
| CCEA GCE Further Mathematics specification map | Topic identity, LO IDs and syllabus boundary |
| Further Maths README module map | Topic placement and bridge relationship |
| Further Maths evidence checklist | Evidence completeness expectations |
| Ordinary A-Level Maths bridge extracts | Bridge context only |
| User lesson-pack prompt | Workflow, phase structure, evidence hierarchy and pause rules |

### Lesson-specific evidence used

| Source | Used for |
|---|---|
| `FM1-Chp5-ObliqueCollisions.pdf` | Main slide evidence for smoothness, component equations, fixed wall impact, vector examples, scalar product method, and two-sphere line-of-centres model |
| `Chapter_5_Elastic_Collisions_in_Two_Dimensions_🎯_(Further_Mechanics_1)_screenshots.pdf` | Visual screenshot evidence and handwritten annotations |
| `transcripts.md` | Teacher explanations, warnings, correction notes, method preferences and modelling interpretation |

### Cross-board source notes

| Cross-board source | How it was treated |
|---|---|
| Pearson Further Mechanics references in slides | Used as lesson-specific worked-example style evidence, not as CCEA authority |
| Edexcel M4 references in slides | Logged as cross-board enrichment, not labelled as CCEA past-paper content |
| Teacher transcript references to Edexcel/Pearson | Used for mathematical explanation only where the CCEA topic boundary supports the method |

### Final evidence boundary statement

This lesson is a CCEA FA22 Restitution lesson. The controlling boundary is `FA22-REST`, especially Newton’s law of restitution and direct elastic collisions between smooth spheres or between a smooth sphere and a fixed plane. Cross-board material is used only where it reinforces that boundary. Anything outside that boundary is either excluded or labelled as optional enrichment.

---

## 19. Final Student Checklist

### Prerequisite confidence checklist

- [ ] Resolve a velocity into perpendicular components using sine and cosine.
- [ ] Use exact values such as \(\sin60^\circ=\frac{\sqrt3}{2}\).
- [ ] Use Pythagoras to find speed from components.
- [ ] Calculate vector magnitude.
- [ ] Calculate scalar product.
- [ ] Use \(I=m(v-u)\) in one dimension.
- [ ] Use \(\mathbf{I}=m(\mathbf{v}-\mathbf{u})\) with vectors.
- [ ] Use kinetic energy \(\frac12mv^2\), remembering that \(v\) is speed.

### Further Maths method checklist

- [ ] Identify the normal direction.
- [ ] Identify the tangential / parallel direction.
- [ ] State that a smooth surface gives no frictional impulse.
- [ ] State that the parallel component of velocity is unchanged.
- [ ] Apply Newton’s law of restitution only in the normal / line-of-centres direction.
- [ ] For two spheres, apply conservation of momentum along the line of centres.
- [ ] Preserve tangential components in two-sphere collisions.
- [ ] Recombine components to find speed.
- [ ] Use scalar products for angled walls or angled line-of-centres questions when useful.
- [ ] Calculate impulse and kinetic energy loss where required.

### Exam technique checklist

- [ ] Draw a clear before-and-after diagram.
- [ ] Label \(u\), \(v\), \(\alpha\), \(\beta\), \(e\), masses and directions.
- [ ] Write “parallel component unchanged” before doing algebra.
- [ ] Write “normal component uses restitution” before doing algebra.
- [ ] Keep units for speed, impulse and energy.
- [ ] Use exact values until the final answer where possible.
- [ ] Give angles to suitable accuracy if decimals are required.
- [ ] Say “smooth” in modelling explanations.
- [ ] Avoid claiming a cross-board practice question is CCEA.
- [ ] Check whether the question asks for speed, velocity, impulse, energy loss or angle.

### Bridge checklist

- [ ] One-dimensional restitution becomes normal-direction restitution.
- [ ] Ordinary impulse \(I=m(v-u)\) becomes vector impulse \(\mathbf{I}=m(\mathbf{v}-\mathbf{u})\).
- [ ] Ordinary speed is rebuilt from vector components using magnitude.
- [ ] Ordinary trigonometry now chooses the collision axes.
- [ ] Ordinary scalar product becomes a projection tool.

### Final Phase 1 Quality Check Summary

| Check | Status |
|---|---:|
| Unit prefix is Further Maths only: `FA22` | Passed |
| Topic identity recorded as `FA22-REST` | Passed |
| LO IDs preserved exactly: `FA22-REST-LO001`, `FA22-REST-LO002` | Passed |
| Ordinary A-Level Maths appears only as bridge context | Passed |
| Smoothness modelling assumptions included | Passed |
| Fixed smooth plane collisions covered | Passed |
| Smooth sphere collisions with line of centres covered | Passed |
| Newton’s law of restitution applied along correct direction | Passed |
| Cross-board evidence labelled and boundary-controlled | Passed |
| Off-spec material excluded or marked as enrichment | Passed |
| Visual placeholders included for Mermaid, SVG, TikZ and widgets | Passed |
| Unresolved issues | CCEA-specific past-paper and mark-scheme evidence not supplied; screenshot PDF not fully parsed |
