# A22 Further Kinematics

## Title and Metadata

| Field | Value |
|---|---|
| Course | CCEA GCE Mathematics |
| Unit | A22: A2 2 Applied Mathematics |
| Applied strand | Mechanics |
| Topic code | A22-KIN |
| Topic name | Further Kinematics |
| topic_slug | further_kinematics |
| topic_pascal | FurtherKinematics |
| topic_id | A22FurtherKinematics |
| lesson_file | A22_further_kinematics_lesson.md |
| LO IDs | A22-KIN-LO001, A22-KIN-LO002, A22-KIN-LO003, A22-KIN-LO004 |

## Evidence Map

| Evidence | Role |
|---|---|
| CCEA GCE Mathematics Specification Map | Authority for A22 Kinematics and LO IDs |
| README Module Map | Course identity, file naming and folder structure |
| Evidence Drop Checklist | Missing evidence, off-spec logging and placeholder rules |
| MechYr2-Chp8-FurtherKinematics.pdf | Slides, formulas, examples and visual evidence |
| Chapter 8 Further Kinematics transcript | Teacher explanations, worked methods and warnings |
| Screenshots PDF | Visual support only; no parsed text |

## Specification Alignment

### A22-KIN-LO001
Use calculus in kinematics for motion in a straight line:
\[
v=\frac{ds}{dt},\qquad a=\frac{dv}{dt}=\frac{d^2s}{dt^2},\qquad s=\int v\,dt,\qquad v=\int a\,dt.
\]

### A22-KIN-LO002
Use calculus in two-dimensional vector kinematics:
\[
\mathbf v=\frac{d\mathbf r}{dt},\qquad \mathbf a=\frac{d\mathbf v}{dt}=\frac{d^2\mathbf r}{dt^2},\qquad \mathbf r=\int \mathbf v\,dt,\qquad \mathbf v=\int \mathbf a\,dt.
\]

### A22-KIN-LO003
Model motion under gravity in two dimensions using:
\[
\mathbf a=\begin{pmatrix}0\\-9.8\end{pmatrix}\text{ ms}^{-2}.
\]

### A22-KIN-LO004
Solve projectile problems using vector SUVAT and interpretation of horizontal/vertical components.

## Learning Objectives

By the end of this lesson, the student should be able to:

1. Classify motion as constant velocity, constant acceleration or variable acceleration.
2. Use \(\mathbf r=\mathbf r_0+\mathbf vt\).
3. Use vector SUVAT equations correctly.
4. Explain why \(v^2=u^2+2as\) is not used as a vector equation.
5. Find speed by taking the magnitude of velocity.
6. Find bearings from velocity components.
7. Model projectile motion with \(\mathbf a=(0,-9.8)\).
8. Differentiate and integrate vector components.
9. Use vector constants of integration.
10. Interpret answers in context with units and modelling assumptions.

## Prerequisite Recap

For vectors:
\[
\begin{pmatrix}a\\b\end{pmatrix}+\begin{pmatrix}c\\d\end{pmatrix}
=
\begin{pmatrix}a+c\\b+d\end{pmatrix},
\qquad
k\begin{pmatrix}a\\b\end{pmatrix}
=
\begin{pmatrix}ka\\kb\end{pmatrix}.
\]

Magnitude:
\[
\left|\begin{pmatrix}a\\b\end{pmatrix}\right|=\sqrt{a^2+b^2}.
\]

For calculus:
\[
\frac{d}{dt}(t^n)=nt^{n-1},\qquad \int t^n\,dt=\frac{t^{n+1}}{n+1}+C.
\]

## Big Picture

Further kinematics is ordinary kinematics with vectors and calculus wearing the captain’s hat. Instead of describing motion on one line, we allow motion in a plane:
\[
\mathbf r=\begin{pmatrix}x(t)\\y(t)\end{pmatrix},\quad
\mathbf v=\begin{pmatrix}v_x(t)\\v_y(t)\end{pmatrix},\quad
\mathbf a=\begin{pmatrix}a_x(t)\\a_y(t)\end{pmatrix}.
\]
The central rule is component-wise motion: handle the \(i\)-component and \(j\)-component separately, then recombine them.

