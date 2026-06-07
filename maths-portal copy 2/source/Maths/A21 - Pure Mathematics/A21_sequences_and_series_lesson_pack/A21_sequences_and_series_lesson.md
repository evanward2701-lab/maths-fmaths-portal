# A21 Sequences and Series

## Title and Metadata

| Field | Value |
|---|---|
| Course | CCEA GCE Mathematics |
| Unit code | A21 |
| Unit name | A2 1 Pure Mathematics |
| Topic code | A21-SS |
| Topic name | Sequences and series |
| Topic slug | sequences_and_series |
| Topic Pascal | SequencesAndSeries |
| Topic ID | A21SequencesAndSeries |
| Lesson file | A21_sequences_and_series_lesson.md |

## Evidence Map

| Evidence | Lesson use |
|---|---|
| CCEA GCE Mathematics Specification Map | Authority for A21 topic boundary and LO IDs. |
| Project README / Module Map | File naming, metadata and pack structure. |
| Evidence Drop Checklist | Evidence limitations, off-spec logging and visual placeholder rules. |
| Chapter 3 transcript | Main source for teacher explanations, warnings and worked examples. |
| P2 Chapter 3 slide PDF | Slide formulas, definitions, examples and visual layout. |
| Screenshot PDF | Visual-layout evidence only because parsed text was unavailable. |

## Specification Alignment

| LO ID | Status |
|---|---|
| A21-SS-LO001 | Covered: sequences given by formulae and recurrence relations. |
| A21-SS-LO002 | Covered: convergence, divergence, oscillation/alternation, increasing, decreasing and periodic behaviour. |
| A21-SS-LO003 | Covered: sigma notation and sums of series. |
| A21-SS-LO004 | Covered: arithmetic sequences and series, including term and sum formulae. |
| A21-SS-LO005 | Covered: geometric sequences and finite geometric series. |
| A21-SS-LO006 | Covered: proofs of arithmetic and geometric series formulae. |
| A21-SS-LO007 | Covered: sum to infinity and \\(|r|<1\\). |
| A21-SS-LO008 | Gap logged: rational binomial expansion evidence not supplied. |
| A21-SS-LO009 | Covered: modelling with sequences and series. |

## Learning Objectives

By the end of this lesson, you should be able to identify arithmetic, geometric and recurrence-defined sequences; use \\(u_n\\), \\(S_n\\), \\(a\\), \\(d\\), \\(r\\) and sigma notation correctly; prove the arithmetic and geometric series formulae; work with sums to infinity; generate recurrence-defined terms; classify simple sequence behaviour; and use sequences and series in modelling.

## Prerequisite Recap

You should be confident with substitution, factorisation, solving linear and quadratic equations, simultaneous equations, inequalities, index laws, logarithms and exact fractions.

## Big Picture

A **sequence** is a list of terms. A **series** is a sum of terms in a sequence. The chapter has four engines: arithmetic structure, geometric structure, sigma notation and recurrence relations. Most exam questions are formula-selection puzzles wearing algebraic hats.

## Key Definitions and Notation

- \\(u_n\\): the \\(n\\)th term of a sequence.
- \\(n\\): the position of a term.
- \\(a\\): the first term.
- \\(d\\): the common difference of an arithmetic sequence.
- \\(r\\): the common ratio of a geometric sequence.
- \\(S_n\\): the sum of the first \\(n\\) terms.
- \\(S_\\infty\\): the sum to infinity, only when it exists.

For \\(2,5,8,11,14,\\ldots\\),
\\[
u_1=2,\quad u_2=5,\quad u_3=8,\quad u_4=11,\quad u_5=14.
\\]

## Core Theory

## 1. Types of sequences

### Arithmetic sequences

An arithmetic sequence has a common difference between terms. For
\\[
2,5,8,11,14,\\ldots
\\]
we have
\\[
+3,+3,+3,+3,
\\]
so \\(d=3\\).

For
\\[
101,94,87,80,73,\\ldots
\\]
we have
\\[
d=94-101=-7.
\\]

[VISUAL PLACEHOLDER: A21SequencesAndSeriesSVG-001 | Source: Chapter 3 slide PDF | Insert from svg/A21SequencesAndSeriesSVG-001.svg | Purpose: Show arithmetic common difference.]

### Geometric sequences

A geometric sequence has a common ratio between terms. For
\\[
3,6,12,24,48,\\ldots
\\]
we multiply by \\(2\\), so \\(r=2\\).

[VISUAL PLACEHOLDER: A21SequencesAndSeriesSVG-002 | Source: Chapter 3 slide PDF | Insert from svg/A21SequencesAndSeriesSVG-002.svg | Purpose: Show geometric common ratio.]

### Recurrence-defined sequences

The Fibonacci sequence
\\[
1,1,2,3,5,8,13,\\ldots
\\]
uses previous terms, because each new term is the sum of the two before it.

## 2. Arithmetic term formula

An arithmetic sequence has terms:

| Position | Term |
|---:|---|
| 1st | \\(a\\) |
| 2nd | \\(a+d\\) |
| 3rd | \\(a+2d\\) |
| 4th | \\(a+3d\\) |
| \\(n\\)th | \\(a+(n-1)d\\) |

So
\\[
\\boxed{u_n=a+(n-1)d.}
\\]

The \\(n-1\\) appears because the first term already exists before any common differences are added.

## 3. Worked examples: arithmetic sequences

### Example 1: first three terms and first negative term

