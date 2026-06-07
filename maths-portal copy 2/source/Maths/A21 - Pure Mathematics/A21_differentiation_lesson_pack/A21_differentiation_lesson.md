# A21 Differentiation

## Title and Metadata

| Field | Value |
|---|---|
| Course | CCEA GCE Mathematics |
| Unit code | A21 |
| Unit name | A2 1 Pure Mathematics |
| Topic code | A21-DIFF |
| Topic name | Differentiation |
| Topic slug | differentiation |
| Topic Pascal | Differentiation |
| Topic ID | A21Differentiation |
| Lesson file | A21_differentiation_lesson.md |
| Pack status | Written to files and packaged |

## Evidence Map

| Evidence | Role |
|---|---|
| CCEA specification map | Authority for A21-DIFF topic boundary and exact LO IDs. |
| Project module map | Metadata, standard unit prefixes and file conventions. |
| Project evidence checklist | Missing evidence, off-spec and visual placeholder controls. |
| Chapter 9 Differentiation transcript | Core explanations, examples, warnings and exam traps. |
| P2 Chapter 9 Differentiation slide PDF | Slide sequence, formulas, examples and visual prompts. |
| Screenshots PDF | Visual support only; no parsed text was available. |

## Specification Alignment

| LO ID | Coverage |
|---|---|
| A21-DIFF-LO001 | Differentiating \(e^{kx}\), \(\ln(kx)\), \(\sin(kx)\), \(\cos(kx)\), \(\tan(kx)\) and related sums, differences and constant multiples. |
| A21-DIFF-LO002 | Chain rule, product rule and quotient rule. |
| A21-DIFF-LO003 | Differentiating \(\cosec x\), \(\sec x\) and \(\cot x\), including chain-rule forms. |
| A21-DIFF-LO004 | Parametric differentiation, implicit differentiation and second derivatives. |
| A21-DIFF-LO005 | Connected rates included; full construction of simple differential equations is logged as partial evidence. |

## Learning Objectives

By the end of this lesson, you should be able to:

1. Differentiate \(e^{kx}\), \(\ln(kx)\), \(\sin(kx)\), \(\cos(kx)\), \(\tan(kx)\), \(\sec x\), \(\cosec x\) and \(\cot x\).
2. Prove from first principles that \(\frac{d}{dx}(\sin x)=\cos x\).
3. Explain why trigonometric differentiation uses radians.
4. Apply the chain, product and quotient rules.
5. Differentiate parametrically and implicitly.
6. Use \(\frac{d^2y}{dx^2}\) for concavity, convexity and inflection.
7. Solve connected rates of change problems.
8. Recognise inverse trig differentiation as off-spec for this standard CCEA lesson.

## Prerequisite Recap

This lesson uses A-Level prior knowledge only: power-rule differentiation, algebraic simplification, trigonometric identities, radians, small-angle approximations, exponential/log laws and coordinate geometry of tangents and normals.

## Big Picture Explanation

Year 1 differentiation mainly used:

\[
\frac{d}{dx}(ax^n)=anx^{n-1}.
\]

A2 Differentiation expands the toolbox to trigonometric, exponential, logarithmic, composite, product, quotient, parametric and implicit functions. It also applies derivatives to stationary points, tangents, normals, concavity and rates of change.

## Key Definitions and Notation

If \(y=f(x)\), then:

\[
\frac{dy}{dx}=f'(x).
\]

The first-principles derivative is:

\[
f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}.
\]

The limit notation must remain until the limit is taken.

Small-angle approximations used in the proof are:

\[
\sin h\approx h,\qquad \cos h\approx 1-\frac12h^2
\]

in radians.

The addition formula used is:

\[
\sin(x+h)=\sin x\cos h+\cos x\sin h.
\]

## Core Theory 1: Differentiating \(\sin x\) from First Principles

Let:

\[
f(x)=\sin x.
\]

Then:

\[
f'(x)=\lim_{h\to0}\frac{\sin(x+h)-\sin x}{h}.
\]

Use:

\[
\sin(x+h)=\sin x\cos h+\cos x\sin h.
\]

So:

\[
f'(x)=\lim_{h\to0}\frac{\sin x\cos h+\cos x\sin h-\sin x}{h}.
\]

Collect the \(\sin x\) terms:

