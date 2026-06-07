# Variable Acceleration

## Title and Metadata

| Field | Value |
|---|---|
| Course | CCEA GCE Mathematics |
| Unit code | **A22** |
| Unit name | **A2 2 Applied Mathematics** |
| Applied section | Mechanics |
| Topic code | **A22-KIN** |
| Official topic name | Kinematics |
| Lesson title | Variable Acceleration |
| topic_slug | `variable_acceleration` |
| topic_pascal | `VariableAcceleration` |
| topic_id | `A22VariableAcceleration` |
| lesson_file | `A22_variable_acceleration_lesson.md` |
| Core LO ID | **A22-KIN-LO001** |
| Tags | `#A22`, `#Kinematics`, `#Mechanics`, `#VariableAcceleration`, `#CalculusInKinematics` |

---

## Evidence Map

| Evidence | Used for |
|---|---|
| CCEA Mathematics specification map | Unit code, topic code, official LO boundary, and confirmation that variable acceleration calculus is A22 Kinematics. |
| Project README/module map | Metadata fields, file naming and phase structure. |
| Project evidence checklist | Missing evidence log, visual placeholder rules, off-spec logging. |
| `MechYr1-Chp11-VariableAcceleration.pdf` | Slide examples, formulas, diagrams, warnings and worked examples. |
| `Chapter_11_Variable_Acceleration_🚀_(Applied_Year_1,_Mechanics)_Transcript.md` | Teacher explanations, modelling warnings, method-selection notes and graph reasoning. |
| `Chapter_11_Variable_Acceleration_🚀_(Applied_Year_1,_Mechanics)_Screenshots.pdf` | Partial visual confirmation only where readable. |
| Embedded Edexcel/Pearson examples | Cross-board support only, used where the mathematics matches CCEA A22-KIN-LO001. |

---

## Specification Alignment

### Core CCEA outcome

**A22-KIN-LO001**  
Use calculus in kinematics for motion in a straight line:

\[
v=\frac{ds}{dt},
\qquad
 a=\frac{dv}{dt}=\frac{d^2s}{dt^2},
\qquad
s=\int v\,dt,
\qquad
v=\int a\,dt.
\]

The supplied specification map also states that displacement, velocity and acceleration may be given as functions of time. This lesson is therefore a straight-line variable acceleration lesson.

### Coverage table

| Required skill | Lesson coverage |
|---|---|
| \(v=\frac{ds}{dt}\) | Differentiate displacement functions \(s(t)\) or \(x(t)\). |
| \(a=\frac{dv}{dt}\) | Differentiate velocity functions \(v(t)\). |
| \(a=\frac{d^2s}{dt^2}\) | Differentiate displacement twice. |
| \(s=\int v\,dt\) | Integrate velocity and use initial conditions. |
| \(v=\int a\,dt\) | Integrate acceleration and use initial conditions. |
| Instantaneous rest | Solve \(v(t)=0\). |
| Maximum/minimum displacement | Usually solve \(v(t)=0\), then check interval. |
| Maximum/minimum velocity | Usually solve \(a(t)=0\), then check interval. |
| Greatest speed | Compare \(|v|\), including endpoints. |
| Total distance travelled | Split at roots of \(v(t)=0\), integrate each part, add magnitudes. |

---

## Learning Objectives

By the end of this lesson, the student should be able to:

1. Recognise when a mechanics problem involves variable acceleration rather than ordinary constant-acceleration SUVAT.
2. Use \(v=\frac{ds}{dt}\), \(a=\frac{dv}{dt}\), and \(a=\frac{d^2s}{dt^2}\).
3. Use \(s=\int v\,dt\) and \(v=\int a\,dt\).
4. Find when a particle is instantaneously at rest by solving \(v=0\).
5. Find maximum or minimum displacement or velocity using derivatives and interval checks.
6. Distinguish between velocity and speed.
7. Distinguish between displacement and distance travelled.
8. Use initial conditions to find constants of integration.
9. Split a velocity-time integral at sign changes when calculating total distance travelled.
10. Derive \(v=u+at\) and \(s=ut+\frac12at^2\) using integration when acceleration is constant.

---

## Prerequisite Recap

No GCSE source is used. The recap below uses earlier A-Level knowledge only.

| Prior A-Level skill | Why it matters |
|---|---|
| AS2 kinematics language | You need position, displacement, distance travelled, velocity, speed and acceleration. |
| AS2 motion graphs | Gradient of displacement-time gives velocity; gradient of velocity-time gives acceleration; area under velocity-time gives displacement. |
| A-Level differentiation | Variable acceleration is built from rates of change. |
| A-Level integration | Integration reverses differentiation and recovers \(v\) or \(s\). |
| Polynomial algebra | You solve quadratics and cubics for times when \(v=0\) or \(a=0\). |
| Graph sketching | You use graph shape to decide signs, valid intervals and extrema. |

---

## Big Picture Explanation

Earlier kinematics often uses **constant acceleration**. When acceleration is constant, the velocity-time graph is made from straight-line pieces and SUVAT formulae work directly.

Variable acceleration changes the game. Displacement, velocity or acceleration can be given as a function of time, such as

