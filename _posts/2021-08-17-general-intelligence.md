---
layout: post
title: "General factors of intelligence and physical fitness"
image: /img/g/cigar.jpg
tags: statistics personality
hero_light: false
dark_title: false
background_color: black
description: "A review of correlations between human performance on physical and mental tasks, plus a description of how factor analysis is like a cigar"
permalink: /general-intelligence/
background_color: rgb(148,134,121)
category: "psychology"
comment:
    hacker news: https://news.ycombinator.com/item?id=30791424
---

Is there a general factor of intelligence?

This question is a trap. If you try to answer it, you’ll find yourself beset by semantic questions. What’s *intelligence*? What’s a *factor*? And if you get past those, you'll then find a bleak valley of statistical arcana. What do the eigenvalues look like? Do they imply causality?

This is all backward. If your goal is to understand the external world, you can skip the hand wringing and start by looking at the damn data. So let's do that. 

{% comment %}
The facts are pretty simple. People who are good at one physical task also tend to be good at others. Faster runners tend to be able to do more push-ups. For mental tasks, the same positive correlations exist: People who are good at arithmetic also tend to have good memories.

Still, do these correlations have some deeper meaning? One theory is that you can model people's performance on all mental tasks using just a single number plus random noise. This is the idea behind the method called factor analysis. Factor analysis is often described using a lot of math. However, as I'll explain, it all really boils down to the question of how much the data looks like a cigar.
{% endcomment %}

{% comment %}
### Contents
{:.no_toc}

<div style="font-size:100%;" markdown="1">
* auto-gen TOC:
{:toc}
</div>
{% endcomment %}

## Physical tests are correlated

To start, let's forget about intelligence, and ask an easier question: Does it make sense to refer to some people as "more physically fit" than others? Is that reasonable, or do we need to break things down by strength, speed, coordination, etc.?

To answer this, I looked for studies that gave people batteries of different physical tests. I found three that make enough information available to analyze.