\[
f'(x)=\lim_{h\to0}\frac{\sin x(\cos h-1)+\cos x\sin h}{h}.
\]

Split into two fractions:

\[
f'(x)=\lim_{h\to0}\left(\sin x\frac{\cos h-1}{h}+\cos x\frac{\sin h}{h}\right).
\]

Now:

\[
\lim_{h\to0}\frac{\sin h}{h}=1
\]

and:

\[
\lim_{h\to0}\frac{\cos h-1}{h}=0.
\]

For the second limit:

\[
\frac{\cos h-1}{h}\approx
\frac{\left(1-\frac12h^2\right)-1}{h}
=
-\frac12h\to0.
\]

Therefore:

\[
f'(x)=\sin x(0)+\cos x(1)=\cos x.
\]

Hence:

\[
\boxed{\frac{d}{dx}(\sin x)=\cos x.}
\]

[VISUAL PLACEHOLDER: A21DifferentiationMermaid-001 | Source: Chapter 9 transcript + slide PDF | Insert from mermaid/A21DifferentiationMermaid-001.md | Purpose: Show the first-principles proof flow.]

## Core Theory 2: Why Trig Differentiation Uses Radians

The proof uses \(\sin h\approx h\) and \(\cos h\approx1-\frac12h^2\), which only hold in radians. Therefore:

\[
\boxed{\text{A-Level trigonometric differentiation is done in radians.}}
\]

[VISUAL PLACEHOLDER: A21DifferentiationSVG-001 | Source: Chapter 9 transcript + slide PDF | Insert from svg/A21DifferentiationSVG-001.svg | Purpose: Compare sine near zero in radians and degrees.]

## Core Theory 3: Standard Trig Rules

\[
\boxed{\frac{d}{dx}(\sin x)=\cos x}
\]

\[
\boxed{\frac{d}{dx}(\cos x)=-\sin x}
\]

\[
\boxed{\frac{d}{dx}(\sin kx)=k\cos kx}
\]

\[
\boxed{\frac{d}{dx}(\cos kx)=-k\sin kx}
\]

Keep the argument the same:

\[
\frac{d}{dx}(\sin3x)=3\cos3x,
\]

not \(3\cos x\).

[VISUAL PLACEHOLDER: A21DifferentiationSVG-002 | Source: Chapter 9 transcript | Insert from svg/A21DifferentiationSVG-002.svg | Purpose: Show the gradient of \(y=\sin x\) as \(y=\cos x\).]

## Worked Example 1: Quickfire Trig

\[
\frac{d}{dx}(\sin3x)=3\cos3x.
\]

\[
\frac{d}{dx}(\cos5x)=-5\sin5x.
\]

\[
\frac{d}{dx}(3\sin5x)=15\cos5x.
\]

\[
\frac{d}{dx}(4\cos3x)=-12\sin3x.
\]

\[
\frac{d}{dx}\left(-\frac12\sin x\right)=-\frac12\cos x.
\]

\[
\frac{d}{dx}\left(-\frac23\cos\frac{x}{2}\right)=\frac13\sin\frac{x}{2}.
\]

## Worked Example 2: Stationary Points

For:

\[
y=\frac12x-\cos2x,\qquad 0\leq x\leq\pi,
\]

differentiate:

\[
\frac{dy}{dx}=\frac12+2\sin2x.
\]

At stationary points:

\[
\frac12+2\sin2x=0.
\]

\[
\sin2x=-\frac14.
\]

The interval becomes:

\[
0\leq2x\leq2\pi.
\]

Solving:

\[
2x=3.3943\ldots,\qquad 2x=6.0305\ldots
\]

so:

\[
x=1.6971\ldots,\qquad x=3.0152\ldots
\]

Substitute into \(y=\frac12x-\cos2x\):

\[
\boxed{(1.70,1.82)\text{ and }(3.02,0.54).}
\]

[VISUAL PLACEHOLDER: A21DifferentiationTikZ-002 | Source: Chapter 9 worked example | Insert from tikz/A21DifferentiationTikZ-002.tex | Purpose: Show the stationary points.]

## Guided Practice 1

For:

\[
y=\sin3x+2x,\qquad 0\leq x\leq\frac23\pi,
\]

\[
\frac{dy}{dx}=3\cos3x+2.
\]

Set:

\[
3\cos3x+2=0
\]

so:

\[
\cos3x=-\frac23.
\]

With \(0\leq3x\leq2\pi\):

\[
3x=2.3005\ldots,\qquad 3x=3.9827\ldots
\]

\[
x=0.7668\ldots,\qquad x=1.3276\ldots
\]

Substitution gives:

\[
\boxed{(0.767,2.279)\text{ and }(1.328,1.910).}
\]

## Core Theory 4: Exponential and Logarithmic Derivatives

\[
\boxed{\frac{d}{dx}(e^x)=e^x}
\]

\[
\boxed{\frac{d}{dx}(e^{kx})=ke^{kx}}
\]

\[
\boxed{\frac{d}{dx}(a^x)=\ln(a)a^x}
\]

\[
\boxed{\frac{d}{dx}(a^{kx})=k\ln(a)a^{kx}}
\]

\[
\boxed{\frac{d}{dx}(\ln x)=\frac1x}
\]

\[
\boxed{\frac{d}{dx}(\ln(kx))=\frac1x}
\]

because:

\[
\ln(kx)=\ln k+\ln x.
\]

## Worked Example 3: Expand First

\[
y=(e^x+2)^2=(e^x+2)(e^x+2)
\]

\[
=e^x\cdot e^x+2e^x+2e^x+4
\]

\[
=e^{2x}+4e^x+4.
\]

Differentiate:

\[
\boxed{\frac{dy}{dx}=2e^{2x}+4e^x.}
\]

Do not write \(e^x\cdot e^x=e^{x^2}\). Powers add.

## Worked Example 4: Exponential Decay and Rate

Given:

\[
p=460\cdot3^{-2t}.
\]

If \(p=20\):

\[
20=460\cdot3^{-2t}.
\]

\[
\frac1{23}=3^{-2t}.
\]

\[
-2t=\log_3\left(\frac1{23}\right).
\]

\[
\boxed{t\approx1.43\text{ days}.}
\]

Now:

\[
\frac{dp}{dt}=460(-2\ln3)3^{-2t}
=-920\ln3\cdot3^{-2t}.
\]

At \(t=3\):

\[
\boxed{\frac{dp}{dt}\approx-1.39\text{ lice per day}.}
\]

The negative sign means the population is decreasing.

## Worked Example 5: Exponential Growth Target Rate

Given:

\[
p=1000\cdot2^t,
\]

\[
\frac{dp}{dt}=1000\ln2\cdot2^t.
\]

Set:

\[
1000\ln2\cdot2^t=20000.
\]

\[
2^t=\frac{20}{\ln2}.
\]

\[
\boxed{t=\log_2\left(\frac{20}{\ln2}\right)\approx4.85\text{ years}.}
\]

## Core Theory 5: Chain, Product and Quotient Rules

### Chain Rule

If:

\[
y=f(u),\qquad u=g(x),
\]

then:

\[
\boxed{\frac{dy}{dx}=\frac{dy}{du}\frac{du}{dx}.}
\]

Example:

\[
y=(3x+1)^5.
\]

Let \(u=3x+1\). Then \(y=u^5\).

\[
\frac{dy}{du}=5u^4,\qquad \frac{du}{dx}=3.
\]

\[
\boxed{\frac{dy}{dx}=15(3x+1)^4.}
\]

Example:

\[
y=e^{2x^2}.
\]

Let \(u=2x^2\). Then:

\[
\boxed{\frac{dy}{dx}=4xe^{2x^2}.}
\]

Example:

\[
y=\ln(x^2+5).
\]

\[
\boxed{\frac{dy}{dx}=\frac{2x}{x^2+5}.}
\]

### Product Rule

If:

\[
y=uv,
\]

then:

\[
\boxed{\frac{dy}{dx}=u\frac{dv}{dx}+v\frac{du}{dx}.}
\]

Example:

\[
y=x\sin x.
\]

\[
\boxed{\frac{dy}{dx}=x\cos x+\sin x.}
\]

Example:

\[
y=x^2e^{3x}.
\]

\[
\frac{dy}{dx}=x^2(3e^{3x})+e^{3x}(2x)
=xe^{3x}(3x+2).
\]

\[
\boxed{\frac{dy}{dx}=xe^{3x}(3x+2).}
\]

### Quotient Rule

If:

\[
y=\frac{u}{v},
\]

then:

\[
\boxed{
\frac{dy}{dx}
=
\frac{v\frac{du}{dx}-u\frac{dv}{dx}}{v^2}.
}
\]