\[
v=\frac12t^3.
\]

Then the velocity-time graph can be curved. Its gradient can change from moment to moment, so acceleration can change from moment to moment too.

The whole topic is the chain

\[
\boxed{s \xrightarrow{\frac{d}{dt}} v \xrightarrow{\frac{d}{dt}} a}
\]

and, in reverse,

\[
\boxed{a \xrightarrow{\int\,dt} v \xrightarrow{\int\,dt} s}.
\]

Down the chain, differentiate. Up the chain, integrate. This is the calculus engine humming under the bonnet.

---

## Key Definitions and Notation

### Time

\[
t
\]

usually means time in seconds.

### Displacement

\[
s(t)\quad\text{or}\quad x(t)
\]

means the signed position of the particle relative to a fixed point or origin. Displacement can be negative.

### Distance travelled

Distance travelled is the total length of the path. It is never negative. If a particle moves forwards and backwards, distance travelled is not simply final displacement minus initial displacement.

### Velocity

\[
v(t)
\]

means signed rate of change of displacement:

\[
v=\frac{ds}{dt}.
\]

Velocity can be negative. Negative velocity means motion in the negative direction.

### Speed

Speed is the magnitude of velocity:

\[
\text{speed}=|v|.
\]

For example, if \(v=-25\text{ m s}^{-1}\), the speed is \(25\text{ m s}^{-1}\).

### Acceleration

\[
a(t)
\]

means rate of change of velocity:

\[
a=\frac{dv}{dt}.
\]

Since

\[
v=\frac{ds}{dt},
\]

we also have

\[
a=\frac{d}{dt}\left(\frac{ds}{dt}\right)=\frac{d^2s}{dt^2}.
\]

### Instantaneously at rest

A particle is instantaneously at rest when

\[
v=0.
\]

“Instantaneously” means it is at rest for a moment. It may immediately start moving again.

---

## Core Theory

### 1. Functions of time

In variable acceleration problems, displacement, velocity or acceleration is given as a function of \(t\).

For example:

\[
v=\frac12t^3.
\]

To find velocity after \(4\) seconds, substitute \(t=4\):

\[
v=\frac12(4)^3.
\]

To find the time when \(v=108\text{ m s}^{-1}\), solve

\[
108=\frac12t^3.
\]

If \(s\), \(v\), or \(a\) is given as a function of time, do not automatically use SUVAT. SUVAT is for constant acceleration unless a derivation or special condition allows it.

---

### 2. Differentiating down the chain

\[
s \longrightarrow v \longrightarrow a.
\]

From displacement to velocity:

\[
v=\frac{ds}{dt}.
\]

If the displacement is called \(x\), then

\[
v=\frac{dx}{dt}.
\]

From velocity to acceleration:

\[
a=\frac{dv}{dt}.
\]

From displacement to acceleration directly:

\[
a=\frac{d^2s}{dt^2}
\]

or, if displacement is \(x\),

\[
a=\frac{d^2x}{dt^2}.
\]

---

### 3. Integrating up the chain

\[
a \longrightarrow v \longrightarrow s.
\]

From acceleration to velocity:

\[
v=\int a\,dt.
\]

From velocity to displacement:

\[
s=\int v\,dt.
\]

If you integrate indefinitely, include a constant:

\[
s=\int v\,dt+C.
\]

Then use a known value such as \(t=0,\ s=5\) to find \(C\).

---

### 4. Rest, direction changes and roots

A particle is at rest when

\[
v=0.
\]

Solving \(v(t)=0\) gives possible times when the particle stops, turns around or touches rest momentarily.

If a velocity-time graph crosses the \(t\)-axis, velocity changes sign. That means the particle changes direction.

---

### 5. Velocity versus speed

Velocity is signed. Speed is magnitude.

Compare:

\[
v=24
\]

and

\[
v=-30.
\]

The greatest velocity is \(24\), because \(24>-30\).  
The greatest speed is \(30\), because \(|-30|=30\).

---

### 6. Maximum and minimum problems

If \(s(t)\) has a local maximum or minimum, then

\[
\frac{ds}{dt}=0.
\]

Since

\[
\frac{ds}{dt}=v,
\]

this means

\[
v=0.
\]

If \(v(t)\) has a local maximum or minimum, then

\[
\frac{dv}{dt}=0.
\]

Since

\[
\frac{dv}{dt}=a,
\]

this means

\[
a=0.
\]

For a closed interval such as \(0\leq t\leq5\), always check endpoints and stationary points inside the interval.

---

### 7. Displacement versus total distance travelled

Signed displacement over an interval is

\[
\int_a^b v(t)\,dt.
\]

Total distance travelled is

\[
\int_a^b |v(t)|\,dt.
\]

In practice:

1. solve \(v(t)=0\);
2. split the interval at valid roots;
3. integrate each part;
4. take positive area values;
5. add them.

If the velocity-time graph goes above and below the axis, one signed integral can cancel positive and negative movement. That gives displacement, not total distance.

---

### 8. Deriving SUVAT using integration

If acceleration is constant, then \(a\) is a constant.

Starting from

