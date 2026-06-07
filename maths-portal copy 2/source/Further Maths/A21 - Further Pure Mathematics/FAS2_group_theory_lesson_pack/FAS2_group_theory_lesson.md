# FAS2 Group Theory

# 1. Lesson Title and Metadata

| Field | Value |
|---|---|
| Date generated | 2026-06-05 |
| Course | CCEA GCE Further Mathematics |
| Unit | `FAS2` - Further AS 2 Applied Mathematics |
| Applied section | Section D: Discrete and Decision Mathematics |
| Topic code | `FAS2-GROUP` |
| Topic name | Group theory |
| Topic slug | `group_theory` |
| Topic Pascal | `GroupTheory` |
| Topic ID | `FAS2GroupTheory` |
| Lesson file name | `FAS2_group_theory_lesson.md` |
| LO IDs | `FAS2-GROUP-LO001`, `FAS2-GROUP-LO002`, `FAS2-GROUP-LO003`, `FAS2-GROUP-LO004`, `FAS2-GROUP-LO005`, `FAS2-GROUP-LO006`, `FAS2-GROUP-LO007`, `FAS2-GROUP-LO008`, `FAS2-GROUP-LO009` |
| Bridge tags | Ordinary A-Level algebra, proof, function composition, transformations, inverse notation, set notation, counting |
| Topic tags | groups, binary operation, closure, identity, inverse, associativity, Cayley table, subgroup, Lagrange, cyclic group, generator, isomorphism |

Group theory studies mathematical structure. Instead of learning only a new calculation technique, we study what happens when a set of objects is equipped with a rule for combining them.

A group is written as

\[
(G,*)
\]

where \(G\) is a set and \(*\) is a binary operation satisfying the four group axioms: closure, identity, inverse and associativity.

# 2. Evidence Map

| Evidence source | Role in lesson | Limitation |
|---|---|---|
| `CCEA_GCE_Further_Mathematics_Specification_Map.md` | Authoritative source for `FAS2-GROUP`, LO IDs and syllabus boundary | None for topic identity |
| `Further_Maths_README_module_map.md` | Project metadata, naming and phase workflow | General source, not topic-specific worked examples |
| `Further_Maths_EVIDENCE_DROP_CHECKLIST.md` | Evidence and asset preservation protocol | General checklist |
| `Further Maths Portal Build – Knowledge Evidence.txt` | Portal build workflow and subject evidence rules | General source |
| `Ordinary_A_Level_Maths_Bridge_Spec_Extracts.md` | Ordinary A-Level Maths bridge context only | Does not override Further Maths specification |
| `CCEA_GCE_Mathematics_Specification_Map.md` | Ordinary Maths bridge context only | Not Further Maths authority |
| `transcripts.md` | Main lesson-specific evidence for explanations, examples, warnings and teaching sequence | Auto-transcript errors normalised where mathematically clear, e.g. Cayley table |
| `Chapter_2_Groups_♾️_(Further_Pure_2)_screenshots.pdf` | Visual evidence for modulo table, triangle symmetries, cup permutations and tables | Image-only PDF; only visible/readable details claimed |

The uploaded evidence title says FP2 / Further Pure 2, but the CCEA specification boundary places this lesson in `FAS2-GROUP`, Section D: Discrete and Decision Mathematics. CCEA controls the unit identity.

# 3. Specification Alignment

| LO ID | Official learning outcome | Lesson coverage |
|---|---|---|
| `FAS2-GROUP-LO001` | recall that a group consists of a set of elements together with a binary operation which is closed and associative, for which an identity exists in the set and for which every element has an inverse in the set | Full definition and four-axiom method |
| `FAS2-GROUP-LO002` | use the basic group properties to show that a given structure is, or is not, a group | Worked examples using integers, reals, complex numbers, matrices, modular arithmetic and finite tables |
| `FAS2-GROUP-LO003` | recall the meaning of the term order of a group | Defines \(|G|\) as number of elements |
| `FAS2-GROUP-LO004` | determine the period of elements in a given group | Defines period/order of an element and practises repeated operation |
| `FAS2-GROUP-LO005` | demonstrate understanding of the idea of a subgroup of a group, find subgroups in simple cases and show that given subsets are, or are not, proper subgroups | Generated subgroups, proper subgroups, trivial subgroup |
| `FAS2-GROUP-LO006` | recall and apply Lagrange's theorem concerning the order of a subgroup of a finite group | States and applies \(|H|\mid |G|\), proof excluded |
| `FAS2-GROUP-LO007` | demonstrate understanding of the meaning of the term cyclic as applied to groups | Cyclic groups via generators |
| `FAS2-GROUP-LO008` | use the term generator in relation to cyclic groups | Uses \(G=\langle a\rangle\) and generator examples |
| `FAS2-GROUP-LO009` | demonstrate understanding of the idea of isomorphism between groups and determine whether given groups are, or are not, isomorphic | Isomorphism by identity, periods and Cayley-table structure |

# 4. Learning Objectives

