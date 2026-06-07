# 1. Lesson Title and Metadata

| Field | Value |
|---|---|
| Date generated | 2026-06-05 |
| Course | CCEA GCE Further Mathematics |
| Unit | `FAS2` - Further AS 2 Applied Mathematics |
| Applied section | Section D: Discrete and Decision Mathematics |
| Topic code | `FAS2-REC` |
| Topic name | Recurrence relationships |
| Topic slug | `recurrence_relationships` |
| Topic Pascal | `RecurrenceRelationships` |
| Topic ID | `FAS2RecurrenceRelationships` |
| Lesson file | `FAS2_recurrence_relationships_lesson.md` |
| Learning outcome IDs | `FAS2-REC-LO001`; `FAS2-REC-LO002` |
| Bridge tags | A21 Sequences and Series; AS1 Algebra; indices; summation notation; quadratic equations |
| Topic tags | `#FAS2`, `#REC`, `#Decision`, `#Recurrence`, `#SectionD`, `#ClosedForm`, `#Fibonacci`, `#CharacteristicEquation` |

# Recurrence Relationships

By the end of this lesson, you should be able to look at a process that happens step by step, write it as a recurrence relation with the correct initial condition, generate terms from it, and solve key types of recurrence relation to obtain a closed form.

\[
\text{recurrence relation}+\text{initial condition(s)} \longrightarrow \text{sequence/model}
\]

and, when we solve it,

\[
\text{recursive form} \longrightarrow \text{closed form}.
\]

---

# 2. Evidence Map

| Evidence source | How it is used in this lesson |
|---|---|
| `CCEA_GCE_Further_Mathematics_Specification_Map.md` | Determines `FAS2-REC`, official LO wording, applied section and syllabus boundary. |
| `Further_Maths_README_module_map.md` | Determines ordinary Maths bridge: A21 Sequences and Series; AS1 Algebra. |
| `Further_Maths_EVIDENCE_DROP_CHECKLIST.md` | Determines missing-evidence and off-spec logging structure. |
| `transcripts.md` | Main evidence source for definitions, examples, worked methods, warnings and teacher explanations. |
| `Chapter_4_Recurrence_Relations_♾️_(Further_Pure_2)_screenshots.pdf` | Visual confirmation of slide structure and handwritten annotations. Image-only limitation logged. |
| `Ordinary_A_Level_Maths_Bridge_Spec_Extracts.md` | Used only to explain prerequisite knowledge and bridge risks. |

## Visual evidence limitation

The screenshot PDF is image-only and no text could be parsed from it. Visible rendered pages show the title “FP2: Chapter 4, Recurrence Relations”, “D2: Chapter 7, Recurrence Relations”, examples of recurrence relations, handwritten annotations such as “initial conditions”, “closed form”, and worked recurrence model examples. The lesson uses only visible/readable details and the transcript. No uninspected page detail is claimed.

---

# 3. Specification Alignment

| LO ID | Official wording | Lesson coverage | Evidence source | Boundary | Ordinary Maths bridge |
|---|---|---|---|---|---|
| `FAS2-REC-LO001` | demonstrate understanding of and apply the basic structure of recurrence models, namely a recurrence relation together with initial conditions | Definitions of recurrence, recursive process, recurrence relation, initial condition; forming models for sequences, money, drug dosage, populations; interpreting and criticising models | CCEA spec map; transcript videos 1-3; screenshot PDF pages showing introductory examples | Core CCEA content | A21 sequences and series; AS1 algebra |
| `FAS2-REC-LO002` | solve homogeneous, constant coefficient and linear recurrence relations, including Fibonacci-type relations | Closed forms; verifying closed forms; first-order homogeneous solutions; backward substitution; auxiliary/characteristic equation; complementary function; particular solution where supported by elaboration; Fibonacci-type recurrence | CCEA spec map; transcript videos 4-11; transcript exam-question videos | Core CCEA content, with non-homogeneous breadth handled carefully | A21 geometric sequences, summation, quadratics, indices |

The official CCEA topic identity is:

\[
\boxed{\texttt{FAS2-REC Recurrence relationships}}
\]

under:

\[
\boxed{\text{Section D: Discrete and Decision Mathematics}}.
\]

Proof by induction from the transcript is not taught as core `FAS2-REC` content because it is not named in the two supplied CCEA recurrence learning outcomes.

---

# 4. Learning Objectives

## 4.1 Core Further Maths objectives

By the end of the lesson, you should be able to:

1. Explain what a recurrence relation is.
2. Explain what an initial condition is and why a recurrence relation without enough initial conditions may not determine a unique sequence.
3. Generate terms from a recurrence relation.
4. Distinguish a recursive form from a closed form.
5. Form first-order recurrence relations from written modelling contexts.
6. Interpret and criticise recurrence models in context.
7. Understand the order of a recurrence relation from the difference between subscripts.
8. Solve first-order homogeneous recurrence relations of the form \(u_n=a u_{n-1}\).
9. Use backward substitution for suitable first-order non-homogeneous recurrence relations with \(a=1\), such as \(u_n=u_{n-1}+g(n)\).
10. Use complementary function plus particular solution methods for suitable recurrence relations.
11. Solve second-order homogeneous recurrence relations using an auxiliary or characteristic equation.
12. Recognise Fibonacci-type recurrence relations.

## 4.2 Bridge objectives

You should be able to connect this topic to ordinary A-Level Mathematics by recognising that arithmetic and geometric sequences are old friends wearing new notation, an nth term formula is a closed form, a term-to-term rule is a recursive form, summation formulae help when backward substitution produces a sum, quadratic equations reappear as characteristic equations, and index laws control expressions such as \(a^n\), \(a^{n-1}\), and \(a^{n-2}\).

## 4.3 Exam technique objectives

State the recurrence relation and the initial condition(s), define every variable, use integer time steps for discrete models, show substitution clearly when verifying a closed form, use exact algebra unless context demands decimals, and criticise recurrence models when they predict impossible values.

---

# 5. Explicit Prerequisite Recap

## 5.1 GCSE foundations

| Foundation | Why it matters here |
|---|---|
| Substitution | To calculate \(u_1\), \(u_2\), \(u_3\) from a recurrence relation. |
| Rearranging equations | To solve for constants in closed forms. |
| Percentages | To model interest, decay and dosage contexts. |
| Indices | To simplify \(a\cdot a^{n-1}=a^n\). |
| Sequences | To recognise term-to-term rules and nth term rules. |