\[
a=\frac{dv}{dt},
\]

integrate:

\[
v=\int a\,dt.
\]

Since \(a\) is constant,

\[
v=at+c.
\]

If initial velocity is \(u\), then when \(t=0\),

\[
v=u.
\]

So

\[
u=a(0)+c,
\]

\[
u=c.
\]

Therefore

\[
v=u+at.
\]

Now integrate again:

\[
s=\int v\,dt.
\]

Substitute \(v=u+at\):

\[
s=\int(u+at)\,dt.
\]

Since \(u\) and \(a\) are constants,

\[
s=ut+\frac12at^2+c.
\]

If initial displacement is \(0\), then when \(t=0\),

\[
s=0.
\]

So

\[
0=u(0)+\frac12a(0)^2+c,
\]

\[
0=0+0+c,
\]

\[
c=0.
\]

Therefore

\[
s=ut+\frac12at^2.
\]

---

## Visual Asset Integration

[VISUAL PLACEHOLDER: A22VariableAccelerationSVG-001 | Source: CCEA A22-KIN-LO001 + lesson PDF page 3 | Insert from svg/A22VariableAccelerationSVG-001.svg | Purpose: Show constant acceleration graph pieces beside a curved velocity-time graph.]

[VISUAL PLACEHOLDER: A22VariableAccelerationSVG-002 | Source: CCEA A22-KIN-LO001 + lesson PDF pages 5 and 11 | Insert from svg/A22VariableAccelerationSVG-002.svg | Purpose: Show the \(s\), \(v\), \(a\) differentiation and integration chain.]

[VISUAL PLACEHOLDER: A22VariableAccelerationSVG-003 | Source: lesson PDF page 8 | Insert from svg/A22VariableAccelerationSVG-003.svg | Purpose: Show the yo-yo cubic displacement graph and why \(0\leq t\leq3\).]

[VISUAL PLACEHOLDER: A22VariableAccelerationSVG-004 | Source: lesson PDF pages 12 and 13 | Insert from svg/A22VariableAccelerationSVG-004.svg | Purpose: Show positive and negative velocity-time areas for total distance travelled.]

[VISUAL PLACEHOLDER: A22VariableAccelerationSVG-005 | Source: lesson PDF pages 3 and 9 | Insert from svg/A22VariableAccelerationSVG-005.svg | Purpose: Show that greatest speed means greatest \(|v|\).]

[INTERACTIVE PLACEHOLDER: A22VariableAccelerationWidget-001 | Source: CCEA A22-KIN-LO001 + lesson evidence | Insert from widgets/A22VariableAccelerationWidget-001.html | Purpose: Let the student enter \(s(t)\), \(v(t)\) or \(a(t)\) and move up/down the calculus chain.]

[INTERACTIVE PLACEHOLDER: A22VariableAccelerationWidget-002 | Source: lesson PDF pages 12 and 13 | Insert from widgets/A22VariableAccelerationWidget-002.html | Purpose: Compare signed displacement with total distance travelled.]

[INTERACTIVE PLACEHOLDER: A22VariableAccelerationWidget-003 | Source: lesson PDF pages 8 and 9 | Insert from widgets/A22VariableAccelerationWidget-003.html | Purpose: Practise choosing \(v=0\), \(a=0\), \(|v|\), or integration.]

---

## Worked Examples

### Worked Example 1: Substituting into a velocity function

The velocity-time graph of a body is given by

\[
v=\frac12t^3.
\]

#### (a) Find the velocity after \(4\) seconds.

Substitute \(t=4\):

\[
v=\frac12(4)^3.
\]

\[
4^3=64.
\]

\[
v=\frac12(64).
\]

\[
v=32.
\]

\[
\boxed{32\text{ m s}^{-1}}
\]

#### (b) Find how many seconds have elapsed when \(v=108\text{ m s}^{-1}\).

\[
108=\frac12t^3.
\]

Multiply by \(2\):

\[
216=t^3.
\]

Take the cube root:

\[
t=\sqrt[3]{216}.
\]

Since

\[
6^3=216,
\]

\[
\boxed{t=6\text{ s}}.
\]

---

### Worked Example 2: Velocity as a quadratic function of time

A body moves in a straight line such that

\[
v=2t^2-16t+24.
\]

Find:

1. the initial velocity;
2. the values of \(t\) when the body is instantaneously at rest;
3. the value of \(t\) when \(v=64\text{ m s}^{-1}\);
4. the greatest speed in \(0\leq t\leq5\).

#### (a) Initial velocity

Initial means \(t=0\).

\[
v=2(0)^2-16(0)+24.
\]

\[
v=24.
\]

\[
\boxed{24\text{ m s}^{-1}}
\]

#### (b) Instantaneously at rest

At rest means \(v=0\).

\[
0=2t^2-16t+24.
\]

Divide by \(2\):

\[
0=t^2-8t+12.
\]

Factorise:

\[
0=(t-2)(t-6).
\]

So

\[
\boxed{t=2\text{ s}\quad\text{or}\quad t=6\text{ s}}.
\]

#### (c) Velocity \(64\text{ m s}^{-1}\)