Example:

\[
y=\frac{x^2+1}{x-3}.
\]

\[
\frac{dy}{dx}
=
\frac{(x-3)(2x)-(x^2+1)}{(x-3)^2}
=
\frac{x^2-6x-1}{(x-3)^2}.
\]

\[
\boxed{\frac{dy}{dx}=\frac{x^2-6x-1}{(x-3)^2}.}
\]

Example:

\[
y=\frac{\sin x}{x}.
\]

\[
\boxed{\frac{dy}{dx}=\frac{x\cos x-\sin x}{x^2}.}
\]

[VISUAL PLACEHOLDER: A21DifferentiationMermaid-002 | Source: CCEA A21-DIFF-LO002 + transcript | Insert from mermaid/A21DifferentiationMermaid-002.md | Purpose: Choose chain, product, quotient, parametric, implicit or connected rates.]

## Core Theory 6: \(\tan x\), \(\sec x\), \(\cosec x\), \(\cot x\)

Since:

\[
\tan x=\frac{\sin x}{\cos x},
\]

quotient rule gives:

\[
\frac{d}{dx}(\tan x)=
\frac{\cos x(\cos x)-\sin x(-\sin x)}{\cos^2x}
=
\frac{\cos^2x+\sin^2x}{\cos^2x}
=
\sec^2x.
\]

So:

\[
\boxed{\frac{d}{dx}(\tan x)=\sec^2x.}
\]

The reciprocal trig derivatives are:

\[
\boxed{\frac{d}{dx}(\sec x)=\sec x\tan x}
\]

\[
\boxed{\frac{d}{dx}(\cosec x)=-\cosec x\cot x}
\]

\[
\boxed{\frac{d}{dx}(\cot x)=-\cosec^2x.}
\]

With \(kx\):

\[
\frac{d}{dx}(\tan kx)=k\sec^2(kx),
\]

\[
\frac{d}{dx}(\sec kx)=k\sec(kx)\tan(kx),
\]

\[
\frac{d}{dx}(\cosec kx)=-k\cosec(kx)\cot(kx),
\]

\[
\frac{d}{dx}(\cot kx)=-k\cosec^2(kx).
\]

## Worked Example 6: Reciprocal Trig Quotient

Differentiate:

\[
y=\frac{\cosec2x}{x^2}.
\]

Let:

\[
u=\cosec2x,\qquad v=x^2.
\]

\[
u'=-2\cosec2x\cot2x,\qquad v'=2x.
\]

\[
\frac{dy}{dx}
=
\frac{x^2(-2\cosec2x\cot2x)-(\cosec2x)(2x)}{x^4}.
\]

\[
=
\frac{-2x^2\cosec2x\cot2x-2x\cosec2x}{x^4}.
\]

\[
=
\frac{-2x\cosec2x(x\cot2x+1)}{x^4}.
\]

\[
\boxed{
\frac{dy}{dx}=
\frac{-2\cosec2x(x\cot2x+1)}{x^3}.
}
\]

Do not cancel the \(x\) inside \(\cosec2x\) or \(\cot2x\).

## Worked Example 7: Powers of Sec

\[
y=\sec^3x=(\sec x)^3.
\]

Let \(u=\sec x\). Then:

\[
\frac{dy}{du}=3u^2,\qquad \frac{du}{dx}=\sec x\tan x.
\]

\[
\boxed{\frac{dy}{dx}=3\sec^3x\tan x.}
\]

## Worked Example 8: Composite Tan

\[
y=\tan(e^x+\sin2x).
\]

Let \(u=e^x+\sin2x\). Then:

\[
\frac{dy}{du}=\sec^2u,\qquad \frac{du}{dx}=e^x+2\cos2x.
\]

\[
\boxed{
\frac{dy}{dx}=(e^x+2\cos2x)\sec^2(e^x+\sin2x).
}
\]

## Off-Spec Warning: Inverse Trig Derivatives

Derivatives of \(\arcsin x\), \(\arccos x\) and \(\arctan x\) are excluded from this standard CCEA Mathematics core lesson. They are logged as Further Maths or extension material.

## Core Theory 7: Parametric Differentiation

If:

\[
x=f(t),\qquad y=g(t),
\]

then:

\[
\boxed{\frac{dy}{dx}=\frac{dy/dt}{dx/dt}.}
\]

