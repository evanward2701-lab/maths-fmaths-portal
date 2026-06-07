# FA22 Further Kinematics: Variable Acceleration, Straight-Line Motion and 3D Kinematics

## 1. Lesson Title and Metadata

| Metadata field | Value |
|---|---|
| Date generated | 2026-06-04 |
| Course | CCEA GCE Further Mathematics |
| Unit | `FA22`: Further A2 2 Applied Mathematics |
| Applied section | Section B: Mechanics 2 |
| Topic code | `FA22-FKIN` |
| Topic name | Further kinematics |
| Topic slug | `further_kinematics` |
| Topic Pascal | `FurtherKinematics` |
| Topic ID | `FA22FurtherKinematics` |
| Lesson file | `FA22_further_kinematics_lesson.md` |
| Core LO IDs | `FA22-FKIN-LO001`, `FA22-FKIN-LO002` |
| Bridge tags | AS2 Kinematics, A22 Kinematics, AS1 Vectors, A21 Calculus |
| Topic tags | `#FA22`, `#FKIN`, `#Mechanics2`, `#Kinematics3D`, `#VariableAcceleration`, `#SectionB` |

### Lesson focus

This lesson teaches CCEA **Further kinematics** through two intertwined strands:

1. **Variable acceleration along a straight line**, where acceleration may be given as a function of time, displacement or velocity.
2. **Three-dimensional kinematics**, where position, velocity and acceleration are vector functions using \(\mathbf{i}\), \(\mathbf{j}\), and \(\mathbf{k}\).

The supplied lesson evidence is strongest for the straight-line variable-acceleration strand. The 3D vector strand is included because it is required by the CCEA Further Mathematics specification, but it is marked as evidence-light where appropriate.

## 2. Evidence Map

| Source | Type | Used in this lesson | Evidence status |
|---|---|---|---|
| `CCEA_GCE_Further_Mathematics_Specification_Map.md` | Project source | Official unit, topic and LO boundary | Authority source. |
| `Further_Maths_README_module_map.md` | Project source | Bridge mapping and topic organisation | Supporting source. |
| `Further_Maths_EVIDENCE_DROP_CHECKLIST.md` | Project source | Phase 0 and preservation rules | Process source. |
| `Ordinary_A_Level_Maths_Bridge_Spec_Extracts.md` | Project source | Bridge table and prerequisite context | Bridge only. |
| `CCEA_GCE_Mathematics_Specification_Map.md` | Project source | Ordinary AS2/A22 kinematics and A21 calculus background | Bridge only. |
| `FM2-Chp4-Kinematics.pdf` | Lesson-specific PDF | Chapter overview, worked examples, functions of time/displacement/velocity | Cross-board support where CCEA-aligned. The PDF states the chapter is familiar from A-Level Mechanics and Core Pure, but with harder integration techniques. |
| `Chapter_4_Kinematics_🚗_(Further_Mechanics_2)_screenshots.pdf` | Screenshot PDF | Visual annotations, graphs, handwritten algebra | Used only for readable visible details. Parsed text unavailable. |
| `transcripts.md` | Teacher transcript | Teacher explanations, warnings, notation, method choices and worked examples | Major evidence source. It describes kinematics as study of motion involving acceleration, velocity, displacement and time, and says the supplied chapter is very integration heavy. |

## 3. Specification Alignment

| LO ID | Official wording | Lesson coverage | Evidence source | Syllabus boundary | Ordinary A-Level Maths bridge |
|---|---|---|---|---|---|
| `FA22-FKIN-LO001` | solve problems involving kinematics in three dimensions, including use of calculus and \(\mathbf{i}\), \(\mathbf{j}\) and \(\mathbf{k}\) unit vectors | Section 8 includes the componentwise vector calculus method. Section 13 includes generated practice. | CCEA Further Mathematics specification map. Lesson-specific evidence does not supply full worked examples. | Include vector-valued \(\mathbf{r}(t)\), \(\mathbf{v}(t)\), \(\mathbf{a}(t)\), differentiation and integration with constants. | AS1 Vectors, A22 Kinematics, A21 Calculus. |
| `FA22-FKIN-LO002` | solve problems involving variable acceleration along a straight line, where acceleration is given as a function of time, velocity or displacement, including examples involving constant power | Main lesson body. Includes \(a=f(t)\), \(a=f(x)\), \(a=f(v)\), \(v=f(t)\), \(v=f(x)\), definite integration, distance vs displacement, separable DEs, constants of integration and terminal-speed reasoning. | Transcript, screenshots and FM2 PDF. | Include straight-line variable acceleration and method choice. Constant power is included as a boundary note unless worked evidence is supplied. | AS2 Kinematics, A22 Kinematics, A21 Calculus and Differential Equations. |

## 4. Learning Objectives

### Core Further Maths objectives

By the end of this lesson, you should be able to:

1. Use the relationships

\[
v=\frac{dx}{dt}, \qquad a=\frac{dv}{dt}=\frac{d^2x}{dt^2}.
\]

2. Move between displacement, velocity and acceleration using differentiation and integration.

3. Use definite integration to find total change in displacement and velocity:

\[
\Delta x=\int_{t_1}^{t_2}v\,dt,
\qquad
\Delta v=\int_{t_1}^{t_2}a\,dt.
\]

4. Distinguish **displacement** from **distance travelled**, especially when velocity changes sign.

5. Recognise and use the chain-rule form

\[
a=\frac{dv}{dt}
  =\frac{dv}{dx}\frac{dx}{dt}
  =v\frac{dv}{dx}.
\]

6. Recognise and use

\[
v\frac{dv}{dx}
=
\frac{d}{dx}\left(\frac12v^2\right).
\]

7. Choose the right differential equation according to whether the given function depends on \(t\), \(x\), or \(v\).

8. Solve separable differential equations that arise in kinematics.

9. Use \(\mathbf{i}\), \(\mathbf{j}\), and \(\mathbf{k}\) unit vectors to differentiate and integrate vector functions of time in three-dimensional kinematics.

### Bridge objectives

You should connect this lesson to ordinary A-Level Maths by recognising that:

1. AS2 Kinematics gave the language of displacement, velocity, speed and acceleration.
2. A22 Kinematics introduced calculus in motion.
3. A21 Calculus supplied the product rule, chain rule, integration by parts, exponentials, logarithms and separable differential equations.
4. AS1 Vectors and A22 vector kinematics prepare you for the 3D strand of CCEA FKIN.

### Exam technique objectives

You should be able to:

1. Write constants of integration every time an indefinite integral is used.
2. Use initial conditions immediately and clearly.
3. Split integrals at roots of \(v\) when finding distance travelled.
4. State units at the end of mechanics answers.
5. Use exact forms such as \(\dfrac{4}{\pi}\), \(16(1-2e^{-1})\), \(\ln 2\), and \(\arctan\left(\dfrac{U}{k}\right)\) unless a decimal is requested.
6. Avoid treating cross-board examples as CCEA past-paper questions.

## 5. Explicit Prerequisite Recap

### GCSE foundations

You should already be comfortable with:

- substituting values into formulae;
- rearranging equations;
- solving linear and quadratic equations;
- interpreting gradients and areas on graphs;
- using units such as metres, seconds, metres per second and metres per second squared.

### Ordinary AS/A2 Mathematics foundations

| Foundation | Why it matters here |
|---|---|
| AS2 Kinematics | Provides displacement, distance, velocity, speed, acceleration and motion graphs. |
| A22 Kinematics | Provides calculus relationships between \(x\), \(v\), and \(a\). |
| A21 Differentiation | Needed for chain rule, product rule and implicit differentiation ideas. |
| A21 Integration | Needed for definite integrals, integration by parts, exponentials, logs and inverse trig/hyperbolic forms. |
| A21 Differential Equations | Needed for separating variables. |
| AS1 Vectors | Needed for \(\mathbf{i}\), \(\mathbf{j}\), \(\mathbf{k}\) vector kinematics. |

### Previous Further Mathematics foundations

Helpful Further Maths ideas include:

- stronger calculus fluency from FA21 Further calculus;
- differential equations from FA21 Differential equations;
- mechanics modelling assumptions from FAS2/FA22 applied topics.

### A-Level Maths Bridge: What You Already Know and What Further Maths Changes

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| AS2 Kinematics | Position, displacement, distance travelled, velocity, speed and acceleration | Same language, but now with more advanced calculus and differential equations | Signed velocity matters. Distance is not automatically displacement. |
| AS2 Kinematics graphs | Velocity-time graph area gives displacement; gradient gives acceleration | Areas may need splitting because a particle can reverse direction | Negative area must be subtracted when computing distance travelled. |
| A22 Kinematics | \(v=\dfrac{ds}{dt}\), \(a=\dfrac{dv}{dt}=\dfrac{d^2s}{dt^2}\), \(s=\int v\,dt\), \(v=\int a\,dt\) | Adds \(a=f(x)\), \(a=f(v)\), \(v=f(x)\), separable differential equations and chain-rule forms | You cannot blindly integrate with respect to \(t\) when the function is in \(x\) or \(v\). |
| A21 Calculus | Product rule, chain rule, integration by parts and exponentials/logs | These tools now appear inside motion problems | A calculus slip becomes a mechanics error with wrong units. |
| A21 Differential equations | Separating variables and applying initial conditions | Used to convert \(dx/dt=f(x)\), \(dv/dt=f(v)\), and \(v\,dv/dx=f(x)\) into solvable equations | Variables must be separated before integration. |
| AS1 Vectors and A22 vector motion | Vector notation and componentwise calculus in two dimensions | CCEA FKIN requires three-dimensional kinematics using \(\mathbf{i},\mathbf{j},\mathbf{k}\) | The supplied straight-line evidence is not enough for full LO001 coverage. |

In ordinary A-Level Maths, this idea appeared as motion in a straight line, often with constant acceleration or with displacement, velocity and acceleration as functions of time.

In Further Maths, the same idea becomes a calculus control panel: you must decide whether the problem is driven by \(t\), \(x\), or \(v\), then choose the right differential equation.

The key upgrade is the chain-rule link

\[
a=v\frac{dv}{dx},
\]

which lets you handle acceleration as a function of displacement or velocity.

The danger is using the right-looking formula in the wrong variable. That is the mathematical equivalent of steering using the rear-view mirror. Elegant, doomed, and probably not worth the insurance claim.

## 6. Big Picture Explanation

Kinematics is the study of motion. In this topic, the main quantities are:

\[
\text{displacement}, \quad \text{distance}, \quad \text{velocity}, \quad \text{speed}, \quad \text{acceleration}, \quad \text{time}.
\]

The transcript explicitly distinguishes kinematics from dynamics: kinematics studies motion, while dynamics studies forces and how they produce movement. Dynamics therefore builds on kinematics.

In ordinary mechanics, you often saw motion through SUVAT or through direct calculus with time:

\[
v=\frac{dx}{dt}, \qquad a=\frac{dv}{dt}.
\]

In this Further Maths topic, the motion may be described less directly. Acceleration might be given as:

\[
a=f(t), \qquad a=f(x), \qquad a=f(v).
\]

Velocity might also be given as:

\[
v=f(t), \qquad v=f(x).
\]

So the central skill is not just integrating or differentiating. The central skill is **choosing the correct route through the motion maze**.

For straight-line motion:

- if the function is in \(t\), use ordinary time differentiation/integration;
- if the function is in \(x\), use \(v=\dfrac{dx}{dt}\) or \(a=v\dfrac{dv}{dx}\);
- if the function is in \(v\), use \(a=\dfrac{dv}{dt}\) for velocity/time questions and \(a=v\dfrac{dv}{dx}\) for displacement/distance questions.

For three-dimensional kinematics, the same calculus is applied component by component:

\[
\mathbf{r}(t)=x(t)\mathbf{i}+y(t)\mathbf{j}+z(t)\mathbf{k}.
\]

Then

\[
\mathbf{v}(t)=\frac{d\mathbf{r}}{dt},
\qquad
\mathbf{a}(t)=\frac{d\mathbf{v}}{dt}
=\frac{d^2\mathbf{r}}{dt^2}.
\]

This is the same idea, but the particle now moves through 3D space rather than along a single signed line.

## 7. Key Definitions and Notation

### Particle

A **particle** is a body whose size and shape are ignored. Its motion is represented by its position.

### Fixed origin

A fixed point \(O\) is often used as the origin. Displacement from \(O\) is measured along a line or by a position vector.