Given
\\[
u_n=55-2n,
\\]
find the first three terms:
\\[
u_1=55-2(1)=53,
\\]
\\[
u_2=55-2(2)=51,
\\]
\\[
u_3=55-2(3)=49.
\\]
So the first three terms are
\\[
\\boxed{53,51,49.}
\\]

To find the first negative term:
\\[
55-2n<0
\\]
\\[
-2n<-55
\\]
Divide by \\(-2\\), reversing the inequality:
\\[
n>\\frac{55}{2}=27.5.
\\]
The first integer position is \\(n=28\\). Then
\\[
u_{28}=55-2(28)=55-56=-1.
\\]
So the first negative term is
\\[
\\boxed{-1}
\\]
at position
\\[
\\boxed{28.}
\\]

### Example 2: find the \\(n\\)th term

For
\\[
6,20,34,48,62,\\ldots
\\]
we have
\\[
a=6,\quad d=20-6=14.
\\]
Then
\\[
u_n=6+(n-1)14
\\]
\\[
u_n=6+14n-14
\\]
\\[
\\boxed{u_n=14n-8.}
\\]

For
\\[
101,94,87,80,73,\\ldots
\\]
we have
\\[
a=101,\quad d=94-101=-7.
\\]
Then
\\[
u_n=101+(n-1)(-7)
\\]
\\[
u_n=101-7n+7
\\]
\\[
\\boxed{u_n=108-7n.}
\\]

### Example 3: two terms determine the sequence

A sequence has form \\(u_n=an+b\\), with \\(u_3=5\\) and \\(u_8=20\\). First use the arithmetic form \\(u_n=a+(n-1)d\\).

For \\(u_3=5\\):
\\[
5=a+2d.
\\]
For \\(u_8=20\\):
\\[
20=a+7d.
\\]
Subtract:
\\[
15=5d
\\]
\\[
d=3.
\\]
Substitute into \\(5=a+2d\\):
\\[
5=a+6
\\]
\\[
a=-1.
\\]
Then
\\[
u_n=-1+(n-1)3=-1+3n-3=3n-4.
\\]
Comparing with \\(u_n=an+b\\),
\\[
\\boxed{a=3,\quad b=-4.}
\\]

### Example 4: expressions form an arithmetic sequence

For
\\[
-8,\quad x^2,\quad 17x
\\]
to be arithmetic, consecutive differences must be equal:
\\[
x^2-(-8)=17x-x^2.
\\]
So
\\[
x^2+8=17x-x^2
\\]
\\[
2x^2-17x+8=0
\\]
\\[
(2x-1)(x-8)=0.
\\]
Therefore
\\[
\\boxed{x=\\frac12\text{ or }x=8.}
\\]

## 4. Arithmetic series

A series is a sum of terms in a sequence. For an arithmetic series,
\\[
\\boxed{S_n=\\frac n2(2a+(n-1)d).}
\\]

### Proof of the arithmetic series formula

Write the sum forwards:
\\[
S_n=a+(a+d)+(a+2d)+\\cdots+(a+(n-2)d)+(a+(n-1)d).
\\]
Write it backwards:
\\[
S_n=(a+(n-1)d)+(a+(n-2)d)+\\cdots+(a+d)+a.
\\]
Add the two rows. The first pair is
\\[
a+(a+(n-1)d)=2a+(n-1)d.
\\]
The second pair is
\\[
(a+d)+(a+(n-2)d)=2a+d+(n-2)d=2a+(n-1)d.
\\]
Every opposite pair has the same total, and there are \\(n\\) pairs, so
\\[
2S_n=n(2a+(n-1)d).
\\]
Divide by \\(2\\):
\\[
\\boxed{S_n=\\frac n2(2a+(n-1)d).}
\\]

[VISUAL PLACEHOLDER: A21SequencesAndSeriesSVG-003 | Source: Chapter 3 slide PDF page 11 | Insert from svg/A21SequencesAndSeriesSVG-003.svg | Purpose: Show reverse pairing proof.]

If the last term is \\(L\\), then
\\[
\\boxed{S_n=\\frac n2(a+L).}
\\]

## 5. Arithmetic series examples

For
\\[
2+5+8+11+14
\\]
write the sum forwards and backwards:
\\[
S_5=2+5+8+11+14,
\\]
\\[
S_5=14+11+8+5+2.
\\]
Then
\\[
2S_5=16+16+16+16+16=80,
\\]
so
\\[
\\boxed{S_5=40.}
\\]

For the first \\(30\\) terms of
\\[
2+5+8+11+\\cdots,
\\]
\\[
n=30,\quad a=2,\quad d=3.
\\]
\\[
S_{30}=\\frac{30}{2}(2(2)+(30-1)3)
\\]
\\[
S_{30}=15(4+87)=15(91)=\\boxed{1365.}
\\]

For
\\[
100+98+96+\\cdots
\\]
with \\(30\\) terms,
\\[
n=30,\quad a=100,\quad d=-2.
\\]
\\[
S_{30}=15(200+29(-2))=15(142)=\\boxed{2130.}
\\]

For
\\[
p+2p+3p+\\cdots
\\]
with \\(30\\) terms,
\\[
n=30,\quad a=p,\quad d=p.
\\]
\\[
S_{30}=15(2p+29p)=15(31p)=\\boxed{465p.}
\\]

## 6. Geometric sequences

A geometric sequence multiplies by a fixed common ratio \\(r\\). To find \\(r\\), divide a term by the previous term:
\\[
r=\\frac{\\text{term after}}{\\text{term before}}.
\\]
For
\\[
27,18,12,8,\\ldots
\\]
\\[
r=\\frac{18}{27}=\\frac23.
\\]

A negative common ratio gives alternating terms. For
\\[
5,-5,5,-5,\\ldots
\\]
\\[
r=-1.
\\]

For
\\[
x,-2x^2,4x^3,\\ldots
\\]
\\[
r=\\frac{-2x^2}{x}=-2x,
\\]
and
\\[
\\frac{4x^3}{-2x^2}=-2x.
\\]

[VISUAL PLACEHOLDER: A21SequencesAndSeriesSVG-004 | Source: Chapter 3 geometric sequence evidence | Insert from svg/A21SequencesAndSeriesSVG-004.svg | Purpose: Show common ratio by division.]

## 7. Geometric term formula

For a geometric sequence:

| Position | Term |
|---:|---|
| 1st | \\(a\\) |
| 2nd | \\(ar\\) |
| 3rd | \\(ar^2\\) |
| 4th | \\(ar^3\\) |
| \\(n\\)th | \\(ar^{n-1}\\) |

So
\\[
\\boxed{u_n=ar^{n-1}.}
\\]

## 8. Worked examples: geometric sequences

### Example 9: second and fourth terms

Suppose \\(u_2=4\\), \\(u_4=8\\), and \\(r>0\\).

Using \\(u_n=ar^{n-1}\\):
\\[
4=ar,
\\]
\\[
8=ar^3.
\\]
Divide:
\\[
\\frac{ar^3}{ar}=\\frac84
\\]
\\[
r^2=2.
\\]
Since \\(r>0\\),
\\[
\\boxed{r=\\sqrt2.}
\\]
Now
\\[
4=a\\sqrt2
\\]
\\[
a=\\frac4{\\sqrt2}=\\frac{4\\sqrt2}{2}=\\boxed{2\\sqrt2.}
\\]
The tenth term is
\\[
u_{10}=ar^9=2\\sqrt2(\\sqrt2)^9=2(\\sqrt2)^{10}=2(2^5)=\\boxed{64.}
\\]

### Example 10: expressions form a positive geometric sequence

For
\\[
3,\quad x,\quad x+6
\\]
to be geometric:
\\[
\\frac{x}{3}=\\frac{x+6}{x}.
\\]
Cross-multiply:
\\[
x^2=3(x+6)=3x+18
\\]
\\[
x^2-3x-18=0
\\]
\\[
(x-6)(x+3)=0.
\\]
So \\(x=6\\) or \\(x=-3\\). Since the sequence is positive,
\\[
\\boxed{x=6.}
\\]
Then \\(a=3\\), \\(r=2\\), and
\\[
u_{10}=3(2)^9=3(512)=\\boxed{1536.}
\\]

### Example 11: first term exceeding one million

For
\\[
3,6,12,24,\\ldots
\\]
\\[
a=3,\quad r=2,
\\]
so
\\[
u_n=3(2)^{n-1}.
\\]
Solve
\\[
3(2)^{n-1}>1,000,000.
\\]
Divide by \\(3\\):
\\[
2^{n-1}>\\frac{1,000,000}{3}.
\\]
Take logs:
\\[
(n-1)\\ln2>\\ln\\left(\\frac{1,000,000}{3}\\right).
\\]
Thus
\\[
n-1>\\frac{\\ln(1,000,000/3)}{\\ln2}=18.3466\\ldots
\\]
so
\\[
n>19.3466\\ldots
\\]
and the first integer is \\(n=20\\). Then
\\[
u_{20}=3(2)^{19}=3(524288)=\\boxed{1572864.}
\\]

### Example 12: third and fifth terms

If \\(u_3=20\\), \\(u_5=80\\), and all terms are positive:
\\[
20=ar^2,
\\]
\\[
80=ar^4.
\\]
Divide:
\\[
r^2=4.
\\]
Since terms are positive,
\\[
r=2.
\\]
Then
\\[
20=a(2)^2=4a,
\\]
so
\\[
a=5.
\\]
The twentieth term is
\\[
u_{20}=5(2)^{19}=5(524288)=\\boxed{2621440.}
\\]

### Example 13: second, third and fourth terms are expressions

For
\\[
x,\quad x+6,\quad 5x-6
\\]
set ratios equal:
\\[
\\frac{x+6}{x}=\\frac{5x-6}{x+6}.
\\]
Cross-multiply:
\\[
(x+6)^2=x(5x-6).
\\]
Expand:
\\[
x^2+12x+36=5x^2-6x.
\\]
Move all terms:
\\[
0=4x^2-18x-36.
\\]
Divide by \\(2\\):
\\[
2x^2-9x-18=0.
\\]
Factorise:
\\[
(2x+3)(x-6)=0.
\\]
Therefore
\\[
\\boxed{x=-\\frac32\text{ or }x=6.}
\\]

## 9. Geometric series

For a geometric sequence
\\[
a,ar,ar^2,ar^3,\\ldots
\\]
the geometric series is
\\[
a+ar+ar^2+ar^3+\\cdots.
\\]
The finite sum formula is
\\[
\\boxed{S_n=\\frac{a(1-r^n)}{1-r}.}
\\]
Equivalently,
\\[
\\boxed{S_n=\\frac{a(r^n-1)}{r-1}.}
\\]

## 10. Proof of the finite geometric series formula

