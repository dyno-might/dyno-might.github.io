---
layout: post
title: "Contra Wirecutter on the IKEA air purifier"
image: /img/ikea-purifier/wires-prog.jpg
tags: science
description: "The Wirecutter's review of the IKEA air purifier is a mishmash of scientific errors, shoddy testing, and self-contradictory logic."
excerpt: "IKEA has recently made some moves into the air purifier space. The Wirecutter is not impressed. They allow that this purifier is inexpensive and pretty. But still, it's terrible and you should instead buy a different purifier that totally coincidentally happens to pay affiliate marketing commissions.  When reading this review, I couldn't help but notice that it's rife with factual errors, misleading statements, and self-contradictory experiments. I also noticed that this stems from an ignorance of basic science, air filtration standards, IKEA's public specs, and the same common-sense logic the Wirecutter uses elsewhere for other purifiers."
permalink: /ikea-purifier/
background_color: rgb(0,0,0)
category: "air quality"
comment:
    reddit: https://old.reddit.com/r/dynomight/comments/vgpgbe/contra_wirecutter_on_the_ikea_air_purifier/
    substack: https://dynomight.substack.com/p/contra-wirecutter-on-the-ikea-air
    hacker news: https://news.ycombinator.com/item?id=31812259
---

<span style="font-size:80%" markdown="1">
[*Content warning*: Polemic]
</span>

IKEA has recently made some moves into the air purifier space. The Wirecutter is not impressed.

![wirecutter review](/img/ikea-purifier/wirecutter-prog.jpg){: width="860px" height="957px"}

They allow that this purifier is inexpensive and pretty. But still, it's terrible and you should instead buy a different purifier that totally coincidentally happens to pay affiliate marketing commissions. 

When reading this review, I couldn't help but notice that it's rife with factual errors, misleading statements, and self-contradictory experiments. I also noticed that this stems from an ignorance of basic science, air filtration standards, IKEA's public specs, and the same common-sense logic the Wirecutter uses elsewhere for *other* purifiers.

Wirecutter, let *me* help *you*.

{% comment %}
## Contents
{:.no_toc}

<div style="font-size:90%; line-height:110%;" markdown="1">

* auto-gen TOC:
{:toc}

</div>
{% endcomment %}

## On true-HEPA filters

Claim:

> "it isn’t a true-HEPA purifier"

