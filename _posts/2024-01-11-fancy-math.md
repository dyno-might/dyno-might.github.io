---
layout: post
title: "Fancy math doesn't make simple math stop being true"
image: /img/fancy-math/davinci.jpg
tags: 
description: "on butts and instrumental variables"
excerpt: 
permalink: /fancy-math/
background_color: rgb(179,167,151)
category: "science"
comment:
#    substack: https://dynomight.substack.com/p/fancy-math
---

![](/img/fancy-math/venn.svg)

What are you supposed to do when someone disagrees with you using a bunch of math you can't understand?

I've been thinking about that recently because of the [NordICC colonoscopy trial](https://doi.org/10.1056/nejmoa2208375). It took 85k Europeans aged 55-64, invited a third of them for a free one-time screening colonoscopy, and then waited 10 years to see who got colorectal cancer. That turned out to be 0.918% for those who were invited and 1.104% for those who weren't, for a difference of 0.186%.

This caused a lot of squabbling. Some people say NordICC shows colonoscopies are great, some people say it shows they're bad.

The biggest cause of squabbling was that of the third of people who were invited, only 42% accepted and did colonoscopies. But for statistical reasons, *all* the invited people are included in the calculations. If you want to know how good colonoscopies are, probably you'd like to know what would have happened if everyone had agreed. Surely the decrease in colorectal cancer would have been larger than 0.186%. But *how much* larger?

[Originally](https://asteriskmag.com/issues/04/you-re-invited-to-a-colonoscopy), my simple-minded logic was that the overall decrease is a weighted average of the decreases for 42% of people who are acceptors and the 58% of people who are refusers, i.e.,

<div class="eq" markdown="1">
&nbsp;&nbsp;&nbsp;&nbsp;(0.186% overall decrease)  
&nbsp;&nbsp;&nbsp;&nbsp;= 0.42 × (decrease for acceptors)  
&nbsp;&nbsp;&nbsp;&nbsp;+ 0.58 × (decrease for refusers).
</div>

Technically, both the decreases on the right are unknown, but it's reasonable to assume the "decrease" for refusers is zero, since they didn't do colonoscopies. If that's true, then

<div class="eq" markdown="1">
&nbsp;&nbsp;&nbsp;&nbsp;(decrease for acceptors) = 0.186% / 0.42 = 0.443%.
</div>

(There *could* be a decrease for refusers—maybe getting an invitation is scary, and so if your butt starts acting weird a few years later you go to the doctor faster. But probably not?)

I claimed this 0.443% number was **biased**, because acceptors are different from the general population. This sampling bias is not some abstract possibility. We *know* it matters, because at the end of the trial, *refusers* had less colorectal cancer then *controls*, even though neither did colonoscopies.

Presumably that happens because people have some idea of their cancer risk and are more likely to agree to a colonoscopy when that risk is higher. So if refusers were at lower risk than controls, that means *acceptors* must have been at *higher* risk. If you give colonoscopies to *random* 55-64 year-old Europeans, the decrease in colorectal cancer would be less than 0.443%.

Or so I thought.

<br>

After that article came out, I was contacted by a few economists. They said something like this:

> That calculation is what we call an *instrumental variables* method. Because of fancy math reasons, instrumental variables methods are unbiased. So 0.443% is **unbiased**. Yay!

This confused me. I'd previously seen a [post](https://www.sensible-med.com/p/using-instrumental-variable-iv-methods) making this argument, but I didn't see the point. After all, It's the same calculation, and I trusted my argument for bias.

Then in December 2023 a [paper](https://doi.org/10.1073/pnas.2311556120) came out in the Proceedings of the National Academy of Sciences making the instrumental variables argument again, except with even more math and even more insistence that selection bias has been solved. This *really* confused me.

I mean, was my argument for bias *wrong*? I asked everyone who contacted me what my error was, but I could never get a clear answer—the response was always to return to instrumental variables and how awesome they are. I heard lots about *potential outcomes* and *monotonicity* and *local treatment effects* and *two-stage least squares*, but never anything about where my poor little logic went wrong.

I'm sure instrumental variables are great! (Did I mention that one of the authors of that paper won a Nobel prize for inventing instrumental variables?) But in this *particular* case, they produce the same number as my [grug](/grug/)-brained logic, via the *same calculation*.

So is 0.443% biased, or isn't it? Does the instrumental variable reframing add anything?

Who's right, the impeccably-credentialed experts with papers in prestigious journals, or me, overconfident internet autodidact?

Me.

(Technically everyone, but mostly me.)

<br>

Say you've got a big pile of bricks, and you ask your friends [Alice and Bob](https://en.wikipedia.org/wiki/Alice_and_Bob) how much it weighs.

**Alice:** I counted 500-ish bricks. I weighed one and it was 2 kg. So your pile is around 1000 kg.

**Bob**: Oh, ho, ho, no! Bricks are a mixture of silica, alumina, lime, iron oxide, and magnesia. From the color of your pile, I infer a density of around 1900 kg/m³. The pile is 0.5 m tall and 4 m wide and has roughly the shape of a cone, so the volume is around ⅓ π (2 m)² (0.5 m) ≈ 2.09 m³. Assuming  half the interior volume is air, the total weight is 2.09 m³ × 0.5 × 1900 kg/m³ ≈ 1,985.5 kg. How lucky for you, Alice, to have this chance to learn from me!

I think Bob is bad.

That's not because his logic is too fancy or his brain is too big. Often we need big brains and fancy arguments.

My objection is that Bob doesn't identify the *flaw* in Alice's argument, and instead gives a (more complicated) *parallel argument*.

Why does Bob have that burden and not Alice? Well, *one* of them has to be wrong. Alice's argument is simple, so if she made a mistake, it should be easy for Bob to find. But Bob's argument involves lots of background Alice might not have, and has more steps, so if it's wrong, there are more places to "hide the bodies".

So that's the first claim I want to make: If two people disagree, it should be the responsibility Dr. Fancy to explain what's wrong with Dr. Simple, not the reverse.

This seems like a pretty obvious idea, enough that there ought to be some Latin phrase to throw around. But as far as I can tell, there isn't. So how about "*onus probandi incumbit Bob*"?

<br>

The other point I wanted to make is that simple math doesn't, like, disappear when a fancy alternative is presented. Maybe it's human nature to favor fancy arguments over simple ones, with some instinctual logic like:

1. Bob displays more domain knowledge than Alice.
2. So Bob is more of an expert than Alice.
3. So Bob is more likely to be right.

In a Bayesian sense, that logic might be right!

Certainly, if you *just* knew that (1) some elite economists say 0.443% is unbiased and (2) some internet rando disagrees, then you *should* have a prior favoring the economists. So if you don't want to examine the actual arguments, maybe it's reasonable to favor fancy ones. 

But if you *do* read the arguments, and the simple one is convincing, then that's strong evidence for it. And it's *still* strong evidence, *even if you can't understand the fancy argument*.

<br>

So what's going on with the instrumental variables? Now, I'm no expert and I just wrote 1200 words arguing I shouldn't have to explain them. But hahaha this is a blog and I just couldn't help myself. So I spent a couple hours reading the [recent paper](https://doi.org/10.1073/pnas.2311556120) and I *think* I understand what's happening.

(If you're terrified of math, you can skip the next three paragraphs.)

For each person, imagine two branches of the multiverse where they either get a colonoscopy or they don't. Let Yᶜ indicate if the person gets colorectal cancer in the "colonoscopy" branch of the multiverse (Yᶜ=1 if cancer, and Yᶜ=0 if no cancer.) Similarly, let Yⁿ indicate if they get colorectal cancer in the "no colonoscopy" branch. Finally, let C indicate if they *accepted an invitation* to do a colonoscopy. 

Now, define the Local Average Treatment Effect to be LATE = 𝔼[C × (Yᶜ - Yⁿ)] / 𝔼[C], where the expectations are over all the different people in the invited group. With some technical assumptions, you can show that the numerator becomes the total difference in colorectal cancer rates between the invited and control groups (0.186%) while the denominator is the fraction of people who agree to screening (0.42). So LATE = 0.186% / 0.42 = -0.443%.

And you can also show, under the same assumptions, that LATE = 𝔼[Yᶜ \| C=1] - 𝔼[Y ⁿ\| C=1]. So 0.443% is how much a colonoscopy reduces your odds of getting colorectal cancer, supposing you are the kind of person who would have agreed to participate in the NordICC trial.

(That's the end of the math, sorry about that.)

So, technically, everyone is right:

 1. If you want to know how much a colonoscopy will help a random 55-64 year-old European, then 0.443% is "biased".
2. If you want to know how much a colonoscopy will help the high-risk subset of 55-64 year-old Europeans who agree to do colonoscopies when invited to colonoscopy trials, then 0.443% is "unbiased".

On the other hand... remember our trivial little calculation at the top of this post? In three sentences, we found that (decrease for acceptors) = 0.443%. So while the second point is true, we already knew it, and we didn't need no instrumental variables.

Rephrasing the same calculation with instrumental variables doesn't change anything. How could it? If instrumental variables make anything unbiased here, they do it by redefining the "right answer" to be the average over what most people would consider a biased sub-population. But that change is somewhat obscured by the math, so if you aren't an expert, you might not realize it's happened.

---

*Note*: My original calculations were slightly different, because I used published numbers from the NordICC paper—1.2%/0.98% colorectal cancer for the control/invited groups. But the [supporting information](https://www.pnas.org/doi/suppl/10.1073/pnas.2311556120/suppl_file/pnas.2311556120.sapp.pdf) of [Angrist and Hull (2003)](https://doi.org/10.1073/pnas.2311556120) points out that the raw counts in the appendix for the NordICC paper suggest those numbers should be 1.104%/0.918%, which I've used here. (I asked the NordICC authors about this but haven't heard back from them yet.)

*Also*: All the economists I've corresponded with about this have been nothing but kind. But in the spirit of [arguing without warning](/arguing/) I'm posting this without getting any feedback. If you're one of them and you'd like me to signal-boost a response, I'd be happy to do that.