## 5.2 A-Level Maths Bridge: What You Already Know and What Further Maths Changes

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| A21 Sequences and Series | A sequence can have an nth term such as \(u_n=3n+1\) | This is called a closed form because it depends only on \(n\), not earlier sequence terms | Do not confuse “find \(u_n\)” with “write a recurrence relation”. |
| A21 Sequences and Series | A term-to-term rule tells you how to get the next term | A recurrence relation formalises this using notation such as \(u_{n+1}=u_n+3\) | The recurrence still needs an initial condition such as \(u_0=3\). |
| A21 Geometric sequences | Repeated multiplication creates powers | A homogeneous recurrence \(u_n=a u_{n-1}\) has solution \(u_n=C a^n\) | The constant \(C\) depends on the initial condition. |
| A21 Series | Summation formulae compress repeated addition | Backward substitution turns repeated recurrence steps into \(\sum\)-notation | The summation index must match the recurrence index. |
| AS1/A21 Algebra | Quadratics can be solved by factorising or formula | Second-order recurrences use an auxiliary equation | The roots of the auxiliary equation control the closed form. |

In ordinary A-Level Maths, this idea appeared as sequences: either a term-to-term rule or an nth term formula. In Further Maths, the same idea becomes a model-building and model-solving machine. The key upgrade is that the recurrence relation can encode dynamic processes: money growing with interest, medicine decaying and being topped up, populations growing, or Fibonacci-type structures. The danger is that old “spot the pattern” habits are too fragile. Here, the algebraic structure must be classified before the method is chosen.

---

# 6. Big Picture Explanation

A recurrence relationship describes a process where the next state is built from earlier states. The transcript defines recurrence as meaning “to occur again” and describes a recursive process as one where results are found by repeated application of a rule to previous results.

For example:

\[
u_{n+1}=u_n+3
\]

says the next term is the previous term plus \(3\). But this rule alone is not enough. To know the actual sequence, we need a starting value such as \(u_0=3\). Then

\[
u_1=u_0+3=3+3=6,
\]

\[
u_2=u_1+3=6+3=9,
\]

\[
u_3=u_2+3=9+3=12.
\]

So the recurrence relation and initial condition together generate:

\[
3,6,9,12,15,\ldots
\]

The core CCEA idea is:

\[
\boxed{\text{recurrence relation}+\text{initial condition(s)}=\text{recurrence model}}.
\]

Some processes are easier to describe by how they update than by a direct nth term formula. A bank account might be described by \(a_n=1.02a_{n-1}+100\). A drug model might be \(d_n=0.1d_{n-1}+125\). A Fibonacci-type sequence might be \(x_n=x_{n-1}+x_{n-2}\).

Solving a recurrence relation means finding a closed form: a formula depending only on \(n\), not previous sequence terms.

---

# 7. Key Definitions and Notation

## 7.1 Sequence

A sequence is an ordered list of terms. The \(n\)th term may be written \(u_n\). The subscript \(n\) tells us the position or step number.

## 7.2 Subscript warning

\[
u_{n-1}\ne u_n-1.
\]

The expression \(u_{n-1}\) means “the term whose index is \(n-1\)”. It does not mean subtract \(1\) from \(u_n\).

## 7.3 Recurrence relation

A recurrence relation defines a term using one or more previous terms:

\[
u_{n+1}=u_n+3,
\]

\[
x_n=x_{n-1}+x_{n-2},
\]

\[
a_n=1.02a_{n-1}+100.
\]

## 7.4 Initial condition

An initial condition gives the starting value or starting values needed to generate a sequence. A first-order recurrence usually needs one initial condition. A second-order recurrence usually needs two.

## 7.5 Closed form

A closed form is a formula for a term using only its position \(n\), not earlier terms. For example, \(u_n=3n\) is closed, whereas \(u_{n+1}=u_n+3\) is recursive.

## 7.6 Order

The order is determined by the difference between the highest and lowest subscripts. For \(u_n=a u_{n-1}+g(n)\), the order is \(1\). For \(u_n=a u_{n-1}+b u_{n-2}\), the order is \(2\).

## 7.7 Homogeneous and non-homogeneous

In \(u_n=a u_{n-1}+g(n)\), the part \(a u_{n-1}\) is the homogeneous part. If \(g(n)=0\), the recurrence is homogeneous. If an extra term such as \(4n\), \(100\), or \(2^n\) is present, it is non-homogeneous.

## 7.8 Fibonacci-type relation

A Fibonacci-type relation depends on the previous two terms:

\[
F_n=F_{n-1}+F_{n-2}.
\]

With \(F_1=1\), \(F_2=1\), the sequence begins:

\[
1,1,2,3,5,8,13,\ldots
\]

## 7.9 Characteristic equation

For a second-order homogeneous recurrence

\[
u_n=a u_{n-1}+b u_{n-2},
\]

try \(u_n=Cr^n\). This leads to the characteristic or auxiliary equation:

\[
\boxed{r^2-ar-b=0}.
\]

---

# 8. Core Theory

## 8.1 Anatomy of a recurrence model

A recurrence model has two essential parts:

\[
\boxed{\text{recurrence relation}}
\qquad\text{and}\qquad
\boxed{\text{initial condition(s)}}.
\]

Example:

\[
u_{n+1}=u_n+3,\qquad u_0=3.
\]

Then:

\[
u_1=3+3=6,
\]
\[
u_2=6+3=9,
\]
\[
u_3=9+3=12.
\]

## 8.2 Recurrence form versus closed form

The recurrence relation

\[
u_{n+1}=u_n+3,\qquad u_0=3
\]

gives \(3,6,9,12,\ldots\). With \(u_0\)-indexing, a closed form is

\[
u_n=3n+3.
\]

Check:

\[
u_0=3(0)+3=3,
\]
\[
u_1=3(1)+3=6,
\]
\[
u_2=3(2)+3=9.
\]

The same pattern may have a different formula if indexing begins at \(u_1\), so always check the starting index.

## 8.3 Forming first-order recurrence relations

A first-order recurrence relation relates a term to the previous term, often in the form:

\[
u_n=a u_{n-1}+b.
\]

### Money account

If an account earns \(2\%\) interest per month and receives £100 per month, with \(a_0=500\), then

\[
a_n=1.02a_{n-1}+100,\qquad a_0=500.
\]

\[
a_1=1.02(500)+100=510+100=610.
\]

\[
a_2=1.02(610)+100=622.20+100=722.20.
\]

### Loan repayment

A £8000 loan increases by \(3\%\) each month and then £500 is repaid:

\[
u_n=1.03u_{n-1}-500,\qquad u_0=8000.
\]

\[
u_1=1.03(8000)-500=8240-500=7740.
\]

Model criticism: after a while the recurrence may predict a negative balance, which is not meaningful once the loan is repaid.

### Drug dosage