## Core Further Maths objectives

By the end of the lesson, you should be able to define a group, test the four axioms, construct and read Cayley tables, find the order of a group, determine periods of elements, find subgroups, apply Lagrange's theorem, identify cyclic groups and generators, and test isomorphism.

## Bridge objectives

You should be able to connect group theory to ordinary A-Level Maths through operations, functions, proof, inverse notation, graph/shape transformations and counting arrangements.

## Exam technique objectives

You should be able to write clear axiom-by-axiom proofs, use counterexamples correctly, avoid assuming commutativity, and use exact notation.

# 5. Explicit Prerequisite Recap

## GCSE foundations

You need substitution, expanding brackets, factorising, negative numbers, factors, divisibility and remainders.

## Ordinary AS/A2 Mathematics foundations

You need algebraic manipulation, proof by deduction and counterexample, set notation, function notation, composite functions, transformations and, where relevant, matrices.

### A-Level Maths Bridge: What You Already Know and What Further Maths Changes

| Ordinary A-Level Maths source | What was learned there | Further Maths extension in this topic | New risk or warning |
|---|---|---|---|
| Operations | You used \(+,-,\times,\div\) to calculate | A binary operation may be any defined rule | Do not assume \(*\) means multiplication |
| Functions | You used rules such as \(f(x)\) and compositions | A group operation may combine transformations or permutations | Product order may be right-to-left |
| Inverses | You met inverse functions and reciprocals | Inverse elements undo under the group operation | \(a^{-1}\) does not always mean \(1/a\) |
| Proof | You proved identities and used counterexamples | Axioms must be verified for all elements | Examples disprove but do not prove universal closure |
| Transformations | You transformed graphs and shapes | Symmetry transformations can form groups | A diagram alone is not a group proof |
| Counting | You counted arrangements | Permutations become elements with a composition operation | Counting \(3!\) arrangements is not enough; you need operation structure |

In ordinary A-Level Maths, operations were usually tools. In Further Maths, the operation and the set become the object of study. The key upgrade is abstraction; the danger is carrying over rules such as commutativity or reciprocal inverses without checking the operation.

# 6. Big Picture Explanation

Group theory asks: what do different mathematical situations have in common when their objects combine by a rule? The evidence begins with \(G=\{0,1,2\}\) under addition modulo 3, then moves to symmetries of an equilateral triangle and permutations of three cups. These look different, but group theory reveals the structure beneath them.

For \(G=\{0,1,2\}\) with \(a*b\equiv a+b\pmod3\), the operation table is

\[
\begin{array}{c|ccc}
* & 0 & 1 & 2\\
\hline
0 & 0 & 1 & 2\\
1 & 1 & 2 & 0\\
2 & 2 & 0 & 1
\end{array}
\]

The element \(0\) is the identity and every result remains in \(G\), so closure is visible.

The six symmetries of an equilateral triangle are

\[
G=\{I,P,Q,R,S,T\}
\]

where \(I\) is do nothing, \(P\) is rotation by \(120^\circ\) clockwise, \(Q\) is rotation by \(120^\circ\) anticlockwise, and \(R,S,T\) are the three reflections. Composition of these transformations is the operation. The order matters: the evidence gives examples such as \(S*P=R\) but \(P*S=T\), so \(S*P\ne P*S\).

The three-cup permutation example has six arrangements, matching the six triangle symmetries. This is the intuitive doorway into isomorphism: different surface stories can share the same group structure.

# 7. Key Definitions and Notation

## Set and element

A set is a collection of objects. In group theory, the objects are called elements. If \(a\) is an element of \(G\), write \(a\in G\).

## Binary operation

A binary operation combines two elements. If \(a,b\in G\), then \(a*b\) is the result of combining \(a\) and \(b\). A binary operation on \(G\) must produce an element of \(G\).

## Group

A group is a pair \((G,*)\) where \(G\) is a set and \(*\) is a binary operation satisfying the four axioms:

\[
\begin{aligned}
&\text{Closure:} && a,b\in G\Rightarrow a*b\in G.\\
&\text{Identity:} && \exists e\in G\text{ such that }a*e=e*a=a.\\
&\text{Inverse:} && \forall a\in G,\exists a^{-1}\in G\text{ such that }a*a^{-1}=a^{-1}*a=e.\\
&\text{Associativity:} && a*(b*c)=(a*b)*c.
\end{aligned}
\]

## Order of a group

The order of a finite group \(G\) is the number of elements in \(G\), written \(|G|\).

## Period/order of an element

The period of \(a\in G\) is the smallest positive integer \(k\) such that

\[
a^k=e.
\]

The transcript often calls this the order of an element; CCEA uses the term period.

## Cayley table

A Cayley table is an operation table for a finite group. Unless a question says otherwise, read row \(*\) column.

## Subgroup

A subset \(H\subseteq G\) is a subgroup if it forms a group under the same operation. Write \(H\leq G\).

## Lagrange's theorem

If \(G\) is finite and \(H\leq G\), then

\[
|H|\mid |G|.
\]

## Cyclic group and generator

A group is cyclic if some element \(a\) generates every element by repeated operation. Write

\[
G=\langle a\rangle.
\]

## Isomorphism

Groups \(G\) and \(H\) are isomorphic, written \(G\cong H\), if there is a bijection \(\phi:G\to H\) preserving the operation:

\[
\phi(a*b)=\phi(a)\circ\phi(b).
\]

# 8. Core Theory

## 8.1 The four-axiom group test

To prove \((G,*)\) is a group, show closure, identity, inverse and associativity. To disprove a group, one failed axiom is enough, but the failed axiom must be named.

## 8.2 Closure

Closure means combining elements does not escape the set. For example, if

\[
S=\{x+y\sqrt3:x,y\in\mathbb Z\},
\]

then addition is closed because for

\[
s_1=a+b\sqrt3,\qquad s_2=c+d\sqrt3,
\]

with \(a,b,c,d\in\mathbb Z\),

\[
s_1+s_2=(a+c)+(b+d)\sqrt3,
\]

and \(a+c,b+d\in\mathbb Z\).

By contrast, \(\mathbb N\) is not closed under subtraction because \(7,10\in\mathbb N\), but \(7-10=-3\notin\mathbb N\).

## 8.3 Identity

An identity does nothing. Under addition the identity is \(0\); under multiplication it is \(1\); for matrices it is \(I=\begin{pmatrix}1&0\\0&1\end{pmatrix}\); for triangle symmetries it is \(I\), the do-nothing symmetry.

For a custom operation, solve \(a*e=a\) and check \(e*a=a\).

## 8.4 Inverse

The inverse of \(a\) is the element that returns the identity. It depends on the operation.

For \(a*b=a+b+ab\), solve for the identity:

\[
a*e=a+e+ae=a.
\]

Then

\[
e+ae=0,
\]

\[
e(1+a)=0,
\]

so \(e=0\). For the inverse of \(m\):

\[
m*m^{-1}=0,
\]

\[
m+m^{-1}+mm^{-1}=0,
\]

\[
m^{-1}(1+m)=-m,
\]

\[
m^{-1}=-\frac{m}{1+m},\qquad m\ne -1.
\]

## 8.5 Associativity

Associativity is

\[
a*(b*c)=(a*b)*c.
\]

It is not commutativity. Commutativity is \(a*b=b*a\).

For \(a\circ b=ab+1\),

\[
a\circ(b\circ c)=a\circ(bc+1)=a(bc+1)+1=abc+a+1,
\]

while

\[
(a\circ b)\circ c=(ab+1)\circ c=(ab+1)c+1=abc+c+1.
\]

These are not equal for all \(a,c\), so \(\circ\) is not associative. A numerical counterexample is \(2,3,4\):

\[
2\circ(3\circ4)=27,
\]

but

\[
(2\circ3)\circ4=29.
\]

## 8.6 Example: \((\mathbb Z,+)\) is a group

Closure: integer plus integer is integer.

Identity: \(0\in\mathbb Z\) and \(a+0=0+a=a\).

Inverse: for \(a\in\mathbb Z\), \(-a\in\mathbb Z\) and \(a+(-a)=(-a)+a=0\).

Associativity: ordinary addition is associative.

Therefore \((\mathbb Z,+)\) is a group.

## 8.7 Example: \((\mathbb Z,\times)\) is not a group

Closure holds and identity \(1\) exists. But \(0\in\mathbb Z\) has no multiplicative inverse because \(0x=0\) for every integer \(x\), never \(1\). The inverse axiom fails.

## 8.8 Example: \((\mathbb R,*)\), \(a*b=a+b-1\)

Closure holds because real numbers are closed under addition and subtraction.

Identity:

\[
a*e=a+e-1=a\Rightarrow e=1.
\]

Check \(1*a=1+a-1=a\). Inverse:

\[
a*a^{-1}=1,
\]

\[
a+a^{-1}-1=1,
\]

\[
a^{-1}=2-a.
\]

Associativity:

\[
a*(b*c)=a*(b+c-1)=a+b+c-2,
\]

and

\[
(a*b)*c=(a+b-1)*c=a+b+c-2.
\]

So \((\mathbb R,*)\) is a group.

## 8.9 Cayley tables

For \(G=\{1,-1,i,-i\}\) under multiplication:

\[
\begin{array}{c|cccc}
\times & 1 & -1 & i & -i\\
\hline
1 & 1 & -1 & i & -i\\
-1 & -1 & 1 & -i & i\\
i & i & -i & -1 & 1\\
-i & -i & i & 1 & -1
\end{array}
\]

The identity is \(1\). Inverses are

\[
1^{-1}=1,
\]

\[
(-1)^{-1}=-1,
\]

\[
i^{-1}=-i,
\]

\[
(-i)^{-1}=i.
\]

## 8.10 Modular multiplication example that is not a group

Let \(G=\{1,3,7,9\}\) under multiplication modulo 12. The table is