## Key Definitions and Notation

- **Particle:** an object modelled as having negligible size.
- **Position vector:** \(\mathbf r=\begin{pmatrix}x\\y\end{pmatrix}\), measured from a fixed origin.
- **Initial position vector:** \(\mathbf r_0\), the position when \(t=0\).
- **Velocity vector:** \(\mathbf v=\dfrac{d\mathbf r}{dt}\).
- **Acceleration vector:** \(\mathbf a=\dfrac{d\mathbf v}{dt}=\dfrac{d^2\mathbf r}{dt^2}\).
- **Speed:** scalar magnitude of velocity, \(|\mathbf v|\).
- **Direction of motion:** given by velocity, not position.

## Core Theory

### Constant velocity vector motion

If velocity is constant:
\[
\boxed{\mathbf r=\mathbf r_0+\mathbf vt}.
\]
If
\[
\mathbf r_0=\begin{pmatrix}x_0\\y_0\end{pmatrix},
\qquad
\mathbf v=\begin{pmatrix}a\\b\end{pmatrix},
\]
then
\[
\mathbf r=
\begin{pmatrix}x_0\\y_0\end{pmatrix}
+
t\begin{pmatrix}a\\b\end{pmatrix}
=
\begin{pmatrix}x_0+at\\y_0+bt\end{pmatrix}.
\]

### Compass directions

Assume \(\mathbf i\) is east and \(\mathbf j\) is north.

| Position condition | Component condition |
|---|---|
| Due east or west | \(j\)-component is 0 |
| Due north or south | \(i\)-component is 0 |
| North-east | \(i\)-component = \(j\)-component |
| Meeting/collision | same position vector at same time |

### Constant acceleration vector SUVAT

Valid vector equations include:
\[
\boxed{\mathbf v=\mathbf u+\mathbf at},
\]
\[
\boxed{\mathbf r=\mathbf r_0+\mathbf ut+\frac12\mathbf at^2},
\]
\[
\boxed{\mathbf r=\mathbf r_0+\mathbf vt-\frac12\mathbf at^2}.
\]

Do **not** use
\[
\mathbf v^2=\mathbf u^2+2\mathbf a\mathbf r
\]
because this would require squaring vectors in a way not used in this course.

### Speed and bearing

For
\[
\mathbf v=\begin{pmatrix}3\\10\end{pmatrix},
\]
speed is:
\[
|\mathbf v|=\sqrt{3^2+10^2}=\sqrt{109}=10.4\text{ ms}^{-1}.
\]
Bearing is measured clockwise from north:
\[
\tan\theta=\frac{3}{10},\qquad \theta=16.7^\circ,
\]
so the bearing is:
\[
\boxed{017^\circ}.
\]

### Projectiles using vectors

For motion under gravity:
\[
\mathbf a=\begin{pmatrix}0\\-9.8\end{pmatrix}.
\]
If:
\[
\mathbf r_0=\begin{pmatrix}0\\20\end{pmatrix},\qquad
\mathbf u=\begin{pmatrix}5\\8\end{pmatrix},
\]
then:
\[
\mathbf v=\mathbf u+\mathbf at
=
\begin{pmatrix}5\\8-9.8t\end{pmatrix}.
\]
Position:
\[
\mathbf r=\mathbf r_0+\mathbf ut+\frac12\mathbf at^2
=
\begin{pmatrix}0\\20\end{pmatrix}
+
\begin{pmatrix}5t\\8t\end{pmatrix}
+
\begin{pmatrix}0\\-4.9t^2\end{pmatrix}
=
\begin{pmatrix}5t\\20+8t-4.9t^2\end{pmatrix}.
\]
At ground impact:
\[
20+8t-4.9t^2=0.
\]