If \(90\%\) of the drug is lost every 24 hours, only \(10\%=0.1\) remains. If \(125\text{ mg}\) is administered daily, then

\[
d_n=0.1d_{n-1}+125.
\]

Using the transcript’s chosen initial condition:

\[
d_0=125.
\]

Then:

\[
d_1=0.1(125)+125=137.5,
\]
\[
d_2=0.1(137.5)+125=138.75,
\]
\[
d_3=0.1(138.75)+125=138.875.
\]

If the model tends to a limit \(L\), then

\[
L=0.1L+125,
\]
\[
0.9L=125,
\]
\[
L=\frac{1250}{9}\text{ mg}.
\]

The transcript notes an initial-condition ambiguity depending on whether the first dose has already been administered at time \(0\).

## 8.4 Forming second-order recurrence relations

A second-order recurrence relation uses the previous two terms:

\[
u_n=a u_{n-1}+b u_{n-2}.
\]

### Fibonacci

\[
x_n=x_{n-1}+x_{n-2},\qquad x_0=1,\quad x_1=1.
\]

\[
x_2=1+1=2,
\quad x_3=2+1=3,
\quad x_4=3+2=5.
\]

### Bacteria growth

Let \(b_n\) be the bacteria population after \(n\) hours, with \(b_0=200\), \(b_1=220\). If the number of additional bacteria per hour doubles each hour, then

\[
b_n-b_{n-1}=2(b_{n-1}-b_{n-2}).
\]

Expand:

\[
b_n-b_{n-1}=2b_{n-1}-2b_{n-2}.
\]

Add \(b_{n-1}\):

\[
\boxed{b_n=3b_{n-1}-2b_{n-2}},\qquad b_0=200,\quad b_1=220.
\]

### Staircase model

If Claudia climbs by one or two steps, and \(S_n\) is the number of ways to climb \(n\) steps, then first move case-splitting gives

\[
S_n=S_{n-1}+S_{n-2},\qquad S_1=1,\quad S_2=2.
\]

## 8.5 Verifying closed forms

To verify \(u_n=3n+1\) satisfies \(u_n=u_{n-1}+3\):

\[
u_{n-1}=3(n-1)+1=3n-2.
\]

Then:

\[
u_{n-1}+3=(3n-2)+3=3n+1=u_n.
\]

So the closed form satisfies the recurrence.

To verify \(u_n=2\cdot3^{n-1}\) satisfies \(u_n=3u_{n-1}\):

\[
u_{n-1}=2\cdot3^{n-2}.
\]

\[
3u_{n-1}=3(2\cdot3^{n-2})=2\cdot3^1\cdot3^{n-2}=2\cdot3^{n-1}=u_n.
\]

To verify \(u_n=3^n-n-\frac32\) satisfies \(u_n=3u_{n-1}+2n\):

\[
u_{n-1}=3^{n-1}-(n-1)-\frac32.
\]

\[
3u_{n-1}+2n=3\left(3^{n-1}-(n-1)-\frac32\right)+2n.
\]

\[
=3^n-3n+3-\frac92+2n=3^n-n-\frac32=u_n.
\]

## 8.6 Solving first-order homogeneous recurrence relations

For

\[
u_n=a u_{n-1},
\]

backward substitution gives:

\[
u_n=a u_{n-1}=a(a u_{n-2})=a^2u_{n-2}=a^3u_{n-3}=\cdots=a^nu_0.
\]

Since \(u_0\) is constant, write:

\[
\boxed{u_n=Ca^n}.
\]

Example:

\[
x_n=2x_{n-1},\qquad x_0=3.
\]

\[
x_n=C2^n.
\]

Use \(x_0=3\):

\[
3=C2^0=C.
\]

Therefore

\[
\boxed{x_n=3\cdot2^n}.
\]

Example with non-zero starting index:

\[
P_n=-3P_{n-1},\qquad P_1=60.
\]

\[
P_n=C(-3)^n.
\]

\[
60=C(-3)^1=-3C,
\]

so

\[
C=-20,
\]

and

\[
\boxed{P_n=-20(-3)^n}.
\]

## 8.7 First-order non-homogeneous recurrences when \(a=1\)

For

\[
u_n=u_{n-1}+g(n),
\]

the transcript recommends backward substitution:

\[
\boxed{u_n=u_0+\sum_{r=1}^{n}g(r)}.
\]

Example:

\[
u_n=u_{n-1}+2n+1,\qquad u_0=7.
\]

Here \(g(n)=2n+1\). Therefore

\[
u_n=7+\sum_{r=1}^{n}(2r+1).
\]

\[
=7+2\sum_{r=1}^{n}r+\sum_{r=1}^{n}1.
\]

\[
=7+2\left(\frac12n(n+1)\right)+n.
\]

\[
=7+n(n+1)+n=n^2+2n+7.
\]

So

\[
\boxed{u_n=n^2+2n+7}.
\]

Example with \(x_1\) given:

\[
x_n=x_{n-1}+5^n,
\qquad x_1=3.
\]

\[
x_n=x_0+\sum_{r=1}^{n}5^r=x_0-\frac54(1-5^n).
\]

Use \(x_1=3\):

\[
3=x_0+5,
\]

so

\[
x_0=-2.
\]

Thus

\[
\boxed{x_n=-2-\frac54(1-5^n)}.
\]

## 8.8 First-order non-homogeneous recurrences when \(a\ne1\)

For

\[
u_n=a u_{n-1}+g(n),\qquad a\ne1,
\]

use:

\[
\boxed{\text{general solution}=\text{complementary function}+\text{particular solution}}.
\]

The complementary function is:

\[
Ca^n.
\]

### Constant example

Solve:

\[
u_n=4u_{n-1}+3,
\qquad u_0=10.
\]

Complementary function:

\[
C4^n.
\]

Try particular solution \(u_n=\lambda\). Then \(u_{n-1}=\lambda\), so

\[
\lambda=4\lambda+3,
\]

\[
-3\lambda=3,
\]

\[
\lambda=-1.
\]

Thus

\[
u_n=C4^n-1.
\]

Use \(u_0=10\):

\[
10=C4^0-1=C-1,
\]

so \(C=11\). Hence

\[
\boxed{u_n=11\cdot4^n-1}.
\]

### Linear example

Solve:

\[
u_n=3u_{n-1}+4n,\qquad u_1=2.
\]

Complementary function:

\[
C3^n.
\]

Try:

\[
u_n=\lambda n+\mu.
\]

Then

\[
u_{n-1}=\lambda(n-1)+\mu=\lambda n-\lambda+\mu.
\]

Substitute:

\[
\lambda n+\mu=3(\lambda n-\lambda+\mu)+4n.
\]