Start with
\\[
S_n=a+ar+ar^2+\\cdots+ar^{n-2}+ar^{n-1}.
\\]
Multiply by \\(r\\):
\\[
rS_n=ar+ar^2+ar^3+\\cdots+ar^{n-1}+ar^n.
\\]
Subtract:
\\[
S_n-rS_n=a-ar^n.
\\]
Factorise:
\\[
S_n(1-r)=a(1-r^n).
\\]
Divide by \\(1-r\\):
\\[
\\boxed{S_n=\\frac{a(1-r^n)}{1-r}.}
\\]

[VISUAL PLACEHOLDER: A21SequencesAndSeriesSVG-005 | Source: Chapter 3 geometric series proof | Insert from svg/A21SequencesAndSeriesSVG-005.svg | Purpose: Show cancellation proof.]

## 11. Worked examples: finite geometric series

For the first ten terms of
\\[
3+6+12+\\cdots,
\\]
\\[
a=3,\quad r=2,\quad n=10.
\\]
\\[
S_{10}=\\frac{3(1-2^{10})}{1-2}=\\frac{3(1-1024)}{-1}=\\boxed{3069.}
\\]

For the first ten terms of
\\[
4+2+1+\\cdots,
\\]
\\[
a=4,\quad r=\\frac12,\quad n=10.
\\]
\\[
S_{10}=\\frac{4(1-(1/2)^{10})}{1-1/2}
\\]
\\[
=\\frac{4(1-1/1024)}{1/2}
=4\\left(\\frac{1023}{1024}\\right)2
=\\frac{1023}{128}.
\\]
So
\\[
\\boxed{S_{10}=\\frac{1023}{128}.}
\\]

Find the least \\(n\\) such that
\\[
1+2+4+\\cdots
\\]
exceeds \\(2,000,000\\). Since
\\[
S_n=\\frac{1(1-2^n)}{1-2}=2^n-1,
\\]
we need
\\[
2^n-1>2,000,000.
\\]
Thus
\\[
2^n>2,000,001.
\\]
Taking logs:
\\[
n>\\frac{\\ln(2,000,001)}{\\ln2}=20.9315\\ldots
\\]
so
\\[
\\boxed{n=21.}
\\]

If \\(u_2=192\\) and \\(u_3=144\\), then
\\[
r=\\frac{144}{192}=\\frac34.
\\]
Since \\(u_2=ar\\),
\\[
192=a\\left(\\frac34\\right),
\\]
so
\\[
a=192\\cdot\\frac43=\\boxed{256.}
\\]
Then
\\[
S_n=\\frac{256(1-(3/4)^n)}{1-3/4}=1024\\left(1-\\left(\\frac34\\right)^n\\right).
\\]
For \\(S_n>1000\\):
\\[
1024\\left(1-\\left(\\frac34\\right)^n\\right)>1000
\\]
\\[
1-\\left(\\frac34\\right)^n>\\frac{125}{128}
\\]
\\[
-\\left(\\frac34\\right)^n>-\\frac3{128}
\\]
\\[
\\left(\\frac34\\right)^n<\\frac3{128}.
\\]
Taking logs:
\\[
n\\ln\\left(\\frac34\\right)<\\ln\\left(\\frac3{128}\\right).
\\]
Since \\(\\ln(3/4)<0\\), divide and reverse:
\\[
n>\\frac{\\ln(3/128)}{\\ln(3/4)}=13.0401\\ldots
\\]
so
\\[
\\boxed{n=14.}
\\]

## 12. Sum to infinity

A geometric series has a finite sum to infinity only when
\\[
\\boxed{|r|<1.}
\\]
From
\\[
S_n=\\frac{a(1-r^n)}{1-r},
\\]
if \\(|r|<1\\), then
\\[
r^n\\to0.
\\]
So
\\[
S_\\infty=\\frac{a(1-0)}{1-r},
\\]
therefore
\\[
\\boxed{S_\\infty=\\frac{a}{1-r},\quad |r|<1.}
\\]

[VISUAL PLACEHOLDER: A21SequencesAndSeriesSVG-006 | Source: Chapter 3 sum-to-infinity evidence | Insert from svg/A21SequencesAndSeriesSVG-006.svg | Purpose: Show convergence when \\(|r|<1\\).]

[VISUAL PLACEHOLDER: A21SequencesAndSeriesSVG-007 | Source: Chapter 3 optional intuition | Insert from svg/A21SequencesAndSeriesSVG-007.svg | Purpose: Area intuition for \\(1+1/2+1/4+\\cdots=2\\).]

## 13. Sum to infinity examples

For
\\[
1+\\frac12+\\frac14+\\frac18+\\cdots,
\\]
\\[
a=1,\quad r=\\frac12,\quad |r|<1.
\\]
\\[
S_\\infty=\\frac{1}{1-1/2}=\\frac{1}{1/2}=\\boxed{2.}
\\]

For
\\[
27-9+3-1+\\cdots,
\\]
\\[
a=27,\quad r=\\frac{-9}{27}=-\\frac13.
\\]
Since \\(|r|=1/3<1\\),
\\[
S_\\infty=\\frac{27}{1-(-1/3)}=\\frac{27}{4/3}=27\\cdot\\frac34=\\boxed{\\frac{81}{4}}.
\\]

For
\\[
p+p^2+p^3+\\cdots,\quad -1<p<1,
\\]
we have \\(a=p\\), \\(r=p\\), and \\(|p|<1\\). Therefore
\\[
\\boxed{S_\\infty=\\frac{p}{1-p}.}
\\]

