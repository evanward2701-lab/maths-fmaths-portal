# Elastic Collisions in One Dimension

## 1. Lesson Title and Metadata

| Field | Value |
|---|---|
| Date generated | 2026-06-04 |
| Course | CCEA GCE Further Mathematics |
| Unit | FA22: Further A2 2 Applied Mathematics |
| Applied section | Section B: Mechanics 2 |
| Topic code | FA22-REST |
| Topic name | Restitution |
| Lesson title | Elastic Collisions in One Dimension |
| Topic slug | elastic_collisions_in_one_dimension |
| Topic Pascal | ElasticCollisionsInOneDimension |
| Topic ID | FA22ElasticCollisionsInOneDimension |
| Lesson file name | FA22_elastic_collisions_in_one_dimension_lesson.md |
| Core LO IDs | FA22-REST-LO001; FA22-REST-LO002 |
| Bridge tags | `#A22ImpulseAndMomentum`, `#AS2Kinematics`, `#A21GeometricSeries`, `#EnergyBridge`, `#SignConventions` |
| Topic tags | `#FA22`, `#REST`, `#Mechanics2`, `#Restitution`, `#Collisions`, `#NewtonLawOfRestitution`, `#PCLM`, `#DirectImpact`, `#SmoothSpheres`, `#FixedPlane` |

This lesson teaches how to solve one-dimensional direct collision problems using

\[
\boxed{\text{PCLM}+\text{NLR}}
\]

where

\[
\text{PCLM}=\text{Principle of Conservation of Linear Momentum}
\]

and

