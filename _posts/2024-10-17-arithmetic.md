---
layout: post
title: "Arithmetic is an underrated world-modeling technology"
image: /img/arithmetic/hippos2.jpg
tags: 
description: "if you keep units" 
excerpt: ""
permalink: /arithmetic/
background_color: rgb(147,131,120)
category: "math"
#comment:
#  substack: "https://dynomight.substack.com/p/arithmetic/"

---

Of all the cognitive tools our ancestors left us, what's best? Society seems to think pretty highly of arithmetic. It's one of the first things we learn as children. So I think it's weird that only a tiny percentage of people seem to know how to actually *use* arithmetic. Or maybe even understand what arithmetic is for. Why?

I think the problem is the idea that arithmetic is about "calculating". No! Arithmetic is a world-modeling technology. Arguably, it's the *best* world-modeling technology: It's simple, it's intuitive, and it applies to everything. It allows you to trespass into scientific domains where you don't belong. It even has an amazing error-catching mechanism built in.

One hundred years ago, maybe it was important to learn long division. But the *point* of long division was to enable you to do world-modeling. Computers don't make arithmetic obsolete. If anything, they do the opposite. Without arithmetic, you simply can't access a huge fraction of the most important facts about the world.

The magic lives in a thing called "units".

## Chimps

It's amazing how much we don't know about nutrition. For example, would you live longer if you ate less salt? How much longer? We can [guess](https://doi.org/10.1093/eurheartj/ehac208), but we don't really know.

To really be sure, we'd need to take two groups of people, get them to eat different amounts of salt, and then see how long they live. This is expensive, ethically fraught, and runs into the problem that when you tell people to eat differently, they usually ignore you.

So I've often wondered: Why don't we do these experiments on *animals*? Why not get two big groups of chimpanzees, and feed them different amounts of salt? Chimps aren't people, but it would tell us something, right?

Why don't we do this? Because arithmetic.

How much would such a study cost? To figure this out, you will need three numbers:

1. The average lifespan of a chimp.
2. The cost to maintain one chimp in a research facility for one day.
3. The number of chimps you'd need for a study.

Let's do these. First, how long do chimps live? In captivity the average seems to be around 36.3 years. (Incidentally, female chimps seem to live 25% longer than males—imagine human women lived until 90 while men died at 71.)

Second, how much does it cost to maintain a chimp? [Capaldo et al.](https://www.releasechimps.org/photos-and-pics/Economics%20%20Chimp%20Research_T%20%20Capaldo%20et%20al%20revised%20for%20website.pdf) looked at the average costs in various research facilities in the US in 2009. They estimate around $75/day (in 2024 dollars).

Finally, how many chimps do you need? To calculate this, you should do a "power calculation"—you guess how much life expectancy varies due to (a) salt and (b) all random factors, and work backwards to see how many chimps you need to separate the signal from the noise. There are lots of [calculators](https://clincalc.com/stats/samplesize.aspx) for this. If you assume chimps live 36.3±8 years and salt would change life expectancy by 2 years, these will tell you that you need 502 chimps.

So now we can do our calculation:

&nbsp;&nbsp;502 chimps  
&nbsp;&nbsp;&nbsp;&nbsp;  × 36.3 years  
&nbsp;&nbsp;&nbsp;&nbsp;  × 365.25 days / year  
&nbsp;&nbsp;&nbsp;&nbsp;  × 75 dollars / (chimp day)  
&nbsp;&nbsp;&nbsp;&nbsp;  ≈ 499,185,349 dollars

Notice three things.

First, 500 million dollars is a *lot*. That's five times what the [big alcohol trial](https://dynomight.net/alcohol-trial/) would have cost. It's a gigantic amount of money for something that would only give indirect evidence for the impact of salt in humans, and wouldn't even do that until decades in the future.

Second, notice how I kept the units. Always keep units! On the "top" of the calculation, the units were "chimps × years × days × dollars". On the "bottom", the units were "years × chimps × days". When you cancel terms, you're left with dollars only. Units are great because if you made a mistake, it will probably show up in the units not working out. We'll see other benefits below. So: ALWAYS KEEP UNITS.

(If you think you're an exception and you don't need units, then you *especially* need to keep units.)

Finally, notice that this calculation didn't just tell us how expensive the study would be. It also points towards *why* it's so expensive, and what would be needed to make it cheaper.

One option would be to try to get away with fewer chimps. The reason so many are needed is because the likely impact of salt is pretty small compared to natural variation in life expectancy. You might be able to reduce that natural variation by, for example, using pairs of chimp twins to eliminate genetic variation. If that reduced the standard deviation from 8 years to 5 years, then you'd only need 196 chimps and the total cost would be "only" 195 million dollars. Sounds nice, though I imagine that creating 98 chimp twins wouldn't be free.

Another option would be to reduce the cost of maintaining chimps. Doesn't $75 per chimp per day seem *very* expensive? Perhaps you could find a way to use existing chimps in zoos? Or you could use dogs instead of chimps and offer dog owners subsidized dog chow with slightly varying salt levels? Or you could built a gigantic outdoor facility with 50,000 chimps where you could amortize costs by running 100 experiments in parallel?

I'm not sure which (if any) of these options would work. My point is that doing the arithmetic quickly takes you into specifics about what would be necessary to actually move the needle. Without doing the arithmetic, what chance would you have to say anything meaningful?

## Big blocks

If I know my readers then at some point in your life you probably considered using gravity to store energy. Maybe you can put solar panels on your roof, but instead of storing their energy in batteries, you can just lift up a giant block into the air. At night you can slowly let the block down to power your house. How big a block do you need?

Let's assume you don't know much physics.

To answer this question, you'll need two numbers:

1. How much energy you need to store to power your house?
2. How much energy can you store by lifting up a giant block?

If you check the internet, you'll learn that the average US household uses around 30 kWh of energy per day. Now, what's a "kWh"? To you, person who doesn't know much physics, it looks scary, but apparently it's some kind of unit of energy, so let's just write it down. Assume you need to store half your daily energy for usage at night, or 15 kWh.

Now, how much energy can you store by lifting a giant block up into the air? A little bit of searching reveals that "[potential energy](https://en.wikipedia.org/wiki/Potential_energy#Overview)" is the product of mass, gravity, and height: If you lift a block of weight *MASS* up to height *HEIGHT*, the stored energy is *U=MASS × g × HEIGHT* where *g ≈ 9.8 m/s²* on Earth. Your house is 6m tall, and you reckon that's as high as you could lift a block, so you use *h* = 6m. Thus, the amount of energy you can store is

&nbsp;&nbsp;*MASS × (9.8 m/s²) × 6 m*.

What now? Now, you're done! You just equate the energy you need to store with the energy you can store with a block that weighs *MASS*:

&nbsp;&nbsp;15 kWh = *MASS* × (9.8 m/s²) × 6 m.

Is this frightening? There are units everywhere. You never figured out what a kWh is. How is that related to meters and seconds? What does it mean to square a second? Panic!

Relax. We have computers. You can just mechanically solve the above the above equation to get *MASS* = 15 kWh / (9.8 m/s² × 6 m) and then [*literally type that into a search engine*](https://www.google.com/search?q=15+kWh+%2F+(+9.8+m%2Fs^2+*+6+m)) to find that *MASS* is:

<img src="/img/arithmetic/calc1.png" style="max-width:373px;">

Look at that—the answer is in kilograms!

It happens to be the case that 1 kWh = 3,600,000 kg/s². You *could* substitute this and cancel units to get the same answer. But don't. Attempting that just gives you the chance to screw things up. Why complicate your life?

And as before, the units give you a sort of "type checking". If your calculation was wrong, you'd have to be very unlucky to get an answer that was in kg anyway.

Here the units did most of the work for you. So it's a good thing you kept units.

**ALWAYS KEEP UNITS**.

## More big blocks

So, a 918 thousand kg block. How much would that cost? It seems natural to use rock, but it's hard to get million kilogram boulders delivered to your house these days. So let's use steel. Current steel prices are $350/ton. So we want to solve 

&nbsp;&nbsp;*918,367 kg = MONEY × 1 ton / $350*.

How are tons related to kilograms? Say it with me: *Not your problem*. Just solve the above equation for *MONEY* and ask the [big computer](https://www.google.com/search?q=918367+kg+%2F+%281+ton+%2F+%24350%29) to learn that *MONEY* is

<img src="/img/arithmetic/calc2.png" style="max-width:400px;">

That's 65× more than just buying a 20 kWh home battery. But let's say you're committed to the bit. How *big* would that block be? Some searching reveals that the density of steel is around 7.85 g/cm³. So if you have a cubic block of volume VOLUME, then 

&nbsp;&nbsp;*MASS = 2.7 g / cm³ × VOLUME*.

Solving for *VOLUME*, using the previous value for *MASS*, and not stressing about units, you can [easily find](https://www.google.com/search?q=918367+kg+%2F+(2.7+g+%2F+cm^3)+in+m^3) that *VOLUME* is:


<img src="/img/arithmetic/calc3.png" style="max-width:282px;">

A 340 cubic meter block is around 7 meters on all sides. So, roughly speaking, your house will look something like this:

![](/img/arithmetic/house.svg)

As it happens, 1 million kg cranes *do* exist. But even used, they'll set you back another million dollars or so. If you're going to get one of those, then may I suggest that the same weight is given by almost exactly 4.5 Statues of Liberty? So I suggest you also consider this option (drawn to scale):

![](/img/arithmetic/liberty.svg)

Either way, your neighbors will love it.


<br>

P.S. Today's link is to Philosophy Bear on [Have you tried talking to people about what you believe?](https://philosophybear.substack.com/p/have-you-tried-talking-to-people):

> But what I find most interesting about the result is not that it has been achieved by LLMs, but that it has been achieved at all. The myth that homo sapiens cannot be persuaded by reason may be just that- a myth created by a coalition of: