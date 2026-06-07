# A22 Projectiles Lesson

## Title and Metadata

| Field | Value |
|---|---|
| Course | CCEA GCE Mathematics |
| Unit | A22: A2 2 Applied Mathematics |
| Section | Mechanics |
| Topic code | A22-KIN |
| Topic area | Kinematics |
| Lesson focus | Projectiles |
| Topic slug | projectiles |
| Topic Pascal | Projectiles |
| Topic ID | A22Projectiles |
| Lesson file | A22_projectiles_lesson.md |
| LO IDs | A22-KIN-LO001, A22-KIN-LO002, A22-KIN-LO003, A22-KIN-LO004 |
| Tags | `#A22`, `#Mechanics`, `#Kinematics`, `#Projectiles`, `#VectorMotion`, `#Modelling` |

---

## Evidence Map

| Evidence | Lesson use |
|---|---|
| CCEA GCE Mathematics Specification Map | Confirms A22 Kinematics and LO IDs. |
| README-Module-Map.txt | Confirms standard unit prefixes, metadata requirements and folder structure. |
| Source-Evidence-Drop-Checklist.txt | Controls missing evidence, visual placeholders and off-spec logging. |
| Chapter_6_Projectiles_🎲_(Applied_Year_2,_Mechanics)_Transcript.md | Main teaching evidence: modelling assumptions, explanations, worked examples and warnings. |
| Chapter_6_Projectiles_🎲_(Applied_Year_2,_Mechanics)_Screenshots.pdf | Visual evidence for projectile paths, component diagrams and animation-style supports. |
| MechYr2-Chp6-Projectiles.pdf | Cross-board support used only where aligned to CCEA A22-KIN projectiles. |

---

## Specification Alignment

| LO ID | How this lesson covers it |
|---|---|
| A22-KIN-LO001 | Uses vertical kinematics and constant-acceleration formulae, linking displacement, velocity and acceleration through time. |
| A22-KIN-LO002 | Uses vector form of two-dimensional kinematics with \(\mathbf{i}\) and \(\mathbf{j}\). |
| A22-KIN-LO003 | Models motion under gravity in two dimensions using horizontal and vertical components. |
| A22-KIN-LO004 | Solves projectile problems including horizontal projection, angled projection, height, time of flight, range, trajectory equation, speed at a point and simultaneous projectile problems. |

---

## Learning Objectives

By the end of this lesson, you should be able to:

1. Model a projectile as a particle moving freely under gravity.
2. Resolve an initial velocity into horizontal and vertical components.
3. Use \(a_x=0\) horizontally and \(a_y=-g\) vertically.
4. Use \(d=vt\) horizontally and SUVAT vertically.
5. Find time of flight, greatest height, range and speed at a given point.
6. Derive the standard projectile formulae when required.
7. Use vector notation for two-dimensional projectile motion.
8. Handle exam-style projectile problems where two projectiles meet.

---

## Prerequisite Recap

This lesson relies on earlier A-Level Mathematics mechanics and pure skills. No GCSE source evidence is used.

You need to be secure with:

\[
s=ut+\frac12at^2,
\]

\[
v=u+at,
\]

\[
v^2=u^2+2as,
\]

and

\[
\text{distance}=\text{speed}\times\text{time}.
\]

You also need:

\[
\sin\theta=\frac{\text{opposite}}{\text{hypotenuse}}, \qquad
\cos\theta=\frac{\text{adjacent}}{\text{hypotenuse}}, \qquad
\tan\theta=\frac{\text{opposite}}{\text{adjacent}}.
\]

For vectors:

\[
\mathbf{r}=x\mathbf{i}+y\mathbf{j},
\]

where \(\mathbf{i}\) is horizontal and \(\mathbf{j}\) is vertical.

---

## Big Picture Explanation

A projectile problem looks like a flying object problem, but the mathematics works because we split the motion into two separate stories:

\[
\text{horizontal motion} \qquad \text{and} \qquad \text{vertical motion}.
\]

The teacher transcript stresses that these two directions do not interfere with each other. The horizontal motion keeps the same velocity because gravity does not act sideways. The vertical motion changes because gravity acts downwards.

That is the whole engine room:

\[
\boxed{\text{Horizontal: constant velocity}}
\]

\[
\boxed{\text{Vertical: constant acceleration under gravity}}
\]

A projectile path is modelled as a parabola. In real life, air resistance and drag can flatten the path, but in A-Level Mechanics the particle model allows us to ignore these effects.

---

## Key Definitions and Notation

### Projectile

A **projectile** is an object projected into the air and then moving freely under gravity.

In this lesson, a projectile is usually modelled as a **particle**, meaning its size and shape are ignored.

### Moving freely under gravity

“Moving freely under gravity” means the only acceleration is due to gravity.

