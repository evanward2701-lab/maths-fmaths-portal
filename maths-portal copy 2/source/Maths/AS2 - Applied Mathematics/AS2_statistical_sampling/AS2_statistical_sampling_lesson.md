# AS2 Statistical Sampling Lesson

## Title and Metadata

**Course:** CCEA GCE Mathematics  
**Unit code:** AS2  
**Unit name:** AS 2 Applied Mathematics  
**Applied strand:** Statistics  
**Topic code:** AS2-SAMP  
**Topic name:** Statistical sampling  
**Topic slug:** statistical_sampling  
**Topic Pascal:** StatisticalSampling  
**Topic ID:** AS2StatisticalSampling  
**Lesson file:** AS2_statistical_sampling_lesson.md

**Learning outcome IDs covered:**

- AS2-SAMP-LO001
- AS2-SAMP-LO002
- AS2-SAMP-LO003
- AS2-SAMP-LO004

**Core tags:** `#AS2`, `#Statistics`, `#Sampling`, `#CritiqueMethod`, `#DataCollection`

---

## Evidence Map

| Evidence source | Used for | Status |
|---|---|---|
| CCEA GCE Mathematics Specification Map | Unit, topic code, LO IDs, official learning outcomes, syllabus boundary | Core authority |
| README Module Map | Project naming conventions, file naming, lesson structure | Core project guidance |
| Evidence Drop Checklist | Missing evidence log, off-spec log, visual placeholder rules | Core project guidance |
| S1-Chp1-DataCollection.pdf | Definitions, diagrams, worked examples, method tables, data type summary | Lesson evidence, cross-board source controlled by CCEA boundary |
| Chapter 1 Data Collection transcript | Teacher explanations, verbal warnings, worked method detail, exam-technique comments | Lesson evidence, cross-board source controlled by CCEA boundary |
| Data Collection Screenshots PDF | Visual confirmation of diagrams and slide layout | Visual evidence only |

---

## Specification Alignment

| LO ID | Official CCEA learning outcome | Lesson coverage |
|---|---|---|
| AS2-SAMP-LO001 | demonstrate understanding of and use the terms population and sample | Defines population, sample, sampling unit, sampling frame, census, qualitative/quantitative/discrete/continuous data. |
| AS2-SAMP-LO002 | use samples to make informal inferences about the population | Uses avocado ripeness example and sample-to-population reasoning. Explains why sample size and representativeness matter. |
| AS2-SAMP-LO003 | demonstrate understanding of and use sampling techniques, including simple random sampling and stratified sampling | Covers simple random sampling and stratified sampling in full. Includes systematic, quota and opportunity sampling as supporting comparison and critique vocabulary. |
| AS2-SAMP-LO004 | select or critique sampling techniques in the context of solving a statistical problem, including understanding that different samples can lead to different conclusions about the population | Gives method-selection examples, advantages/disadvantages, bias warnings, rounding checks, sampling-frame checks and full solutions. |

---

## Learning Objectives

By the end of this lesson, you should be able to:

1. Define **population**, **sample**, **sampling unit**, **sampling frame** and **census**.
2. Explain why a sample is often used instead of a census.
3. Use a sample to make an informal inference about a population, while recognising limitations.
4. Describe how to carry out a **simple random sample**.
5. Describe how to carry out a **stratified sample**, including calculating strata sizes.
6. Select an appropriate sampling method for a context.
7. Critique a sampling method by identifying bias, missing sampling frames, destructive testing or poor representativeness.
8. Distinguish between qualitative, quantitative, discrete and continuous data.

---

## Prerequisite Recap

This lesson does **not** rely on GCSE source material. The only prior mathematical skills needed are:

| Skill | Why it matters here |
|---|---|
| Percentages and proportions | Used to calculate how many items to sample from each stratum. |
| Rounding sensibly | Stratified sample sizes may not be whole numbers at first. |
| Interpreting context | Sampling questions are often word-heavy, tiny trapdoors in exam clothing. |
| Clear written explanation | Many marks are awarded for describing a method, not for calculation. |

For stratified sampling, the key proportional idea is:

\[
\text{sample from a group}
=
\frac{\text{group size}}{\text{population size}}
\times
\text{total sample size}
\]

or, using notation:

\[
n_h=\frac{N_h}{N}\times n
\]

where:

- \(N\) is the population size;
- \(n\) is the total sample size;
- \(N_h\) is the size of stratum \(h\);
- \(n_h\) is the number sampled from stratum \(h\).

---

## Big Picture Explanation

Statistics begins with a deceptively simple question:

> Where did the data come from?

Before calculating a mean, drawing a histogram, finding a probability or testing a hypothesis, we need to know whether the data is trustworthy enough to speak for the population.

A **population** is the whole group we care about. A **sample** is the smaller group we actually observe. The sample is meant to act like a tiny window into the population. A good window is clear; a bad one is cracked, fogged, or pointing at the neighbour's shed.

Sampling is therefore not just admin. It controls whether a conclusion is meaningful.

For example, if a supermarket cuts open 5 avocados and finds 4 are ripe, it might estimate:

\[
\frac{4}{5}=0.8=80\%
\]

So it might infer that about \(80\%\) of the whole delivery is ripe. But this inference depends on the sample being large enough and representative enough.

This lesson is mostly “bookwork” in the sense that there is not much algebra, but the language needs to be precise. In exams, these are often one-mark and two-mark questions that students underestimate.

---

## Key Definitions and Notation

### Population

A **population** is the whole set of items that are of interest.

A population does not have to mean people. It could mean:

- all light bulbs produced by a factory in a day;
- all cars in the UK;
- all students in a school;
- all fish in a lake;
- all avocados in a delivery.

### Sample

A **sample** is some subset of the population intended to represent the population.

If the population is all avocados in a delivery, a sample might be 5 avocados chosen from that delivery.

### Sampling unit

A **sampling unit** is each individual thing in the population that can be sampled.

| Population | Sampling unit |
|---|---|
| All students in a school | One student |
| All cars in the UK | One car |
| All bulbs in a batch | One bulb |
| All fish in a lake | One fish |

### Sampling frame

A **sampling frame** is a list of sampling units.

| Context | Sampling frame? |
|---|---|
| A school has a register of every pupil | Yes, the register can be a sampling frame. |
| A telephone directory lists names | Yes, the directory can be a sampling frame. |
| A lake contains fish | Usually no, because there is no list of every fish. |
| UK residents and their handedness | Usually no, because there is no complete list of left-handed and right-handed residents. |

A sampling frame is essential for random methods such as simple random sampling, systematic sampling and stratified sampling.

### Census

A **census** is data collected from the entire population.

If every item in the population is tested or surveyed, the process is a census.

### Qualitative and quantitative data

| Data type | Meaning | Example |
|---|---|---|
| Qualitative or categorical | Non-numerical values | Colour, species, type of drink |
| Quantitative | Numerical values | Height, age, mass, number of children |

### Discrete and continuous data

Quantitative data can be split further:

| Data type | Meaning | Example |
|---|---|---|
| Discrete | Can only take specific values | Shoe size, number of children, number of attempts before success |
| Continuous | Can take any decimal value within a possible range | Height, mass, length of a foot, time |

A discrete variable can still have infinitely many possible values. For example, “number of attempts before success” can be \(1,2,3,\ldots\), with no fixed upper limit, but it cannot be \(2.7\) attempts.

### Grouped data vocabulary

Sometimes data is grouped for conciseness, at the cost of losing exact original values.

A group such as

\[
20\leq w<70
\]

is a **class interval**.

For this class interval:

\[
\text{lower class boundary}=20
\]

\[
\text{upper class boundary}=70
\]

\[
\text{class width}=70-20=50
\]

\[
\text{midpoint}=\frac{20+70}{2}=\frac{90}{2}=45
\]

Grouped data is included here only as vocabulary. More detailed calculations with grouped data belong naturally with data presentation and interpretation.

---

## Core Theory

## 1. Census vs Sample

We could collect data from:

1. the entire population;
2. a sample of the population.

Data from the entire population is a **census**.

### Advantages and disadvantages of a census

| Census | Details |
|---|---|
| Advantage | Should give a completely accurate result, because every member of the population is included. |
| Disadvantage | Time consuming and expensive. |
| Disadvantage | Cannot be used when testing involves destruction. |
| Disadvantage | Produces a large volume of data to process. |

### Advantages and disadvantages of a sample

| Sample | Details |
|---|---|
| Advantage | Cheaper. |
| Advantage | Quicker. |
| Advantage | Less data to process. |
| Disadvantage | Data may not be accurate. |
| Disadvantage | Data may not be large enough to represent small subgroups. |

### Destructive testing

Sometimes a census is impossible because testing destroys the item.

Example: a supermarket wants to test a delivery of avocados for ripeness by cutting them in half. If it tested every avocado, all avocados would be cut open and could not be sold. Therefore, a census would destroy the stock.

Another example: testing the lifespan of batteries may require using them until they are depleted. A census would use up every battery and leave none to sell.

---

## 2. Informal Inference from a Sample

A sample can be used to make an informal inference about the population.

Suppose a supermarket tests 5 avocados and finds 4 are ripe.

The sample proportion ripe is:

\[
\frac{4}{5}
\]

Convert to a decimal:

\[
\frac{4}{5}=0.8
\]

Convert to a percentage:

\[
0.8=80\%
\]

So the supermarket may estimate that \(80\%\) of the delivery is ripe.

But this is only an estimate. A sample of 5 is very small, so it may not represent the full delivery well.

To improve the estimate, the supermarket could increase the sample size.

---

## 3. Random Sampling

In random sampling, we want each sampling unit in the sampling frame to have an equal chance of being chosen, in order to avoid bias.

Random sampling needs a sampling frame.

If there is no sampling frame, a random method cannot be carried out properly.

---

## 4. Simple Random Sampling

### What it is

In simple random sampling, every sampling unit has an equal chance of being selected.

A stronger version of the idea is that every possible sample of the required size has an equal chance of being selected.

### How to carry it out using numbers

Suppose the population has \(N\) sampling units and the required sample size is \(n\).

1. Create or use a sampling frame.
2. Assign a unique number from \(1\) to \(N\) to each sampling unit.
3. Use a random number generator, calculator or random number table to select \(n\) different numbers from \(1\) to \(N\).
4. The sampling units corresponding to those numbers form the sample.

The word **different** matters. If the same number is selected twice, it corresponds to the same sampling unit, so another number must be generated.

### How to carry it out using lottery sampling

1. Write every sampling unit’s name or identifier on identical pieces of paper.
2. Place them in a hat, bowl or equivalent container.
3. Mix thoroughly.
4. Draw out the required number of names without replacement.
5. Those names form the sample.

