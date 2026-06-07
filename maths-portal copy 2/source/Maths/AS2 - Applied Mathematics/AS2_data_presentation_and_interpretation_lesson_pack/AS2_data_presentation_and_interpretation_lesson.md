# AS2 Data Presentation and Interpretation: Representations of Data

## Title and Metadata

| Field | Value |
|---|---|
| Course | CCEA GCE Mathematics |
| Unit code | AS2 |
| Unit name | AS 2 Applied Mathematics |
| Applied section | Statistics |
| Topic code | AS2-DPI |
| Topic name | Data presentation and interpretation |
| Chapter focus | Representations of Data |
| Topic slug | data_presentation_and_interpretation |
| Topic Pascal | DataPresentationAndInterpretation |
| Topic ID | AS2DataPresentationAndInterpretation |
| Lesson file | AS2_data_presentation_and_interpretation_lesson.md |
| Core LO IDs | AS2-DPI-LO001, AS2-DPI-LO002, AS2-DPI-LO003, AS2-DPI-LO008, AS2-DPI-LO009, AS2-DPI-LO010 |
| Same-topic but not covered here | AS2-DPI-LO004, AS2-DPI-LO005, AS2-DPI-LO006, AS2-DPI-LO007 |

---

## Evidence Map

| Evidence ID | Source | Lesson use |
|---|---|---|
| E1 | CCEA GCE Mathematics Specification Map | Defines AS2-DPI learning outcomes and boundary. |
| E2 | Project README Module Map | Defines metadata, file naming and phase structure. |
| E3 | Evidence Drop Checklist | Defines missing evidence, off-spec logging and visual placeholder rules. |
| E4 | `S1-Chp3-RepresentationsOfData.pdf` | Main slide evidence for box plots, cumulative frequency diagrams, histograms and frequency polygons. |
| E5 | `Chapter_3_Representations_of_Data_🤖_(Applied_Year_1)_Transcript.md` | Main worked-example and teacher-explanation evidence. |
| E6 | `Chapter_3_Representations_of_Data_🤖_(Applied_Year_1)_Screenshots.pdf` | Image evidence for early annotated box plot/outlier slides. |

**Evidence limitation note:** The screenshot PDF is image-only in the supplied file-search extract. It is used for visible diagram support only. The lesson relies mainly on the transcript and the main PDF for exact mathematical content.

---

## Specification Alignment

| LO ID | Official wording | Lesson coverage |
|---|---|---|
| AS2-DPI-LO001 | interpret diagrams for single-variable data, including understanding that area in a histogram represents frequency and connections to probability distributions | Box plots, cumulative frequency diagrams, histograms, frequency-density interpretation, frequency polygons. |
| AS2-DPI-LO002 | interpret measures of central tendency and variation, including standard deviation and variance | Median, quartiles, IQR, range, mean, standard deviation, comparing distributions. |
| AS2-DPI-LO003 | calculate standard deviation and variance of a population or sample, including from summary statistics | Outlier rules using mean and standard deviation, summary-statistic examples. |
| AS2-DPI-LO008 | recognise and interpret possible outliers in data sets and statistical diagrams | \(1.5IQR\) rule, mean \(\pm2\sigma\) rule, crosses on box plots, anomaly cleaning. |
| AS2-DPI-LO009 | select or critique data presentation techniques in the context of a statistical problem | Critiquing bar charts versus histograms, choosing box plot/histogram interpretations, comparing data displays. |
| AS2-DPI-LO010 | clean data, including dealing with missing data, errors and outliers | Anomalies, removing impossible or erroneous values, interpreting outliers cautiously. |

---

## Learning Objectives

By the end of this lesson, you should be able to:

1. Read and draw a box plot from the five-number summary.
2. Interpret the range, interquartile range and the four \(25\%\) sections of a box plot.
3. Identify outliers using \(Q_1-1.5IQR\), \(Q_3+1.5IQR\), or \(\bar{x}\pm2\sigma\), depending on the rule stated in the question.
4. Distinguish between an outlier and an anomaly.
5. Use cumulative frequency diagrams to estimate quartiles, medians and counts.
6. Construct and interpret histograms where area is proportional to frequency.
7. Use class width, frequency density and scaling constants correctly.
8. Deal with gaps in class intervals and true class boundaries.
9. Find the drawn width and height of histogram bars when a scale is given.
10. Form a frequency polygon by joining midpoints of histogram bars.
11. Compare distributions using a measure of location and a measure of spread, both in context.

---

## A-Level Prerequisite Recap

No external GCSE sources are used. This recap is included only as mathematical groundwork needed for the AS2 evidence.

| Skill | Needed for |
|---|---|
| Finding a median from an ordered list | Quartiles and box plots |
| Subtracting two values | Range and IQR |
| Reading graph scales | Cumulative frequency and histograms |
| Area of a rectangle | Histogram bar areas |
| Proportional reasoning | Histogram scaling |
| Substitution into formulae | Outlier boundaries |
| Mean and standard deviation notation | Mean \(\pm2\sigma\) outlier rules |
| Contextual interpretation | Comparing distributions and critiquing claims |

---

## Big Picture Explanation

This chapter is about turning processed data into diagrams that can be read, compared and criticised.

Statistics has two big jobs:

1. **Summarise data without lying by accident.**
2. **Display data so patterns become visible.**

A table can hold the data, but a diagram can make the data speak. Box plots show the **location and spread** of data. Cumulative frequency diagrams show the **running total** up to a value. Histograms show how densely continuous data is packed into intervals.

The biggest A-Level upgrade is this:

\[
\textbf{In a histogram, area represents frequency, but the area is not always numerically equal to frequency.}
\]

Instead, at A-Level we treat area and frequency as proportional:

\[
\text{Area}=k\times \text{frequency}.
\]

---

## Key Definitions and Notation

### Five-number summary

A box plot is built from:

\[
\text{minimum},\quad Q_1,\quad Q_2,\quad Q_3,\quad \text{maximum}.
\]

| Symbol/name | Meaning |
|---|---|
| Minimum | Smallest value, unless outliers are drawn separately. |
| \(Q_1\) | Lower quartile. About \(25\%\) of the data lie at or below this value. |
| \(Q_2\) | Median. About \(50\%\) of the data lie at or below this value. |
| \(Q_3\) | Upper quartile. About \(75\%\) of the data lie at or below this value. |
| Maximum | Largest value, unless outliers are drawn separately. |

### Range

\[
\text{range}=\text{maximum}-\text{minimum}.
\]

### Interquartile range

\[
IQR=Q_3-Q_1.
\]

The IQR measures the spread of the middle \(50\%\) of the data.

### Outlier

An **outlier** is an extreme value.

A common rule is:

\[
\text{lower outlier boundary}=Q_1-1.5IQR,
\]

\[
\text{upper outlier boundary}=Q_3+1.5IQR.
\]

A different rule may also be used:

\[
\bar{x}-2\sigma,\qquad \bar{x}+2\sigma.
\]

The exam question should state which rule to use.

### Anomaly

An **anomaly** is an outlier that appears to have occurred because of an error. Removing anomalies is called **cleaning the data**.

Important distinction:

\[
\text{outlier} \neq \text{automatic mistake}.
\]

### Cumulative frequency

Cumulative frequency means the running total up to a particular value. For example, if the frequencies are:

\[
1,\quad 4,\quad 10,\quad 17,
\]

then the cumulative frequencies are:

\[
1,\quad 1+4=5,\quad 5+10=15,\quad 15+17=32.
\]

### Histogram

A histogram is used for continuous data divided into class intervals. It has no gaps between bars unless there is a genuine gap in the class intervals. Bar area is proportional to frequency.

### Class width

\[
\text{class width}=\text{upper class boundary}-\text{lower class boundary}.
\]

### Frequency density

\[
\text{frequency density}=\frac{\text{frequency}}{\text{class width}}.
\]

Rearranging:

\[
\text{frequency}=\text{frequency density}\times \text{class width}.
\]

### A-Level histogram scaling

At A-Level, area is proportional to frequency:

\[
\text{area}=\text{frequency}\times k.
\]

So:

\[
k=\frac{\text{area}}{\text{frequency}}.
\]

Then:

\[
\text{frequency}=\frac{\text{area}}{k}.
\]

---

## Core Theory

## 1. Box Plots

A box plot visually represents the **distribution** and **location** of data.

The **distribution** is about spread:

\[
IQR,\quad \text{range},\quad \text{width of boxes and whiskers}.
\]

The **location** is about where the values lie:

\[
Q_1,\quad Q_2,\quad Q_3,\quad \text{minimum},\quad \text{maximum}.
\]

[VISUAL PLACEHOLDER: AS2DataPresentationSVG-001 | Source: S1-Chp3-RepresentationsOfData.pdf pages 5-6 and screenshot PDF pages 4-18 | Insert from svg/AS2DataPresentationSVG-001.svg | Purpose: Label minimum, lower quartile, median, upper quartile, maximum, range and IQR on a box plot.]

### 1.1 Each section of a box plot represents \(25\%\)

A box plot is divided into four quarters:

1. Minimum to \(Q_1\): \(25\%\)
2. \(Q_1\) to median: \(25\%\)
3. Median to \(Q_3\): \(25\%\)
4. \(Q_3\) to maximum: \(25\%\)

This is why a wider section does **not** mean more people or more items. It means the same proportion of data is more spread out.

### Key interpretation warning

If the right-hand box is wider than the left-hand box, do not say:

> The right box contains more people.

Say:

> The data values in that \(25\%\) section are more spread out.

---

## 2. Outliers

An outlier is an extreme value. The common rule in the evidence is:

\[
Q_1-1.5IQR,\qquad Q_3+1.5IQR.
\]

Values below the lower boundary or above the upper boundary are outliers.

[VISUAL PLACEHOLDER: AS2DataPresentationSVG-002 | Source: S1-Chp3-RepresentationsOfData.pdf page 7 and screenshot PDF pages 19-20 | Insert from svg/AS2DataPresentationSVG-002.svg | Purpose: Show lower and upper outlier boundaries using \(Q_1-1.5IQR\) and \(Q_3+1.5IQR\).]

### 2.1 Outlier rule using quartiles

\[
IQR=Q_3-Q_1.
\]

Lower boundary:

\[
Q_1-1.5IQR.
\]

Upper boundary:

\[
Q_3+1.5IQR.
\]

Then compare actual data values with the boundaries.

### 2.2 Outlier rule using mean and standard deviation

Another rule in the evidence is:

\[
\bar{x}-2\sigma,\qquad \bar{x}+2\sigma.
\]

A value is an outlier if it lies outside those boundaries.

### 2.3 Outlier versus anomaly

Outliers may be genuine. An anomaly is an outlier caused by an error.

For example, if a birthday-party age is recorded as \(165\), this is not just unusual. It is impossible for an ordinary human age dataset, so it is likely an anomaly and should be removed when cleaning the data.

---

## 3. Drawing Box Plots with Outliers

When drawing a box plot:

1. Calculate \(IQR\).
2. Calculate outlier boundaries.
3. Identify outliers.
4. Draw the box from \(Q_1\) to \(Q_3\).
5. Draw the median inside the box.
6. Draw whiskers.
7. Mark outliers with crosses.

When there is an outlier at one end, the evidence states two acceptable choices for the whisker endpoint:

1. the maximum/minimum value that is **not** an outlier;
2. the outlier boundary.

Use one or the other, not both.

**Exam tip:** You must show your outlier boundary calculations.

---

## 4. Comparing Box Plots

To compare two distributions using box plots, include:

1. a measure of **location**, usually the median;
2. a measure of **spread**, usually the IQR or range;
3. context.

A two-mark comparison often needs one sentence about location and one sentence about spread.

---

## 5. Cumulative Frequency Diagrams

Cumulative frequency diagrams show the running total up to a particular value.

They are useful for estimating:

\[
Q_1,\quad Q_2,\quad Q_3,\quad IQR.
\]

[VISUAL PLACEHOLDER: AS2DataPresentationSVG-003 | Source: S1-Chp3-RepresentationsOfData.pdf pages 17-18 | Insert from svg/AS2DataPresentationSVG-003.svg | Purpose: Show cumulative frequency plotting points, quartile reading lines and count estimates.]

For grouped continuous data, plot:

\[
(\text{upper class boundary},\text{cumulative frequency}).
\]

Also include the starting point at the lower boundary with cumulative frequency \(0\). The evidence joins points with straight line segments because the values are assumed to be evenly distributed within each class interval.

If there are \(n\) values:

\[
Q_1 \text{ is read at cumulative frequency } \frac{n}{4},
\]

\[
Q_2 \text{ is read at cumulative frequency } \frac{n}{2},
\]

\[
Q_3 \text{ is read at cumulative frequency } \frac{3n}{4}.
\]

Then:

\[
IQR=Q_3-Q_1.
\]

For a value more than \(a\):

\[
\text{number more than }a=\text{total frequency}-\text{number less than }a.
\]

For a value between \(a\) and \(b\):

\[
\text{number between }a\text{ and }b=\text{CF at }b-\text{CF at }a.
\]

---

## 6. Histograms

Histograms are used for continuous data. A histogram is not just a bar chart wearing a statistics hat. The key difference is that frequency is represented by **area**, not simply height.

[VISUAL PLACEHOLDER: AS2DataPresentationSVG-004 | Source: S1-Chp3-RepresentationsOfData.pdf pages 20-24 | Insert from svg/AS2DataPresentationSVG-004.svg | Purpose: Show why unequal class widths need frequency density rather than raw frequency height.]

Suppose there are:

| Age interval | Frequency |
|---|---:|
| \(15\leq a<20\) | 15 |
| \(20\leq a<50\) | 15 |

If both bars are drawn with height \(15\), the second bar looks just as dense as the first, even though those \(15\) people are spread over a much wider interval.

For \(15\leq a<20\):

\[
\text{class width}=20-15=5,
\]

\[
\text{frequency density}=\frac{15}{5}=3.
\]

For \(20\leq a<50\):

\[
\text{class width}=50-20=30,
\]

\[
\text{frequency density}=\frac{15}{30}=0.5.
\]

So the first group is much denser.

### 6.1 Frequency density formula

\[
\text{frequency density}=\frac{\text{frequency}}{\text{class width}}.
\]

This rearranges to:

\[
\text{frequency}=\text{frequency density}\times \text{class width}.
\]

Since a histogram bar is a rectangle:

\[
\text{area}=\text{width}\times \text{height}.
\]

So when the vertical axis is frequency density:

\[
\text{area}=\text{class width}\times\text{frequency density}=\text{frequency}.
\]

### 6.2 A-Level correction: area is proportional to frequency

At A-Level, the vertical scale may be scaled. So:

\[
\text{area}\not\equiv \text{frequency}
\]

in every question.

Instead:

\[
\text{area}=k\times\text{frequency}.
\]

To find \(k\), use a known area and a known frequency:

\[
k=\frac{\text{known area}}{\text{known frequency}}.
\]

---

## 7. Gaps and True Class Widths

If data are given to the nearest unit, the true class boundaries matter. For example, if a weight class is written as:

\[
1-2
\]

to the nearest kg, the true class interval is:

\[
0.5\leq w<2.5.
\]

So the width is:

\[
2.5-0.5=2.
\]

Not:

\[
2-1=1.
\]

[VISUAL PLACEHOLDER: AS2DataPresentationSVG-005 | Source: S1-Chp3-RepresentationsOfData.pdf pages 28-29 | Insert from svg/AS2DataPresentationSVG-005.svg | Purpose: Show how gaps and true class limits affect histogram class widths.]

---

## 8. Width and Height of Drawn Histogram Bars

Sometimes the question gives the width and height of one bar in centimetres and asks for the width and height of another bar.

[VISUAL PLACEHOLDER: AS2DataPresentationSVG-006 | Source: S1-Chp3-RepresentationsOfData.pdf page 30 | Insert from svg/AS2DataPresentationSVG-006.svg | Purpose: Show proportional scaling from class width to drawn width and from frequency to drawn area.]

Strategy:

1. Use class width to find drawn width.
2. Use the known bar area and known frequency to find the area-frequency scale.
3. Use the new frequency to find the required drawn area.
4. Divide by the new drawn width to find the required drawn height.

---

## 9. Frequency Polygons

A frequency polygon is formed by joining the midpoint of the top of each histogram bar.

[VISUAL PLACEHOLDER: AS2DataPresentationSVG-007 | Source: S1-Chp3-RepresentationsOfData.pdf page 32 | Insert from svg/AS2DataPresentationSVG-007.svg | Purpose: Show a frequency polygon formed by joining histogram bar midpoints.]

Important evidence note: If an interval has frequency \(0\), still include its midpoint at height \(0\). Do not skip it.

---

# Worked Examples

## Worked Example 1: Outliers using \(1.5IQR\), Roman coins

The diameters of 11 different Roman coins are measured in centimetres:

\[
2.2,\;2.5,\;2.7,\;2.7,\;2.8,\;3.0,\;3.1,\;3.1,\;3.2,\;4.0,\;4.7.
\]

Determine the quartiles and hence any outliers.

There are \(n=11\) values.

For the lower quartile:

\[
\frac{11}{4}=2.75.
\]

Because this is a decimal position in an ordered list, use the next position:

\[
Q_1=\text{3rd item}=2.7.
\]

For the median:

\[
\frac{11}{2}=5.5.
\]

Use the next position:

\[
Q_2=\text{6th item}=3.0.
\]

For the upper quartile:

\[
\frac{3\times 11}{4}=8.25.
\]

Use the next position:

\[
Q_3=\text{9th item}=3.2.
\]

Now calculate the IQR:

\[
IQR=Q_3-Q_1=3.2-2.7=0.5.
\]

Lower outlier boundary:

\[
Q_1-1.5IQR=2.7-1.5(0.5)=2.7-0.75=1.95.
\]

Upper outlier boundary:

\[
Q_3+1.5IQR=3.2+1.5(0.5)=3.2+0.75=3.95.
\]

So any value below \(1.95\) or above \(3.95\) is an outlier.

The values above \(3.95\) are:

\[
4.0,\quad 4.7.
\]

Therefore:

\[
\boxed{4.0\text{ cm and }4.7\text{ cm are outliers}.}
\]

---

## Worked Example 2: Outliers using mean and standard deviation, giant African land snails

The lengths, in cm, of 12 giant African land snails are:

\[
17,\;18,\;18,\;19,\;20,\;20,\;20,\;20,\;21,\;23,\;24,\;32.
\]

Given:

\[
\sum x=252,\qquad \sum x^2=5468.
\]

Mean:

\[
\bar{x}=\frac{\sum x}{n}=\frac{252}{12}=21.
\]

Standard deviation:

\[
\sigma=\sqrt{\frac{\sum x^2}{n}-\bar{x}^{2}}
=\sqrt{\frac{5468}{12}-21^2}.
\]

\[
\frac{5468}{12}=455.666\ldots,
\qquad 21^2=441.
\]

\[
\sigma=\sqrt{455.666\ldots-441}=\sqrt{14.666\ldots}=3.8297\ldots
\]

\[
\sigma=3.83\quad \text{to 3 s.f.}
\]

Use \(\bar{x}\pm2\sigma\):

\[
21-2(3.83)=21-7.66=13.34.
\]

\[
21+2(3.83)=21+7.66=28.66.
\]

Since \(32>28.66\):

\[
\boxed{32\text{ cm is an outlier}.}
\]

This does not automatically mean \(32\) is an anomaly. It may be a genuinely large snail.

---

## Worked Example 3: Comparing two outlier rules, ages of MPs

The ages of 15 MPs are:

\[
11,\;18,\;20,\;27,\;30,\;31,\;32,\;32,\;35,\;36,\;37,\;58,\;63,\;78,\;105.
\]

Also given:

\[
\sum x=613,\qquad \sum x^2=33815.
\]

Using the \(1.5IQR\) rule:

\[
\frac{15}{4}=3.75 \Rightarrow Q_1=\text{4th item}=27.
\]

\[
\frac{3\times15}{4}=11.25 \Rightarrow Q_3=\text{12th item}=58.
\]

\[
IQR=58-27=31.
\]

Lower boundary:

\[
27-1.5(31)=27-46.5=-19.5.
\]

Upper boundary:

\[
58+1.5(31)=58+46.5=104.5.
\]

Since \(105>104.5\):

\[
\boxed{105\text{ is an outlier}.}
\]

Using the mean and standard deviation rule:

\[
\bar{x}=\frac{613}{15}=40.866\ldots\approx40.9.
\]

\[
\sigma=\sqrt{\frac{33815}{15}-\left(\frac{613}{15}\right)^2}.
\]

\[
\frac{33815}{15}=2254.333\ldots,
\qquad \left(\frac{613}{15}\right)^2=1669.084\ldots
\]

\[
\sigma=\sqrt{2254.333\ldots-1669.084\ldots}=\sqrt{585.248\ldots}=24.191\ldots\approx24.2.
\]

Boundaries:

\[
40.9-2(24.2)=40.9-48.4=-7.5.
\]

\[
40.9+2(24.2)=40.9+48.4=89.3.
\]

Since \(105>89.3\):

\[
\boxed{105\text{ is an outlier}.}
\]

Both rules identify \(105\) as an outlier.

---

## Worked Example 4: Cleaning an anomaly

A dataset contains an age of \(165\). Given:

\[
\bar{x}=47,\qquad \sigma=44.02.
\]

Use the rule \(\bar{x}\pm2\sigma\).

Lower boundary:

\[
47-2(44.02)=47-88.04=-41.04.
\]

Upper boundary:

\[
47+2(44.02)=47+88.04=135.04.
\]

Since:

\[
165>135.04,
\]

\(165\) is an outlier. But an age of \(165\) is not realistic in this context, so it is likely an anomaly. Therefore the data should be cleaned by removing:

\[
\boxed{165}.
\]

---

## Worked Example 5: Drawing a box plot with an outlier

Given:

| Statistic | Value |
|---|---:|
| Smallest values | \(0,3\) |
| Largest values | \(21,27\) |
| Lower quartile | \(8\) |
| Median | \(10\) |
| Interquartile range | \(6\) |

Find the upper quartile.

\[
IQR=Q_3-Q_1.
\]

\[
6=Q_3-8.
\]

\[
Q_3=14.
\]

Lower boundary:

\[
8-1.5(6)=8-9=-1.
\]

Upper boundary:

\[
14+1.5(6)=14+9=23.
\]

Since \(27>23\), \(27\) is an outlier. The largest value that is not an outlier is \(21\). So the box plot has:

\[
\text{minimum}=0,
\quad Q_1=8,
\quad Q_2=10,
\quad Q_3=14,
\quad \text{upper whisker}=21,
\]

with a cross at \(27\).

Alternative allowed whisker endpoint: \(23\), the outlier boundary. Use one of \(21\) or \(23\), not both.

---

## Worked Example 6: Sales per month and a box plot claim

A company records monthly sales in thousands of pounds.

| Statistic | Value |
|---|---:|
| Two lowest values | \(3,4\) |
| Lower quartile | \(7\) |
| Median | \(12\) |
| Upper quartile | \(14\) |
| Two highest values | \(20,25\) |

\[
IQR=Q_3-Q_1=14-7=7.
\]

Lower boundary:

\[
7-1.5(7)=7-10.5=-3.5.
\]

Upper boundary:

\[
14+1.5(7)=14+10.5=24.5.
\]

Since \(25>24.5\), \(25\) is an outlier. The value \(20\) is the largest value that is not an outlier.

Claim: for \(75\%\) of the months, the amount received per month is greater than £10 000.

The data are in thousands of pounds, so:

\[
£10,000=10.
\]

The lower quartile is \(Q_1=7\). This means \(75\%\) of the months are above £7000, not necessarily above £10 000. Therefore:

\[
\boxed{\text{The claim is false; the box plot supports }75\%\text{ above }£7000,\text{ not }£10000.}
\]

---

## Worked Example 7: Comparing house prices using box plots

Prompt:

> Compare the prices of houses in Croydon with those in Kingston.

A good two-mark answer must include a measure of location, a measure of spread and context.

Example answer:

> The median house price in Kingston is greater than the median house price in Croydon, so a typical house price is higher in Kingston. The interquartile range of house prices in Kingston is greater than the interquartile range in Croydon, so the middle \(50\%\) of house prices are more spread out in Kingston.

---

## Worked Example 8: Cumulative frequency diagram

| Time interval | Frequency | Cumulative frequency |
|---|---:|---:|
| \(9.6<t\leq9.7\) | \(1\) | \(1\) |
| \(9.7<t\leq9.9\) | \(4\) | \(1+4=5\) |
| \(9.9<t\leq10.05\) | \(10\) | \(5+10=15\) |
| \(10.05<t\leq10.2\) | \(17\) | \(15+17=32\) |

Plot:

\[
(9.6,0),\quad(9.7,1),\quad(9.9,5),\quad(10.05,15),\quad(10.2,32).
\]

Total frequency:

\[
n=32.
\]

Lower quartile position:

\[
\frac{32}{4}=8.
\]

From the graph:

\[
Q_1\approx9.95.
\]

Median position:

\[
\frac{32}{2}=16.
\]

From the graph:

\[
Q_2\approx10.07.
\]

Upper quartile position:

\[
\frac{3(32)}{4}=24.
\]

From the graph:

\[
Q_3\approx10.13.
\]

Therefore:

\[
IQR\approx10.13-9.95=0.18.
\]

Less than \(10.15\) seconds:

\[
CF(10.15)\approx26.
\]

More than \(9.95\) seconds:

\[
32-8=24.
\]

Between \(9.8\) and \(10.0\) seconds:

\[
11-3=8.
\]

---

## Worked Example 9: Histogram introduction with unequal class widths

| Age interval | Frequency |
|---|---:|
| \(15\leq a<20\) | \(15\) |
| \(20\leq a<50\) | \(15\) |

For the first group:

\[
\text{class width}=20-15=5,
\]

\[
\text{frequency density}=\frac{15}{5}=3.
\]

For the second group:

\[
\text{class width}=50-20=30,
\]

\[
\text{frequency density}=\frac{15}{30}=0.5.
\]

So the histogram heights should be \(3\) and \(0.5\).

---

## Worked Example 10: Frequency density table

| Weight interval | Frequency | Frequency density |
|---|---:|---:|
| \(0<w\leq10\) | \(40\) | ? |
| \(10<w\leq15\) | \(6\) | ? |
| \(15<w\leq35\) | ? | \(2.6\) |
| \(35<w\leq45\) | ? | \(1\) |

Row 1:

\[
\text{class width}=10-0=10,
\qquad
\text{frequency density}=\frac{40}{10}=4.
\]

Row 2:

\[
\text{class width}=15-10=5,
\qquad
\text{frequency density}=\frac{6}{5}=1.2.
\]

Row 3:

\[
\text{class width}=35-15=20,
\qquad
\text{frequency}=2.6\times20=52.
\]

Row 4:

\[
\text{class width}=45-35=10,
\qquad
\text{frequency}=1\times10=10.
\]