They make a big deal about this, which is weird since ["true-HEPA" has no legal or scientific meaning](https://en.wikipedia.org/wiki/HEPA#Marketing). Meanwhile, they refer to the IKEA purifier as using a "PM2.5 filter" which also isn't a thing.

What *is* the filter that the IKEA purifier uses? Well, perhaps we should, I don't know, read the IKEA website?

![ikea page](/img/ikea-purifier/ikea-page2.jpg){: loading="lazy" height="957" width="860"}

(This, *this* is the kind of groundbreaking research I dreamed of when starting this blog.)

From these details, we can quickly figure out that there is a [European HEPA filter standard](https://en.wikipedia.org/wiki/HEPA#Specifications), with various classes:

| Class | Performance |
| ----- | ----------- |
| E10   | 85%         |
| E11   | 95%         |
| E12   | 99.5%       |
| H13   | 99.95%      |
| H14   | 99.995%     |
| U15   | 99.9995%    |
| U16   | 99.99995%   |
| U17   | 99.999995%  |

The IKEA purifier uses a filter of class E12, whereas the one the Wirecutter recommends instead uses a filter of class H13---one level stricter. So it seems Wirecutter is using "true-HEPA" to mean "H13".

Except---what's the logic here? This difference is core to Wirecutter's dismissal of the IKEA purifier. But we are never given a reason why H13 is good enough, but E12 isn't. Surely it's not just that higher numbers are better? Because then why not insist on a level 17 filter?

They never once recognize the IKEA filter is of class E12, instead using the misleading term "PM2.5 filter" and saying things like:

> It’s designed to capture PM2.5—that is, particles 2.5 microns in diameter and above, in contrast to the 0.3-micron HEPA standard.

It's an accomplishment to pack so many errors into such a small passage.

1. This passage implies that a ("true"?) HEPA filter is designed to capture particles that are 0.3 microns or larger. But an H13 filter must, by definition, capture 99.95% of particles of all sizes.
2. This passage states that the IKEA filter is designed to capture particles that are 2.5 microns or larger. That is also incorrect. What the IKEA filter is designed to do is to meet the E12 spec---which says that it must capture 99.5% of particles of all sizes.
3. Neither size mentioned (0.3 microns or 2.5 microns) has any relationship to either of the design specs.

This is just the beginning of our problems.

## On physics

Claim:

> If you’re looking to improve your indoor air quality, a true-HEPA [is] exceptionally good at capturing ultrafine smoke particles, down to at least 0.01 micron in diameter. 

Wrong.

Another claim:

> [The IKEA purifier is] optimized for larger airborne particles, such as pollen and mold spores, rather than for very fine particulates like wildfire smoke, as HEPA filters are. 

Also wrong.

The physics of air purifiers seem simple. If you create some material with small holes and push air through it, the bigger particles won't be able to fit through the holes. So you'd expect something like this:

![physics.002](/img/ikea-purifier/physics2-comp.svg){: loading="lazy"}

This is strainers and sieves work in your kitchen. It's how the Wirecutter seems to think air filters work. But it's not how air filters work.

Would you believe me if I told you they work like *this*?

![physics.003](/img/ikea-purifier/physics4-comp.svg){: loading="lazy"}

I thought you might not, so here are some figures, from [Heimbuch et al. (2007)](https://apps.dtic.mil/sti/pdfs/ADA464232.pdf), [Fisk et al. (2001)](https://doi.org/10.1034/j.1600-0668.2002.01136.x), [Christopherson et al. (2020)](https://doi.org/10.1177/0194599820941838), and [Wikipedia](https://en.wikipedia.org/wiki/HEPA#/media/File:Filteration_Collection_Mechanisms-en.svg):

| ![heimbuch](/img/ikea-purifier/heimbuch.svg){: loading="lazy"} | ![fisk](/img/ikea-purifier/fisk.svg){: loading="lazy"} |
| ![Christopherson](/img/ikea-purifier/vijayakumar.jpg){: loading="lazy"} | ![wikipedia](/img/ikea-purifier/Filteration_Collection_Mechanisms-en.svg){: loading="lazy"} |

Air filters *do not work like sieves*. They are complicated materials that create a maze of tangled paths for air to run through. There are two different mechanisms:

**Impaction/interception**: When larger particles go through, they sometimes "can't make a turn" and get stuck. But you shouldn't think of this like a particle "plugging a hole"---it's more a statistical phenomenon, and it still happens for particles much smaller than the pores in the filter media.

**Diffusion**: Smaller particles have less momentum and so can't easily resist the motion of the air. But for the same reason, they are beset by random fluctuations known as Brownian motion. These can *also* cause the particles to get stuck in the filter material. This works especially well for the smallest particles.

Get that? Air filters easily catch both large and small particles. It's the intermediate regime where things are hard. The size where the filter performs *worst* is called the Most Penetrating Particle Size (MPPS). Typically this is around 0.15 microns.

The EU HEPA filter spec---yours to download today for a bargain [$1148.24](https://www.en-standard.eu/set-en-1822-and-en-iso-29463-standards-for-heigh-efficiency-air-filters-epa-hepa-and-ulpa/)---says that filters should meet their guarantees *at their MPPS*. An E12 filter must block 99.5% of particles at its worst-case particle size, while an H13 filter must block 99.**9**5%.

So it's rubbish to claim that an H13 filter will do a better job than an E12 filter for very fine particles. Those are easy to catch because they are well into the diffusion regime, so both an E12 and an H13 filter will block almost all of them.

## On filters

Now, how much should we care about the difference between an E12 and an H13 filter?

Here's a thought experiment: Take a 1000 cubic feet room and a purifier that processes 100 cubic feet of air per minute. (I follow Wirecutter in using vulgar imperial units.) Assume pessimistically that all particles are the worst-case size. If you run that purifier with an E12 filter, the fraction of particles that will remain after one minute is

&nbsp;&nbsp;&nbsp;&nbsp; .1 × (1-.995) + .9 = 0.9005.

That's because 10% of the air goes through the purifier and has 99.5% of particles removed, while 90% of the air doesn't go through the purifier at all.

Meanwhile, if you run that purifier with an H13 filter instead then the fraction of particles that remain will be

&nbsp;&nbsp;&nbsp;&nbsp; .1 × (1-.99**9**5) + .9 = 0.900**0**5.


If you noticed that 0.9005 and 0.90005 are almost identical then congratulations---you understand air filters better than the Wirecutter. Both 99.5% and 99.95% are close enough to 100% that performance is almost entirely determined by the *volume of air* they process.

The stricter specs are most useful for situations like cleanrooms or medical applications where you need to make sure that all air that crosses a boundary is clean.
Far from being an "automatic dismissal", if you're just cleaning the air and then circulating it back into a room as a freestanding air purifier does, the difference between an E12 and an H13 purifier is a complete non-issue.

<details markdown="1">
<summary>(details)</summary>

Many particles will be far from the MPPS and so will be blocked equally well by each. But let's be pessimistic and focus on worst-case particles. How much should we care about a 99.5% vs 99.95% difference?

The answer is: Not much.

These higher grades mostly make a difference if you'll be putting air through it just once, like in a medical application or a cleanroom or something. For an air purifier sitting in a room, the air will go through it again and again. If you missed some tiny fraction of particles the first time, you'll get them on the next cycle. What matters is how fast you push air through the filter.

Here's a simple simulated experiment. We take two filters, one that blocks 99.5% of particles, and one that blocks 99.95%. Then, we put them in a 700 cubic foot (19.8 cubic meter) room with different airspeeds. Here will be the fraction of particles remaining after 30 minutes:

![filters](/img/ikea-purifier/filters.svg){: loading="lazy"}

If that looks like two curves on top of each other, well... yeah. 99.5% and 99.95% are both very close to 100%. For either of them, the limiting factor is going to be how fast you push air through them, not the tiny fraction of particles they let through.

</details>


## On weakness

The second---and seemingly more valid---criticism of the IKEA purifier regards its strength.

> with a clean air delivery rate (CADR) of just 82.4 cubic feet per minute, the Förnuftig is appropriate for only very small rooms

> Our pick among small-space purifiers [...] and has a CADR of 135 

The CADR is the volume of air that goes through the purifier in a minute, times the fraction of particles removed from that it. A purifier that churns through 100 cubic feet of air but removes 50% of particles has a CADR of 50, just like a purifier that goes through 50 cubic feet of air but removes all particles.

(Technically a CADR should be computed for particles of a given *size*, but the Wirecutter---and most manufacturers---and [I](/better-DIY-air-purifier.html)---tend to neglect that.)

So the CADR is a good way to measure how powerful a purifier is. And the IKEA purifier isn't super powerful. But let's do another thought experiment:

* Say you have a 10-foot by 7-foot bedroom with 10-foot high ceilings.
* This room is pretty drafty so after an hour, half the air is replaced with air from outside.
* You live in a moderately polluted city, with an outdoor air level of 30 μg/m³ of PM2.5 particles.

If you run the IKEA purifier, this will give you a steady-state level of

&nbsp;&nbsp;&nbsp;&nbsp; 2.39 μg/m³

while the *more powerful* recommended purifier would lead to a level of

&nbsp;&nbsp;&nbsp;&nbsp; 1.38 μg/m³.

<details markdown="1">
<summary>(math)</summary>

* Take a 10' by 7' bedroom with 10' high ceilings. That's 700 cubic feet of space.
* Say the [ventilation half-life](/air/#half-lives-of-air-in-homes) in that room is 1 hour meaning that within 1 hour, half of the air has been replaced by air from outside. (This is relatively fast, as these things go.)
* Say you live in a moderately polluted city, with an outdoor air level of PM2.5 30 μg/m^3 of particles. (The same logic works for smaller particles too.)

If half the air changes with the outdoors in an hour, then around 1.149% of air changes in a minute. (Since (1-0.011486)⁶⁰=0.5). Say the air starts at a level of L. Now, let a single minute pass. The outside air coming will change the level to L + 0.011486 × (30-L).

Meanwhile, the 82.4 CADR will remove a fraction of 82.4/700=0.117 of the particles. (Technically these things happen at the same time, but this is a decent approximation since we're just looking at a short time interval.) So, L will be a steady state if (L + 0.011486 × (30-L)) × (1-0.117) = L, which is solved by L = 2.39.

On the other hand, if we used the MORE POWERFUL purifier with a CADR of 135 it will remove a fraction of 135/700=0.192857 of the particles. So L will be a steady state if (L + 0.011486 × (30-L)) × (1-0.192857) = L, which is solved by L=1.376.

</details>

That's lower, but do we care? The first level is already comparable to the [least polluted cities on the planet](http://berkeleyearth.lbl.gov/air-quality/CityAverageList.php). And most people reading this probably have less drafty windows or cleaner outside air.

This is to say: In small spaces, a modest CADR is often perfectly adequate to reduce particle levels to almost zero.

Other than cleaning, what else might we care about?

## On money

Claim:

>  Our pick among small-space purifiers [...] is not much more expensive

Let's do a little comparison.

|                           | IKEA purifier | IKEA+carbon filter | Wirecutter pick |
| ------------------------- | ------------- | -------------------------------- | --------------- |
| Original cost             | \$70          | \$86                             | \$100           |
| CADR                      | 82.4          | 70.6                             | 135             |
| Electricity usage         | 16W           | 14W                              | 45W             |
| Electricity cost per year | \$21.02       | \$18.40                          | \$59.13         |
| Replacement filters       | \$10          | \$26                             | \$30            |


The IKEA purifier uses a *lot* less energy. Above, I've computed electricity costs assuming you run each purifier on high year-round at US-average electricity prices. (Yeah, power usage goes *down* when you add the extra carbon filter to the IKEA purifier. I've confirmed this myself with a power meter. Physics is weird.)

What about filters? Well, IKEA recommends replacing them every 4 months, while the Wirecutter pick recommends doing it every 6 months.

Personally, I suspect those recommendations are (both) conservative. The "change filter" light almost always just counts elapsed days---but filters don't really get "old", they get "full". Smart Air has done experiments [[1](https://smartairfilters.com/en/blog/hepa-lifespan-how-long-filters-last/) [2](https://smartairfilters.com/en/blog/hepa-lifespan-how-long-filters-last/) [3](https://smartairfilters.com/en/blog/blast-mini-hepa-filters-lifespan/)] that found efficacy only declined after filters looked worryingly dirty, which took something like six months even with real (highly polluted) Beijing air. I've used some IKEA purifiers in small rooms for almost a year with the same filter and seen little drop in performance.

What we'd *like* to know is how many particles each filter can absorb per dollar. This is hard, though some very crude very estimates for the size/weight of the different replacement filters suggest you get at least as much for your money with the IKEA filters.

So the IKEA purifier is cheaper, uses much less energy, and plausibly requires less money for filters (especially if you don't use the carbon filter).

<details markdown="1">
<summary>(math)</summary>

If you ran the IKEA purifier (without a carbon filter) on high year-round and your electricity cost a US-typical $0.15 per kilowatt-hour, that would cost you

&nbsp;&nbsp;&nbsp;&nbsp; (16 W)×(365 d/y)×(24 h/d)×(\$0.15/1000Wh) = \$21.02/y.

If you did the same thing while using the carbon filter, the cost would be \$18.40. For the Wirecutter pick, the cost would be \$59.13.

</details>

<details markdown="1">
<summary>(crude estimates)</summary>

This is a little complicated because the Wirecutter recommendation is a combined particle/carbon filter, but the \$10 IKEA particle filter has a surface area similar to the Wirecutter recommendation, and the \$26 IKEA carbon filter *by itself* weighs almost as much as the entire \$30 filter. Both of these suggest that you get "as much for your money" with the IKEA filters, though this definitely isn't the final word. (Also, having separate particle and carbon filters saves you from replacing both when only one is exhausted.)

The IKEA particle filter is a rectangle with an area of 155 in^2

* The IKEA particle filter weighs 6 oz
* The IKEA carbon filter weighs 14 oz
* The Wirecutter pick has a cylindrical filter that I estimated to have an area of 148 in^2 using the overall size and trigonometry.
* The Wirecutter pick (which combines particle and carbon filter layers) has a total weight of 17.6 oz.

</details>


## On tests

The final complaint is based on some tests that they did. They generated particles in a 1600 ft³ bedroom and tested how many of them could be removed in half an hour. They tried each purifier on particles of two different sizes and ran the purifiers at two different speeds. Here's what they report:

| Speed  | Particle size | IKEA           | Wirecutter pick | 
| ------ | ------------- | -------------- | --------------- | 
| medium | 3.0 microns   | 73.6% removed  | “virtually all” | 
| high   | 3.0 microns   | 85.2% removed  | “virtually all” | 
| medium | 0.3 microns   | 53.5% removed  | 92.6% removed   | 
| high   | 0.3 microns   | 64.5% removed  | 97.4% removed   | 

These tests... are not credible.

Take the 3.0-micron tests on medium, where Wirecutter claims "virtually all" particles were removed. If we take that to mean 99%, that implies a CADR of 236.2. (The math is below.) That is 75% higher than the manufacturer's claimed performance on *high*.

It also contradicts the Wirecutter's own tests. On a different page, they tested the same purifier on medium in a (smaller) 1215 ft³ room and found only *92%* of particles were removed. This implies a (plausible) CADR of just 98.1.

So we can either (a) accept that the purifier's performance randomly varies by a factor of more than 2.4 or (b) conclude that the Wirecutter did an extremely shoddy job of running these tests.

But whatever, I converted all the above numbers into implied CADR values:

| Speed  | Particle size | IKEA           | Wirecutter pick | 
| ------ | ------------- | -------------- | --------------- | 
| medium | 3.0 microns   | CADR 72.2      | ???             | 
| high   | 3.0 microns   | CADR 102.4     | ???             | 
| medium | 0.3 microns   | CADR 41.8      | CADR 138.0      |
| high   | 0.3 microns   | CADR 56.3      | CADR 190.1      |

If we still for some reason believed that these tests were meaningful, what then?

Well, IKEA claims a CADR of 82.4 on high, and 53.0 on medium. So even taken at face value, this says that IKEA performs a bit above spec on 3.0-micron particles and a bit below spec on 0.3-micron particles. (That's assuming no carbon filter was used when testing the IKEA purifier, something the Wirecutter never clarifies.)

Even if we accepted *all* these test results (we don't) that would just show the Wirecutter pick provides around 3.3 times as much cleaning per second.

More cleaning would be good. But the Wirecutter pick also costs more, uses 3x more electricity, and requires more expensive filters. In real life, higher CADR has rapidly diminishing impact since once you've removed all the particles, there's nothing left to do. Even assuming these (unbelievable) tests were correct, the IKEA purifier would *still* be a better choice for many smaller rooms.

<details markdown="1">
<summary>(math)</summary>

First, take the "virtually all" statements. If you removed removed 99% in half an hour on medium in a 1600 ft³ room, that's equivalent to saying that

&nbsp;&nbsp;&nbsp;&nbsp; (1-C/1660)³⁰ = (1-.99),

where C is the CADR. This equation is solved by C = 236.2. This is in contrast to a manufacturer's claimed CADR of 135.

Meanwhile, take the other test that removed 92% in half an hour on medium in a 1215 ft³ room. That's equivalent to saying that

&nbsp;&nbsp;&nbsp;&nbsp; (1-C/1215)³⁰ = (1-.92),

which is solved by C=98.1.

Now, for the IKEA purifier on high for 0.3 micron particles

* It removed 64.5% of particles in half an hour.
* This is equivalent to saying (1-C/1660)³⁰ = (1-.645)
* This is solved by C = 56.32

For the IKEA purifier on medium for 0.3 micron particles

* It removed 53.5% of particles in half an hour.
* This is equivalent to saying (1-C/1660)³⁰ = (1-.535)
* This is solved by C = 41.8,

The other values can be obtained in the same way.

(Technically I'm approximating things by discretizing to one-minute intervals, but this is an OK approximation and this makes the math much easier to understand.)

</details>

## On logic

Maybe we should be generous and ignore all the errors and misstatements above. Maybe we should just think that the Wirecutter for some reason prioritizes high-performance purifiers.

Except we can't do that: Here's a quote from another page on their site discussing another (affiliate-paying) purifier:

> Although these models are not our first choice because of their slower rate of cleaning, we are comfortable recommending them for their exceptional energy efficiency and corresponding low long-term running costs. [...] The total five-year running costs are thus just $200, about 60% less than the costs [Wirecutter Pick #1]. Add in [Wirecutter Pick #2]'s quiet operation and good looks, and they are an attractive option for small spaces.

So the IKEA purifier is cheap and attractive and has low electricity costs, but it's garbage and no one should buy it because it is weaker and something something "true HEPA" mumble mumble mumble. Instead, they should buy [Wirecutter Pick #1]. But at the same time, [Wirecutter Pick #2] is weaker than [Wirecutter Pick #1] but it's still a decent choice because it's cheap and attractive and has low electricity costs.

Might there be a contradiction here?

(If you're wondering, compared to Wirecutter Pick #2, the IKEA purifier has slightly lower performance, *very* slightly higher energy usage, much cheaper filters, and costs half as much.)

## Conclusion

Sometimes you want a big powerful purifier, which the IKEA purifier isn't. I keep a big powerful purifier in the kitchen which I turn on as needed. (Remember: [cooking creates lots of particles](/air/#things-that-create-particles-indoors)!) But for small rooms (and low infiltration rates and less polluted air) you don't need much to reduce particles to zero. In those cases, the IKEA purifier:

* Is pretty.
* Comes with a cleanable pre-filter, which prolongs filter life.
* Has particle/carbon filters that can be replaced separately.
* Uses minimal energy.
* Is cheap.
* Has cheap particle filters.
* Has cheap carbon filters.
* Cheap.

So if you have a small space and the IKEA purifier appeals to you, go ahead and get it. It may be the most cost-effective purifier on the market, and the evidence the Wirecutter uses to huffily dismiss it is ill-informed, misleading, and self-contradictory.

<details markdown="1">
<summary style="font-weight:bold">Appendix: On Mistakes</summary>

Here's a list of the biggest mistakes in the Wirecutter's review:

1. They incorrectly call the IKEA filter a "PM2.5 filter", implying there is a qualitative difference with the "true-HEPA" filter they recommend. In reality, the IKEA filter is an E12 filter, a specification only slightly less strict than the H13 filter they recommend.

2. They incorrectly state that the IKEA purifier will struggle to remove any particles smaller than 2.5 microns. But the E12 spec has nothing to do with 2.5 microns. What is says is that the filter must remove 99.5% of particles of all sizes.

3. They incorrectly state that their recommended purifier will do a much better job than the IKEA purifier of removing very small particles with sizes near 0.01 microns. This contradicts the basic physics of air purifiers. These tiny particles are very easy to remove because they are well into the diffusion regime and both E12 and H13 filters will catch almost all of them.

4. Their test results for their recommended purifier are not credible: They far exceed the manufacturer's claimed CADR. They also exceed *their own* tests of the same purifier by a factor of more than 2.4.

5. Their economic logic is self-contradictory. On the one hand, the IKEA purifier is rejected for being relatively weak and a more powerful purifier is recommended instead---ignoring that the IKEA purifier is cheaper and much more energy efficient. Yet on another page, they are happy to recommend a *different* purifier that is *also* weaker, because *it* is energy efficient---even though it costs twice as much as the IKEA purifier.

</details>

<details markdown="1">
<summary style="font-weight:bold">Appendix: Disclosure</summary>

People are suspicious about the motives of online reviews (why could that be?) so just to state it outright: I make no money. I haven't linked to any purifiers, and IKEA has no affiliate program anyway. The only motive here is indignation.

</details>