\[
64=2t^2-16t+24.
\]

\[
0=2t^2-16t-40.
\]

Divide by \(2\):

\[
0=t^2-8t-20.
\]

\[
0=(t-10)(t+2).
\]

So

\[
t=10
\]

or

\[
t=-2.
\]

Reject \(t=-2\) for time after the start:

\[
\boxed{t=10\text{ s}}.
\]

#### (d) Greatest speed in \(0\leq t\leq5\)

Speed is \(|v|\). The roots of the quadratic are \(t=2\) and \(t=6\), so by symmetry the vertex is at

\[
t=\frac{2+6}{2}=4.
\]

Check \(t=0\), \(t=4\), and \(t=5\).

At \(t=0\), \(v=24\).

At \(t=4\),

\[
v=2(4)^2-16(4)+24=32-64+24=-8.
\]

At \(t=5\),

\[
v=2(5)^2-16(5)+24=50-80+24=-6.
\]

Compare speeds:

\[
|24|=24,
\qquad
|-8|=8,
\qquad
|-6|=6.
\]

\[
\boxed{24\text{ m s}^{-1}}
\]

---

### Worked Example 3: Differentiating displacement

A particle \(P\) moves on the \(x\)-axis. At time \(t\) seconds, displacement from \(O\) is

\[
x=t^4-32t+14.
\]

Differentiate displacement:

\[
v=\frac{dx}{dt}=4t^3-32.
\]

Velocity when \(t=3\):

\[
v=4(3)^3-32=4(27)-32=76.
\]

\[
\boxed{76\text{ m s}^{-1}}
\]

At rest:

\[
4t^3-32=0.
\]

\[
4t^3=32.
\]

\[
t^3=8.
\]

\[
\boxed{t=2\text{ s}}
\]

Acceleration:

\[
a=\frac{dv}{dt}=12t^2.
\]

At \(t=1.5\):

\[
a=12(1.5)^2=12(2.25)=27.
\]

\[
\boxed{27\text{ m s}^{-2}}
\]

---

### Worked Example 4: The cat displacement problem

Pudding the Cat’s displacement from a house is

\[
s=t^3-\frac32t^2-36t.
\]

Differentiate:

\[
v=\frac{ds}{dt}=3t^2-3t-36.
\]

When \(t=2\):

\[
v=3(2)^2-3(2)-36=12-6-36=-30.
\]

\[
\boxed{-30\text{ m s}^{-1}}
\]

At rest:

\[
3t^2-3t-36=0.
\]

Divide by \(3\):

\[
t^2-t-12=0.
\]

\[
(t+3)(t-4)=0.
\]

Reject negative time:

\[
\boxed{t=4\text{ s}}.
\]

Acceleration:

\[
a=\frac{dv}{dt}=6t-3.
\]

At \(t=5\):

\[
a=6(5)-3=27.
\]

\[
\boxed{27\text{ m s}^{-2}}
\]

---

### Worked Example 5: Maximum distance of a yo-yo

A yo-yo has distance from the child’s hand

\[
s=0.6t+0.4t^2-0.2t^3,
\qquad
0\leq t\leq3.
\]

#### (a) Justify the restriction \(0\leq t\leq3\)

Write decimals as fractions:

\[
s=\frac35t+\frac25t^2-\frac15t^3.
\]

Factor out \(\frac15t\):

\[
s=\frac15t(3+2t-t^2).
\]

Factor the quadratic:

\[
3+2t-t^2=(3-t)(1+t).
\]

So

\[
s=\frac15t(3-t)(1+t).
\]

The roots are

\[
t=0,
\quad
 t=3,
\quad
 t=-1.
\]

The motion starts at \(t=0\), so negative time is not relevant. For \(0<t<3\), all factors \(t\), \(3-t\), and \(1+t\) are positive, so \(s>0\). At \(t=0\) and \(t=3\), \(s=0\). For \(t>3\), \(s<0\), which is impossible for a distance from the hand.

\[
\boxed{0\leq t\leq3}
\]

#### (b) Find the maximum distance

\[
\frac{ds}{dt}=0.6+0.8t-0.6t^2.
\]

Set equal to zero:

\[
0.6+0.8t-0.6t^2=0.
\]

Multiply by \(10\):

\[
6+8t-6t^2=0.
\]

\[
6t^2-8t-6=0.
\]

Divide by \(2\):

\[
3t^2-4t-3=0.
\]

Use the quadratic formula:

\[
t=\frac{4\pm\sqrt{(-4)^2-4(3)(-3)}}{2(3)}.
\]

\[
t=\frac{4\pm\sqrt{52}}{6}.
\]

\[
t=1.8685\ldots
\]

or

\[
t=-0.5351\ldots
\]

Reject the negative time. Substitute \(t=1.8685\ldots\) into \(s\):

\[
s=0.6(1.8685)+0.4(1.8685)^2-0.2(1.8685)^3.
\]

\[
s=1.209\ldots
\]

\[
\boxed{1.21\text{ m to 3 s.f.}}
\]

---

### Worked Example 6: Maximum velocity of a dolphin

The slide version gives