Completed table:

| Weight interval | Frequency | Frequency density |
|---|---:|---:|
| \(0<w\leq10\) | \(40\) | \(4\) |
| \(10<w\leq15\) | \(6\) | \(1.2\) |
| \(15<w\leq35\) | \(52\) | \(2.6\) |
| \(35<w\leq45\) | \(10\) | \(1\) |

---

## Worked Example 11: A-Level histogram scaling

There were \(60\) runners in a \(100\) m race.

The first bar has area:

\[
3\times5=15.
\]

The second bar has area:

\[
6\times1.5=9.
\]

Total area:

\[
15+9=24.
\]

Total frequency:

\[
60.
\]

Use:

\[
\text{area}=k\times\text{frequency}.
\]

So:

\[
24=k\times60.
\]

\[
k=\frac{24}{60}=0.4.
\]

The area above \(14\) seconds is:

\[
4\times1.5=6.
\]

Using \(\text{area}=k\times\text{frequency}\):

\[
6=0.4\times\text{frequency}.
\]

\[
\text{frequency}=\frac{6}{0.4}=15.
\]

Therefore:

\[
\boxed{15\text{ runners}.}
\]

Alternative method:

\[
\frac{6}{24}=\frac14,
\qquad
\frac14\times60=15.
\]

---

## Worked Example 12: Speeding cars and scaled histogram areas

A policeman records the speeds of \(450\) cars.

| Speed interval | Area |
|---|---:|
| \(10\leq s<15\) | \(7.5\) |
| \(20\leq s<30\) | \(60\) |
| \(30\leq s<35\) | \(22.5\) |
| \(35\leq s<40\) | \(7.5\) |
| \(40\leq s<45\) | \(15\) |

Total area:

\[
7.5+60+22.5+7.5+15=112.5.
\]

Total frequency:

\[
450.
\]

\[
112.5=k\times450,
\qquad
k=\frac{112.5}{450}=0.25.
\]

So:

\[
\text{frequency}=\frac{\text{area}}{0.25}.
\]

| Speed interval | Area | Frequency |
|---|---:|---:|
| \(10\leq s<15\) | \(7.5\) | \(7.5\times4=30\) |
| \(20\leq s<30\) | \(60\) | \(60\times4=240\) |
| \(30\leq s<35\) | \(22.5\) | \(22.5\times4=90\) |
| \(35\leq s<40\) | \(7.5\) | \(7.5\times4=30\) |
| \(40\leq s<45\) | \(15\) | \(15\times4=60\) |

Cars exceeding the speed limit by at least \(5\) mph:

\[
s\geq35.
\]

Relevant frequency:

\[
30+60=90.
\]

\[
\boxed{90\text{ cars}.}
\]

Mean speed estimate:

\[
\sum fx=12.5(30)+25(240)+32.5(90)+37.5(30)+42.5(60).
\]

\[
=375+6000+2925+1125+2550=12975.
\]

\[
\bar{x}=\frac{12975}{450}=28.833\ldots\approx28.8\text{ mph}.
\]

Median speed estimate:

Median position:

\[
\frac{450}{2}=225.
\]

The \(225\)th value lies in \(20\leq s<30\), because the cumulative frequency goes from \(30\) to \(270\) in that class.

\[
\text{median}=20+\frac{225-30}{270-30}\times(30-20).
\]

\[
=20+\frac{195}{240}\times10=20+8.125=28.125.
\]

\[
\boxed{\text{median}\approx28.1\text{ mph}.}
\]

---

## Worked Example 13: Gaps in a histogram

If classes are given to the nearest kg:

\[
1-2,
\quad 3-6,
\quad 7-9,
\]

their true class intervals are:

\[
0.5\leq w<2.5,
\]

\[
2.5\leq w<6.5,
\]

\[
6.5\leq w<9.5.
\]

Therefore the class widths are:

\[
2.5-0.5=2,
\]

\[
6.5-2.5=4,
\]

\[
9.5-6.5=3.
\]

---

## Worked Example 14: Motorway delays and histogram gaps

Known total frequencies used:

\[
6,\quad14,\quad17,\quad45,\quad9,\quad5.
\]

Total:

\[
6+14+17+45+9+5=96.
\]

Estimate the percentage delayed between \(8.5\) and \(13.5\) minutes.

From \(8.5\) to \(9.5\), frequency \(17\). From \(9.5\) to \(12.5\), frequency \(45\). From \(12.5\) to \(13.5\), this is \(\frac13\) of a class with frequency \(9\), so:

\[
\frac13\times9=3.
\]

Number between \(8.5\) and \(13.5\):

\[
17+45+3=65.
\]

Percentage:

\[
\frac{65}{96}\times100=67.7083\ldots
\]

\[
\boxed{67.7\%}.
\]

---

## Worked Example 15: Width and height of a drawn histogram bar

A histogram bar for \(0\) to \(4\) seconds is drawn with:

\[
\text{width}=6\text{ cm},
\qquad
\text{height}=8\text{ cm}.
\]

Its area is:

\[
6\times8=48\text{ cm}^2.
\]

The class width \(0\) to \(4\) seconds is:

\[
4.
\]

A second bar is for \(4\) to \(6\) seconds, so its class width is:

\[
6-4=2.
\]

Since:

\[
2=\frac12\times4,
\]

the drawn width is:

\[
\frac12\times6=3\text{ cm}.
\]

The known bar frequency is \(8\), and its area is \(48\), so the area-frequency scale is:

\[
\frac{48}{8}=6.
\]