[VISUAL PLACEHOLDER: A21DifferentiationSVG-004 | Source: Chapter 9 transcript | Insert from svg/A21DifferentiationSVG-004.svg | Purpose: Show \(dx/dt\), \(dy/dt\) and \(\frac{dy}{dx}\).]

Example:

\[
x=t^3+t,\qquad y=t^2+1.
\]

\[
\frac{dx}{dt}=3t^2+1,\qquad \frac{dy}{dt}=2t.
\]

\[
\frac{dy}{dx}=\frac{2t}{3t^2+1}.
\]

At \(t=2\):

\[
\boxed{\frac{dy}{dx}=\frac4{13}.}
\]

Example normal:

\[
x=3\sin\theta,\qquad y=5\cos\theta,\qquad \theta=\frac{\pi}{6}.
\]

\[
\frac{dy}{dx}=\frac{-5\sin\theta}{3\cos\theta}=-\frac53\tan\theta.
\]

At \(\theta=\frac{\pi}{6}\):

\[
m_{\text{tangent}}=-\frac{5}{3\sqrt3}
\]

so:

\[
m_{\text{normal}}=\frac{3\sqrt3}{5}.
\]

The point is:

\[
\left(\frac32,\frac{5\sqrt3}{2}\right).
\]

The normal is:

\[
\boxed{
y-\frac{5\sqrt3}{2}
=
\frac{3\sqrt3}{5}\left(x-\frac32\right).
}
\]

## Core Theory 8: Implicit Differentiation

For implicit relations, \(x\) and \(y\) are mixed. Remember:

\[
\boxed{\frac{d}{dx}(y^n)=ny^{n-1}\frac{dy}{dx}.}
\]

[VISUAL PLACEHOLDER: A21DifferentiationMermaid-004 | Source: Chapter 9 transcript | Insert from mermaid/A21DifferentiationMermaid-004.md | Purpose: Show implicit differentiation workflow.]

Example:

\[
x^2+y^2=16.
\]

Differentiate:

\[
2x+2y\frac{dy}{dx}=0.
\]

\[
\boxed{\frac{dy}{dx}=-\frac{x}{y}.}
\]

[VISUAL PLACEHOLDER: A21DifferentiationTikZ-003 | Source: Chapter 9 implicit differentiation evidence | Insert from tikz/A21DifferentiationTikZ-003.tex | Purpose: Show radius-tangent geometry.]

Example:

\[
x^2-2xy+y^2-3\sin x=0.
\]

Differentiate:

\[
2x-2\left(x\frac{dy}{dx}+y\right)+2y\frac{dy}{dx}-3\cos x=0.
\]

Expand:

\[
2x-2x\frac{dy}{dx}-2y+2y\frac{dy}{dx}-3\cos x=0.
\]

Collect:

\[
-2x\frac{dy}{dx}+2y\frac{dy}{dx}
=
-2x+2y+3\cos x.
\]

\[
\frac{dy}{dx}(-2x+2y)= -2x+2y+3\cos x.
\]

\[
\boxed{
\frac{dy}{dx}
=
\frac{-2x+2y+3\cos x}{-2x+2y}.
}
\]

## Core Theory 9: Second Derivative, Concavity and Inflection

\[
\frac{d^2y}{dx^2}
\]

tells us how the gradient is changing.

\[
\frac{d^2y}{dx^2}<0\Rightarrow\text{concave}
\]

\[
\frac{d^2y}{dx^2}>0\Rightarrow\text{convex}
\]

A point of inflection occurs where the curve changes concavity. \(\frac{d^2y}{dx^2}=0\) is a clue, but the sign change must be checked.

[VISUAL PLACEHOLDER: A21DifferentiationSVG-003 | Source: Chapter 9 second derivative evidence | Insert from svg/A21DifferentiationSVG-003.svg | Purpose: Show concavity and inflection.]

Example:

\[
y=x^3-2x^2-4x+5.
\]

\[
\frac{dy}{dx}=3x^2-4x-4.
\]

\[
\frac{d^2y}{dx^2}=6x-4.
\]

Convex:

\[
6x-4>0\Rightarrow x>\frac23.
\]

Inflection:

\[
6x-4=0\Rightarrow x=\frac23.
\]