### Differentiating vectors

If:
\[
\mathbf r=\begin{pmatrix}x(t)\\y(t)\end{pmatrix},
\]
then:
\[
\mathbf v=\frac{d\mathbf r}{dt}=
\begin{pmatrix}\dfrac{dx}{dt}\\[4pt]\dfrac{dy}{dt}\end{pmatrix},
\qquad
\mathbf a=\frac{d\mathbf v}{dt}=
\begin{pmatrix}\dfrac{d^2x}{dt^2}\\[4pt]\dfrac{d^2y}{dt^2}\end{pmatrix}.
\]

Example:
\[
\mathbf r=\begin{pmatrix}2t^3\\50t^{-1/2}\end{pmatrix}.
\]
Velocity:
\[
\mathbf v=
\begin{pmatrix}
\dfrac{d}{dt}(2t^3)\\[4pt]
\dfrac{d}{dt}(50t^{-1/2})
\end{pmatrix}
=
\begin{pmatrix}
6t^2\\
-25t^{-3/2}
\end{pmatrix}.
\]
Acceleration:
\[
\mathbf a=
\begin{pmatrix}
12t\\
\frac{75}{2}t^{-5/2}
\end{pmatrix}.
\]

### Integrating vectors

If:
\[
\mathbf v=\begin{pmatrix}3t\\\frac12t^2\end{pmatrix},
\]
then:
\[
\mathbf r=\int \mathbf v\,dt
=
\begin{pmatrix}\int 3t\,dt\\[4pt]\int \frac12t^2\,dt\end{pmatrix}
+
\mathbf C
=
\begin{pmatrix}\frac32t^2\\[2pt]\frac16t^3\end{pmatrix}
+
\mathbf C.
\]
If \(\mathbf r=\begin{pmatrix}2\\-3\end{pmatrix}\) when \(t=0\), then:
\[
\mathbf C=\begin{pmatrix}2\\-3\end{pmatrix}.
\]
So:
\[
\boxed{
\mathbf r=
\begin{pmatrix}
\frac32t^2+2\\[2pt]
\frac16t^3-3
\end{pmatrix}}.
\]

## Visual Asset Integration

[VISUAL PLACEHOLDER: A22FurtherKinematicsSVG-001 | Source: PDF p.3 and transcript | Insert from svg/A22FurtherKinematicsSVG-001.svg | Purpose: Show \(\mathbf r=\mathbf r_0+\mathbf vt\).]

[VISUAL PLACEHOLDER: A22FurtherKinematicsSVG-002 | Source: PDF p.5 | Insert from svg/A22FurtherKinematicsSVG-002.svg | Purpose: Show vector SUVAT quantities and scalar time.]

[VISUAL PLACEHOLDER: A22FurtherKinematicsSVG-003 | Source: PDF p.5 and transcript | Insert from svg/A22FurtherKinematicsSVG-003.svg | Purpose: Show speed and bearing from \(\binom{3}{10}\).]

[VISUAL PLACEHOLDER: A22FurtherKinematicsSVG-004 | Source: PDF p.9 | Insert from svg/A22FurtherKinematicsSVG-004.svg | Purpose: Show projectile motion under gravity.]

[VISUAL PLACEHOLDER: A22FurtherKinematicsSVG-005 | Source: specification and transcript | Insert from svg/A22FurtherKinematicsSVG-005.svg | Purpose: Show \(\mathbf r\), \(\mathbf v\), \(\mathbf a\) calculus chain.]

[INTERACTIVE PLACEHOLDER: A22FurtherKinematicsWidget-001 | Source: projectile equations | Insert from widgets/A22FurtherKinematicsWidget-001.html | Purpose: Explore projectile vectors interactively.]

## Worked Examples

### Example 1: Constant velocity