\[
\lambda n+\mu=(3\lambda+4)n+(-3\lambda+3\mu).
\]

Compare coefficients:

\[
\lambda=3\lambda+4\Rightarrow \lambda=-2.
\]

\[
\mu=-3\lambda+3\mu.
\]

Substitute \(\lambda=-2\):

\[
\mu=6+3\mu\Rightarrow \mu=-3.
\]

So

\[
u_n=C3^n-2n-3.
\]

Use \(u_1=2\):

\[
2=3C-2-3=3C-5,
\]

so

\[
C=\frac73.
\]

Therefore

\[
\boxed{u_n=\frac73 3^n-2n-3}.
\]

### Exponential clash example

Solve:

\[
u_n=2u_{n-1}+3\cdot2^n,\qquad u_0=2.
\]

The complementary function is \(C2^n\). Since the non-homogeneous term also contains \(2^n\), do not try \(\lambda2^n\). Try

\[
u_n=\lambda n2^n.
\]

Then

\[
u_{n-1}=\lambda(n-1)2^{n-1}.
\]

Substitute:

\[
\lambda n2^n=2\left[\lambda(n-1)2^{n-1}\right]+3\cdot2^n.
\]

\[
\lambda n2^n=\lambda(n-1)2^n+3\cdot2^n.
\]

Divide by \(2^n\):

\[
\lambda n=\lambda n-\lambda+3.
\]

So \(\lambda=3\). General solution:

\[
u_n=C2^n+3n2^n.
\]

Use \(u_0=2\):

\[
2=C.
\]

Therefore

\[
\boxed{u_n=2\cdot2^n+3n2^n=2^n(2+3n)}.
\]

## 8.9 Second-order homogeneous recurrence relations

For

\[
u_n=a u_{n-1}+b u_{n-2},
\]

try \(u_n=Cr^n\). Then

\[
Cr^n=aCr^{n-1}+bCr^{n-2}.
\]

Divide by \(Cr^{n-2}\):

\[
r^2=ar+b.
\]

So

\[
\boxed{r^2-ar-b=0}.
\]

Root cases:

| Root type | General solution |
|---|---|
| Distinct real roots \(\alpha,\beta\) | \(u_n=A\alpha^n+B\beta^n\) |
| Repeated real root \(\alpha\) | \(u_n=(A+Bn)\alpha^n\) |
| Complex roots \(R(\cos\theta\pm i\sin\theta)\) | \(u_n=R^n(A\cos n\theta+B\sin n\theta)\) |

## 8.10 Worked second-order examples

### Distinct real roots

Solve:

\[
u_n=2u_{n-1}+8u_{n-2},\qquad u_0=4,\quad u_1=10.
\]

Auxiliary equation:

\[
r^2-2r-8=0.
\]

\[
(r-4)(r+2)=0.
\]

So \(r=4\) or \(r=-2\). Therefore

\[
u_n=A4^n+B(-2)^n.
\]

Use \(u_0=4\):

\[
A+B=4. \tag{1}
\]

Use \(u_1=10\):

\[
4A-2B=10. \tag{2}
\]

From \((1)\), \(B=4-A\). Substitute:

\[
4A-2(4-A)=10,
\]

\[
6A-8=10,
\]

\[
A=3.
\]

So \(B=1\). Thus

\[
\boxed{u_n=3\cdot4^n+(-2)^n}.
\]

### Repeated root

Solve:

\[
p_n=4p_{n-1}-4p_{n-2},\qquad p_1=1,\quad p_2=1.
\]

Auxiliary equation:

\[
r^2-4r+4=0=(r-2)^2.
\]

Repeated root \(r=2\) gives:

\[
p_n=(A+Bn)2^n.
\]

Use \(p_1=1\):

\[
1=2(A+B)=2A+2B. \tag{1}
\]

Use \(p_2=1\):

\[
1=4(A+2B)=4A+8B. \tag{2}
\]

Double \((1)\):

\[
4A+4B=2. \tag{3}
\]

Subtract \((3)\) from \((2)\):

\[
4B=-1,
\]

so

\[
B=-\frac14.
\]

Then

\[
2A+2\left(-\frac14\right)=1,
\]

\[
2A=\frac32,
\]

\[
A=\frac34.
\]

Therefore

\[
\boxed{p_n=\left(\frac34-\frac14n\right)2^n=(3-n)2^{n-2}}.
\]

### Complex roots

Solve:

\[
x_n=2x_{n-1}-2x_{n-2},\qquad x_0=1,\quad x_2=2.
\]

Auxiliary equation:

\[
r^2-2r+2=0.
\]

Using the quadratic formula:

\[
r=\frac{2\pm\sqrt{4-8}}{2}=1\pm i.
\]

For \(1+i\), modulus \(R=\sqrt2\), argument \(\theta=\pi/4\). Thus

\[
x_n=(\sqrt2)^n\left(A\cos\frac{n\pi}{4}+B\sin\frac{n\pi}{4}\right).
\]

Use \(x_0=1\):

\[
1=A.
\]

Use \(x_2=2\):

\[
2=(\sqrt2)^2\left(A\cos\frac{\pi}{2}+B\sin\frac{\pi}{2}\right)=2B.
\]

So \(B=1\). Therefore

\[
\boxed{x_n=(\sqrt2)^n\left(\cos\frac{n\pi}{4}+\sin\frac{n\pi}{4}\right)}.
\]

Boundary note: complex-root recurrence examples are included because they appear in the supplied transcript and follow naturally from the characteristic-equation method. If a CCEA mark scheme narrows expected examples, follow the mark scheme.

## 8.11 Closed form of the Fibonacci sequence

The Fibonacci recurrence is

\[
F_n=F_{n-1}+F_{n-2},\qquad F_1=1,\quad F_2=1.
\]

Auxiliary equation:

\[
r^2-r-1=0.
\]

By the quadratic formula:

\[
r=\frac{1\pm\sqrt5}{2}.
\]

Let

\[
\alpha=\frac{1+\sqrt5}{2},\qquad \beta=\frac{1-\sqrt5}{2}.
\]

Then

\[
F_n=A\alpha^n+B\beta^n.
\]

Using \(F_1=1\) and \(F_2=1\), the transcript obtains

\[
A=\frac{1}{\sqrt5},\qquad B=-\frac{1}{\sqrt5}.
\]

Therefore

\[
\boxed{F_n=\frac{1}{\sqrt5}\left[\left(\frac{1+\sqrt5}{2}\right)^n-\left(\frac{1-\sqrt5}{2}\right)^n\right]}.
\]

## 8.12 Boundary-sensitive extension

Second-order non-homogeneous recurrence relations such as