\[
y=\left(\frac23\right)^3-2\left(\frac23\right)^2-4\left(\frac23\right)+5
=
\frac{47}{27}.
\]

\[
\boxed{x>\frac23,\qquad \left(\frac23,\frac{47}{27}\right).}
\]

## Core Theory 10: Connected Rates

Connected rates are chain rule in context.

\[
\boxed{\frac{dA}{dt}=\frac{dA}{dr}\frac{dr}{dt}}
\]

[INTERACTIVE PLACEHOLDER: A21DifferentiationWidget-001 | Source: Connected rates transcript | Insert from widgets/A21DifferentiationWidget-001.html | Purpose: Build connected-rate chains.]

[VISUAL PLACEHOLDER: A21DifferentiationSVG-005 | Source: Chapter 9 connected rates evidence | Insert from svg/A21DifferentiationSVG-005.svg | Purpose: Show circle/cylinder connected rates.]

Example: expanding circle.

\[
A=\pi r^2,\qquad \frac{dr}{dt}=5.
\]

\[
\frac{dA}{dr}=2\pi r.
\]

\[
\frac{dA}{dt}=2\pi r\cdot5=10\pi r.
\]

At \(r=3\):

\[
\boxed{\frac{dA}{dt}=30\pi\approx94.2\text{ cm}^2\text{s}^{-1}.}
\]

Example: cylinder cross-section.

\[
A=\pi x^2,\qquad \frac{dA}{dt}=0.032.
\]

\[
\frac{dA}{dx}=2\pi x.
\]

\[
0.032=(2\pi x)\frac{dx}{dt}.
\]

\[
\frac{dx}{dt}=\frac{0.032}{2\pi x}.
\]

At \(x=2\):

\[
\boxed{\frac{dx}{dt}\approx0.00255\text{ cm s}^{-1}.}
\]

Example: cylinder volume.

\[
V=5\pi x^3.
\]

\[
\frac{dV}{dx}=15\pi x^2.
\]

\[
\frac{dV}{dt}=15\pi x^2\frac{dx}{dt}.
\]

At \(x=2\), \(\frac{dx}{dt}=0.00255\):

\[
\boxed{\frac{dV}{dt}\approx0.481\text{ cm}^3\text{s}^{-1}.}
\]

## Guided Practice 2: Rule Selection and Differentiation

Differentiate each function.

1. \[
y=(5x-2)^4.
\]

2. \[
y=e^{x^3}.
\]

3. \[
y=\ln(4x^2+1).
\]

4. \[
y=x^3\cos x.
\]

5. \[
y=\frac{x^2}{\sin x}.
\]

## Full Worked Solutions to Guided Practice 2

1. Let \(u=5x-2\):

\[
\boxed{\frac{dy}{dx}=20(5x-2)^3.}
\]

2. Let \(u=x^3\):

\[
\boxed{\frac{dy}{dx}=3x^2e^{x^3}.}
\]

3. Let \(u=4x^2+1\):

\[
\boxed{\frac{dy}{dx}=\frac{8x}{4x^2+1}.}
\]

4. Product rule:

\[
\boxed{\frac{dy}{dx}=3x^2\cos x-x^3\sin x.}
\]

5. Quotient rule:

\[
\boxed{
\frac{dy}{dx}
=
\frac{2x\sin x-x^2\cos x}{\sin^2x}.
}
\]

## Guided Practice 3: Later Chapter Skills

1. Differentiate \(y=\tan4x\).
2. Differentiate \(y=\sec^2(3x)\).
3. Differentiate \(y=\frac{\cot x}{x}\).
4. For \(x=t^2+1,\ y=t^3-2t\), find \(\frac{dy}{dx}\) and the gradient at \(t=1\).
5. Find \(\frac{dy}{dx}\) for \(x^2+xy+y^2=7\).
6. For \(y=x^3-6x^2+9x+1\), find where the curve is convex and its point of inflection.
7. A sphere has volume \(V=\frac43\pi r^3\). Its radius increases at \(2\text{ cm s}^{-1}\). Find \(\frac{dV}{dt}\) when \(r=5\text{ cm}\).

## Full Worked Solutions to Guided Practice 3

1. \[
\boxed{\frac{dy}{dx}=4\sec^2(4x).}
\]

2. \[
\boxed{\frac{dy}{dx}=6\sec^2(3x)\tan(3x).}
\]