A particle starts from:
\[
\mathbf r_0=\begin{pmatrix}3\\7\end{pmatrix}
\]
and moves with:
\[
\mathbf v=\begin{pmatrix}2\\-1\end{pmatrix}.
\]

At \(t=4\):
\[
\mathbf r=\mathbf r_0+\mathbf vt
=
\begin{pmatrix}3\\7\end{pmatrix}
+
4\begin{pmatrix}2\\-1\end{pmatrix}
=
\begin{pmatrix}3\\7\end{pmatrix}
+
\begin{pmatrix}8\\-4\end{pmatrix}
=
\begin{pmatrix}11\\3\end{pmatrix}.
\]

General position:
\[
\mathbf r=
\begin{pmatrix}3\\7\end{pmatrix}
+
t\begin{pmatrix}2\\-1\end{pmatrix}
=
\begin{pmatrix}3+2t\\7-t\end{pmatrix}.
\]
Due east means \(j=0\):
\[
7-t=0\quad\Rightarrow\quad t=7.
\]

### Example 2: Speed and bearing

\[
\mathbf u=\begin{pmatrix}-3\\1\end{pmatrix},\quad
\mathbf a=\begin{pmatrix}2\\3\end{pmatrix},\quad
t=3.
\]
\[
\mathbf v=\mathbf u+\mathbf at
=
\begin{pmatrix}-3\\1\end{pmatrix}
+
3\begin{pmatrix}2\\3\end{pmatrix}
=
\begin{pmatrix}3\\10\end{pmatrix}.
\]
Speed:
\[
|\mathbf v|=\sqrt{3^2+10^2}=\sqrt{109}=10.4\text{ ms}^{-1}.
\]
Bearing:
\[
\tan\theta=\frac{3}{10},\quad \theta=16.7^\circ,
\]
so:
\[
\boxed{017^\circ}.
\]

### Example 3: Ice-skater model

Initial velocity:
\[
\mathbf u=\begin{pmatrix}2.4\\-0.6\end{pmatrix}.
\]
At \(t=20\):
\[
\mathbf v=\begin{pmatrix}-5.6\\3.4\end{pmatrix}.
\]
Use:
\[
\mathbf v=\mathbf u+20\mathbf a.
\]
\[
20\mathbf a=
\begin{pmatrix}-5.6\\3.4\end{pmatrix}
-
\begin{pmatrix}2.4\\-0.6\end{pmatrix}
=
\begin{pmatrix}-8\\4\end{pmatrix}.
\]
\[
\boxed{\mathbf a=\begin{pmatrix}-0.4\\0.2\end{pmatrix}\text{ ms}^{-2}}.
\]

Since the skater starts at \(O\):
\[
\mathbf s=\mathbf ut+\frac12\mathbf at^2.
\]
\[
\mathbf s=
\begin{pmatrix}2.4t\\-0.6t\end{pmatrix}
+
\begin{pmatrix}-0.2t^2\\0.1t^2\end{pmatrix}
=
\boxed{\begin{pmatrix}2.4t-0.2t^2\\-0.6t+0.1t^2\end{pmatrix}}.
\]

North-east means components equal:
\[
2.4t-0.2t^2=-0.6t+0.1t^2.
\]
\[
3t-0.3t^2=0
\]
\[
t(3-0.3t)=0.
\]
So \(t=0\) or \(t=10\). Reject \(t=0\) because the skater is at the origin:
\[
\boxed{t=10\text{ seconds}}.
\]

Second skater:
\[
\mathbf r=\begin{pmatrix}0\\1.1t-6\end{pmatrix}.
\]
For meeting:
\[
\begin{pmatrix}2.4t-0.2t^2\\-0.6t+0.1t^2\end{pmatrix}
=
\begin{pmatrix}0\\1.1t-6\end{pmatrix}.
\]
Compare \(i\)-components:
\[
2.4t-0.2t^2=0
\]
\[
0.2t(12-t)=0.
\]
So \(t=0\) or \(t=12\). At \(t=12\), both \(j\)-components are:
\[
-0.6(12)+0.1(12)^2=7.2,
\]
\[
1.1(12)-6=7.2.
\]
So they meet at:
\[
\boxed{t=12\text{ seconds}}.
\]