\[
u_n=a u_{n-1}+b u_{n-2}+g(n)
\]

can be approached using complementary function plus particular solution. However, because the supplied CCEA LO wording for `FAS2-REC-LO002` explicitly emphasises homogeneous constant coefficient recurrence relations, broad second-order non-homogeneous cases are treated here as boundary-sensitive enrichment.

For example, for

\[
u_n=2u_{n-1}-u_{n-2}+2^n,
\]

the homogeneous part has auxiliary equation

\[
r^2-2r+1=0=(r-1)^2,
\]

so the complementary function is

\[
A+Bn.
\]

Try \(u_n=\lambda2^n\). Substitution gives \(\lambda=4\), so

\[
\boxed{u_n=A+Bn+4\cdot2^n}.
\]

## 8.13 Proof by induction: excluded from core `FAS2-REC`

The transcript includes proof by induction for recurrence closed forms and states that it is FP2-only in its source context. Since the supplied CCEA `FAS2-REC` LOs do not name proof by induction, it is not taught as core content here. It may be useful enrichment in a separate proof-focused Further Pure lesson.

## 8.14 Method selection summary

| Task | Method |
|---|---|
| Form recurrence model | Define variable, write update rule, state initial condition(s), interpret/criticise if asked. |
| Verify closed form | Find \(u_{n-1}\), substitute into recurrence, simplify to given \(u_n\). |
| Solve \(u_n=a u_{n-1}\) | Use \(u_n=Ca^n\). |
| Solve \(u_n=u_{n-1}+g(n)\) | Use \(u_n=u_0+\sum_{r=1}^{n}g(r)\). |
| Solve \(u_n=a u_{n-1}+g(n), a\ne1\) | Complementary function plus particular solution. |
| Solve \(u_n=a u_{n-1}+b u_{n-2}\) | Auxiliary equation \(r^2-ar-b=0\). |

## 8.15 Model assumptions and limitations

| Context | Assumption | Limitation |
|---|---|---|
| Bank account | Interest rate and deposit stay fixed | Real rates may change. |
| Loan | Repayment happens regularly | The model may predict negative debt. |
| Drug dosage | Same fraction remains each day | Timing and medical thresholds may matter. |
| Population | Growth rule remains fixed | Resources and capacity are ignored. |
| Staircase count | Only allowed step sizes are used | If allowed moves change, recurrence changes. |

---

# 9. Visual Asset Integration

[VISUAL PLACEHOLDER: FAS2RecurrenceRelationshipsMermaid-001 | Source: CCEA Further Mathematics specification map + transcript evidence | Insert from mermaid/FAS2RecurrenceRelationshipsMermaid-001.md | Purpose: Show the route from recurrence model to closed form. The diagram must branch from “Form recurrence relation + initial conditions” into “generate terms”, “verify closed form”, “solve first-order”, and “solve second-order”.]

[VISUAL PLACEHOLDER: FAS2RecurrenceRelationshipsSVG-001 | Source: Transcript introduction and closed-form discussion | Insert from svg/FAS2RecurrenceRelationshipsSVG-001.svg | Purpose: Compare \(u_{n+1}=u_n+3,\ u_0=3\) with a closed form such as \(u_n=3n+3\), showing term generation \(3,6,9,12,\ldots\).]

[VISUAL PLACEHOLDER: FAS2RecurrenceRelationshipsSVG-002 | Source: Transcript modelling examples | Insert from svg/FAS2RecurrenceRelationshipsSVG-002.svg | Purpose: Show the components of a recurrence model: state variable, update rule, initial condition, units/context, and limitation.]

[VISUAL PLACEHOLDER: FAS2RecurrenceRelationshipsSVG-003 | Source: Transcript solving methods | Insert from svg/FAS2RecurrenceRelationshipsSVG-003.svg | Purpose: Help students select the correct first-order solving method.]

[VISUAL PLACEHOLDER: FAS2RecurrenceRelationshipsSVG-004 | Source: CCEA LO002 + transcript second-order theory | Insert from svg/FAS2RecurrenceRelationshipsSVG-004.svg | Purpose: Show how \(u_n=a u_{n-1}+b u_{n-2}\) leads to \(r^2-ar-b=0\), then to root-case solution forms.]

[VISUAL PLACEHOLDER: FAS2RecurrenceRelationshipsBridgeSVG-001 | Source: Ordinary A-Level Maths bridge + Further Maths specification | Insert from svg/FAS2RecurrenceRelationshipsBridgeSVG-001.svg | Purpose: Compare prior ordinary Maths method with Further Maths extension.]

[VISUAL PLACEHOLDER: FAS2RecurrenceRelationshipsTikZ-001 | Source: Transcript notation discussion | Insert from tikz/FAS2RecurrenceRelationshipsTikZ-001.tex | Purpose: Show \(u_{n-2}\), \(u_{n-1}\), \(u_n\), and \(u_{n+1}\) on a discrete index line, with first-order and second-order gaps labelled.]

---

# 10. Interactive Learning Widgets

[INTERACTIVE PLACEHOLDER: FAS2RecurrenceRelationshipsWidget-001 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FAS2RecurrenceRelationshipsWidget-001.html | Purpose: Generate terms from a recurrence relation and initial condition.]

[INTERACTIVE PLACEHOLDER: FAS2RecurrenceRelationshipsWidget-002 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FAS2RecurrenceRelationshipsWidget-002.html | Purpose: Solve characteristic equations and display root-case templates.]

[INTERACTIVE PLACEHOLDER: FAS2RecurrenceRelationshipsWidget-003 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FAS2RecurrenceRelationshipsWidget-003.html | Purpose: Practise interpreting and criticising recurrence models.]

---

# 11. Worked Examples

## Worked Example 1: Generate a first-order recurrence sequence

Question: The next number in a sequence is the previous number add \(3\). The first term is \(u_0=3\). Write a recurrence relation and generate the first five terms.

Solution:

\[
u_{n+1}=u_n+3,\qquad u_0=3.
\]

\[
u_1=u_0+3=3+3=6,
\]
\[
u_2=u_1+3=6+3=9,
\]
\[
u_3=u_2+3=9+3=12,
\]
\[
u_4=u_3+3=12+3=15.
\]

\[
\boxed{3,6,9,12,15}
\]

## Worked Example 2: Fibonacci-type recurrence

\[
x_n=x_{n-1}+x_{n-2},\qquad x_0=1,\quad x_1=1.
\]

\[
x_2=x_1+x_0=1+1=2,
\]
\[
x_3=x_2+x_1=2+1=3,
\]
\[
x_4=x_3+x_2=3+2=5,
\]
\[
x_5=x_4+x_3=5+3=8.
\]

## Worked Example 3: Bank account