\[
\begin{array}{c|cccc}
*_ {12} & 1 & 3 & 7 & 9\\
\hline
1 & 1 & 3 & 7 & 9\\
3 & 3 & 9 & 9 & 3\\
7 & 7 & 9 & 1 & 3\\
9 & 9 & 3 & 3 & 9
\end{array}
\]

Closure holds and the identity is \(1\). But the row for \(3\) contains no \(1\), so \(3\) has no inverse. Therefore it is not a group.

## 8.11 Permutations and two-row notation

A permutation such as

\[
\begin{pmatrix}1&2&3\\2&1&3\end{pmatrix}
\]

means \(1\mapsto2\), \(2\mapsto1\), \(3\mapsto3\). The six permutations of three objects are

\[
\begin{pmatrix}1&2&3\\1&2&3\end{pmatrix},
\quad
\begin{pmatrix}1&2&3\\2&1&3\end{pmatrix},
\quad
\begin{pmatrix}1&2&3\\1&3&2\end{pmatrix},
\]

\[
\begin{pmatrix}1&2&3\\3&2&1\end{pmatrix},
\quad
\begin{pmatrix}1&2&3\\3&1&2\end{pmatrix},
\quad
\begin{pmatrix}1&2&3\\2&3&1\end{pmatrix}.
\]

These form the symmetric group \(S_3\), which is isomorphic to the triangle symmetry group.

## 8.12 Periods in the triangle group

For \(G=\{I,P,Q,R,S,T\}\), \(|G|=6\). The periods are

\[
\operatorname{period}(I)=1,
\]

\[
\operatorname{period}(P)=\operatorname{period}(Q)=3,
\]

\[
\operatorname{period}(R)=\operatorname{period}(S)=\operatorname{period}(T)=2.
\]

## 8.13 Cyclic groups

A group is cyclic if one element generates the whole group. For \(G=\{0,1,2,3,4,5,6,7\}\) under addition modulo 8, the element \(3\) generates:

\[
3,6,1,4,7,2,5,0.
\]

Thus \(G=\langle3\rangle\). Under addition modulo 8, powers mean repeated addition.

The group \(\{1,3,5,7\}\) under multiplication modulo 8 is not cyclic because every non-identity element squares to \(1\), so no element has period 4.

## 8.14 Subgroups

A subgroup \(H\leq G\) must be a group under the same operation. In the triangle group,

\[
\langle P\rangle=\{I,P,Q\}
\]

is a proper subgroup. Also \(\{I,R\}\), \(\{I,S\}\) and \(\{I,T\}\) are subgroups.

For \(G=\{0,1,2,3,4,5,6,7\}\) under addition modulo 8,

\[
\langle2\rangle=\{0,2,4,6\},
\]

and

\[
\langle4\rangle=\{0,4\}.
\]

Both are non-trivial proper subgroups.

## 8.15 Lagrange's theorem

If \(H\leq G\), then \(|H|\mid |G|\). For a group of order 6, possible subgroup orders are \(1,2,3,6\). There is no subgroup of order 4 or 5. However, a divisor does not guarantee a subgroup exists; it only passes the divisibility test.

## 8.16 Isomorphism

An isomorphism is a structure-preserving bijection. Identity maps to identity, periods match, inverses correspond and products are preserved. Triangle symmetries and permutations of three cups are isomorphic because both have six elements and the same operation structure.

A useful disproof method is to compare period patterns. For example, \(\{1,3,5,7\}\) under multiplication modulo 8 has three non-identity elements of period 2, while \(\mathbb Z_4\) has two elements of period 4. Therefore they are not isomorphic.

# 9. Visual Asset Integration

[VISUAL PLACEHOLDER: FAS2GroupTheoryMermaid-001 | Source: CCEA FAS2-GROUP specification + transcript sections on group axioms | Insert from mermaid/FAS2GroupTheoryMermaid-001.md | Purpose: Show the four group axioms as a decision process: closure, identity, inverse, associativity. Description: A flowchart beginning with \((G,*)\), then branching through each axiom, ending in “Group” or “Not a group”.]

[VISUAL PLACEHOLDER: FAS2GroupTheoryMermaid-002 | Source: Transcript proof and group-check examples | Insert from mermaid/FAS2GroupTheoryMermaid-002.md | Purpose: Help students decide whether to prove a structure is a group or disprove it using one failed axiom. Description: A decision tree with routes for closure failure, identity failure, inverse failure and associativity counterexample.]

[VISUAL PLACEHOLDER: FAS2GroupTheorySVG-001 | Source: Screenshot PDF opening example + transcript introduction | Insert from svg/FAS2GroupTheorySVG-001.svg | Purpose: Preserve the introductory group \(G=\{0,1,2\}\) under addition modulo 3. Description: A clean Cayley-style table showing \(0,1,2\), with \(0\) highlighted as identity and all results highlighted as elements of \(G\).]