If upwards is positive:

\[
a_y=-g.
\]

If downwards is positive:

\[
a_y=+g.
\]

Usually:

\[
g=9.8\text{ m s}^{-2},
\]

unless the question says to use another value, such as

\[
g=10\text{ m s}^{-2}.
\]

### Range

The **range** is the horizontal distance from the point of projection to the point where the projectile lands.

The transcript describes it as how far along the ground the object travels from where it is thrown to where it lands.

### Components of velocity

If a projectile is launched with speed \(U\) at angle \(\theta\) above the horizontal, then:

\[
u_x=U\cos\theta,
\]

\[
u_y=U\sin\theta.
\]

---

## Core Theory

## 1. The two-direction model

For a projectile:

\[
\boxed{a_x=0}
\]

and

\[
\boxed{a_y=-g}
\]

if upwards is positive.

So the horizontal motion is:

\[
x=u_xt.
\]

The vertical motion is:

\[
y=u_yt-\frac12gt^2.
\]

If the projectile is launched with speed \(U\) at angle \(\theta\), then:

\[
u_x=U\cos\theta,
\]

\[
u_y=U\sin\theta.
\]

So:

\[
\boxed{x=U\cos\theta \, t}
\]

and

\[
\boxed{y=U\sin\theta \, t-\frac12gt^2}.
\]

This pair of equations is the central model behind nearly every projectile problem.

---

## 2. Horizontally projected particles

If a particle is projected horizontally, then its initial vertical velocity is zero.

So:

\[
u_y=0.
\]

The horizontal velocity is constant:

\[
u_x=U.
\]

The vertical displacement is found using:

\[
s=ut+\frac12at^2.
\]

If downwards is positive and the particle falls a height \(h\), then:

\[
s=h,\qquad u=0,\qquad a=g.
\]

So:

\[
h=0t+\frac12gt^2,
\]

\[
h=\frac12gt^2.
\]

Then:

\[
t^2=\frac{2h}{g},
\]

\[
\boxed{t=\sqrt{\frac{2h}{g}}}.
\]

Once \(t\) is known, horizontal distance is:

\[
\boxed{x=Ut}.
\]

The teacher transcript calls \(t\) the bridge value because it links the vertical calculation to the horizontal calculation.

---

## 3. Angled projection

For a particle launched with speed \(U\) at angle \(\theta\):

\[
u_x=U\cos\theta,
\]

\[
u_y=U\sin\theta.
\]

Horizontal:

\[
x=U\cos\theta \, t.
\]

Vertical:

\[
y=U\sin\theta \, t-\frac12gt^2.
\]

At the highest point:

\[
v_y=0.
\]

The horizontal velocity is still:

\[
v_x=U\cos\theta.
\]

So at the highest point, the speed is:

\[
\boxed{U\cos\theta}
\]

because the vertical component is zero.

---

## 4. Greatest height

At the greatest height, the vertical velocity is zero.

Use vertical motion only:

\[
v^2=u^2+2as.
\]

Let upwards be positive.

\[
u=U\sin\theta,\qquad v=0,\qquad a=-g,\qquad s=H.
\]

Substitute:

\[
0^2=(U\sin\theta)^2+2(-g)H.
\]

\[
0=U^2\sin^2\theta-2gH.
\]

\[
2gH=U^2\sin^2\theta.
\]

Therefore:

\[
\boxed{H=\frac{U^2\sin^2\theta}{2g}}.
\]

---

## 5. Time to greatest height

At the greatest height:

\[
v=0.
\]

Use:

\[
v=u+at.
\]

With upwards positive:

\[
0=U\sin\theta-gt.
\]

So:

\[
gt=U\sin\theta,
\]

\[
\boxed{t=\frac{U\sin\theta}{g}}.
\]

---

## 6. Time of flight on a horizontal plane

Suppose the particle lands back at the same vertical level from which it was projected.

Then its final vertical displacement is:

\[
s=0.
\]

Use:

\[
s=ut+\frac12at^2.
\]

With upwards positive:

\[
0=U\sin\theta \, t-\frac12gt^2.
\]

Factorise:

\[
0=t\left(U\sin\theta-\frac12gt\right).
\]

So either:

\[
t=0
\]

or

\[
U\sin\theta-\frac12gt=0.
\]

The solution \(t=0\) is the starting moment, not the landing moment.

So:

\[
\frac12gt=U\sin\theta,
\]

\[
gt=2U\sin\theta,
\]

\[
\boxed{T=\frac{2U\sin\theta}{g}}.
\]

---

## 7. Range on a horizontal plane

Range is horizontal distance.

Horizontal velocity is:

\[
U\cos\theta.
\]

Time of flight is:

\[
T=\frac{2U\sin\theta}{g}.
\]