\[
a_n=1.02a_{n-1}+100,\qquad a_0=500.
\]

\[
a_1=1.02(500)+100=610,
\]
\[
a_2=1.02(610)+100=722.20.
\]

## Worked Example 4: Loan repayment

\[
u_n=1.03u_{n-1}-500,\qquad u_0=8000.
\]

\[
u_1=1.03(8000)-500=7740.
\]

Criticism: after a while, \(u_n\) may become negative, which does not make sense for a remaining loan balance.

## Worked Example 5: Drug dosage

\[
d_n=0.1d_{n-1}+125,
\qquad d_0=125.
\]

\[
d_1=0.1(125)+125=137.5,
\]
\[
d_2=0.1(137.5)+125=138.75,
\]
\[
d_3=0.1(138.75)+125=138.875.
\]

Limiting value:

\[
L=0.1L+125\Rightarrow0.9L=125\Rightarrow L=\frac{1250}{9}\text{ mg}.
\]

## Worked Example 6: Bacteria recurrence

\[
b_n-b_{n-1}=2(b_{n-1}-b_{n-2})
\]

\[
b_n=3b_{n-1}-2b_{n-2},\qquad b_0=200,\quad b_1=220.
\]

## Worked Example 7: Staircase recurrence

If the first move is one step, there are \(S_{n-1}\) ways remaining. If the first move is two steps, there are \(S_{n-2}\) ways remaining. Therefore:

\[
S_n=S_{n-1}+S_{n-2},\qquad S_1=1,\quad S_2=2.
\]

## Worked Example 8: Verify \(u_n=3n+1\)

\[
u_{n-1}=3(n-1)+1=3n-2.
\]

\[
u_{n-1}+3=3n-2+3=3n+1=u_n.
\]

## Worked Example 9: First-order homogeneous

\[
x_n=2x_{n-1},\qquad x_0=3.
\]

\[
x_n=C2^n,
\]

\[
3=C2^0=C.
\]

\[
\boxed{x_n=3\cdot2^n}.
\]

## Worked Example 10: \(a=1\) non-homogeneous

\[
u_n=u_{n-1}+2n+1,\qquad u_0=7.
\]

\[
u_n=7+\sum_{r=1}^{n}(2r+1)=7+2\sum_{r=1}^{n}r+\sum_{r=1}^{n}1=n^2+2n+7.
\]

## Worked Example 11: \(a\ne1\) non-homogeneous

\[
u_n=3u_{n-1}+4n,\qquad u_1=2.
\]

Complementary function:

\[
C3^n.
\]

Particular solution:

\[
u_n=\lambda n+\mu.
\]

Substitution gives \(\lambda=-2\), \(\mu=-3\), so

\[
u_n=C3^n-2n-3.
\]

Use \(u_1=2\):

\[
2=3C-5\Rightarrow C=\frac73.
\]

\[
\boxed{u_n=\frac73 3^n-2n-3}.
\]

## Worked Example 12: Distinct roots

\[
u_n=2u_{n-1}+8u_{n-2},\qquad u_0=4,\quad u_1=10.
\]

\[
r^2-2r-8=0=(r-4)(r+2).
\]

\[
u_n=A4^n+B(-2)^n.
\]

Using \(u_0=4\), \(u_1=10\) gives \(A=3\), \(B=1\), so

\[
\boxed{u_n=3\cdot4^n+(-2)^n}.
\]

## Worked Example 13: Repeated root

\[
p_n=4p_{n-1}-4p_{n-2},\qquad p_1=1,\quad p_2=1.
\]

\[
r^2-4r+4=(r-2)^2.
\]

\[
p_n=(A+Bn)2^n.
\]

Using \(p_1=1\), \(p_2=1\) gives

\[
A=\frac34,
\qquad B=-\frac14.
\]

\[
\boxed{p_n=\left(\frac34-\frac14n\right)2^n}.
\]

## Worked Example 14: Fibonacci closed form

\[
F_n=F_{n-1}+F_{n-2},\qquad F_1=1,\quad F_2=1.
\]

\[
r^2-r-1=0.
\]

\[
r=\frac{1\pm\sqrt5}{2}.
\]

\[
\boxed{F_n=\frac{1}{\sqrt5}\left[\left(\frac{1+\sqrt5}{2}\right)^n-\left(\frac{1-\sqrt5}{2}\right)^n\right]}.
\]

---

# 12. Common Mistakes and Exam Traps

1. Forgetting initial conditions.
2. Mixing up \(u_{n-1}\) and \(u_n-1\).
3. Using one initial condition for a second-order recurrence.
4. Forgetting to define variables and units.
5. Using \(0.03\) instead of \(1.03\) for a \(3\%\) increase.
6. Using \(0.9\) instead of \(0.1\) for a \(90\%\) decrease.
7. Confusing recursive form with closed form.
8. Not checking whether indexing starts at \(u_0\) or \(u_1\).
9. Using the summation shortcut when \(a\ne1\).
10. Choosing a particular solution that clashes with the complementary function.
11. Using \(A\alpha^n+B\alpha^n\) for repeated roots instead of \((A+Bn)\alpha^n\).
12. Forgetting brackets around negative bases such as \((-2)^n\).
13. Giving vague model criticism instead of context-specific limitations.

---

# 13. Practice Questions

These are generated practice questions based on the lesson evidence and CCEA `FAS2-REC` boundary. They are not claimed to be past-paper or textbook questions.

## Basic fluency

1. A sequence is defined by \(u_{n+1}=u_n+4,\ u_0=2\). Find \(u_1,u_2,u_3,u_4\).
2. A sequence is defined by \(x_n=x_{n-1}+x_{n-2},\ x_0=2,\ x_1=3\). Find \(x_2,x_3,x_4,x_5\).
3. State the order of: \(u_n=5u_{n-1}\), \(x_n=3x_{n-1}-2x_{n-2}\), \(a_{n+1}=a_n+7\), \(p_n=4p_{n-3}\).
4. State whether each is recursive or closed: \(u_n=2n+5\), \(u_n=u_{n-1}+6\), \(x_n=3\cdot2^n\), \(x_n=4x_{n-1}-x_{n-2}\).

## Bridge and modelling

5. The sequence \(5,8,11,14,17,\ldots\) increases by \(3\). Write a recurrence using \(u_0=5\), then a closed form.
6. Given \(u_n=7\cdot3^n\), find \(u_0\) and a recurrence of the form \(u_n=a u_{n-1}\).
7. Solve \(u_n=u_{n-1}+3n,\ u_0=4\).
8. A savings account contains £600 initially. Each month, it increases by \(1.5\%\), then £80 is added. Form a recurrence and find \(a_1,a_2\).
9. A loan begins at £5000. Each month, \(2\%\) interest is added, then £300 is repaid. Form a recurrence, find \(L_1\), and criticise the model.
10. A medicine model assumes \(20\%\) remains each day, then \(50\text{ mg}\) is added. With \(M_0=50\), form a recurrence, find \(M_1,M_2,M_3\), and find the limiting value.