[VISUAL PLACEHOLDER: FAS2GroupTheorySVG-002 | Source: Screenshot PDF pages showing \(I,P,Q,R,S,T\) symmetries + transcript explanation | Insert from svg/FAS2GroupTheorySVG-002.svg | Purpose: Visualise the triangle symmetry group. Description: Six labelled equilateral triangles with tracking symbols and rotation/reflection information.]

[VISUAL PLACEHOLDER: FAS2GroupTheorySVG-003 | Source: Screenshot PDF cup-permutation slides + transcript correction of cycle notation | Insert from svg/FAS2GroupTheorySVG-003.svg | Purpose: Connect permutations of three cups to \(S_3\). Description: Six arrangements of three cups with two-row notation beneath each.]

[VISUAL PLACEHOLDER: FAS2GroupTheorySVG-004 | Source: Transcript sections on identity and inverse | Insert from svg/FAS2GroupTheorySVG-004.svg | Purpose: Show identity as “do nothing” and inverse as “undo”. Description: Split diagram showing \(a*e=e*a=a\) and \(a*a^{-1}=a^{-1}*a=e\).]

[VISUAL PLACEHOLDER: FAS2GroupTheoryBridgeSVG-001 | Source: Ordinary A-Level Maths bridge + Further Maths specification | Insert from svg/FAS2GroupTheoryBridgeSVG-001.svg | Purpose: Compare prior ordinary Maths method with Further Maths extension. Description: A bridge from operations, functions, transformations and proof to group axioms, Cayley tables, cyclic groups and isomorphism.]

[VISUAL PLACEHOLDER: FAS2GroupTheoryTikZ-001 | Source: Transcript finite group and Cayley table sections | Insert from tikz/FAS2GroupTheoryTikZ-001.tex | Purpose: Provide a precise printable Cayley table template. Description: A labelled row-by-column table with arrows explaining how to read \(x*y\).]

[VISUAL PLACEHOLDER: FAS2GroupTheoryTikZ-002 | Source: Transcript and screenshot PDF triangle symmetry examples | Insert from tikz/FAS2GroupTheoryTikZ-002.tex | Purpose: Record the group operation table for \(I,P,Q,R,S,T\). Description: A full Cayley table for triangle symmetries, with identity row and column highlighted.]

[VISUAL PLACEHOLDER: FAS2GroupTheoryTikZ-003 | Source: Transcript Cayley table example for \(\{1,-1,i,-i\}\) | Insert from tikz/FAS2GroupTheoryTikZ-003.tex | Purpose: Show a finite group under complex multiplication. Description: A Cayley table for \(\{1,-1,i,-i\}\), with inverse pairs highlighted.]

# 10. Interactive Learning Widgets

[INTERACTIVE PLACEHOLDER: FAS2GroupTheoryWidget-001 | Source: AI-proposed teaching enhancement based on lesson evidence | Insert from widgets/FAS2GroupTheoryWidget-001.html | Purpose: Let students test whether a small operation table forms a group.]

[INTERACTIVE PLACEHOLDER: FAS2GroupTheoryWidget-002 | Source: AI-proposed teaching enhancement based on transcript Cayley table examples | Insert from widgets/FAS2GroupTheoryWidget-002.html | Purpose: Train students to locate identity elements and inverses from a Cayley table.]

[INTERACTIVE PLACEHOLDER: FAS2GroupTheoryWidget-003 | Source: AI-proposed teaching enhancement based on transcript cyclic group examples | Insert from widgets/FAS2GroupTheoryWidget-003.html | Purpose: Explore generators in addition modulo \(n\).]

[INTERACTIVE PLACEHOLDER: FAS2GroupTheoryWidget-004 | Source: AI-proposed teaching enhancement based on transcript isomorphism sections | Insert from widgets/FAS2GroupTheoryWidget-004.html | Purpose: Help students match two small groups by identity, element periods and operation preservation.]

# 11. Worked Examples

## Worked Example 1: addition modulo 3

Given \(G=\{0,1,2\}\) and \(a*b\equiv a+b\pmod3\), the table is

\[
\begin{array}{c|ccc}
* & 0 & 1 & 2\\
\hline
0&0&1&2\\
1&1&2&0\\
2&2&0&1
\end{array}
\]

The identity is \(0\). The operation is addition modulo 3. Closure holds because every table entry is in \(G\).

## Worked Example 2: triangle symmetries

For \(G=\{I,P,Q,R,S,T\}\), with the second letter applied first, the evidence examples include

\[
S*P=R,
\]

\[
P*S=T,
\]

\[
T*Q=R,
\]

\[
Q*T=S.
\]

Thus the operation is not commutative.

## Worked Example 3: triangle identity, inverses and periods

The identity is \(I\). Inverses are

\[
I^{-1}=I,
\quad P^{-1}=Q,
\quad Q^{-1}=P,
\quad R^{-1}=R,
\quad S^{-1}=S,
\quad T^{-1}=T.
\]

The group order is \(|G|=6\). Periods are \(1\) for \(I\), \(3\) for \(P,Q\), and \(2\) for \(R,S,T\).

## Worked Example 4: two-row permutation notation

