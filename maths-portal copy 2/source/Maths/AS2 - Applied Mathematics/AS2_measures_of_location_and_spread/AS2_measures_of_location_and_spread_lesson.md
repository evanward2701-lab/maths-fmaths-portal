# Measures of Location and Spread

## Title and Metadata

| Field | Value |
|---|---|
| Course | CCEA GCE Mathematics |
| Unit code | `AS2` |
| Unit name | AS 2 Applied Mathematics |
| Applied section | Statistics |
| Official topic code | `AS2-DPI` |
| Official topic name | Data presentation and interpretation |
| Lesson topic | Measures of Location and Spread |
| Topic slug | `measures_of_location_and_spread` |
| Topic Pascal | `MeasuresOfLocationAndSpread` |
| Topic ID | `AS2MeasuresOfLocationAndSpread` |
| Lesson file | `AS2_measures_of_location_and_spread_lesson.md` |
| Core LO IDs | `AS2-DPI-LO002`, `AS2-DPI-LO003` |
| Supporting LO IDs | `AS2-DPI-LO008`, `AS2-DPI-LO010` |

## Evidence Map

| Evidence source | Used for | Status |
|---|---|---|
| CCEA GCE Mathematics Specification Map | Unit, topic, LO IDs, boundaries | Core authority |
| README Module Map | File conventions, metadata conventions, phase structure | Project authority |
| Source Evidence Drop Checklist | Evidence logging, off-spec logging, visual placeholder rules | Project authority |
| `S1-Chp2-MeasuresOfLocationAndSpread.pdf` | Slide content: definitions, examples, warnings, visual diagrams | Cross-board support, CCEA-filtered |
| `Chapter_2_Measures_of_Location_&_Spread_Transcript.md` | Teacher explanation, worked methods, calculator notes, warnings | Cross-board support, CCEA-filtered |
| Screenshots PDF | Visual evidence for early slides and handwritten annotations | Partial visual support |

## Specification Alignment

### `AS2-DPI-LO002`

> Interpret measures of central tendency and variation, including standard deviation and variance.

This lesson covers measures of central tendency, measures of location, measures of spread, interpretation of spread as similarity/variability, and interpretation of changes to the mean and median when a data value changes.

### `AS2-DPI-LO003`

> Calculate standard deviation and variance of a population or sample, including from summary statistics.

This lesson covers mean from listed data, mean from ungrouped frequency tables, estimated mean from grouped frequency tables using midpoints, median from listed and grouped data, linear interpolation for grouped medians, standard deviation and variance using summary statistics, and calculator statistics mode where appropriate.

### Supporting links

`AS2-DPI-LO008` supports IQR-based outlier work, so quartiles and IQR are included as core-supporting statistics. `AS2-DPI-LO010` supports missing-data awareness, but missing data is not the centre of this lesson.

## Learning Objectives

By the end of this lesson, the student should be able to:

1. Explain the difference between a statistical variable and an algebraic variable.
2. Distinguish measures of central tendency, location and spread.
3. Calculate and interpret \(\bar{x}\), \(\sum x\), \(n\), \(\sum fx\), \(\sum f\), variance and standard deviation.
4. Use midpoints to estimate the mean from grouped data.
5. Explain why grouped-data means are estimates.
6. Find the correct median and quartile positions for listed and grouped data.
7. Use linear interpolation to estimate medians and quartiles from grouped data.
8. Calculate and interpret range, IQR and standard deviation.
9. Know which calculator outputs may be used directly and which must not be used for grouped medians/quartiles.
10. Recognise boundary-risk enrichment such as percentiles, deciles and coding.

## Prerequisite Recap

No GCSE source is used here. These are the mathematical skills this A-Level lesson assumes.

| Skill | Why needed |
|---|---|
| Arithmetic with fractions and decimals | For means, interpolation fractions and standard deviation formulae |
| Rearranging simple formulae | For coding and summary statistics |
| Frequency tables | For \(\sum fx\), cumulative frequency and grouped data |
| Coordinates/number-line thinking | For linear interpolation diagrams |
| Calculator statistics mode | For checking \(\sum x\), \(n\), \(\bar{x}\), standard deviation and summary values |

## Big Picture Explanation

Statistics often starts with a pile of data that is too awkward to understand directly. Measures of location and spread are the data-compression machines.

A **measure of location** tells us where a meaningful value sits in the data. A **measure of central tendency** is a special kind of location measure that tries to describe the centre. A **measure of spread** tells us how stretched out the data is.

\[
\text{location answers “where?”}
\]

\[
\text{central tendency answers “where is the centre?”}
\]

\[
\text{spread answers “how scattered?”}
\]

The evidence overview describes this chapter as statistics used to summarise data, including mean, standard deviation, quartiles and percentiles, with linear interpolation for estimating medians and quartiles.

## Key Definitions and Notation

### Statistical variable

In algebra, \(x\) usually represents one value.

In statistics, \(x\) can represent a whole collection of values. For example, if \(x\) represents people’s heights, then \(x\) means the height data for all the people being studied.

### Sum notation

\[
\sum x
\]

means:

\[
\text{the sum of all the }x\text{-values.}
\]

If the values are:

\[
2.2,\ 2.5,\ 2.6,\ 2.65,\ 2.9
\]

then:

\[
\sum x = 2.2+2.5+2.6+2.65+2.9=12.85
\]

### Number of data values

\[
n
\]

means the number of data values. For the list \(2.2,2.5,2.6,2.65,2.9\), there are five values, so \(n=5\).

### Mean

The sample mean is written:

\[
\bar{x}
\]

For listed data:

\[
\bar{x}=\frac{\sum x}{n}
\]

### Frequency table notation

If values occur with frequencies, each value must be multiplied by its frequency.

\[
\bar{x}=\frac{\sum fx}{\sum f}
\]

where \(x\) is a data value, \(f\) is the frequency of that value, \(fx\) means frequency multiplied by value, \(\sum fx\) is the total of all repeated data values, and \(\sum f\) is the total frequency.

### Measures of central tendency

\[
\text{mean},\quad \text{median},\quad \text{mode}
\]

### Measures of location

\[
\text{minimum},\quad Q_1,\quad Q_2,\quad Q_3,\quad \text{maximum}
\]

where:

\[
Q_1=\text{lower quartile},\quad Q_2=\text{median},\quad Q_3=\text{upper quartile}
\]

### Measures of spread

\[
\text{range},\quad IQR,\quad \text{variance},\quad \text{standard deviation}
\]

where:

\[
IQR=Q_3-Q_1
\]

## Core Theory

## 1. Variables in Statistics

A variable in statistics represents the value of some quantity, such as shoe size, height, colour or weight.

Unlike algebra, a statistical variable can represent many values at once. If \(x\) represents the heights of all people in a room, then \(x\) is the collection of all those heights.

This makes expressions such as:

\[
\sum x
\]

meaningful in statistics, because we are adding the whole collection of \(x\)-values.

But if \(x=4\) in algebra, then:

\[
\sum x
\]

does not make sense unless a collection of values has been defined.

## 2. Measures of Location and Measures of Spread

| Category | Meaning | Examples |
|---|---|---|
| Measures of central tendency | Values describing the centre of the data | mean, median, mode |
| Measures of location | Values describing a position in the data | minimum, maximum, quartiles, percentiles, deciles |
| Measures of spread | Values describing how spread out data is | range, IQR, standard deviation, variance |

A common trap is to group range with mean, median and mode because that is how students often first meet it. But range is not a measure of centre. It is a measure of spread.

## 3. Mean of Listed Data

For listed data:

\[
\bar{x}=\frac{\sum x}{n}
\]

### Worked Example 1: Mean of coin diameters

The evidence uses the listed data:

\[
2.2,\ 2.5,\ 2.6,\ 2.65,\ 2.9
\]

Add the values:

\[
\sum x=2.2+2.5+2.6+2.65+2.9=12.85
\]

Count the values:

\[
n=5
\]

Use the mean formula:

\[
\bar{x}=\frac{\sum x}{n}=\frac{12.85}{5}=2.57
\]

So the mean diameter is:

\[
\boxed{2.57}
\]

### Calculator note

For one-variable data, the calculator can give \(\sum x\), \(n\), and \(\bar{x}\). But in an exam, you should still show the important division when method marks are available.

## 4. Mean from an Ungrouped Frequency Table

A frequency table avoids writing repeated values.

If \(x=0\) has frequency \(4\), then this means:

\[
0,\ 0,\ 0,\ 0
\]

If \(x=1\) has frequency \(3\), then this means:

\[
1,\ 1,\ 1
\]

The mean from a frequency table is:

\[
\bar{x}=\frac{\sum fx}{\sum f}
\]

### Worked Example 2: Number of children in a family

| Number of children \(x\) | Frequency \(f\) | \(fx\) |
|---:|---:|---:|
| 0 | 4 | \(0\times4=0\) |
| 1 | 3 | \(1\times3=3\) |
| 2 | 9 | \(2\times9=18\) |
| 3 | 2 | \(3\times2=6\) |

Now add:

\[
\sum fx=0+3+18+6=27
\]

\[
\sum f=4+3+9+2=18
\]

Use the formula:

\[
\bar{x}=\frac{\sum fx}{\sum f}=\frac{27}{18}=1.5
\]

So the mean number of children is:

\[
\boxed{1.5}
\]

## 5. Estimated Mean from Grouped Data

For grouped data, we do not know the exact values inside each class interval.

For example, if a height is in the group:

\[
0.5<h\leq1.2
\]

we do not know the exact height. So we use the midpoint of the class interval.

The midpoint is:

\[
\frac{\text{lower boundary}+\text{upper boundary}}{2}
\]

For:

\[
0.5<h\leq1.2
\]

the midpoint is:

\[
\frac{0.5+1.2}{2}=\frac{1.7}{2}=0.85
\]

Then use the same frequency-table mean formula:

\[
\bar{x}\approx\frac{\sum fx}{\sum f}
\]

The symbol \(\approx\) is appropriate because the mean is only an estimate.

### Worked Example 3: Bear heights

The evidence gives the grouped-data calculation:

\[
\sum fx=46.75,
\qquad \sum f=40
\]

So:

\[
\bar{x}\approx\frac{\sum fx}{\sum f}=\frac{46.75}{40}=1.16875
\]

To two decimal places:

\[
\boxed{\bar{x}\approx1.17\text{ m}}
\]

### Why is it only an estimate?

Because grouping data loses information. We do not know the exact heights inside each interval.

## 6. Warning: Calculator Quartiles for Grouped Data

For grouped data, do **not** use calculator-generated quartiles or medians from midpoint input.

If you enter midpoints into the calculator, the calculator thinks the data values really are those exact midpoint values. For example, it treats the first four bears as if they all had height \(0.25\), not as unknown values in an interval.

So:

\[
\text{calculator mean from midpoints is acceptable as an estimate}
\]

but:

\[
\text{calculator median/quartiles from midpoint input are not valid for grouped data.}
\]

## 7. Combined Mean

This subtopic appears in the evidence as exam-aware material. It is not treated as a separate CCEA LO, but it is useful within mean calculations.