### Advantages

- Bias free.
- Easy and cheap to implement.
- Each number has a known equal chance of being selected.

### Disadvantages

- Not suitable when the population size is large.
- A sampling frame is needed.

---

## 5. Systematic Sampling

Systematic sampling is included as supporting comparison and critique vocabulary. The CCEA named anchors are simple random and stratified sampling, but systematic sampling is useful when choosing or critiquing methods.

### What it is

In systematic sampling, required elements are chosen at regular intervals in an ordered list.

### Key formula

\[
k=\frac{\text{population size}}{\text{sample size}}
\]

or:

\[
k=\frac{N}{n}
\]

where:

- \(N\) is the population size;
- \(n\) is the required sample size;
- \(k\) is the sampling interval.

### How to carry it out

1. Put the population into a list.
2. Calculate \(k=\frac{N}{n}\).
3. Randomly select a starting number between \(1\) and \(k\).
4. Select every \(k\)th item after that until the sample is complete.

### Why the random start matters

You cannot just say “select every \(k\)th person”. You must say where the counting starts, and that starting point should be random.

### Advantages

- Simple and quick to use.
- Suitable for large samples or populations.

### Disadvantages

- A sampling frame is needed.
- Can introduce bias if the sampling frame is not random.

Example bias: if every 10th item on a production line comes from the same machine, systematic sampling every 10th item may test only that machine rather than the whole process.

---

## 6. Stratified Sampling

### What it is

In stratified sampling, the population is divided into distinct groups called **strata**.

A simple random sample is then taken from each stratum.

The number sampled from each stratum is proportional to the size of that stratum in the population.

### Key formula

For a stratum of size \(N_h\):

\[
n_h=\frac{N_h}{N}\times n
\]

where:

- \(N_h\) is the size of the stratum;
- \(N\) is the total population size;
- \(n\) is the total sample size;
- \(n_h\) is the number sampled from the stratum.

### Why stratified sampling is used

Stratified sampling is useful when the population naturally divides into groups and those groups may affect the variable being studied.

Examples of possible strata:

- year groups in a school;
- age ranges in a workplace;
- gender categories in a survey;
- regions of a country;
- product types in a factory.

### Advantages

- Reflects the population structure.
- Guarantees proportional representation of groups within the population.

### Disadvantages

- The population must be clearly classified into distinct strata.
- Selection within each stratum suffers from the same disadvantages as simple random sampling.

That second disadvantage means: once you are inside each stratum, you still need a sampling frame and a random method.

---

## 7. Quota Sampling

Quota sampling is non-random. It appears in the evidence and is useful for critique, especially where there is no sampling frame.

### What it is

In quota sampling:

1. The population is divided into groups according to a characteristic.
2. A quota of items or people in each group is set to reflect the group’s proportion in the whole population.
3. The interviewer selects the actual sampling units until each quota is filled.

The word **quota** means a fixed share or number of something.

### Why it may be used

Quota sampling may be used when there is no sampling frame.

Example: you want to survey whether left-handedness affects IQ. You do not have a complete list of all left-handed and non-left-handed people in the UK. Therefore, random sampling is problematic.

### Advantages

- Allows a small sample to still be representative of the population.
- No sampling frame required.
- Quick, easy and inexpensive.
- Allows easy comparison between different groups in the population.

### Disadvantages

- Non-random sampling can introduce bias.
- The population must be divided into groups, which can be costly or inaccurate.
- Increasing the scope of the study increases the number of groups, adding time and expense.
- Non-responses are not recorded.

---

## 8. Opportunity or Convenience Sampling

Opportunity sampling is also called convenience sampling.

### What it is

A sample is taken from people who are available at the time of the study and who meet the criteria.

Example: an interviewer stands outside a supermarket and asks available shoppers to answer questions.

### Advantages

- Easy to carry out.
- Inexpensive.

### Disadvantages

- Unlikely to provide a representative sample.
- Highly dependent on the individual researcher.

### Difference between quota and opportunity sampling

| Method | Key idea |
|---|---|
| Quota sampling | Fill required group quotas. |
| Opportunity sampling | Use whoever is available at the time. |

If someone stands outside a supermarket and asks the first 30 people willing to answer, that is opportunity sampling.

If someone stands outside a supermarket and keeps asking until they have 15 males and 15 females, that may be quota sampling.

---

## Visual Asset Integration

[VISUAL PLACEHOLDER: AS2StatisticalSamplingSVG-001 | Source: S1-Chp1-DataCollection.pdf pages 5-6 and transcript Data Collection 1 | Insert from svg/AS2StatisticalSamplingSVG-001.svg | Purpose: Show population, sample, sampling unit and sampling frame in one labelled diagram.]

[VISUAL PLACEHOLDER: AS2StatisticalSamplingSVG-002 | Source: S1-Chp1-DataCollection.pdf page 7 | Insert from svg/AS2StatisticalSamplingSVG-002.svg | Purpose: Compare census and sample advantages and disadvantages.]

[VISUAL PLACEHOLDER: AS2StatisticalSamplingMER-001 | Source: CCEA AS2-SAMP outcomes plus lesson evidence | Insert from mermaid/AS2StatisticalSamplingMER-001.md | Purpose: Decision flowchart for choosing a sampling method based on sampling frame, strata and representativeness.]

