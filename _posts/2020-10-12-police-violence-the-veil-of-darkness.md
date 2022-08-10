---

layout: post
title: "The veil of darkness"
image: /img/police/court_light_cropped.jpg
tags: statistics policy
description: Explores some natural experiments that try to measure police violence.
seo:
  date_modified:2021-02-09
permalink: /:year/:month/:day/:title/
category: "politics/policy"
---

Measuring police bias using simple ratios [doesn't work](https://dynomight.net/2020/10/08/police-violence-your-ratios-dont-prove-what-you-think-they-prove/). You can never cleanly separate the impact of race from other associated factors.

But imagine we had augmented-reality goggles that made race invisible. Suppose we ran the following experiment:

* Have half of police wear race-invisibility goggles for a year.
* Have the other half wear non-invisibility goggles.
* Look at the difference of the two groups.

The police with invisibility goggles would [*not*](https://dynomight.net/2020/10/08/police-violence-your-ratios-dont-prove-what-you-think-they-prove/#a-thought-experiment) have equal statistics with respect to race. That's because race is correlated with many things other than how people look.

However, the only difference between the two groups of police is if they can see race. Thus, their *difference* would reveals exactly the impact of police bias.

We haven't done this experiment, of course. But we've done a kind of low-tech approximation. Instead of augmented reality goggles, we use the geometry of the earth and sun. Here's the idea: Take all cars stopped by police in some around around 7:15. It will be light in summer, but dark in winter, meaning it's harder to tell the race of the driver. So we ask: does the racial mix of stopped drivers change throughout the year?

# Stopping data

This was first studied in [Grogger and Ridgeway](https://www.rand.org/pubs/reprints/RP1253.html) in 2006 with a small and unreliable dataset. A heroic follow-up was done by [Pierson et al.](https://5harad.com/papers/100M-stops.pdf) in 2020. They filed public records requests with 50 states and over 100 municipal police departments. (You do not, it appears, screw around with Pierson et al.) They ended up with a database of around 95 million stops from 21 state patrol agencies and 35 municipal police departments.

Sure enough, they find that the fraction of stopped drivers who are black is lower when it's dark. Their results (eyeballing a graph) are:

| | Black |
|-|-|
|% stopped when it is light outside | ~25%|
|% stopped when it is dark outside | ~22%|

I think this is both more and less than it first seems.

This is around a 12% drop, which might seem small. But I think it suggests a larger bias: Reduced light has a modest effect on officers' ability to see race. Often, it changes nothing, either because race was *already invisible* in daylight, or *remained visible* despite darkness. Roughly speaking there are four cases:

| | Light Outside | Dark Outside |
|-|-|-|
|**Case A** | Visible| Visible|
|**Case B** | Invisible | Invisible |
|**Case C** | Visible | Invisible |
|**Case D** | Invisible | Visible |

Case A might happen near bright streetlights. Case B might happen if the driver is far away from the officer. The measured effect is coming *only* from case C (and partially cancelled by case D). Imagine switching from a regime where officers *always* saw race to one where they *never* saw race. Then the effect &ndash; if real &ndash; would probably be much larger.

<!--
| | Light Outside | Dark Outside |
|-|-|-|
|Case A | Visible| Visible|
|Case B | Invisible | Invisible |
|Case C | Visible | Invisible |
|Case D | Invisible | Visible | -->

But is the effect real? It looks conclusive at first. But there are three major problems:
* First, sunlight might change **driver demographics**. Some race might have more jobs tied to daylight hours, meaning driving times vary throughout the year. Or, some race might have more parents, meaning a greater sensitivity to school being out in summer.
* Second, sunlight might change **driver behavior**. Maybe some race speeds less when it is dark. Maybe people consume alcohol at different hours.
* Third, sunlight might change officers' access to **information other than race**. Broken taillights might be easier to detect when it's dark. Contraband or domestic disputes might be easier to detect during the day.

It's not clear what effect these factors could be having. They could be making the effect look larger than it is. They could also be making the effect look smaller. They might cancel out. Since there's no reason for them to point in either direction, I give higher probability to the bias being real than not.

So this data is weird. I think it gives fairly *weak* evidence of a fairly *large* effect. There's a huge amount of uncertainty due to all the uncontrolled factors.

> **Stopping data**
> * Record all drivers who are stopped by police around 7:15pm during a whole year. The fraction who are black is around 12% lower during times of the year when it is dark outside.
> * Suggests a larger bias than 12% since changing light only affects a fraction of situations.
> * Could be confounded by three other things that might change during the year: Driver demographics, driver behavior, and officers' access to information other than race.

# Search data

Pierson et al. also look at a 8 state patrol agencies and 6 municipal police departments that provide extra data. For these, we know if the police decided to perform a search of the car. The results are as follows.

| | Black | White| Hispanic |
|-|-|-|-|
|% searched, state patrol agencies | 4.3  | 1.9 | 4.1  |
|% searched, municipal police departments | 9.5 | 3.9  | 7.2 |


There are big differences, but of course this doesn't prove anything (yet) because we don't know searches were performed because of race or because of other factors correlated with race.

But here things get interesting. There's also data on *if officers report finding contraband*.

| | Black | White| Hispanic |
|-|-|-|-|
|% of searches yielding contraband, state patrol agencies| 29.4 | 32 | 24.3 |
|% of searches yielding contraband, municipal police departments| 13.9 | 18.2 | 11.0 |

The obvious explanation is that police tend to require stronger indicators to trigger searches of whites than they do for non-whites, so searches of white people yield contraband more often.

The observed bias is smaller for whites vs. blacks (8% or 30%) than for whites vs. hispanics (31% or 65%). We are also observing the "full effect". We can assume that police are aware of the race of (almost) all drivers the step. This isn't just a fraction of the true bias, like with the stop data above. State patrol agencies show less than half as much bias as municipal police departments.

While this is decent evidence, it's not completely conclusive. It's possible that race-blind policing could produce data like this. Here's three examples:

1. Different "base rates". Imagine that some fraction of cars are randomly chosen to be searched (race-blind). Some races might be more likely to carry contraband.  Drivers of that race would have a higher "hit rate" than others, even though police were not biased.

2. Some races might be more likely to give off *signals* of contraband. Imagine a world with two drugs and two races.

| Drug A | Drug B |
|-|-|
| Smoked at home | Smoked in car |
| Lingering smell on clothing | Smell dissipates quickly|
| Used by 50% of green people | Used by 0% of green people|
| Used by 0% of purple people | Used by 50% of purple people|

Suppose police are race blind, and always search when they smell either drug. There will be more searches of greens than purples, but searches of purples will more often be successful.  (Aside: While the police treat each individual the same one might argue the *policy* to search when smelling drug A is wrong or "racist" since it gives so many false positives and the burden falls on green people. This is a complex issue I'll come back to later.)

3. Sometimes police are suspicious but don't have enough evidence for a mandatory search. In these cases police may ask drivers to agree to ["voluntary" searches](https://www.aclu.org/know-your-rights/stopped-by-police/).  This is (deliberately) phrased in a way that the driver may think it is mandatory. Some races might be less likely to agree to such searches. This would tend to increase the "hit rate" for that race since the searches that do occur tend to happen with strong evidence.

While these effects could distort the data, there's no reason the distortion would be in any particular direction. Such effects could create an illusion of bias when there is none. Or they might be masking even *stronger* bias.

I don't rate these mitigating effects as super strong. They could exist, but they are less plausible than those that could explain the twilight data. It also seems like their effect would be relatively modest.

So, I think this provides moderate evidence in favor of police bias. It's no smoking gun, but it's a glimpse of something that's very hard to see. Also, while it relates to police *bias* it tells us nothing about how that bias relates to police *violence*.

> **Search data**
> * Police find contraband 8-30% more often in searches of whites than blacks and 31-65% more often than hispanics. This is consistent with police applying a higher threshold of evidence to trigger a search of whites.
> * Data could be confounded by different rates of carrying contraband, different rates of giving evidence (or false evidence) of contraband, or different rates of agreeing to "voluntary" searches.

# What would it take?

I can imagine someone who believes police are racially biased grinding their teeth at this point. "Simple ratios show a bias, but you don't believe them. Fine. So you look at the effect of darkness. That *also* shows a bias, but you worry it's confounded. OK! Then you look at search rates. Since you don't believe the bias they show, you check the *hit rate* of searches, which are... biased. Always you invent stories about confounders. What does it take!?"

My response is this: We are making progress. I give *zero* weight to things like number of people killed per capita. The data discussed above isn't totally conclusive, but it definitely should be given *some* value. (In Bayesian terms, you should update your prior in the direction of bias.)

As for what it takes, there's some more data that could help a *lot* with understanding the impact of confounders here. That would be to repeat the analysis with different groupings of people other than race. Does the fraction stopped of drivers who are male change when it's dark? What about the fraction of the old? Those in poverty? Those who are politically conservative? Pick any group that police can't see or don't have a bias around.

If we verified that the fraction of stopped drivers who were old/male/poor/educated/conservative did *not* change with darkness but the fraction who were black *did*, then the confounders probably aren't too much of a problem. (It's possible in principle that race is confound but not these other groups. But since [race is correlated with everything](https://dynomight.net/2020/10/08/police-violence-your-ratios-dont-prove-what-you-think-they-prove/#population-size) I doubt it.)

Of course, analyzing some data is easy! The hard part will be assembling a database of millions of police stops with tags for these other driver attributes. Good luck with that.

---

This post is part of a series on bias in policing with several posts still to come.
* Part 1: [Your ratios don't prove what you think they prove](https://dynomight.net/2020/10/08/police-violence-your-ratios-dont-prove-what-you-think-they-prove/)
* Part 2: **The veil of darkness (This post)**
* Part 3: [Policy proposals and what we don't know about them](https://dynomight.net/2020/11/21/police-violence-policy-proposals-and-what-we-dont-know-about-them/)
* Part 4: [Why fairness is basically unobservable](https://dynomight.net/2020/11/23/police-violence-why-fairness-is-basically-unobservable/)