If two groups are combined, do **not** average the two means directly unless the group sizes are equal.

Use:

\[
\text{combined mean}=\frac{\text{total from group 1}+\text{total from group 2}}{\text{total number of values}}
\]

### Worked Example 4: Two classes

Class A:

\[
20\text{ pupils},\quad \text{mean}=62
\]

Class B:

\[
30\text{ pupils},\quad \text{mean}=75
\]

Total score from Class A:

\[
20\times62=1240
\]

Total score from Class B:

\[
30\times75=2250
\]

Total score:

\[
1240+2250=3490
\]

Total number of pupils:

\[
20+30=50
\]

Combined mean:

\[
\frac{3490}{50}=69.8
\]

So the overall mean is:

\[
\boxed{69.8}
\]

A student should have received \(100\) instead of \(95\). This adds \(5\) marks to the total.

New total:

\[
3490+5=3495
\]

New mean:

\[
\frac{3495}{50}=69.9
\]

So the mean increases:

\[
69.8\to69.9
\]

The median is not affected by a change at an extreme end unless the order/central position changes.

## 8. Median Position: Listed Data vs Grouped Data

### Listed data

For listed data, first ensure the data are ordered.

To find the median position for listed data:

\[
\frac{n}{2}
\]

Then:

- if \(\frac{n}{2}\) is a decimal, round up;
- if \(\frac{n}{2}\) is a whole number, go halfway between that item and the next item.

If \(n=5\):

\[
\frac{n}{2}=\frac{5}{2}=2.5
\]

Round up:

\[
2.5\to3
\]

Median is the 3rd item.

If \(n=4\):

\[
\frac{n}{2}=\frac{4}{2}=2
\]

This is a whole number, so the median is halfway between the 2nd and 3rd items.

### Grouped data

For grouped data, use:

\[
\frac{n}{2}
\]

but **do not round or adjust**.

If:

\[
n=17
\]

then:

\[
\frac{n}{2}=\frac{17}{2}=8.5
\]

So the median position is:

\[
\boxed{8.5}
\]

For grouped data, we then use linear interpolation.

## 9. Linear Interpolation for Grouped Data

For grouped data, the median, quartiles and other position-based values often lie **inside a class interval**. Linear interpolation estimates where inside that class interval the required value sits.

The idea is:

\[
\text{same fraction through the frequency interval}=\text{same fraction through the class interval}
\]

So the interpolation template is:

\[
\text{estimate}=L+\left(\frac{k-C_{\text{before}}}{C_{\text{after}}-C_{\text{before}}}\right)w
\]

where:

| Symbol | Meaning |
|---|---|
| \(L\) | lower boundary of the class interval containing the required item |
| \(k\) | item position required, such as median position \(\frac n2\) |
| \(C_{\text{before}}\) | cumulative frequency before the required class |
| \(C_{\text{after}}\) | cumulative frequency by the end of the required class |
| \(w\) | class width |

### Worked Example 5: Median height of trees

Suppose the median is the \(75\)th item. The \(75\)th item lies in the class:

\[
0.60 \leq h < 0.65
\]

The cumulative frequency before this class is \(55\). The cumulative frequency by the end of this class is \(100\). So:

\[
C_{\text{before}}=55,\quad C_{\text{after}}=100,\quad k=75,\quad L=0.60,\quad w=0.65-0.60=0.05
\]

Now calculate the fraction through the frequency interval:

\[
\frac{k-C_{\text{before}}}{C_{\text{after}}-C_{\text{before}}}
=\frac{75-55}{100-55}=\frac{20}{45}
\]

So the median estimate is:

\[
0.60+\left(\frac{20}{45}\times0.05\right)=0.6222\ldots
\]

To two decimal places:

\[
\boxed{0.62\text{ m}}
\]

### Worked Example 6: Median weight of cats

Median position is the \(16\)th item and the required class is:

\[
3 \leq w < 4
\]

The cumulative frequency before the class is \(10\), and the cumulative frequency after the class is \(18\).

\[
k=16,
\quad C_{\text{before}}=10,
\quad C_{\text{after}}=18,
\quad L=3,
\quad w=4-3=1
\]

Fraction through the frequency interval:

\[
\frac{16-10}{18-10}=\frac{6}{8}
\]

Median estimate:

\[
3+\left(\frac{6}{8}\times1\right)=3+0.75=\boxed{3.75\text{ kg}}
\]

### Worked Example 7: Median time

\[
k=10,
\quad 12 \leq t < 14,
\quad C_{\text{before}}=7,
\quad C_{\text{after}}=20,
\quad L=12,
\quad w=2
\]

Fraction through the frequency interval:

\[
\frac{10-7}{20-7}=\frac{3}{13}
\]

Median estimate:

\[
12+\left(\frac{3}{13}\times2\right)=12+\frac{6}{13}=12.461538\ldots
\]

To two decimal places:

\[
\boxed{12.46\text{ s}}
\]

## 10. True Class Limits

Sometimes class intervals are written with gaps because the data have been rounded.

For example:

\[
10-12
\]

for weight measured to the nearest kg does **not** literally mean only values from \(10\) to \(12\). It represents values that round to \(10,11,12\).

So the true class limits are:

\[
9.5 \leq w < 12.5
\]

The class width is:

\[
12.5-9.5=3
\]

not:

\[
12-10=2
\]

### Rule for rounded class intervals

If values are measured to the nearest whole number, move half a unit below and half a unit above:

\[
10-12\quad \Rightarrow \quad 9.5 \leq w < 12.5
\]

\[
13-15\quad \Rightarrow \quad 12.5 \leq w < 15.5
\]