3. \[
\boxed{\frac{dy}{dx}=\frac{-x\cosec^2x-\cot x}{x^2}.}
\]

4. \[
\frac{dx}{dt}=2t,\qquad \frac{dy}{dt}=3t^2-2.
\]

\[
\boxed{\frac{dy}{dx}=\frac{3t^2-2}{2t}.}
\]

At \(t=1\):

\[
\boxed{\frac12.}
\]

5. \[
2x+\left(x\frac{dy}{dx}+y\right)+2y\frac{dy}{dx}=0.
\]

\[
\frac{dy}{dx}(x+2y)=-(2x+y).
\]

\[
\boxed{\frac{dy}{dx}=-\frac{2x+y}{x+2y}.}
\]

6. \[
\frac{dy}{dx}=3x^2-12x+9.
\]

\[
\frac{d^2y}{dx^2}=6x-12.
\]

Convex:

\[
x>2.
\]

Point of inflection:

\[
x=2,\qquad y=3.
\]

\[
\boxed{x>2,\quad (2,3).}
\]

7. \[
\frac{dV}{dr}=4\pi r^2.
\]

\[
\frac{dV}{dt}=4\pi r^2\frac{dr}{dt}.
\]

At \(r=5\) and \(\frac{dr}{dt}=2\):

\[
\frac{dV}{dt}=4\pi(25)(2)=200\pi.
\]

\[
\boxed{200\pi\text{ cm}^3\text{s}^{-1}\approx628\text{ cm}^3\text{s}^{-1}.}
\]

## Common Mistakes and Exam Traps

1. Dropping \(\lim_{h\to0}\) too early.
2. Differentiating trig functions in degrees.
3. Changing the argument of a trig function.
4. Forgetting \(\frac{d}{dx}(\cos x)=-\sin x\).
5. Forgetting the chain-rule multiplier.
6. Thinking \(\ln(kx)\) differentiates to \(\frac1{kx}\). It differentiates to \(\frac1x\).
7. Multiplying derivatives instead of using product rule.
8. Reversing the quotient-rule numerator.
9. Cancelling inside arguments like \(\cosec2x\).
10. Treating inverse trig derivatives as core content.
11. Forgetting \(\frac{dy}{dx}\) in implicit differentiation.
12. Reversing \(\frac{dy/dt}{dx/dt}\) in parametric differentiation.
13. Thinking every point of inflection is stationary.
14. Omitting units in connected rates.

## Exam Technique Notes

| Expression type | Likely method |
|---|---|
| \(e^{kx}\), \(\sin(kx)\), \(\cos(kx)\), \(\tan(kx)\) | Standard rule plus chain multiplier |
| \((\text{inside})^n\) | Chain rule |
| \(u(x)v(x)\) | Product rule |
| \(\frac{u(x)}{v(x)}\) | Quotient rule |
| \(x=f(t), y=g(t)\) | Parametric differentiation |
| \(x\) and \(y\) mixed together | Implicit differentiation |
| Rate of change in context | Connected rates |

For tangents and normals:

\[
m_{\text{normal}}=-\frac1{m_{\text{tangent}}}.
\]

Then use:

\[
y-y_1=m(x-x_1).
\]

For connected rates, write the derivative chain before substituting numbers and always include units.

## Common CCEA-Style Wording

| Wording | Meaning |
|---|---|
| Differentiate with respect to \(x\) | Find \(\frac{dy}{dx}\). |
| Find stationary points | Set \(\frac{dy}{dx}=0\), solve for \(x\), then find \(y\). |
| Equation of tangent | Use derivative gradient and point-line equation. |
| Equation of normal | Use negative reciprocal gradient. |
| Defined parametrically | Use \(\frac{dy}{dx}=\frac{dy/dt}{dx/dt}\). |
| Defined implicitly | Differentiate both sides and collect \(\frac{dy}{dx}\). |
| Point of inflection | Use \(\frac{d^2y}{dx^2}=0\) and check concavity changes. |

## Master Derivative Rule Table