### Displacement

Displacement is signed position relative to a chosen origin.

For straight-line motion, the evidence uses \(x\), and sometimes \(s\), for displacement:

\[
x=x(t)
\quad \text{or} \quad
s=s(t).
\]

Positive and negative values indicate direction.

### Distance travelled

Distance travelled is the total length of path covered. It is never negative.

If the particle does not change direction, then

\[
\text{distance travelled}=\left|\text{displacement change}\right|.
\]

If the particle changes direction, then distance must be found by splitting the motion into intervals where \(v\) has constant sign.

### Velocity

Velocity is the rate of change of displacement with respect to time:

\[
v=\frac{dx}{dt}.
\]

The transcript also records dot notation:

\[
v=\dot{x}.
\]

Velocity is signed. Positive velocity means motion in the positive direction; negative velocity means motion in the negative direction.

### Speed

Speed is the magnitude of velocity:

\[
\text{speed}=|v|.
\]

Speed is never negative.

### Acceleration

Acceleration is the rate of change of velocity with respect to time:

\[
a=\frac{dv}{dt}.
\]

Since \(v=\dfrac{dx}{dt}\), acceleration can also be written as

\[
a=\frac{d^2x}{dt^2}.
\]

Dot notation gives

\[
a=\ddot{x}.
\]

### Instantaneous rest

A particle is at **instantaneous rest** when

\[
v=0.
\]

This often indicates a possible change in direction, so distance and displacement may separate.

### Maximum displacement

For straight-line motion where \(x=x(t)\), a stationary value of displacement occurs when

\[
\frac{dx}{dt}=0.
\]

Since

\[
\frac{dx}{dt}=v,
\]

a maximum or minimum displacement occurs at a time satisfying

\[
v=0,
\]

with the usual care about whether it is actually a maximum.

### Maximum velocity

For velocity \(v=v(t)\), a stationary value of velocity occurs when

\[
\frac{dv}{dt}=0.
\]

Since

\[
\frac{dv}{dt}=a,
\]

a maximum or minimum velocity occurs at a time satisfying

\[
a=0,
\]

again with the usual care about whether it is actually a maximum.

### Three-dimensional position vector

For 3D kinematics, position is written as

\[
\mathbf{r}(t)=x(t)\mathbf{i}+y(t)\mathbf{j}+z(t)\mathbf{k},
\]

where:

- \(\mathbf{i}\) is the unit vector in the \(x\)-direction;
- \(\mathbf{j}\) is the unit vector in the \(y\)-direction;
- \(\mathbf{k}\) is the unit vector in the \(z\)-direction.

Velocity and acceleration are then:

\[
\mathbf{v}(t)=\frac{d\mathbf{r}}{dt},
\]

\[
\mathbf{a}(t)=\frac{d\mathbf{v}}{dt}
=\frac{d^2\mathbf{r}}{dt^2}.
\]

## 8. Core Theory

### 8.1 The straight-line kinematics ladder

For straight-line motion, the main ladder is:

\[
x \longrightarrow v \longrightarrow a.
\]

Going down the ladder means differentiating with respect to time:

\[
v=\frac{dx}{dt},
\]

\[
a=\frac{dv}{dt}.
\]

So

\[
a=\frac{d}{dt}\left(\frac{dx}{dt}\right)
=\frac{d^2x}{dt^2}.
\]

Going up the ladder means integrating with respect to time:

\[
v=\int a\,dt,
\]

\[
x=\int v\,dt.
\]

If starting from acceleration and going all the way to displacement:

\[
x=\iint a\,dt\,dt.
\]

Each indefinite integration produces a constant. Therefore:

- one integration gives one constant;
- double integration gives two independent constants.

**Bridge Note:** In ordinary A-Level Maths, you used \(v=\dfrac{ds}{dt}\) and \(a=\dfrac{dv}{dt}\). Here, Further Maths keeps that ladder but uses harder functions and differential equations.

### 8.2 Definite integrals and total change

If \(v=v(t)\), then the total change in displacement from \(t=t_1\) to \(t=t_2\) is

\[
\Delta x=\int_{t_1}^{t_2}v(t)\,dt.
\]

If \(a=a(t)\), then the total change in velocity from \(t=t_1\) to \(t=t_2\) is

\[
\Delta v=\int_{t_1}^{t_2}a(t)\,dt.
\]

This is area-under-the-graph thinking, but now the graph is wearing calculus boots.

### 8.3 Distance travelled versus displacement

Displacement is signed:

\[
\Delta x=\int_{t_1}^{t_2}v(t)\,dt.
\]

Distance travelled uses magnitude:

\[
\text{distance travelled}
=
\int_{t_1}^{t_2}|v(t)|\,dt.
\]

In exam work, this usually means:

1. Find when \(v(t)=0\).
2. Split the interval at those times.
3. Integrate \(v(t)\) over each interval.
4. Take the magnitude of each signed area.
5. Add the magnitudes.

For example, if a velocity-time graph is positive on \([0,2]\), negative on \([2,5]\), and positive on \([5,6]\), then

\[
\text{distance}
=
\int_0^2 v\,dt
-
\int_2^5 v\,dt
+
\int_5^6 v\,dt.
\]

The middle integral is subtracted because it is negative area. Subtracting the negative area adds its magnitude.

**Bridge Note:** Ordinary AS2 Kinematics taught that area under a velocity-time graph gives displacement. Further Maths makes you police the sign of the area.

### 8.4 Function of time: \(a=f(t)\)

If acceleration is given as a function of time,

\[
a=f(t),
\]

then

\[
\frac{dv}{dt}=f(t).
\]

Multiply by \(dt\):

\[
dv=f(t)\,dt.
\]

Integrate:

\[
\int 1\,dv=\int f(t)\,dt.
\]

So

\[
v=\int f(t)\,dt+C.
\]

Then use an initial condition, such as \(v=v_0\) when \(t=0\), to find \(C\).

If displacement is needed, use

\[
\frac{dx}{dt}=v(t),
\]

so

\[
dx=v(t)\,dt,
\]

and therefore

\[
x=\int v(t)\,dt+C.
\]

Again, use an initial condition, such as \(x=0\) when \(t=0\), to find \(C\).

### 8.5 Function of time: \(v=f(t)\)

If velocity is given as a function of time,

\[
v=f(t),
\]

then acceleration is found by differentiating:

\[
a=\frac{dv}{dt}
=\frac{d}{dt}\left(f(t)\right).
\]

Displacement is found by integrating:

\[
x=\int v\,dt
=\int f(t)\,dt+C.
\]

### 8.6 Maximum displacement and maximum velocity

If \(x=x(t)\), then a maximum or minimum displacement occurs when

\[
\frac{dx}{dt}=0.
\]

Since

\[
\frac{dx}{dt}=v,
\]

solve

\[
v=0.
\]

If \(v=v(t)\), then a maximum or minimum velocity occurs when

\[
\frac{dv}{dt}=0.
\]

Since

\[
\frac{dv}{dt}=a,
\]

solve

\[
a=0.
\]

Do not simply solve \(v=0\) and declare victory. Check context, direction, interval and whether the point is actually a maximum.

### 8.7 Why \(a=v\dfrac{dv}{dx}\)

When acceleration is written as a function of displacement, using

\[
a=\frac{dv}{dt}
\]

is not enough by itself, because the right-hand side may involve \(x\), not \(t\).

Use the chain rule:

\[
a=\frac{dv}{dt}.
\]

Insert \(x\) as the intermediate variable:

\[
\frac{dv}{dt}
=
\frac{dv}{dx}\frac{dx}{dt}.
\]

But

\[
\frac{dx}{dt}=v.
\]

Therefore

\[
a
=
\frac{dv}{dx}\cdot v
=
v\frac{dv}{dx}.
\]

So the key formula is

\[
\boxed{a=v\frac{dv}{dx}}.
\]

**Bridge Note:** In A21 calculus, the chain rule linked rates through an intermediate variable. Here, the intermediate variable is displacement \(x\), and the result becomes a mechanics formula.

### 8.8 Why \(v\dfrac{dv}{dx}=\dfrac{d}{dx}\left(\frac12v^2\right)\)

Start with:

\[
\frac{d}{dx}\left(\frac12v^2\right).
\]

Since \(v\) depends on \(x\), use the chain rule:

\[
\frac{d}{dx}\left(\frac12v^2\right)
=
\frac12\cdot 2v\frac{dv}{dx}.
\]

Simplify:

\[
\frac{d}{dx}\left(\frac12v^2\right)
=
v\frac{dv}{dx}.
\]

Therefore

\[
\boxed{
v\frac{dv}{dx}
=
\frac{d}{dx}\left(\frac12v^2\right)
}.
\]

This is why, when

\[
a=f(x),
\]

we can write

\[
\frac{d}{dx}\left(\frac12v^2\right)=f(x).
\]

Integrating with respect to \(x\):

\[
\frac12v^2=\int f(x)\,dx+C.
\]

Then use an initial condition to find \(C\).

### 8.9 Function of displacement: \(a=f(x)\)

If acceleration is given as a function of displacement,

\[
a=f(x),
\]

then use

\[
a=v\frac{dv}{dx}.
\]

So

\[
v\frac{dv}{dx}=f(x).
\]

Separate variables:

\[
v\,dv=f(x)\,dx.
\]

Integrate both sides:

\[
\int v\,dv=\int f(x)\,dx.
\]

So

\[
\frac12v^2=\int f(x)\,dx+C.
\]

Then solve for \(v\), applying direction information carefully. If the particle is moving in the direction of increasing \(x\), choose the positive square root. If it is moving in the direction of decreasing \(x\), choose the negative square root.

### 8.10 Function of displacement: \(v=f(x)\)

If velocity is given as a function of displacement,

\[
v=f(x),
\]

then use

\[
v=\frac{dx}{dt}.
\]

So

\[
\frac{dx}{dt}=f(x).
\]

Separate variables:

\[
\frac{1}{f(x)}\,dx=dt.
\]

Integrate:

\[
\int \frac{1}{f(x)}\,dx=\int 1\,dt.
\]

So

\[
\int \frac{1}{f(x)}\,dx=t+C.
\]

Use the initial condition to find \(C\), then solve for \(x\) in terms of \(t\) if required.

### 8.11 Function of velocity: \(a=f(v)\)

If acceleration is given as a function of velocity,

\[
a=f(v),
\]

then choose your route based on the question.

#### If the question asks about velocity or time

Use

\[
a=\frac{dv}{dt}.
\]

So

\[
\frac{dv}{dt}=f(v).
\]

Separate variables:

\[
\frac{1}{f(v)}\,dv=dt.
\]

Integrate:

\[
\int \frac{1}{f(v)}\,dv=\int 1\,dt.
\]

Therefore

\[
\int \frac{1}{f(v)}\,dv=t+C.
\]

#### If the question asks about displacement or distance

Use

\[
a=v\frac{dv}{dx}.
\]

So

\[
v\frac{dv}{dx}=f(v).
\]

Separate variables:

\[
\frac{v}{f(v)}\,dv=dx.
\]

Integrate:

\[
\int \frac{v}{f(v)}\,dv=\int 1\,dx.
\]

Therefore

\[
\int \frac{v}{f(v)}\,dv=x+C.
\]

### 8.12 Constant power boundary note

The CCEA FKIN LO explicitly includes examples involving constant power.

Power is linked to force and velocity by

\[
P=Fv.
\]

If a vehicle has constant power \(P\), then the driving force may be modelled as

\[
F=\frac{P}{v}.
\]

When combined with resistance, Newton’s second law can lead to an acceleration involving \(v\), for example

\[
a=f(v).
\]

That is why constant power belongs naturally with the function-of-velocity method.

This lesson includes the method boundary, but no full evidence-backed constant-power worked example is claimed because the supplied evidence only gives a modelling mention, not a complete constant-power worked solution.

### 8.13 Three-dimensional kinematics with \(\mathbf{i}\), \(\mathbf{j}\), \(\mathbf{k}\)

This is required by CCEA `FA22-FKIN-LO001`.

A particle moving in three dimensions has position vector

\[
\mathbf{r}(t)=x(t)\mathbf{i}+y(t)\mathbf{j}+z(t)\mathbf{k}.
\]

Differentiate component by component to get velocity:

\[
\mathbf{v}(t)
=
\frac{d\mathbf{r}}{dt}
=
\frac{dx}{dt}\mathbf{i}
+
\frac{dy}{dt}\mathbf{j}
+
\frac{dz}{dt}\mathbf{k}.
\]