\[
16-18\quad \Rightarrow \quad 15.5 \leq w < 18.5
\]

### Worked Example 8: Median distance travelled to work

A sample has:

\[
n=120
\]

Median position:

\[
\frac{n}{2}=\frac{120}{2}=60
\]

The cumulative frequencies around the median class are:

\[
29 \quad \text{and} \quad 72
\]

The class is written as:

\[
20-29
\]

but the distances are to the nearest mile, so the true class limits are:

\[
19.5 \leq d < 29.5
\]

Now:

\[
k=60,
\quad C_{\text{before}}=29,
\quad C_{\text{after}}=72,
\quad L=19.5,
\quad w=29.5-19.5=10
\]

Fraction through the frequency interval:

\[
\frac{60-29}{72-29}=\frac{31}{43}
\]

Median estimate:

\[
19.5+\left(\frac{31}{43}\times10\right)=26.7093\ldots
\]

To three significant figures:

\[
\boxed{26.7\text{ miles}}
\]

## 11. Quartiles

Quartiles split data into quarters.

\[
Q_1=\text{lower quartile},\quad Q_2=\text{median},\quad Q_3=\text{upper quartile}
\]

The median is also the second quartile:

\[
Q_2=\text{median}
\]

### Quartile positions for listed data

For listed data:

\[
Q_1\text{ position}=\frac{n}{4}
\]

\[
Q_3\text{ position}=\frac{3n}{4}
\]

Then use the same listed-data position rule as the median:

- if the position is a decimal, round up;
- if the position is a whole number, go halfway between that item and the next.

### Example: \(n=5\)

Lower quartile position:

\[
\frac{n}{4}=\frac{5}{4}=1.25
\]

This is a decimal, so round up:

\[
1.25 \to 2
\]

So:

\[
Q_1=\text{2nd item}
\]

Upper quartile position:

\[
\frac{3n}{4}=\frac{3\times5}{4}=\frac{15}{4}=3.75
\]

This is a decimal, so round up:

\[
3.75 \to 4
\]

So:

\[
Q_3=\text{4th item}
\]

### Example: \(n=4\)

Lower quartile position:

\[
\frac{n}{4}=\frac{4}{4}=1
\]

This is a whole number, so \(Q_1\) is halfway between the 1st and 2nd items.

Upper quartile position:

\[
\frac{3n}{4}=\frac{3\times4}{4}=3
\]

This is a whole number, so \(Q_3\) is halfway between the 3rd and 4th items.

### Quartiles for grouped data

For grouped data, do **not round** the positions.

Use:

\[
Q_1\text{ position}=\frac{n}{4},\qquad Q_3\text{ position}=\frac{3n}{4}
\]

Then use linear interpolation.

### Worked Example 9: Grouped quartiles

Suppose:

\[
n=17
\]

Lower quartile position:

\[
\frac{17}{4}=4.25
\]

Upper quartile position:

\[
\frac{3\times17}{4}=\frac{51}{4}=12.75
\]

So:

\[
Q_1\text{ is estimated using the }4.25\text{th item}
\]

\[
Q_3\text{ is estimated using the }12.75\text{th item}
\]

If \(Q_1\) lies in the first class:

\[
80 \leq x < 90
\]

and the cumulative frequency goes from \(0\) to \(7\), then:

\[
k=4.25,
\quad C_{\text{before}}=0,
\quad C_{\text{after}}=7,
\quad L=80,
\quad w=10
\]

So:

\[
Q_1=80+\left(\frac{4.25-0}{7-0}\times10\right)
=80+6.0714\ldots=86.0714\ldots
\]

So:

\[
\boxed{Q_1\approx86.07}
\]

## 12. Percentiles and Deciles

This section appears in the supplied lesson evidence, but it is logged as **boundary-risk enrichment** because the supplied CCEA LO wording does not explicitly name percentiles and deciles. It is still useful vocabulary because quartiles and percentiles are related.

### Percentiles

Percentiles split data into 100 equal parts. The \(r\)th percentile is written:

\[
P_r
\]

The item position for \(P_r\), in grouped-data style, is:

\[
\frac{r}{100}n
\]

So:

\[
P_{64}\text{ position}=\frac{64}{100}n=0.64n
\]

### Deciles

Deciles split data into 10 equal parts. The \(r\)th decile is written:

\[
D_r
\]

For example:

\[
D_3\text{ position}=\frac{3}{10}n=0.3n
\]

### Links between quartiles, percentiles and deciles

\[
Q_1=P_{25}
\]

\[
Q_2=P_{50}=D_5=\text{median}
\]

\[
Q_3=P_{75}
\]

\[
D_3=P_{30}
\]

## 13. Range, Interquartile Range and Interpercentile Range

### Range

\[
\text{Range}=\text{maximum}-\text{minimum}
\]

Range uses only two values, so it can be strongly affected by extreme values.

### Interquartile range

The interquartile range, or IQR, measures the spread of the middle 50% of the data.

\[
IQR=Q_3-Q_1
\]

It ignores the lowest 25% and highest 25% of the data, so it is less affected by extreme values than the range.

### Interpercentile range

Boundary-risk enrichment:

\[
\text{interpercentile range}=P_b-P_a
\]

For example:

\[
P_{90}-P_{10}
\]

measures the spread of the middle 80% of the data.

### Worked Example 10: Interpercentile range

Suppose:

\[
P_{10}=54.47,
\quad P_{90}=850.91
\]

Then:

\[
P_{90}-P_{10}=850.91-54.47=796.44
\]

To the nearest centimetre:

\[
\boxed{796\text{ cm}}
\]