| Function | Derivative |
|---|---|
| \(x^n\) | \(nx^{n-1}\) |
| \(\sin x\) | \(\cos x\) |
| \(\cos x\) | \(-\sin x\) |
| \(\tan x\) | \(\sec^2x\) |
| \(\sin(kx)\) | \(k\cos(kx)\) |
| \(\cos(kx)\) | \(-k\sin(kx)\) |
| \(\tan(kx)\) | \(k\sec^2(kx)\) |
| \(e^x\) | \(e^x\) |
| \(e^{kx}\) | \(ke^{kx}\) |
| \(a^x\) | \(\ln(a)a^x\) |
| \(a^{kx}\) | \(k\ln(a)a^{kx}\) |
| \(\ln x\) | \(\frac1x\) |
| \(\ln(kx)\) | \(\frac1x\) |
| \(\sec x\) | \(\sec x\tan x\) |
| \(\cosec x\) | \(-\cosec x\cot x\) |
| \(\cot x\) | \(-\cosec^2x\) |

## Syllabus Gap Check

| LO ID | Status |
|---|---|
| A21-DIFF-LO001 | Covered |
| A21-DIFF-LO002 | Covered |
| A21-DIFF-LO003 | Covered |
| A21-DIFF-LO004 | Covered |
| A21-DIFF-LO005 | Partially covered: connected rates included; full differential-equation construction logged as partial evidence. |

## Off-Spec Content Found but Excluded

| Evidence item | Decision |
|---|---|
| Inverse trig differentiation | Excluded from core standard CCEA Mathematics lesson. |
| STEP/MAT/UKMT extension material | Excluded from core. |
| Full separable differential-equation solving | Excluded from this Differentiation lesson core; more natural in Integration. |
| GCSE bridge-source teaching | Excluded, as requested. |

## Visual and Interactive Asset Plan

### Mermaid assets

- `mermaid/A21DifferentiationMermaid-001.md`
- `mermaid/A21DifferentiationMermaid-002.md`
- `mermaid/A21DifferentiationMermaid-003.md`
- `mermaid/A21DifferentiationMermaid-004.md`

### SVG assets

- `svg/A21DifferentiationSVG-001.svg`
- `svg/A21DifferentiationSVG-002.svg`
- `svg/A21DifferentiationSVG-003.svg`
- `svg/A21DifferentiationSVG-004.svg`
- `svg/A21DifferentiationSVG-005.svg`

### TikZ assets

- `tikz/A21DifferentiationTikZ-001.tex`
- `tikz/A21DifferentiationTikZ-002.tex`
- `tikz/A21DifferentiationTikZ-003.tex`
- `tikz/A21DifferentiationTikZ-004.tex`

### Widget assets

- `widgets/A21DifferentiationWidget-001.html`
- `widgets/A21DifferentiationWidget-002.html`
- `widgets/A21DifferentiationWidget-003.html`
- `widgets/A21DifferentiationWidget-004.html`

## Supplementary Sources Used

| Source | Status |
|---|---|
| CCEA GCE Mathematics specification map | Core authority. |
| Generic project module map | Project convention source. |
| Project evidence checklist | Project convention source. |
| Chapter 9 teacher transcript | Core lesson evidence. |
| P2 Chapter 9 Differentiation slide PDF | Core lesson evidence where on-spec. |
| Screenshots PDF | Visual evidence only. |
| DrFrost/Pearson labels | Cross-board support only where content matches CCEA A21 Differentiation. |

## Final Student Checklist

- [ ] I can reproduce the first-principles proof for \(\frac{d}{dx}(\sin x)=\cos x\).
- [ ] I know why trig differentiation uses radians.
- [ ] I can differentiate trig, exponential and logarithmic functions.
- [ ] I can use chain, product and quotient rules.
- [ ] I can differentiate \(\tan x\), \(\sec x\), \(\cosec x\) and \(\cot x\).
- [ ] I can solve stationary-point problems.
- [ ] I can differentiate parametrically.
- [ ] I can differentiate implicitly.
- [ ] I can use the second derivative for concavity and inflection.
- [ ] I can solve connected rates problems with units.
- [ ] I know inverse trig derivatives are not treated as core content here.

## Final Quality Check

| Check | Result |
|---|---|
| Unit prefix correct | Passed: A21 |
| Topic identity correct | Passed: A21-DIFF |
| LO IDs preserved exactly | Passed |
| On-spec evidence covered | Passed with A21-DIFF-LO005 caveat |
| Off-spec material excluded | Passed |
| Placeholders match generated files | Passed |
| Manifest and source reference included | Passed |
| Unresolved issues | A21-DIFF-LO005 remains partially evidenced until direct material on constructing simple differential equations is supplied. |