Differentiate again to get acceleration:

\[
\mathbf{a}(t)
=
\frac{d\mathbf{v}}{dt}
=
\frac{d^2x}{dt^2}\mathbf{i}
+
\frac{d^2y}{dt^2}\mathbf{j}
+
\frac{d^2z}{dt^2}\mathbf{k}.
\]

If acceleration is given and velocity is needed, integrate each component:

\[
\mathbf{v}(t)=\int \mathbf{a}(t)\,dt.
\]

This means

\[
\mathbf{v}(t)
=
\left(\int a_x(t)\,dt\right)\mathbf{i}
+
\left(\int a_y(t)\,dt\right)\mathbf{j}
+
\left(\int a_z(t)\,dt\right)\mathbf{k}
+
\mathbf{C},
\]

where

\[
\mathbf{C}=C_1\mathbf{i}+C_2\mathbf{j}+C_3\mathbf{k}
\]

is a constant vector.

If position is needed, integrate velocity:

\[
\mathbf{r}(t)=\int \mathbf{v}(t)\,dt.
\]

Again, the constant of integration is a vector.

**Evidence warning:** The supplied lesson-specific transcript says this chapter evidence concerns moving in a straight line with no vectors. That is useful for LO002, but it does not remove CCEA’s LO001 requirement. This 3D vector section is therefore included from the CCEA specification boundary, with no claim that the supplied FM2 transcript gives full 3D worked examples.

### 8.14 Method choice summary

| Given information | Need | Use |
|---|---|---|
| \(a=f(t)\) | \(v\) | \(\dfrac{dv}{dt}=f(t)\), integrate with respect to \(t\). |
| \(v=f(t)\) | \(a\) | \(a=\dfrac{dv}{dt}\). |
| \(v=f(t)\) | \(x\) | \(x=\int v(t)\,dt+C\). |
| \(a=f(x)\) | \(v\) | \(a=v\dfrac{dv}{dx}\). |
| \(v=f(x)\) | \(x(t)\) | \(\dfrac{dx}{dt}=f(x)\), separate variables. |
| \(a=f(v)\) | \(v(t)\) or time | \(a=\dfrac{dv}{dt}\), separate variables. |
| \(a=f(v)\) | \(x\) or distance | \(a=v\dfrac{dv}{dx}\), separate variables. |
| \(\mathbf{a}(t)\) in 3D | \(\mathbf{v}(t)\), \(\mathbf{r}(t)\) | Integrate componentwise and use vector constants. |
| \(\mathbf{r}(t)\) in 3D | \(\mathbf{v}(t)\), \(\mathbf{a}(t)\) | Differentiate componentwise. |

## 9. Visual Asset Integration

[VISUAL PLACEHOLDER: FA22FurtherKinematicsMermaid-001 | Source: CCEA FA22-FKIN boundary + transcript summary slide | Insert from mermaid/FA22FurtherKinematicsMermaid-001.md | Purpose: Show how to choose the correct kinematics equation depending on whether the given function involves \(t\), \(x\), or \(v\).]

[VISUAL PLACEHOLDER: FA22FurtherKinematicsMermaid-002 | Source: CCEA Further Mathematics specification map | Insert from mermaid/FA22FurtherKinematicsMermaid-002.md | Purpose: Separate the two CCEA FKIN learning outcomes and show which parts of the lesson support each one.]

[VISUAL PLACEHOLDER: FA22FurtherKinematicsSVG-001 | Source: Transcript notation recap and screenshot evidence | Insert from svg/FA22FurtherKinematicsSVG-001.svg | Purpose: Show a particle \(P\) moving on a straight line from a fixed origin \(O\), with positive \(x\), velocity \(v\), and acceleration \(a\).]

[VISUAL PLACEHOLDER: FA22FurtherKinematicsSVG-002 | Source: Screenshot PDF velocity-time graph + transcript warning about negative areas | Insert from svg/FA22FurtherKinematicsSVG-002.svg | Purpose: Show why distance travelled requires splitting intervals when the velocity-time graph crosses the axis.]

[VISUAL PLACEHOLDER: FA22FurtherKinematicsSVG-003 | Source: FM2 PDF page 5 adapted textbook example | Insert from svg/FA22FurtherKinematicsSVG-003.svg | Purpose: Show a piecewise velocity function, instantaneous rest at \(t=0.5\) and \(t=3\), and the split into areas \(A\), \(B\), and \(C\).]

[VISUAL PLACEHOLDER: FA22FurtherKinematicsBridgeSVG-001 | Source: Ordinary A-Level Maths bridge + CCEA Further Mathematics specification | Insert from svg/FA22FurtherKinematicsBridgeSVG-001.svg | Purpose: Compare prior ordinary Maths method with Further Maths extension.]

[VISUAL PLACEHOLDER: FA22FurtherKinematicsTikZ-001 | Source: Transcript notation recap | Insert from tikz/FA22FurtherKinematicsTikZ-001.tex | Purpose: Give a precise typeset diagram of the \(x\), \(v\), \(a\) ladder.]

[VISUAL PLACEHOLDER: FA22FurtherKinematicsTikZ-002 | Source: Transcript derivation of acceleration as a function of displacement | Insert from tikz/FA22FurtherKinematicsTikZ-002.tex | Purpose: Show the chain-rule derivation of \(a=v\dfrac{dv}{dx}\).]

[VISUAL PLACEHOLDER: FA22FurtherKinematicsTikZ-003 | Source: CCEA FA22-FKIN-LO001 | Insert from tikz/FA22FurtherKinematicsTikZ-003.tex | Purpose: Show 3D position, velocity and acceleration vectors using \(\mathbf{i}\), \(\mathbf{j}\), and \(\mathbf{k}\).]

## 10. Interactive Learning Widgets

[INTERACTIVE PLACEHOLDER: FA22FurtherKinematicsWidget-001 | Source: AI-proposed teaching enhancement based on CCEA FKIN + transcript method summary | Insert from widgets/FA22FurtherKinematicsWidget-001.html | Purpose: Help the student choose the correct kinematics equation from the variable given and the variable required.]

This widget asks what is given and what is needed, then recommends the correct relationship such as \(a=\dfrac{dv}{dt}\), \(a=v\dfrac{dv}{dx}\), or componentwise vector calculus. It checks errors such as integrating \(f(x)\) with respect to \(t\), forgetting vector constants, and confusing distance with displacement.

[INTERACTIVE PLACEHOLDER: FA22FurtherKinematicsWidget-002 | Source: AI-proposed teaching enhancement based on transcript warning about negative areas | Insert from widgets/FA22FurtherKinematicsWidget-002.html | Purpose: Let students enter roots of \(v(t)\) and build the correct distance integral.]

This widget asks for interval endpoints, roots of \(v(t)\), and the sign of velocity on the first interval. It displays the displacement integral, the distance integral, and the interval-by-interval sign logic.

[INTERACTIVE PLACEHOLDER: FA22FurtherKinematicsWidget-003 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FA22FurtherKinematicsWidget-003.html | Purpose: Practise rearranging differential equations before integration.]

This widget shows setup, separated form, integral setup, result after integration, and a common wrong move for cases such as \(dx/dt=2x\), \(v\,dv/dx=2x\), and \(dv/dt=12-3v\).

## 11. Worked Examples

### Worked Example 1: Velocity \(v=4\sin(2\pi t)\), acceleration and greatest distance from \(O\)

**Evidence source:** Teacher transcript and screenshot evidence.  
**On-spec status:** On-spec for `FA22-FKIN-LO002`, variable acceleration along a straight line where velocity is a function of time.  
**Ordinary Maths idea used:** Differentiate velocity to acceleration; integrate velocity to displacement.  
**Further Maths upgrade:** Trigonometric calculus, exact value reasoning and maximum displacement reasoning.

#### Question

A particle is moving in a straight line with velocity at time \(t\) seconds given by

\[
v=4\sin(2\pi t)\ \text{m s}^{-1},
\qquad t\geq 0.
\]

The particle is at \(O\) at time \(t=0\). Find:

1. the magnitude of the acceleration when \(t=\frac23\);
2. the greatest distance from \(O\) attained by the particle during the motion.

#### Part (a): Magnitude of acceleration

\[
v=4\sin(2\pi t).
\]

Acceleration is

\[
a=\frac{dv}{dt}.
\]

Differentiate using the chain rule:

\[
a=\frac{d}{dt}\left(4\sin(2\pi t)\right).
\]

The derivative of \(\sin(2\pi t)\) is

\[
2\pi\cos(2\pi t).
\]

Therefore

\[
a=4\cdot 2\pi\cos(2\pi t)=8\pi\cos(2\pi t).
\]

When \(t=\frac23\),

\[
a=8\pi\cos\left(2\pi\cdot \frac23\right)
=8\pi\cos\left(\frac{4\pi}{3}\right).
\]

Since

\[
\cos\left(\frac{4\pi}{3}\right)=-\frac12,
\]

we get

\[
a=8\pi\left(-\frac12\right)=-4\pi.
\]

The magnitude is

\[
|a|=|-4\pi|=4\pi.
\]

\[
\boxed{4\pi\ \text{m s}^{-2}}.
\]

#### Part (b): Greatest distance from \(O\)

We need displacement \(x\), and

\[
v=\frac{dx}{dt}.
\]

So

\[
x=\int v\,dt.
\]

Substitute the velocity:

\[
x=\int 4\sin(2\pi t)\,dt.
\]

Integrate:

\[
x=-\frac{4}{2\pi}\cos(2\pi t)+C
=-\frac{2}{\pi}\cos(2\pi t)+C.
\]

Use \(t=0, x=0\):

\[
0=-\frac{2}{\pi}\cos(0)+C.
\]

Since \(\cos(0)=1\),

\[
0=-\frac{2}{\pi}+C,
\]

so

\[
C=\frac{2}{\pi}.
\]

Hence

\[
x=\frac{2}{\pi}-\frac{2}{\pi}\cos(2\pi t).
\]

To maximise \(x\), use the minimum value of cosine:

\[
\cos(2\pi t)=-1.
\]

Then

\[
x_{\max}=\frac{2}{\pi}-\frac{2}{\pi}(-1)
=\frac{4}{\pi}.
\]

\[
\boxed{\frac{4}{\pi}\ \text{m}}.
\]

**Teaching note:** This example is a neat little clockwork beetle: differentiate once for acceleration, integrate once for displacement, then use the range of cosine rather than doing extra unnecessary calculus.

### Worked Example 2: Velocity \(v=te^{-t/4}\), distance from \(O\) when \(a=0\)

**Evidence source:** Teacher transcript and screenshot evidence.  
**On-spec status:** On-spec for `FA22-FKIN-LO002`, straight-line variable acceleration with velocity as a function of time.  
**Ordinary Maths idea used:** Product rule and integration by parts.  
**Further Maths upgrade:** Mixed differentiation and integration in one mechanics problem.

#### Question

A particle \(P\) is moving along the \(x\)-axis. Initially \(P\) is at the origin \(O\). At time \(t\) seconds, where \(t\geq 0\), the velocity is

\[
v=te^{-t/4}\ \text{m s}^{-1}.
\]

Find the distance of \(P\) from \(O\) when the acceleration of \(P\) is zero.

#### Step 1: Record the initial condition

Initially \(P\) is at the origin, so

\[
t=0,
\qquad
x=0.
\]

#### Step 2: Find acceleration

Acceleration is

\[
a=\frac{dv}{dt}.
\]

Given

\[
v=te^{-t/4}.
\]

Use the product rule. Let

\[
u=t,
\qquad
w=e^{-t/4}.
\]

Then

\[
u'=1,
\qquad
w'=-\frac14e^{-t/4}.
\]

Therefore

\[
a=1\cdot e^{-t/4}+t\left(-\frac14e^{-t/4}\right)
=e^{-t/4}-\frac14te^{-t/4}.
\]

Write this as

\[
a=-\frac14te^{-t/4}+e^{-t/4}.
\]

#### Step 3: Set acceleration equal to zero

\[
0=-\frac14te^{-t/4}+e^{-t/4}.
\]

Factorise:

\[
0=e^{-t/4}\left(-\frac14t+1\right).
\]

Since \(e^{-t/4}\neq 0\),

\[
-\frac14t+1=0.
\]

So

\[
1=\frac14t,
\]

and hence

\[
t=4.
\]

#### Step 4: Find \(x\) by integrating \(v\)