The six permutations of three objects are

\[
\begin{pmatrix}1&2&3\\1&2&3\end{pmatrix},
\begin{pmatrix}1&2&3\\2&1&3\end{pmatrix},
\begin{pmatrix}1&2&3\\1&3&2\end{pmatrix},
\]

\[
\begin{pmatrix}1&2&3\\3&2&1\end{pmatrix},
\begin{pmatrix}1&2&3\\3&1&2\end{pmatrix},
\begin{pmatrix}1&2&3\\2&3&1\end{pmatrix}.
\]

## Worked Example 5: closure of \(S=\{x+y\sqrt3:x,y\in\mathbb Z\}\)

Let \(s_1=a+b\sqrt3\) and \(s_2=c+d\sqrt3\). Then

\[
s_1+s_2=(a+c)+(b+d)\sqrt3.
\]

Since \(a+c,b+d\in\mathbb Z\), the sum is in \(S\). So addition is a binary operation on \(S\).

## Worked Example 6: \(\mathbb N\) not closed under subtraction

\[
7,10\in\mathbb N,
\]

but

\[
7-10=-3\notin\mathbb N.
\]

Therefore \(\mathbb N\) is not closed under subtraction.

## Worked Example 7: identity and inverse for \(a*b=a+b+ab\)

As shown in Core Theory, \(e=0\) and

\[
m^{-1}=-\frac{m}{1+m},\qquad m\ne -1.
\]

## Worked Example 8: non-associativity of \(a\circ b=ab+1\)

\[
2\circ(3\circ4)=27,
\]

but

\[
(2\circ3)\circ4=29.
\]

Therefore \(\circ\) is not associative.

## Worked Example 9: \((\mathbb Z,+)\) is a group

Closure, identity \(0\), inverse \(-a\), and associativity all hold.

## Worked Example 10: \((\mathbb Z,\times)\) is not a group

The inverse axiom fails because \(0\) has no multiplicative inverse in \(\mathbb Z\).

## Worked Example 11: \((\mathbb R,*)\), \(a*b=a+b-1\)

The identity is \(1\), inverse is \(2-a\), and associativity holds, so it is a group.

## Worked Example 12: \(\{1,-1,i,-i\}\) table

The Cayley table has identity \(1\), with \(i^{-1}=-i\) and \((-i)^{-1}=i\).

## Worked Example 13: modulo 12 non-group

For \(\{1,3,7,9\}\) under multiplication modulo 12, \(3\) has no inverse, so it is not a group.

## Worked Example 14: addition modulo 8 generated by 3

\[
3,6,1,4,7,2,5,0
\]

is the full group, so \(3\) is a generator.

## Worked Example 15: subgroups of addition modulo 8

\[
\langle2\rangle=\{0,2,4,6\},
\]

\[
\langle4\rangle=\{0,4\}.
\]

Both are non-trivial proper subgroups.

## Worked Example 16: associativity of \(a*b=a+b+ab\)

\[
a*(b*c)=a+b+c+ab+ac+bc+abc,
\]

and

\[
(a*b)*c=a+b+c+ab+ac+bc+abc.
\]

Thus \(*\) is associative.

## Worked Example 17: multiplication modulo 7 cyclic group

For \(G=\{1,2,3,4,5,6\}\) under multiplication modulo 7,

\[
3,2,6,4,5,1
\]

are the powers of \(3\), so \(G=\langle3\rangle\).

## Worked Example 18: abstract group algebra

Given \(p*p=s\), \(s*s=r\), and \(p*p*p=q\), then

\[
p*q=p*(p*p*p)=(p*p)*(p*p)=s*s=r.
\]

Also

\[
s*p=(p*p)*p=p*p*p=q.
\]

## Worked Example 19: isomorphism method

Match identity first, then periods, then products. For triangle symmetries and cup permutations, identity maps to do nothing, rotations map to cycles, and reflections map to swaps.

## Worked Example 20: subgroup \(\{1,7,9,15\}\) modulo 16

Under multiplication modulo 16,

\[
7^2\equiv9^2\equiv15^2\equiv1\pmod{16}.
\]

The subgroup has identity \(1\) and three self-inverse non-identity elements.

## Worked Example 21: Lagrange

If \(|G|=8\) and \(|H|=4\), then \(4\mid8\), so the subgroup order satisfies Lagrange's theorem.

# 12. Common Mistakes and Exam Traps

1. Treating \(*\) as ordinary multiplication.
2. Assuming \(a^{-1}=1/a\).
3. Proving closure using examples only.
4. Forgetting the identity must belong to the set.
5. Checking identity or inverse on only one side in a non-commutative context.
6. Assuming commutativity.
7. Confusing associativity and commutativity.
8. Using numerical examples to prove associativity.
9. Reading transformation products in the wrong order.
10. Confusing order of a group with period of an element.
11. Using Lagrange's theorem backwards.
12. Calling the whole group a proper subgroup.
13. Forgetting the trivial subgroup.
14. Thinking a Cayley table automatically proves associativity.
15. Matching isomorphic groups by labels instead of structure.
16. Treating cyclic as a visual pattern rather than generation by one element.
17. Getting modulo arithmetic wrong.
18. Ignoring excluded values in inverse formulae.