Paper | Population
- | - 
[Baumgartner and Zuidema, 1972](https://doi.org/10.1080/10671188.1972.10615157) | 283 male and 336 female college students in Michigan
[Marsh and Redmaye, 1994](https://doi.org/10.1123/jsep.16.1.43) | 105 students at two private girls' schools in Sydney
[Ibrahim et al., 2011](https://doi.org/10.2466/03.06.19.25.pms.113.5.491-508) | 330 Malaysian students aged 12-15

Here are the correlations among the different tests (click to open/close). The columns are the same as the rows---so the 3rd square in the first row is the correlation between hand grip and pull-ups.

{% comment %}
Are strong people also fast? Here are the correlations among males in Baumgartner and Zuidema's study. (Females are similar except with lower correlations in upper-body strength.)

[![baumgartner 1973 physical fitness correlations](/img/g/tables/baumgartner1972.svg)](/img/g/tables/baumgartner1972.pdf)

And here are the other studies (click to open/close):
{% endcomment %}

<details markdown="1" open="1">
<summary><b>Baumgartner and Zuidema</b></summary>
[![baumgartner 1973 physical fitness correlations](/img/g/tables/baumgartner1972.svg)](/img/g/tables/baumgartner1972.pdf)
This is males. (Females are similar, except with lower correlations in upper-body strength.)
</details>

<details markdown="1">
<summary><b>Marsh and Redmaye</b></summary>
[![marsh 1994 physical fitness correlations](/img/g/tables/marsh1994.svg)](/img/g/tables/marsh1994.pdf)
</details>

<details markdown="1">
<summary><b>Ibrahim et al.</b></summary>
[![ibrahim 2011 physical fitness correlations](/img/g/tables/ibrahim2011.svg)](/img/g/tables/ibrahim2011.pdf)
</details>

Most tests are positively correlated, and none are negative. Is this surprising? I don't know. For our purposes, we just want this as a point of comparison.

## Mental tests are correlated

We can do the same analysis with batteries of mental tests. For whatever reason, many more studies have been done with mental tests, so I picked four of the best.

Paper | Population
- | - 
[Alderton et al. 1997](https://doi.org/10.1207/s15327876mp0901_1) | 12,813 members of the US Navy, Army, and Air Forces
[Deary, 2000](https://doi.org/10.1093/acprof:oso/9780198524175.001.0001) |  365 representative Scottish people
[Chabris 2011](http://www.chabris.com/Chabris2007a.pdf) | 111 Boston adults 18 - 60 years old
[MacCann et al., 2014](https://doi.org/10.1037/a0034755) | 688 students from colleges around the US.

Here are the correlations in each of the studies (again, click to open/close):

<details markdown="1" open="1">
<summary><b>Alderton et al.</b></summary>
[![Alderton 1997 correlations](/img/g/tables/alderton1997.svg)](/img/g/tables/alderton1997.pdf)
This test battery is designed to measure aptitude for various military tasks. Some of these, like tracking and target identification, are partly physical.
</details>


<details markdown="1">
<summary><b>Deary</b></summary>
[![chabris 2007 correlations](/img/g/tables/chabris2007a.svg)](/img/g/tables/chabris2007a.pdf)
These subjects were tested on the 11-component revised [Wechsler Adult Intelligence Scale](https://en.wikipedia.org/wiki/Wechsler_Adult_Intelligence_Scale#WAIS-R).

As an aside, the origins of these data are somewhat obscure: Chabris published them, crediting [Deary (2000)](https://doi.org/10.1093/acprof:oso/9780198524175.001.0001) who in turn credits personal communication from Crawford, with no other information. Whoever Crawford is, they deserve way more recognition on [Wikipedia](https://en.wikipedia.org/wiki/G_factor_(psychometrics)#Cognitive_ability_testing).

</details>

<details markdown="1">
<summary><b>Chabris</b></summary>
[![chabris 2007 correlations](/img/g/tables/chabris2007b.svg)](/img/g/tables/chabris2007b.pdf)
The data was gathered as part of a project to test decision-making. [Raven's matrices](https://en.wikipedia.org/wiki/Raven%27s_Progressive_Matrices) test shape pattern recognition, working memory is tested via [3-back](https://en.wikipedia.org/wiki/N-back), and the coordinate encoding tests check if people can tell the distance or orientation of a dot relative to a line.
</details>

<details markdown="1">
<summary><b>MacCann et al.</b></summary>
[![maccann 2014 correlations](/img/g/tables/maccann2014.svg)](/img/g/tables/maccann2014.pdf)
The colors group the tests into those that test fluid reasoning, comprehension, quantitative knowledge, visual processing, and long-term storage/retrieval.
</details>

## What do we see?

The same basic pattern holds for both physical and mental tests.

First, **almost everything is positively correlated**. You might imagine that people with more upper-body strength would be worse runners---what with the extra muscle they need to carry around. You might imagine that people who are good at paragraph comprehension would be worse at math. But that's not what happens.

Second, **more similar stuff is more correlated**. It's natural that chin-ups are strongly correlated with pull-ups, or that arithmetic reasoning is strongly correlated with mathematics knowledge. It's more surprising that hand-grip strength is correlated with the 75-yd dash or that paragraph comprehension is correlated with target identification. These more surprising correlations are weaker, but still positive.

Third, **the results are robust**. The tests span several decades, different countries, and many different test batteries. The basic pattern doesn't change.

Things are correlated. No one seems to seriously dispute this. So why all the debates?

For one thing, the discussion sometimes ascends into meta-controversy. There are many arguments to be had about the definition of "general intelligence". Some people even debate [if there is anything controversial](https://doi.org/10.1007/s10519-014-9646-x)! (I take no position here, but note that the "not surprising" camp doesn't seem to agree on *why* it's not surprising...)

On the lower planes of argument, the main issue is if the tests are *just correlated* or if there's something deeper going on underneath of them. Here, the burden of proof falls on whoever claims there is something deeper.

*Aside*: The mental correlations are somewhat stronger than the physical ones, but don't take that too seriously. The mental tests used more diverse populations than the physical tests. Imagine doing physical tests on a group of 20-year-olds. If you throw in a bunch of 80-year-olds, they'll be worse at everything and correlations will shoot up.

{% comment %}
One way to approach this is to ask how many numbers you need to describe someone. Suppose you've tested people on four physical tasks:

* Push-ups
* Pull-ups
* 5-kilometer run
* 100-meter sprint

With four numbers for each person, you could describe everyone perfectly. With *zero* numbers, the best you could do is remember the population averages. The question is, how well can you do with just a single number? This is the basic idea behind the statistical technique called [factor analysis](https://en.wikipedia.org/wiki/Factor_analysis).
{% endcomment %}

## Factor analysis is like a cigar

The typical argument that there's something deeper happening relies on a statistical technique called [factor analysis](https://en.wikipedia.org/wiki/Factor_analysis). This is usually described with fancy technical language, but the basic idea is just that you can summarize all the tests for each person using a single number.

{% comment %}
While factor analysis is usually described with fancy technical language, the basic idea is simple: Picture your data as a point cloud, approximate it with a cigar, and then describe each point using its position along the length of the cigar. If a cigar fits the data well, then one number captures all the interesting latent structure behind the data. If it doesn't fit well, then there's something more interesting going on.
{% endcomment %}

Let's make this concrete. Say you go out and grab random people and test them, and get this data:

{% comment %}
```
Person    Test 1   Test 2   Test 3
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Antonio    1       -1        1.5
Bart      -0.5      0.5     -0.75
Cathy     -2        2       -3
Dara        .67     -.67     1
```
{% endcomment %}

<div style="display:flex; justify-content:center;" markdown="1">
<div markdown="1">

Person | Test 1 | Test 2 | Test 3
-|-|-|-
Antonio |    1    |   -1   |     1.5
Bart    |    .67  |   -.67 |    1
Cathy   |  -0.5   |   0.5  |   -0.75
Dara    |  -2     |   2    |   -3

</div>
</div>

<br>

You can visualize the data as a magical rotating point-cloud:

<!--
![spinning point cloud of dataset](/img/g/3dplot/data.gif)
-->

{% include video.html where="/img/g/3dplot/data" title="spinning point cloud of dataset" %}

Now, notice something important: This data is *special*, in that the points fall along a straight line. This means that even though each person took 3 tests, you can represent each person using a single number, namely their position on the line. If you tested lots of people, and the data looked like this, then each person's position along the line would be the "general factor".

Of course, real data would never exactly look like this. It would have noise! To reflect that, we need to build a "model". That is, we will try to build a "simulator" that can make fake data that (hopefully) looks like real data.

### Simulations
{:.no_toc}

The simplest simulator would be to just generate people along a line. First, pick some direction of variation. Then, to simulate a person (i.e. a set of test scores), draw a random number **g** from a standard "bell curve" [Normal distribution](https://en.wikipedia.org/wiki/Normal_distribution) to represent their position along the main direction.

Here's an example, where we choose a direction of variation similar to the dataset above. If you simulate a bunch of people, you'll get a dataset that looks like this:

<!--
![factor analysis with no noise](/img/g/3dplot/line.gif)
-->

{% include video.html where="/img/g/3dplot/line" title="factor analysis with no noise" %}

Of course, real data will never look like that---there will always be "noise", either from measurement error, or from certain people randomly being good/bad at certain tasks. To account for this, let's update our simulator, by adding some random noise to each point. This produces data that looks like a cigar.

<!--
![factor analysis with noise](/img/g/3dplot/cigar.gif)
-->

{% include video.html where="/img/g/3dplot/cigar-nolines" title="factor analysis with noise" %}

The critical thing here is that cigars are rotationally symmetric. If you "roll" the point cloud along the main axis of variation, it still looks basically the same.

Now we can finally say what factor analysis is. It's an algorithm that takes a real dataset and adjusts the shape of the cigar so that the simulated data will look as much like the real data as possible. It can modify the direction of variation, and how "thick" the cigar is, but that's it. (Note: all this describes the *simplest* possible variant of factor analysis, which is all we need here.)

If your dataset looks like a cigar, factor analysis will fit well. If not, it will fit poorly. Here's an example of the kind of data factor analysis can't represent:

<!--
![cigar](/img/g/3dplot/noncigar.gif)
-->

{% include video.html where="/img/g/3dplot/noncigar-nolines" title="data that factor analysis doesn't fit" %}

## The meaning of cigars

Factor analysis tries to approximate your data with a cigar. Why should you care about this?

Let's back up. As we saw earlier, physical and mental tests are correlated. If you learn that Bob scored well on paragraph comprehension that raises your estimate for how Bob will do on coding speed.

But say your data was a cigar. Take Bob's position along the length of the cigar, and call it **g**. Say Bob's value for **g** is low. If that's all you know, and you had to guess Bob's coding speed, you'd give a low number.

Now, suppose that in addition to **g**, you learn that Bob did well on paragraph comprehension. How does this change your estimate of Bob's coding speed? Amazingly, *it doesn't*. The single number **g** contains all the shared information between the tests.

In a cigar distribution, once you know **g**, everything else is just random noise---one test no longer tells you anything about any other. (Mathematically, once you control for **g**, the partial correlations of the tests are zero.)

In a *non*-cigar distribution, this doesn't happen. There's no single number that will make all the tests uncorrelated. Some interesting structure would remain unexplained.

## Mental tests aren't not cigars

So, what does real data look like? Is it a cigar? Can we capture all the structure with a single number?

{% comment %}
We'll need to talk about the "shape" of data quantitatively. For any dataset, you can find a set of lines[^svd] that represent the shape. For example, here's the earlier cigar data:

[^svd]: I don't know how to give a non-technical explanation of how to find these lines, so here a technical one. You can compute them for any dataset by doing a [singular value decomposition](https://en.wikipedia.org/wiki/Singular_value_decomposition) of the covariance matrix of the data.
{% endcomment %}

Here I took the earlier cigar data, and manually drew three lines to capture the "shape" of the data:

{% include video.html where="/img/g/3dplot/cigar-lines" title="factor analysis with noise, with singular vectors" %}

The blue line corresponds to the main direction of variation, while the shorter red and green lines correspond to the random noise added to each point. You can see that the shorter lines are the same length. This happens because factor analysis models are rotationally symmetric.

In contrast, here's the earlier "non-cigar" data:

{% include video.html where="/img/g/3dplot/noncigar-lines" title="data that factor analysis doesn't fit, with singular vectors" %}

Here, the shorter green and red lines are different lengths, reflecting that there is no rotational symmetry.

{% comment %}
cut this?
{% endcomment %}

OK, I lied. I didn't draw the lines manually. There's a simple algorithm that can automatically compute these for any dataset. (By computing a [singular value decomposition](https://en.wikipedia.org/wiki/Singular_value_decomposition) of the covariance matrix, if those words mean anything to you.) The details don't particularly matter, just that we can automatically find lines that span a point cloud. This will be important when we move beyond three dimensions.

So now we have a plan: We will take a real dataset, compute these lines, and see how long they are. If we have one long line and a bunch of equal-length short lines, then the data is cigar-like, meaning that a single variable explains all the "interesting" latent structure. If we have a bunch of lines of random lengths, then the data isn't cigar-like, meaning that we can't summarize things with one number.

I'd like to show you the real data from the datasets above, but none of them seem to be publicly available. Still, we can approximate it by generating data from a multivariate Normal with the known covariance.

Here are the first three tests of Alderton et al.'s (Paragraph comprehension, work knowledge, and general science).

<!--

![chabris's data](/img/g/3dplot/chabris.mp4)

-->

{% include video.html where="/img/g/3dplot/alderton" %}

It's not a perfect cigar, but it's not exactly *not* a cigar either. Here are the relative lengths of the three directions in decreasing order:

```
1st direction (blue line):   0.890
2nd direction (red line):    0.362
3rd direction (green line):  0.279
```

What if we use all seven tests? We can't make pretty pictures in seven dimensions, but we can still do the math. With **N** tests, a factor analysis model always produces **1** "long" direction and **N-1** "short" directions. If we plot the length of the directions, it should look like this:

[![exact factor analysis lengths](/img/g/tables/factor analysis model_svds.svg)](/img/g/tables/factor analysis model_svds.pdf)

In contrast, here's how things would look if all the tests were completely uncorrelated.

[![independent model lengths](/img/g/tables/independent model_svds.svg)](/img/g/tables/independent model_svds.pdf)

What do the lengths on real data look like? Well, judge for yourself. (Again, click to open/close)


<details markdown="1" open="1">
<summary><b>Alderton et al.</b></summary>
[![Alderton mental factor analysis lengths](/img/g/tables/alderton1997_svds.svg)](/img/g/tables/alderton1997_svds.pdf)
</details>

<details markdown="1">
<summary><b>Deary</b></summary>
[![Deary mental fitness factor analysis lengths](/img/g/tables/chabris2007a_svds.svg)](/img/g/tables/chabris2007a_svds.pdf)
</details>

<details markdown="1">
<summary><b>Chabris</b></summary>
[![Chabris mental fitness factor analysis lengths](/img/g/tables/chabris2007b_svds.svg)](/img/g/tables/chabris2007b_svds.pdf)
</details>

<details markdown="1">
<summary><b>MacCann et al.</b></summary>
[![MacCann mental fitness factor analysis lengths](/img/g/tables/maccann2014_svds.svg)](/img/g/tables/maccann2014_svds.pdf)
</details>

{% comment %}

Physical tests look similar, or perhaps slightly worse:

<center>

<details markdown="1">
<summary><b>Baumgartner and Zuidema</b></summary>
[![baumgartner 1973 physical fitness factor analysis lengths](/img/g/tables/baumgartner1972_svds.svg)](/img/g/tables/baumgartner1972_svds.pdf)
</details>

<details markdown="1">
<summary><b>Marsh and Redmaye</b></summary>
[![Marsh and Redmaye 1994 physical fitness factor analysis lengths](/img/g/tables/marsh1994_svds.svg)](/img/g/tables/marsh1994_svds.pdf)
</details>

<details markdown="1">
<summary><b>Ibrahim et al.</b></summary>
[![Ibrahim et al. 2011 physical fitness factor analysis lengths](/img/g/tables/ibrahim2011_svds.svg)](/img/g/tables/ibrahim2011_svds.pdf)
</details>

</center>

{% endcomment %}

Do these look exactly like what factor analysis can produce? No. But it's a reasonable approximation.

## Directions of variation

Here's another way of visualizing things. For any dataset, we can take the principal direction of variation (the blue line) and look at its length along each of the tests. This says, essentially, how much each of the tests contributes to the main direction of variation. Here's what we get if we do that for Alderton et al.:

[![alderton 1997 g loadings](/img/g/tables/alderton1997_g.svg)](/img/g/tables/alderton1997_g.pdf)

Calculating **g** is similar to taking a simple average of the test scores, though the weights are *slightly* higher on some tasks than others.

If we calculate **g** like this for each person, we can then compute the *partial* correlations. These are the correlations once you control for **g**. Here's what that gives for Alderton et al.:

[![alderton 1997 correlations](/img/g/tables/alderton1997_partials.svg)](/img/g/tables/alderton1997_partials.pdf)

Mostly it's a sea of gray, indicating that the partial correlations are all quite small.

And here's the *g* loadings and partial correlations for the other studies:

<details markdown="1">
<summary><b>Deary</b></summary>

[![deary 2007 g loadings](/img/g/tables/chabris2007a_g.svg)](/img/g/tables/chabris2007a_g.pdf)

[![deary 2007 partial correlations](/img/g/tables/chabris2007a_partials.svg)](/img/g/tables/chabris2007a_partials.pdf)
</details>

<details markdown="1">
<summary><b>Chabris</b></summary>

[![chabris 2007 g loadings](/img/g/tables/chabris2007b_g.svg)](/img/g/tables/chabris2007b_g.pdf)

[![chabris 2007 partial correlations](/img/g/tables/chabris2007b_partials.svg)](/img/g/tables/chabris2007b_partials.pdf)
</details>

<details markdown="1">
<summary><b>MacCann et al.</b></summary>

[![maccann 2014 g loadings](/img/g/tables/maccann2014_g.svg)](/img/g/tables/maccann2014_g.pdf)

[![maccann 2014 partial correlations](/img/g/tables/maccann2014_partials.svg)](/img/g/tables/maccann2014_partials.pdf)
</details>

If factor analysis was a perfect fit, these would all be zero, which they aren't. But they are pretty small, meaning that in each case, the single number *g* captures most of the interesting correlations.

## What would **g** look like?

Factor analysis is a decent but not perfect model of mental tests. What does this tell us about how intelligence works? Well, suppose that factor analysis was a *perfect* model. Would that mean that we're all born with some single number **g** that determines how good we are at thinking?

No. A perfect fit would only mean that, across a population, a single number would *describe* how people do on tests (except for the "noise"). It does not mean that number *causes* test performance to be correlated.

This is a point that often comes up in "refutations" of the existence of *g*. People argue, essentially, that even though tests are correlated, they might be produced by many *independent causes*. I'd go further---we *know* there are many causes. While intelligence is strongly [heritable](/heritability), it's highly polygenic. [Dozens of genes](https://doi.org/10.1038/ng.3869) are already known to be linked to it, and more are likely to be discovered. How "broad" the effects of individual genes are is an active research topic. It's harder to quantify environmental influences, but there are surely many that matter there, too.

So, no, the above data doesn't imply that there's a magical number **g** hidden in our brains, just like it doesn't imply that there's single number in our bodies that says how good we are at running, balancing, or throwing stuff. But that doesn't change the fact that a single number provides a good *description* of how good we are at various mental tasks.

Suppose you're hiring someone for a job that requires a few different mental tasks. (Arithmetic, sequential memory, whatever.) If you knew someone's **g**, you could guess how well they'd do at each task. But it would only be a guess! To really know, you still need to test the skills individually. That's the key word: *Individually*. It's not that **g** tells you everything---it doesn't---it's just that once you know **g**, how good someone is at one task doesn't tell you anything about how good they'll be at another.

Again, that's assuming factor analysis were a perfect fit. Which it isn't. Though it's close.

## Takeaways

1. Skill at mental and physical tasks are positively correlated. More similar stuff is more correlated.
3. A factor analysis model tries to model data with a "cigar" shape. These models fit mental and physical tests reasonably well, but not perfectly.
5. Call the position along the "long axis" of the cigar **g**. A perfect fit wouldn't mean that **g** contains all the information about how good someone is at different tasks---only that it contains all *shared* information.

{% comment %}
Here's an analogy: What determines how quickly an air purifier can clean the air? Lots of things: The quality of the filters, the number of filters, the strength of the fan, etc. Yet, if you tell me the [clean-air delivery rate](https://en.wikipedia.org/wiki/Clean_air_delivery_rate), that's all I need to know to predict how it will work. There's lots of *causes*, but they can be summarized by a single number.

{% endcomment %}