## Solving

11. Solve \(u_n=4u_{n-1},\ u_0=3\).
12. Solve \(p_n=-2p_{n-1},\ p_1=10\).
13. Solve \(u_n=u_{n-1}+2n-1,\ u_0=6\).
14. Solve \(u_n=5u_{n-1}+8,\ u_0=1\).
15. Solve \(u_n=2u_{n-1}+3n,\ u_0=4\).
16. Solve \(u_n=3u_{n-1}+2\cdot3^n,\ u_0=5\).
17. Solve \(u_n=5u_{n-1}-6u_{n-2},\ u_0=2,\ u_1=5\).
18. Solve \(x_n=6x_{n-1}-9x_{n-2},\ x_0=1,\ x_1=6\).
19. For \(F_n=F_{n-1}+F_{n-2},\ F_0=0,\ F_1=1\), find \(F_2\) to \(F_6\), then write the auxiliary equation.
20. Solve \(S_n=S_{n-1}+S_{n-2},\ S_0=2,\ S_1=1\).
21. A population \(P_n\) has \(P_0=100\), \(P_1=130\). The increase each hour is triple the previous increase. Write a recurrence and find \(P_2,P_3\).
22. A person climbs stairs by taking one or three steps. Explain why \(T_n=T_{n-1}+T_{n-3}\) and state suitable \(T_1,T_2,T_3\).

---

# 14. Worked Solutions

## Solution 1

\[
u_1=2+4=6,
\quad u_2=6+4=10,
\quad u_3=10+4=14,
\quad u_4=14+4=18.
\]

## Solution 2

\[
x_2=3+2=5,
\quad x_3=5+3=8,
\quad x_4=8+5=13,
\quad x_5=13+8=21.
\]

## Solution 3

(a) first-order; (b) second-order; (c) first-order; (d) third-order.

## Solution 4

(a) closed form; (b) recursive form; (c) closed form; (d) recursive form.

## Solution 5

\[
u_{n+1}=u_n+3,\quad u_0=5;
\qquad u_n=3n+5.
\]

## Solution 6

\[
u_0=7\cdot3^0=7.
\]

\[
u_n=3u_{n-1},\qquad u_0=7.
\]

## Solution 7

\[
u_n=4+\sum_{r=1}^{n}3r=4+3\cdot\frac12n(n+1)=4+\frac32n(n+1).
\]

## Solution 8

\[
a_n=1.015a_{n-1}+80,\qquad a_0=600.
\]

\[
a_1=1.015(600)+80=689.
\]

\[
a_2=1.015(689)+80=779.335\approx £779.34.
\]

## Solution 9

\[
L_n=1.02L_{n-1}-300,
\qquad L_0=5000.
\]

\[
L_1=1.02(5000)-300=4800.
\]

Criticism: the model may eventually predict a negative loan balance, which does not make sense once the loan is fully repaid.

## Solution 10

\[
M_n=0.2M_{n-1}+50,
\qquad M_0=50.
\]

\[
M_1=60,
\quad M_2=62,
\quad M_3=62.4.
\]

Limit:

\[
L=0.2L+50\Rightarrow0.8L=50\Rightarrow L=62.5\text{ mg}.
\]

## Solution 11

\[
u_n=C4^n,
\quad 3=C4^0=C,
\quad \boxed{u_n=3\cdot4^n}.
\]

## Solution 12

\[
p_n=C(-2)^n,
\quad 10=C(-2),
\quad C=-5,
\quad \boxed{p_n=-5(-2)^n}.
\]

## Solution 13

\[
u_n=6+\sum_{r=1}^{n}(2r-1)=6+2\sum r-\sum1=6+n(n+1)-n=n^2+6.
\]

## Solution 14

Complementary function \(C5^n\). Try \(\lambda\):

\[
\lambda=5\lambda+8\Rightarrow -4\lambda=8\Rightarrow \lambda=-2.
\]

\[
u_n=C5^n-2.
\]

Use \(u_0=1\):

\[
1=C-2\Rightarrow C=3.
\]

\[
\boxed{u_n=3\cdot5^n-2}.
\]

## Solution 15

Complementary function \(C2^n\). Try \(\lambda n+\mu\). Substitute:

\[
\lambda n+\mu=2(\lambda n-\lambda+\mu)+3n.
\]

\[
\lambda=2\lambda+3\Rightarrow \lambda=-3.
\]

\[
\mu=-2\lambda+2\mu\Rightarrow \mu=6+2\mu\Rightarrow \mu=-6.
\]

\[
u_n=C2^n-3n-6.
\]

Use \(u_0=4\):

\[
4=C-6\Rightarrow C=10.
\]

\[
\boxed{u_n=10\cdot2^n-3n-6}.
\]

## Solution 16

Complementary function \(C3^n\). Since \(3^n\) clashes, try \(\lambda n3^n\).

\[
\lambda n3^n=3[\lambda(n-1)3^{n-1}]+2\cdot3^n.
\]

\[
\lambda n=\lambda n-\lambda+2\Rightarrow \lambda=2.
\]

\[
u_n=C3^n+2n3^n.
\]

Use \(u_0=5\): \(C=5\). Thus

\[
\boxed{u_n=3^n(5+2n)}.
\]

## Solution 17

\[
r^2-5r+6=0=(r-2)(r-3).
\]

\[
u_n=A2^n+B3^n.
\]

Use \(u_0=2\): \(A+B=2\). Use \(u_1=5\): \(2A+3B=5\). Then \(B=1\), \(A=1\), so

\[
\boxed{u_n=2^n+3^n}.
\]

## Solution 18

\[
r^2-6r+9=(r-3)^2.
\]

\[
x_n=(A+Bn)3^n.
\]

Use \(x_0=1\): \(A=1\). Use \(x_1=6\):

\[
6=3(A+B)\Rightarrow 2=A+B\Rightarrow B=1.
\]

\[
\boxed{x_n=(1+n)3^n}.
\]

## Solution 19

\[
F_2=1,
\quad F_3=2,
\quad F_4=3,
\quad F_5=5,
\quad F_6=8.
\]

Auxiliary equation:

\[
\boxed{r^2-r-1=0}.
\]

## Solution 20

\[
r^2-r-1=0,
\quad \alpha=\frac{1+\sqrt5}{2},
\quad \beta=\frac{1-\sqrt5}{2}.
\]