\[
v=t^3-16t^2+64t.
\]

At maximum velocity:

\[
\frac{dv}{dt}=0.
\]

\[
\frac{dv}{dt}=3t^2-32t+64.
\]

\[
3t^2-32t+64=0.
\]

Factorise:

\[
(3t-8)(t-8)=0.
\]

So

\[
t=\frac83
\]

or

\[
t=8.
\]

The local maximum occurs at \(t=\frac83\). Substitute into \(v\):

\[
v=\left(\frac83\right)^3-16\left(\frac83\right)^2+64\left(\frac83\right).
\]

\[
v=\frac{512}{27}-\frac{1024}{9}+\frac{512}{3}.
\]

Use denominator \(27\):

\[
v=\frac{512}{27}-\frac{3072}{27}+\frac{4608}{27}.
\]

\[
v=\frac{2048}{27}=75.8518\ldots
\]

\[
\boxed{75.9\text{ m s}^{-1}\text{ to 3 s.f.}}
\]

---

### Worked Example 7: Greatest speed in an interval

A particle has velocity

\[
v=2t^2-14t+20,
\qquad t\geq0.
\]

At rest:

\[
2t^2-14t+20=0.
\]

\[
2(t^2-7t+10)=0.
\]

\[
2(t-2)(t-5)=0.
\]

\[
\boxed{t=2\text{ s}\quad\text{or}\quad t=5\text{ s}}
\]

For greatest speed, check endpoints and stationary velocity.

\[
a=\frac{dv}{dt}=4t-14.
\]

Set \(a=0\):

\[
4t-14=0.
\]

\[
t=\frac72.
\]

Evaluate \(v\) at \(t=0,\frac72,4\):

\[
v(0)=20.
\]

\[
v\left(\frac72\right)=2\left(\frac72\right)^2-14\left(\frac72\right)+20.
\]

\[
=\frac{49}{2}-49+20.
\]

\[
=-\frac92.
\]

\[
v(4)=32-56+20=-4.
\]

Compare speeds:

\[
|20|=20,
\qquad
\left|-\frac92\right|=\frac92,
\qquad
|-4|=4.
\]

\[
\boxed{20\text{ m s}^{-1}}
\]

---

### Worked Example 8: Integrating velocity to find displacement

A particle is at \(x=5\) when \(t=0\). Its velocity is

\[
v=6t-t^2.
\]

Since

\[
v=\frac{dx}{dt},
\]

\[
x=\int(6t-t^2)\,dt.
\]

\[
x=3t^2-\frac13t^3+c.
\]

Use \(t=0,\ x=5\):

\[
5=0-0+c.
\]

\[
c=5.
\]

\[
\boxed{x=3t^2-\frac13t^3+5}
\]

At \(t=6\):

\[
x=3(6)^2-\frac13(6)^3+5.
\]

\[
x=108-72+5=41.
\]

Starting point was \(x=5\). Distance from starting point:

\[
41-5=36.
\]

\[
\boxed{36\text{ m}}
\]

---

### Worked Example 9: Distance in the third second

A particle has velocity

\[
v=5-3t^2,
\qquad t\geq0.
\]

The third second is

\[
2\leq t\leq3.
\]

Signed displacement:

\[
\int_2^3(5-3t^2)\,dt.
\]

\[
=\left[5t-t^3\right]_2^3.
\]

\[
=(15-27)-(10-8).
\]

\[
=-12-2=-14.
\]

Distance is positive:

\[
\boxed{14\text{ m}}
\]

---

### Worked Example 10: Total distance when velocity changes sign

A particle has velocity

\[
v=2t^2-9t+4.
\]

When \(t=0\), it is \(15\text{ m}\) from \(O\).

At rest:

\[
2t^2-9t+4=0.
\]

\[
(2t-1)(t-4)=0.
\]

\[
\boxed{t=\frac12\text{ s}\quad\text{or}\quad t=4\text{ s}}
\]

Acceleration:

\[
a=\frac{dv}{dt}=4t-9.
\]

At \(t=5\):

\[
a=20-9=11.
\]

\[
\boxed{11\text{ m s}^{-2}}
\]

Integrate velocity:

\[
s=\int(2t^2-9t+4)\,dt.
\]

\[
s=\frac23t^3-\frac92t^2+4t+C.
\]

Use \(s(0)=15\):

\[
C=15.
\]

\[
s=\frac23t^3-\frac92t^2+4t+15.
\]

Evaluate at key times:

\[
s(0)=15.
\]

\[
s\left(\frac12\right)=\frac23\left(\frac12\right)^3-\frac92\left(\frac12\right)^2+4\left(\frac12\right)+15.
\]

\[
=\frac1{12}-\frac98+2+15.
\]

\[
=\frac{383}{24}.
\]

\[
s(4)=\frac23(64)-\frac92(16)+16+15.
\]

\[
=\frac{128}{3}-72+31.
\]

\[
=\frac{5}{3}.
\]

\[
s(5)=\frac23(125)-\frac92(25)+20+15.
\]

\[
=\frac{250}{3}-\frac{225}{2}+35.
\]

\[
=\frac{35}{6}.
\]

