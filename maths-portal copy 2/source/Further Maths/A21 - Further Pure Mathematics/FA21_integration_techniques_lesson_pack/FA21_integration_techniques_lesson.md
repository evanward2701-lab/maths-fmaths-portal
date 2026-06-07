# FA21 Further Calculus: Integration Techniques and Reduction Formulae

## 1. Lesson Title and Metadata

| Metadata field | Value |
|---|---|
| Date generated | 2026-06-05 |
| Course | CCEA GCE Further Mathematics |
| Unit | `FA21` Further A2 1 Pure Mathematics |
| Applied section | Not applicable, Pure Mathematics |
| Topic code | `FA21-FCALC` |
| Topic name | Further calculus: Integration techniques |
| Topic slug | `integration_techniques` |
| Topic Pascal | `IntegrationTechniques` |
| Topic ID | `FA21IntegrationTechniques` |
| Lesson file | `FA21_integration_techniques_lesson.md` |
| Core LO IDs | `FA21-FCALC-LO005`, `FA21-FCALC-LO006` |
| Supporting synoptic LO ID | `FA21-HYP-LO002` |
| Bridge tags | `AS1 Integration`, `A21 Integration`, `A21 Trigonometry`, `A21 Sequences and Series`, `A21 Volume of Revolution`, `A21 Parametric Equations` |
| Topic tags | `#FA21`, `#FCALC`, `#FurtherCalculus`, `#Integration`, `#ReductionFormulae`, `#IntegrationByParts`, `#RecurrenceRelations`, `#TrigIdentities`, `#ExactWorking` |

**Student-facing title:** Integration Techniques: turning long integrals into recurrence machines.

The central idea is that instead of grinding through an integral repeatedly, we define a family of integrals \(I_n\), then build a relationship between \(I_n\) and an earlier member such as \(I_{n-1}\) or \(I_{n-2}\). The algebra becomes a staircase. Step down enough times and the difficult integral becomes a base case.

## 2. Evidence Map

| Evidence source | Used for | Notes |
|---|---|---|
| CCEA Further Mathematics Specification Map | Topic boundary, LO IDs, official wording | Authority for the lesson. |
| Further Maths README module map | Naming conventions, file structure, phase workflow | Project-level authority. |
| Further Maths Evidence Drop Checklist | Evidence logs and off-spec/boundary-risk handling | Project-level authority. |
| `transcripts.md` | Reduction formula theory, non-trig examples, trig examples, teacher warnings, exam-style method notes | Main lesson-specific evidence. |
| `Chapter_6_Integration_Techniques_(A2)_♾️_(Further_Pure_2)_screenshots.pdf` | Visual overview of FP2 Chapter 6 and handwritten working style | Text was not parsed; visible screenshots used only where inspected. |
| Ordinary A-Level Maths bridge extracts | Bridge context | Bridge only, not Further Maths authority. |
| CCEA ordinary Mathematics Specification Map | Ordinary integration and trig foundations | Bridge only. |

**Visual evidence limitation:** the screenshot PDF contains 150 pages, but no text could be parsed from it. The visible rendered pages confirm the chapter heading, exercise structure and several handwritten derivations, but this lesson does not claim uninspected visual details from all pages.

## 3. Specification Alignment