So:

\[
R=U\cos\theta \times \frac{2U\sin\theta}{g}.
\]

\[
R=\frac{2U^2\sin\theta\cos\theta}{g}.
\]

Use:

\[
\sin 2\theta=2\sin\theta\cos\theta.
\]

Therefore:

\[
\boxed{R=\frac{U^2\sin 2\theta}{g}}.
\]

---

## 8. Equation of trajectory

From horizontal motion:

\[
x=U\cos\theta \, t.
\]

Make \(t\) the subject:

\[
t=\frac{x}{U\cos\theta}.
\]

Vertical motion:

\[
y=U\sin\theta \, t-\frac12gt^2.
\]

Substitute:

\[
y=U\sin\theta\left(\frac{x}{U\cos\theta}\right)-\frac12g\left(\frac{x}{U\cos\theta}\right)^2.
\]

Simplify the first term:

\[
U\sin\theta\left(\frac{x}{U\cos\theta}\right)
=
x\frac{\sin\theta}{\cos\theta}.
\]

Since:

\[
\tan\theta=\frac{\sin\theta}{\cos\theta},
\]

the first term becomes:

\[
x\tan\theta.
\]

Simplify the second term:

\[
\frac12g\left(\frac{x}{U\cos\theta}\right)^2
=
\frac12g\frac{x^2}{U^2\cos^2\theta}
=
\frac{gx^2}{2U^2\cos^2\theta}.
\]

Therefore:

\[
\boxed{y=x\tan\theta-\frac{gx^2}{2U^2\cos^2\theta}}.
\]

Since:

\[
\sec^2\theta=1+\tan^2\theta,
\]

and

\[
\frac{1}{\cos^2\theta}=1+\tan^2\theta,
\]

we can also write:

\[
\boxed{y=x\tan\theta-\frac{gx^2}{2U^2}\left(1+\tan^2\theta\right)}.
\]

The CCEA elaboration states that the equation of the path of flight may need to be derived.

---

## Visual Asset Integration

[VISUAL PLACEHOLDER: A22ProjectilesSVG-001 | Source: Screenshots PDF page 1 and transcript introduction | Insert from svg/A22ProjectilesSVG-001.svg | Purpose: Show a projectile path with \(u_x=U\cos\theta\), \(u_y=U\sin\theta\), maximum height and range.]

[VISUAL PLACEHOLDER: A22ProjectilesSVG-002 | Source: Teacher transcript and DrFrost acceleration slide | Insert from svg/A22ProjectilesSVG-002.svg | Purpose: Compare horizontal motion \(a_x=0\) with vertical motion \(a_y=-g\).]

[VISUAL PLACEHOLDER: A22ProjectilesSVG-003 | Source: Transcript vector example | Insert from svg/A22ProjectilesSVG-003.svg | Purpose: Show vector displacement and velocity components after a fixed time.]

[VISUAL PLACEHOLDER: A22ProjectilesSVG-004 | Source: Transcript simultaneous projectiles example | Insert from svg/A22ProjectilesSVG-004.svg | Purpose: Show two projectiles meeting at the same point at the same time.]

[INTERACTIVE PLACEHOLDER: A22ProjectilesWidget-001 | Source: GeoGebra-style screenshots and transcript animation discussion | Insert from widgets/A22ProjectilesWidget-001.html | Purpose: Let the student vary launch speed and angle and observe horizontal velocity, vertical velocity, height and range.]

---

# Worked Examples

## Worked Example 1: Particle projected horizontally from a height

A particle is projected horizontally at \(25\text{ m s}^{-1}\) from a point \(78.4\text{ m}\) above a horizontal surface.

Find:

1. the time taken to reach the surface;
2. the horizontal distance travelled;
3. the distance of the impact point from the original point.

### Part A: Time to reach the surface

Consider vertical motion.

Take downwards as positive.

\[
s=78.4,\qquad u=0,\qquad a=9.8,\qquad t=?
\]

Use:

\[
s=ut+\frac12at^2.
\]

Substitute:

\[
78.4=0t+\frac12(9.8)t^2.
\]

\[
78.4=4.9t^2.
\]

Divide by \(4.9\):

\[
t^2=\frac{78.4}{4.9}.
\]

\[
t^2=16.
\]

\[
t=\pm 4.
\]

Time cannot be negative in this context, so:

\[
\boxed{t=4\text{ s}}.
\]

### Part B: Horizontal distance

Consider horizontal motion.

\[
\text{speed}=25,\qquad t=4.
\]

\[
x=vt.
\]

\[
x=25\times 4.
\]

\[
\boxed{x=100\text{ m}}.
\]

### Part C: Distance from original point to impact point

This is not the curved distance travelled through the air.

It is the straight-line distance from the starting point to the impact point.

Use Pythagoras:

\[
d^2=78.4^2+100^2.
\]

\[
d=\sqrt{78.4^2+100^2}.
\]

\[
d=\sqrt{6146.56+10000}.
\]

\[
d=\sqrt{16146.56}.
\]

\[
d=127.068\ldots
\]

So:

\[
\boxed{d=127\text{ m to 3 s.f.}}
\]

or

\[
\boxed{d=130\text{ m to 2 s.f.}}
\]

Exam trap: do not try to find the length of the curved path. That is not being asked.

---

## Worked Example 2: Horizontally projected particle with unknown initial speed

A particle is projected horizontally with speed \(U\text{ m s}^{-1}\) from a point \(122.5\text{ m}\) above a horizontal plane. It hits the plane at a point \(90\text{ m}\) horizontally from the starting point.

Find \(U\).

### Step 1: Use vertical motion to find time

Take downwards as positive.

\[
s=122.5,\qquad u=0,\qquad a=9.8,\qquad t=?
\]

\[
s=ut+\frac12at^2.
\]

\[
122.5=0t+\frac12(9.8)t^2.
\]

\[
122.5=4.9t^2.
\]

\[
t^2=\frac{122.5}{4.9}.
\]

\[
t^2=25.
\]

\[
t=5.
\]

So:

\[
t=5\text{ s}.
\]

### Step 2: Use horizontal motion

\[
\text{distance}=\text{speed}\times\text{time}.
\]

\[
90=U\times 5.
\]

\[
U=\frac{90}{5}.
\]

\[
\boxed{U=18\text{ m s}^{-1}}.
\]

---

## Worked Example 3: Find the height \(h\)

A particle is projected horizontally with speed \(20\text{ m s}^{-1}\) from a point \(h\text{ m}\) above a horizontal plane. It lands \(100\text{ m}\) horizontally from the starting point.

Find \(h\).

### Step 1: Horizontal motion

\[
x=vt.
\]

\[
100=20t.
\]

\[
t=\frac{100}{20}.
\]

\[
t=5.
\]

### Step 2: Vertical motion

Take downwards as positive.

\[
s=h,\qquad u=0,\qquad a=9.8,\qquad t=5.
\]

\[
s=ut+\frac12at^2.
\]

\[
h=0(5)+\frac12(9.8)(5^2).
\]

\[
h=4.9\times 25.
\]

\[
\boxed{h=122.5\text{ m}}.
\]

---

## Worked Example 4: Angled projection from ground level

A particle is projected from a point \(O\) on a horizontal plane with speed \(28\text{ m s}^{-1}\) at an angle of elevation \(30^\circ\). It moves freely under gravity until it strikes the plane at \(A\).

Find:

1. the greatest height above the plane;
2. the time of flight;
3. the distance \(OA\).

### Step 1: Resolve the initial velocity

Horizontal component:

\[
28\cos30^\circ.
\]

Since:

\[
\cos30^\circ=\frac{\sqrt3}{2},
\]

\[
28\cos30^\circ=28\cdot\frac{\sqrt3}{2}=14\sqrt3.
\]

Vertical component:

\[
28\sin30^\circ.
\]

Since:

\[
\sin30^\circ=\frac12,
\]

\[
28\sin30^\circ=28\cdot\frac12=14.
\]

So:

\[
u_x=14\sqrt3,\qquad u_y=14.
\]

### Part A: Greatest height

At greatest height:

\[
v_y=0.
\]

Use vertical motion with upwards positive.

\[
u=14,\qquad v=0,\qquad a=-9.8,\qquad s=H.
\]

Use:

\[
v^2=u^2+2as.
\]

\[
0^2=14^2+2(-9.8)H.
\]

\[
0=196-19.6H.
\]

\[
19.6H=196.
\]

\[
H=\frac{196}{19.6}.
\]

\[
\boxed{H=10\text{ m}}.
\]

### Part B: Time of flight

The particle starts and ends on the same horizontal plane, so its vertical displacement is:

\[
s=0.
\]

Use vertical motion:

\[
s=ut+\frac12at^2.
\]

\[
0=14t+\frac12(-9.8)t^2.
\]

\[
0=14t-4.9t^2.
\]

Factorise:

\[
0=t(14-4.9t).
\]

So:

\[
t=0
\]

or

\[
14-4.9t=0.
\]

Ignore \(t=0\), because that is the launch time.

\[
4.9t=14.
\]

\[
t=\frac{14}{4.9}.
\]

\[
t=2.857\ldots
\]

So:

\[
\boxed{t=2.86\text{ s to 3 s.f.}}
\]

### Part C: Distance \(OA\)

Horizontal speed is:

\[
14\sqrt3.
\]

Time is:

\[
2.857\ldots
\]

So:

\[
OA=14\sqrt3\times 2.857\ldots
\]

Using exact \(t=\frac{14}{4.9}=\frac{20}{7}\):

\[
OA=14\sqrt3\times \frac{20}{7}.
\]

\[
OA=2\sqrt3\times 20.
\]

\[
OA=40\sqrt3.
\]

\[
OA=69.282\ldots
\]

\[
\boxed{OA=69.3\text{ m to 3 s.f.}}
\]

---

## Worked Example 5: Projection from above ground with \(\tan\theta=\frac43\)

A particle is projected from a point \(O\) with speed \(V\text{ m s}^{-1}\) at an angle of elevation \(\theta\), where:

\[
\tan\theta=\frac43.
\]

The point \(O\) is \(42.5\text{ m}\) above a horizontal plane. The particle strikes the plane at \(A\), \(5\text{ s}\) after it is projected.

Show that:

\[
V=20,
\]

then find \(OA\).

### Step 1: Build the triangle for \(\theta\)

Since:

\[
\tan\theta=\frac43,
\]

take:

\[
\text{opposite}=4,\qquad \text{adjacent}=3.
\]

Then:

\[
\text{hypotenuse}=\sqrt{3^2+4^2}.
\]

\[
\text{hypotenuse}=\sqrt{9+16}=5.
\]

So:

\[
\sin\theta=\frac45,
\]

\[
\cos\theta=\frac35.
\]

Resolve the initial velocity:

\[
u_x=V\cos\theta=\frac35V,
\]

\[
u_y=V\sin\theta=\frac45V.
\]

### Step 2: Use vertical motion

Take upwards as positive.

The particle finishes \(42.5\text{ m}\) below its starting point, so:

\[
s=-42.5.
\]

Also:

\[
u=\frac45V,\qquad a=-9.8,\qquad t=5.
\]

Use:

\[
s=ut+\frac12at^2.
\]

Substitute:

\[
-42.5=\left(\frac45V\right)(5)+\frac12(-9.8)(5^2).
\]

Simplify the first term:

\[
\left(\frac45V\right)(5)=4V.
\]

Simplify the second term:

\[
\frac12(-9.8)(25)=-4.9(25)=-122.5.
\]

So:

\[
-42.5=4V-122.5.
\]

Add \(122.5\) to both sides:

\[
80=4V.
\]

\[
\boxed{V=20}.
\]

### Step 3: Horizontal distance

\[
u_x=\frac35V.
\]

Since \(V=20\):

\[
u_x=\frac35(20)=12.
\]

Time is \(5\text{ s}\), so:

\[
x=12\times 5.
\]

\[
x=60.
\]

The horizontal distance is:

\[
60\text{ m}.
\]

### Step 4: Distance \(OA\)

The vertical difference is:

\[
42.5\text{ m}.
\]

The horizontal difference is:

\[
60\text{ m}.
\]

Use Pythagoras:

\[
OA^2=42.5^2+60^2.
\]

\[
OA=\sqrt{42.5^2+60^2}.
\]

\[
OA=\sqrt{1806.25+3600}.
\]

\[
OA=\sqrt{5406.25}.
\]

\[
OA=73.527\ldots
\]

\[
\boxed{OA=73.5\text{ m to 3 s.f.}}
\]

---

## Worked Example 6: Time above a given height

A particle is projected from a point \(O\) with speed \(35\text{ m s}^{-1}\) at angle of elevation \(30^\circ\). It moves freely under gravity.

Find the length of time for which the particle is \(15\text{ m}\) or more above \(O\).

### Step 1: Resolve vertically

\[
u_y=35\sin30^\circ.
\]

\[
u_y=35\cdot\frac12.
\]

\[
u_y=17.5.
\]

Use vertical motion with upwards positive:

\[
s=15,\qquad u=17.5,\qquad a=-9.8.
\]

Use:

\[
s=ut+\frac12at^2.
\]

\[
15=17.5t+\frac12(-9.8)t^2.
\]

\[
15=17.5t-4.9t^2.
\]

Bring all terms to one side:

\[
4.9t^2-17.5t+15=0.
\]

### Step 2: Solve the quadratic

Use exact fractions:

\[
4.9=\frac{49}{10},\qquad 17.5=\frac{35}{2}.
\]

The roots are:

\[
t=\frac{10}{7}
\]

and

\[
t=\frac{15}{7}.
\]

These are the two times when the projectile is exactly \(15\text{ m}\) above \(O\).

### Step 3: Find the time between them

\[
\text{time above }15\text{ m}=\frac{15}{7}-\frac{10}{7}.
\]

\[
=\frac{5}{7}.
\]

\[
=0.714285\ldots
\]

So:

\[
\boxed{0.71\text{ s to 2 s.f.}}
\]

---

## Worked Example 7: Vector projectile motion

A particle \(P\) is projected from the origin with velocity:

\[
12\mathbf{i}+24\mathbf{j}\text{ m s}^{-1},
\]

where \(\mathbf{i}\) and \(\mathbf{j}\) are horizontal and vertical unit vectors. The particle moves freely under gravity.

Find:

1. the position vector after \(3\text{ s}\);
2. the speed after \(3\text{ s}\).

### Part A: Position vector after \(3\text{ s}\)

Horizontal motion:

\[
u_x=12,\qquad t=3.
\]

\[
x=12\times3.
\]

\[
x=36.
\]

Vertical motion, upwards positive:

\[
u_y=24,\qquad a=-9.8,\qquad t=3.
\]

Use:

\[
s=ut+\frac12at^2.
\]

\[
y=24(3)+\frac12(-9.8)(3^2).
\]

\[
y=72-4.9(9).
\]

\[
y=72-44.1.
\]

\[
y=27.9.
\]

So the position vector is:

\[
\boxed{\mathbf{r}=36\mathbf{i}+27.9\mathbf{j}\text{ m}}.
\]

### Vector method

You can also do the calculation as:

\[
\mathbf{r}=\mathbf{u}t+\frac12\mathbf{a}t^2.
\]

Here:

\[
\mathbf{u}=12\mathbf{i}+24\mathbf{j},
\]

\[
\mathbf{a}=0\mathbf{i}-9.8\mathbf{j}.
\]

So:

\[
\mathbf{r}=(12\mathbf{i}+24\mathbf{j})(3)+\frac12(0\mathbf{i}-9.8\mathbf{j})(3^2).
\]

\[
\mathbf{r}=36\mathbf{i}+72\mathbf{j}+\frac12(0\mathbf{i}-9.8\mathbf{j})(9).
\]

\[
\mathbf{r}=36\mathbf{i}+72\mathbf{j}+(0\mathbf{i}-44.1\mathbf{j}).
\]

\[
\mathbf{r}=36\mathbf{i}+27.9\mathbf{j}.
\]

### Part B: Speed after \(3\text{ s}\)

Horizontal velocity remains constant:

\[
v_x=12.
\]

Vertical velocity:

\[
v_y=u_y+at.
\]

\[
v_y=24+(-9.8)(3).
\]

\[
v_y=24-29.4.
\]

\[
v_y=-5.4.
\]

The velocity vector is:

\[
\mathbf{v}=12\mathbf{i}-5.4\mathbf{j}.
\]

Speed is the magnitude:

\[
|\mathbf{v}|=\sqrt{12^2+(-5.4)^2}.
\]

\[
|\mathbf{v}|=\sqrt{144+29.16}.
\]

\[
|\mathbf{v}|=\sqrt{173.16}.
\]

\[
|\mathbf{v}|=13.159\ldots
\]

\[
\boxed{13.2\text{ m s}^{-1}\text{ to 3 s.f.}}
\]

---

## Guided Practice

### Practice 1

A particle is projected horizontally at \(30\text{ m s}^{-1}\) from a point \(44.1\text{ m}\) above horizontal ground.

Find:

1. the time of flight;
2. the horizontal distance travelled before impact.

### Practice 2

A particle is projected from ground level with speed \(40\text{ m s}^{-1}\) at an angle of elevation \(30^\circ\).

Find:

1. its greatest height;
2. its time of flight;
3. its range on the horizontal plane.

Take \(g=9.8\text{ m s}^{-2}\).

### Practice 3

A particle is projected with initial velocity:

\[
18\mathbf{i}+20\mathbf{j}\text{ m s}^{-1}.
\]

Find:

1. its position vector after \(2\text{ s}\);
2. its speed after \(2\text{ s}\).

### Practice 4

A projectile is launched with speed \(U\) at angle \(\theta\) above the horizontal. Show that its path is:

\[
y=x\tan\theta-\frac{gx^2}{2U^2}\left(1+\tan^2\theta\right).
\]

---

## Common Mistakes and Exam Traps

### Trap 1: Using SUVAT horizontally when \(d=vt\) is enough

You may use SUVAT horizontally with \(a=0\), but it usually turns into:

\[
s=ut.
\]

### Trap 2: Writing all five SUVAT letters every time

The transcript warns against writing all five quantities automatically. Instead, write only the values you know and the one you want. This helps you see the correct formula faster.

### Trap 3: Forgetting that \(t\) links the directions

The same time \(t\) applies to both horizontal and vertical motion. It is the bridge value.

### Trap 4: Using the wrong sign for gravity

If upwards is positive:

\[
a=-9.8.
\]

If downwards is positive:

\[
a=+9.8.
\]