For
\\[
p+1+\\frac1p+\\cdots,
\\]
we have \\(a=p\\), \\(r=1/p\\). Then
\\[
S_\\infty=\\frac{p}{1-1/p}=\\frac{p}{(p-1)/p}=\\boxed{\\frac{p^2}{p-1}}.
\\]

If \\(u_4=1.08\\) and \\(u_7=0.23328\\), then
\\[
1.08=ar^3,
\\]
\\[
0.23328=ar^6.
\\]
Divide:
\\[
r^3=\\frac{0.23328}{1.08}=0.216.
\\]
So
\\[
r=\\sqrt[3]{0.216}=0.6.
\\]
Since \\(|0.6|<1\\), the series converges. Then
\\[
1.08=a(0.6)^3=a(0.216),
\\]
so
\\[
a=\\frac{1.08}{0.216}=5.
\\]
Thus
\\[
S_\\infty=\\frac5{1-0.6}=\\frac5{0.4}=\\boxed{12.5.}
\\]

If \\(S_4=15\\) and \\(S_\\infty=16\\), then
\\[
15=\\frac{a(1-r^4)}{1-r},\quad 16=\\frac{a}{1-r}.
\\]
So
\\[
15=16(1-r^4).
\\]
\\[
\\frac{15}{16}=1-r^4.
\\]
\\[
r^4=\\frac1{16}.
\\]
Therefore
\\[
r=\\pm\\frac12.
\\]
If all terms are positive, \\(r=1/2\\). Then
\\[
16=\\frac{a}{1-1/2}=\\frac{a}{1/2},
\\]
so
\\[
\\boxed{a=8.}
\\]

If
\\[
S_\\infty=\\frac87S_6,
\\]
then
\\[
\\frac{a}{1-r}=\\frac87\\left(\\frac{a(1-r^6)}{1-r}\\right).
\\]
Cancel \\(a/(1-r)\\):
\\[
1=\\frac87(1-r^6).
\\]
\\[
7=8(1-r^6).
\\]
\\[
\\frac78=1-r^6.
\\]
\\[
r^6=\\frac18.
\\]
Taking the cube root:
\\[
r^2=\\frac12.
\\]
Thus
\\[
r=\\pm\\sqrt{\\frac12}=\\boxed{\\pm\\frac1{\\sqrt2}},
\\]
and \\(k=2\\).

## 14. Sigma notation

Sigma notation is a compact way to write a sum:
\\[
\\sum.
\\]
For example,
\\[
\\sum_{r=1}^{5}(2r+1)
\\]
means use \\(r=1,2,3,4,5\\) and add the results:
\\[
(2(1)+1)+(2(2)+1)+(2(3)+1)+(2(4)+1)+(2(5)+1).
\\]
So
\\[
=3+5+7+9+11=\\boxed{35.}
\\]
The letter \\(r\\) is a dummy variable. The same sum could be written using \\(k\\):
\\[
\\sum_{k=1}^{5}(2k+1).
\\]

For
\\[
\\sum_{k=5}^{15}(10-2k),
\\]
the values are \\(5,6,\\ldots,15\\). There are
\\[
15-5+1=11
\\]
terms. In general, from \\(m\\) to \\(N\\), the number of terms is
\\[
\\boxed{N-m+1.}
\\]

[VISUAL PLACEHOLDER: A21SequencesAndSeriesSVG-008 | Source: Chapter 3 sigma notation evidence | Insert from svg/A21SequencesAndSeriesSVG-008.svg | Purpose: Break down sigma notation.]

## 15. Sigma notation examples

Evaluate
\\[
\\sum_{n=1}^{7}3n.
\\]
Expand:
\\[
3+6+9+12+15+18+21.
\\]
This is arithmetic with \\(a=3\\), \\(L=21\\), \\(n=7\\). Thus
\\[
S_7=\\frac72(3+21)=\\frac72(24)=\\boxed{84.}
\\]

Evaluate
\\[
\\sum_{k=5}^{15}(10-2k).
\\]
There are \\(15-5+1=11\\) terms. First term:
\\[
10-2(5)=0.
\\]
Last term:
\\[
10-2(15)=-20.
\\]
So
\\[
S_{11}=\\frac{11}{2}(0-20)=11(-10)=\\boxed{-110.}
\\]

Evaluate
\\[
\\sum_{k=1}^{12}5\cdot3^{k-1}.
\\]
The terms are
\\[
5,15,45,\\ldots
\\]
so \\(a=5\\), \\(r=3\\), \\(n=12\\). Hence
\\[
S_{12}=\\frac{5(1-3^{12})}{1-3}.
\\]
Since \\(3^{12}=531441\\),
\\[
S_{12}=\\frac{5(1-531441)}{-2}=\\frac{-2657200}{-2}=\\boxed{1328600.}
\\]

Evaluate
\\[
\\sum_{r=10}^{30}(7+2r).
\\]
First term:
\\[
7+2(10)=27.
\\]
Last term:
\\[
7+2(30)=67.
\\]
Number of terms:
\\[
30-10+1=21.
\\]
So
\\[
S_{21}=\\frac{21}{2}(27+67)=\\frac{21}{2}(94)=21(47)=\\boxed{987.}
\\]
Alternatively,
\\[
\\sum_{r=10}^{30}(7+2r)=\\sum_{r=1}^{30}(7+2r)-\\sum_{r=1}^{9}(7+2r).
\\]

## 16. Recurrence relations

A recurrence relation defines each term using previous terms. This differs from a position-to-term formula.