### Example 4: Projectile

\[
\mathbf r_0=\begin{pmatrix}0\\20\end{pmatrix},\quad
\mathbf u=\begin{pmatrix}5\\8\end{pmatrix},\quad
\mathbf a=\begin{pmatrix}0\\-9.8\end{pmatrix}.
\]

Velocity after \(1.5\) seconds:
\[
\mathbf v=\mathbf u+\mathbf at
=
\begin{pmatrix}5\\8\end{pmatrix}
+
1.5\begin{pmatrix}0\\-9.8\end{pmatrix}
=
\begin{pmatrix}5\\-6.7\end{pmatrix}.
\]
Speed:
\[
\sqrt{5^2+(-6.7)^2}=8.36\text{ ms}^{-1}.
\]

Position:
\[
\mathbf r=\mathbf r_0+\mathbf ut+\frac12\mathbf at^2
=
\boxed{\begin{pmatrix}5t\\20+8t-4.9t^2\end{pmatrix}}.
\]

Ground impact:
\[
20+8t-4.9t^2=0.
\]
The positive solution is:
\[
t=2.995\ldots.
\]
Distance:
\[
OB=5t=14.976\ldots=15.0\text{ m}.
\]

### Example 5: Variable acceleration in one dimension

Given:
\[
a=\cos(2\pi t),\qquad v(0)=\frac{1}{2\pi}.
\]
Integrate:
\[
v=\int \cos(2\pi t)\,dt
=
\frac{1}{2\pi}\sin(2\pi t)+C.
\]
Use \(v(0)=\frac{1}{2\pi}\):
\[
\frac{1}{2\pi}=0+C.
\]
So:
\[
\boxed{v=\frac{1}{2\pi}\sin(2\pi t)+\frac{1}{2\pi}}.
\]
Maximum speed:
\[
\frac{1}{2\pi}+\frac{1}{2\pi}=\frac{1}{\pi}.
\]
Distance in first 3 seconds:
\[
\int_0^3\left(\frac{1}{2\pi}\sin(2\pi t)+\frac{1}{2\pi}\right)dt
=
\left[-\frac{1}{4\pi^2}\cos(2\pi t)+\frac{t}{2\pi}\right]_0^3
=
\frac{3}{2\pi}=0.477\text{ m}.
\]

### Example 6: Differentiating vector position

Given:
\[
\mathbf r=\begin{pmatrix}2t^3\\50t^{-1/2}\end{pmatrix}.
\]
\[
\mathbf v=\begin{pmatrix}6t^2\\-25t^{-3/2}\end{pmatrix}.
\]
At \(t=4\):
\[
\mathbf v(4)=\begin{pmatrix}96\\-25/8\end{pmatrix}.
\]
Speed:
\[
\sqrt{96^2+\left(-\frac{25}{8}\right)^2}=96.1\text{ ms}^{-1}.
\]
Acceleration:
\[
\mathbf a=\begin{pmatrix}12t\\\frac{75}{2}t^{-5/2}\end{pmatrix}.
\]
At \(t=2\):
\[
\mathbf a(2)=\begin{pmatrix}24\\6.63\end{pmatrix}\text{ ms}^{-2}.
\]
If \(m=0.8\):
\[
\mathbf F=m\mathbf a
=
0.8\begin{pmatrix}24\\6.63\end{pmatrix}
=
\begin{pmatrix}19.2\\5.30\end{pmatrix}\text{ N}.
\]

### Example 7: Integrating vector acceleration

Given:
\[
\mathbf a=\begin{pmatrix}4\\-2t\end{pmatrix}.
\]
Then:
\[
\mathbf v=\int \mathbf a\,dt
=
\begin{pmatrix}4t\\-t^2\end{pmatrix}
+
\mathbf c.
\]
If \(\mathbf v(3)=\begin{pmatrix}6\\0\end{pmatrix}\):
\[
\begin{pmatrix}6\\0\end{pmatrix}
=
\begin{pmatrix}12\\-9\end{pmatrix}
+
\mathbf c,
\]
so:
\[
\mathbf c=\begin{pmatrix}-6\\9\end{pmatrix}.
\]
Thus:
\[
\mathbf v=\begin{pmatrix}4t-6\\-t^2+9\end{pmatrix}.
\]
At \(t=2\):
\[
\mathbf v=\begin{pmatrix}2\\5\end{pmatrix}.
\]
Angle from \(\mathbf i\):
\[
\tan\theta=\frac{5}{2},\quad \theta=68.2^\circ.
\]

Integrate velocity:
\[
\mathbf r=
\begin{pmatrix}2t^2-6t\\-\frac13t^3+9t\end{pmatrix}
+
\mathbf d.
\]
If \(\mathbf r(3)=\begin{pmatrix}20\\3\end{pmatrix}\):
\[
\begin{pmatrix}20\\3\end{pmatrix}
=
\begin{pmatrix}0\\18\end{pmatrix}+\mathbf d,
\]
so:
\[
\mathbf d=\begin{pmatrix}20\\-15\end{pmatrix}.
\]
At \(t=0\):
\[
\mathbf r(0)=\begin{pmatrix}20\\-15\end{pmatrix}.
\]
Distance from \(O\):
\[
\sqrt{20^2+(-15)^2}=25\text{ m}.
\]

## Guided Practice

1. A particle starts at \(\binom{-2}{5}\) m and moves with constant velocity \(\binom{3}{-2}\) ms\(^{-1}\). Find its position after 4 seconds and the time when it is due east/west of the origin.
2. A particle has \(\mathbf u=\binom{4}{-1}\) and \(\mathbf a=\binom{-2}{5}\). Find velocity, speed and bearing at \(t=3\).
3. A ball starts at \(\binom{0}{12}\) m with velocity \(\binom{6}{7}\) under gravity. Find velocity and speed after 1 second, the position vector, and impact time.
4. For \(\mathbf r=\binom{t^3-2t}{4t^{1/2}}\), find \(\mathbf v\), \(\mathbf a\) and speed at \(t=4\).
5. If \(\mathbf a=\binom{6t}{-4}\) and \(\mathbf v(1)=\binom{5}{-2}\), find \(\mathbf v(t)\).

## Full Worked Solutions to Guided Practice

### Solution 1
\[
\mathbf r=\binom{-2}{5}+4\binom{3}{-2}=\binom{10}{-3}.
\]
General:
\[
\mathbf r=\binom{-2+3t}{5-2t}.
\]
Due east/west:
\[
5-2t=0\Rightarrow t=2.5.
\]

### Solution 2
\[
\mathbf v=\binom{4}{-1}+3\binom{-2}{5}=\binom{-2}{14}.
\]
\[
|\mathbf v|=\sqrt{(-2)^2+14^2}=\sqrt{200}=14.1.
\]
The direction is 2 west and 14 north:
\[
\theta=\tan^{-1}\left(\frac{2}{14}\right)=8.13^\circ.
\]
Bearing:
\[
360^\circ-8.13^\circ=352^\circ.
\]

### Solution 3
\[
\mathbf v(1)=\binom{6}{7}+\binom{0}{-9.8}=\binom{6}{-2.8}.
\]
\[
|\mathbf v|=\sqrt{6^2+(-2.8)^2}=6.62.
\]
\[
\mathbf r=\binom{0}{12}+t\binom{6}{7}+\frac12t^2\binom{0}{-9.8}
=
\binom{6t}{12+7t-4.9t^2}.
\]
Impact:
\[
12+7t-4.9t^2=0\Rightarrow t=2.41\text{ s}
\]
using the positive root.