Since

\[
v=\frac{dx}{dt},
\]

we have

\[
x=\int v\,dt=\int te^{-t/4}\,dt.
\]

Use integration by parts. Let

\[
u=t,
\qquad
dv=e^{-t/4}\,dt.
\]

Then

\[
du=dt,
\qquad
v_{\text{parts}}=\int e^{-t/4}\,dt=-4e^{-t/4}.
\]

Using

\[
\int u\,dv=uv-\int v\,du,
\]

we get

\[
\int te^{-t/4}\,dt
=t(-4e^{-t/4})-
\int(-4e^{-t/4})\,dt.
\]

So

\[
x=-4te^{-t/4}+4\int e^{-t/4}\,dt.
\]

Now

\[
\int e^{-t/4}\,dt=-4e^{-t/4}.
\]

Therefore

\[
x=-4te^{-t/4}-16e^{-t/4}+C.
\]

Use \(t=0,x=0\):

\[
0=-4(0)e^0-16e^0+C=-16+C.
\]

So

\[
C=16.
\]

Hence

\[
x=-4te^{-t/4}-16e^{-t/4}+16.
\]

#### Step 5: Substitute \(t=4\)

\[
x=-4(4)e^{-4/4}-16e^{-4/4}+16.
\]

So

\[
x=-16e^{-1}-16e^{-1}+16=16-32e^{-1}.
\]

Factorise:

\[
x=16(1-2e^{-1}).
\]

\[
\boxed{16(1-2e^{-1})\ \text{m}}.
\]

**Teaching note:** The two halves of the problem are independent gears: \(a=0\) tells you when to evaluate; integration of \(v\) tells you what the displacement is at that time.

### Worked Example 3: Acceleration \(a=4e^{-0.5t}\), velocity cannot exceed \(10\)

**Evidence source:** Teacher transcript “Your Turn” solution.  
**On-spec status:** On-spec for `FA22-FKIN-LO002`, straight-line variable acceleration with \(a=f(t)\).  
**Ordinary Maths idea used:** Integrate acceleration to velocity.  
**Further Maths upgrade:** Use exponential behaviour to prove a limiting speed.

#### Question

A particle \(P\) is moving along the \(x\)-axis. Initially \(P\) is at the origin and moving with speed \(2\ \text{m s}^{-1}\) in the direction of \(Ox\). At time \(t\) seconds, where \(t\geq 0\), the acceleration of \(P\) is

\[
a=4e^{-0.5t}\ \text{m s}^{-2}
\]

directed away from \(O\).

1. Find the velocity of \(P\) at time \(t\).
2. Show that the speed of \(P\) cannot exceed \(10\ \text{m s}^{-1}\).
3. Sketch a velocity-time graph to illustrate the motion.

#### Part (a): Find velocity

Since

\[
a=\frac{dv}{dt},
\]

we have

\[
v=\int a\,dt.
\]

Substitute \(a=4e^{-0.5t}\):

\[
v=\int 4e^{-0.5t}\,dt.
\]

The integral of \(e^{-0.5t}\) is

\[
\frac{1}{-0.5}e^{-0.5t}=-2e^{-0.5t}.
\]

Therefore

\[
v=4(-2e^{-0.5t})+C=-8e^{-0.5t}+C.
\]

Use \(t=0, v=2\):

\[
2=-8e^0+C=-8+C.
\]

So

\[
C=10.
\]

Therefore

\[
\boxed{v=10-8e^{-0.5t}\ \text{m s}^{-1}}.
\]

#### Part (b): Show speed cannot exceed \(10\)

For all real \(t\),

\[
e^{-0.5t}>0.
\]

Therefore

\[
-8e^{-0.5t}<0.
\]

Add \(10\):

\[
10-8e^{-0.5t}<10.
\]

But

\[
v=10-8e^{-0.5t}.
\]

Hence

\[
v<10.
\]

So the speed cannot exceed

\[
\boxed{10\ \text{m s}^{-1}}.
\]

#### Part (c): Sketch description

The graph of

\[
v=10-8e^{-0.5t}
\]

has:

- initial value:

\[
v(0)=10-8=2;
\]

- horizontal asymptote:

\[
v=10;
\]

- increasing curve approaching \(10\) from below.

**Teaching note:** The exponential term shrinks but never becomes zero, so the particle approaches \(10\ \text{m s}^{-1}\) but never reaches or exceeds it.

### Worked Example 4: Acceleration \(a=\cos(2\pi t)\), maximum speed and distance

**Evidence source:** FM2 PDF page 4.  
**On-spec status:** On-spec for `FA22-FKIN-LO002`, acceleration as a function of time.  
**Ordinary Maths idea used:** Integrate acceleration to velocity; integrate velocity to displacement/distance.  
**Further Maths upgrade:** Constants of integration and trigonometric integration in a mechanics setting.

#### Question

A particle is moving in a straight line with acceleration at time \(t\) seconds given by

\[
a=\cos(2\pi t)\ \text{m s}^{-2},
\qquad t\geq 0.
\]

The velocity of the particle at time \(t=0\) is

\[
\frac{1}{2\pi}\ \text{m s}^{-1}.
\]

Find:

1. an expression for the velocity at time \(t\) seconds;
2. the maximum speed;
3. the distance travelled in the first \(3\) seconds.

#### Part (a): Find \(v(t)\)

Since

\[
a=\frac{dv}{dt},
\]

we have

\[
v=\int a\,dt=\int \cos(2\pi t)\,dt.
\]

Integrate:

\[
v=\frac{1}{2\pi}\sin(2\pi t)+C.
\]

Use \(t=0\), \(v=\dfrac{1}{2\pi}\):

\[
\frac{1}{2\pi}=\frac{1}{2\pi}\sin(0)+C.
\]

Since \(\sin(0)=0\),

\[
C=\frac{1}{2\pi}.
\]

Therefore

\[
\boxed{v=\frac{1}{2\pi}\sin(2\pi t)+\frac{1}{2\pi}}.
\]

#### Part (b): Maximum speed

\[
v=\frac{1}{2\pi}\sin(2\pi t)+\frac{1}{2\pi}.
\]

The maximum value of \(\sin(2\pi t)\) is \(1\), so

\[
v_{\max}=\frac{1}{2\pi}+\frac{1}{2\pi}=\frac{1}{\pi}.
\]

Since this velocity is non-negative throughout, maximum speed equals maximum velocity.

\[
\boxed{\frac{1}{\pi}\ \text{m s}^{-1}}.
\]

#### Part (c): Distance travelled in the first \(3\) seconds

Since \(v\) is always positive, distance travelled equals displacement:

\[
s=\int_0^3 v\,dt.
\]

So

\[
s=\int_0^3\left(\frac{1}{2\pi}\sin(2\pi t)+\frac{1}{2\pi}\right)dt.
\]

Factor:

\[
s=\frac{1}{2\pi}\int_0^3(\sin(2\pi t)+1)\,dt.
\]

Integrate:

\[
s=\frac{1}{2\pi}\left[-\frac{1}{2\pi}\cos(2\pi t)+t\right]_0^3.
\]

At \(t=3\):

\[
-\frac{1}{2\pi}\cos(6\pi)+3=-\frac{1}{2\pi}+3.
\]

At \(t=0\):

\[
-\frac{1}{2\pi}\cos(0)+0=-\frac{1}{2\pi}.
\]

Therefore

\[
s=\frac{1}{2\pi}\left[\left(-\frac{1}{2\pi}+3\right)-\left(-\frac{1}{2\pi}\right)\right]
=\frac{1}{2\pi}\cdot 3.
\]

So

\[
s=\frac{3}{2\pi}=0.477\ldots
\]

\[
\boxed{\frac{3}{2\pi}\ \text{m}}\qquad \text{or}\qquad \boxed{0.477\ \text{m to 3 s.f.}}.
\]

### Worked Example 5: Piecewise velocity, instantaneous rest, displacement and total distance

**Evidence source:** FM2 PDF page 5.  
**On-spec status:** On-spec for `FA22-FKIN-LO002`, velocity as a function of time and distance versus displacement.  
**Ordinary Maths idea used:** Definite integration of a velocity-time graph.  
**Further Maths upgrade:** Piecewise function and signed area splitting.

#### Question

A particle \(P\) moves on the positive \(x\)-axis. The velocity, \(v\ \text{m s}^{-1}\), of \(P\) at time \(t\) seconds is

\[
v=
\begin{cases}
2t^2-7t+3, & 0\leq t\leq 3,\\
5t-15, & 3<t\leq 5.
\end{cases}
\]

When \(t=0\), \(P\) is \(10\ \text{m}\) from the origin \(O\).

Find:

1. the values of \(t\) when \(P\) is at instantaneous rest;
2. the displacement of \(P\) from \(O\) when \(t=5\);
3. the total distance travelled by \(P\) when \(t=5\).

#### Part (a): Instantaneous rest

Instantaneous rest means

\[
v=0.
\]

For \(0\leq t\leq 3\), solve

\[
2t^2-7t+3=0.
\]

Factorise:

\[
2t^2-7t+3=(2t-1)(t-3).
\]

So

\[
(2t-1)(t-3)=0.
\]

Hence

\[
t=\frac12
\quad \text{or} \quad
t=3.
\]

For \(3<t\leq 5\), solve

\[
5t-15=0.
\]

Then

\[
t=3,
\]

already found at the join.

Therefore

\[
\boxed{t=0.5\ \text{s} \quad \text{and} \quad t=3\ \text{s}}.
\]

#### Part (b): Displacement from \(O\) when \(t=5\)

The change in displacement from \(t=0\) to \(t=5\) is

\[
\int_0^3 (2t^2-7t+3)\,dt
+
\int_3^5 (5t-15)\,dt.
\]

First integral:

\[
\int_0^3 (2t^2-7t+3)\,dt
=
\left[\frac{2}{3}t^3-\frac{7}{2}t^2+3t\right]_0^3.
\]

At \(t=3\):

\[
\frac{2}{3}(3)^3-\frac{7}{2}(3)^2+3(3)
=18-\frac{63}{2}+9.
\]

Now \(18+9=27=\dfrac{54}{2}\), so

\[
18-\frac{63}{2}+9=\frac{54}{2}-\frac{63}{2}=-\frac92.
\]

Thus

\[
\int_0^3 (2t^2-7t+3)\,dt=-\frac92.
\]

Second integral:

\[
\int_3^5(5t-15)\,dt
=
\left[\frac52t^2-15t\right]_3^5.
\]

At \(t=5\):

\[
\frac52(25)-15(5)=\frac{125}{2}-75=-\frac{25}{2}.
\]

At \(t=3\):

\[
\frac52(9)-15(3)=\frac{45}{2}-45=-\frac{45}{2}.
\]

Therefore

\[
\int_3^5(5t-15)\,dt=-\frac{25}{2}-\left(-\frac{45}{2}\right)=10.
\]

So the total change in displacement is

\[
-\frac92+10=\frac{11}{2}.
\]

The particle was initially \(10\ \text{m}\) from \(O\), so its displacement from \(O\) when \(t=5\) is

\[
10+\frac{11}{2}=\frac{31}{2}=15.5.
\]

\[
\boxed{\frac{31}{2}\ \text{m}}\quad \text{or}\quad \boxed{15.5\ \text{m}}.
\]

#### Part (c): Total distance travelled by \(t=5\)

Distance must be found by splitting at the zeros of \(v\):

\[
t=0.5,
\qquad
t=3.
\]

On \([0,0.5]\), \(v>0\).  
On \([0.5,3]\), \(v<0\).  
On \([3,5]\), \(v>0\).

Therefore

\[
\text{distance}
=
\int_0^{0.5}(2t^2-7t+3)\,dt
-
\int_{0.5}^3(2t^2-7t+3)\,dt
+
\int_3^5(5t-15)\,dt.
\]

Let

\[
F(t)=\frac{2}{3}t^3-\frac{7}{2}t^2+3t.
\]

First area:

\[
F\left(\frac12\right)-F(0).
\]

Now

\[
F\left(\frac12\right)
=
\frac{2}{3}\left(\frac18\right)
-
\frac72\left(\frac14\right)
+
3\left(\frac12\right).
\]

Calculate term by term:

\[
\frac{2}{3}\cdot\frac18=\frac{1}{12},
\]

\[
\frac72\cdot\frac14=\frac78,
\]

\[
3\cdot\frac12=\frac32.
\]

So