| LO ID | Official wording | Lesson coverage | Evidence source | Syllabus boundary | Ordinary A-Level Maths bridge |
|---|---|---|---|---|---|
| `FA21-FCALC-LO005` | use repeated integration by parts | Students derive reduction formulae by selecting \(u\) and \(v'\), applying integration by parts, then rewriting the new integral as \(I_{n-1}\) or \(I_{n-2}\). | CCEA Further Maths map; transcript Ex 6A | Core | A21 Integration by parts |
| `FA21-FCALC-LO006` | demonstrate understanding of and use simple reduction formulae in integration | Students define \(I_n\), prove formulae, apply recurrence chains, compute base cases and use exact values. | CCEA Further Maths map; transcript Ex 6A | Core | A21 Sequences and Series, A21 Integration |
| `FA21-HYP-LO002` | differentiate and integrate hyperbolic functions | Used only when the transcript uses \(\tanh x\), \(\operatorname{sech}^2x\), \(\cosh x\), and related formulae in reduction examples. | CCEA Further Maths map; transcript trig/hyperbolic section | Supporting | A21 exponentials/logarithms and calculus |

## 4. Learning Objectives

### Core Further Maths objectives

By the end of this lesson, you should be able to:

1. Define an indexed integral such as \(I_n=\int x^n e^x\,dx\) or \(I_n=\int_0^{\pi/2}\sin^n x\,dx\).
2. Use repeated integration by parts to derive a reduction formula.
3. Recognise when a new integral is exactly \(I_{n-1}\), \(I_{n-2}\), or another earlier term.
4. Rearrange formulae containing \(I_n\) on both sides.
5. Apply a reduction formula repeatedly to compute a required integral.
6. Use base cases such as \(I_0=\int e^x\,dx=e^x\), \(I_0=\int1\,dx=x\), or \(I_0=\int_0^{\pi/2}1\,dx=\frac{\pi}{2}\).
7. Use trig identities such as \(\cos^2x=1-\sin^2x\) and \(\tan^2x=\sec^2x-1\) to reshape integrals into recurrence form.

### Bridge objectives

Connect this lesson back to integration by parts, integration by substitution and reverse chain rule, trigonometric identities and exact values, recurrence relations, sequence notation and definite integral evaluation.

### Exam technique objectives

Avoid shortcut methods when the question asks you to prove or use a reduction formula; write \(I_n\), \(I_{n-1}\), \(I_{n-2}\) clearly; show enough algebra when collecting \(I_n\)-terms; treat \(n\) as a constant with respect to \(x\); use exact values.

## 5. Explicit Prerequisite Recap

### GCSE foundations

| Foundation | Why it matters here |
|---|---|
| Algebraic factorisation | Pulling constants such as \(n\), \(\frac23 n\), and \(n-1\) outside integrals |
| Index laws | Splitting powers such as \(\sin^n x=\sin^{n-1}x\sin x\) |
| Surds and exact values | Keeping exact forms instead of decimals |
| Rearranging equations | Making \(I_n\) the subject when \(I_n\) appears on both sides |

### Ordinary AS/A2 Mathematics foundations

| Ordinary topic | Required skill | Used here as |
|---|---|---|
| AS1 Integration | Reverse differentiation, definite integrals | Base cases and exact evaluation |
| A21 Integration | Integration by parts and substitution | Main derivation engine |
| A21 Trigonometry | Identities and exact values | Reshaping trig powers |
| A21 Sequences and Series | Recurrence notation | Understanding \(I_n\to I_{n-1}\to I_{n-2}\) |
| A21 Parametric Equations / Volume of Revolution | Curves and rotation context | Bridge only because arc length/surface area are not confirmed as CCEA core here |

### A-Level Maths Bridge: What You Already Know and What Further Maths Changes

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| A21 Integration | Use integration by parts: \(\int u v'\,dx=uv-\int u'v\,dx\) | Use integration by parts not merely to integrate, but to manufacture a recurrence formula | A shortcut answer may miss the required proof |
| A21 Integration | Use substitution and reverse chain rule | Use reverse chain rule as a support step inside a reduction proof | Students may integrate too soon instead of preserving \(I_n\)-structure |
| A21 Trigonometry | Use identities such as \(\sin^2x+\cos^2x=1\) | Convert unwanted trig powers into earlier indexed integrals | Wrong identity choice can create a dead end |
| A21 Sequences and Series | Use recurrence-style notation | Treat \(I_n\) as a sequence of integrals | Forgetting base cases makes the recurrence unusable |
| AS1 Integration | Evaluate definite integrals | Apply limits to the non-recursive boundary term | Endpoint values often make the boundary term vanish, but only after checking |

In ordinary A-Level Maths, this idea appeared as integration by parts: choose \(u\), choose \(v'\), then integrate. In Further Maths, the same idea becomes a formula-producing machine. You are not just trying to get the answer. You are trying to turn an integral with power \(n\) into an earlier integral. The key upgrade is recognising structure: \(I_n\to I_{n-1}\) or \(I_n\to I_{n-2}\). The danger is that ordinary Maths habits can be too direct.

## 6. Big Picture Explanation

Some integrals are not hard because the idea is impossible. They are hard because the calculation is long. For example, \(\int x^7e^x\,dx\) can be handled by repeated integration by parts. Each time integration by parts is used, the polynomial power decreases by one:
\[
x^7e^x\to x^6e^x\to x^5e^x\to x^4e^x\to\cdots
\]
The clever move is to define \(I_n=\int x^n e^x\,dx\), derive \(I_n=x^ne^x-nI_{n-1}\), then calculate by the chain \(I_4\to I_3\to I_2\to I_1\to I_0\).

## 7. Key Definitions and Notation

### Indexed integral

An indexed integral is a family of integrals labelled by an integer \(n\). Example: \(I_n=\int x^n e^x\,dx\). Here \(I_{n-1}=\int x^{n-1}e^x\,dx\) and \(I_{n-2}=\int x^{n-2}e^x\,dx\), where defined.

### Reduction formula

A reduction formula writes \(I_n\) in terms of an earlier integral, for example:
\[
I_n=x^ne^x-nI_{n-1},\qquad I_n=\frac{2n}{2n+3}I_{n-1},\qquad I_n=-\frac1n\sin^{n-1}x\cos x+\frac{n-1}{n}I_{n-2}.
\]

### Integration by parts

\[
\int u\,v'\,dx=uv-\int u'v\,dx.
\]

### Base case

A base case is the integral where the recurrence stops:
\[
I_0=\int e^x\,dx=e^x,\quad I_0=\int1\,dx=x,\quad I_0=\int_0^{\pi/2}1\,dx=\frac\pi2,\quad I_1=\int_0^{\pi/2}\sin x\,dx=1.
\]

### Treating \(n\) correctly

In \(\int nx^{n-1}e^x\,dx\), \(n\) is constant with respect to \(x\), so \(\int nx^{n-1}e^x\,dx=n\int x^{n-1}e^x\,dx\).

## 8. Core Theory

### 8.1 Non-trig reduction formula: \(I_n=\int x^n e^x\,dx\)

Let
\[
I_n=\int x^ne^x\,dx,\qquad n\in\mathbb Z^+.
\]
Use integration by parts. Choose \(u=x^n\), \(v'=e^x\). Then \(u'=nx^{n-1}\), \(v=e^x\). Hence
\[
I_n=x^ne^x-\int nx^{n-1}e^x\,dx=x^ne^x-n\int x^{n-1}e^x\,dx.
\]
But \(I_{n-1}=\int x^{n-1}e^x\,dx\). Therefore
\[
\boxed{I_n=x^ne^x-nI_{n-1}}.
\]

### 8.2 Using the formula to find \(\int x^4e^x\,dx\)

Base case:
\[
I_0=\int x^0e^x\,dx=\int e^x\,dx=e^x.
\]
Then
\[
I_1=xe^x-I_0=xe^x-e^x.
\]
\[
I_2=x^2e^x-2I_1=x^2e^x-2(xe^x-e^x)=x^2e^x-2xe^x+2e^x.
\]
\[
I_3=x^3e^x-3I_2=x^3e^x-3(x^2e^x-2xe^x+2e^x)=x^3e^x-3x^2e^x+6xe^x-6e^x.
\]
\[
I_4=x^4e^x-4I_3=x^4e^x-4(x^3e^x-3x^2e^x+6xe^x-6e^x).
\]
Therefore
\[
\boxed{\int x^4e^x\,dx=x^4e^x-4x^3e^x+12x^2e^x-24xe^x+24e^x+C.}
\]

### 8.3 Definite reduction formula: \(I_n=\int_0^1x^n\sqrt{1-x}\,dx\)

Let
\[
I_n=\int_0^1x^n(1-x)^{1/2}\,dx.
\]
Choose \(u=x^n\), \(v'=(1-x)^{1/2}\). Then \(u'=nx^{n-1}\) and \(v=-\frac23(1-x)^{3/2}\). Thus
\[
I_n=\left[-\frac23x^n(1-x)^{3/2}\right]_0^1+\frac23n\int_0^1x^{n-1}(1-x)^{3/2}\,dx.
\]
The boundary term is zero. Now
\[
(1-x)^{3/2}=(1-x)^{1/2}(1-x),
\]
so
\[
I_n=\frac23n\int_0^1x^{n-1}(1-x)^{1/2}(1-x)\,dx.
\]
Expand:
\[
I_n=\frac23n\int_0^1x^{n-1}(1-x)^{1/2}\,dx-\frac23n\int_0^1x^n(1-x)^{1/2}\,dx.
\]
Recognise \(I_{n-1}\) and \(I_n\):
\[
I_n=\frac23nI_{n-1}-\frac23nI_n.
\]
Collect terms:
\[
I_n+\frac23nI_n=\frac23nI_{n-1},\qquad I_n\left(\frac{2n+3}{3}\right)=\frac{2n}{3}I_{n-1}.
\]
Therefore
\[
\boxed{I_n=\frac{2n}{2n+3}I_{n-1}},\qquad n\ge1.
\]

### 8.4 Trig reduction formula: \(I_n=\int\sin^n x\,dx\)

Let \(I_n=\int\sin^n x\,dx\). Split
\[
\sin^nx=\sin^{n-1}x\sin x.
\]
Choose \(u=\sin^{n-1}x\), \(v'=\sin x\). Then
\[
u'=(n-1)\sin^{n-2}x\cos x,\qquad v=-\cos x.
\]
Integration by parts gives
\[
I_n=-\cos x\sin^{n-1}x+(n-1)\int\sin^{n-2}x\cos^2x\,dx.
\]
Use \(\cos^2x=1-\sin^2x\):
\[
I_n=-\cos x\sin^{n-1}x+(n-1)\int\sin^{n-2}x\,dx-(n-1)\int\sin^nx\,dx.
\]
So
\[
I_n=-\cos x\sin^{n-1}x+(n-1)I_{n-2}-(n-1)I_n.
\]
Collect:
\[
nI_n=-\cos x\sin^{n-1}x+(n-1)I_{n-2}.
\]
Hence
\[
\boxed{I_n=-\frac1n\sin^{n-1}x\cos x+\frac{n-1}{n}I_{n-2}}.
\]

For \(I_4\):
\[
I_4=-\frac14\sin^3x\cos x+\frac34I_2,\qquad I_2=-\frac12\sin x\cos x+\frac12I_0,\qquad I_0=x.
\]
Therefore
\[
\boxed{\int\sin^4x\,dx=-\frac14\sin^3x\cos x-\frac38\sin x\cos x+\frac38x+C.}
\]

### 8.5 Definite sine-power recurrence

Let
\[
I_n=\int_0^{\pi/2}\sin^n x\,dx.
\]
Using the previous formula,
\[
I_n=\left[-\frac1n\sin^{n-1}x\cos x\right]_0^{\pi/2}+\frac{n-1}{n}I_{n-2}.
\]
At \(x=\frac\pi2\), \(\cos\frac\pi2=0\). At \(x=0\), \(\sin0=0\). Hence the boundary term is \(0-0=0\). Therefore
\[
\boxed{I_n=\frac{n-1}{n}I_{n-2}},\qquad \boxed{nI_n=(n-1)I_{n-2}}.
\]
Then
\[
I_5=\frac45I_3=\frac45\cdot\frac23I_1=\frac{8}{15},\qquad I_1=1.
\]
Also
\[
I_6=\frac56I_4=\frac56\cdot\frac34I_2=\frac56\cdot\frac34\cdot\frac12I_0=\frac56\cdot\frac34\cdot\frac12\cdot\frac\pi2=\frac{5\pi}{32}.
\]

### 8.6 Tangent reduction formula

Let \(I_n=\int\tan^n x\,dx\). Split
\[
I_n=\int\tan^{n-2}x\tan^2x\,dx.
\]
Use \(\tan^2x=\sec^2x-1\):
\[
I_n=\int\sec^2x\tan^{n-2}x\,dx-\int\tan^{n-2}x\,dx.
\]
Since \(\frac d{dx}\tan x=\sec^2x\),
\[
\int\sec^2x\tan^{n-2}x\,dx=\frac{1}{n-1}\tan^{n-1}x.
\]
Thus
\[
\boxed{I_n=\frac{1}{n-1}\tan^{n-1}x-I_{n-2}},\qquad n\ge2.
\]

### 8.7 Hyperbolic reduction formula and method of differences

Let
\[
I_n=\int_0^{\ln2}\tanh^n x\,dx.
\]
Use \(\tanh^2x=1-\operatorname{sech}^2x\):
\[
I_n=\int_0^{\ln2}\tanh^{n-2}x\,dx-\int_0^{\ln2}\operatorname{sech}^2x\tanh^{n-2}x\,dx.
\]
Since \(\frac d{dx}\tanh x=\operatorname{sech}^2x\),
\[
I_n=I_{n-2}-\left[\frac{1}{n-1}\tanh^{n-1}x\right]_0^{\ln2}.
\]
Using \(\tanh(\ln2)=\frac35\) and \(\tanh0=0\),
\[
\boxed{I_n=I_{n-2}-\frac{1}{n-1}\left(\frac35\right)^{n-1}}.
\]
Rearrange:
\[
\frac{1}{n-1}\left(\frac35\right)^{n-1}=I_{n-2}-I_n.
\]
Set \(n-1=2r\), so \(n=2r+1\):
\[
\frac{1}{2r}\left(\frac35\right)^{2r}=I_{2r-1}-I_{2r+1}.
\]
Then
\[
\sum_{r=1}^{k}\frac{1}{2r}\left(\frac35\right)^{2r}=(I_1-I_3)+(I_3-I_5)+\cdots+(I_{2k-1}-I_{2k+1})=I_1-I_{2k+1}.
\]
Given \(\lim_{n\to\infty}I_n=0\),
\[
\sum_{r=1}^{\infty}\frac{1}{2r}\left(\frac35\right)^{2r}=I_1.
\]
Now
\[
I_1=\int_0^{\ln2}\tanh x\,dx=[\ln(\cosh x)]_0^{\ln2}=\ln\left(\frac54\right)-\ln1=\ln\left(\frac54\right).
\]
Therefore
\[
\boxed{\sum_{r=1}^{\infty}\frac{1}{2r}\left(\frac35\right)^{2r}=\ln\left(\frac54\right)}.
\]

### 8.8 Extra trig identity example

Let
\[
I_n=\int\frac{\sin nx}{\sin x}\,dx.
\]
Then
\[
I_{n+2}-I_n=\int\frac{\sin((n+2)x)-\sin(nx)}{\sin x}\,dx.
\]
Use
\[
\sin A-\sin B=2\cos\left(\frac{A+B}{2}\right)\sin\left(\frac{A-B}{2}\right).
\]
With \(A=(n+2)x\), \(B=nx\), this gives
\[
\sin((n+2)x)-\sin(nx)=2\cos((n+1)x)\sin x.
\]
Hence
\[
I_{n+2}-I_n=\int2\cos((n+1)x)\,dx=\boxed{\frac{2\sin((n+1)x)}{n+1}}.
\]
For \(I_6\), use
\[
I_6=\frac{2\sin5x}{5}+\frac{2\sin3x}{3}+2\sin x+I_0,
\]
where \(I_0=0\). Therefore
\[
\int_{\pi/4}^{\pi/3}\frac{\sin6x}{\sin x}\,dx=\left[\frac{2\sin5x}{5}+\frac{2\sin3x}{3}+2\sin x\right]_{\pi/4}^{\pi/3}=\boxed{\frac1{15}(12\sqrt3-17\sqrt2)}.
\]

### 8.9 Cosecant reduction formula

Let \(I_n=\int\cosec^n x\,dx\). Split
\[
I_n=\int\cosec^{n-2}x\cosec^2x\,dx.
\]
Choose \(u=\cosec^{n-2}x\), \(v'=\cosec^2x\). Then
\[
v=-\cot x,\qquad u'=-(n-2)\cosec^{n-2}x\cot x.
\]
So
\[
I_n=-\cot x\cosec^{n-2}x-(n-2)\int\cosec^{n-2}x\cot^2x\,dx.
\]
Use \(\cot^2x=\cosec^2x-1\):
\[
I_n=-\cot x\cosec^{n-2}x-(n-2)\int(\cosec^nx-\cosec^{n-2}x)\,dx.
\]
Thus
\[
I_n=-\cot x\cosec^{n-2}x-(n-2)I_n+(n-2)I_{n-2}.
\]
Collect:
\[
(n-1)I_n=-\cot x\cosec^{n-2}x+(n-2)I_{n-2}.
\]
Therefore
\[
\boxed{I_n=\frac{n-2}{n-1}I_{n-2}-\frac{\cot x\cosec^{n-2}x}{n-1}}.
\]

## 9. Visual Asset Integration

[VISUAL PLACEHOLDER: FA21IntegrationTechniquesMermaid-001 | Source: CCEA Further Mathematics specification boundary + transcript reduction formula examples | Insert from mermaid/FA21IntegrationTechniquesMermaid-001.md | Purpose: Show the decision process for choosing between integration by parts, trig identity reshaping, reverse chain rule, and recurrence substitution.]

[VISUAL PLACEHOLDER: FA21IntegrationTechniquesSVG-001 | Source: Transcript examples for \(I_n=\int x^n e^x\,dx\), \(I_n=\int\sin^n x\,dx\), and definite trig reduction formulae | Insert from svg/FA21IntegrationTechniquesSVG-001.svg | Purpose: Visualise reduction formulae as a staircase from \(I_n\) down to a base case.]

[VISUAL PLACEHOLDER: FA21IntegrationTechniquesSVG-002 | Source: AI-proposed teaching enhancement based on transcript integration by parts examples | Insert from svg/FA21IntegrationTechniquesSVG-002.svg | Purpose: Show how the choice of \(u\) and \(v'\) is made to create an earlier indexed integral.]

[VISUAL PLACEHOLDER: FA21IntegrationTechniquesBridgeSVG-001 | Source: Ordinary A-Level Maths bridge + Further Maths specification | Insert from svg/FA21IntegrationTechniquesBridgeSVG-001.svg | Purpose: Compare ordinary A-Level integration by parts with Further Maths reduction formula derivation.]

[VISUAL PLACEHOLDER: FA21IntegrationTechniquesTikZ-001 | Source: Transcript examples for \(I_4=\int x^4e^x\,dx\), \(I_5\), and \(I_6\) | Insert from tikz/FA21IntegrationTechniquesTikZ-001.tex | Purpose: Provide a precise mathematical recurrence diagram for printed notes.]

## 10. Interactive Learning Widgets

[INTERACTIVE PLACEHOLDER: FA21IntegrationTechniquesWidget-001 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FA21IntegrationTechniquesWidget-001.html | Purpose: Let students step through a recurrence chain such as \(I_n=\frac{n-1}{n}I_{n-2}\) and identify the required base case.]

[INTERACTIVE PLACEHOLDER: FA21IntegrationTechniquesWidget-002 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FA21IntegrationTechniquesWidget-002.html | Purpose: Help students choose \(u\) and \(v'\) so that the resulting integral becomes \(I_{n-1}\), \(I_{n-2}\), or \(I_n\).]

## 11. Worked Examples

### Worked Example 1: Deriving and using \(I_n=\int x^ne^x\,dx\)

Given \(I_n=\int x^ne^x\,dx\), show \(I_n=x^ne^x-nI_{n-1}\), hence find \(\int x^4e^x\,dx\).

Solution follows Section 8.1 and 8.2 exactly:
\[
I_n=x^ne^x-\int nx^{n-1}e^x\,dx=x^ne^x-nI_{n-1}.
\]
Then
\[
I_0=e^x,
\]
\[
I_1=xe^x-e^x,
\]
\[
I_2=x^2e^x-2xe^x+2e^x,
\]
\[
I_3=x^3e^x-3x^2e^x+6xe^x-6e^x,
\]
\[
I_4=x^4e^x-4x^3e^x+12x^2e^x-24xe^x+24e^x.
\]
Thus
\[
\boxed{\int x^4e^x\,dx=x^4e^x-4x^3e^x+12x^2e^x-24xe^x+24e^x+C.}
\]

### Worked Example 2: Definite reduction formula with \(\sqrt{1-x}\)

Show that if \(I_n=\int_0^1x^n\sqrt{1-x}\,dx\), then \(I_n=\frac{2n}{2n+3}I_{n-1}\). The detailed derivation is the one in Section 8.3. The essential steps are:
\[
I_n=\frac23n\int_0^1x^{n-1}(1-x)^{3/2}\,dx,
\]
\[
(1-x)^{3/2}=(1-x)^{1/2}(1-x),
\]
\[
I_n=\frac23nI_{n-1}-\frac23nI_n,
\]
\[
\boxed{I_n=\frac{2n}{2n+3}I_{n-1}}.
\]

### Worked Example 3: Trig reduction formula for \(\int\sin^nx\,dx\)

Show that
\[
\boxed{I_n=-\frac1n\sin^{n-1}x\cos x+\frac{n-1}{n}I_{n-2}}.
\]
The full derivation is in Section 8.4. The key moment is using \(\cos^2x=1-\sin^2x\), giving both \(I_{n-2}\) and \(I_n\).

Hence
\[
\boxed{\int\sin^4x\,dx=-\frac14\sin^3x\cos x-\frac38\sin x\cos x+\frac38x+C.}
\]

### Worked Example 4: Definite trig reduction formula and values of \(I_5\), \(I_6\)

For \(I_n=\int_0^{\pi/2}\sin^nx\,dx\),
\[
\boxed{I_n=\frac{n-1}{n}I_{n-2}}.
\]
Then
\[
\boxed{I_5=\frac{8}{15}},\qquad \boxed{I_6=\frac{5\pi}{32}}.
\]

### Worked Example 5: Reduction formula for \(\int\tan^nx\,dx\)

\[
I_n=\int\tan^{n-2}x(\sec^2x-1)\,dx=\frac{1}{n-1}\tan^{n-1}x-I_{n-2}.
\]

### Worked Example 6: Hyperbolic reduction formula and method of differences

\[
I_n=I_{n-2}-\frac{1}{n-1}\left(\frac35\right)^{n-1},
\]
which leads to
\[
\sum_{r=1}^{\infty}\frac{1}{2r}\left(\frac35\right)^{2r}=\ln\left(\frac54\right).
\]

### Worked Example 7: Extra trig identity reduction using \(\frac{\sin nx}{\sin x}\)

\[
I_{n+2}-I_n=\frac{2\sin((n+1)x)}{n+1}.
\]
Therefore
\[
\boxed{\int_{\pi/4}^{\pi/3}\frac{\sin6x}{\sin x}\,dx=\frac1{15}(12\sqrt3-17\sqrt2)}.
\]

### Worked Example 8: Cosecant reduction formula

\[
\boxed{I_n=\frac{n-2}{n-1}I_{n-2}-\frac{\cot x\cosec^{n-2}x}{n-1}}.
\]

## 12. Common Mistakes and Exam Traps

1. Trying to just integrate when the question asks for a reduction formula.
2. Forgetting that \(n\) is constant with respect to \(x\).
3. Choosing \(u\) and \(v'\) without checking whether the target is \(I_{n-1}\), \(I_{n-2}\), or \(I_n\).
4. Losing the negative sign in \(\int\sin x\,dx=-\cos x\).
5. Forgetting to collect \(I_n\)-terms when they appear on both sides.
6. Confusing \(I_{n-1}\) and \(I_{n-2}\).
7. Using the wrong base case: odd sine chains end at \(I_1\), even sine chains end at \(I_0\).
8. Forgetting limits on the boundary term.
9. Mishandling trig identities.
10. Forgetting \(+C\) in indefinite integrals.
11. Calculator mode traps: exact trig values involving \(\pi\) require radian mode if checked numerically.
12. Boundary-risk trap: arc length and surface area appear in the evidence, but are excluded from the core CCEA lesson unless further CCEA evidence confirms them.

## 13. Practice Questions

1. Let \(I_n=\int x^ne^{2x}\,dx\). Use integration by parts to show \(I_n=\frac12x^ne^{2x}-\frac n2I_{n-1}\).
2. Given \(I_n=\int x^n\cos x\,dx\), use integration by parts once to express \(I_n\) in terms of an integral involving \(x^{n-1}\sin x\).
3. Let \(I_n=\int_0^{\pi/2}\cos^nx\,dx\). Write down the recurrence for \(I_n\), and state \(I_0\) and \(I_1\).
4. Explain why ordinary integration by parts alone is not enough for a “show that” reduction formula question.
5. For \(I_n=\int\sin^nx\,dx\), explain why \(\sin^nx=\sin^{n-1}x\sin x\) is useful.
6. Given \(I_n=x^ne^x-nI_{n-1}\), find \(\int x^3e^x\,dx\).
7. Use \(I_n=\frac{n-1}{n}I_{n-2}\) to find \(I_7\) and \(I_8\), where \(I_n=\int_0^{\pi/2}\sin^nx\,dx\).
8. Derive \(I_n=\frac{1}{n-1}\tan^{n-1}x-I_{n-2}\).
9. Let \(I_n=\int_0^1x^n(1-x)^2\,dx\). Derive a reduction formula in terms of \(I_{n-1}\).
10. Given the cosecant reduction formula, find \(\int\cosec^4x\,dx\).

## 14. Worked Solutions

### Solution 1

Choose \(u=x^n\), \(v'=e^{2x}\). Then \(u'=nx^{n-1}\), \(v=\frac12e^{2x}\). Hence
\[
I_n=\frac12x^ne^{2x}-\frac n2\int x^{n-1}e^{2x}\,dx=\boxed{\frac12x^ne^{2x}-\frac n2I_{n-1}}.
\]

### Solution 2

Choose \(u=x^n\), \(v'=\cos x\). Then \(u'=nx^{n-1}\), \(v=\sin x\). Therefore
\[
\boxed{I_n=x^n\sin x-n\int x^{n-1}\sin x\,dx}.
\]

### Solution 3

\[
\boxed{I_n=\frac{n-1}{n}I_{n-2}},\quad I_0=\frac\pi2,\,\quad I_1=1.
\]

### Solution 4

A reduction formula question asks for a general relationship involving \(n\), not a single final integral. For \(I_n=\int x^ne^x\,dx\), integration by parts gives \(I_n=x^ne^x-nI_{n-1}\). The Further Maths step is recognising the recurrence.

### Solution 5

The split \(\sin^nx=\sin^{n-1}x\sin x\) lets us choose \(u=\sin^{n-1}x\), \(v'=\sin x\). This produces \(\sin^{n-2}x\cos^2x\), and \(\cos^2x=1-\sin^2x\) creates both \(I_{n-2}\) and \(I_n\).

### Solution 6

\[
I_0=e^x,
\]
\[
I_1=xe^x-e^x,
\]
\[
I_2=x^2e^x-2xe^x+2e^x,
\]
\[
I_3=x^3e^x-3x^2e^x+6xe^x-6e^x.
\]
Thus
\[
\boxed{\int x^3e^x\,dx=x^3e^x-3x^2e^x+6xe^x-6e^x+C}.
\]

### Solution 7

\[
I_7=\frac67\cdot\frac45\cdot\frac23I_1=\frac67\cdot\frac45\cdot\frac23=\boxed{\frac{16}{35}}.
\]
\[
I_8=\frac78\cdot\frac56\cdot\frac34\cdot\frac12I_0=\frac78\cdot\frac56\cdot\frac34\cdot\frac12\cdot\frac\pi2=\boxed{\frac{35\pi}{256}}.
\]

### Solution 8

\[
I_n=\int\tan^{n-2}x(\sec^2x-1)\,dx=\int\sec^2x\tan^{n-2}x\,dx-I_{n-2}=\boxed{\frac{1}{n-1}\tan^{n-1}x-I_{n-2}}.
\]

### Solution 9

Let \(I_n=\int_0^1x^n(1-x)^2\,dx\). Choose \(u=x^n\), \(v'=(1-x)^2\). Then \(u'=nx^{n-1}\), \(v=-\frac13(1-x)^3\). Boundary terms vanish, so
\[
I_n=\frac n3\int_0^1x^{n-1}(1-x)^3\,dx.
\]
Use \((1-x)^3=(1-x)^2(1-x)\):
\[
I_n=\frac n3I_{n-1}-\frac n3I_n.
\]
Thus
\[
\boxed{I_n=\frac{n}{n+3}I_{n-1}}.
\]

### Solution 10

For \(n=4\),
\[
I_4=\frac23I_2-\frac13\cot x\cosec^2x.
\]
Since \(I_2=-\cot x\),
\[
\boxed{\int\cosec^4x\,dx=-\frac13\cot x\cosec^2x-\frac23\cot x+C}.
\]

## 15. Exam Technique Notes

For “show that” questions, define \(I_n\), state the method, choose \(u\) and \(v'\) where relevant, show \(u'\) and \(v\), apply the formula, rewrite the new integral as \(I_{n-1}\), \(I_{n-2}\), or \(I_n\), then rearrange.

For “hence find” questions, use the formula you have just proved. For definite integrals, write and evaluate the boundary term explicitly. Keep exact values and include \(+C\) only for indefinite integrals.

## 16. Syllabus Gap Check

| LO ID | Official wording | Covered? | Evidence strength | Notes |
|---|---|---:|---|---|
| `FA21-FCALC-LO005` | use repeated integration by parts | Yes | Strong | Core derivations repeatedly use integration by parts |
| `FA21-FCALC-LO006` | demonstrate understanding of and use simple reduction formulae in integration | Yes | Strong | Lesson defines \(I_n\), derives and applies reduction formulae |
| `FA21-HYP-LO002` | differentiate and integrate hyperbolic functions | Partly | Moderate | Used only in the hyperbolic reduction formula example |

### Off-Spec Content Found but Excluded

| Content found in evidence | Reason excluded from core | Notes |
|---|---|---|
| Arc Length of Curves, Ex 6B | Not confirmed in supplied CCEA Further Maths specification map for `FA21-FCALC` | The screenshot overview visibly includes Ex 6B, but CCEA boundary evidence is missing. |
| Surface Areas of Revolution, Ex 6C | Not confirmed in supplied CCEA Further Maths specification map for `FA21-FCALC` | The screenshot overview visibly includes Ex 6C, but CCEA boundary evidence is missing. |
| Polar arc length and polar surface area | Polar co-ordinates appear in Further Maths, but these specific techniques were not confirmed by the supplied CCEA map | Logged as boundary-risk enrichment. |

### Optional Enrichment Not Required by CCEA

Cartesian arc length, parametric arc length, surface area of revolution and polar arc length/surface-style results may be useful for a wider FP2-style library, but they should not be labelled as confirmed CCEA FA21 core unless further specification evidence is supplied.

## 17. Recommended Enhancements Not in the Evidence

Recommended enhancements include recurrence ladder diagrams, an integration-by-parts target map, a bridge visual comparing ordinary integration by parts with Further Maths recurrence building, a recurrence chain builder widget, an integration by parts choice checker widget, and extra examples such as \(I_n=\int x^n\sin x\,dx\) or \(I_n=\int_0^1x^n(1-x)^m\,dx\).

## 18. Supplementary Sources Used

Project Sources used: `CCEA_GCE_Further_Mathematics_Specification_Map.md`, `Further_Maths_README_module_map.md`, `Further_Maths_EVIDENCE_DROP_CHECKLIST.md`, `Further Maths Portal Build – Knowledge Evidence.txt`, `Ordinary_A_Level_Maths_Bridge_Spec_Extracts.md`, `CCEA_GCE_Mathematics_Specification_Map.md`.

Lesson-specific evidence used: `transcripts.md` and `Chapter_6_Integration_Techniques_(A2)_♾️_(Further_Pure_2)_screenshots.pdf`.

Ordinary A-Level Maths sources were used only as bridge context and not as Further Maths authority. No cross-board sources were deliberately used.

## 19. Final Student Checklist

### Prerequisite confidence checklist

- [ ] I can use \(\int uv'\,dx=uv-\int u'v\,dx\).
- [ ] I can differentiate \(x^n\), \(\sin^{n-1}x\), and \(\cosec^{n-2}x\).
- [ ] I can integrate \(e^x\), \(e^{2x}\), \(\sin x\), \(\cosec^2x\), and \(\sec^2x\).
- [ ] I can use \(\cos^2x=1-\sin^2x\), \(\tan^2x=\sec^2x-1\), and exact values at standard angles.

### Further Maths method checklist

- [ ] I can define an indexed integral \(I_n\).
- [ ] I can recognise \(I_{n-1}\) and \(I_{n-2}\) inside a calculation.
- [ ] I can derive and use the major reduction formulae in this lesson.
- [ ] I can decide whether an odd/even recurrence ends at \(I_1\) or \(I_0\).

### Exam technique checklist

- [ ] I can show the \(u\), \(u'\), \(v'\), \(v\) setup clearly.
- [ ] I can show and evaluate boundary terms.
- [ ] I can keep exact fractions and surds.
- [ ] I can include \(+C\) only where appropriate.
- [ ] I can collect \(I_n\)-terms correctly.

### Bridge checklist

- [ ] I understand that ordinary A-Level integration by parts is the engine.
- [ ] I understand that Further Maths turns that engine into a recurrence formula.
- [ ] I understand that recurrence notation behaves like a sequence, but each term is an integral.