### Solution 4
\[
\mathbf v=\binom{3t^2-2}{2t^{-1/2}},
\qquad
\mathbf a=\binom{6t}{-t^{-3/2}}.
\]
At \(t=4\):
\[
\mathbf v(4)=\binom{46}{1}.
\]
Speed:
\[
\sqrt{46^2+1^2}=46.0.
\]

### Solution 5
\[
\mathbf v=\int\binom{6t}{-4}\,dt
=
\binom{3t^2}{-4t}+\mathbf c.
\]
Use \(\mathbf v(1)=\binom{5}{-2}\):
\[
\binom{5}{-2}=\binom{3}{-4}+\mathbf c,
\]
so:
\[
\mathbf c=\binom{2}{2}.
\]
Therefore:
\[
\boxed{\mathbf v=\binom{3t^2+2}{-4t+2}}.
\]

## Common Mistakes and Exam Traps

- Giving velocity when the question asks for speed.
- Forgetting that \(t\) is scalar.
- Using \(v^2=u^2+2as\) as a vector equation.
- Mixing vector force \(\mathbf F=m\mathbf a\) with magnitude \(|\mathbf F|=m|\mathbf a|\).
- Measuring bearings from east instead of north.
- Using position instead of velocity for direction of motion.
- Forgetting vector constants of integration.
- Integrating velocity to find distance without checking whether velocity changes sign.

## Exam Technique

| Wording | What to do |
|---|---|
| speed | take \(|\mathbf v|\) |
| velocity | give vector \(\mathbf v\) |
| bearing | use velocity components and measure clockwise from north |
| direction of motion | use velocity |
| position vector | use \(\mathbf r\) |
| strikes ground | set vertical component equal to zero |
| meet/collide | same position at same time |
| freely under gravity | use \(\mathbf a=\binom{0}{-9.8}\) |

## Syllabus Gap Check

| LO ID | Covered? |
|---|---|
| A22-KIN-LO001 | Yes |
| A22-KIN-LO002 | Yes |
| A22-KIN-LO003 | Yes |
| A22-KIN-LO004 | Yes |

## Off-Spec Content Found but Excluded

| Evidence item | Decision |
|---|---|
| Further Mathematics vector products | Excluded from core |
| Edexcel/Pearson labels | Used only as cross-board support where aligned with A22-KIN |
| Old M1/M2 references | Historical context only |
| GCSE analogies | Not used as core evidence |

## Supplementary Sources

- CCEA GCE Mathematics Specification Map: syllabus authority.
- README Module Map: metadata and file structure.
- Evidence Drop Checklist: evidence and off-spec control.
- Dr Frost Further Kinematics PDF and transcript: lesson evidence.
- Screenshots PDF: visual support only.

## Final Student Checklist

- [ ] I can use \(\mathbf r=\mathbf r_0+\mathbf vt\).
- [ ] I can use vector SUVAT.
- [ ] I can explain why \(v^2=u^2+2as\) is not a vector formula here.
- [ ] I can find speed from a velocity vector.
- [ ] I can find a bearing from velocity components.
- [ ] I can model projectiles with \(\mathbf a=\binom{0}{-9.8}\).
- [ ] I can differentiate \(\mathbf r\) to get \(\mathbf v\) and \(\mathbf a\).
- [ ] I can integrate \(\mathbf a\) to get \(\mathbf v\), and \(\mathbf v\) to get \(\mathbf r\).
- [ ] I can use vector constants of integration.
- [ ] I can show two particles meet by same position at same time.

## Progress Manifest

| Phase | Status |
|---|---|
| Phase 0 | Complete |
| Phase 1 | Complete |
| Phase 2 | Complete |
| Phase 3 | Complete |
| Phase 4 | Complete |
| Phase 5 | Complete |
| Phase 6 | Complete and packaged |
