---
layout: post
title: "What is heritability, really? Just a ratio."
image: /img/heritability/birds.jpg
tags: statistics personality
hero_light: false
dark_title: false
background_color: black
description: "What heritability really is: A fluid statistic that changes whenever society changes."
permalink: /heritability/
background_color: rgb(60,64,50)
head: "<style>
details{
    }
details summary{
  padding-bottom: 12pt;
}
img{
    display:block;
    margin-left: auto;
    margin-right: auto;
}
table tr{
    border-style: hidden;
    text-align:center;
}
@media (min-width:501px){
table{
  max-width:100;
  max-width:100%;
  font-size: 90%;
}
}
@media (max-width:500px) and (min-width:301px) {
table{
  max-width:100;
  max-width:100%;
  font-size: 3.2vw;
}
}
@media (max-width:300px) {
table{
  max-width:100;
  max-width:100%;
  font-size: 0.5em;
}
.fixed{
    max-width:100;
    max-width:100%;
    overflow:scroll;
}
}
</style>"
---

All psychological traits are heritable. This is the [best replicated](https://dx.doi.org/10.1177%2F1745691615617439) finding in all of behavioral genetics. Some recent numbers include:

* Religiosity: [44%](https://doi.org/10.1111%2Fj.1467-6494.2005.00316.x)
* Schizophrenia: [79%](https://doi.org/10.1016/j.biopsych.2017.08.017)
* [Big five](/better-personalities/) personality traits: [~40%](https://doi.org/10.1111/j.1467-6494.2005.00316.x)

But what, exactly, does "heritability" mean?

I used to have a mental model something like this: Each person has some number of "religiosity points" that come from genes and some number that come from the environment. If religiosity was 40% genetic, I pictured there being 10 total points, 4 of which come from genes and 6 of which come from the environment:

<div style="font-size:min(4vw,12pt); font-family:monospace; text-align:center;" markdown="1">

&nbsp;Genes&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;★★★☆&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\\
&nbsp;Environment&nbsp;★★☆☆☆☆&nbsp;&nbsp;&nbsp;&nbsp;\\
&nbsp;Total&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;★★★★★☆☆☆☆☆  

<br>
</div>

The problem with this picture—aside from being completely wrong—is that it suggests heritability is an immutable constant, like the number of chromosomes in a cell or the [fine structure constant](https://en.wikipedia.org/wiki/Fine-structure_constant). It isn't.

So what *is* heritability? It's the ratio of the *genetic variance* of a trait with the *total variance*, including all causes. Since the environment is always changing, so is heritability.

Let's explore this definition. We'll see that it leads to several puzzles:
* Why is heritability often higher for traits that seem less important? Why, for example, is pig back-fat thickness 14× more heritable than pig litter size?
* How, even when there are large environmental effects, can a trait still be 100% heritable?
* How, when there are correlations between genes and the environment, can traits can be *more than* 100% heritable?

The only math we'll use is the concept of [variance](https://en.wikipedia.org/wiki/Variance). If you're not familiar with that, just think of it as "how variable" something is. Humans have high variance in how much we like folk music, but low variance in our number of fingers.

One note on terminology: Biologists use "phenotype" to refer to what actually happens, including all genetic or environmental causes. The phenotypic length of your foot is, thrillingly, the actual length of your foot.

<div style="font-size:80%;" markdown="1">

* auto-gen TOC:
{:toc}

</div>

## Simplest example

Say that people's height depends on only one gene, which can be either **short** or **tall**. The genetic contribution to height is 2m if they get the short gene, and 4m if they get the tall gene. (The math is easier if we make everyone giants.)

| **genes** | Genetic value |
| --------- | ------------- |
| short     | 2             |
| tall      | 4             |

The only thing that matters in the environment is food. At birth, people are assigned either to **diet** or to **feast**. If on a diet, they lose 1m of height compared to their genetic baseline. If on a feast, they gain 1m of height.

| **env** | Environmental value |
| ------- | ------------------- |
| diet    | -1                  |
| feast   | +1                  |

A person's height is the sum of their genetic and environmental values. Using **P** for phenotypic, write the final height as

<div style="text-align:center; padding-bottom:10pt;" markdown="1">

​	**P(genes,env) = G(genes) + E(env).**

</div>

With all these assumptions, can we calculate heritability? Not yet! We need the **population distribution**, i.e., what fraction of people have each combination of genes and environments. Assume for now that half of people have each gene, and half of people have each environment, and that these are independent.

| population distribution | diet | feast |
| ----------------------- | ---- | ----- |
| **short**               | ¼  | ¼   |
| **tall**                | ¼  | ¼   |

## The definition of heritability

Given any trait with P=G+E, the (broad-sense) heritability is

<div style="text-align:center; padding-bottom:10pt;" markdown="1">

**H<sup>2</sup> = var(G) / var(P).**

</div>


Heritability is how much the *genetic* contribution to the trait varies as compared to how much that trait varies *overall*. These variances are computed with respect to random people from the population.  

In the above example, the variance of E is one, since it is -1 half the time, and +1 the other half. Similarly, G is always one off from its mean of three, so the variance of G is also one. Since the genes and the environment are independent, the [variance of their sum](https://en.wikipedia.org/wiki/Variance#Sum_of_uncorrelated_variables_(Bienaym%C3%A9_formula)) is **var(P)=var(G)+var(E)**. This tells us that

<div style="text-align:center; padding-bottom:10pt;" markdown="1">

​	**H<sup>2</sup> =  ½**.

</div>

This is natural, since the effects of genes and environments are symmetric—changing either one changes height by 2m.

## Let them eat more (or possibly less)

Let's change how much food people get. Suppose that there's some parameter **b** that reflects how much more food the feast group gets than the diet group.

| **env** | Environmental value |
| ------- | ------------------- |
| diet    | **-b**              |
| feast   | **+b**              |

As **b** changes, the environmental variance changes. If you feed the two groups almost equally (**b** is near zero) then the variance is near zero. As the difference between groups increases, variance increases.

[![scenario 2 variances](/img/heritability/scenario-2-var.svg)](/img/heritability/scenario-2-var.pdf)

Here's what the corresponding heritability looks like:

[![scenario 2 heritability](/img/heritability/scenario-2-H.svg)](/img/heritability/scenario-2-H.pdf)

If the two groups are fed equally, then height is 100% heritable. If the feast group is fed much more (**b=2**), then height is only 20% heritable.

**Takeaway**: Heritability depends on how variable the environment is. If the environment becomes more variable, heritability decreases. If the environment becomes more consistent, heritability increases.

#### Example: Changing the heritability of IQ

Research suggests that childhood lead exposure can decrease IQ by [5-10 points](https://doi.org/10.1289%2Fehp.7688) and heavy prenatal [alcohol](https://dynomight.net/alcohol) exposure can decrease IQ by [15-20 points](https://doi.org/10.1016/S0022-3476(97)70099-4). Current estimates are that intelligence is [40-80%](https://dx.doi.org/10.1038%2Fmp.2014.105) heritable. But suppose society managed to eliminate lead and alcohol exposure. Environmental variance would decrease, and heritability would go up.

In theory, it's possible to push the heritability of *all* traits to 100%. Just make sure each person is exposed to *completely identical environments*. (You can argue that free will or quantum mechanics or the butterfly effect means there is no such thing as two identical environments, but let's not get distracted.)

One could decrease the heritability by doing the opposite: Take half of kids and make it illegal to teach them to read or whatever. Then, take the other half of kids and give them private tutors. Environmental variance would increase, and heritability would go down.


## The purge

Now let's delete a bunch of people. After the purge, instead of half being short and half tall, some fraction **a** are short, and a fraction **(1-a)** are tall. If short people are more likely than tall people to survive the purge, then **a > ½**. If they are less likely, then **a < ½**.

Leave the food difference fixed at **b=1**. The environment doesn't change, so the variance of E remains one.

The genetic variance does change. If almost everyone has short genes (**a** is near zero), then almost everyone will have G=2, meaning the variance of G will be small. If **a** is ½, we get the previous model. A bit of math gives the following plot.

[![scenario 1 variances](/img/heritability/scenario-1-var.svg)](/img/heritability/scenario-1-var.pdf)

The heritability is still **H<sup>2</sup> = var(G) / (var(G)+var(E))**, which now looks like this:

[![scenario 1 heritability](/img/heritability/scenario-1-H.svg)](/img/heritability/scenario-1-H.pdf)

Heritability decreases hugely if the population gets really imbalanced in either direction.

**Takeaway**: Heritability depends on how much genetic diversity there is.

#### Example: Hair in Japan

How heritable is hair color in Japan, before anyone goes grey? Say 99% of people have genes for black hair, so **var(G)** is very low. Yet, lots of people have (artificially) non-black hair, so **var(P)** will be reasonably high. Assume that the choice to dye your hair isn't genetically determined. Then, hair color in Japan has low heritability. (Lower, for example, than the US, which has more genetic diversity in hair color.) At the same time, we know that genes pretty much 100% determine what color hair grows on your head. Heritability is not a measure of how deterministic genes are in their effects.

#### Example: Heritability in different species

Here are some numbers, courtesy of Falconer's *Introduction to Quantitative Genetics*.

| Animal             | Trait                         | Heritability (%) |
| ------------------ | ----------------------------- | ---------------- |
| **Human**          | Height                        | 65               |
|                    | Immunoglobulin                | 45               |
| **Cow**            | Adult weight                  | 65               |
|                    | Butterfat %                   | 40               |
|                    | Milk yield                    | 35               |
| **Pig**            | Back-fat thickness            | 70               |
|                    | Efficiency of food conversion | 50               |
|                    | Litter size                   | 5                |
| **Chicken**        | Weight                        | 55               |
|                    | Egg production                | 10               |
| **Mouse**          | Tail length                   | 40               |
|                    | Weight                        | 35               |
|                    | Litter size                   | 20               |
| **Fruit Fly**      | Bristle number                | 50               |
|                    | Body size                     | 40               |
|                    | Ovary size                    | 30               |
|                    | Egg production                | 20               |

Notice anything? The closer something is to reproduction, the lower heritability is. This seems odd at first. Isn't the number of eggs a fly produces incredibly important? Yes, but that's precisely the point! *Because* it is so important, evolution can select strongly for the genes with the optimal egg production numbers, leaving little genetic variance, and driving heritability down.

So low heritability doesn't necessarily mean that genes don't *matter* -- it simply means that in the current population, most people have genes that do similar stuff, as compared with environmental causes.

(Technically, the numbers in the above table are estimates of *narrow*-sense heritability rather than *broad*-sense heritability as we are discussing. It doesn't matter since we're only looking at the general trend.)


## Selective feeding

So far, genes and the environment have been independent. No one looked at your genes when deciding if you get a diet or feast environment. Let's change that. (We assume genes and the environment have the same effects as in the simplest model, i.e. **b = 1** and **a = ½**.)

While half of people are short/tall, and half get a diet/feast environment, change the odds that feasts go to the people with short vs. tall genes. Specifically, take this distribution:

| population distribution | diet  | feast |
| ----------------------- | ----- | ----- |
| **short**               | ¼ - c | ¼ + c |
| **tall**                | ¼ + c | ¼ - c |

Here, **c** is any number between -¼ and +¼. If **c = -¼**, then people with short genes *always* get a diet, and people with tall genes always get a feast. If **c = +¼**, it's the opposite.

Now, there's something odd about this scenario. The genetic and environmental variances are always one. That's because, no matter the value of **c**, the distribution over genes and environments are always uniform. (You can check that the row and column sums in the above table are always 0.5.)

However, the *phenotypic* variance does change with **c**. Suppose that **c = ¼**. People with short genes always get a feast, and thus have a height of 3. People with tall genes always get a diet, and so *also* have a height of 3. Everyone has the same height, so the phenotypic variance is zero!

Or suppose that **c = -¼**. People with short genes always get a diet, and so have a height of 1. People with tall genes always get a feast, and so have a height of 5. There is lots of phenotypic variance.

[![scenario 3 variances](/img/heritability/scenario-3-var.svg)](/img/heritability/scenario-3-var.pdf)

(Mathematically, what's happening here is that G and E are no-longer independent, so the variance of P is not just the sum of the variances of G and E but must be adjusted to include their (now-nonzero) covariance.)

The heritability, as ever, is **H<sup>2</sup>=var(G)/var(P)**. If we plot this it looks like the following:

[![scenario 3 heritability](/img/heritability/scenario-3-H.svg)](/img/heritability/scenario-3-H.pdf)

In the "starve the short" regime (negative **c**) heritability decreases. In the "feed the short" regime (positive **c**) it increases.

Speaking of which, on the right of the plot, heritability goes above one! This is not a mistake. Remember, heritability is the ratio of genetic variance and phenotypic variance. *Usually*, the environment creates more variance, so this ratio is less than one. However, if people with short genes get more food than people with tall genes, then environment *decreases* variance. (Technically, if **c=¼**, then the phenotypic variance is zero, meaning the heritability is *infinite*!)

**Takeaway:** When the environment depends on genes, things get weird. If the environment *exacerbates* genetic differences, that *decreases* heritability. If the environment *reduces* genetic differences, then that *increases* heritability.

#### Example: Education and intelligence

It's plausible that education exacerbates genetic differences in intelligence. In most places today, I'd bet that genetic intelligence is positively correlated with the quality and quantity of education someone gets. (Partly because [intelligence is correlated with income](https://doi.org/10.1016/j.intell.2007.02.003) and partly because it helps to qualify for scholarships and selective schools/classes.) It also appears that [education increases intelligence](https://en.wikipedia.org/wiki/Intelligence_and_education).

Now, imagine that society is reformed to remove correlations between genetic intelligence and education. (Maybe all students are assigned to public schools at random.) This would be like moving to the right on the above graph. Thus, strangely, more equal access to education would cause heritability to go *up*. If we went further and provided *better* education to less gifted students, that would increase things even further.

It doesn't matter if more equal education is a good idea, or even if we truly are in a "starve the short" regime now. The point is that *heritability depends on society*.

## Three key takeaways

1. Less random environments lead to higher heritability. If everyone had completely equal environments, every trait would be 100% heritable.

2. Heritability depends on the amount of genetic variance in the population. If people have similar genes, heritability goes down. You don't need anything dramatic like new mutations.

3. If genetics are correlated with the environment, weird things can happen. If environmental correlations decrease variance, then total variance might be lower then genetic variance. If so, heritability is greater than 100%!

Heritability is really just a ratio of variances. You'll mislead yourself thinking about it any other way.