\[
F\left(\frac12\right)=\frac{1}{12}-\frac78+\frac32.
\]

Using denominator \(24\):

\[
\frac{1}{12}=\frac{2}{24},
\qquad
-\frac78=-\frac{21}{24},
\qquad
\frac32=\frac{36}{24}.
\]

Therefore

\[
F\left(\frac12\right)=\frac{2-21+36}{24}=\frac{17}{24}.
\]

So

\[
A=\frac{17}{24}.
\]

Second signed integral:

\[
\int_{0.5}^{3}(2t^2-7t+3)\,dt
=F(3)-F\left(\frac12\right).
\]

We already found \(F(3)=-\dfrac92\). So

\[
F(3)-F\left(\frac12\right)
=-\frac92-\frac{17}{24}.
\]

Convert:

\[
-\frac92=-\frac{108}{24}.
\]

So

\[
-\frac{108}{24}-\frac{17}{24}=-\frac{125}{24}.
\]

The magnitude is

\[
\frac{125}{24}.
\]

Third area:

\[
\int_3^5(5t-15)\,dt=10.
\]

Therefore total distance is

\[
\frac{17}{24}+\frac{125}{24}+10
=\frac{142}{24}+10
=\frac{71}{12}+\frac{120}{12}
=\frac{191}{12}.
\]

\[
\boxed{\frac{191}{12}\ \text{m}}.
\]

### Worked Example 6: Velocity as a function of displacement, \(v=2x\)

**Evidence source:** Teacher transcript, functions of displacement introduction.  
**On-spec status:** On-spec for `FA22-FKIN-LO002`, straight-line motion where velocity is a function of displacement.  
**Ordinary Maths idea used:** \(v=\dfrac{dx}{dt}\).  
**Further Maths upgrade:** Separate variables before integrating.

#### Question

Given

\[
v=2x,
\]

find \(x\) as a function of \(t\), given that

\[
x=1
\quad \text{when} \quad
t=0.
\]

#### Solution

Since

\[
v=\frac{dx}{dt},
\]

the equation becomes

\[
\frac{dx}{dt}=2x.
\]

Separate variables:

\[
\frac{1}{x}\,dx=2\,dt.
\]

Integrate:

\[
\int \frac{1}{x}\,dx=\int 2\,dt.
\]

So

\[
\ln x=2t+C.
\]

Use \(t=0,x=1\):

\[
\ln 1=2(0)+C.
\]

Since \(\ln 1=0\), \(C=0\). Therefore

\[
\ln x=2t.
\]

Exponentiate:

\[
\boxed{x=e^{2t}}.
\]

### Worked Example 7: Acceleration as a function of displacement, \(a=-\frac12e^{-x}\)

**Evidence source:** Teacher transcript, functions of displacement.  
**On-spec status:** On-spec for `FA22-FKIN-LO002`, acceleration as a function of displacement.  
**Ordinary Maths idea used:** Direction along the \(x\)-axis and \(v=\dfrac{dx}{dt}\).  
**Further Maths upgrade:** Use \(a=v\dfrac{dv}{dx}\), then separate variables.

#### Question

A particle \(P\) is moving along the \(x\)-axis. Initially \(P\) is at the origin and is moving with velocity \(1\ \text{m s}^{-1}\) in the direction of increasing \(x\).

At time \(t\) seconds, \(P\) is \(x\) metres from \(O\), has velocity \(v\ \text{m s}^{-1}\), and has acceleration of magnitude

\[
\frac12e^{-x}\ \text{m s}^{-2}
\]

directed towards \(O\).

Find:

1. \(v\) in terms of \(x\);
2. \(x\) in terms of \(t\).

#### Step 1: Interpret direction

The particle moves in the direction of increasing \(x\), but acceleration is directed towards \(O\). So

\[
a=-\frac12e^{-x}.
\]

#### Part (a): Find \(v\) in terms of \(x\)

Use

\[
a=v\frac{dv}{dx}.
\]

So

\[
v\frac{dv}{dx}=-\frac12e^{-x}.
\]

Separate variables:

\[
v\,dv=-\frac12e^{-x}\,dx.
\]

Integrate:

\[
\int v\,dv=\int -\frac12e^{-x}\,dx.
\]

Left-hand side:

\[
\int v\,dv=\frac12v^2.
\]

Right-hand side:

\[
\int -\frac12e^{-x}\,dx=\frac12e^{-x}.
\]

Therefore

\[
\frac12v^2=\frac12e^{-x}+C.
\]

Use \(x=0,v=1\):

\[
\frac12(1)^2=\frac12e^0+C.
\]

So

\[
\frac12=\frac12+C,
\]

hence

\[
C=0.
\]

Therefore

\[
\frac12v^2=\frac12e^{-x}.
\]

Multiply by \(2\):

\[
v^2=e^{-x}.
\]

Since the particle is moving in the direction of increasing \(x\), take the positive square root:

\[
\boxed{v=e^{-x/2}\ \text{m s}^{-1}}.
\]

#### Part (b): Find \(x\) in terms of \(t\)

Use

\[
v=\frac{dx}{dt}.
\]

From part (a),

\[
v=e^{-x/2}.
\]

So

\[
\frac{dx}{dt}=e^{-x/2}.
\]

Separate variables:

\[
e^{x/2}\,dx=dt.
\]

Integrate:

\[
\int e^{x/2}\,dx=\int 1\,dt.
\]

Thus

\[
2e^{x/2}=t+K.
\]

Use \(t=0,x=0\):

\[
2e^0=0+K,
\]

so

\[
K=2.
\]

Therefore

\[
2e^{x/2}=t+2.
\]

Divide by \(2\):

\[
e^{x/2}=\frac{t}{2}+1.
\]

Take natural logarithms:

\[
\frac{x}{2}=\ln\left(\frac{t}{2}+1\right).
\]

So

\[
\boxed{x=2\ln\left(\frac{t}{2}+1\right)\ \text{m}}.
\]

### Worked Example 8: Acceleration \(a=2x\), speed \(6\) at \(O\)

**Evidence source:** FM2 PDF page 9.  
**On-spec status:** On-spec for `FA22-FKIN-LO002`, acceleration as a function of displacement.  
**Evidence limitation:** The parsed text from the PDF is partly garbled on this example, especially the final inverse hyperbolic line. The setup supports \(a=2x\), \(v=6\) when \(x=0\), and the warning that the positive square root is used because the particle moves in the direction of increasing \(x\).

#### Question

A particle \(P\) moves on the \(x\)-axis in the direction of increasing \(x\). When the displacement of \(P\) from \(O\) is \(x\) metres and its speed is \(v\ \text{m s}^{-1}\), the acceleration of \(P\) is

\[
a=2x\ \text{m s}^{-2}.
\]

When \(P\) is at \(O\), its speed is

\[
6\ \text{m s}^{-1}.
\]

Find:

1. \(v\) in terms of \(x\);
2. \(x\) in terms of \(t\).

#### Part (a): Find \(v\) in terms of \(x\)

Use

\[
a=v\frac{dv}{dx}.
\]

So

\[
v\frac{dv}{dx}=2x.
\]

Separate variables:

\[
v\,dv=2x\,dx.
\]

Integrate:

\[
\int v\,dv=\int 2x\,dx.
\]

So

\[
\frac12v^2=x^2+C.
\]

Use \(x=0,v=6\):

\[
\frac12(6)^2=0^2+C.
\]

So

\[
C=18.
\]

Hence

\[
\frac12v^2=x^2+18.
\]

Multiply by \(2\):

\[
v^2=2x^2+36.
\]

Since \(P\) moves in the direction of increasing \(x\), take the positive square root:

\[
\boxed{v=\sqrt{2x^2+36}}.
\]

#### Part (b): Find \(x\) in terms of \(t\)

Use

\[
v=\frac{dx}{dt}.
\]

So

\[
\frac{dx}{dt}=\sqrt{2x^2+36}.
\]

Separate variables:

\[
\frac{dx}{\sqrt{2x^2+36}}=dt.
\]

Integrate:

\[
\int \frac{dx}{\sqrt{2x^2+36}}=\int dt.
\]

Factor inside the square root:

\[
2x^2+36=2(x^2+18).
\]

So

\[
\sqrt{2x^2+36}=\sqrt2\sqrt{x^2+18}.
\]

Therefore

\[
\int \frac{dx}{\sqrt{2x^2+36}}
=
\frac{1}{\sqrt2}
\int \frac{dx}{\sqrt{x^2+18}}.
\]

Use

\[
\int \frac{dx}{\sqrt{x^2+a^2}}=\operatorname{arsinh}\left(\frac{x}{a}\right)+C.
\]

Here

\[
a^2=18,
\qquad
a=\sqrt{18}=3\sqrt2.
\]

So

\[
\frac{1}{\sqrt2}
\operatorname{arsinh}\left(\frac{x}{\sqrt{18}}\right)=t+C.
\]

Use \(t=0,x=0\). Since \(\operatorname{arsinh}(0)=0\), \(C=0\). Hence

\[
\operatorname{arsinh}\left(\frac{x}{\sqrt{18}}\right)=\sqrt2\,t.
\]

Apply \(\sinh\):

\[
\frac{x}{\sqrt{18}}=\sinh(\sqrt2\,t).
\]

Therefore

\[
\boxed{x=3\sqrt2\,\sinh(\sqrt2\,t)}.
\]

### Worked Example 9: Acceleration as a function of velocity, \(a=4v\)

**Evidence source:** FM2 PDF page 13 and transcript functions-of-velocity example.  
**On-spec status:** On-spec for `FA22-FKIN-LO002`, acceleration as a function of velocity.  
**Ordinary Maths idea used:** Acceleration and velocity along a straight line.  
**Further Maths upgrade:** Use \(a=v\dfrac{dv}{dx}\) for a displacement/distance target.

#### Question

A particle \(P\) moves in a straight line. When the velocity of \(P\) is \(v\ \text{m s}^{-1}\), the acceleration of \(P\) is given by

\[
a=4v\ \text{m s}^{-2}.
\]

Find the distance moved by \(P\) as the velocity increases from \(10\ \text{m s}^{-1}\) to \(15\ \text{m s}^{-1}\).

#### Solution

We want distance, so use

\[
a=v\frac{dv}{dx}.
\]

Given

\[
a=4v.
\]

Therefore

\[
v\frac{dv}{dx}=4v.
\]

Assuming \(v\neq 0\) in this interval, divide by \(v\):

\[
\frac{dv}{dx}=4.
\]

Rearrange:

\[
dv=4\,dx.
\]

Equivalently,

\[
\frac14\,dv=dx.
\]

Integrate:

\[
\int \frac14\,dv=\int 1\,dx.
\]

So

\[
\frac14v=x+C.
\]

When \(v=10\), let the position be \(x_1\):

\[
\frac{10}{4}=x_1+C.
\]

When \(v=15\), let the position be \(x_2\):

\[
\frac{15}{4}=x_2+C.
\]

Subtract:

\[
x_2-x_1=\left(\frac{15}{4}-C\right)-\left(\frac{10}{4}-C\right).
\]

The constants cancel:

\[
x_2-x_1=\frac{15}{4}-\frac{10}{4}=\frac54.
\]

\[
\boxed{\frac54\ \text{m}}\quad \text{or}\quad \boxed{1.25\ \text{m}}.
\]

### Worked Example 10: Acceleration \(a=-(k^2+v^2)\), distance and time to rest

**Evidence source:** FM2 PDF page 14 and transcript functions-of-velocity example.  
**On-spec status:** On-spec for `FA22-FKIN-LO002`, acceleration as a function of velocity.  
**Ordinary Maths idea used:** A particle moves along the positive \(x\)-axis and comes to rest.  
**Further Maths upgrade:** Use both \(a=v\dfrac{dv}{dx}\) and \(a=\dfrac{dv}{dt}\) in the same problem, selecting according to the target.

#### Question

A particle \(P\) moves along the positive \(x\)-axis. At time \(t\) seconds, the acceleration of the particle is

\[
a=-(k^2+v^2),
\]

where \(v\ \text{m s}^{-1}\) is the velocity of the particle and \(k\) is a positive constant.

When \(t=0\), \(P\) is at \(O\) and \(v=U\). The particle comes to rest at point \(A\). Find, in terms of \(k\) and \(U\):

1. the distance \(OA\);
2. the time \(P\) takes to travel from \(O\) to \(A\).

#### Part (a): Find \(OA\)

Since we want distance/displacement, use

\[
a=v\frac{dv}{dx}.
\]

Given

\[
a=-(k^2+v^2),
\]

we get

\[
v\frac{dv}{dx}=-(k^2+v^2).
\]

Separate variables:

\[
\frac{v}{k^2+v^2}\,dv=-dx.
\]

Integrate:

\[
\int \frac{v}{k^2+v^2}\,dv=\int -1\,dx.
\]

The left-hand side is

\[
\frac12\ln(k^2+v^2).
\]

So

\[
\frac12\ln(k^2+v^2)=-x+C.
\]

Use \(x=0,v=U\):

\[
\frac12\ln(k^2+U^2)=C.
\]

Therefore

\[
\frac12\ln(k^2+v^2)=-x+\frac12\ln(k^2+U^2).
\]

Rearrange:

\[
x=\frac12\ln(k^2+U^2)-\frac12\ln(k^2+v^2).
\]

Use log laws:

\[
x=\frac12\ln\left(\frac{k^2+U^2}{k^2+v^2}\right).
\]

At \(A\), the particle comes to rest, so \(v=0\). Thus

\[
OA=\frac12\ln\left(\frac{k^2+U^2}{k^2}\right).
\]

\[
\boxed{OA=\frac12\ln\left(1+\frac{U^2}{k^2}\right)}.
\]

#### Part (b): Find the time from \(O\) to \(A\)

Now we want time, so use

\[
a=\frac{dv}{dt}.
\]

Given

\[
a=-(k^2+v^2),
\]

we have

\[
\frac{dv}{dt}=-(k^2+v^2).
\]

Separate variables:

\[
\frac{1}{k^2+v^2}\,dv=-dt.
\]

Integrate:

\[
\int \frac{1}{k^2+v^2}\,dv=\int -1\,dt.
\]

Use the standard integral:

\[
\int \frac{1}{k^2+v^2}\,dv
=
\frac{1}{k}\arctan\left(\frac{v}{k}\right).
\]

So

\[
\frac{1}{k}\arctan\left(\frac{v}{k}\right)=-t+C.
\]

Use \(t=0,v=U\):

\[
C=\frac{1}{k}\arctan\left(\frac{U}{k}\right).
\]

Therefore

\[
\frac{1}{k}\arctan\left(\frac{v}{k}\right)
=-t+
\frac{1}{k}\arctan\left(\frac{U}{k}\right).
\]

Rearrange:

\[
t=\frac{1}{k}\arctan\left(\frac{U}{k}\right)-\frac{1}{k}\arctan\left(\frac{v}{k}\right).
\]

At \(A\), \(v=0\), so

\[
t=\frac{1}{k}\arctan\left(\frac{U}{k}\right)-\frac{1}{k}\arctan(0).
\]

Since \(\arctan(0)=0\),

\[
\boxed{t=\frac{1}{k}\arctan\left(\frac{U}{k}\right)\ \text{s}}.
\]

### Worked Example 11: Three-dimensional vector kinematics, componentwise calculus

**Evidence source:** CCEA FKIN LO001 requirement.  
**On-spec status:** Core CCEA content for `FA22-FKIN-LO001`.  
**Evidence limitation:** This is generated CCEA-aligned instruction because the supplied FM2 lesson evidence is straight-line only and repeatedly says no vectors in that evidence set.  
**Ordinary Maths idea used:** AS1 vector components and A22 kinematics.  
**Further Maths upgrade:** Three-dimensional \(\mathbf{i},\mathbf{j},\mathbf{k}\) componentwise calculus.

#### Question

A particle has position vector

\[
\mathbf{r}(t)
=
(t^3-2t)\mathbf{i}
+
(4t^2+1)\mathbf{j}
+
(e^t-3t)\mathbf{k}.
\]

Find:

1. the velocity \(\mathbf{v}(t)\);
2. the acceleration \(\mathbf{a}(t)\);
3. the speed at \(t=0\).

#### Part (a): Velocity

Velocity is

\[
\mathbf{v}(t)=\frac{d\mathbf{r}}{dt}.
\]

Differentiate each component separately:

\[
\frac{d}{dt}(t^3-2t)=3t^2-2,
\]

\[
\frac{d}{dt}(4t^2+1)=8t,
\]

\[
\frac{d}{dt}(e^t-3t)=e^t-3.
\]

Therefore

\[
\boxed{
\mathbf{v}(t)
=
(3t^2-2)\mathbf{i}
+
8t\mathbf{j}
+
(e^t-3)\mathbf{k}
}.
\]

#### Part (b): Acceleration

Acceleration is

\[
\mathbf{a}(t)=\frac{d\mathbf{v}}{dt}.
\]

Differentiate each component:

\[
\frac{d}{dt}(3t^2-2)=6t,
\]

\[
\frac{d}{dt}(8t)=8,
\]

\[
\frac{d}{dt}(e^t-3)=e^t.
\]

Therefore

\[
\boxed{
\mathbf{a}(t)
=
6t\mathbf{i}
+
8\mathbf{j}
+
e^t\mathbf{k}
}.
\]

#### Part (c): Speed at \(t=0\)

First find velocity at \(t=0\):

\[
\mathbf{v}(0)
=
(3(0)^2-2)\mathbf{i}
+
8(0)\mathbf{j}
+
(e^0-3)\mathbf{k}.
\]

Simplify:

\[
\mathbf{v}(0)=-2\mathbf{i}+0\mathbf{j}-2\mathbf{k}.
\]

The speed is the magnitude:

\[
|\mathbf{v}(0)|
=
\sqrt{(-2)^2+0^2+(-2)^2}
=\sqrt{8}
=2\sqrt2.
\]

\[
\boxed{2\sqrt2\ \text{units s}^{-1}}.
\]

## 12. Common Mistakes and Exam Traps

### 12.1 Treating distance and displacement as the same thing

Displacement is signed:

\[
\Delta x=\int_{t_1}^{t_2}v(t)\,dt.
\]

Distance travelled is total path length:

\[
\text{distance}=\int_{t_1}^{t_2}|v(t)|\,dt.
\]

If \(v(t)\) becomes negative, the area under the velocity-time graph is negative, so it must be handled separately.

**Exam-safe rule:** If the question says **distance travelled**, find where \(v=0\) inside the interval, split the integral there, then add magnitudes.

### 12.2 Forgetting constants of integration

Every indefinite integration needs a constant:

\[
v=\int a\,dt+C,
\]

\[
x=\int v\,dt+C.
\]

**Bad:**

\[
v=\int \cos(2\pi t)\,dt=\frac{1}{2\pi}\sin(2\pi t).
\]

**Good:**

\[
v=\int \cos(2\pi t)\,dt
=
\frac{1}{2\pi}\sin(2\pi t)+C.
\]

Then use the initial condition.

### 12.3 Using \(a=\dfrac{dv}{dt}\) when the question needs displacement

When acceleration is given as a function of velocity,

\[
a=f(v),
\]

do not automatically use

\[
a=\frac{dv}{dt}.
\]

Use this if the question asks for velocity or time.

If the question asks for displacement or distance, use

\[
a=v\frac{dv}{dx}.
\]

### 12.4 Trying to integrate \(f(x)\) with respect to \(t\) before separating variables

If

\[
\frac{dx}{dt}=2x,
\]

you cannot write

\[
x=\int 2x\,dt
\]

as though \(x\) were a constant.

You must separate variables:

\[
\frac{1}{x}\,dx=2\,dt.
\]

Then integrate:

\[
\ln x=2t+C.
\]

### 12.5 Losing the direction sign

Words such as **towards \(O\)** and **away from \(O\)** are not decorative.

If \(x\) is positive and acceleration is directed towards \(O\), then acceleration is negative:

\[
a<0.
\]

If \(x\) is positive and acceleration is directed away from \(O\), then acceleration is positive:

\[
a>0.
\]

A common error is to use the magnitude as the signed value. For example, if the acceleration has magnitude \(4x\) directed towards \(O\), then

\[
a=-4x,
\]

not

\[
a=4x.
\]

### 12.6 Choosing the wrong square root

From

\[
v^2=e^{-x},
\]

you get

\[
v=\pm e^{-x/2}.
\]

The sign depends on direction. If the particle is moving in the direction of increasing \(x\), then

\[
v=e^{-x/2}.
\]

### 12.7 Mistaking instantaneous rest for “the particle stops forever”

Instantaneous rest means

\[
v=0
\]

at an instant. It does not mean the motion ends.

It often marks a change of direction, especially on a velocity-time graph. Treat it as a signpost, not a full stop.

### 12.8 Dropping vector constants in 3D

If

\[
\mathbf{a}(t)=2t\mathbf{i}+3\mathbf{j}-4t^3\mathbf{k},
\]

then

\[
\mathbf{v}(t)=t^2\mathbf{i}+3t\mathbf{j}-t^4\mathbf{k}+\mathbf{C}.
\]

The constant is a vector:

\[
\mathbf{C}=C_1\mathbf{i}+C_2\mathbf{j}+C_3\mathbf{k}.
\]

Do not use a single scalar constant for a 3D vector integration.

### 12.9 Treating cross-board examples as CCEA past-paper questions

The supplied FM2 evidence includes Pearson/Edexcel-style examples and exam references. These are useful for technique where CCEA confirms the topic is on-spec, but they are not CCEA past-paper evidence. The lesson keeps them as supporting evidence, with CCEA as the boundary ruler.

## 13. Practice Questions

All questions below are **generated practice questions**, not past-paper or textbook questions.

### Basic fluency questions

#### Question 1: Function of time

A particle moves in a straight line with velocity

\[
v=3t^2-12t+9
\]

for \(0\leq t\leq 5\).

1. Find the acceleration at time \(t\).
2. Find the times when the particle is instantaneously at rest.
3. Find the displacement from \(t=0\) to \(t=5\).
4. Find the total distance travelled from \(t=0\) to \(t=5\).

#### Question 2: Integrating acceleration

A particle moves along a line with acceleration

\[
a=6t-4.
\]

At \(t=0\),

\[
v=5,
\qquad
x=2.
\]

Find:

1. \(v\) in terms of \(t\);
2. \(x\) in terms of \(t\).

### Bridge questions

#### Question 3: Velocity as a function of displacement

A particle moves along the positive \(x\)-axis. Its velocity is

\[
v=3x.
\]

When \(t=0\),

\[
x=2.
\]

Find \(x\) in terms of \(t\).

#### Question 4: Acceleration as a function of displacement

A particle moves along the \(x\)-axis. Its acceleration is

\[
a=6x.
\]

When \(x=0\), its velocity is

\[
v=4.
\]

The particle moves in the direction of increasing \(x\). Find \(v\) in terms of \(x\).

### Standard exam-style questions

#### Question 5: Function of velocity for time

A particle moves along a straight line from rest. Its acceleration is

\[
a=12-3v,
\]

where \(v\ \text{m s}^{-1}\) is its velocity at time \(t\) seconds.

1. Find \(v\) in terms of \(t\).
2. Show that \(v\) cannot exceed \(4\ \text{m s}^{-1}\).

#### Question 6: Function of velocity for distance

A particle moves in a straight line. When its velocity is \(v\ \text{m s}^{-1}\), its acceleration is

\[
a=5v.
\]

Find the distance moved while its velocity increases from \(8\ \text{m s}^{-1}\) to \(18\ \text{m s}^{-1}\).

### Harder synthesis questions

#### Question 7: Constant power model

A car of mass \(1000\ \text{kg}\) moves along a straight horizontal road. Its engine supplies constant power \(20000\ \text{W}\). Resistance is constant and equal to \(500\ \text{N}\).

At a moment when the car’s speed is \(v\ \text{m s}^{-1}\), show that its acceleration is

\[
a=\frac{20}{v}-\frac12.
\]

Then find the speed at which the acceleration is zero.

#### Question 8: Three-dimensional kinematics

A particle has acceleration

\[
\mathbf{a}(t)=6t\mathbf{i}-4\mathbf{j}+12t^2\mathbf{k}.
\]

At \(t=0\),

\[
\mathbf{v}(0)=2\mathbf{i}+3\mathbf{j}-\mathbf{k}
\]

and

\[
\mathbf{r}(0)=\mathbf{i}-2\mathbf{j}+4\mathbf{k}.
\]

Find:

1. \(\mathbf{v}(t)\);
2. \(\mathbf{r}(t)\);
3. the speed at \(t=1\).

## 14. Worked Solutions