For a position formula such as
\\[
u_n=2n+3,
\\]
we find \\(u_{50}\\) directly:
\\[
u_{50}=2(50)+3=103.
\\]

For a recurrence relation such as
\\[
u_{n+1}=2u_n+4,\quad u_1=3,
\\]
each term uses the previous term:
\\[
u_2=2u_1+4=2(3)+4=10,
\\]
\\[
u_3=2u_2+4=2(10)+4=24,
\\]
\\[
u_4=2u_3+4=2(24)+4=52.
\\]
So the sequence begins
\\[
3,10,24,52,\\ldots
\\]
It is not arithmetic, because the differences are \\(7,14,28\\). It is not geometric either, because the ratios are not constant.

[VISUAL PLACEHOLDER: A21SequencesAndSeriesSVG-009 | Source: Chapter 3 recurrence relation evidence | Insert from svg/A21SequencesAndSeriesSVG-009.svg | Purpose: Compare position-to-term and recurrence definitions.]

## 17. Recurrence worked examples

A sequence is defined by
\\[
x_1=1,\quad x_{n+1}=x_n^2-kx_n.
\\]
Find \\(x_2\\):
\\[
x_2=x_1^2-kx_1=1^2-k(1)=\\boxed{1-k.}
\\]
Find \\(x_3\\):
\\[
x_3=x_2^2-kx_2=(1-k)^2-k(1-k).
\\]
Expand:
\\[
(1-k)^2=1-2k+k^2,
\\]
\\[
-k(1-k)=-k+k^2.
\\]
So
\\[
x_3=1-2k+k^2-k+k^2=\\boxed{1-3k+2k^2.}
\\]
If \\(x_3=1\\), then
\\[
1=1-3k+2k^2
\\]
\\[
0=2k^2-3k
\\]
\\[
0=k(2k-3).
\\]
So
\\[
\\boxed{k=0\text{ or }k=\\frac32.}
\\]
For \\(k=3/2\\),
\\[
x_1=1,\quad x_2=1-\\frac32=-\\frac12,\quad x_3=1.
\\]
The terms repeat:
\\[
1,-\\frac12,1,-\\frac12,\\ldots
\\]
One pair sums to
\\[
1-\\frac12=\\frac12.
\\]
There are \\(50\\) pairs in \\(100\\) terms, so
\\[
\\sum_{n=1}^{100}x_n=50\\left(\\frac12\\right)=\\boxed{25.}
\\]

For
\\[
a_1=3,\quad a_{n+1}=\\frac{a_n-3}{a_n-2},
\\]
generate terms:
\\[
a_2=\\frac{3-3}{3-2}=0,
\\]
\\[
a_3=\\frac{0-3}{0-2}=\\frac32,
\\]
\\[
a_4=\\frac{\\frac32-3}{\\frac32-2}=\\frac{-3/2}{-1/2}=3.
\\]
So the repeating block is
\\[
3,0,\\frac32.
\\]
One block sums to
\\[
3+0+\\frac32=\\frac92.
\\]
Since
\\[
100=33\cdot3+1,
\\]
there are \\(33\\) full blocks and one extra term \\(3\\). Thus
\\[
\\sum_{r=1}^{100}a_r=33\\left(\\frac92\\right)+3=\\frac{297}{2}+\\frac62=\\boxed{\\frac{303}{2}}.
\\]
Also,
\\[
\\sum_{r=1}^{99}a_r=33\\left(\\frac92\\right)=\\frac{297}{2}.
\\]
Therefore
\\[
\\sum_{r=1}^{100}a_r+\\sum_{r=1}^{99}a_r=\\frac{303}{2}+\\frac{297}{2}=\\boxed{300.}
\\]

## 18. Increasing, decreasing and periodic sequences

A sequence is strictly increasing if
\\[
u_{n+1}>u_n.
\\]
A sequence is strictly decreasing if
\\[
u_{n+1}<u_n.
\\]
A sequence is periodic if a block repeats, for example
\\[
2,3,0,2,3,0,\\ldots
\\]
has order \\(3\\).

[VISUAL PLACEHOLDER: A21SequencesAndSeriesSVG-010 | Source: Chapter 3 behaviour evidence | Insert from svg/A21SequencesAndSeriesSVG-010.svg | Purpose: Compare increasing, decreasing and periodic sequences.]

Examples:

If
\\[
u_{n+1}=u_n+3,\quad u_1=7,
\\]
then
\\[
7,10,13,16,\\ldots
\\]
so the sequence is increasing.

If
\\[
u_{n+1}=u_n^2,\quad u_1=\\frac12,
\\]
then
\\[
\\frac12,\\frac14,\\frac1{16},\\frac1{256},\\ldots
\\]
so the sequence is decreasing.

If
\\[
u_{n+1}=\\sin(90^\\circ n),
\\]
then for \\(n=0,1,2,3,4,\\ldots\\):
\\[
0,1,0,-1,0,1,0,-1,\\ldots
\\]
so it is periodic of order \\(4\\).

## 19. Modelling with sequences and series

Use an arithmetic model when a quantity changes by a fixed amount. Use a geometric model when a quantity changes by a fixed multiplier or percentage.

[VISUAL PLACEHOLDER: A21SequencesAndSeriesSVG-011 | Source: Chapter 3 modelling evidence | Insert from svg/A21SequencesAndSeriesSVG-011.svg | Purpose: Show arithmetic versus geometric model choice.]

### Arithmetic profit model with a cap

