---
layout: post
title: Heritability puzzlers
image: /img/heritable/baby.jpg
tags:
  - science
  - math
  - effort
description: What heritability actually means
excerpt: ""
permalink: /heritable/
background_color: rgb(29,19,17)
category: science
comment:
  lemmy: https://old.lemmy.world/post/34097041
  substack: https://dynomight.substack.com/p/heritable
---

The heritability wars have been a-raging. Watching these, I couldn't help but notice that there's near-universal confusion about what "heritable" means. Partly, that's because it's a subtle concept. But it also seems relevant that almost all explanations of heritability are very, *very* confusing. For example, here's [Wikipedia's definition](https://en.wikipedia.org/wiki/Heritability#Definition):

> Any particular phenotype can be modeled as the sum of genetic and environmental effects:
>
> &nbsp;&nbsp; Phenotype (*P*) = Genotype (*G*) + Environment (*E*).
> 
> Likewise the phenotypic variance in the trait – Var (*P*) – is the sum of effects as follows:
> 
> &nbsp;&nbsp; Var(*P*) = Var(*G*) + Var(*E*) + 2 Cov(*G*,*E*).
>
> In a planned experiment Cov(*G*,*E*) can be controlled and held at 0. In this case, heritability, *H*², is defined as 
>
> &nbsp;&nbsp; *H*² = Var(*G*) / Var(*P*)
> 
> *H*² is the broad-sense heritability.

Do you find that helpful? I hope not, because it's a mishmash of undefined terminology, unnecessary equations, and borderline-false statements. If you're in the mood for a mini-polemic:

1. Phenotype (*P*) is never defined. This is a minor issue, since it just means "trait".
2. Genotype (*G*) is never defined. This is a *huge* issue, since it's very tricky and heritability makes no sense without it.
3. Environment (*E*) is never defined. This is worse than it seems, since in heritability, different people use "environment" and *E* to refer to different things.
4. When we write *P* = *G* + *E*, are we assuming some kind of linear interaction? The text implies not, but why? What does this equation mean? If this equation is always true, then why do people often add other stuff like *G* × *E* on the right?
5. The text states that *if* you do a planned experiment (how?) and make Cov(*G*, *E*) = 0, *then* heritability is Var(*G*) / Var(*P*). But in fact, heritability is *always* defined that way. You don't need a planned experiment and it's fine if Cov(*G*, *E*) ≠ 0.
6. And—wait a second—that definition doesn't refer to environmental effects at all. So what was the point of introducing them? What was the point of writing *P* = *G* + *E*? What are we doing?

Reading this almost does more harm than good. While the final definition is correct, it never even attempts to explain what *G* and *P* are, it gives an incorrect condition for when the definition applies, and instead mostly devotes itself to an unnecessary digression about environmental effects. The rest of the page doesn't get much better. Despite being 6700 words long, I think it would be *impossible* to understand heritability simply by reading it.

Meanwhile, some people argue that heritability is meaningless for human traits like intelligence or income or personality. They claim that those traits are the product of complex interactions between genes and the environment and it's impossible to disentangle the two. These arguments have always struck me as "suspiciously convenient". I figured that the people making them couldn't cope with the hard reality that genes are very important and have an enormous influence on what we are.

But I increasingly feel that the skeptics have a point. While I think it's a fact that most human traits are substantially heritable, it's also true the technical definition of heritability is *really* weird, and simply does not mean what most people think it means.

In this post, I will explain *exactly* what heritability is, while assuming no background. I will skip everything that can be skipped but—unlike most explanations—I will not skip things that can't be skipped. Then I'll go through a series of puzzles demonstrating just how strange heritability is.

## What is heritability?

How tall you are depends on your genes, but also on what you eat, what diseases you got as a child, and how much gravity there is on your home planet. And all those things interact. How do you take all that complexity and reduce it to a single number, like "80% heritable"?

The short answer is: Statistical brute force. The long answer is: Read the rest of this post.

It turns out that the hard part of heritability isn't heritability. Lurking in the background is a slippery concept known as a *genotypic value*. Discussions of heritability often skim past these. Quite possibly, just looking at the words "genotypic value", you are thinking about skimming ahead right now. Resist that urge! Genotypic values are the core concept, and without them you cannot possibly understand heritability.

For any trait, your genotypic value is the "typical" outcome if someone with your DNA were raised in many different random environments. In principle, if you wanted to know your genotypic height, you'd need to do this:

1. Create a million embryonic clones of yourself.
2. Implant them in the wombs of randomly chosen women around the world who were about to get pregnant on their own.
3. Convince them to raise those babies exactly like a baby of their own.
4. Wait 25 years, find all your clones and take their average height.

Since you can't / shouldn't do that, you'll never know your genotypic height. But that's how it's defined in principle—the average height someone with your DNA would grow to in a random environment. If you got lots of food and medical care as a child, your actual height is probably above your genotypic height. If you suffered from rickets, your actual height is probably lower than your genotypic height.

Comfortable with genotypic values? OK. Then (broad-sense) heritability is easy. It's the ratio

&nbsp;&nbsp; `heritability = var[genotype] / var[height].`

Here, `var` is the [variance](https://en.wikipedia.org/wiki/Variance), basically just how much things vary in the population. Among all adults worldwide, `var[height]` is around 50 cm². (Incidentally, did you know that variance was invented [for the purpose](http://digamoo.free.fr/fisher1919.pdf) of defining heritability?)

Meanwhile, `var[genotype]` is how much *genotypic* height varies in the population. That might seem hopeless to estimate, given that we don't know anyone's genotypic height. But it turns out that we can still estimate the *variance* using, e.g., pairs of adopted twins, and it's thought to be around 40 cm². If we use those numbers, the heritability of height would be

&nbsp;&nbsp; `heritability ≈ (40 cm²) / (50 cm²) ≈ 0.8.`

People often convert this to a percentage and say "height is 80% heritable". I'm not sure I like that, since it masks heritability's true nature as a ratio. But everyone does it, so I'll do it too. People who really want to be intimidating might also say, "genes explain 80% of the variance in height".

Of course, basically the same definition works for any trait, like weight or income or fondness for pseudonymous existential angst science blogs. But instead of replacing "height" with "trait", biologists have invented the ultra-fancy word "phenotype" and write

&nbsp;&nbsp; `heritability = var[genotype] / var[phenotype].`

The word "phenotype" suggests some magical concept that would take years of study to understand. But don't be intimidated. It just means the actual observed value of some trait(s). You can measure your phenotypic height with a tape measure.

## On meaning

Let me make two points before moving on.

First, this definition of heritability assumes nothing. We are not assuming that genes are independent of the environment or that "genotypic effects" combine linearly with "environmental effects". We are not assuming that genes are in [Hardy-Weinberg equilibrium](https://en.wikipedia.org/wiki/Hardy%E2%80%93Weinberg_principle), whatever that is. No. I didn't talk about that stuff because I don't need to. There are no hidden assumptions. The above definition always works.
   
Second, many normal English words have parallel technical meanings, such as ["field"](https://en.wikipedia.org/wiki/Field_(physics)), ["insulator"](https://en.wikipedia.org/wiki/Insulator_(electricity)), ["phase"](https://en.wikipedia.org/wiki/Phase), ["measure"](https://en.wikipedia.org/wiki/Measure_(mathematics)), ["tree"](https://en.wikipedia.org/wiki/Tree_(abstract_data_type)), or ["stack"](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)). Those are all nice, because they're evocative and it's almost always clear from context which meaning is intended. But sometimes, scientists redefine existing words to mean something technical that overlaps but also *contradicts* the normal meaning, as in ["salt"](https://en.wikipedia.org/wiki/Salt_(chemistry)), ["glass"](https://en.wikipedia.org/wiki/Glass), ["normal"](https://en.wikipedia.org/wiki/Normal_distribution),  ["berry"](https://dynomight.net/valid-invalid/#2), or ["nut"](https://dynomight.net/valid-invalid/#2). These all cause confusion, but "heritability" must be the most egregious case in all of science.

Before you ever heard the technical definition of heritability, you surely had some fuzzy concept in your mind. Personally, I thought of heritability as meaning how many "points" you get from genes versus the environment. If charisma was 60% heritable, I [pictured](https://dynomight.net/heritability/) each person has having 10 total "charisma points", 6 of which come from genes, and 4 from the environment:

```
  Genes       ★★★☆☆☆
  Environment ★☆☆☆
  Total       ★★★★☆☆☆☆☆☆
```

If you take nothing else from this post, please remember that **the technical definition of heritability does not work like that**.  You might hope that if we add some plausible assumptions, the above ratio-based definition would simplify into something nice and natural, that aligns with what "heritability" means in normal English. But that does not happen. If that's confusing, well, it's not my fault.
## Intermission

Not sure what's happening here, but it seems relevant.

[![](/img/heritable/madonna_and_child.jpg)](https://www.nga.gov/artworks/46107-madonna-and-child)

## Heritability puzzles

So "heritability" is just the ratio of genotypic and phenotypic variance. Is that so bad?

I think... maybe?

**How heritable is eye color?**

Close to 100%.

This seems obvious, but let's justify it using our definition that `heritability = var[genotype] / var[phenotype]`.

Well, people have the same eye color, no matter what environment they are raised in. That means that genotypic eye color and phenotypic eye color are the same thing. So they have the same variance, and the ratio is 1. Nothing tricky here.

**How heritable is speaking Turkish?**

Close to 0%.

Your native language is determined by your environment. If you grow up in a family that speaks Turkish, you speak Turkish. Genes don't matter.

Of course, there are lots of genes that are *correlated* with speaking Turkish, since Turks are not, genetically speaking, a random sample of the global population. But that doesn't matter, because if you put Turkish babies in Korean households, they speak Korean. Genotypic values are defined by what happens in a *random* environment, which breaks the correlation between speaking Turkish and having Turkish genes.

Since 1.1% of humans speak Turkish, the genotypic value for speaking Turkish is around 0.011 for everyone, no matter their DNA. Since that's basically constant, the genotypic variance is near zero, and heritability is near zero.

**How heritable is speaking English?**

Perhaps 30%. Probably somewhere between 10% and 50%. Definitely more than zero.

That's right. Turkish isn't heritable but English is. *Yes it is*. If you ask an LLM, it will tell you that the heritability of English is zero. But the LLM is wrong and I am right.

Why? Let me first acknowledge that Turkish is a *little* bit heritable. For one thing, some people have genes that make them non-verbal. And there's surely some genetic basis for being a crazy polyglot that learns many languages for fun. But speaking Turkish as a second language is [quite rare](https://en.wikipedia.org/wiki/List_of_languages_by_total_number_of_speakers), meaning that the genotypic value of speaking Turkish is *close* to 0.011 for *almost* everyone.

English is different. While only 1 in 20 people in the world speak English as a first language, 1 in 7 learn it as a second language. And who does that? Educated people.

<details markdown="1">
<summary>
Most people say educational attainment is around 40% heritable. My guess is that speaking English as a second language is similar. But since there's a minority of native speakers (where genes don't really matter), I'm dropping my estimate to 30%.
</summary>

Some [argue](https://theinfinitesimal.substack.com/p/no-intelligence-is-not-like-height) the heritability of educational attainment is much lower. I'd like to avoid debating the exact numbers, but note that these lower numbers are usually estimates of "narrow-sense" heritability rather than "broad-sense" heritability as we're talking about. So they *should* be lower. (I'll explain the difference later.) It's entirely possible that broad-sense heritability is lower than 40%, but everyone agrees it's much larger than zero. So the heritability of English is surely much larger than zero, too.

</details>

**Say there's an island where genes have no impact on height. How heritable is height among people on this island?**

0%.

There's nothing tricky here.

**Say there's an island where genes entirely determine height. How heritable is height?**

100%.

Again, nothing tricky.

**Say there's an island where neither genes nor the environment influence height and everyone is exactly 165 cm tall. How heritable is height?**

It's undefined.

In this case, everyone has exactly the same phenotypic and genotypic height, namely 165 cm. Since those are both constant, their variance is zero and heritability is zero divided by zero. That's meaningless.

**Say there's an island where some people have genes that predispose them to be taller than others. But the island is ruled by a cruel despot who denies food to children with taller genes, so that on average, everyone is 165 ± 5 cm tall. How heritable is height?**

0%.

On this island, everyone has a genotypic height of 165 cm. So genotypic variance is zero, but phenotypic variance is positive, due to the ± 5 cm random variation. So heritability is zero divided by some positive number.

**Say there's an island where some people have genes that predispose them to be tall and some have genes that predispose them to be short. But, the same genes that make you tall also make you semi-starve your children, so in practice everyone is exactly 165 cm tall. How heritable is height?**

∞%. Not 100%, mind you, infinitely heritable.

To see why, note that if babies with short/tall genes are adopted by parents with short/tall genes, there are four possible cases.

| Baby genes | Parent genes | Food            | Height           |
| ---------- | ------------ | --------------- | ---------------- |
| Short      | Short        | Lots            | 165 cm           |
| Short      | Tall         | Semi-starvation | Less than 165 cm |
| Tall       | Short        | Lots            | More than 165 cm |
| Tall       | Tall         | Semi-starvation | 165 cm           |

If a baby with short genes is adopted into random families, they will be shorter on average than if a baby with tall genes. So genotypic height varies. However, in reality, everyone is the same height, so *phenotypic* height is constant. So genotypic variance is positive while phenotypic variance is zero. Thus, heritability is some positive number divided by zero, i.e. infinity.

(Are you worried that humans are "diploid", with two genes (alleles) at each locus, one from each biological parent? Or that when there are multiple parents, they all tend to have thoughts on the merits of semi-starvation? If so, please pretend people on this island reproduce asexually. Or, if you like, pretend that there's strong assortative mating so that everyone either has all-short or all-tall genes and only breeds with similar people. Also, don't fight the hypothetical.)

**Say there are two islands. They all live the same way and have the same gene pool, except people on island A have some gene that makes them grow to be 150 ± 5 cm tall, while on island B they have a gene that makes them grow to be 160 ± 5 cm tall. How heritable is height?**

It's 0% for island A and 0% for island B, and 50% for the two islands together.

Why? Well on island A, everyone has the same genotypic height, namely 150 cm. Since that's constant, genotypic variance is zero. Meanwhile, phenotypic height varies a bit, so phenotypic variance is positive. Thus, heritability is zero.

For similar reasons, heritability is zero on island B.

But if you put the two islands together, half of people have a genotypic height of 150 cm and half have a genotypic height of 160 cm, so suddenly (via math) genotypic variance is 25 cm². There's some extra random variation so (via more math) phenotypic variance turns out to be 50 cm². So heritability is 25 / 50 = 50%.

<details markdown="1">
<summary>
(Math)
</summary>

If you combine the populations, then genotypic variance is 

```
Var[150 cm + 10 cm × Bernoulli(0.5)]
 = (10 cm)² × Var[Bernoulli(0.5)]
 = (10 cm)² × 0.25
 = 25 cm².
```

Meanwhile phenotypic variance is

```
Var[150 cm + 10 cm × Bernoulli(0.5) + 5 cm × Normal(0,1)]
 = (10 cm)² × Var[Bernoulli(0.5)] + (5 cm)² × Var[Normal(0,1)]
 = (10 cm)² × 0.25 + (5 cm)² × 1
 = 50 cm².
```

</details>

**Say there's an island where neither genes nor the environment influence height. Except, some people have a gene that makes them inject their babies with human growth hormone, which makes them 5 cm taller. How heritable is height?**

0%.

True, people with that gene will tend be taller. And the gene is *causing* them to be taller. But if babies are adopted into random families, it's the genes of the *parents* that determine if they get injected or not. So everyone has the same genotypic height, genotypic variance is zero, and heritability is zero.

**Suppose there's an island where neither genes nor the environment influence height. Except, some people have a gene that makes them, as babies, talk their parents into injecting them with human growth hormone. The babies are very persuasive. How heritable is height?**

We're back to 100%.

The difference with the previous scenario is that now babies with that gene get injected with human growth hormone no matter who their parents are. Since nothing else influences height, genotype and phenotype are the same, have the same variance, and heritability is 100%.

**Suppose there's an island where neither genes nor the environment influence height. Except, there are crabs that seek out blue-eyed babies and inject them with human growth hormone. The crabs, they are unstoppable. How heritable is height?**

Again, 100%.

Babies with DNA for blue eyes get injected. Babies without DNA for blue eyes don't. Since nothing else influences height, genotype and phenotype are the same and heritability is 100%.

Note that if the crabs were seeking out *parents* with blue eyes and then injecting their babies, then height would be 0% heritable.

It doesn't matter that human growth hormone is weird thing that's coming from outside the baby. It doesn't matter if we think crabs should be semantically classified as part of "the environment". It doesn't matter that heritability would drop to zero if you killed all the crabs, or that the direct causal effect of the relevant genes has nothing to do with height. Heritability is a ratio and doesn't care.

## What good is heritability?

So heritability can be high even when genes have no direct causal effect on the trait in question. It can be low even when there is a strong direct effect. It changes when the environment changes. It even changes based on how you group people together. It can be larger than 100% or even undefined.

Even so, I'm worried people might interpret this post as a long way of saying *heritability is dumb and bad, trolololol*. So I thought I'd mention that this is not my view.

Say a bunch of companies create different LLMs and train them on different datasets. Some of the resulting LLMs are better at writing fiction than others. Now I ask you, "What percentage of the difference in fiction writing performance is due to the base model code, rather than the datasets or the GPUs or the learning rate schedules?"

That's a natural question. But if you put it to an AI expert, I bet you'll get a funny look. You need code *and* data *and* GPUs to make an LLM. None of those things can write fiction by themselves. Experts would prefer to think about one change at a time: Given *this* model, changing the dataset in *this* way changes fiction writing performance *this* much.

Similarly, for humans, I think what we really care about is interventions. If we changed this gene, could we eliminate a disease? If we educate children differently, can we make them healthier and happier? No single number can possibly contain all that information.

But heritability is *something*. I think of it as saying how much hope we have to find an intervention by looking at changes in *current* genes or *current* environments.

1. If heritability is high, then given **current typical genes**, you can't influence the trait much through **current typical environmental changes**. If you only knew that eye color was 100% heritable, that means you won't change your kid's eye color by reading to them, or putting them on a vegetarian diet, or moving to higher altitude. But it's conceivable you could do it by putting electromagnets under their bed or forcing them to communicate in interpretive dance.

2. If heritability is high, that also means that given **current typical environments** you *can* influence the trait through **current typical genes**. If the world was ruled by an evil despot who forced red-haired people to take pancreatic cancer pills, then pancreatic cancer would be highly heritable. And you could change the odds someone gets pancreatic cancer by swapping in existing genes for black hair.

3. If heritability is low, that means that given **current typical environments**, you can't cause much difference through **current typical genetic changes**. If we only knew that speaking Turkish was ~0% heritable, that means that doing embryo selection won't much change the odds that your kid speaks Turkish.

4. If heritability is low, that also means that given **current typical genes**, you *might* be able change the trait through **current typical environmental changes**. If we only know that speaking Turkish was 0% heritable, then that means there might be something you could do to change the odds your kid speaks Turkish, e.g. moving to Turkey. Or, it's conceivable that it's just random and moving to Turkey wouldn't do anything.

| Heritability | Influenced by typical genes? | Influenced by typical environments? |
|-|-|-|
| High | Yes | No | 
|-|-|-|
| Low | No | Maybe | 

But be careful. Just because heritability is high doesn't mean that changing genes is easy. And just because heritability is low doesn't mean that changing the environment is easy.

And heritability doesn't say anything about *non-typical* environments or *non-typical* genes.

If an evil despot is giving all the red-haired people cancer pills, perhaps we could solve that by intervening on the despot. And if you want your kid to speak Turkish, it's possible that there's some crazy genetic modifications that would turn them into unstoppable Turkish learning machine.

Heritability has no idea about any of that, because it's just an observational statistic based on the world as it exists today.

### Recommended reading

* [Heritability: Five Battles](https://www.lesswrong.com/posts/xXtDCeYLBR88QWebJ/heritability-five-battles) by Steven Byrnes. Covers similar issues in way that's more connected to the world and less shy about making empirical claims.

* [A molecular genetics perspective on the heritability of human behavior and group differences](http://gusevlab.org/projects/hsq/) by Alexander Gusev. I find the quantitative genetics literature to be incredibly sloppy about notation and definitions and math. (Is this why LLMs are so bad at it?) This is the only source I've found that didn't drive me completely insane.

### Appendix

<details markdown="1">
<summary>
The other heritability
</summary>

## Appendix: Narrow heritability

This post focused on "broad-sense" heritability.  But there a second heritability out there, called "narrow-sense". Like broad-sense heritability, we can define the narrow-sense heritability of height as a ratio:

&nbsp;&nbsp; `narrow heritability = var[additive height] / var[phenotype]`

The difference is that rather than having height in the numerator, we now have "additive height". To define that, imagine doing the following for each of your genes, one at a time:

1. Find a million random women in the world who just became pregnant.
2. For each of them, take your gene and insert it into the embryo, replacing whatever was already at that gene's locus.
3. Convince everyone to raise those babies exactly like a baby of their own.
4. Wait 25 years, find all the resulting people, and take the difference of *their* average height from *overall* average height.

For example, say overall average human height is 150 cm, but when you insert gene #4023 from yourself into random embryos, their average height is 149.8 cm. Then the additive effect of your gene #4023 is -0.2 cm.

Your "additive height" is average human height plus the sum of additive effects for each of your genes. If the average human height is 150 cm, you have one gene with a -0.2 cm additive effect, another gene with a +0.3 cm additive effect and the rest of your genes have no additive effect, then your "additive height" is 150 cm - 0.2 cm + 0.3 cm = 150.1 cm.

Note: This terminology of "additive height" is non-standard. People usually define narrow-sense heritability using "additive *effects*", which are the same thing but without including the mean. This doesn't change anything since adding a constant doesn't change the variance. But it's easier to say "your additive height is 150.1 cm" rather than "the additive effect of your genes on height is +0.1 cm" so I'll do that.

Honestly, I don't think the distinction between "broad-sense" and "narrow-sense" heritability is *that* important. We've already seen that broad-sense heritability is weird, and narrow-sense heritability is similar but different. So it won't surprise you to learn that narrow-sense heritability is *differently*-weird.

## Appendix: Narrow heritability puzzles

But if you really want to understand the difference, I can offer you some more puzzles.

**Say there's an island where people have two genes, each of which is equally likely to be A or B. People are 100 cm tall if they have an AA genotype, 150 cm tall if they have an AB or BA genotype, and 200 cm tall if they have a BB genotype. How heritable is height?**

Both broad and narrow-sense heritability are 100%.

The explanation for broad-sense heritability is like many we've seen already. Genes entirely determine someone's height, and so genotypic and phenotypic height are the same.

For narrow-sense heritability, we need to calculate some additive heights. The overall mean is 150 cm, each A gene has an additive effect of -25 cm, and each B gene has an additive effect of +25 cm. But wait! Let's work out the additive height for all four cases:

| genotype | phenotypic height | additive height                 |
| -------- | ----------------- | ------------------------------- |
| AA       | 100 cm            | 150 cm - 25 cm - 25 cm = 100 cm |
| AB       | 150 cm            | 150 cm - 25 cm + 25 cm = 150 cm |
| BA       | 150 cm            | 150 cm + 25 cm - 25 cm = 150 cm |
| BB       | 200 cm            | 150 cm + 25 cm + 25 cm = 200 cm |

Since additive height is also the same as phenotypic height, narrow-sense heritability is also 100%.

In this case, the two heritabilities were the same. At a high level, that's because the genes act independently. When there are "gene-gene" interactions, you tend to get different numbers.

**Say there's an island where people have two genes, each of which is equally likely to be A or B. People with AA or BB genomes are 100 cm, while people with AB or BA genomes are 200 cm. How heritable is height?**

Broad-sense heritability is 100%, while narrow-sense heritability is 0%.

You know the story for broad-sense heritability by now. For narrow-sense heritability, we need to do a little math.

1. The overall mean height is 150 cm.
2. If you take a random embryo and replace one gene with A, then the there's a 50% chance the other gene is A, so they're 100 cm, and there's a 50% chance the other gene is B, so they're 200 cm, for an average of 150 cm. Since that's the same as the overall mean, the additive effect of an A gene is +0 cm.
3. By similar logic, the additive effect of a B gene is also +0 cm.

So everyone has an additive height of 150 cm, no matter their genes. That's constant, so narrow-sense heritability is zero.

## Appendix: Why are there two heritabilities?

I think basically for two reasons:

First, for some types of data (twin studies) it's much easier to estimate broad-sense heritability. For other types of data (GWAS) it's much easier to estimate narrow-sense heritability. So we take what we can get.

Second, they're useful for different things. Broad-sense heritability is defined by looking at what all your genes do together. That's nice, since you are the product of all your genes working together. But combinations of genes are not well-preserved by reproduction. If you have a kid, then they breed with someone, their kids breed with other people, and so on. Generations later, any special combination of genes you might have is gone. So if you're interested in the long-term impact of you having another kid, narrow-sense heritability might be the way to go.

(Sexual reproduction doesn't really allow for preserving the genetics that make you uniquely "you". Remember, almost all your genes are shared by lots of other people. If you have any unique genes, that's almost certainly because they have deleterious de-novo mutations. From the perspective of evolution, your life just amounts to a tiny increase or decrease in the per-locus population frequencies of your individual genes. The participants in the game of evolution are genes. Living creatures like you are part of the playing field. Food for thought.)

</details>