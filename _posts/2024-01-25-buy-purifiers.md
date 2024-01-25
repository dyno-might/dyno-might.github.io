---
layout: post
title: "What if you just bought everyone air purifiers?"
image: /img/buy-purifiers/city2.jpg
tags: 
description: "amazing or nah"
excerpt: 
permalink: /buy-purifiers/
background_color: rgb(241,241,241)
category: "air quality"
comment:
#    substack: https://dynomight.substack.com/p/buy-purifiers
---

I haven't written about air quality in a while. Ominously, sometimes people ask me if I still care about it. So, lest anyone think I have some kind of dreadful healthy mental balance, I thought I should do some Fermi estimates.

Say you're one of the [five humans](https://www.forbes.com/billionaires/) who have $100 billion. You could, in principle, buy 1.3 billion [IKEA air purifiers](/ikea-purifier/). That's enough for one for every household in China, India, the US, Indonesia, Brazil, Russia, Japan, Nigeria, and Germany. How good of an idea would that be?

## TLDR

OK-ish, I guess? Not terrible, but also not great?

I estimate that for an average person in the United States, putting air purifiers in their house and running them for one year extends their life by 0.0033 disability-adjusted life years (DALYs), or a bit over a day. I also estimate that if you add up the purifiers, the filters, and the electricity, this costs around \$109 per year.