## 14. Variance and Standard Deviation

Variance and standard deviation are measures of spread.

Variance is a measure of spread that takes all values into account.

\[
\text{variance}=\text{average squared distance from the mean}
\]

The simplified mnemonic is:

\[
\text{mean of the squares minus the square of the mean}
\]

### Population variance

For a population:

\[
\sigma^2=\frac{\sum (x-\bar{x})^2}{n}
\]

This says:

1. find each distance from the mean;
2. square each distance;
3. add the squared distances;
4. divide by \(n\).

The simplified formula is:

\[
\sigma^2=\frac{\sum x^2}{n}-\bar{x}^2
\]

Since:

\[
\bar{x}=\frac{\sum x}{n}
\]

we can also write:

\[
\sigma^2=\frac{\sum x^2}{n}-\left(\frac{\sum x}{n}\right)^2
\]

### Population standard deviation

Standard deviation is the square root of variance:

\[
\sigma=\sqrt{\sigma^2}
\]

So:

\[
\sigma=\sqrt{\frac{\sum x^2}{n}-\bar{x}^2}
\]

or:

\[
\sigma=\sqrt{\frac{\sum x^2}{n}-\left(\frac{\sum x}{n}\right)^2}
\]

### Frequency-table variance

For frequency tables:

\[
\bar{x}=\frac{\sum fx}{\sum f}
\]

and:

\[
\sigma^2=\frac{\sum fx^2}{\sum f}-\bar{x}^2
\]

So:

\[
\sigma=\sqrt{\frac{\sum fx^2}{\sum f}-\bar{x}^2}
\]

### Grouped frequency tables

For grouped frequency tables, use the midpoint of each interval as \(x\). That means:

\[
x=\text{class midpoint}
\]

Then calculate \(fx\) and \(fx^2\) using those midpoints.

Because grouped data loses exact values, the mean, variance and standard deviation are estimates.

### Sample standard deviation

The CCEA map states that students should be able to use either:

\[
\sigma_n
\]

or:

\[
\sigma_{n-1}
\]

as appropriate. The \(n-1\) version is used for sample standard deviation when the question requires it.

Do not guess which one is wanted. Use the wording of the question, the calculator label, or the formula supplied.

## 15. Worked Examples: Standard Deviation and Variance

### Worked Example 11: Summary statistics

Suppose:

\[
n=20,
\quad \sum t=374,
\quad \sum t^2=7600
\]

Mean:

\[
\bar{t}=\frac{\sum t}{n}=\frac{374}{20}=18.7
\]

Variance:

\[
\sigma^2=\frac{\sum t^2}{n}-\bar{t}^2
\]

\[
\sigma^2=\frac{7600}{20}-(18.7)^2
\]

Since:

\[
\frac{7600}{20}=380
\]

and:

\[
(18.7)^2=349.69
\]

then:

\[
\sigma^2=380-349.69=30.31
\]

Standard deviation:

\[
\sigma=\sqrt{30.31}=5.50545\ldots
\]

To two decimal places:

\[
\boxed{\sigma=5.51}
\]

### Worked Example 12: Grouped standard deviation from calculator summary values

The transcript gives a grouped-data example where the calculator summary gives:

\[
\sum ft=4837.5,
\quad n=200,
\quad \sum ft^2=134281.25
\]

Mean:

\[
\bar{t}=\frac{\sum ft}{n}=\frac{4837.5}{200}=24.1875
\]

Standard deviation:

\[
\sigma=\sqrt{\frac{\sum ft^2}{n}-\bar{t}^2}
\]

\[
\sigma=\sqrt{\frac{134281.25}{200}-(24.1875)^2}
\]

First calculate:

\[
\frac{134281.25}{200}=671.40625
\]

Now calculate:

\[
(24.1875)^2=585.03515625
\]

Subtract:

\[
671.40625-585.03515625=86.37109375
\]

Square root:

\[
\sigma=\sqrt{86.37109375}=9.2936\ldots
\]

To two decimal places:

\[
\boxed{\sigma=9.29}
\]

### Interpretation: What does standard deviation mean?

A larger standard deviation means the data are more spread out.

A smaller standard deviation means the data are more clustered around the mean.

## 16. Coding

Coding appears in the supplied lesson evidence. It is logged as **boundary-risk enrichment/support** because it is not listed as a standalone CCEA LO in the supplied map, but it supports transformed summary-statistic questions.

Coding means transforming a variable to make calculations easier.

### General coding form

Suppose:

\[
y=ax+b
\]

Then:

\[
\bar{y}=a\bar{x}+b
\]

Standard deviation transforms as:

\[
\sigma_y=|a|\sigma_x
\]

Variance transforms as:

\[
\sigma_y^2=a^2\sigma_x^2
\]

### Adding or subtracting

If:

\[
y=x+b
\]

then:

\[
\bar{y}=\bar{x}+b
\]

but:

\[
\sigma_y=\sigma_x
\]

and:

\[
\sigma_y^2=\sigma_x^2
\]

Adding the same number to every data value shifts the whole dataset but does not make it more or less spread out.

### Multiplying or dividing

If:

\[
y=ax
\]

then:

\[
\bar{y}=a\bar{x}
\]

\[
\sigma_y=|a|\sigma_x
\]

\[
\sigma_y^2=a^2\sigma_x^2
\]

### Worked Example 13: Coding maximum gust

Suppose:

\[
h=\frac{g-5}{10}
\]

and:

\[
\bar{h}=2
\]

Find \(\bar{g}\).

Start with:

\[
h=\frac{g-5}{10}
\]

For means:

\[
\bar{h}=\frac{\bar{g}-5}{10}
\]