Distances:

\[
\left|s\left(\frac12\right)-s(0)\right|
=\left|\frac{383}{24}-15\right|
=\frac{23}{24}.
\]

\[
\left|s(4)-s\left(\frac12\right)\right|
=\left|\frac53-\frac{383}{24}\right|
=\frac{343}{24}.
\]

\[
|s(5)-s(4)|
=\left|\frac{35}{6}-\frac53\right|
=\frac{25}{6}
=\frac{100}{24}.
\]

Total distance:

\[
\frac{23}{24}+\frac{343}{24}+\frac{100}{24}
=\frac{466}{24}
=\frac{233}{12}.
\]

\[
\boxed{\frac{233}{12}\text{ m}=19.4\text{ m to 3 s.f.}}
\]

---

### Worked Example 11: Deriving constant acceleration formulae

Given constant acceleration \(a\), initial velocity \(u\), and initial displacement \(0\), prove:

\[
v=u+at
\]

and

\[
s=ut+\frac12at^2.
\]

Start with

\[
a=\frac{dv}{dt}.
\]

\[
v=\int a\,dt.
\]

Because \(a\) is constant,

\[
v=at+C.
\]

When \(t=0\), \(v=u\):

\[
u=0+C.
\]

\[
C=u.
\]

Therefore

\[
\boxed{v=u+at}.
\]

Now

\[
s=\int v\,dt.
\]

\[
s=\int(u+at)\,dt.
\]

\[
s=ut+\frac12at^2+C.
\]

When \(t=0\), \(s=0\):

\[
0=0+0+C.
\]

\[
C=0.
\]

Therefore

\[
\boxed{s=ut+\frac12at^2}.
\]

---

## Guided Practice

### Practice Question 1

A particle moves in a straight line with displacement

\[
s=t^3-6t^2+9t.
\]

Find:

1. \(v(t)\);
2. \(a(t)\);
3. the times when the particle is instantaneously at rest.

### Practice Question 2

A particle has velocity

\[
v=t^2-5t+6.
\]

Find:

1. the times when the particle is instantaneously at rest;
2. the displacement from \(t=0\) to \(t=4\);
3. the total distance travelled from \(t=0\) to \(t=4\).

### Practice Question 3

A particle has velocity

\[
v=2t^2-3t+5.
\]

Show that the particle never comes to rest.

### Practice Question 4

A body starts at rest and moves in a straight line. Its displacement from its starting point is

\[
s=4t^3-t^4.
\]

For \(0\leq t\leq4\), show that:

1. the body returns to its starting point at \(t=4\);
2. \(s\) is always non-negative;
3. the maximum displacement is \(27\text{ m}\).

---

## Common Mistakes and Exam Traps

### Mistake 1: Using SUVAT when acceleration is variable

If

\[
v=2t^2-16t+24,
\]

then

\[
a=\frac{dv}{dt}=4t-16,
\]

which changes with time. Ordinary SUVAT is not the first method.

### Mistake 2: Forgetting the constant of integration

\[
x=\int(6t-t^2)\,dt=3t^2-\frac13t^3+C.
\]

Do not drop \(C\) unless you are using a definite integral.

### Mistake 3: Putting a critical time into the wrong function

If you solve \(a=0\) to find the time of maximum velocity, substitute the time into \(v(t)\), not \(a(t)\).

### Mistake 4: Treating speed and velocity as the same

Speed is \(|v|\). Velocity is signed.

### Mistake 5: Using one signed integral for total distance

\[
\int_a^b v(t)\,dt
\]

gives displacement. Total distance needs split intervals if \(v\) changes sign.

### Mistake 6: Keeping negative time when the model starts at \(t=0\)

Reject negative times unless the context explicitly allows them.

### Mistake 7: Not checking endpoints

Maximum values on a closed interval can occur at endpoints.

---

## Exam Technique

| Wording | Mathematical translation |
|---|---|
| Initial velocity | Set \(t=0\) in \(v(t)\). |
| Initial displacement | Set \(t=0\) in \(s(t)\). |
| Instantaneously at rest | Set \(v=0\). |
| Maximum displacement | Usually solve \(v=0\), then check interval. |
| Maximum velocity | Usually solve \(a=0\), then check interval. |
| Greatest speed | Compare \(|v|\) at candidates. |
| Distance travelled | Integrate \(|v|\), or split signed areas. |
| Displacement | Signed integral of velocity. |

### Method selection

If given \(s(t)\):

\[
s(t)\xrightarrow{\frac{d}{dt}}v(t)\xrightarrow{\frac{d}{dt}}a(t).
\]

If given \(v(t)\):

\[
v(t)\xrightarrow{\frac{d}{dt}}a(t),
\]

or

\[
v(t)\xrightarrow{\int\,dt}s(t).
\]

If given \(a(t)\):

\[
a(t)\xrightarrow{\int\,dt}v(t)\xrightarrow{\int\,dt}s(t).
\]

### Units

| Quantity | Unit |
|---|---|
| \(t\) | seconds, s |
| \(s,x\) | metres, m |
| \(v\) | metres per second, \(\text{m s}^{-1}\) |
| \(a\) | metres per second squared, \(\text{m s}^{-2}\) |