[VISUAL PLACEHOLDER: AS2StatisticalSamplingSVG-003 | Source: S1-Chp1-DataCollection.pdf pages 13-14 and transcript Data Collection 2 | Insert from svg/AS2StatisticalSamplingSVG-003.svg | Purpose: Show proportional allocation in stratified sampling.]

[VISUAL PLACEHOLDER: AS2StatisticalSamplingSVG-004 | Source: S1-Chp1-DataCollection.pdf page 20 | Insert from svg/AS2StatisticalSamplingSVG-004.svg | Purpose: Show qualitative, quantitative, discrete and continuous data as a classification tree.]

[INTERACTIVE PLACEHOLDER: AS2StatisticalSamplingWIDGET-001 | Source: Stratified sampling worked examples in lesson evidence | Insert from widgets/AS2StatisticalSamplingWIDGET-001.html | Purpose: Let students enter stratum sizes and total sample size, then calculate proportional sample sizes and rounding checks.]

---

## Worked Examples

## Worked Example 1: Why Not Use a Census?

A supermarket wants to test a delivery of avocados for ripeness by cutting them in half.

### Part a

**Question:** Suggest a reason why the supermarket should not test all the avocados in the delivery.

**Solution:**

Testing the avocados involves cutting them in half.

Cutting an avocado in half damages or destroys it for sale.

Therefore, the supermarket should not test all the avocados because testing the whole population would destroy the stock.

### Part b

The supermarket tests a sample of 5 avocados and finds that 4 are ripe. They estimate that \(80\%\) of the avocados in the delivery are ripe.

**Question:** Suggest one way the supermarket could improve their estimate.

**Solution:**

The sample size is:

\[
5
\]

The number ripe is:

\[
4
\]

The sample proportion ripe is:

\[
\frac{4}{5}=0.8=80\%
\]

But \(5\) is a small sample size.

To improve the estimate, the supermarket could use a larger sample size.

A larger sample is more likely to represent the population accurately.

---

## Worked Example 2: Simple Random Sample of Pupils

There are 64 girls and 56 boys in a school.

Explain briefly how you could take a random sample of 15 pupils using a simple random sample.

### Solution

First find the total number of pupils:

\[
64+56=120
\]

So the population size is:

\[
N=120
\]

The required sample size is:

\[
n=15
\]

A full-mark explanation should include three things:

1. how to identify each sampling unit;
2. how to choose the units randomly;
3. how the selected identifiers become the sample.

Write:

Assign each pupil a unique number from \(1\) to \(120\).

Use a random number generator, calculator or random number table to select \(15\) different numbers from \(1\) to \(120\).

The pupils corresponding to those \(15\) numbers form the sample.

### Mark anatomy

| Required point | Explanation |
|---|---|
| Identifier | Number each pupil from \(1\) to \(120\). |
| Random method | Use a random number generator, calculator or random number table. |
| Link numbers to pupils | Select the pupils whose numbers are generated. |

The word **different** is important because selecting the same number twice would select the same pupil twice.

---

## Worked Example 3: Systematic Sample from a Telephone Directory

A telephone directory contains \(50\,000\) names. A researcher wishes to select a systematic sample of \(100\) names from the directory.

Explain in detail how the researcher should obtain such a sample.

### Solution

Population size:

\[
N=50\,000
\]

Sample size:

\[
n=100
\]

Calculate the sampling interval:

\[
k=\frac{N}{n}
\]

Substitute:

\[
k=\frac{50\,000}{100}
\]

Calculate:

\[
k=500
\]

So the researcher should select every \(500\)th name.

Now choose a random starting point.

The starting point should be a random number from \(1\) to \(500\).

For example, if the random starting number were \(17\), the selected names would be:

\[
17,\ 517,\ 1017,\ 1517,\ldots
\]

continuing every \(500\) names until \(100\) names have been selected.

### Final answer

Randomly select a starting number between \(1\) and \(500\), then select that name and every \(500\)th name after it until \(100\) names have been chosen.

### Exam trap

Do not only write:

> Select every 500th person.

That is incomplete because it does not say how the first item is chosen.

---

## Worked Example 4: Stratified Sample in a School

A school has 15 classes and a sixth form.

In each class there are 30 students.

In the sixth form there are 150 students.

There are equal numbers of boys and girls in each class.

There are equal numbers of boys and girls in the sixth form.

The head teacher wishes to obtain the opinions of the students about school uniforms.

Explain how the head teacher would take a stratified sample of size 40.

### Step 1: Find the total population size

There are 15 classes.

Each class has 30 students.

So the total number of class students is:

\[
15\times 30=450
\]

The sixth form has:

\[
150
\]

students.

So the total school population is:

\[
450+150=600
\]

Therefore:

\[
N=600
\]

The total sample size is:

\[
n=40
\]

### Step 2: Find the sample proportion

\[
\frac{n}{N}=\frac{40}{600}
\]

Simplify:

\[
\frac{40}{600}=\frac{4}{60}
\]

\[
\frac{4}{60}=\frac{2}{30}
\]

\[
\frac{2}{30}=\frac{1}{15}
\]

So the sample should contain:

\[
\frac{1}{15}
\]

of each stratum.

### Step 3: Work out the number from each class

Each class has 30 students.

Number sampled from one class:

\[
\frac{1}{15}\times 30
\]

\[
=\frac{30}{15}
\]