The new bar has frequency \(9\), so the required area is:

\[
9\times6=54\text{ cm}^2.
\]

Area of rectangle:

\[
\text{area}=\text{width}\times\text{height}.
\]

So:

\[
54=3\times\text{height}.
\]

\[
\text{height}=\frac{54}{3}=18\text{ cm}.
\]

Therefore:

\[
\boxed{\text{width}=3\text{ cm},\quad \text{height}=18\text{ cm}.}
\]

---

## Worked Example 16: Sunshine hours drawn histogram bar

The \(8\) to \(11\) group is represented by a bar of:

\[
\text{width}=1.5\text{ cm},
\qquad
\text{height}=8\text{ cm}.
\]

So its area is:

\[
1.5\times8=12\text{ cm}^2.
\]

This corresponds to a class width of:

\[
11-8=3\text{ hours}.
\]

So:

\[
3\text{ hours}\leftrightarrow1.5\text{ cm}.
\]

Thus:

\[
1\text{ hour}\leftrightarrow\frac{1.5}{3}=0.5\text{ cm}.
\]

For the \(0\) to \(5\) group:

\[
5\text{ hours}\leftrightarrow5(0.5)=2.5\text{ cm}.
\]

So the width is \(2.5\text{ cm}\).

For the \(8\) to \(11\) group, area \(12\) represents frequency \(8\):

\[
12=8k,
\qquad
k=\frac{12}{8}=1.5.
\]

The \(0\) to \(5\) group has frequency \(12\), so the required area is:

\[
12\times1.5=18\text{ cm}^2.
\]

Use:

\[
\text{area}=\text{width}\times\text{height}.
\]

\[
18=2.5\times\text{height}.
\]

\[
\text{height}=\frac{18}{2.5}=7.2\text{ cm}.
\]

Therefore:

\[
\boxed{\text{width}=2.5\text{ cm},\quad \text{height}=7.2\text{ cm}.}
\]

---

## Guided Practice

1. The ordered data are \(4,5,7,9,10,12,14,15,16,31\). Given \(Q_1=7\), \(Q_3=15\), use \(Q_1-1.5IQR\) and \(Q_3+1.5IQR\) to identify any outliers.
2. A dataset has \(\bar{x}=52\), \(\sigma=6.5\). An outlier is any value outside \(\bar{x}\pm2\sigma\). Decide whether \(39\), \(41\), \(65\), and \(68\) are outliers.
3. A cumulative frequency graph has total frequency \(80\). The graph gives \(Q_1\approx12.4\), \(Q_3\approx19.7\). Find the IQR.
4. Complete the table: \(0<x\leq5\), frequency \(20\); \(5<x\leq15\), density \(3\); \(15<x\leq25\), frequency \(15\).
5. A histogram represents \(120\) observations. The total area is \(30\). A shaded part has area \(7.5\). Estimate the number represented by the shaded region.
6. Bus A has median \(24\), IQR \(8\). Bus B has median \(31\), IQR \(4\). Compare in context using one measure of location and one measure of spread.

---

# Common Mistakes and Exam Traps

- A wider box plot section does **not** mean more observations. Each section is \(25\%\).
- Show outlier boundary calculations before drawing outlier crosses.
- Do not treat every outlier as an error.
- At A-Level, histogram area is proportional to frequency. It is not always numerically equal to frequency.
- Do not use raw frequency as histogram height for unequal class widths.
- Use true class boundaries when data are rounded or intervals have gaps.
- Do not skip zero-frequency intervals in a frequency polygon.
- Compare distributions in context, not just with bare phrases like “bigger IQR”.

---

# Exam Technique

## Box plot comparison template

Use:

\[
\text{Median comparison}+\text{context}
\]

and

\[
\text{IQR or range comparison}+\text{context}.
\]

## Outlier technique

1. Write the rule.
2. Calculate \(IQR\) or \(\sigma\) boundaries.
3. Compare actual values.
4. Mark outliers clearly.
5. Interpret cautiously.

## Histogram technique

When given a histogram and asked for a frequency:

1. Find the relevant area.
2. Find the total area or a known area.
3. Find the scale factor.
4. Convert area to frequency.

When asked for mean, median or quartiles from a histogram:

1. Convert the histogram to a grouped frequency table.
2. Use midpoints for the mean.
3. Use cumulative frequencies for median and quartiles.

## Frequency polygon technique

1. Find the midpoint of each class interval.
2. Plot the midpoint at the top of the histogram bar.
3. Join points with straight line segments.
4. Include zero-frequency intervals.

---

# Full Worked Solutions to Guided Practice

## Solution 1

\[
IQR=Q_3-Q_1=15-7=8.
\]

Lower boundary:

\[
7-1.5(8)=7-12=-5.
\]

Upper boundary:

\[
15+1.5(8)=15+12=27.
\]

Since \(31>27\):

\[
\boxed{31\text{ is an outlier}.}
\]

## Solution 2

\[
52-2(6.5)=52-13=39.
\]

\[
52+2(6.5)=52+13=65.
\]

Values outside \(39\leq x\leq65\) are outliers. \(39\) and \(65\) are on the boundary, so they are not outside. \(41\) is inside. \(68>65\), so:

\[
\boxed{68\text{ only}.}
\]

## Solution 3

\[
IQR=Q_3-Q_1=19.7-12.4=7.3.
\]

\[
\boxed{IQR\approx7.3}.
\]

## Solution 4

Row 1:

\[
\frac{20}{5}=4.
\]

Row 2:

\[
3\times10=30.
\]

Row 3:

\[
\frac{15}{10}=1.5.
\]

| Class interval | Frequency | Frequency density |
|---|---:|---:|
| \(0<x\leq5\) | \(20\) | \(4\) |
| \(5<x\leq15\) | \(30\) | \(3\) |
| \(15<x\leq25\) | \(15\) | \(1.5\) |

## Solution 5

\[
\frac{\text{shaded frequency}}{120}=\frac{7.5}{30}=0.25.
\]

\[
\text{shaded frequency}=0.25(120)=30.
\]

\[
\boxed{30\text{ observations}.}
\]

## Solution 6

Bus B has the higher median journey time because \(31>24\), so a typical Bus B journey takes longer. Bus A has the greater IQR because \(8>4\), so the middle \(50\%\) of Bus A journey times are more spread out.

---

# Syllabus Gap Check

| LO ID | Coverage in this lesson | Gap status |
|---|---|---|
| AS2-DPI-LO001 | Strong coverage through box plots, cumulative frequency diagrams, histograms and frequency polygons. | Covered. |
| AS2-DPI-LO002 | Covered through median, IQR, range, mean and standard deviation interpretation. | Covered for this chapter. |
| AS2-DPI-LO003 | Partly covered through standard deviation outlier examples and grouped histogram mean/median calculations. | Further full variance lesson may be needed. |
| AS2-DPI-LO008 | Strong coverage through outlier rules and box plot examples. | Covered. |
| AS2-DPI-LO009 | Covered through display critique and comparison technique. | Covered. |
| AS2-DPI-LO010 | Covered through anomaly and cleaning examples. | Covered. |
| AS2-DPI-LO004 | Scatter diagrams/regression. | Not part of this chapter. |
| AS2-DPI-LO005 | Informal correlation. | Not part of this chapter. |
| AS2-DPI-LO006 | PMCC. | Not part of this chapter. |
| AS2-DPI-LO007 | Correlation does not imply causation. | Not part of this chapter. |

---

# Visual and Interactive Asset Plan

## Mermaid assets

- `AS2DataPresentationMERMAID-001.md` to `AS2DataPresentationMERMAID-010.md`

## SVG assets

- `AS2DataPresentationSVG-001.svg` to `AS2DataPresentationSVG-007.svg`

## TikZ assets

- `AS2DataPresentationTikZ-001.tex` to `AS2DataPresentationTikZ-008.tex`

## Widgets

- `AS2DataPresentationWidget-001.html`: outlier boundary calculator.
- `AS2DataPresentationWidget-002.html`: histogram scaling explorer.
- `AS2DataPresentationWidget-003.html`: cumulative frequency reader.

---

# Supplementary Sources Used

| Source | Status |
|---|---|
| Dr Frost / Pearson / Edexcel-style lesson evidence | Used only where content matches CCEA AS2-DPI. |
| Edexcel Large Data Set examples | Not treated as CCEA-required core. Used only as optional context for interpreting box plots and summary statistics. |
| Normal distribution comments | Treated as future A2 context only. |
| Integration under frequency-density curve comments | Excluded from AS2-DPI core and logged as enrichment/boundary-risk. |
| Sampling subparts in transcript exam questions | Excluded from this chapter core because sampling is a separate AS2 topic. |

---

# Final Student Checklist

## Box plots

- [ ] I can identify the minimum, \(Q_1\), median, \(Q_3\) and maximum.
- [ ] I can calculate the range.
- [ ] I can calculate \(IQR=Q_3-Q_1\).
- [ ] I know that each section of a box plot represents \(25\%\) of the data.
- [ ] I can compare box plots using a measure of location and a measure of spread.

## Outliers and cleaning data

- [ ] I can use \(Q_1-1.5IQR\) and \(Q_3+1.5IQR\).
- [ ] I can use \(\bar{x}-2\sigma\) and \(\bar{x}+2\sigma\).
- [ ] I can explain why an outlier is not automatically an error.
- [ ] I can identify an anomaly when the context makes a value impossible or likely wrong.
- [ ] I can explain what cleaning data means.

## Cumulative frequency

- [ ] I can calculate cumulative frequencies.
- [ ] I can plot upper class boundaries against cumulative frequency.
- [ ] I can estimate \(Q_1\), median and \(Q_3\).
- [ ] I can estimate how many values are less than, more than or between given values.

## Histograms

- [ ] I know histograms are for continuous data.
- [ ] I know frequency is represented by area.
- [ ] I know area may be proportional to frequency rather than equal to it.
- [ ] I can calculate frequency density.
- [ ] I can use a scale factor \(k\).
- [ ] I can handle gaps and true class widths.
- [ ] I can find drawn widths and heights of histogram bars.
- [ ] I can form a frequency polygon using midpoints.

## Exam readiness

- [ ] I show boundary calculations for outliers.
- [ ] I write comparisons in context.
- [ ] I use grouped frequency tables for histogram mean/median questions.
- [ ] I include zero-frequency classes in frequency polygons.
- [ ] I avoid using cross-board-specific assumptions as if they are CCEA requirements.

---

## Final Quality Check Summary

| Check | Result |
|---|---|
| Unit prefix and topic identity | Correct: AS2, AS2-DPI |
| LO IDs | Preserved exactly |
| On-spec evidence | Covered where supplied |
| Off-spec material | Excluded or marked |
| Placeholders | Match asset files in `svg/`, `tikz/`, `mermaid/`, and `widgets/` |
| Unresolved issues | Screenshot PDF text was not parsed; CCEA-specific past-paper questions were not supplied |