\[
S_n=A\alpha^n+B\beta^n.
\]

Use \(S_0=2\): \(A+B=2\). Use \(S_1=1\): \(A\alpha+B\beta=1\). Solving gives \(A=1\), \(B=1\), so

\[
\boxed{S_n=\left(\frac{1+\sqrt5}{2}\right)^n+\left(\frac{1-\sqrt5}{2}\right)^n}.
\]

## Solution 21

\[
P_n-P_{n-1}=3(P_{n-1}-P_{n-2}).
\]

\[
P_n=4P_{n-1}-3P_{n-2},\qquad P_0=100,\quad P_1=130.
\]

\[
P_2=4(130)-3(100)=220.
\]

\[
P_3=4(220)-3(130)=490.
\]

## Solution 22

If the first move is one step, there are \(T_{n-1}\) ways left. If the first move is three steps, there are \(T_{n-3}\) ways left. Hence

\[
T_n=T_{n-1}+T_{n-3}.
\]

Initial values:

\[
T_1=1,
\quad T_2=1,
\quad T_3=2.
\]

---

# 15. Exam Technique Notes

1. Always write the recurrence relation and initial condition(s).
2. Define the variable before using it.
3. Use correct percentage multipliers: \(3\%\) increase is \(1.03\), \(90\%\) decrease leaves \(0.1\).
4. Be precise about timing in dosage or payment problems.
5. Criticise the context, not the algebra.
6. Classify before solving.
7. For verification, write \(u_{n-1}\) explicitly and substitute.
8. For second-order recurrences, write the auxiliary equation before solving it.
9. For repeated roots, use \((A+Bn)\alpha^n\).
10. For exponential particular-solution clashes, multiply by \(n\).
11. Use exact values unless decimals are required by context.
12. Calculator checking is useful, but written method earns the marks.

---

# 16. Syllabus Gap Check

| LO ID | Official wording | Covered? | Evidence-backed coverage |
|---|---|---:|---|
| `FAS2-REC-LO001` | demonstrate understanding of and apply the basic structure of recurrence models, namely a recurrence relation together with initial conditions | Yes | Definitions, recurrence anatomy, initial conditions, first-order and second-order model formation, money/drug/bacteria/staircase examples. |
| `FAS2-REC-LO002` | solve homogeneous, constant coefficient and linear recurrence relations, including Fibonacci-type relations | Yes | First-order homogeneous, first-order linear cases, second-order homogeneous constant-coefficient cases, Fibonacci-type recurrence and closed form. |

## Off-Spec Content Found but Excluded

| Content | Source | Reason excluded from core |
|---|---|---|
| Proof by induction for recurrence closed forms | Teacher transcript | Transcript labels this as FP2-only in source context; not named in supplied CCEA `FAS2-REC` LOs. |
| Broad second-order non-homogeneous recurrence relations | Teacher transcript | Included only as boundary-sensitive extension because supplied CCEA wording emphasises homogeneous constant-coefficient recurrence relations. |
| FP2/D2 course identity labels | Teacher transcript and screenshot PDF | CCEA lesson identity must use `FAS2`, not FP2 or D2. |
| Cross-board exercise labels such as FP2 Ex4A or D2 Ex7A | Transcript titles | Useful source navigation only; not CCEA topic metadata. |

## Missing Evidence Log

| Missing evidence | Impact |
|---|---|
| Full textbook extract | Limits exact preservation of textbook wording and exercise sequence. |
| Topic-specific local module map for `FAS2-REC` | Project-wide map used instead. |
| Complete OCR/parsed text for screenshot PDF | Visual details are treated cautiously. |
| CCEA past-paper recurrence questions and mark schemes | Practice questions are generated and not labelled as past-paper. |

---

# 17. Recommended Enhancements Not in the Evidence

AI-proposed enhancements include method-selection diagrams, recursive-versus-closed-form visuals, characteristic-equation root-case charts, term-generation widgets, model-critique widgets, verification checkers, and more examples on repeated roots and Fibonacci-type recurrence.

These are proposed teaching assets, not evidence-backed official CCEA materials.

---

# 18. Supplementary Sources Used

Project sources used:

- `CCEA_GCE_Further_Mathematics_Specification_Map.md`
- `Further_Maths_README_module_map.md`
- `Further_Maths_EVIDENCE_DROP_CHECKLIST.md`
- `Further Maths Portal Build – Knowledge Evidence.txt`

Lesson-specific evidence used:

- `transcripts.md`
- `Chapter_4_Recurrence_Relations_♾️_(Further_Pure_2)_screenshots.pdf`

Ordinary A-Level Maths bridge sources used:

- `Ordinary_A_Level_Maths_Bridge_Spec_Extracts.md`
- `CCEA_GCE_Mathematics_Specification_Map.md`

Ordinary A-Level Mathematics sources are bridge context only. They do not override the Further Mathematics specification.

---

# 19. Final Student Checklist

## Prerequisite confidence

- [ ] Use percentage multipliers such as \(1.03\), \(0.1\), \(1.015\).
- [ ] Expand brackets such as \(3(n-1)+1\).
- [ ] Use index laws such as \(a\cdot a^{n-1}=a^n\).
- [ ] Use summation formulae such as \(\sum_{r=1}^{n}r=\frac12n(n+1)\).
- [ ] Solve quadratic equations.
- [ ] Solve simultaneous equations.

## Further Maths method

- [ ] Define a recurrence relation.
- [ ] Define an initial condition.
- [ ] Generate terms from a recurrence relation.
- [ ] Distinguish recursive form from closed form.
- [ ] State the order of a recurrence relation.
- [ ] Identify homogeneous and non-homogeneous recurrence relations.
- [ ] Solve \(u_n=a u_{n-1}\) using \(u_n=Ca^n\).
- [ ] Solve \(u_n=u_{n-1}+g(n)\) using \(u_n=u_0+\sum_{r=1}^{n}g(r)\).
- [ ] Solve suitable \(u_n=a u_{n-1}+g(n)\), \(a\ne1\), using complementary function plus particular solution.
- [ ] Form an auxiliary equation for \(u_n=a u_{n-1}+b u_{n-2}\).
- [ ] Use distinct-root, repeated-root and Fibonacci-type solution forms.

## Exam technique

- [ ] Define variables and units.
- [ ] Include initial condition(s).
- [ ] Show substitution steps.
- [ ] Write the auxiliary equation.
- [ ] Use brackets around negative bases.
- [ ] Use \((A+Bn)\alpha^n\) for repeated roots.
- [ ] Multiply by \(n\) when a particular solution clashes.
- [ ] Give context-specific model criticisms.