Do not mix the sign convention halfway through.

### Trap 5: Treating the curved path length as the distance from start to impact

If the question asks for the distance of the impact point from the original point, use straight-line distance with Pythagoras.

Do not try to find the length of the parabolic arc.

### Trap 6: Forgetting \(v_y=0\) at the highest point

At maximum height:

\[
v_y=0,
\]

but the projectile is still moving horizontally.

So the speed at the highest point is not zero. It is the horizontal speed.

### Trap 7: Confusing speed and velocity

Velocity has direction.

Speed is magnitude.

If:

\[
\mathbf{v}=12\mathbf{i}-5.4\mathbf{j},
\]

then speed is:

\[
|\mathbf{v}|=\sqrt{12^2+(-5.4)^2}.
\]

---

## Exam Technique

For most projectile questions, use this structure:

1. Draw a diagram.
2. Resolve initial velocity into components.
3. Decide sign convention.
4. Write vertical motion separately.
5. Write horizontal motion separately.
6. Use time \(t\) to connect them.
7. Recombine components only if asked for speed, direction or magnitude.
8. Interpret the answer in context.

The transcript’s repeated exam message is that projectile questions usually come down to:

\[
\text{vertical SUVAT}+\text{horizontal }d=vt+\text{solving equations}.
\]

---

## Full Worked Solutions to Guided Practice

## Solution 1

A particle is projected horizontally at \(30\text{ m s}^{-1}\) from \(44.1\text{ m}\) above ground.

Take downwards as positive.

\[
s=44.1,\qquad u=0,\qquad a=9.8.
\]

Use:

\[
s=ut+\frac12at^2.
\]

\[
44.1=0t+\frac12(9.8)t^2.
\]

\[
44.1=4.9t^2.
\]

\[
t^2=\frac{44.1}{4.9}.
\]

\[
t^2=9.
\]

\[
t=3.
\]

So:

\[
\boxed{t=3\text{ s}}.
\]

Horizontal distance:

\[
x=vt.
\]

\[
x=30\times 3.
\]

\[
\boxed{x=90\text{ m}}.
\]

---

## Solution 2

A particle is projected from ground level with speed \(40\text{ m s}^{-1}\) at \(30^\circ\).

Resolve:

\[
u_x=40\cos30^\circ,
\]

\[
u_y=40\sin30^\circ.
\]

Since:

\[
\sin30^\circ=\frac12,
\]

\[
u_y=20.
\]

Since:

\[
\cos30^\circ=\frac{\sqrt3}{2},
\]

\[
u_x=20\sqrt3.
\]

### Greatest height

At greatest height:

\[
v_y=0.
\]

Use:

\[
v^2=u^2+2as.
\]

\[
0^2=20^2+2(-9.8)H.
\]

\[
0=400-19.6H.
\]

\[
19.6H=400.
\]

\[
H=\frac{400}{19.6}.
\]

\[
H=20.408\ldots
\]

\[
\boxed{H=20.4\text{ m to 3 s.f.}}
\]

### Time of flight

Since the particle returns to the same vertical level:

\[
s=0.
\]

\[
0=20t-4.9t^2.
\]

\[
0=t(20-4.9t).
\]

So:

\[
t=0
\]

or

\[
20-4.9t=0.
\]

\[
4.9t=20.
\]

\[
t=\frac{20}{4.9}.
\]

\[
t=4.0816\ldots
\]

\[
\boxed{t=4.08\text{ s to 3 s.f.}}
\]

### Range

\[
R=u_xt.
\]

\[
R=20\sqrt3\times 4.0816\ldots
\]

\[
R=141.391\ldots
\]

\[
\boxed{R=141\text{ m to 3 s.f.}}
\]

---

## Solution 3

\[
\mathbf{u}=18\mathbf{i}+20\mathbf{j}.
\]

\[
\mathbf{a}=0\mathbf{i}-9.8\mathbf{j}.
\]

### Position after \(2\text{ s}\)

\[
\mathbf{r}=\mathbf{u}t+\frac12\mathbf{a}t^2.
\]

\[
\mathbf{r}=(18\mathbf{i}+20\mathbf{j})(2)+\frac12(0\mathbf{i}-9.8\mathbf{j})(2^2).
\]

\[
\mathbf{r}=36\mathbf{i}+40\mathbf{j}+\frac12(0\mathbf{i}-9.8\mathbf{j})(4).
\]

\[
\mathbf{r}=36\mathbf{i}+40\mathbf{j}+(0\mathbf{i}-19.6\mathbf{j}).
\]

\[
\boxed{\mathbf{r}=36\mathbf{i}+20.4\mathbf{j}\text{ m}}.
\]

### Speed after \(2\text{ s}\)

Horizontal velocity:

\[
v_x=18.
\]

Vertical velocity:

\[
v_y=20-9.8(2).
\]

\[
v_y=20-19.6.
\]

\[
v_y=0.4.
\]

Speed:

\[
|\mathbf{v}|=\sqrt{18^2+0.4^2}.
\]

\[
|\mathbf{v}|=\sqrt{324+0.16}.
\]

\[
|\mathbf{v}|=\sqrt{324.16}.
\]

\[
|\mathbf{v}|=18.004\ldots
\]

\[
\boxed{18.0\text{ m s}^{-1}\text{ to 3 s.f.}}
\]

---

## Solution 4

Horizontal motion:

\[
x=U\cos\theta \, t.
\]

Make \(t\) the subject:

\[
t=\frac{x}{U\cos\theta}.
\]

Vertical motion:

\[
y=U\sin\theta \, t-\frac12gt^2.
\]

Substitute:

\[
y=U\sin\theta\left(\frac{x}{U\cos\theta}\right)-\frac12g\left(\frac{x}{U\cos\theta}\right)^2.
\]

Simplify:

\[
y=x\frac{\sin\theta}{\cos\theta}-\frac{gx^2}{2U^2\cos^2\theta}.
\]

\[
y=x\tan\theta-\frac{gx^2}{2U^2\cos^2\theta}.
\]

Use:

\[
\frac{1}{\cos^2\theta}=1+\tan^2\theta.
\]

Therefore:

\[
\boxed{y=x\tan\theta-\frac{gx^2}{2U^2}\left(1+\tan^2\theta\right)}.
\]

---

## Syllabus Gap Check

| LO ID | Covered? | Evidence |
|---|---:|---|
| A22-KIN-LO001 | Covered as support | Vertical SUVAT, time equations, displacement/velocity links. |
| A22-KIN-LO002 | Covered | Vector projectile example with \(\mathbf{i},\mathbf{j}\). |
| A22-KIN-LO003 | Covered | Motion under gravity in two dimensions with \(a_x=0\), \(a_y=-g\). |
| A22-KIN-LO004 | Covered | Projectile problems, derivations, range, height, trajectory. |

No official CCEA past-paper mark scheme was supplied, so the lesson does not claim exact CCEA mark allocations.

---

## Visual and Interactive Asset Plan

| Asset ID | Type | Purpose |
|---|---|---|
| A22ProjectilesMermaid-001 | Mermaid | Overall projectile problem-solving workflow. |
| A22ProjectilesMermaid-002 | Mermaid | Horizontal vs vertical motion split. |
| A22ProjectilesMermaid-003 | Mermaid | Horizontally projected particle workflow. |
| A22ProjectilesMermaid-004 | Mermaid | Angled projection workflow. |
| A22ProjectilesMermaid-005 | Mermaid | Formula derivation map. |
| A22ProjectilesMermaid-006 | Mermaid | Vector projectile workflow. |
| A22ProjectilesMermaid-007 | Mermaid | Exam trap checklist. |
| A22ProjectilesSVG-001 | SVG | Main projectile path: components, maximum height, range. |
| A22ProjectilesSVG-002 | SVG | Horizontal vs vertical motion comparison. |
| A22ProjectilesSVG-003 | SVG | Vector projectile after a given time. |
| A22ProjectilesSVG-004 | SVG | Two projectiles meeting simultaneously. |
| A22ProjectilesSVG-005 | SVG | Trajectory equation derivation. |
| A22ProjectilesTikZ-001 | TikZ | Clean exam-style projectile diagram. |
| A22ProjectilesWidget-001 | HTML widget | Interactive launch speed/angle simulator. |

---

## Supplementary Sources Used

The DrFrost/MechYr2 PDF is cross-board support, not the official CCEA specification. It is used because the CCEA A22-KIN specification includes projectiles and the derivation of projectile formulae may be required.

No GCSE source evidence is used in this lesson.

---

## Final Student Checklist

You are ready for CCEA A22 projectiles when you can:

- [ ] State the projectile modelling assumptions.
- [ ] Explain why \(a_x=0\).
- [ ] Explain why \(a_y=-g\) if upwards is positive.
- [ ] Resolve \(U\) into \(U\cos\theta\) and \(U\sin\theta\).
- [ ] Use \(d=vt\) horizontally.
- [ ] Use SUVAT vertically.
- [ ] Use time as the bridge between horizontal and vertical motion.
- [ ] Find greatest height using \(v_y=0\).
- [ ] Find range using horizontal distance.
- [ ] Find speed from velocity components using Pythagoras.
- [ ] Derive the equation of trajectory.
- [ ] Handle questions where the projectile lands below or above its starting height.
- [ ] Avoid using curved path length unless explicitly required.
- [ ] Check units and significant figures.