Substitute:

\[
2=\frac{\bar{g}-5}{10}
\]

Multiply both sides by \(10\):

\[
20=\bar{g}-5
\]

Add \(5\):

\[
25=\bar{g}
\]

So:

\[
\boxed{\bar{g}=25}
\]

Now suppose:

\[
\frac{S_{hh}}{n}=\frac{43.58}{61}
\]

Then the variance of \(h\) is:

\[
\sigma_h^2=\frac{43.58}{61}
\]

So the standard deviation of \(h\) is:

\[
\sigma_h=\sqrt{\frac{43.58}{61}}=0.845\ldots
\]

Since:

\[
h=\frac{g-5}{10}
\]

the standard deviation has been divided by \(10\). So:

\[
\sigma_h=\frac{\sigma_g}{10}
\]

Multiply by \(10\):

\[
\sigma_g=10\sigma_h=10(0.845\ldots)=8.45\ldots
\]

So:

\[
\boxed{\sigma_g\approx8.45}
\]

## Visual Asset Integration

[VISUAL PLACEHOLDER: AS2MeasuresLocationSpreadSVG-001 | Source: S1-Chp2-MeasuresOfLocationAndSpread.pdf page 6 + transcript section 1 | Insert from svg/AS2MeasuresLocationSpreadSVG-001.svg | Purpose: Show the relationship between measures of central tendency, location and spread.]

[VISUAL PLACEHOLDER: AS2MeasuresLocationSpreadSVG-002 | Source: S1-Chp2-MeasuresOfLocationAndSpread.pdf pages 17-20 + transcript section 6 | Insert from svg/AS2MeasuresLocationSpreadSVG-002.svg | Purpose: Show linear interpolation as matching a frequency fraction to a class-interval fraction.]

[VISUAL PLACEHOLDER: AS2MeasuresLocationSpreadSVG-003 | Source: S1-Chp2-MeasuresOfLocationAndSpread.pdf pages 21-23 + transcript section 7 | Insert from svg/AS2MeasuresLocationSpreadSVG-003.svg | Purpose: Show true class limits for rounded intervals.]

[VISUAL PLACEHOLDER: AS2MeasuresLocationSpreadSVG-004 | Source: S1-Chp2-MeasuresOfLocationAndSpread.pdf pages 28-32 + transcript sections 8-10 | Insert from svg/AS2MeasuresLocationSpreadSVG-004.svg | Purpose: Show \(Q_1,Q_2,Q_3\), the middle 50%, and the interquartile range.]

[VISUAL PLACEHOLDER: AS2MeasuresLocationSpreadSVG-005 | Source: S1-Chp2-MeasuresOfLocationAndSpread.pdf pages 35-40 + transcript section 11 | Insert from svg/AS2MeasuresLocationSpreadSVG-005.svg | Purpose: Show variance as average squared distance from the mean and standard deviation as the square root of variance.]

[VISUAL PLACEHOLDER: AS2MeasuresLocationSpreadSVG-006 | Source: S1-Chp2-MeasuresOfLocationAndSpread.pdf pages 45-48 + transcript sections 12-13 | Insert from svg/AS2MeasuresLocationSpreadSVG-006.svg | Purpose: Show coding effects on mean, standard deviation and variance for \(y=ax+b\).]

[INTERACTIVE PLACEHOLDER: AS2MeasuresLocationSpreadWidget-001 | Source: Lesson evidence on grouped medians and interpolation | Insert from widgets/AS2MeasuresLocationSpreadWidget-001.html | Purpose: Let the student move an item position through a grouped interval and see the interpolated estimate update.]

[INTERACTIVE PLACEHOLDER: AS2MeasuresLocationSpreadWidget-002 | Source: Lesson evidence on variance and standard deviation | Insert from widgets/AS2MeasuresLocationSpreadWidget-002.html | Purpose: Let the student adjust data values and observe how the mean, variance and standard deviation change.]

[INTERACTIVE PLACEHOLDER: AS2MeasuresLocationSpreadWidget-003 | Source: Lesson evidence on coding | Insert from widgets/AS2MeasuresLocationSpreadWidget-003.html | Purpose: Let the student transform \(x\) by \(y=ax+b\) and see the resulting mean, standard deviation and variance.]

## Guided Practice

### Question 1: Listed mean

Find the mean of:

\[
4,\ 7,\ 9,\ 10,\ 15
\]

### Question 2: Frequency-table mean

| \(x\) | \(f\) |
|---:|---:|
| 1 | 3 |
| 2 | 5 |
| 3 | 4 |
| 4 | 2 |

Find \(\bar{x}\).

### Question 3: Estimated mean from grouped data

| Class interval | Frequency |
|---|---:|
| \(0\leq x<10\) | 4 |
| \(10\leq x<20\) | 7 |
| \(20\leq x<30\) | 9 |

Estimate the mean.

### Question 4: Median position

For listed data with \(n=18\), state the median position. For grouped data with \(n=18\), state the median position.

### Question 5: Linear interpolation

A grouped frequency table has \(40\) values. The median lies in the class \(20\leq x<30\). The cumulative frequency before the class is \(12\), and the cumulative frequency by the end of the class is \(28\). Estimate the median.

### Question 6: Quartiles

A grouped table has \(n=60\). Find the item positions used for \(Q_1,Q_2,Q_3\).

### Question 7: Standard deviation from summary statistics

Given:

\[
n=10,
\quad \sum x=80,
\quad \sum x^2=700
\]

calculate the population variance and standard deviation.

### Question 8: Coding