So: If you go buying air purifiers for random Americans, you can extend life expectancy at a cost of around **\$33k / DALY**. (That's \$109 / 0.0033 DALY.)

Is that good? Well, back in the golden days when GiveWell used to score interventions in terms of dollars per DALY, they found that [artemisinin combination therapy](https://www.givewell.org/international/technical/programs/malaria-treatment) for malaria could extend lifespan at a cost of $150 / DALY. That's... substantially lower.

But maybe air purifiers would work better in other countries? In India, there's more air pollution, electricity is cheaper, and people less living space, all of which help purifiers. There, I estimate a cost of $1.6k / DALY.  Much better, but still 10× higher than malaria drugs.

Or maybe you don't want to compare to hyper-efficient interventions like malaria drugs? OK, then how about normal healthcare?

In countries with very high human development—like the US—healthcare saves one DALY for around each $70k spent. In countries with low development—like India—saving one DALY only costs around \$1k. Both of those are fairly close to what you'd get from buying random air purifiers.

So this wouldn't be a *terrible* way to spend money, but it's probably not something you'd want to pursue philanthropically. At least, assuming you're the kind of person who is ruthlessly focused on efficiency.

## Exercise for the reader

Can you reconcile this conclusion with a claim that fixing your personal air quality is the [single-most effective thing](/air/) you can do for your health? Points to consider:

* Almost everyone spends money on themselves for benefits that are tiny compared to what that money might do for someone else. Like, I sometimes spend \$12.50 on a burrito, when I could have used that money to buy someone else an entire month of life. Is that grotesque, or healthy participation in the only kind of economic system that's even been shown to work?

* The more you spend on regular healthcare, the harder it is to spend efficiently. (Antibiotics can save a life for a few dollars, but no matter how rich you are, you don't get to live to 125.) So the *marginal* value of spending more on regular healthcare is probably lower than the average value.

* Is air quality a substitute or a complement for healthcare? That is, if the government bought everyone purifiers, would that improve health and reduce healthcare spending? Or would it make everyone live longer and die even older and more expensively than they do now? Does this matter?

## How much would indoor air purification help?

OK, let's do the calculations. To start, we need a few numbers.

How much does getting exposed to air pollution hurt you? Air purifiers remove particulate pollution. A [reasonable heuristic](/air/#a-heuristic-to-quantify-harms) is that being exposed to a (very high) level of 2500 PM₂.₅ for a full year costs one DALY. Equivalently, getting exposed to 1 PM₂.₅ for a year costs 0.004 DALY.

How much air pollution are most people exposed to? Obviously, that depends on the person. The population-mean PM₂.₅ level in the USA is around 10 μg/m³. But what we care about is *indoor* levels. My best estimate for that is 16 μg/m³, which I arrived at by taking figure 5 of [this paper](https://doi.org/10.1101/2021.11.10.21266177) and using the good-old "count number of pixels" method.

Now, air purifiers only work indoors. How much time do people spend indoors? The [National Human Activity Pattern Survey](/air/#where-people-spend-their-time) says that people spend 87% of their time indoors, and 69% of their time in a home (theirs or someone else's). That survey was done in the early 90s, but it probably hasn't changed drastically.

Finally, how much indoor air pollution should we expect air purifiers to remove? My best estimate is 75%, which I arrived at by making it up. (Air purifiers drop steady-state levels pretty low, but you still get occasional bursts of particles from cooking or whatever that take a while to go away.)

So, what do we have? If we multiply the above numbers, we get that the average benefit of installing air purifiers in all homes in the US for a year is

<div class="eq" markdown="1">
&nbsp;&nbsp;&nbsp;&nbsp;.0004 DALY / PM₂.₅  
&nbsp;&nbsp;&nbsp;&nbsp;× 16 PM₂.₅  
&nbsp;&nbsp;&nbsp;&nbsp;× 0.69  
&nbsp;&nbsp;&nbsp;&nbsp;× 0.75  
&nbsp;&nbsp;&nbsp;&nbsp;≈ .003312 DALY
</div>

That's about 29 disability adjusted life hours.

## What would it cost?

An IKEA purifier currently goes for \$75. Let's assume it needs to be replaced every 5 years, for a yearly cost of \$15.

Replacement particle filters cost \$13. Let's assume they need to be replaced once per year. (I've personally run some even longer than that.) Since the machine itself comes with a filter, you need to buy a filter only every 4 out of 5 years, for an average cost of \$10.40.

Run on high, this purifier uses 14 W. At US average electricity prices of $0.23 / kWh, running the purifier all year would cost

<div class="eq" markdown="1">
&nbsp;&nbsp;&nbsp;&nbsp;14 W  
&nbsp;&nbsp;&nbsp;&nbsp;× 365.25 days / year  
&nbsp;&nbsp;&nbsp;&nbsp;× 24 hours / day  
&nbsp;&nbsp;&nbsp;&nbsp;× $0.23 / (1000 Wh)  
&nbsp;&nbsp;&nbsp;&nbsp;≈ $28.23 / year.
</div>

But let's assume people turn it off a third of the time and call it \$20 / year.

So, the total cost to run one purifier for a year is

<div class="eq" markdown="1">
&nbsp;&nbsp;&nbsp;&nbsp;$15 (for the purifier)  
&nbsp;&nbsp;&nbsp;&nbsp;\+ $10.40 (for replacement filters)  
&nbsp;&nbsp;&nbsp;&nbsp;\+ $20 (for electricity)  
&nbsp;&nbsp;&nbsp;&nbsp;\= $45.40.
</div>

How many purifiers would be needed? The average person in the US apparently has around [700](https://www.titlemax.com/discovery-center/first-time-home-buyer/where-in-the-u-s-can-you-get-the-most-square-feet-per-person/) square feet of living space. While the IKEA purifier claims it can only purify a space of around 100 square feet, that seems very conservative. My guess is that one purifier per "room" should be sufficient. According to the OECD, the average home in the US contains [2.4 rooms](https://www.oecdbetterlifeindex.org/topics/housing/) per person (🦅🇺🇸), as compared to the OECD average of 1.7. So let's assume 2.4 purifiers are needed per person.

That implies a yearly cost, per-person, of $45.40 × 2.4 = $108.96 per year.

## Drumroll

So how much money is needed to save a DALY with air purifiers? So far we've estimated that giving a random American adequate air purification for a year provides around 0.003312 DALY, and costs around \$108.96. So how much money is needed to save a DALY this way? Behold division:

&nbsp;&nbsp;&nbsp;&nbsp;\$108.96 / 0.003312 DALY = \$32,899 / DALY.

## What about other countries?

That was all specific to the US. The calculations might be quite different in other places. In India, for example, air pollution is much higher, electricity is cheaper, and people have less living space per capita. All of those will change things.

So let's do an estimate for India. There, mean air particulate levels are around 8 times higher than in the US. That suggests that air purifiers might provide a benefit that's 8 times as large or 0.0265 DALYs (that's 8 × 0.003312 DALY). That's around 9.8 days.

At the same time, Indians have much less living space than Americans (around [100 square feet](https://en.wikipedia.org/wiki/Housing_in_India), as opposed to around 700 square feet). This suggests fewer purifiers are needed. However, with higher particle levels, filters would surely need to be replaced more often. And electricity in India only costs around a third as much in the US. If you re-do the previous cost calculations assuming 1 purifier per person, filters replaced twice a year, and electricity that costs 1/3 as much, that implies a yearly cost of

<div class="eq" markdown="1">
&nbsp;&nbsp;&nbsp;&nbsp;$15 (for the purifier)  
&nbsp;&nbsp;&nbsp;&nbsp;\+ $10.40 × 2 (for replacement filters)  
&nbsp;&nbsp;&nbsp;&nbsp;\+ $20 / 3 (for electricity)  
&nbsp;&nbsp;&nbsp;&nbsp;\= $42.47
</div>

So, in India, the cost per DALY should be around

<div class="eq" markdown="1">
&nbsp;&nbsp;&nbsp;&nbsp;$42.47 / 0.0265 DALY = \$1,603 / DALY.
</div>

## Is that good?

It's not great.

Open Philanthropy values a DALY at [around $100k](https://www.openphilanthropy.org/research/technical-updates-to-our-global-health-and-wellbeing-cause-prioritization-framework/#3-new-moral-weights). So creating new DALYs for \$33k or \$1.6k is good. On the other hand, Open Philanthropy also now expects a [2000× return](https://forum.effectivealtruism.org/posts/KuByzfn6yiKMWBKmr/our-planned-allocation-to-givewell-s-recommendations-for-the) on investment—even with hundreds of millions to spend, they think they can buy DALYs at a price of **\$50 / DALY**. Air purifiers aren't even close.

Meanwhile, [Daroudi et al. (2021)](https://doi.org/10.1186/s12962-021-00260-0) estimate the average $ / DALY for standard healthcare in different countries. Here's what they estimate:

| Human Development Index | Mean $ / DALY |
|-|-|
| Low | $998 |
| Medium | $6,522 |
| High | $23,782 | 
| Very high | $69,499 |

Maybe purifiers are a bit better than this. *Probably* they're a bit better on the margin, especially if you price in the user experience. (Getting extra DALYs via purifiers is more fun than getting them via colonoscopies or chemotherapy.) So, if you compare to how our world normally allocates resources, air purifiers are fine. But if you compare to ruthlessly efficient philanthropy, they aren't remotely close to rising to the top of the pile.