Bruce has profits of \\(£20,000\\) in year \\(1\\), increasing by \\(£5000\\) each year until reaching \\(£100,000\\), then remaining there. Find the total over \\(20\\) years.

Here
\\[
a=20000,\quad d=5000.
\\]
Find the year when profit reaches \\(100000\\):
\\[
100000=20000+(n-1)5000.
\\]
Subtract \\(20000\\):
\\[
80000=(n-1)5000.
\\]
Divide by \\(5000\\):
\\[
16=n-1.
\\]
So
\\[
n=17.
\\]
Sum the first \\(17\\) years:
\\[
S_{17}=\\frac{17}{2}(20000+100000)=17(60000)=1020000.
\\]
The final \\(3\\) years add
\\[
3(100000)=300000.
\\]
Total:
\\[
1020000+300000=\\boxed{£1,320,000.}
\\]
One limitation: profits are unlikely to increase by exactly the same amount every year.

### Geometric profit model

If yearly profits start at \\(£20,000\\) and increase by \\(5\\%\\) per annum, then
\\[
a=20000,\quad r=1.05,\quad n=20.
\\]
Use
\\[
S_{20}=\\frac{20000(1.05^{20}-1)}{1.05-1}.
\\]
So
\\[
S_{20}=\\boxed{£661,319.08}\quad\text{to the nearest penny.}
\\]

### Paper folding model

A sheet has thickness \\(0.5\\) mm and each fold doubles the thickness. This is geometric:
\\[
a=0.5,\quad r=2.
\\]
After four folds:
\\[
0.5\times2^4=0.5(16)=\\boxed{8\text{ mm}.}
\\]
After twenty folds:
\\[
0.5\times2^{20}=0.5(1048576)=\\boxed{524288\text{ mm}}=524.288\text{ m}.
\\]
One limitation: it is impossible to fold the paper that many times.

## Interactive Placeholders

[INTERACTIVE PLACEHOLDER: A21SequencesAndSeriesWidget-001 | Source: Chapter 3 sigma notation evidence | Insert from widgets/A21SequencesAndSeriesWidget-001.html | Purpose: Let the student expand a sigma sum and identify whether it is arithmetic or geometric.]

[INTERACTIVE PLACEHOLDER: A21SequencesAndSeriesWidget-002 | Source: Chapter 3 recurrence relation evidence | Insert from widgets/A21SequencesAndSeriesWidget-002.html | Purpose: Let the student input a recurrence relation and generate terms, spotting cycles.]

[INTERACTIVE PLACEHOLDER: A21SequencesAndSeriesWidget-003 | Source: Chapter 3 modelling evidence | Insert from widgets/A21SequencesAndSeriesWidget-003.html | Purpose: Compare arithmetic and geometric models over time.]

## 20. Guided Practice

1. An arithmetic sequence begins \\(7,12,17,22,\\ldots\\). Find \\(a\\), \\(d\\), \\(u_n\\), and \\(u_{40}\\).
2. Find the sum of the first \\(50\\) terms of \\(4+9+14+19+\\cdots\\).
3. The \\(n\\)th term is \\(u_n=73-4n\\). Find the first negative term.
4. A geometric sequence has \\(a=6\\), \\(r=3\\). Find \\(u_n\\), \\(u_8\\), and \\(S_8\\).
5. A geometric sequence has \\(u_3=18\\), \\(u_5=162\\), and positive \\(r\\). Find \\(r\\), \\(a\\), and \\(u_{10}\\).
6. Find the sum to infinity of \\(12-6+3-\\frac32+\\cdots\\), and state why it converges.
7. Evaluate \\(\\sum_{r=4}^{20}(3r-5)\\).
8. Given \\(x_1=2\\), \\(x_{n+1}=3x_n-1\\), find \\(x_2,x_3,x_4\\) and classify the sequence.
9. The sequence \\(2,-1,4,2,-1,4,\\ldots\\) repeats. Find \\(\\sum_{r=1}^{100}a_r\\).
10. A company earns \\(£30,000\\) in year \\(1\\), increasing by \\(4\\%\\) each year. Find the total over \\(10\\) years and state a limitation.

## 21. Full Worked Solutions

1. \\(a=7\\), \\(d=5\\). Then \\(u_n=7+(n-1)5=5n+2\\), so \\(u_{40}=5(40)+2=\\boxed{202}\\).
2. \\(a=4\\), \\(d=5\\), \\(n=50\\). \\(S_{50}=25(8+49(5))=25(253)=\\boxed{6325}\\).
3. \\(73-4n<0\\), so \\(-4n<-73\\). Divide by \\(-4\\): \\(n>18.25\\). First integer \\(n=19\\), so \\(u_{19}=73-76=\\boxed{-3}\\).
4. \\(u_n=6\cdot3^{n-1}\\). \\(u_8=6\cdot3^7=13122\\). \\(S_8=\\frac{6(1-3^8)}{1-3}=\\boxed{19680}\\).
5. \\(18=ar^2\\), \\(162=ar^4\\). Divide: \\(r^2=9\\), positive \\(r=3\\). Then \\(18=9a\\), so \\(a=2\\). \\(u_{10}=2(3)^9=\\boxed{39366}\\).
6. \\(a=12\\), \\(r=-1/2\\), \\(|r|<1\\). \\(S_\\infty=\\frac{12}{1-(-1/2)}=\\frac{12}{3/2}=\\boxed{8}\\).
7. Terms from \\(r=4\\) to \\(20\\): \\(n=17\\). First term \\(7\\), last term \\(55\\). \\(S=\\frac{17}{2}(62)=\\boxed{527}\\).
8. \\(x_2=3(2)-1=5\\), \\(x_3=3(5)-1=14\\), \\(x_4=3(14)-1=41\\). Differences are \\(3,9,27\\), ratios are not constant, so neither arithmetic nor geometric.
9. One block sums to \\(2-1+4=5\\). Since \\(100=33\cdot3+1\\), sum is \\(33(5)+2=\\boxed{167}\\).
10. \\(a=30000\\), \\(r=1.04\\), \\(n=10\\). \\(S_{10}=\\frac{30000(1.04^{10}-1)}{0.04}=\\boxed{£360,183.21}\\) to nearest penny. Limitation: the model assumes exactly \\(4\\%\\) growth each year.