### Solution 1: Function of time

Given

\[
v=3t^2-12t+9.
\]

#### Part 1: Acceleration

\[
a=\frac{dv}{dt}=6t-12.
\]

\[
\boxed{a=6t-12}.
\]

#### Part 2: Instantaneous rest

Instantaneous rest means \(v=0\):

\[
3t^2-12t+9=0.
\]

Factor out \(3\):

\[
3(t^2-4t+3)=0.
\]

So

\[
t^2-4t+3=0.
\]

Factorise:

\[
(t-1)(t-3)=0.
\]

Therefore

\[
\boxed{t=1,\ 3}.
\]

#### Part 3: Displacement from \(0\) to \(5\)

\[
\Delta x=\int_0^5 v\,dt
=\int_0^5(3t^2-12t+9)\,dt.
\]

Integrate:

\[
\Delta x=
\left[t^3-6t^2+9t\right]_0^5.
\]

At \(t=5\):

\[
5^3-6(5)^2+9(5)=125-150+45=20.
\]

At \(t=0\), the expression is \(0\). Therefore

\[
\boxed{20\ \text{m}}.
\]

#### Part 4: Total distance travelled

Split at \(t=1\) and \(t=3\). Let

\[
F(t)=t^3-6t^2+9t.
\]

Calculate:

\[
F(0)=0,
\]

\[
F(1)=1-6+9=4,
\]

\[
F(3)=27-54+27=0,
\]

\[
F(5)=20.
\]

Velocity is positive on \([0,1]\), negative on \([1,3]\), and positive on \([3,5]\). Hence

\[
\text{distance}=(F(1)-F(0))-(F(3)-F(1))+(F(5)-F(3)).
\]

Substitute:

\[
\text{distance}=(4-0)-(0-4)+(20-0)=28.
\]

\[
\boxed{28\ \text{m}}.
\]

### Solution 2: Integrating acceleration

Given

\[
a=6t-4,
\]

with

\[
v=5,
\quad
x=2
\quad \text{when} \quad t=0.
\]

Since

\[
a=\frac{dv}{dt},
\]

we have

\[
v=\int(6t-4)\,dt=3t^2-4t+C.
\]

Use \(v=5\) when \(t=0\):

\[
5=C.
\]

Therefore

\[
\boxed{v=3t^2-4t+5}.
\]

Now

\[
x=\int v\,dt
=\int(3t^2-4t+5)\,dt.
\]

So

\[
x=t^3-2t^2+5t+C.
\]

Use \(x=2\) when \(t=0\):

\[
2=C.
\]

Therefore

\[
\boxed{x=t^3-2t^2+5t+2}.
\]

### Solution 3: Velocity as a function of displacement

Given

\[
v=3x.
\]

But

\[
v=\frac{dx}{dt}.
\]

So

\[
\frac{dx}{dt}=3x.
\]

Separate variables:

\[
\frac{1}{x}\,dx=3\,dt.
\]

Integrate:

\[
\ln x=3t+C.
\]

Use \(x=2\) when \(t=0\):

\[
\ln 2=C.
\]

Therefore

\[
\ln x=3t+\ln 2.
\]

Exponentiate:

\[
x=e^{3t+\ln 2}=e^{3t}e^{\ln 2}=2e^{3t}.
\]

\[
\boxed{x=2e^{3t}}.
\]

### Solution 4: Acceleration as a function of displacement

Given

\[
a=6x.
\]

Use

\[
a=v\frac{dv}{dx}.
\]

So

\[
v\frac{dv}{dx}=6x.
\]

Separate variables:

\[
v\,dv=6x\,dx.
\]

Integrate:

\[
\int v\,dv=\int 6x\,dx.
\]

Thus

\[
\frac12v^2=3x^2+C.
\]

Use \(x=0, v=4\):

\[
\frac12(4)^2=3(0)^2+C.
\]

So

\[
8=C.
\]

Therefore

\[
\frac12v^2=3x^2+8.
\]

Multiply by \(2\):

\[
v^2=6x^2+16.
\]

Since the particle moves in the direction of increasing \(x\), take the positive square root:

\[
\boxed{v=\sqrt{6x^2+16}}.
\]

### Solution 5: Function of velocity for time

Given

\[
a=12-3v.
\]

Since the question asks for \(v\) in terms of \(t\), use

\[
a=\frac{dv}{dt}.
\]

So

\[
\frac{dv}{dt}=12-3v.
\]

Separate variables:

\[
\frac{1}{12-3v}\,dv=dt.
\]

Integrate:

\[
\int \frac{1}{12-3v}\,dv=\int 1\,dt.
\]

Let \(u=12-3v\), so \(du/dv=-3\). Hence

\[
\int \frac{1}{12-3v}\,dv
=
-\frac13\ln(12-3v).
\]

Thus

\[
-\frac13\ln(12-3v)=t+C.
\]

The particle starts from rest, so \(v=0\) when \(t=0\). Substitute:

\[
-\frac13\ln(12)=C.
\]

Therefore

\[
-\frac13\ln(12-3v)=t-\frac13\ln 12.
\]

Multiply by \(-3\):

\[
\ln(12-3v)=-3t+
\ln 12.
\]

Exponentiate:

\[
12-3v=12e^{-3t}.
\]

Then

\[
-3v=12e^{-3t}-12.
\]

Divide by \(-3\):

\[
v=4-4e^{-3t}=4(1-e^{-3t}).
\]

\[
\boxed{v=4(1-e^{-3t})}.
\]

Since \(e^{-3t}>0\),

\[
1-e^{-3t}<1.
\]

Therefore

\[
4(1-e^{-3t})<4.
\]

So \(v<4\), and the speed cannot exceed

\[
\boxed{4\ \text{m s}^{-1}}.
\]

### Solution 6: Function of velocity for distance

Given

\[
a=5v.
\]

We need distance, so use

\[
a=v\frac{dv}{dx}.
\]

Thus

\[
v\frac{dv}{dx}=5v.
\]

Since \(v\neq 0\) on the interval from \(8\) to \(18\), divide by \(v\):

\[
\frac{dv}{dx}=5.
\]

Rearrange:

\[
dv=5\,dx,
\]

so

\[
dx=\frac15\,dv.
\]

Integrate between \(v=8\) and \(v=18\):

\[
\Delta x=\int_8^{18}\frac15\,dv.
\]

So

\[
\Delta x=\frac15[v]_8^{18}=\frac15(18-8)=2.
\]

\[
\boxed{2\ \text{m}}.
\]

### Solution 7: Constant power model

Given:

\[
m=1000\ \text{kg},
\qquad
P=20000\ \text{W},
\qquad
R=500\ \text{N}.
\]

Power is

\[
P=Fv.
\]

So the driving force is

\[
F=\frac{P}{v}=\frac{20000}{v}.
\]

The resultant force in the direction of motion is

\[
\frac{20000}{v}-500.
\]

Use Newton’s second law:

\[
F_{\text{resultant}}=ma.
\]

Thus

\[
1000a=\frac{20000}{v}-500.
\]

Divide by \(1000\):

\[
a=\frac{20000}{1000v}-\frac{500}{1000}
=\frac{20}{v}-\frac12.
\]

\[
\boxed{a=\frac{20}{v}-\frac12}.
\]

When acceleration is zero:

\[
0=\frac{20}{v}-\frac12.
\]

So

\[
\frac12=\frac{20}{v}.
\]

Multiply by \(v\):

\[
\frac12v=20.
\]

Therefore

\[
v=40.
\]

\[
\boxed{40\ \text{m s}^{-1}}.
\]

### Solution 8: Three-dimensional kinematics

Given

\[
\mathbf{a}(t)=6t\mathbf{i}-4\mathbf{j}+12t^2\mathbf{k}.
\]

Also

\[
\mathbf{v}(0)=2\mathbf{i}+3\mathbf{j}-\mathbf{k},
\]

\[
\mathbf{r}(0)=\mathbf{i}-2\mathbf{j}+4\mathbf{k}.
\]

#### Part 1: Find \(\mathbf{v}(t)\)

Integrate acceleration component by component:

\[
\mathbf{v}(t)=\int \mathbf{a}(t)\,dt.
\]

So

\[
\mathbf{v}(t)
=
\int 6t\,dt\ \mathbf{i}
+
\int (-4)\,dt\ \mathbf{j}
+
\int 12t^2\,dt\ \mathbf{k}
+
\mathbf{C}.
\]

Integrate:

\[
\int 6t\,dt=3t^2,
\]

\[
\int (-4)\,dt=-4t,
\]

\[
\int 12t^2\,dt=4t^3.
\]

Therefore

\[
\mathbf{v}(t)=3t^2\mathbf{i}-4t\mathbf{j}+4t^3\mathbf{k}+\mathbf{C}.
\]

Let

\[
\mathbf{C}=C_1\mathbf{i}+C_2\mathbf{j}+C_3\mathbf{k}.
\]

Use \(\mathbf{v}(0)=2\mathbf{i}+3\mathbf{j}-\mathbf{k}\). At \(t=0\):

\[
\mathbf{v}(0)=C_1\mathbf{i}+C_2\mathbf{j}+C_3\mathbf{k}.
\]

So

\[
C_1=2,
\quad
C_2=3,
\quad
C_3=-1.
\]

Therefore

\[
\boxed{
\mathbf{v}(t)
=
(3t^2+2)\mathbf{i}
+
(3-4t)\mathbf{j}
+
(4t^3-1)\mathbf{k}
}.
\]

#### Part 2: Find \(\mathbf{r}(t)\)

Integrate velocity:

\[
\mathbf{r}(t)=\int \mathbf{v}(t)\,dt.
\]

So

\[
\mathbf{r}(t)
=
\int(3t^2+2)\,dt\ \mathbf{i}
+
\int(3-4t)\,dt\ \mathbf{j}
+
\int(4t^3-1)\,dt\ \mathbf{k}
+
\mathbf{D}.
\]

Integrate:

\[
\int(3t^2+2)\,dt=t^3+2t,
\]

\[
\int(3-4t)\,dt=3t-2t^2,
\]

\[
\int(4t^3-1)\,dt=t^4-t.
\]

So

\[
\mathbf{r}(t)
=
(t^3+2t)\mathbf{i}
+
(3t-2t^2)\mathbf{j}
+
(t^4-t)\mathbf{k}
+
\mathbf{D}.
\]

Let

\[
\mathbf{D}=D_1\mathbf{i}+D_2\mathbf{j}+D_3\mathbf{k}.
\]

Use \(\mathbf{r}(0)=\mathbf{i}-2\mathbf{j}+4\mathbf{k}\). At \(t=0\):

\[
\mathbf{r}(0)=D_1\mathbf{i}+D_2\mathbf{j}+D_3\mathbf{k}.
\]

So

\[
D_1=1,
\quad
D_2=-2,
\quad
D_3=4.
\]

Therefore

\[
\boxed{
\mathbf{r}(t)
=
(t^3+2t+1)\mathbf{i}
+
(3t-2t^2-2)\mathbf{j}
+
(t^4-t+4)\mathbf{k}
}.
\]

#### Part 3: Speed at \(t=1\)

First find velocity at \(t=1\):

\[
\mathbf{v}(1)
=
(3(1)^2+2)\mathbf{i}
+
(3-4(1))\mathbf{j}
+
(4(1)^3-1)\mathbf{k}.
\]

So

\[
\mathbf{v}(1)=5\mathbf{i}-\mathbf{j}+3\mathbf{k}.
\]

Speed is magnitude:

\[
|\mathbf{v}(1)|=\sqrt{5^2+(-1)^2+3^2}
=\sqrt{25+1+9}
=\sqrt{35}.
\]

\[
\boxed{\sqrt{35}\ \text{m s}^{-1}}.
\]

## 15. Exam Technique Notes

### 15.1 Start by writing the known conditions

For example:

\[
t=0,
\quad
x=0,
\quad
v=U.
\]

This prevents condition drift, where you solve correctly but substitute the wrong pair of values.

### 15.2 Decide the target before choosing the formula

Ask:

```text
Do I need time, velocity, displacement, distance, or a vector?
```

Then choose:

\[
a=\frac{dv}{dt}
\]

for velocity/time, and

\[
a=v\frac{dv}{dx}
\]

for displacement/distance when \(a\) is tied to \(x\) or \(v\).

### 15.3 Use exact values unless decimals are requested

Keep answers such as:

\[
\frac{4}{\pi},
\qquad
16(1-2e^{-1}),
\qquad
\frac12\ln\left(1+\frac{U^2}{k^2}\right).
\]

Only round when asked.

### 15.4 Show the constant even if it disappears

For example:

\[
\frac14v=x+C.
\]

Even if you later take a difference and \(C\) cancels, the constant shows the general relationship.

### 15.5 For “show that” questions, aim at the printed target

If a question asks you to show a particular differential equation, shape your algebra towards the required form rather than wandering through unrelated variables.

### 15.6 For terminal velocity, explain the limiting idea

If \(v\) tends towards a value but never reaches it, state that clearly. Terminal velocity is approached but not exactly reached in the idealised model.

### 15.7 For 3D vector kinematics, keep components aligned

Write:

\[
\mathbf{v}(t)=v_x(t)\mathbf{i}+v_y(t)\mathbf{j}+v_z(t)\mathbf{k}.
\]

Do not mix components:

- \(\mathbf{i}\)-component integrates with \(\mathbf{i}\);
- \(\mathbf{j}\)-component integrates with \(\mathbf{j}\);
- \(\mathbf{k}\)-component integrates with \(\mathbf{k}\).

## 16. Syllabus Gap Check

### 16.1 LO coverage table

| LO ID | Coverage status | Evidence strength | Notes |
|---|---|---|---|
| `FA22-FKIN-LO001` | Partly covered | Weak lesson-specific evidence | Theory and generated practice included for 3D \(\mathbf{i},\mathbf{j},\mathbf{k}\) kinematics. Supplied transcript/PDF evidence focuses on straight-line motion and does not supply CCEA-style 3D worked examples. |
| `FA22-FKIN-LO002` | Strongly covered | Strong | Covered through \(a=f(t)\), \(v=f(t)\), \(v=f(x)\), \(a=f(x)\), \(a=f(v)\), distance vs displacement, separable DEs, constants and constant-power boundary note. |

### 16.2 Evidence coverage table

| Evidence feature | Covered in lesson? | Notes |
|---|---:|---|
| Kinematics as study of motion | Yes | Included in Big Picture. |
| Dynamics distinction | Yes | Logged as future chapter, not core. |
| Integration-heavy warning | Yes | Included in prerequisite and exam technique. |
| \(x,v,a\) ladder | Yes | Included in theory and TikZ placeholder. |
| Dot notation \(\dot{x},\ddot{x}\) | Yes | Included in definitions. |
| Negative velocity-time graph areas | Yes | Included in theory, visual plan, examples and mistakes. |
| \(v=4\sin(2\pi t)\) example | Yes | Fully worked. |
| \(v=te^{-t/4}\) example | Yes | Fully worked. |
| \(a=\cos(2\pi t)\) example | Yes | Fully worked. |
| Piecewise velocity example | Yes | Fully worked. |
| \(v=2x\) separation example | Yes | Fully worked. |
| \(a=v\dfrac{dv}{dx}\) derivation | Yes | Included in theory and visual plan. |
| \(a=2x\) example | Yes | Included with evidence limitation. |
| \(a=4v\) example | Yes | Fully worked. |
| \(a=-(k^2+v^2)\) example | Yes | Fully worked. |
| Terminal velocity examples | Partly | Included as technique note and practice flavour. |
| Constant power | Partly | Included as boundary note and generated practice. More CCEA evidence desirable. |
| 3D vector kinematics | Partly | Required by CCEA. Included from syllabus, but not supported by supplied lesson-specific worked evidence. |

### 16.3 Bridge coverage table

| Bridge area | Covered? | Location |
|---|---:|---|
| AS2 displacement, velocity, acceleration | Yes | Sections 5, 7, 8 |
| Velocity-time graph area | Yes | Sections 8, 9, 11, 12 |
| A22 calculus kinematics | Yes | Sections 5, 8 |
| A21 product rule and integration by parts | Yes | Worked Example 2 |
| A21 separable differential equations | Yes | Sections 8, 11, 14 |
| AS1 vectors into 3D \(\mathbf{i},\mathbf{j},\mathbf{k}\) | Yes | Sections 8, 11, 14 |

### 16.4 Off-Spec Content Found but Excluded

| Content | Source | Reason excluded from core |
|---|---|---|
| Full dynamics treatment using forces to produce motion | Transcript chapter comparison | Dynamics is a separate chapter and not the core FKIN lesson. |
| F=ma example flagged as “not technically covered until chapter 5” | FM2 PDF page reference | The PDF itself warns this belongs at the start of chapter 5, so it is excluded from core FKIN. |
| Edexcel/Pearson past exam identity | FM2 PDF and transcript | Used only as cross-board style evidence. Not presented as CCEA past-paper content. |
| Uninspected screenshot details | Screenshot PDF | Screenshot PDF has no parsed text; only visible/readable details are used. No hidden diagram detail is claimed. |

### 16.5 Optional Enrichment Not Required by CCEA

- Extra terminal velocity modelling with air resistance.
- Full dynamics derivation from forces before Chapter 5.
- Detailed constant-power vehicle modelling beyond the FKIN method boundary.
- Additional Core Pure integration tables and formula-book strategy drills.

### 16.6 Weak evidence warnings

1. `FA22-FKIN-LO001` needs stronger CCEA-specific 3D kinematics evidence.
2. Constant-power examples are required by CCEA wording but only lightly evidenced in the supplied material.
3. The screenshot PDF contains many pages, but parsed text was unavailable, so only visible/readable screenshot details from the tool preview were used.

### 16.7 Missing evidence log

| Missing evidence | Effect |
|---|---|
| CCEA 3D kinematics worked examples | LO001 is covered by generated CCEA-aligned examples, not lesson-specific worked evidence. |
| CCEA constant-power worked examples | Constant-power practice included, but evidence-backed treatment is limited. |
| CCEA mark schemes for FKIN | Exam technique is general and evidence-aligned, not mark-scheme-specific. |
| Clean OCR from screenshot PDF | Some handwritten details may be omitted rather than guessed. |

## 17. Recommended Enhancements Not in the Evidence

These are proposed enhancements, not evidence-backed source details.

### 17.1 Diagrams

1. A clean \(x,v,a\) ladder showing differentiate down and integrate up.
2. A velocity-time graph shaded by sign to distinguish displacement from distance.
3. A decision tree for \(a=f(t)\), \(a=f(x)\), and \(a=f(v)\).
4. A 3D vector kinematics coordinate diagram using \(\mathbf{i}\), \(\mathbf{j}\), \(\mathbf{k}\).
5. A constant-power model diagram showing:

\[
P=Fv,
\qquad
F=\frac{P}{v},
\qquad
ma=\frac{P}{v}-R.
\]

### 17.2 Animations

1. A particle moving along a number line while \(v(t)\) changes sign.
2. A live velocity-time graph where negative area is flipped for distance.
3. A 3D path with moving velocity and acceleration vectors.

### 17.3 Widgets

1. Method selector: choose the correct formula from given and target variables.
2. Distance splitter: build \(\int |v|\,dt\) from velocity roots.
3. Separating variables checker: catch invalid integrations.
4. Vector component calculator: differentiate/integrate \(\mathbf{i},\mathbf{j},\mathbf{k}\) components.
5. Constant-power explorer: vary \(P\), \(R\), \(m\), and \(v\), then observe \(a\).

### 17.4 Extra examples

1. A clean CCEA-style 3D vector problem with initial velocity and position.
2. A constant-power vehicle problem with resistance proportional to velocity.
3. A function-of-velocity problem requiring partial fractions.
4. A problem where \(v\) changes sign more than once.
5. A problem requiring exact logarithmic simplification.

## 18. Supplementary Sources Used

### Project Sources used

- `CCEA_GCE_Further_Mathematics_Specification_Map.md`
- `Further_Maths_README_module_map.md`
- `Further_Maths_EVIDENCE_DROP_CHECKLIST.md`
- `Ordinary_A_Level_Maths_Bridge_Spec_Extracts.md`
- `CCEA_GCE_Mathematics_Specification_Map.md`

### Lesson-specific evidence used

- `FM2-Chp4-Kinematics.pdf`
- `Chapter_4_Kinematics_🚗_(Further_Mechanics_2)_screenshots.pdf`
- `transcripts.md`

### Cross-board source notes

The FM2 PDF and transcript are Pearson/Edexcel-style Further Mechanics resources. They are used only where the CCEA Further Mathematics FKIN specification confirms the content is on-spec. The PDF itself labels some content as Edexcel and Pearson, so this lesson treats it as supporting evidence rather than CCEA authority.

### Ordinary A-Level Maths bridge sources

Ordinary CCEA A-Level Mathematics sources were used only to explain prerequisite knowledge and transition points:

- AS2 Kinematics;
- A22 Kinematics;
- A21 Calculus;
- AS1 Vectors.

They do not override the CCEA Further Mathematics topic boundary.

### Evidence limitations

- The screenshot PDF was not text-parsed. Visual details are included only where visible/readable.
- The supplied lesson evidence repeatedly focuses on straight-line motion and says no vectors in that evidence set, but CCEA FKIN includes 3D vector kinematics, so a CCEA-required vector section was included with weak evidence warning.
- Some PDF-parsed formulae are garbled, so clean algebra was reconstructed only where the setup was clear from the transcript/PDF context.

## 19. Final Student Checklist

### Prerequisite confidence checklist

Before exam practice, you should be able to say yes to each of these:

- [ ] I know the difference between displacement and distance.
- [ ] I know that velocity is signed but speed is non-negative.
- [ ] I can differentiate \(x(t)\) to get \(v(t)\).
- [ ] I can differentiate \(v(t)\) to get \(a(t)\).
- [ ] I can integrate \(a(t)\) to get \(v(t)\), including \(+C\).
- [ ] I can integrate \(v(t)\) to get \(x(t)\), including \(+C\).
- [ ] I can use initial conditions such as \(t=0,\ x=0,\ v=U\).
- [ ] I can separate variables in a differential equation.
- [ ] I can use product rule and integration by parts when needed.
- [ ] I can work with \(\mathbf{i}\), \(\mathbf{j}\), and \(\mathbf{k}\) components.

### Further Maths method checklist

- [ ] If \(a=f(t)\), I use \(a=\dfrac{dv}{dt}\).
- [ ] If \(v=f(t)\), I differentiate for \(a\) and integrate for \(x\).
- [ ] If \(v=f(x)\), I use \(v=\dfrac{dx}{dt}\) and separate variables.
- [ ] If \(a=f(x)\), I use \(a=v\dfrac{dv}{dx}\).
- [ ] If \(a=f(v)\) and I need time or velocity, I use \(a=\dfrac{dv}{dt}\).
- [ ] If \(a=f(v)\) and I need displacement or distance, I use \(a=v\dfrac{dv}{dx}\).
- [ ] I know that

\[
v\frac{dv}{dx}
=
\frac{d}{dx}\left(\frac12v^2\right).
\]

- [ ] I choose the correct square root sign using direction of motion.

### Exam technique checklist

- [ ] I write constants of integration.
- [ ] I label units.
- [ ] I keep exact answers unless decimals are requested.
- [ ] I split distance integrals at roots of \(v\).
- [ ] I do not assume instantaneous rest means the particle stops permanently.
- [ ] I state whether acceleration is towards or away from \(O\).
- [ ] I check whether a question asks for displacement or distance.
- [ ] I use the formula book for harder standard integrals where appropriate.
- [ ] I follow the structure of “show that” questions instead of wandering off-road.

### Bridge checklist

- [ ] I can explain how ordinary A-Level \(x,v,a\) calculus becomes Further Maths variable acceleration.
- [ ] I can explain why \(a=f(x)\) needs \(a=v\dfrac{dv}{dx}\).
- [ ] I can explain why \(a=f(v)\) may need either \(\dfrac{dv}{dt}\) or \(v\dfrac{dv}{dx}\).
- [ ] I can explain why vector kinematics is just componentwise calculus in 3D.

### Visual understanding checklist

- [ ] I can read a velocity-time graph and identify positive and negative areas.
- [ ] I can mark intervals where \(v>0\), \(v=0\), and \(v<0\).
- [ ] I can sketch a velocity approaching an asymptote.
- [ ] I can draw a straight-line motion axis with \(O\), \(P\), \(x\), \(v\), and \(a\).
- [ ] I can draw or interpret \(\mathbf{r}(t)\), \(\mathbf{v}(t)\), and \(\mathbf{a}(t)\) in 3D.