# 13. Practice Questions

1. Let \(G=\{0,1,2,3\}\) under addition modulo 4. Write the Cayley table, identify the identity, find inverses, find periods and decide whether \(G\) is cyclic.
2. Let \(S=\{a+b\sqrt2:a,b\in\mathbb Z\}\). Show \(S\) is closed under addition.
3. Show \(\mathbb N\) is not closed under subtraction.
4. Let \(a*b=a+b+2\) on \(\mathbb R\). Find identity, inverse and decide whether it is a group.
5. Let \(a\circ b=ab+a\). Show \(\circ\) is not associative.
6. Explain why \(a^{-1}\) does not always mean \(1/a\).
7. Explain how function composition helps interpret transformation products.
8. Distinguish associativity and commutativity.
9. Let \(G=\mathbb R\setminus\{-1\}\) with \(a*b=a+b+ab\). Show \(G\) is a group.
10. Let \(G=\{1,2,4\}\) under multiplication modulo 7. Write the table, show it is a group, find periods, and decide if cyclic.
11. Let \(G=\{0,1,2,3,4,5\}\) under addition modulo 6. Find \(\langle2\rangle\) and \(\langle3\rangle\).
12. Decide whether \(\{1,-1,i,-i\}\) under multiplication is isomorphic to \(\{0,1,2,3\}\) under addition modulo 4.
13. In a group, if \(a^2=b\) and \(b^2=e\), show \(a^4=e\).
14. For the four-element table with all non-identity elements self-inverse, find inverses, periods and cyclic status.
15. In the triangle group, find \(\langle P\rangle\), explain it is proper, use Lagrange to rule out order 4, and explain why the group is not cyclic.
16. For \(\{1,3,5,7\}\) under multiplication modulo 8, write the table, show group status, show self-inverses, decide cyclic status and compare with \(\mathbb Z_4\).
17. For \(a*b=a+b-k\) on \(\mathbb R\), find identity, inverse and prove group status.
18. Explain why \(\phi(x)=\ln x\) gives \((\mathbb R^+,\times)\cong(\mathbb R,+)\), but not \((\mathbb R\setminus\{0\},\times)\cong(\mathbb R,+)\).

# 14. Worked Solutions

## Solution 1

For addition modulo 4:

\[
\begin{array}{c|cccc}
+_4&0&1&2&3\\
\hline
0&0&1&2&3\\
1&1&2&3&0\\
2&2&3&0&1\\
3&3&0&1&2
\end{array}
\]

Identity is \(0\). Inverses are \(0^{-1}=0\), \(1^{-1}=3\), \(2^{-1}=2\), \(3^{-1}=1\). Periods are \(1,4,2,4\). The group is cyclic, generated by \(1\) or \(3\).

## Solution 2

Let \(s_1=a+b\sqrt2\), \(s_2=c+d\sqrt2\). Then \(s_1+s_2=(a+c)+(b+d)\sqrt2\in S\), so \(S\) is closed.

## Solution 3

\(3,5\in\mathbb N\) but \(3-5=-2\notin\mathbb N\), so \(\mathbb N\) is not closed under subtraction.

## Solution 4

For \(a*b=a+b+2\), identity \(e=-2\). Inverse solves \(a+a^{-1}+2=-2\), so \(a^{-1}=-a-4\). Associativity gives both sides \(a+b+c+4\). Therefore it is a group.

## Solution 5

With \(a\circ b=ab+a\), use \(1,2,3\):

\[
1\circ(2\circ3)=1\circ8=9,
\]

but

\[
(1\circ2)\circ3=3\circ3=12.
\]

Thus not associative.

## Solution 6

Under addition, inverse of \(a\) is \(-a\); under multiplication, inverse of \(a\) is \(1/a\) where allowed. The operation decides the meaning.

## Solution 7

Just as \(f(g(x))\) means apply \(g\) first, a transformation product may require the second symbol to be applied first.

## Solution 8

Associativity: \(a*(b*c)=(a*b)*c\). Commutativity: \(a*b=b*a\). Groups require associativity, not necessarily commutativity.

## Solution 9

For \(G=\mathbb R\setminus\{-1\}\), \(a*b=a+b+ab\). Closure follows because if \(a*b=-1\), then \((a+1)(b+1)=0\), forcing \(a=-1\) or \(b=-1\), impossible. Identity \(e=0\). Inverse \(a^{-1}=-a/(1+a)\), which is not \(-1\). Associativity expands to \(a+b+c+ab+ac+bc+abc\) on both sides. Thus it is a group.

## Solution 10

For \(G=\{1,2,4\}\) modulo 7:

\[
\begin{array}{c|ccc}
\times_7&1&2&4\\
\hline
1&1&2&4\\
2&2&4&1\\
4&4&1&2
\end{array}
\]