---

## Full Worked Solutions to Guided Practice

### Solution to Practice Question 1

\[
s=t^3-6t^2+9t.
\]

\[
v=\frac{ds}{dt}=3t^2-12t+9.
\]

\[
a=\frac{dv}{dt}=6t-12.
\]

At rest:

\[
3t^2-12t+9=0.
\]

Divide by \(3\):

\[
t^2-4t+3=0.
\]

\[
(t-1)(t-3)=0.
\]

\[
\boxed{t=1\text{ s}\quad\text{or}\quad t=3\text{ s}}
\]

---

### Solution to Practice Question 2

\[
v=t^2-5t+6.
\]

At rest:

\[
t^2-5t+6=0.
\]

\[
(t-2)(t-3)=0.
\]

\[
\boxed{t=2\text{ s}\quad\text{or}\quad t=3\text{ s}}
\]

Displacement:

\[
\int_0^4(t^2-5t+6)\,dt.
\]

\[
=\left[\frac13t^3-\frac52t^2+6t\right]_0^4.
\]

\[
=\frac{64}{3}-40+24.
\]

\[
=\frac{64}{3}-16.
\]

\[
=\frac{16}{3}.
\]

\[
\boxed{\frac{16}{3}\text{ m}}
\]

Total distance: split at \(t=2\) and \(t=3\).

Let

\[
F(t)=\frac13t^3-\frac52t^2+6t.
\]

\[
F(0)=0.
\]

\[
F(2)=\frac83-10+12=\frac{14}{3}.
\]

\[
F(3)=9-\frac{45}{2}+18=\frac92.
\]

\[
F(4)=\frac{16}{3}.
\]

Distance pieces:

\[
\left|F(2)-F(0)\right|=\frac{14}{3}.
\]

\[
\left|F(3)-F(2)\right|=\left|\frac92-\frac{14}{3}\right|=\frac16.
\]

\[
\left|F(4)-F(3)\right|=\left|\frac{16}{3}-\frac92\right|=\frac56.
\]

Total:

\[
\frac{14}{3}+\frac16+\frac56
=\frac{14}{3}+1
=\frac{17}{3}.
\]

\[
\boxed{\frac{17}{3}\text{ m}}
\]

---

### Solution to Practice Question 3

\[
v=2t^2-3t+5.
\]

To show the particle never comes to rest, show \(v=0\) has no real solution.

\[
\Delta=b^2-4ac.
\]

Here

\[
a=2,
\quad
b=-3,
\quad
c=5.
\]

\[
\Delta=(-3)^2-4(2)(5).
\]

\[
\Delta=9-40=-31.
\]

Since \(\Delta<0\), the quadratic has no real roots. Since the coefficient of \(t^2\) is positive, \(v>0\) for all real \(t\).

\[
\boxed{\text{The particle never comes to rest.}}
\]

---

### Solution to Practice Question 4

\[
s=4t^3-t^4.
\]

At \(t=4\):

\[
s=4(4)^3-(4)^4.
\]

\[
s=4(64)-256=256-256=0.
\]

So the body returns to its starting point at \(t=4\).

Factorise:

\[
s=4t^3-t^4=t^3(4-t).
\]

For \(0\leq t\leq4\):

\[
t^3\geq0
\]

and

\[
4-t\geq0.
\]

Therefore

\[
s=t^3(4-t)\geq0.
\]

For maximum displacement:

\[
v=\frac{ds}{dt}=12t^2-4t^3.
\]

\[
v=4t^2(3-t).
\]

Set \(v=0\):

\[
4t^2(3-t)=0.
\]

\[
t=0
\quad\text{or}\quad
 t=3.
\]

Check endpoint \(t=4\).

\[
s(0)=0.
\]

\[
s(3)=4(3)^3-(3)^4.
\]

\[
s(3)=108-81=27.
\]

\[
s(4)=0.
\]

\[
\boxed{27\text{ m}}
\]

---

## Common CCEA-Style Wording

| Wording | What to do |
|---|---|
| “At time \(t\) seconds, the displacement is…” | Differentiate to get velocity and acceleration. |
| “At time \(t\) seconds, the velocity is…” | Differentiate for acceleration or integrate for displacement. |
| “Instantaneously at rest” | Solve \(v=0\). |
| “Find the acceleration when…” | Use \(a=\frac{dv}{dt}\) or \(a=\frac{d^2s}{dt^2}\). |
| “Find the distance travelled” | Consider sign changes in \(v\). |
| “Find the displacement” | Use the signed integral of velocity. |
| “Maximum velocity” | Usually solve \(a=0\), then check context. |
| “Greatest speed” | Compare magnitudes \(|v|\), including endpoints. |
| “Justify the restriction” | Use graph, factorisation, physical meaning and \(t\geq0\). |
| “Show that the particle never comes to rest” | Show \(v=0\) has no valid solution. |

---

## Syllabus Gap Check