A variable \(y\) is coded from \(x\) using \(y=3x-7\). Given \(\bar{x}=12\) and \(\sigma_x=5\), find \(\bar{y}\) and \(\sigma_y\).

## Full Worked Solutions

### Solution 1

\[
\sum x=4+7+9+10+15=45
\]

\[
n=5
\]

\[
\bar{x}=\frac{45}{5}=\boxed{9}
\]

### Solution 2

| \(x\) | \(f\) | \(fx\) |
|---:|---:|---:|
| 1 | 3 | \(1\times3=3\) |
| 2 | 5 | \(2\times5=10\) |
| 3 | 4 | \(3\times4=12\) |
| 4 | 2 | \(4\times2=8\) |

\[
\sum fx=3+10+12+8=33
\]

\[
\sum f=3+5+4+2=14
\]

\[
\bar{x}=\frac{33}{14}=2.357142\ldots
\]

To three significant figures:

\[
\boxed{\bar{x}=2.36}
\]

### Solution 3

Find midpoints:

\[
\frac{0+10}{2}=5,
\quad \frac{10+20}{2}=15,
\quad \frac{20+30}{2}=25
\]

| Class interval | Midpoint \(x\) | Frequency \(f\) | \(fx\) |
|---|---:|---:|---:|
| \(0\leq x<10\) | 5 | 4 | \(5\times4=20\) |
| \(10\leq x<20\) | 15 | 7 | \(15\times7=105\) |
| \(20\leq x<30\) | 25 | 9 | \(25\times9=225\) |

\[
\sum fx=20+105+225=350
\]

\[
\sum f=4+7+9=20
\]

\[
\bar{x}\approx\frac{350}{20}=\boxed{17.5}
\]

### Solution 4

For listed data:

\[
\frac{n}{2}=\frac{18}{2}=9
\]

Because this is listed data and the result is a whole number, the median is halfway between the 9th and 10th items.

\[
\boxed{\text{listed median position: halfway between 9th and 10th}}
\]

For grouped data:

\[
\frac{n}{2}=9
\]

For grouped data, use this position directly for interpolation.

\[
\boxed{\text{grouped median position: 9th item}}
\]

### Solution 5

There are \(40\) values, so the median position is:

\[
\frac{40}{2}=20
\]

The median lies in \(20\leq x<30\). So:

\[
L=20,
\quad w=10,
\quad C_{\text{before}}=12,
\quad C_{\text{after}}=28,
\quad k=20
\]

Use interpolation:

\[
\text{median}=L+\left(\frac{k-C_{\text{before}}}{C_{\text{after}}-C_{\text{before}}}\right)w
\]

\[
=20+\left(\frac{20-12}{28-12}\right)10
\]

\[
=20+\left(\frac{8}{16}\right)10
\]

\[
=20+5=\boxed{25}
\]

### Solution 6

Given \(n=60\):

\[
Q_1\text{ position}=\frac{60}{4}=15
\]

\[
Q_2\text{ position}=\frac{60}{2}=30
\]

\[
Q_3\text{ position}=\frac{3\times60}{4}=45
\]

So:

\[
\boxed{Q_1:15\text{th},\quad Q_2:30\text{th},\quad Q_3:45\text{th}}
\]

For grouped data, these positions would be used directly for linear interpolation.

### Solution 7

Given:

\[
n=10,
\quad \sum x=80,
\quad \sum x^2=700
\]

Mean:

\[
\bar{x}=\frac{\sum x}{n}=\frac{80}{10}=8
\]

Variance:

\[
\sigma^2=\frac{\sum x^2}{n}-\bar{x}^2=\frac{700}{10}-8^2=70-64=\boxed{6}
\]

Standard deviation:

\[
\sigma=\sqrt{6}=2.449489\ldots
\]

To three significant figures:

\[
\boxed{\sigma=2.45}
\]

### Solution 8

Given:

\[
y=3x-7,
\quad \bar{x}=12,
\quad \sigma_x=5
\]

Mean transforms by the whole coding rule:

\[
\bar{y}=3\bar{x}-7=3(12)-7=36-7=\boxed{29}
\]

Standard deviation is affected by the scale factor \(3\), but not by subtracting \(7\):

\[
\sigma_y=|3|\sigma_x=3(5)=\boxed{15}
\]

## Common Mistakes and Exam Traps

| Mistake | Why it is wrong | Safer method |
|---|---|---|
| Using calculator quartiles after entering grouped-data midpoints | The calculator treats midpoints as exact values | Use linear interpolation for grouped median/quartiles |
| Forgetting midpoints for grouped means | Exact grouped values are unknown | Use class midpoints and write “estimate” |
| Using written class limits instead of true class boundaries | Rounded intervals may have hidden gaps | Convert to true class boundaries first |
| Rounding grouped-data positions | Grouped medians/quartiles use exact positions | Use \(\frac n2\), \(\frac n4\), \(\frac{3n}{4}\) directly |
| Averaging two means directly | Groups may have different sizes | Multiply each mean by its group size first |
| Forgetting the square root for standard deviation | The formula inside gives variance | Standard deviation is \(\sqrt{\text{variance}}\) |
| Treating variance and standard deviation the same under coding | Variance scales by the square of the scale factor | If \(y=ax+b\), then \(\sigma_y=|a|\sigma_x\), variance multiplies by \(a^2\) |
| Forgetting units | Units help distinguish frequencies from data values | Put units on interpolation diagrams where possible |
| Giving only calculator output | May lose method marks | Write the division or formula substitution |

## Exam Technique Notes