\[
=2
\]

So take \(2\) students from each class.

There are equal numbers of boys and girls in each class.

Each class has:

\[
\frac{30}{2}=15
\]

boys and:

\[
15
\]

girls.

To preserve gender balance within each class, take:

\[
1
\]

boy and:

\[
1
\]

girl from each class.

Across 15 classes, this gives:

\[
15\times 2=30
\]

students.

### Step 4: Work out the number from sixth form

Sixth form size:

\[
150
\]

Number sampled from sixth form:

\[
\frac{1}{15}\times 150
\]

\[
=\frac{150}{15}
\]

\[
=10
\]

There are equal numbers of boys and girls in sixth form.

Number of sixth form boys:

\[
\frac{150}{2}=75
\]

Number of sixth form girls:

\[
75
\]

To preserve gender balance, take:

\[
5
\]

boys and:

\[
5
\]

girls from sixth form.

### Step 5: Check the total sample size

From the 15 classes:

\[
30
\]

From sixth form:

\[
10
\]

Total:

\[
30+10=40
\]

This matches the required sample size.

### Step 6: Explain the random selection

For each of the 15 classes:

- label the boys \(1\) to \(15\);
- label the girls \(1\) to \(15\);
- use a random number generator to select one boy and one girl from each class.

For the sixth form:

- label the boys \(1\) to \(75\);
- label the girls \(1\) to \(75\);
- use a random number generator to select 5 different boys and 5 different girls.

### Final answer

Take one boy and one girl randomly from each of the 15 classes, and take 5 boys and 5 girls randomly from the sixth form, using random numbers within each group. This gives a stratified sample of size \(40\).

---

## Worked Example 5: Stratified Sample of Factory Workers

A factory manager wants to find out what workers think about the factory canteen facilities.

The manager decides to give a questionnaire to a sample of 80 workers.

It is thought that different age groups will have different opinions.

There are:

- 75 workers aged 18 to 32;
- 140 workers aged 33 to 47;
- 85 workers aged 48 to 62.

### Part a: Name the sampling method

Because the population naturally divides into age groups, and the question says different age groups may have different opinions, the manager should use:

\[
\text{stratified sampling}
\]

### Part b: Work out how many workers to sample from each age group

First find the total population size:

\[
N=75+140+85
\]

\[
N=215+85
\]

\[
N=300
\]

The sample size is:

\[
n=80
\]

The sample proportion is:

\[
\frac{n}{N}=\frac{80}{300}
\]

Simplify:

\[
\frac{80}{300}=\frac{8}{30}
\]

\[
\frac{8}{30}=\frac{4}{15}
\]

So the sample should include:

\[
\frac{4}{15}
\]

of each age group.

#### Age group 18 to 32

\[
\frac{4}{15}\times 75
\]

\[
=\frac{4\times 75}{15}
\]

\[
=4\times 5
\]

\[
=20
\]

So sample:

\[
20
\]

workers aged 18 to 32.

#### Age group 33 to 47

\[
\frac{4}{15}\times 140
\]

\[
=\frac{560}{15}
\]

\[
=37.333\ldots
\]

Round to:

\[
37
\]

So sample:

\[
37
\]

workers aged 33 to 47.

#### Age group 48 to 62

\[
\frac{4}{15}\times 85
\]

\[
=\frac{340}{15}
\]

\[
=22.666\ldots
\]

Round to:

\[
23
\]

So sample:

\[
23
\]

workers aged 48 to 62.

### Step 3: Check the total

\[
20+37+23=80
\]

The rounded values add to the required sample size.

### Step 4: Explain how to select the workers

Number the workers in each age group.

Use a random number generator to select:

- 20 workers from the 18 to 32 group;
- 37 workers from the 33 to 47 group;
- 23 workers from the 48 to 62 group.

Give the questionnaire to the selected workers.

---

## Worked Example 6: Quota Sample of Fish

A lake contains three species of fish.

There are estimated to be:

- 1400 trout;
- 600 bass;
- 450 pike.

A survey of the health of the fish in the lake is carried out and a sample of 30 fish is chosen.

### Part a: Why can stratified random sampling not be used?

Stratified random sampling needs a sampling frame.

There is no list of every fish in the lake.

Therefore, stratified random sampling cannot be used.

### Part b: State an appropriate sampling method

An appropriate method is:

\[
\text{quota sampling}
\]

### Part c: Work out the quotas

Total estimated number of fish:

\[
N=1400+600+450
\]

\[
N=2000+450
\]

\[
N=2450
\]

Sample size:

\[
n=30
\]

#### Trout quota

\[
\frac{1400}{2450}\times 30
\]

\[
=\frac{42000}{2450}
\]

\[
=17.142857\ldots
\]

Round to:

\[
17
\]

#### Bass quota

\[
\frac{600}{2450}\times 30
\]

\[
=\frac{18000}{2450}
\]

\[
=7.346938\ldots
\]

Round to:

\[
7
\]

#### Pike quota

\[
\frac{450}{2450}\times 30
\]

\[
=\frac{13500}{2450}
\]

\[
=5.510204\ldots
\]

Round to:

\[
6
\]

### Step 4: Check the total quota

\[
17+7+6=30
\]

So the quotas are:

| Species | Quota |
|---|---:|
| Trout | 17 |
| Bass | 7 |
| Pike | 6 |

### Step 5: Explain how the sample is selected