| LO or topic | Covered? | Notes |
|---|---|---|
| A22-KIN-LO001 | Yes | Fully covered for straight-line motion with calculus. |
| A22-KIN-LO002 | No | Two-dimensional vector calculus is a separate lesson. |
| A22-KIN-LO003 | No | Motion under gravity in two dimensions is a separate lesson. |
| A22-KIN-LO004 | No | Projectiles are a separate lesson. |
| AS2 constant acceleration | Recapped only | Included as comparison and integration derivation. |
| Cross-board examples | Controlled | Used only where aligned to CCEA A22-KIN-LO001. |
| Distance versus displacement | Yes | Covered through signed and absolute area. |
| Maxima/minima | Yes | Covered through \(v=0\), \(a=0\), endpoints and graph reasoning. |

---

## Visual and Interactive Asset Plan

| Asset ID | Type | Purpose |
|---|---|---|
| A22VariableAccelerationMermaid-001 | Mermaid | \(s\), \(v\), \(a\) differentiation/integration chain. |
| A22VariableAccelerationMermaid-002 | Mermaid | Method-choice flowchart. |
| A22VariableAccelerationMermaid-003 | Mermaid | Constant versus variable acceleration. |
| A22VariableAccelerationMermaid-004 | Mermaid | Maxima/minima decision flowchart. |
| A22VariableAccelerationMermaid-005 | Mermaid | Displacement versus total distance. |
| A22VariableAccelerationMermaid-006 | Mermaid | SUVAT derivation by integration. |
| A22VariableAccelerationMermaid-007 | Mermaid | Greatest speed method. |
| A22VariableAccelerationSVG-001 | SVG | Constant versus variable acceleration graph comparison. |
| A22VariableAccelerationSVG-002 | SVG | Calculus chain. |
| A22VariableAccelerationSVG-003 | SVG | Yo-yo valid interval. |
| A22VariableAccelerationSVG-004 | SVG | Signed velocity-time areas. |
| A22VariableAccelerationSVG-005 | SVG | Greatest speed and \(|v|\). |
| A22VariableAccelerationTikZ-001 | TikZ | Calculus chain. |
| A22VariableAccelerationTikZ-002 | TikZ | Constant versus variable acceleration. |
| A22VariableAccelerationTikZ-003 | TikZ | Signed areas and distance. |
| A22VariableAccelerationTikZ-004 | TikZ | Greatest speed. |
| A22VariableAccelerationTikZ-005 | TikZ | Yo-yo interval. |
| A22VariableAccelerationTikZ-006 | TikZ | SUVAT derivation. |
| A22VariableAccelerationWidget-001 | Widget | Polynomial calculus chain explorer. |
| A22VariableAccelerationWidget-002 | Widget | Distance versus displacement checker. |
| A22VariableAccelerationWidget-003 | Widget | Maxima/minima method trainer. |

---

## Supplementary Sources Used

| Source | Status |
|---|---|
| CCEA specification map | Core authority. |
| Module map | Project metadata authority. |
| Evidence checklist | Workflow authority. |
| Dr Frost/Pearson slide PDF | Cross-board lesson evidence, used where CCEA-aligned. |
| Teacher transcript | Cross-board lesson evidence, used where CCEA-aligned. |
| Screenshot PDF | Partial visual confirmation only. |
| Edexcel M2 examples embedded in slides | Cross-board practice support only, not CCEA past-paper evidence. |

---

## Final Student Checklist

- [ ] I can explain why variable acceleration problems use calculus rather than automatic SUVAT.
- [ ] I know \(v=\frac{ds}{dt}\).
- [ ] I know \(a=\frac{dv}{dt}=\frac{d^2s}{dt^2}\).
- [ ] I know \(s=\int v\,dt\).
- [ ] I know \(v=\int a\,dt\).
- [ ] I can find when a particle is instantaneously at rest by solving \(v=0\).
- [ ] I can find maximum displacement by solving \(v=0\), then checking the interval.
- [ ] I can find maximum velocity by solving \(a=0\), then checking the interval.
- [ ] I know speed means \(|v|\), not just \(v\).
- [ ] I can split a velocity-time integral when \(v\) changes sign.
- [ ] I can use initial conditions to find constants of integration.
- [ ] I can derive \(v=u+at\) and \(s=ut+\frac12at^2\) using integration.
- [ ] I can reject negative times when the context starts at \(t=0\).
- [ ] I can explain a physical restriction such as \(0\leq t\leq3\).

---

## Final Quality Check Summary

| Check | Result |
|---|---|
| Unit prefix correct | Yes, A22 |
| Standard CCEA Mathematics, not Further Mathematics | Yes |
| Topic code correct | Yes, A22-KIN |
| Topic identity complete | Yes |
| LO IDs preserved exactly | Yes, A22-KIN-LO001 |
| Other A22 Kinematics LOs controlled | Yes, A22-KIN-LO002 to LO004 excluded from core |
| On-spec evidence covered | Yes |
| Cross-board material labelled | Yes |
| Off-spec material excluded or marked | Yes |
| Visual placeholders planned | Yes |
| Mermaid/SVG/TikZ/widgets listed | Yes |
| Unresolved issues | Screenshot PDF remains partial visual evidence; no CCEA past-paper questions were supplied. |