1. For a mean from a frequency table, write \(\bar{x}=\frac{\sum fx}{\sum f}\) even if your calculator gives the answer.
2. For grouped data, write “estimate” because the exact values inside each class are unknown.
3. For linear interpolation, always identify \(C_{\text{before}}, k, C_{\text{after}}\) and \(L,w\).
4. For rounded classes, find true class limits before interpolating.
5. For variance and standard deviation, write the formula substitution.
6. For coding, separate location and spread.
7. If asked to interpret standard deviation, use comparative language: larger standard deviation means more variation, smaller standard deviation means more consistency.

## Common CCEA-Style Wording

| Wording | What to do |
|---|---|
| “Estimate the mean” | Use midpoints if grouped data are given |
| “Estimate the median” | Use cumulative frequencies and linear interpolation |
| “Calculate the standard deviation from summary statistics” | Use \(\sqrt{\frac{\sum x^2}{n}-\left(\frac{\sum x}{n}\right)^2}\) or the appropriate sample formula |
| “Interpret the standard deviation” | Comment on spread/variation/consistency |
| “Compare the distributions” | Compare centre and spread, not just one of them |
| “Given the data were coded...” | Reverse or apply the coding formula to mean and standard deviation |
| “Identify possible outliers” | Use the rule supplied in the question, such as \(Q_3+1.5IQR\), \(Q_1-1.5IQR\), or mean \(\pm2\sigma\) |

## Syllabus Gap Check

| LO ID | Required content | Covered? | Notes |
|---|---|---:|---|
| `AS2-DPI-LO002` | Interpret measures of central tendency and variation, including standard deviation and variance | Yes | Mean, median, mode, range, IQR, variance, SD and interpretation included |
| `AS2-DPI-LO003` | Calculate standard deviation and variance of a population or sample, including from summary statistics | Yes | Population formula, grouped/frequency formula, summary-statistics formula and sample notation warning included |
| `AS2-DPI-LO008` | Recognise and interpret possible outliers | Partial/supporting | IQR and SD rules noted as question-supplied CCEA tools |
| `AS2-DPI-LO010` | Clean data, including missing data, errors and outliers | Partial/supporting | Mentioned through evidence but not developed as the main lesson |

## Off-Spec or Boundary-Risk Content Found but Controlled

| Evidence item | Status | Treatment |
|---|---|---|
| Percentiles and deciles | Boundary-risk enrichment | Explained as optional notation linked to quartiles, not treated as a required CCEA-only core skill |
| Interpercentile range | Boundary-risk enrichment | Included as enrichment because evidence uses it; IQR remains the core spread statistic |
| Coding | Boundary-risk support/enrichment | Included because evidence contains it and it supports transformed statistics, but flagged as not a standalone supplied CCEA LO |
| Edexcel/Pearson S1 question references | Cross-board support | Methods retained only where they match CCEA AS2-DPI boundaries |
| Large data set locations from evidence | Cross-board context | Not treated as CCEA-specific required place knowledge |

## Visual and Interactive Asset Plan

| Asset ID | Type | Section | Purpose |
|---|---|---|---|
| `AS2MeasuresLocationSpreadSVG-001` | SVG | Measures overview | Venn-style map of location, central tendency and spread |
| `AS2MeasuresLocationSpreadSVG-002` | SVG | Linear interpolation | Show frequency fraction mapped to class-interval fraction |
| `AS2MeasuresLocationSpreadSVG-003` | SVG | True class limits | Show rounded intervals becoming continuous boundaries |
| `AS2MeasuresLocationSpreadSVG-004` | SVG | Quartiles/IQR | Show \(Q_1,Q_2,Q_3\), middle 50%, and IQR |
| `AS2MeasuresLocationSpreadSVG-005` | SVG | Variance/SD | Show squared distances from the mean |
| `AS2MeasuresLocationSpreadSVG-006` | SVG | Coding | Show \(y=ax+b\) effects on mean, SD and variance |
| `AS2MeasuresLocationSpreadWidget-001` | HTML widget | Interpolation | Interactive grouped-data interpolation calculator |
| `AS2MeasuresLocationSpreadWidget-002` | HTML widget | Variance/SD | Interactive mean, variance and SD explorer |
| `AS2MeasuresLocationSpreadWidget-003` | HTML widget | Coding | Interactive coding transformation explorer |

## Supplementary Sources Used

| Source | Role |
|---|---|
| CCEA GCE Mathematics Specification Map | Core authority for AS2-DPI LO IDs and boundaries |
| Dr Frost/Pearson-style Stats 1 Chapter 2 PDF | Cross-board lesson evidence, filtered by CCEA boundary |
| Chapter 2 transcript | Teacher explanation, methods, warnings and worked examples |
| Screenshots PDF | Partial visual evidence for early sections |

No external web sources were used. No files were written at Phase 1 draft time.

## Final Student Checklist

Before moving on, the student should be able to say “yes” to each statement:

- I can explain the difference between \(x\), \(\sum x\), \(n\) and \(\bar{x}\).
- I can calculate a mean from listed data.
- I can calculate a mean from an ungrouped frequency table.
- I can estimate a mean from grouped data using midpoints.
- I can explain why grouped-data means are only estimates.
- I can find the median position for listed data.
- I can find the median position for grouped data.
- I know not to round grouped-data median/quartile positions.
- I can use linear interpolation.
- I can convert rounded intervals into true class limits.
- I can find \(Q_1\), \(Q_2\), \(Q_3\) positions.
- I can calculate the interquartile range.
- I can calculate variance from summary statistics.
- I can calculate standard deviation as the square root of variance.
- I can interpret a larger or smaller standard deviation.
- I know that calculator grouped-data quartiles from midpoints are not valid.
- I can handle simple coding rules for mean and standard deviation as enrichment/support.