\[
\text{NLR}=\text{Newton's Law of Restitution}.
\]

The ordinary A-Level Maths problem was that momentum is conserved, but one equation is often not enough to find two unknown velocities. The Further Maths upgrade is that Newton's law of restitution supplies a second equation by comparing the speed of separation after impact with the speed of approach before impact.

---

## 2. Evidence Map

| Source | Evidence used in this lesson | Authority level |
|---|---|---|
| CCEA GCE Further Mathematics Specification Map | FA22-REST topic, LO IDs, official wording and boundary excluding impulsive tensions in strings. | Highest authority |
| Further Maths README module map | Confirms bridge from `FA22-REST` to A22 Impulse and Momentum and AS2 Kinematics. | Project planning authority |
| Further Maths Evidence Drop Checklist | Controls evidence priority, visual placeholders, missing evidence and off-spec logging. | Project workflow authority |
| Ordinary A-Level Maths Bridge Spec Extracts | A22 Impulse and Momentum, AS2 Kinematics, AS2 mechanics modelling assumptions and A21 geometric series bridge. | Bridge only |
| `FM1-Chp4-ElasticCollisionsInOneDimension.pdf` | Direct impacts, coefficient of restitution, NLR formula, quickfire examples, two-particle example, inequality sources, wall impacts, vertical bounces, kinetic energy and successive impacts. | Lesson-specific evidence, cross-board but on-spec where CCEA confirms |
| `transcripts.md` | Teacher explanation of NLR, PCLM, coefficient of restitution, speed versus velocity, sign traps, common mistakes and step-by-step explanations. | Lesson-specific evidence |
| Screenshot PDF | Visual frames from the same lesson sequence. Used only where readable. | Visual support only |
| Pearson / Edexcel labels embedded in lesson evidence | Some examples are from Pearson or Edexcel M2. | Cross-board support only; not CCEA authority |

**Evidence limitation note.** The screenshot PDF had no parsed text. Some frames show readable lesson pages, but many frames are duplicate OBS or partial screen captures. The descriptions in this lesson preserve only the visible/readable mathematical details and the clearer parsed lesson/transcript text. No uninspected visual detail is claimed.

---

## 3. Specification Alignment

| LO ID | Official wording | Lesson coverage | Evidence source | Syllabus boundary | Ordinary A-Level Maths bridge |
|---|---|---|---|---|---|
| FA22-REST-LO001 | demonstrate understanding of and use Newton's law of restitution | Defines \(e\), speed of separation, speed of approach, \(0\le e\le 1\), perfectly elastic and totally inelastic cases; uses NLR in numerical, algebraic and wall problems. | CCEA spec map; lesson PDF; transcript. | Core. | Extends ordinary collision modelling by adding a second equation beyond PCLM. |
| FA22-REST-LO002 | solve problems involving direct elastic collisions between smooth spheres or between a smooth sphere and a fixed plane | Solves two-sphere direct impacts, sphere-plane impacts, vertical fixed-plane bounces, inequalities and successive direct impacts. | CCEA spec map; lesson PDF; transcript. | Core, but impulsive tensions in strings excluded. | Uses A22 Impulse and Momentum, AS2 Kinematics and ordinary algebra. |

---

## 4. Learning Objectives

### Core Further Maths objectives

By the end of this lesson, you should be able to state Newton's law of restitution, define the coefficient of restitution \(e\), use

\[
e=\frac{\text{speed of separation}}{\text{speed of approach}},
\]

explain why \(0\le e\le 1\), interpret \(e=0\) and \(e=1\), combine PCLM with NLR, solve for unknown velocities after direct impact, interpret negative velocities, solve direct impacts between smooth spheres, solve direct impacts between a smooth sphere and a fixed plane, form inequalities using collision logic, and calculate impulse or kinetic energy loss where appropriate.

### Bridge objectives

You should connect this topic to ordinary A-Level Mathematics by recognising that PCLM comes from impulse and momentum, SUVAT may be needed before a vertical collision, kinetic energy uses \(\frac12mv^2\), repeated bounces may form a geometric series, and modelling assumptions such as smoothness and direct impact determine whether the method is valid.

### Exam technique objectives

Draw a clear before-and-after diagram, choose and state a positive direction, label unknown velocities consistently, write `PCLM` and `NLR`, use exact fractions where possible, avoid treating speeds as signed quantities, check \(0\le e\le 1\), check final directions, and avoid off-spec impulsive-tension string methods.

---

## 5. Explicit Prerequisite Recap

### GCSE foundations

You should already be comfortable with rearranging equations, simultaneous equations, inequalities, speed, distance and time, negative numbers as direction indicators, and kinetic energy

\[
E_K=\frac12mv^2.
\]

### Ordinary AS/A2 Mathematics foundations

You should already have met velocity as a signed quantity, speed as a non-negative magnitude, acceleration under gravity, constant acceleration formulae such as

\[
v^2=u^2+2as,
\]

momentum \(p=mv\), impulse \(I=m(v-u)\), conservation of linear momentum in an isolated system, and geometric series where relevant to repeated bounces.

### Previous Further Mathematics foundations

This lesson assumes that, before adding restitution, the student understands

\[
\text{momentum before}=\text{momentum after}.
\]

This is abbreviated as PCLM:

\[
\sum mu=\sum mv
\]

using signed velocities in one chosen positive direction.

### A-Level Maths Bridge: What You Already Know and What Further Maths Changes

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| A22 Impulse and Momentum | Momentum is \(mv\), impulse is \(m(v-u)\), and momentum is conserved in an isolated collision. | Restitution gives a second equation by comparing relative speeds before and after impact. | PCLM alone usually gives one equation with two unknowns. It is not enough. |
| AS2 Kinematics | Use \(v^2=u^2+2as\) for constant acceleration motion. | Use SUVAT to find speed immediately before or after a vertical collision with a plane. | SUVAT uses signed velocities; NLR uses scalar speeds. |
| AS2 Mechanics modelling | Surfaces may be smooth, particles may be modelled, and resistance may be ignored. | Direct collision models require smooth spheres, fixed planes, normal impacts and no tangential complication. | If the impact is not direct or the plane is not perpendicular to the line of motion, this one-dimensional model is not valid. |
| GCSE / ordinary physics energy | Kinetic energy is \(\frac12mv^2\). | Compare kinetic energy before and after a collision; \(e=1\) means no kinetic energy is lost. | Squaring speed hides direction, so interpret velocity signs before calculating energy. |
| A21 Sequences and Series | Infinite geometric series may have sum \(\frac{a}{1-r}\) when \(|r|<1\). | Repeated vertical bounces can create heights \(h,e^2h,e^4h,\ldots\). | The infinite-bounce model is idealised. |

In ordinary A-Level Maths, this idea appeared as conservation of momentum: if no external impulse acts, total momentum before equals total momentum after. In Further Maths, the same idea becomes a two-equation collision machine. PCLM controls total signed momentum, while NLR controls how the particles separate after the impact compared with how they approached before it. The key upgrade is that the coefficient of restitution \(e\) gives material-specific information about the collision. The danger is that ordinary momentum habits can make you stop too early.

---

## 6. Big Picture Explanation

In ordinary collision problems, you may know everything before impact: both masses, both initial velocities, the direction of motion, whether the surface is smooth, and whether the collision is direct. That still does not uniquely determine both velocities after impact because conservation of momentum gives only one equation.

Newton's law of restitution gives a second equation:

\[
\boxed{e=\frac{\text{speed of separation}}{\text{speed of approach}}}.
\]

Speed of approach means how fast the objects are closing in before impact. Speed of separation means how fast they move apart after impact. The coefficient \(e\) measures how bouncy the collision is.

If \(e=0\), the speed of separation is zero. The particles coalesce and move together after impact. They do not necessarily stop unless one object is fixed or the situation forces that. If \(e=1\), speed of separation equals speed of approach; the collision is perfectly elastic and no kinetic energy is lost. If \(0<e<1\), the collision is partially elastic and some kinetic energy is lost.

The core method is:

\[
\boxed{\text{Draw diagram}\to\text{PCLM}\to\text{NLR}\to\text{solve}\to\text{interpret signs}}.
\]

For applied mechanics, the model assumptions matter: particles or smooth spheres, direct/head-on impact, smooth horizontal plane unless stated otherwise, fixed plane for wall problems, no air resistance for vertical bounce models unless stated otherwise, and only speeds immediately before and after impact used in NLR.

---

## 7. Key Definitions and Notation

### Direct impact

A direct impact is a one-dimensional, head-on collision. The particles move along the same straight line when they collide. For a smooth sphere and fixed plane, direct impact means the particle collides normally with the plane, so its line of motion is perpendicular to the plane.

### Coefficient of restitution

The coefficient of restitution is denoted by \(e\):

\[
\boxed{e=\frac{\text{speed of separation}}{\text{speed of approach}}},\qquad 0\le e\le 1.
\]

The coefficient \(e\) has no units. It depends on the materials or surfaces involved in the collision.

### Newton's law of restitution

Newton's law of restitution, abbreviated NLR, states that for a direct impact

\[
\boxed{\text{speed of separation}=e\times \text{speed of approach}}.
\]

### Principle of Conservation of Linear Momentum

PCLM says that for an isolated system

\[
\boxed{\text{total momentum before impact}=\text{total momentum after impact}}.
\]

In one dimension:

\[
\sum mu=\sum mv.
\]

Momentum uses velocity, so signs matter.

### Speed versus velocity

A velocity has direction and may be positive or negative. A speed is a magnitude and is never negative. NLR uses speeds:

\[
\text{speed of separation}\ge0,\qquad \text{speed of approach}\ge0.
\]

PCLM uses velocities:

\[
v\in\mathbb{R}.
\]

A negative final velocity means motion in the opposite direction to the chosen positive direction. It does not mean negative speed.

### Perfectly elastic collision

A collision is perfectly elastic when \(e=1\). Then speed of separation equals speed of approach and no kinetic energy is lost.

### Totally inelastic collision

A collision is totally inelastic when \(e=0\). Then speed of separation is zero, so the particles coalesce. Coalescing does not always mean stopping.

### Kinetic energy and impulse

\[
E_K=\frac12mv^2,\qquad I=m(v-u),\qquad |I|=|m(v-u)|.
\]

---

## 8. Core Theory

### 8.1 Why PCLM alone is not enough

For two colliding particles with final velocities \(v_1\) and \(v_2\), PCLM gives

\[
m_1u_1+m_2u_2=m_1v_1+m_2v_2.
\]

If \(v_1\) and \(v_2\) are both unknown, this is only one equation. Newton's law of restitution supplies the second equation:

\[
e=\frac{\text{speed of separation}}{\text{speed of approach}}.
\]

Together they form simultaneous equations.

**Bridge Note:** In ordinary A-Level Maths, we used conservation of momentum to connect before and after. Here, Further Maths extends this by adding the coefficient of restitution, which measures how the relative speed changes through the collision.

### 8.2 The two-equation method

For every standard direct collision between two smooth spheres:

1. Draw the before-impact diagram.
2. Draw the after-impact diagram.
3. Choose a positive direction.
4. Label unknown final velocities.
5. Write PCLM using signed velocities.
6. Write NLR using speeds of approach and separation.
7. Solve the simultaneous equations.
8. Interpret signs.
9. Check \(0\le e\le 1\).
10. Check that the answer makes physical sense.

### 8.3 Speed of approach and speed of separation

If particle \(A\) is behind particle \(B\), and both move to the right with speeds \(4\) and \(2\), then \(A\) catches \(B\) with speed of approach

\[
4-2=2.
\]

If after impact their speeds are \(1\) and \(3\), then the speed of separation is

\[
3-1=2,
\]

so

\[
e=\frac22=1.
\]

If particles move towards each other with speeds \(4\) and \(6\), the speed of approach is

\[
4+6=10.
\]

If after impact they separate with speeds \(3\) and \(4\), the speed of separation is

\[
3+4=7,
\]

so

\[
e=\frac{7}{10}.
\]

If after impact one particle moves left with speed \(x\) and the other moves right with speed \(y\), the speed of separation is

\[
x+y.
\]

### 8.4 General algebraic NLR form

Let the initial velocities be \(u_1,u_2\) and final velocities be \(v_1,v_2\), all measured in the same positive direction. A common algebraic form is

\[
\boxed{e=\frac{v_2-v_1}{u_1-u_2}}
\]

when \(u_1>u_2\) before impact and \(v_2>v_1\) after impact. Do not memorise this blindly. Ask what the speed of approach and separation are.

### 8.5 Wall or fixed plane impacts

For a particle colliding normally with a fixed vertical plane:

\[
\boxed{e=\frac{\text{speed after impact}}{\text{speed before impact}}}.
\]

If a particle approaches at \(8\,\text{m s}^{-1}\) and rebounds at \(2\,\text{m s}^{-1}\), then

\[
e=\frac28=\frac14.
\]

If the coefficient is known and the approach speed is \(u\), the rebound speed is \(eu\).

### 8.6 Two particles moving in opposite directions

Two particles \(A\) and \(B\) have masses \(0.2\text{ kg}\) and \(0.4\text{ kg}\). They move towards each other with speeds \(5\) and \(4\). Take the direction of \(A\) as positive, so \(u_A=5\), \(u_B=-4\). Let their final velocities be \(v_1,v_2\), and let \(e=\frac12\).

PCLM:

\[
0.2(5)+0.4(-4)=0.2v_1+0.4v_2.
\]

\[
1-1.6=0.2v_1+0.4v_2,
\]

\[
-0.6=0.2v_1+0.4v_2.
\]

Multiply by \(5\):

\[
\boxed{v_1+2v_2=-3}.
\]

NLR:

\[
\frac12=\frac{v_2-v_1}{9},
\]

so

\[
\boxed{v_2-v_1=\frac92}.
\]

From NLR:

\[
v_2=v_1+\frac92.
\]

Substitute:

\[
v_1+2\left(v_1+\frac92\right)=-3,
\]

\[
v_1+2v_1+9=-3,
\]

\[
3v_1=-12,
\]

\[
v_1=-4.
\]

Then

\[
v_2=-4+\frac92=\frac12.
\]

Therefore

\[
\boxed{v_1=-4\,\text{m s}^{-1}},\qquad \boxed{v_2=\frac12\,\text{m s}^{-1}}.
\]

Particle \(A\) reverses direction and moves with speed \(4\,\text{m s}^{-1}\). Particle \(B\) moves in the positive direction with speed \(\frac12\,\text{m s}^{-1}\).

### 8.7 Choosing unknown velocity directions

If final directions are not given, draw both unknown final velocity arrows in the positive direction. A negative answer simply means the particle actually moves the other way. If the question explicitly says the particles move in opposite directions after impact, use that information.

### 8.8 Algebraic collision example with \(3m,4m,3u,2u\)

Two small spheres \(P\) and \(Q\) have masses \(3m\) and \(4m\). They move towards each other with speeds \(3u\) and \(2u\). Let their final velocities, drawn to the right, be \(x\) and \(y\). The coefficient of restitution is \(e\).

NLR:

\[
e=\frac{y-x}{5u},
\]

so

\[
5eu=y-x,
\]

and

\[
x=y-5eu.
\]

PCLM:

\[
3m(3u)+4m(-2u)=3mx+4my,
\]

\[
9mu-8mu=3mx+4my,
\]

\[
mu=3mx+4my.
\]

Cancel \(m\):

\[
u=3x+4y.
\]

Substitute \(x=y-5eu\):

\[
u=3(y-5eu)+4y,
\]

\[
u=3y-15eu+4y,
\]

\[
u=7y-15eu.
\]

Add \(15eu\):

\[
u+15eu=7y.
\]

Factor:

\[
u(1+15e)=7y.
\]

Thus

\[
\boxed{y=\frac{u}{7}(15e+1)}.
\]

For \(x\):

\[
x=y-5eu=\frac{u}{7}(15e+1)-5eu,
\]

\[
x=\frac{15eu}{7}+\frac{u}{7}-\frac{35eu}{7},
\]

\[
\boxed{x=\frac{u}{7}(1-20e)}.
\]

If the direction of \(P\) is unchanged, then \(x>0\), so

\[
\frac{u}{7}(1-20e)>0.
\]

Since \(u>0\),

\[
1-20e>0,
\]

\[
e<\frac1{20}.
\]

Together with \(0\le e\le1\), the range is

\[
\boxed{0\le e<\frac1{20}}.
\]

If the magnitude of impulse of \(P\) on \(Q\) is \(\frac{80mu}{9}\), then using \(Q\):

\[
\frac{80mu}{9}=4m\left(\frac{u}{7}(15e+1)-(-2u)\right).
\]

Divide by \(4m\):

\[
\frac{20u}{9}=\frac{u}{7}(15e+1)+2u.
\]

Divide by \(u\):

\[
\frac{20}{9}=\frac{15e+1}{7}+2.
\]

Subtract \(2\):

\[
\frac{2}{9}=\frac{15e+1}{7}.
\]

Multiply by \(7\):

\[
\frac{14}{9}=15e+1.
\]

Subtract \(1\):

\[
\frac{5}{9}=15e.
\]

Thus

\[
\boxed{e=\frac1{27}}.
\]

### 8.9 Sources of inequalities

The common starting points are:

1. Direction unchanged: if the final velocity arrow matches the unchanged direction, set the velocity greater than zero.
2. Restitution range: \(0\le e\le1\).
3. Collision logic: particles moving in a straight line cannot overtake without colliding.
4. The particles collide again: the behind particle must be fast enough to catch the ahead particle.

### 8.10 Kinetic energy loss

For several particles,

\[
E_{\text{total}}=\frac12m_1v_1^2+\frac12m_2v_2^2+\cdots.
\]

The loss in kinetic energy is

\[
\boxed{\text{loss in K.E.}=\text{initial K.E.}-\text{final K.E.}}.
\]

If the loss is negative in a passive collision with \(0\le e\le1\), something has gone wrong.

Example: masses \(3\text{ kg}\), \(5\text{ kg}\), initial velocities \(3\) and \(-2\), \(e=\frac35\). PCLM gives

\[
-1=3x+5y,
\]

and NLR gives

\[
3=y-x.
\]

Solving gives \(x=-2\), \(y=1\). Initial kinetic energy:

\[
E_i=\frac12(3)(3^2)+\frac12(5)(2^2)=23.5\text{ J}.
\]

Final kinetic energy:

\[
E_f=\frac12(3)(2^2)+\frac12(5)(1^2)=8.5\text{ J}.
\]

Loss:

\[
\boxed{15\text{ J}}.
\]

### 8.11 Vertical bounces and SUVAT

A ball dropped from rest at height \(h\) has speed just before impact:

\[
v^2=0^2+2gh,
\]

so

\[
v=\sqrt{2gh}.
\]

If the coefficient of restitution with the ground is \(e\), the rebound speed is

\[
e\sqrt{2gh}.
\]

Let the rebound height be \(H\). At the top, velocity is zero:

\[
0=(e\sqrt{2gh})^2-2gH,
\]

\[
0=2e^2gh-2gH,
\]

so

\[
\boxed{H=e^2h}.
\]

Repeated bounce heights are

\[
h,\ e^2h,\ e^4h,\ e^6h,\ldots
\]

The total distance before rest in the ideal model is

\[
D=h+2e^2h+2e^4h+2e^6h+\cdots.
\]

For \(0\le e<1\):

\[
D=h+2e^2h(1+e^2+e^4+\cdots),
\]

\[
D=h+\frac{2e^2h}{1-e^2},
\]

\[
\boxed{D=\frac{h(1+e^2)}{1-e^2}}.
\]

### 8.12 Successive direct impacts

Successive direct impacts introduce no new law, but the bookkeeping becomes more demanding. Use PCLM and NLR for each collision separately. If \(A\) is not involved in the second collision, its velocity remains unchanged during that event. If \(C\) is not involved in the first collision, its velocity remains unchanged during that event. A carefully labelled diagram is essential.

---

## 9. Visual Asset Integration

[VISUAL PLACEHOLDER: FA22ElasticCollisionsInOneDimensionMermaid-001 | Source: CCEA FA22-REST boundary + transcript explanation of PCLM and NLR | Insert from mermaid/FA22ElasticCollisionsInOneDimensionMermaid-001.md | Purpose: Show the full solution flow for direct collision questions.]

[VISUAL PLACEHOLDER: FA22ElasticCollisionsInOneDimensionSVG-001 | Source: Lesson PDF coefficient of restitution slides + transcript speed-of-separation explanation | Insert from svg/FA22ElasticCollisionsInOneDimensionSVG-001.svg | Purpose: Explain how to identify speed of approach and speed of separation from arrows.]

[VISUAL PLACEHOLDER: FA22ElasticCollisionsInOneDimensionSVG-002 | Source: Lesson PDF fixed vertical plane example + transcript wall examples | Insert from svg/FA22ElasticCollisionsInOneDimensionSVG-002.svg | Purpose: Show that a fixed plane impact uses rebound speed divided by approach speed.]

[VISUAL PLACEHOLDER: FA22ElasticCollisionsInOneDimensionSVG-003 | Source: Transcript advice on drawing unknown velocities to the right if final directions are unknown | Insert from svg/FA22ElasticCollisionsInOneDimensionSVG-003.svg | Purpose: Show how negative final velocities are interpreted.]

[VISUAL PLACEHOLDER: FA22ElasticCollisionsInOneDimensionTikZ-001 | Source: Transcript algebraic example and screenshot evidence | Insert from tikz/FA22ElasticCollisionsInOneDimensionTikZ-001.tex | Purpose: Provide a precise diagram for the algebraic worked example.]

[VISUAL PLACEHOLDER: FA22ElasticCollisionsInOneDimensionTikZ-002 | Source: Lesson PDF vertical bounce example + transcript bouncing ball explanation | Insert from tikz/FA22ElasticCollisionsInOneDimensionTikZ-002.tex | Purpose: Show the height sequence \(h,e^2h,e^4h,\ldots\).]

[VISUAL PLACEHOLDER: FA22ElasticCollisionsInOneDimensionBridgeSVG-001 | Source: Ordinary A-Level Maths bridge + Further Maths FA22-REST specification | Insert from svg/FA22ElasticCollisionsInOneDimensionBridgeSVG-001.svg | Purpose: Compare prior ordinary Maths method with Further Maths extension.]

[VISUAL PLACEHOLDER: FA22ElasticCollisionsInOneDimensionSVG-004 | Source: Lesson PDF Sources of Inequalities slide + transcript inequality discussion | Insert from svg/FA22ElasticCollisionsInOneDimensionSVG-004.svg | Purpose: Summarise the four common sources of inequalities in collision questions.]

---

## 10. Interactive Learning Widgets

[INTERACTIVE PLACEHOLDER: FA22ElasticCollisionsInOneDimensionWidget-001 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FA22ElasticCollisionsInOneDimensionWidget-001.html | Purpose: Let students explore how final velocities depend on masses, initial velocities and \(e\).]

Student inputs: masses \(m_1,m_2\), initial velocities \(u_1,u_2\), coefficient \(e\). The widget displays PCLM, NLR, final velocities, direction interpretation, and checks \(0\le e\le1\).

[INTERACTIVE PLACEHOLDER: FA22ElasticCollisionsInOneDimensionWidget-002 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FA22ElasticCollisionsInOneDimensionWidget-002.html | Purpose: Train students to identify whether speeds should be added or subtracted.]

The widget displays before/after arrows, speed of approach, speed of separation, and the coefficient of restitution.

[INTERACTIVE PLACEHOLDER: FA22ElasticCollisionsInOneDimensionWidget-003 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FA22ElasticCollisionsInOneDimensionWidget-003.html | Purpose: Help students identify the starting inequality in harder restitution questions.]

The widget covers direction unchanged, \(0\le e\le1\), collision logic and collide-again logic.

---

## 11. Worked Examples

### Worked Example 1: Fixed plane coefficient of restitution

A particle moves normally towards a fixed vertical plane with speed \(6\,\text{m s}^{-1}\) and rebounds with speed \(2\,\text{m s}^{-1}\). Find \(e\).

For a fixed plane:

\[
e=\frac{\text{speed after impact}}{\text{speed before impact}}=\frac26=\frac13.
\]

\[
\boxed{e=\frac13}.
\]

### Worked Example 2: Fixed plane with unknown rebound speed

A particle moves normally towards a fixed plane with speed \(4\,\text{m s}^{-1}\). The coefficient of restitution is \(e=0.3\). Find the rebound speed \(v\).

\[
0.3=\frac{v}{4}.
\]

\[
v=0.3\times4=1.2.
\]

\[
\boxed{v=1.2\,\text{m s}^{-1}}.
\]

### Worked Example 3: Finding \(e\) from relative speeds

If before collision the speeds are \(4\) and \(2\) in the same direction, the speed of approach is \(4-2=2\). If after collision the speeds are \(1\) and \(3\) in the same direction, the speed of separation is \(3-1=2\), so

\[
e=\frac22=1.
\]

If particles approach with speeds \(4\) and \(6\), speed of approach is \(10\). If they separate with speeds \(3\) and \(4\), speed of separation is \(7\), so

\[
e=\frac7{10}.
\]

### Worked Example 4: Two particles in the same direction

Masses \(2\text{ kg}\), \(3\text{ kg}\), initial speeds \(4\) and \(2\), \(e=0.25\), final velocities \(v_1,v_2\) in the original direction.

NLR:

\[
0.25=\frac{v_2-v_1}{2},
\]

so

\[
0.5=v_2-v_1,\quad v_2=v_1+0.5.
\]

PCLM:

\[
2(4)+3(2)=2v_1+3v_2,
\]

\[
14=2v_1+3v_2.
\]

Substitute:

\[
14=2v_1+3(v_1+0.5),
\]

\[
14=5v_1+1.5,
\]

\[
12.5=5v_1,
\]

\[
v_1=2.5,
\]

\[
v_2=3.
\]

### Worked Example 5: Two particles moving towards each other and separating

Masses \(0.5\text{ kg}\) and \(2\text{ kg}\) move towards each other at speeds \(4\) and \(1\). Let after collision the first moves left with speed \(x\) and the second right with speed \(y\). Let \(e=\frac12\).

PCLM:

\[
0.5(4)+2(-1)=0.5(-x)+2y,
\]

\[
0=-0.5x+2y,
\]

\[
x=4y.
\]

NLR:

\[
\frac12=\frac{x+y}{5},
\]

\[
\frac52=x+y.
\]

Substitute:

\[
\frac52=4y+y=5y,
\]

\[
y=\frac12,
\quad x=2.
\]

### Worked Example 6: Textbook-style direct collision

This is the two-particle example from Section 8.6. The final answer is

\[
\boxed{v_1=-4\,\text{m s}^{-1}},\qquad \boxed{v_2=\frac12\,\text{m s}^{-1}}.
\]

The negative sign means particle \(A\) moves opposite to the chosen positive direction.

### Worked Example 7: Algebraic collision and range of \(e\)

This is the \(3m,4m,3u,2u\) example from Section 8.8. The key results are

\[
\boxed{y=\frac{u}{7}(15e+1)},
\]

\[
\boxed{x=\frac{u}{7}(1-20e)},
\]

\[
\boxed{0\le e<\frac1{20}},
\]

and, if the magnitude of impulse on \(Q\) is \(\frac{80mu}{9}\),

\[
\boxed{e=\frac1{27}}.
\]

### Worked Example 8: Bouncing ball from known heights

A ball falls from rest from height \(22.5\text{ cm}=0.225\text{ m}\) and rebounds to \(10\text{ cm}=0.100\text{ m}\).

Before impact:

\[
v^2=0^2+2(9.8)(0.225)=4.41,
\]

so

\[
v=2.1.
\]

After impact, using downward positive and upward displacement \(-0.100\):

\[
0=u^2+2(9.8)(-0.100),
\]

\[
u^2=1.96,
\]

so the rebound speed is \(1.4\).

Thus

\[
e=\frac{1.4}{2.1}=\frac23.
\]

### Worked Example 9: Total distance before rest in ideal bounce model

A ball is dropped from height \(h\), coefficient of restitution \(e\). The total distance is

\[
D=h+2e^2h+2e^4h+2e^6h+\cdots.
\]

Using a geometric series,

\[
D=h+\frac{2e^2h}{1-e^2}=\frac{h(1+e^2)}{1-e^2}.
\]

### Worked Example 10: Loss of kinetic energy

For masses \(3\) and \(5\), initial speeds \(3\) and \(2\), and final velocities \(-2\) and \(1\), the initial kinetic energy is

\[
\frac12(3)(3^2)+\frac12(5)(2^2)=23.5\text{ J},
\]

and final kinetic energy is

\[
\frac12(3)(2^2)+\frac12(5)(1^2)=8.5\text{ J}.
\]

Loss:

\[
\boxed{15\text{ J}}.
\]

### Worked Example 11: Successive direct impacts

Three spheres have masses \(m,2m,3m\), initial speeds \(7,3,1\), and coefficients \(\frac12\) for \(A\) with \(B\), then \(\frac14\) for \(B\) with \(C\).

First collision:

\[
x+2y=13,
\]

\[
y-x=2,
\]

so \(x=3\), \(y=5\).

Second collision:

\[
2p+3q=13,
\]

\[
q-p=1,
\]

so \(p=2\), \(q=3\). Final velocities:

\[
\boxed{A=3},\quad \boxed{B=2},\quad \boxed{C=3}.
\]

### Off-spec worked evidence deliberately not taught as core

The evidence includes an example involving particles connected by a light inextensible string and a jerk when the string becomes taut. This is excluded from the core worked examples because the CCEA FA22-REST boundary explicitly excludes questions involving impulsive tensions in strings.

---

## 12. Common Mistakes and Exam Traps

1. Using PCLM but forgetting NLR.
2. Treating speed as negative.
3. Forgetting \(0\le e\le1\).
4. Guessing final velocity directions instead of drawing a consistent sign convention.
5. Reversing speed of approach and speed of separation.
6. Forgetting to convert grams to kilograms.
7. Thinking \(e=0\) always means both particles stop.
8. Using kinetic energy conservation when \(e\ne1\).
9. Losing direction in impulse.
10. Mixing SUVAT signed velocity with NLR scalar speed.
11. Treating cross-board examples as CCEA past-paper questions.
12. Importing off-spec impulsive-tension string questions into FA22-REST.

---

## 13. Practice Questions

These are generated practice questions. They are on-spec for FA22-REST unless explicitly marked as bridge/enrichment. They are not past-paper questions.

1. A smooth sphere collides normally with a fixed vertical plane. It approaches at \(12\,\text{m s}^{-1}\) and rebounds at \(5\,\text{m s}^{-1}\). Find \(e\).
2. A particle collides normally with a fixed plane. Its speed immediately before impact is \(10\,\text{m s}^{-1}\). The coefficient of restitution is \(\frac35\). Find its speed immediately after impact.
3. Particle \(A\), mass \(2\text{ kg}\), speed \(6\), catches particle \(B\), mass \(4\text{ kg}\), speed \(3\), moving in the same direction. \(e=\frac13\). Find final velocities.
4. Particles \(P,Q\), masses \(3\text{ kg}\), \(2\text{ kg}\), move towards each other with speeds \(4\) and \(5\). \(e=\frac49\). Find final velocities, positive in the original direction of \(P\).
5. Spheres \(A,B\), masses \(m,2m\), move towards each other with speeds \(3u,u\). Final velocities are \(x,y\), measured in the original direction of \(A\). Coefficient is \(e\). Find \(x,y\), and if \(A\)'s direction is reversed, find the range of \(e\).
6. A ball is dropped from rest from \(0.8\text{ m}\) onto a smooth horizontal plane. \(e=\frac34\). Find the rebound height after the first impact.
7. Particles of masses \(1\text{ kg}\) and \(3\text{ kg}\) move towards each other with speeds \(5\) and \(1\). \(e=\frac12\). Find final velocities and loss of kinetic energy.
8. Spheres \(A,B,C\), masses \(m,m,2m\), have initial speeds \(8,2,1\) in the same direction. \(A\) collides with \(B\), then \(B\) collides with \(C\). \(e=\frac12\) for both collisions. Find final velocities after the second collision.

---

## 14. Worked Solutions

### Solution 1

\[
e=\frac{5}{12}.
\]

### Solution 2

\[
\frac35=\frac{v}{10},\quad v=6.
\]

### Solution 3

PCLM:

\[
2(6)+4(3)=2v_A+4v_B,
\]

so

\[
12=v_A+2v_B.
\]

NLR:

\[
\frac13=\frac{v_B-v_A}{3},
\]

so

\[
v_B=v_A+1.
\]

Then

\[
v_A+2(v_A+1)=12,
\]

\[
3v_A=10,
\]

\[
\boxed{v_A=\frac{10}{3}},\quad \boxed{v_B=\frac{13}{3}}.
\]

### Solution 4

PCLM:

\[
3(4)+2(-5)=3v_P+2v_Q,
\]

\[
2=3v_P+2v_Q.
\]

NLR:

\[
\frac49=\frac{v_Q-v_P}{9},
\]

\[
v_Q=v_P+4.
\]

Substitute:

\[
3v_P+2(v_P+4)=2,
\]

\[
5v_P=-6,
\]

\[
\boxed{v_P=-\frac65},\quad \boxed{v_Q=\frac{14}{5}}.
\]

### Solution 5

PCLM:

\[
m(3u)+2m(-u)=mx+2my,
\]

\[
u=x+2y.
\]

NLR:

\[
e=\frac{y-x}{4u},
\]

\[
x=y-4eu.
\]

Substitute:

\[
(y-4eu)+2y=u,
\]

\[
3y=u+4eu,
\]

\[
\boxed{y=\frac{u}{3}(4e+1)}.
\]

Then

\[
x=\frac{u}{3}(4e+1)-4eu=\frac{u}{3}(1-8e).
\]

If \(A\)'s direction is reversed, \(x<0\):

\[
\frac{u}{3}(1-8e)<0,
\]

so

\[
e>\frac18.
\]

Combine with \(0\le e\le1\):

\[
\boxed{\frac18<e\le1}.
\]

**Diagnostic note:** The originally drafted target \(y=\frac{u}{3}(2e+1)\) was inconsistent with the stated masses and speeds. The corrected result is \(y=\frac{u}{3}(4e+1)\).

### Solution 6

Rebound height is \(e^2h\):

\[
H=\left(\frac34\right)^2(0.8)=\frac{9}{16}\cdot\frac45=\frac9{20}=0.45.
\]

### Solution 7

PCLM:

\[
1(5)+3(-1)=v_1+3v_2,
\]

\[
2=v_1+3v_2.
\]

NLR:

\[
\frac12=\frac{v_2-v_1}{6},
\]

\[
v_2=v_1+3.
\]

Then

\[
v_1+3(v_1+3)=2,
\]

\[
4v_1=-7,
\]

\[
\boxed{v_1=-\frac74},\quad \boxed{v_2=\frac54}.
\]

Initial kinetic energy:

\[
E_i=\frac12(1)(5^2)+\frac12(3)(1^2)=14.
\]

Final kinetic energy:

\[
E_f=\frac12\left(\frac74\right)^2+\frac12(3)\left(\frac54\right)^2=\frac{31}{8}.
\]

Loss:

\[
\boxed{\frac{81}{8}\text{ J}}.
\]

### Solution 8

First collision:

\[
x+y=10,
\]

\[
y-x=3,
\]

so

\[
x=\frac72,
\quad y=\frac{13}{2}.
\]

Second collision:

\[
\frac{13}{2}+2=p+2q,
\]

\[
p+2q=\frac{17}{2}.
\]

NLR:

\[
\frac12=\frac{q-p}{\frac{11}{2}},
\]

\[
q-p=\frac{11}{4}.
\]

Substitute:

\[
p+2\left(p+\frac{11}{4}\right)=\frac{17}{2},
\]

\[
3p=3,
\]

\[
p=1,
\quad q=\frac{15}{4}.
\]

Final velocities:

\[
\boxed{A=\frac72},\quad \boxed{B=1},\quad \boxed{C=\frac{15}{4}}.
\]

---

## 15. Exam Technique Notes

Label equations clearly: write `PCLM` and `NLR`. Choose a positive direction. Draw unknown final velocities in a consistent direction. Use speeds in NLR and signed velocities in PCLM. Use exact fractions. Check \(0\le e\le1\). When asked for a range, combine your derived inequality with the coefficient range. Interpret final answers in words. For numerical simultaneous equations, a calculator can help, but it cannot interpret the sign convention.

---

## 16. Syllabus Gap Check

### LO coverage table

| LO ID | Covered? | Evidence-backed content included | Remaining issue |
|---|---:|---|---|
| FA22-REST-LO001 | Yes | Newton's law of restitution, \(e\), \(0\le e\le1\), speed of approach/separation, wall form. | None. |
| FA22-REST-LO002 | Yes | Direct collisions between smooth spheres, fixed plane impacts, vertical impacts, successive direct impacts. | Some examples are cross-board, but content is on-spec and clearly labelled. |

### Evidence coverage table

| Evidence item | Covered? | Notes |
|---|---:|---|
| Coefficient of restitution definition | Yes | Included. |
| \(0\le e\le1\) | Yes | Included repeatedly. |
| PCLM + NLR simultaneous equations | Yes | Central method throughout. |
| Two-particle numerical examples | Yes | Included. |
| Algebraic \(3m,4m,3u,2u\) example | Yes | Included fully. |
| Inequality sources | Yes | Included. |
| Fixed wall/plane examples | Yes | Included. |
| Vertical bouncing with SUVAT | Yes | Included. |
| Kinetic energy loss | Yes | Included as support/application. |
| Successive direct impacts | Yes | Included. |
| String jerk / impulsive tension | Excluded from core | Logged as off-spec boundary risk. |
| Two-dimensional collisions | Excluded | Mentioned only as future/outside this lesson. |

### Off-Spec Content Found but Excluded

| Off-spec or boundary-risk content | Evidence location | Reason excluded |
|---|---|---|
| Impulsive tensions in strings | Lesson PDF kinetic energy/string jerk section and transcript | CCEA FA22-REST boundary says questions involving impulsive tensions in strings will not be set. |
| Elastic collisions in two dimensions | Transcript mentions Chapter 5 / year-two extension | This lesson is one-dimensional FA22-REST. |
| Unseen Pearson exercises | References only | Full text not supplied, so not reproduced. |
| Edexcel-labelled questions | Embedded in lesson evidence | Used only for on-spec teaching style, not labelled as CCEA. |

### Missing evidence log

| Missing evidence | Impact |
|---|---|
| Original CCEA specification PDF page | Project specification map used instead. |
| Full Pearson textbook pages | Only visible supplied extracts used. |
| Full mark schemes for cross-board examples | Generated solutions are self-contained and not labelled as official. |
| Clean individual slide export | Visual placeholders are proposed from available evidence. |

---

## 17. Recommended Enhancements Not in the Evidence

AI-proposed enhancements include a speed-versus-velocity split diagram, a collision sanity-check diagram, a wall-bounce sign convention diagram, an \(e\)-slider animation, two-sphere collision animation, vertical bounce animation, equation builder widget, sign checker widget, and inequality builder widget. These are proposed enhancements, not evidence-backed content.

---

## 18. Supplementary Sources Used

Project Sources used: CCEA GCE Further Mathematics Specification Map; Further Maths README module map; Further Maths Evidence Drop Checklist; Ordinary A-Level Maths Bridge Spec Extracts; CCEA GCE Mathematics Specification Map for bridge context only.

Lesson-specific sources used: `FM1-Chp4-ElasticCollisionsInOneDimension.pdf`; `transcripts.md`; `Chapter_4_Elastic_Collisions_in_One_Dimension_🏅_(Further_Mechanics_1)_screenshots.pdf`.

Ordinary A-Level Maths bridge sources were used for impulse, momentum, conservation of linear momentum, \(v^2=u^2+2as\), kinetic energy and geometric series. These sources are not used to override the Further Maths specification.

Cross-board Pearson/Edexcel-labelled examples are used only where the mathematics matches the CCEA FA22-REST boundary. They are not presented as CCEA past-paper questions.

Evidence limitations: screenshot PDF has no parsed text; some screenshot frames are duplicates or partial screen captures; full textbook pages and official mark schemes were not supplied; generated practice questions are original and not past-paper questions.

---

## 19. Final Student Checklist

### Prerequisite confidence checklist

- [ ] I can choose a positive direction.
- [ ] I can use signed velocities in momentum equations.
- [ ] I can calculate momentum using \(mv\).
- [ ] I can calculate impulse using \(m(v-u)\).
- [ ] I can use \(v^2=u^2+2as\).
- [ ] I can calculate kinetic energy using \(\frac12mv^2\).
- [ ] I can solve two simultaneous linear equations.
- [ ] I can solve a simple inequality.

### Further Maths method checklist

- [ ] I can state Newton's law of restitution.
- [ ] I know that \(e=\frac{\text{speed of separation}}{\text{speed of approach}}\).
- [ ] I know that \(0\le e\le1\).
- [ ] I can explain \(e=0\) and \(e=1\).
- [ ] I can identify speed of approach and speed of separation.
- [ ] I can solve a direct collision using PCLM and NLR.
- [ ] I can handle a fixed plane collision.
- [ ] I can interpret a negative velocity.
- [ ] I can solve an algebraic collision question.
- [ ] I can form inequalities from unchanged direction.
- [ ] I can use collision logic to decide whether another impact occurs.

### Exam technique checklist

- [ ] I label PCLM and NLR clearly.
- [ ] I draw a before-and-after diagram.
- [ ] I avoid negative speeds.
- [ ] I convert grams to kilograms where necessary.
- [ ] I keep exact fractions unless decimals are requested.
- [ ] I include the lower bound \(0\le e\) in range answers.
- [ ] I interpret final directions in words.
- [ ] I check whether \(e\) is physically possible.
- [ ] I do not call generated questions past-paper questions.
- [ ] I exclude impulsive-tension string questions from core FA22-REST revision.

### Final memory capsule

\[
\boxed{\text{PCLM uses signed velocities.}}
\]

\[
\boxed{\text{NLR uses scalar speeds.}}
\]

\[
\boxed{\text{Together, they solve the collision.}}
\]