Catch fish from the lake until the quotas are filled:

- 17 trout;
- 7 bass;
- 6 pike.

If a fish is caught and that species quota is already full, ignore it for the sample and return it to the lake.

### Advantage

The sample can be obtained quickly and no sampling frame is required.

### Disadvantage

The process is not random, so bias may be introduced.

---

## Guided Practice

### Question 1: Definitions

A researcher is studying the heights of students in a school.

a. State the population.  
b. State one possible sampling unit.  
c. State one possible sampling frame.

### Question 2: Census or Sample?

A factory produces batteries. To test a battery’s lifespan, the battery must be used until it has no energy left.

Explain why the factory should not use a census to test battery lifespan.

### Question 3: Informal Inference

A sample of 20 packets of biscuits is tested. In 3 packets, the number of biscuits is lower than advertised.

a. Find the proportion of packets in the sample with too few biscuits.  
b. Express this as a percentage.  
c. Explain why this may not exactly equal the percentage for all packets produced.

### Question 4: Simple Random Sampling

A club has 100 members listed alphabetically in a membership book.

The committee wants to select a sample of 12 members.

Explain how to use a random number generator to take a simple random sample.

### Question 5: Lottery Sampling

Using the same club of 100 members, explain how to take a lottery sample of 12 members.

### Question 6: Systematic Sampling

A list contains 240 names. A researcher wants a systematic sample of 30 names.

a. Calculate the sampling interval \(k\).  
b. Explain how the sample should be selected.

### Question 7: Stratified Sampling

A college has students in three year groups:

| Year group | Number of students |
|---|---:|
| Year 12 | 180 |
| Year 13 | 120 |
| Year 14 | 60 |

A stratified sample of 60 students is required.

Calculate how many students should be selected from each year group.

### Question 8: Method Selection

Suggest a suitable sampling method for each situation.

a. A factory wants to test light bulbs produced throughout a daily batch.  
b. A company wants quick opinions on a new drink from shoppers outside a supermarket.  
c. A school wants a sample of pupils that fairly represents each year group.

### Question 9: Data Types

Classify each variable as qualitative, quantitative discrete, or quantitative continuous.

a. Colour of a car.  
b. Number of children in a family.  
c. Height of a student.  
d. Shoe size.  
e. Time taken to run 100 m.

---

## Common Mistakes and Exam Traps

### Mistake 1: Saying “population” when you mean “sample”

The population is the whole group of interest. The sample is the smaller group chosen from it.

In a telephone directory question:

- population: all \(50\,000\) names;
- sampling frame: the telephone directory;
- sample: the \(100\) selected names;
- sampling unit: one name/person.

### Mistake 2: Forgetting the sampling frame

Random methods need a list.

If there is no sampling frame, do not claim you can carry out a simple random sample properly.

### Mistake 3: Forgetting the random starting point in systematic sampling

For systematic sampling, you need:

\[
k=\frac{N}{n}
\]

and a random start between \(1\) and \(k\).

Do not merely write:

> Choose every \(k\)th item.

### Mistake 4: Forgetting to use different random numbers

In simple random sampling, use \(n\) different random numbers.

Repeated numbers select the same sampling unit again.

### Mistake 5: Rounding strata sizes without checking the total

In stratified sampling, rounded group sizes must add to the total sample size.

For the factory example:

\[
20+37+23=80
\]

This check is not decorative. It is the little bolt that keeps the statistical wheel on.

### Mistake 6: Calling quota sampling random

Quota sampling is not random. The interviewer selects the actual sampling units.

### Mistake 7: Treating a small sample as definitely accurate

A sample can suggest a population conclusion, but different samples can lead to different conclusions.

### Mistake 8: Using a census when testing destroys items

If the test destroys or damages every item, a census is unsuitable.

---

## Exam Technique Notes

### How to answer “Explain how to take a simple random sample”

Include:

1. assign a number to every sampling unit;
2. use a random number generator or equivalent;
3. choose the required number of different numbers;
4. select the corresponding sampling units.

Template:

> Number the \(N\) sampling units from \(1\) to \(N\). Use a random number generator to select \(n\) different numbers. The sampling units corresponding to these numbers form the sample.

### How to answer “Explain how to take a systematic sample”

Include:

1. calculate \(k=\frac{N}{n}\);
2. randomly choose a starting number from \(1\) to \(k\);
3. select every \(k\)th item after that.

Template:

> Calculate \(k=\frac{N}{n}\). Randomly choose a starting number between \(1\) and \(k\), then select that item and every \(k\)th item after it until the sample is complete.

### How to answer “Explain how to take a stratified sample”

Include:

1. identify the strata;
2. calculate the number from each stratum using proportional allocation;
3. round carefully if needed;
4. check the total sample size;
5. randomly select within each stratum.

Template:

> Divide the population into strata. For each stratum, calculate \(\frac{\text{stratum size}}{\text{population size}}\times\text{sample size}\). Then use a random method to select the required number from each stratum.

### How to critique a method

Ask:

1. Is there a sampling frame?
2. Is the method random?
3. Could the interviewer introduce bias?
4. Does the sample represent important subgroups?
5. Is the sample large enough?
6. Does testing destroy the item?
7. Could different samples lead to different conclusions?

---

## Full Worked Solutions to Guided Practice

## Solution 1: Definitions

A researcher is studying the heights of students in a school.

### Part a

The population is:

\[
\text{all students in the school}
\]

### Part b

One sampling unit is:

\[
\text{one student}
\]

### Part c

One possible sampling frame is:

\[
\text{a complete school register or student list}
\]

---

## Solution 2: Census or Sample?

A factory produces batteries. To test a battery’s lifespan, the battery must be used until it has no energy left.

A census would test every battery in the population.

Testing one battery’s lifespan uses up that battery.

Testing every battery would use up all the batteries.

Therefore, the factory should not use a census because the testing is destructive and the batteries could not then be sold.

---

## Solution 3: Informal Inference

A sample of 20 packets of biscuits is tested.

In 3 packets, the number of biscuits is lower than advertised.

### Part a

The sample proportion is:

\[
\frac{3}{20}
\]

### Part b

Convert to a decimal:

\[
\frac{3}{20}=0.15
\]

Convert to a percentage:

\[
0.15=15\%
\]

So \(15\%\) of the sample had too few biscuits.

### Part c

This may not exactly equal the percentage for all packets because only a sample was tested.

The sample may not be perfectly representative of the whole population of packets.

Different samples could lead to different conclusions.

---

## Solution 4: Simple Random Sampling

A club has 100 members listed alphabetically.

Required sample size:

\[
n=12
\]

Population size:

\[
N=100
\]

Assign each member a unique number from \(1\) to \(100\).

Use a random number generator to select \(12\) different numbers between \(1\) and \(100\).

The members corresponding to those numbers form the sample.

---

## Solution 5: Lottery Sampling

Write all 100 members’ names on identical pieces of paper.

Place the pieces of paper into a hat or bowl.

Mix thoroughly.

Draw out 12 names without replacement.

The 12 names drawn form the sample.

---

## Solution 6: Systematic Sampling

A list contains 240 names.

A researcher wants a systematic sample of 30 names.

### Part a

Population size:

\[
N=240
\]

Sample size:

\[
n=30
\]

Sampling interval:

\[
k=\frac{N}{n}
\]

\[
k=\frac{240}{30}
\]

\[
k=8
\]

### Part b

Randomly choose a starting number between \(1\) and \(8\).

Then select that name and every 8th name after it until 30 names have been selected.

For example, if the random starting number were \(5\), the selected positions would be:

\[
5,\ 13,\ 21,\ 29,\ldots
\]

until the sample contains 30 names.

---

## Solution 7: Stratified Sampling

The college has:

| Year group | Number of students |
|---|---:|
| Year 12 | 180 |
| Year 13 | 120 |
| Year 14 | 60 |

First find the total population size:

\[
N=180+120+60
\]

\[
N=300+60
\]

\[
N=360
\]

The required sample size is:

\[
n=60
\]

The sample proportion is:

\[
\frac{n}{N}=\frac{60}{360}
\]

Simplify:

\[
\frac{60}{360}=\frac{1}{6}
\]

### Year 12

\[
\frac{1}{6}\times 180
\]

\[
=\frac{180}{6}
\]

\[
=30
\]

### Year 13

\[
\frac{1}{6}\times 120
\]

\[
=\frac{120}{6}
\]

\[
=20
\]

### Year 14

\[
\frac{1}{6}\times 60
\]

\[
=\frac{60}{6}
\]

\[
=10
\]

Check:

\[
30+20+10=60
\]

So select:

| Year group | Sample size |
|---|---:|
| Year 12 | 30 |
| Year 13 | 20 |
| Year 14 | 10 |

Then randomly select the required number from each year group.

---

## Solution 8: Method Selection

### Part a

A factory wants to test light bulbs produced throughout a daily batch.

A suitable method is systematic sampling.

Reason: the light bulbs can be taken at regular intervals, such as every \(k\)th bulb, throughout the batch. This is simpler than trying to locate many randomly chosen bulbs.

Caution: if every selected bulb came from the same machine or same part of the production cycle, the sample could be biased.

### Part b

A company wants quick opinions on a new drink from shoppers outside a supermarket.

A suitable method is opportunity sampling.

Reason: the company can ask people who are available at the time.

Caution: this may not be representative of all consumers in the UK.

Quota sampling could also be used if the company wants to fill specific groups, such as age groups.

### Part c

A school wants a sample of pupils that fairly represents each year group.

A suitable method is stratified sampling.

Reason: the school likely has a sampling frame, such as a student register, and the year groups are natural strata. The sample can represent each year group proportionally.

---

## Solution 9: Data Types

### Part a

Colour of a car is non-numerical.

So it is:

\[
\text{qualitative/categorical}
\]

### Part b

Number of children in a family is numerical and can only take whole-number values.

So it is:

\[
\text{quantitative discrete}
\]

### Part c

Height of a student is numerical and can be measured to any level of precision within a range.

So it is:

\[
\text{quantitative continuous}
\]

### Part d

Shoe size can only take specific permitted values.

So it is:

\[
\text{quantitative discrete}
\]

### Part e

Time taken to run 100 m is numerical and can be measured to increasing precision.

So it is:

\[
\text{quantitative continuous}
\]

---

## Common CCEA-Style Wording

### “State the population”

Name the whole group being studied.

Example:

> The population is all students in the school.

### “Identify the sampling frame”

Name the list used to select the sample.

Example:

> The sampling frame is the school register.

### “Suggest why a census is unsuitable”

Use context.

Possible reasons:

- too time consuming;
- too expensive;
- testing destroys or damages the items;
- too much data to process.

### “Suggest one way to improve the estimate”

Possible answers:

- use a larger sample size;
- use a more representative sample;
- use a random sampling method;
- use stratified sampling if important subgroups exist.

### “Describe how a stratified sample would be conducted”

Use the proportional allocation formula and explain the random selection within each group.

---

## Syllabus Gap Check

| LO ID | Coverage status | Notes |
|---|---|---|
| AS2-SAMP-LO001 | Covered | Population, sample, census, qualitative/quantitative/discrete/continuous data included. Sampling unit and sampling frame added as essential vocabulary. |
| AS2-SAMP-LO002 | Covered | Informal inference from avocado and biscuit examples. Limitations of samples explained. |
| AS2-SAMP-LO003 | Covered | Simple random and stratified sampling covered in full. Systematic sampling included as supporting technique vocabulary. |
| AS2-SAMP-LO004 | Covered | Method selection, critique, bias, sample size, sampling frame and context warnings included. |

### Off-spec content excluded from core

| Evidence item | Decision |
|---|---|
| Edexcel Large Data Set weather material | Excluded from core CCEA AS2-SAMP lesson. |
| Edexcel S3 labels | Removed as required exam labels. Examples adapted only where the method matches the CCEA sampling topic. |
| MAT/UKMT extension references | Excluded. |
| Detailed grouped-frequency calculations | Deferred to AS2 Data presentation and interpretation. |

---

## Visual and Interactive Asset Plan

| Asset ID | Type | Planned file | Purpose |
|---|---|---|---|
| AS2StatisticalSamplingSVG-001 | SVG | svg/AS2StatisticalSamplingSVG-001.svg | Population, sample, sampling unit and sampling frame diagram. |
| AS2StatisticalSamplingSVG-002 | SVG | svg/AS2StatisticalSamplingSVG-002.svg | Census vs sample comparison table visual. |
| AS2StatisticalSamplingMER-001 | Mermaid | mermaid/AS2StatisticalSamplingMER-001.md | Sampling method decision flowchart. |
| AS2StatisticalSamplingSVG-003 | SVG | svg/AS2StatisticalSamplingSVG-003.svg | Stratified sampling proportional allocation diagram. |
| AS2StatisticalSamplingSVG-004 | SVG | svg/AS2StatisticalSamplingSVG-004.svg | Data type classification tree. |
| AS2StatisticalSamplingWIDGET-001 | HTML widget | widgets/AS2StatisticalSamplingWIDGET-001.html | Stratified sample calculator with rounding check. |

No diagram, TikZ file or widget was generated inside Phase 1. Phase 1 inserted placeholders only.

---

## Supplementary Sources Used

No additional web sources or external GCSE sources were used.

The lesson uses:

- CCEA specification map and module map as the boundary authority.
- The supplied Data Collection PDF and transcript as lesson evidence.
- The supplied screenshot PDF as visual confirmation only.

Cross-board references in the lesson evidence were controlled against the CCEA AS2-SAMP boundary. Edexcel-specific Large Data Set material was excluded from the core lesson.

---

## Final Student Checklist

### Vocabulary

- [ ] I can define population.
- [ ] I can define sample.
- [ ] I can define sampling unit.
- [ ] I can define sampling frame.
- [ ] I can define census.
- [ ] I can distinguish qualitative and quantitative data.
- [ ] I can distinguish discrete and continuous data.

### Census and sample

- [ ] I can give advantages of a census.
- [ ] I can give disadvantages of a census.
- [ ] I can explain why destructive testing makes a census unsuitable.
- [ ] I can give advantages of a sample.
- [ ] I can give disadvantages of a sample.
- [ ] I can explain why a sample may not represent small subgroups.

### Sampling methods

- [ ] I can describe simple random sampling.
- [ ] I can explain why simple random sampling needs a sampling frame.
- [ ] I can describe systematic sampling, including the random start.
- [ ] I can describe stratified sampling.
- [ ] I can calculate strata sizes using proportional allocation.
- [ ] I can check rounded strata sizes add to the required sample size.
- [ ] I can describe quota sampling as a non-random method.
- [ ] I can describe opportunity sampling as a non-random method.

### Exam readiness

- [ ] I can identify the population, sample, sampling unit and sampling frame in a context.
- [ ] I can choose a suitable sampling method and justify it.
- [ ] I can critique a sampling method.
- [ ] I can explain how different samples can lead to different conclusions.
- [ ] I can write full method descriptions, not just name the method.

---

## Final Quality Check Summary

| Check | Result |
|---|---|
| Unit prefix correct | Yes, AS2 |
| Standard Mathematics, not Further Mathematics | Yes |
| Topic identity complete | Yes |
| Topic code correct | AS2-SAMP |
| Topic ID correct | AS2StatisticalSampling |
| Lesson file name correct | AS2_statistical_sampling_lesson.md |
| LO IDs preserved exactly | AS2-SAMP-LO001 to AS2-SAMP-LO004 |
| On-spec evidence covered | Yes |
| Cross-board evidence controlled | Yes |
| Off-spec material excluded or marked | Yes |
| Diagram placeholders matched to assets | Yes |
| Widget placeholder matched to asset | Yes |
| Manifest drafted | Yes |
| Source reference drafted | Yes |
| Unresolved issues | No CCEA-specific past-paper examples were supplied; otherwise none found |