## 22. Common Mistakes and Exam Traps

- Confusing \\(u_n\\) and \\(S_n\\).
- Using \\(n\\) instead of \\(n-1\\) in term formulae.
- Forgetting that decreasing arithmetic sequences have negative \\(d\\).
- Forgetting to reverse inequalities after dividing by a negative number.
- Using \\(S_\\infty=\\frac{a}{1-r}\\) without first checking \\(|r|<1\\).
- Counting sigma terms as upper minus lower instead of upper minus lower plus one.
- Forcing recurrence relations into arithmetic/geometric formulae.
- Treating cross-board extension material as CCEA core.

## 23. Exam Technique Summary

Ask first: **term or sum?** Then ask: **arithmetic, geometric, sigma or recurrence?**

Formula bank:
\\[
u_n=a+(n-1)d
\\]
\\[
S_n=\\frac n2(2a+(n-1)d)
\\]
\\[
S_n=\\frac n2(a+L)
\\]
\\[
u_n=ar^{n-1}
\\]
\\[
S_n=\\frac{a(1-r^n)}{1-r}
\\]
\\[
S_\\infty=\\frac a{1-r},\quad |r|<1.
\\]

## 24. Syllabus Gap Check

| LO ID | Status | Evidence-backed coverage |
|---|---|---|
| A21-SS-LO001 | Covered | Formula-defined and recurrence-defined sequences. |
| A21-SS-LO002 | Covered | Convergence, divergence, oscillation/alternation, periodic behaviour. |
| A21-SS-LO003 | Covered | Sigma notation and sums of series. |
| A21-SS-LO004 | Covered | Arithmetic sequences and series. |
| A21-SS-LO005 | Covered | Geometric sequences and finite geometric series. |
| A21-SS-LO006 | Covered | Proofs of arithmetic and geometric series formulae. |
| A21-SS-LO007 | Covered | Sum to infinity and \\(|r|<1\\). |
| A21-SS-LO008 | Gap logged | Rational binomial expansion evidence missing. |
| A21-SS-LO009 | Covered | Modelling with sequences and series. |

## 25. Off-Spec Content Found but Excluded

| Evidence item | Decision |
|---|---|
| Taylor series | Excluded from core; Further Mathematics-style enrichment. |
| Harmonic series deep exploration | Excluded from core. |
| STEP / MAT / AEA extension | Logged as enrichment only. |
| Long modular arithmetic progression extension | Excluded from required core. |
| Rational binomial expansion | Officially on-spec, but evidence missing, so logged as a gap rather than invented. |

## 26. Visual and Interactive Asset Plan

| Asset ID | Type | Purpose |
|---|---|---|
| A21SequencesAndSeriesMermaid-001 | Mermaid | Formula-selection flowchart. |
| A21SequencesAndSeriesMermaid-002 | Mermaid | Modelling decision tree. |
| A21SequencesAndSeriesSVG-001 to 011 | SVG | Sequence, proof, convergence, sigma, recurrence and modelling visuals. |
| A21SequencesAndSeriesTikZ-001 | TikZ | Arithmetic series pairing proof. |
| A21SequencesAndSeriesTikZ-002 | TikZ | Geometric convergence plot. |
| A21SequencesAndSeriesWidget-001 | Widget | Sigma explorer. |
| A21SequencesAndSeriesWidget-002 | Widget | Recurrence generator. |
| A21SequencesAndSeriesWidget-003 | Widget | Modelling comparator. |

## 27. Supplementary Sources Used

Cross-board examples were used only where the mathematics matches CCEA A21-SS. Further Maths references, Taylor series, STEP/MAT/AEA-style extension and harmonic-series enrichment were not treated as required CCEA core.

## 28. Final Student Checklist

- [ ] I can identify arithmetic sequences and use \\(u_n=a+(n-1)d\\).
- [ ] I can use both arithmetic series formulae.
- [ ] I can prove the arithmetic series formula by reversing and adding.
- [ ] I can identify geometric sequences and use \\(u_n=ar^{n-1}\\).
- [ ] I can use \\(S_n=\\frac{a(1-r^n)}{1-r}\\).
- [ ] I can prove the geometric series formula using \\(S_n-rS_n\\).
- [ ] I can use \\(S_\\infty=\\frac a{1-r}\\) only when \\(|r|<1\\).
- [ ] I can expand and evaluate sigma notation.
- [ ] I can generate terms from recurrence relations and spot cycles.
- [ ] I can distinguish increasing, decreasing and periodic sequences.
- [ ] I can model fixed changes arithmetically and percentage changes geometrically.
- [ ] I know that \\(A21-SS-LO008\\) rational binomial expansion needs extra evidence for completion.