Identity \(1\), inverses \(1^{-1}=1\), \(2^{-1}=4\), \(4^{-1}=2\). Periods are \(1,3,3\). It is cyclic.

## Solution 11

Under addition modulo 6, \(\langle2\rangle=\{0,2,4\}\) and \(\langle3\rangle=\{0,3\}\). Their orders are 3 and 2, both dividing 6, and both are proper non-trivial subgroups.

## Solution 12

\(\{1,-1,i,-i\}\) under multiplication has periods \(1,2,4,4\). \(\mathbb Z_4\) has periods \(1,4,2,4\). The multisets match. An isomorphism is \(1\mapsto0\), \(i\mapsto1\), \(-1\mapsto2\), \(-i\mapsto3\). Thus the groups are isomorphic.

## Solution 13

\[
a^4=(a^2)^2=b^2=e.
\]

## Solution 14

In the table, \(e\) is identity. Each non-identity element squares to \(e\), so every non-identity element is self-inverse and has period 2. No element has period 4, so the group is not cyclic.

## Solution 15

\(\langle P\rangle=\{I,P,Q\}\). It is proper because it is not all of \(G\). Since \(|G|=6\), no subgroup of order 4 exists because \(4\nmid6\). The group is not cyclic because no element has period 6.

## Solution 16

For \(\{1,3,5,7\}\) modulo 8, all non-identity elements square to 1. It is a group, not cyclic, and not isomorphic to \(\mathbb Z_4\), since \(\mathbb Z_4\) has elements of period 4.

## Solution 17

For \(a*b=a+b-k\), identity \(e=k\), inverse \(a^{-1}=2k-a\), and associativity gives both sides \(a+b+c-2k\). Thus it is a group.

## Solution 18

For \(x,y>0\), \(\ln(xy)=\ln x+\ln y\), identity maps \(1\mapsto0\), and inverses map \(1/x\mapsto-\ln x\). Thus \((\mathbb R^+,\times)\cong(\mathbb R,+)\). But \(\ln x\) is not real-valued for negative non-zero reals, and \(\mathbb R\setminus\{0\}\) under multiplication has \(-1\) of period 2 while \((\mathbb R,+)\) has no non-identity element of period 2.

# 15. Exam Technique Notes

Use this exam sequence: closure, identity, inverse, associativity, conclusion. For closure and associativity proofs, use arbitrary elements. For disproving, one counterexample is enough. For Cayley tables, scan closure, identity row/column, inverses and periods. For isomorphism, compare identity, periods and operation preservation.

# 16. Syllabus Gap Check

All nine `FAS2-GROUP` LO IDs are covered. The lesson includes group axioms, group proof/disproof, order of a group, period of elements, subgroups, Lagrange's theorem, cyclic groups, generators and isomorphism.

## Off-Spec Content Found but Excluded

- FA22 Polya/cycle-index ideas excluded.
- FA22 regular-solid symmetry groups excluded.
- Cross-board FP2/A2 labels do not change the CCEA unit identity.
- Named classification of small groups is marked as optional enrichment only.

## Missing evidence

- Official CCEA textbook pages not separately supplied.
- CCEA past-paper mark schemes not supplied.
- Screenshot PDF is image-only and not fully parseable as text.

# 17. Recommended Enhancements Not in the Evidence

Recommended enhancements include animations for triangle symmetries, a Cayley table highlighter, a generator orbit explorer, a modular multiplication tester, a subgroup lattice visual and isomorphism matching activities. These are proposed enhancements, not additional CCEA authority.

# 18. Supplementary Sources Used

Project sources used: CCEA Further Mathematics specification map, Further Maths module map, evidence checklist, portal build knowledge evidence, ordinary A-Level Maths bridge extracts and ordinary Mathematics specification map. Lesson-specific sources used: `transcripts.md` and the image-only screenshot PDF.

Ordinary A-Level Mathematics sources are bridge context only and do not override the Further Maths specification.

# 19. Final Student Checklist

## Prerequisite confidence

- [ ] I can use set notation.
- [ ] I can expand and factorise algebraic expressions.
- [ ] I can use modular arithmetic.
- [ ] I can read function composition order.
- [ ] I can use counterexamples correctly.

## Further Maths method

- [ ] I can state closure, identity, inverse and associativity.
- [ ] I can prove or disprove group status.
- [ ] I can read a Cayley table.
- [ ] I can find group order and element period.
- [ ] I can find subgroups.
- [ ] I can apply Lagrange's theorem.
- [ ] I can identify cyclic groups and generators.
- [ ] I can test isomorphism.

## Exam technique

- [ ] I do not assume \(*\) is multiplication.
- [ ] I check identity and inverse belong to the set.
- [ ] I do not assume commutativity.
- [ ] I use Lagrange's theorem in the correct direction.
- [ ] I match identity to identity when testing isomorphism.

Final memory core:

\[
\boxed{\text{Group} = \text{set} + \text{operation} + \text{closure, identity, inverse, associativity}.}
\]
