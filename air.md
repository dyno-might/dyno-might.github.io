---
layout: post
title: "Air quality is the easiest way to live longer"
image: /img/air/fires3.jpg
tags: cleanAir science
hero_light: false
dark_title: false
background_color: black
description: "Fixing the air you breathe has a higher return on investment than anything else you might do."
permalink: /air/
background_color: rgb(40, 58, 34)
head: "<style>
details{
    }
details summary{
  padding-bottom: 8pt;
}
img{
    display:block;
    margin-left: auto;
    margin-right: auto;
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

What do you worry about more: Getting exercise, eating vegetables, or the air you breathe?

Most of the things that improve health are well known. Eat well, don't smoke, etc. But there's one that's insanely underrated: Fix your air.

Most people don't realize how important this is. I think this stems from a misconception that air pollution only causes lung cancer, which is super rare in nonsmokers.

*Wrong*.

* The number of [number of nonsmokers](https://www.cdc.gov/cancer/lung/nonsmokers/index.htm) who die of lung cancer is similar to the number of people who die in [motor vehicle accidents](https://en.wikipedia.org/wiki/Motor_vehicle_fatality_rate_in_U.S._by_year#Motor_vehicle_deaths_in_U.S._by_year).

* Lung cancer is only around ⅐ of the harms of air pollution. It also causes diabetes, chronic respiratory disease, heart disease and strokes.

Beyond being underrated, I'll make a more grandiose claim: Fixing your air is often **the most effective health intervention, period**. There's nothing else that's so *important* while also being so *easy to address*.

It's good news-- You can buy extra life with minimal cost in money, effort, or willpower! By all means, control your body-mass, eat well, and start [running](https://dynomight.net/2021/01/25/how-to-run-without-all-the-agonizing-pain/). Those are important, but they're also kind of hard. You might fail to lose weight, but if you try to fix your air, you'll succeed.

You should put the stuff with the highest return on effort first, and that's air.

<h2>Sanity Check</h2>

Let's do a sanity check: Take the four biggest countries in the world and compare [how many people](http://ghdx.healthdata.org/gbd-results-tool) died from various causes in 2019.

<img src="/img/air/deaths_horiz.svg" alt="deaths per year per 1000 people from various causes in china, india, the USA, and indonesia" loading="lazy">

These numbers are only for *ambient* air pollution, e.g., due to cars, power plants, and manufacturing. Indoor air pollution comes on top of this.

A better measure than deaths is disability-adjusted life years or [DALYs](https://en.wikipedia.org/wiki/Disability-adjusted_life_year). This is the number of *years* of life lost plus an adjustment for non-lethal conditions that make life worse. For example, schizophrenia is pretty bad, so this counts who becomes schizophrenic for a year as losing half a DALY. This gives a similar picture.

<img src="/img/air/dalys_horiz.svg" alt="DALYs per year per 1000 people from various causes in china, india, the USA, and indonesia" loading="lazy">

<!--
<details>
<summary>If you compare by DALYs instead of deaths, you reach a similar conclusion.</summary>
<img src="/img/air/dalys.svg" alt="DALYs per year per 1000 people from various causes in china, india, the USA, and indonesia">
</details>
-->

<h2>We need numbers</h2>

It's hard to prioritize health advice. I know I should limit salt and eat cruciferous vegetables and do cardio and sleep well and limit alcohol and do strength training and reduce stress and go for regular checkups. But *how much* do these things matter? If I'm a fallible human, what's most important?

For this, we need numbers. In what follows, I've tried to estimate the impact of various lifestyle changes in terms of how they impact DALYs through air quality.

Lifestyle | Life cost
-|-|-
Be a Viking | 4 years 
Live in Delhi | 3 years 
Commute by train from Newark to NYC | ½ year 
Live in an average part of US  | ¼ year 
Breathe second-hand vape smoke | near zero?

These are all rough estimates, but I've put question marks where there's *even more* doubt. We can do the same thing for one-off events.

Single Event | Life cost
-|-|
Live near 2020 US west-coast wildfires | 2.4 days
Have a really smoky fire at home | 1 day 
Burn a cone of incense | 2.3 hours 
Use an ultrasonic humidifier for one night | 50 min?
Broil fish with windows closed | 45 min
Burn a stick of incense | 27 min 
Use hairspray | 14 min
Smoke one cigarette | 11 min
Blow out a candle before sleep | 10 min

<h2>What I recommend</h2>

If you like action more than reading, just do these things in the following order:

1. If you have an ultrasonic humidifier, kill it.
1. Monitor local air quality like the weather.
1. No incense.
1. Extinguish candles with a lid.
1. Be careful about smoke when cooking.
1. Get a particle counter.
1. Use an air purifier at home all the time. (Move this to #1 if the outdoor air is dirty where you live.)
1. Install a HEPA cabin air filter in your car.
1. Avoid aerosols.
1. Use a mask *very carefully* when in dirty air.

A strange list, admittedly, but it's where the evidence seems to lead.

On a societal level, we have *got* to do something about the air in subways. The current plan seems to be to put air purifiers in trains which is slow and expensive and won't really work. The solution is to put purifiers in stations.

<h2>Contents</h2>

* auto-gen TOC:
{:toc}

## Particles and the trouble they cause

### What we're measuring

We measure particles in terms of "PM<sub>2.5</sub>". In theory, you could measure this as follows:

* Take a cubic meter of air.
* Filter out all of the solid particles.
* Keep only the particles that are 2.5 micrometers / microns (μm) or smaller.
* Weigh the remaining particles in micrograms (μg).

The units are μg/m³, since you're weighing particles (in μg) in one m³ of air.

For reference, human hair is around 70 micrometers wide, bacteria are 1 to 10 and viruses are 0.02 to 0.4. The [EPA](https://www.epa.gov/pm-pollution/particulate-matter-pm-basics#PM) gives a helpful visualization:

<img src="/img/air/pmviz.jpg" alt="harms from particulates" loading="lazy">

You can ask: Are all chemicals equal? Is 50 μg/m³ created by burning coal or manufacturing cement or natural dust equally harmful? The answer is *no* (heard of asbestos?) but we don't really know how much these difference matter in practice.

### How particles hurt you

We worry about small particles because they seem most harmful, particularly in terms of how chronic exposure leads to long-term health problems.

These particles do cause lung cancer, but that's one of the *smaller* harms. They also cause chronic respiratory problems. Still, more than half of harms don't come from the lungs at all, but from diabetes and cardiovascular disease. Here are the <a href="http://ghdx.healthdata.org/gbd-results-tool">harms</a> in the US in 2019:

<img src="/img/air/harms.svg" alt="harms from particulates" loading="lazy">

How particles manage to do all this is still a subject of research. The basic story seems to be that the smallest particles can make their way through the lungs and into the bloodstream. These foreign particles then activate your immune system, which sort of goes on a [rampage](2020/12/22/what-i-learned-about-covid-19-from-pestering-a-bunch-of-biologists/), causing all sorts of problems.

Why so much cardiovascular disease? Well, you can probably guess where the blood goes after it leaves the lungs.

<img src="/img/air/heart.svg" alt="heart and lungs" loading="lazy">

### A heuristic to quantify harms

How *much* do particles hurt you? While it's hard to be precise, this section will give two simple heuristics:

* **A life-long exposure of 33.3 PM<sub>2.5</sub> costs 1 DALY**. This is best for lifestyle changes. For example, moving from somewhere with no particulates to somewhere with a level of 100 costs 3 DALY. 
* **At 2500 PM<sub>2.5</sub>, you lose disability-adjusted life in real time.**  This is best for one-off events. For example, if you're exposed to a level of 5000 for 3 hours, you lose 6 disability-adjusted life hours.

Of course, the only way to be *sure* would be to do [randomized experiments](https://dynomight.net/2020/11/23/police-violence-why-fairness-is-basically-unobservable/) where we lock people inside identical environments for their whole lives, vary the particulates they're exposed to, and see how long they live. Since we can't do that, we're left with observational studies.

A [2013 paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3521092/) looked at life expectancies and particle levels in 545 US counties, while controlling for confounding variables like wealth, smoking, and demographics. They found that each 28.5 μg/m³ of particulates costs 1 year (not disability-adjusted.)

Should we trust this number? Most papers focus on public-health questions, but we can extract estimates. A comprehensive [2017 paper](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(17)30505-6/fulltext) estimates the population mean PM<sub>2.5</sub> in different countries, as well as the health costs of ambient air particles. I took their estimates and multiplied them by [the WHO's](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(17)30505-6/fulltext) life expectancy figures to get an estimate of the total DALYs each person loses over a lifetime. Here are particle levels plotted against total DALYs lost.

<img src="/img/air/pm_vs_daly.svg" alt="DALYs per year from different levels of particulates" loading="lazy">

The straight line shows a fit. It suggests that if you are exposed to 33.3 PM<sub>2.5</sub> for your whole life, you'll lose around 1 DALY as a result. I wouldn't put too much faith in this exact number. It varies from country to country, and this is all built upon some very tricky statistics. Still, it's reassuring that different data and  methods lead to a number close to the 2013 paper.

You might ask: Shouldn't the same level of particles cause more harm somewhere where people live longer since they have more time to inhale the particles?

Maybe. I tried relating the particles to the DALY loss in a single year, without multiplying by life expectancy. It suggests that being exposed to 2500 PM<sub>2.5</sub> for one year costs 1 DALY.

<img src="/img/air/pm_vs_daly_each.svg" alt="DALYs per year from different levels of particulates" loading="lazy">

Put another way, if you breathe particles at a concentration of 2500, you double the speed at which you move towards your (disability-adjusted) destiny. If you're exposed to a level of **X × 2500** for **H** hours, then you lose **XH** disability-adjusted life hours.

In practice, this isn't too different from the previous estimate since life expectancies don't vary *that* much between countries.

## Personal exposure

So, we can estimate how much harm particulates do. The next natural question is, how many particles are you exposed to? *Probably* the answer is ambient levels plus some extra that's created indoors, but it's hard to say how large that extra amount is.

### Where people spend their time

There are good records of outdoor levels, but most people aren't outdoors very much. Here's the [NHAPS](https://indoor.lbl.gov/sites/all/files/lbnl-47713.pdf) survey on how Americans spent their time from 1992 to 1994.

<img src="/img/air/nhaps1.svg" alt="where americans send their time" loading="lazy">

<details>
  <summary>No recent survey seems to equal this. They even have curves of where people are throughout the day.</summary>
  <img src="/img/air/nhaps2.jpg" alt="where americans are throughout the day" loading="lazy">
</details>

### Personal vs. outdoor exposure

Are levels indoors the same as outdoors? There's a strong correlation -- particularly if people keep their windows open -- but it varies. Typically, levels indoors are higher than outdoors. [Chen and Zhao](https://doi.org/10.1016/j.atmosenv.2010.09.048) review a bunch of papers that try to estimate the indoor/outdoor (I/O) ratio:

<img src="/img/air/chen_zhao.svg" alt="indoor outdoor particulate ratios" loading="lazy">

None of this really matters though. Indoor levels vary in space and time. What you care about is your *personal* exposure, the air that actually goes into your lungs.

This is hard to study since you have to carry around a measurement device, but it's been done a few times. Early attempts put a small tube near the mouth that passed that air through a filter that was later weighed. More recent studies use devices that measure light scatter.

I couldn't find any good reviews, so I did my own. Here's a comparison of the mean personal and outdoor levels in all the studies I found:

<img src="/img/air/ovp.svg" alt="outdoor vs. personal particulate exposure" loading="lazy">

<details markdown="1">
<summary>You can expand a table with details on all the studies here if you like.</summary>

Here's all the studies I found that try to compare mean personal (P) exposure to indoor (I) or outdoor (O) exposure.

| Study                                                        | Where                   | I     | O     | P     |                                   |
| ------------------------------------------------------------ | ----------------------- | ----- | ----- | ----- | --------------------------------- |
| [Williams 2003](https://doi.org/10.1016/j.atmosenv.2003.09.019) | North Carolina          | 19.1  | 19.3  | 23.0  |                                   |
| [Meng 2005](https://doi.org/10.1038/sj.jea.7500378)          | Los Angeles             | 16.2  | 19.2  | 29.3  |                                   |
|                                                              | Elizabeth, New Jersey   | 20.1  | 20.4  | 46.9  |                                   |
|                                                              | Houston                 | 17.1  | 14.7  | 37.2  |                                   
| [Koutrakis 2005](https://www.healtheffects.org/publication/characterization-particulate-and-gas-exposures-sensitive-subpopulations-living-baltimore) | Baltimore               |       | 20.1  | 15.1  | seniors, winter                   |
|                                                              | Baltimore               |       | 23.2  | 18.6  | children, summer                  |
|                                                              | Boston                  |       | 11.6  | 14.1  | seniors, winter                   |
|                                                              | Boston                  |       | 17.0  | 30.3  | children, summer                  |
| [Sørensen 2005](https://doi.org/10.1038/sj.jea.7500419)      | Copenhagen              | 13.4 | 9.2  | 17.5 | < 8C (median exposure)                              |
|                                                              | Copenhagen              | 9.5  | 7.8  | 11.9 | > 8C (median exposure)                              |
| [Johannesson 2007](https://doi.org/10.1038/sj.jes.7500562)   | Gothenburg, Sweden      | 9.7   | 7.8   | 11.0  |                                   |
| [Suh 2010](https://doi.org/10.1097/jom.0b013e3181e8071f)     | Atlanta                 |       | 17.17 | 15.78 |                                   |
| [Lei 2016](https://doi.org/10.1007/s11356-016-6422-x)        | Shanghai                |       | 94.5  | 110   |                                   |
| [Chen 2018](https://doi.org/10.1016/j.scitotenv.2018.02.049) | Hong Kong               |       | 35.3  | 35.4  | 88% had windows open              |
| [Sanchez 2019](https://doi.org/10.1038/s41370-019-0150-5)    | Villages near Hyderabad |       | 34.1  | 58.5  | Women (half cooked with biofuels) |
|                                                              | Villages near Hyderabad |       | 31.9  | 55.1  | Men                               |

</details>

Personal exposure is strongly correlated with outdoor levels, but typically a bit higher. If you trust the trendline, it predicts that someone with an outdoor level of 50 would have a personal exposure of 62.5.

However, personal exposure is much less predictable than the graph above would suggest. Each point is averaged over many people. Individual studies that broke things down person by person show a huge range.

So, your exposure is probably ambient levels plus some amount that depends on what you do and where you go. To figure that out, we'll have to dig deeper.

## Particles Outdoors

Most particles are introduced by human activity. Common sources are power plants (particularly coal, but also natural gas and oil), factories, human-made fires, cars, and trucks. Natural sources are dust, wildfires, and (oddly) [sea spray](https://en.wikipedia.org/wiki/Sea_spray).

**Variance with respect to city/region- Large:** Levels vary hugely [throughout the world](https://www.who.int/data/gho/data/indicators/indicator-details/GHO/concentrations-of-fine-particulate-matter-(pm2-5)). Estimates vary, but some countries are really low (New Zealand, Canada) and some are an order of magnitude higher (India, Qatar). Different locations inside of countries are correlated partly because of the same air blowing around and partly because of shared emissions controls. Still, if your city has no wind and lots of factories and cars, levels will be higher.

**Variance with respect to location within a city/region- Smallish:** How much variability is there between different places in the same city? The answer seems to be *some*. A [massive study](https://doi.org/10.1016/j.atmosenv.2012.08.038) in various locations in Europe addressed found that particle levels near streets were around 20% higher than urban measurements which were, in turn, around 20% higher than regional measurements.

**Variance with respect to date- Moderate:** At the same location, levels vary throughout the year. Here's the mean concentration in Los Angeles for every day for 20 years, [courtesy of the EPA](https://www.epa.gov/outdoor-air-quality-data/air-data-multiyear-tile-plot).

<img src="/img/air/la.png" alt="pollution in los angeles, 2000-2020" loading="lazy">

You can see the impact of people blowing up fireworks to celebrate their freedom (July 4 every year), everyone staying at home because of a pandemic (March-April 2020), and [massive nearby wildfires](https://en.wikipedia.org/wiki/2020_Western_United_States_wildfire_season) (September 2020).

Incidentally, how much did [those wildfires](https://en.wikipedia.org/wiki/2020_California_wildfires#/media/File:West_coast_wildfires_ESA22200484.jpeg) matter? Many areas saw their levels rise to around 100 for a few weeks and some spiked as high as [200-500](https://www.npr.org/2020/09/23/915723316/1-in-7-americans-have-experienced-dangerous-air-quality-due-to-wildfires-this-ye). As a pessimistic estimate, suppose your levels rose by 200 for a full month. That raises your yearly average by 16.67, which would cost ½ a DALY if it happened every year. If it just happened once, you'd lose 200/2500=.08 months or 2.4 adjusted life days.

**Variance with respect to time of day- Smallish:** At the same location and date, levels change by the hour. [Manning (2018)](https://doi.org/10.1021/acs.estlett.8b00573) combined measurements from 3110 sites around the world to get the following graph.

<img src="/img/air/time_of_day.jpg" alt="particulates by time of day" loading="lazy">

Here, we have a great riddle: Why are levels lowest in the mid to late afternoon? They suggest that "this remarkable global homogeneity in diurnal PM<sub>2.5</sub> cycles suggests the influence of common factors including the diurnal cycle of mixed layer depth modulated by other processes such as diurnally varying emission patterns."

What I *think* this means is this: The sun heats up the earth in the morning. This causes the air near the earth to rise, mixing up the different layers of air. This pulls lots of particles from close to the ground up into the sky, decreasing the density. After the earth cools, the air stops mixing around so much. Also, maybe it has something to do with when people commute and so on.

I'm fascinated by this phenomenon of mixed layer depth but haven't been able to figure out much about it. Does it change throughout the seasons? Is that why wintertime air quality is often worse? I don't know.

## Particles While Commuting

**Driving:** Cars generate lots of particles. If you're driving near lots of other cars particle levels are probably higher than the overall ambient air. A couple of [studies](https://ww3.arb.ca.gov/research/single-project.php?row_id=64724) I saw found levels in the range of 50-100 in cars. Others suggest it's a not so bad and similar to just being outside. It probably depends on your car, traffic, local emissions controls, and weather.

**Walking, biking, and running:** If you're on a street, your exposure is maybe a bit higher than the background, but not a ton. As mentioned above, street measurements are typically a bit higher than urban measurements. If you're biking or running, you're breathing harder. It seems that a typical adult breathes around 15 times per minute but can speed up by a factor of 4 if exercising hard. This might mean that particles accumulate 4 times as fast, but I can't find any clear evidence. 
 
We could estimate the harms from pollution as a result of running or biking, but I won't since exercise also *improves* cardiovascular health, and I don't know how to calculate the tradeoff.

**Riding the subway:** [Luglio (2020)](https://doi.org/10.1289/EHP7202) measured particles for all the major train systems in the northeastern United States. They did measurements in aboveground stations, but this was always low (10-25).

| City                                                         | On Trains | Underground stations |
| ------------------------------------------------------------ | --------- | -------------------- |
| Boston                                                       | 182       | 327                  |
| New Jersey to New York ([PATH](https://en.wikipedia.org/wiki/PATH_%28rail_system%29) trains) | 449       | 779                  |
| New York ([MTA](https://en.wikipedia.org/wiki/Metropolitan_Transportation_Authority) trains) | 343       | 547                  |
| New York to Long Island ([LIRR](https://en.wikipedia.org/wiki/Long_Island_Rail_Road) trains) | 11.6      | 91.2                 |
| Philadelphia                                                 | 55.7      | 112                  |
| Washington DC                                                | 205       | 362                  |

<details markdown="1">
<summary>
For the worst-offending train system, taking take a single trip from Newark, New Jersey to the World Trade Center in New York should cost 7.5 life minutes. Doing that as a commute five days per week would cost 0.56 DALYs.
</summary>

The <a href="https://old.panynj.gov/path/schedules-full-screen-mod.cfm?id=NWK_WTC_Weekday">trip</a> takes 25 minutes. Suppose you spend a combined 10 minutes in the two stations. Your exposure for the hour you do that trip is 779×10/60 + 449×25/60 = 316.9, leading to a cost of 316.9/2500=.126 hours.

There are 10 total trips, each raising your exposure by 316.9 for one hour. This raises your average weekly exposure by 316.9×10/(7×24)=18.86 with a cost 18.86/33.33 = 0.56 DALY.
</details>


[Smith (2020)](https://doi.org/10.1016/j.envint.2019.105188) found that in the London underground, the Victoria line had a median level of 361, the Northern line 194, a couple other around 50, and the rest even lower. The Victoria line is highest because it is entirely underground, meaning that particles have nowhere to go.

[Martins (2015)](https://doi.org/10.1016/j.scitotenv.2014.12.013) reviews many previous studies with found levels over 100 in London, Buenos Aires, Paris, Beijing, New York, Stockholm, Shanghai, Barcelona, and Seoul. There were lower levels in Budapest, Guangzhou, Helsinki, Los Angeles, Mexico City, Taipei, and Sydney.

**Rant:**  Let's face it, these levels are a scandal. Some places are working on it, but progress is slow because it's hard to retrofit trains. Hear me, transit agencies: *Don't retrofit the damn trains.* Just install normal air purifiers in *stations*. Do this because:
* The problem is that particles build up slowly in tunnels with no place to escape. We can solve the problem at the source by slowly removing particles.
* It's *easy* to put static purifiers in stations. You can use standard components.
* The particles in trains are coming from the stations and tunnels.
* People also breathe the air in stations.

Are air purifiers too expensive? Well, the New York subway (MTA) has [275](https://en.wikipedia.org/wiki/New_York_City_Subway_stations#Station_facilities_and_amenities) underground stations. Assume pessimistically that each station needs 50 purifiers, and it costs $1000 each per year to operate them. (The MTA is fond of [vastly overpaying](https://www.slowboring.com/p/make-blue-america-great-again).) The cost would be 13.75 million per year, less than 0.1% of the MTA's [budget](https://new.mta.info/budget/MTA-operating-budget-basics). Seems worth it to avoid exposing millions of people to air five times more hazardous than the most polluted cities in the world.

## Particles Indoors

Suppose you’re inside your home. The quality of the air you breathe can be reduced to five factors:

1. Particle levels outdoors.
2. How long particles hang in the air indoors.
3. The exchange rate between indoor and outdoor air.
4. Stuff you do that creates particles indoors (cooking, candles).
5. Stuff you do to remove particles indoors (running a purifier).

We've covered #1 already. Let's do the rest. 

### How long particles hang in the air

Maybe indoor air is somehow automatically cleaner than outdoor air? Public health guidance to [stay indoors](https://www.epa.gov/indoor-air-quality-iaq/wildfires-and-indoor-air-quality-iaq) during poor air quality suggests this.

Left alone, particles do settle out of the air. With totally still air, this happens deterministically with larger particles falling faster. With real (turbulent) air, particles bounce around until they stick to a surface. This leads to an exponential decay with a rate depending on the particle size and air turbulence. [Experiments](https://medium.com/edge-of-innovation/how-long-do-aerosol-particles-stay-airborne-7c660e089d9b) suggest something like the following:

| Particle size           | half-life with stirred air |
| ----------------------- | -------------------------- |
| 10 μm (largest PM<sub>10</sub>)   | 2 minutes                  |
| 2.4 μm (largest PM<sub>2.5</sub>) | 3 hours                    |
| 1 μm                    | 1 day                      |
| .1 μm                   | 1 month                    |
| .01 μm                  | 1 year                     |

I have trouble determining how much these times depend on air turbulence or if the stirring rate resembles real-world conditions.

### Half-lives of air in homes

Even with all windows closed, air is constantly moving through cracks in the building. Let's quantify this as a "ventilation half-life", the amount of time after which half of indoor air has been replaced from outdoors. In typical homes this seems to range from around 1 to 5 hours. It's longer in more energy-efficient homes and (much) shorter if windows are open.

<details markdown="1">
<summary>
It's more common (and more confusing) to use something called an "air exchange rate".
</summary>

If you search for "air exchange rate" you'll mostly see definitions like "number of air changes per hour". This obviously doesn't make any sense -- there aren't discrete changes. If you search very hard, you can find that the air exchange rate is the constant **a** such that after time **t**, a fraction of **exp( - a t)** of the initial air is remaining. We can solve this for **1/2** to get that the half-life is **t=ln(2)/a=0.693/a**.
</details>

In summary, unless you actively clean the air, indoor levels are probably similar to outdoor levels *plus* whatever particles you generate inside. The air is exchanging fast enough that that by the time particles have fallen out of the air, new particles have come from outside. (However, closed windows should work for larger particles and there might be some benefit to opening/closing your windows based on changing outdoor levels.)

### Exposure with decaying concentrations

To calculate the impact of specific things that generate particles, we'll need a quick calculation. If you generate a puff of smoke with a peak concentration of **c** and a half-life of **h**, levels will fall off slowly over time. What's your total exposure?

The following graph shows a peak concentration of **c=1000** that decays with a half-life of **h=0.2** hours. This turns out to be equivalent (same area-under-the curve) to being exposed to a constant of 288 for 1 hour.

<img src="/img/air/decay.svg" alt="decaying particle levels compared to a constant level" loading="lazy">

Where did 288 come from? The general formula is **1.44 × c × h**. This is natural enough: It's the peak concentration times the half-life times an extra constant because of math. As you'd expect, doubling the peak concentration or half-life doubles the total exposure.

<details markdown="1">
<summary>
The general formula comes from a simple integral.
</summary>
After an amount of time **t** particles have undergone **t/h** half-lives, meaning the total concentration will have decayed by a factor of **(1/2)^(t/h)**, and so the current level is at time **t** is **c×(1/2)^(t/h)**. If we integrate this to get the total exposure, it is **∫c×(1/2)^(-t/h) dt = c × h/ln(2)**. It happens that **1/ln(2)≈1.44**.
</details>

### Things that create particles indoors

**Smoking:** Have you heard? Smoking is bad for you. [Shaw (2020)](https://doi.org/10.1136/bmj.320.7226.53) estimates that one cigarette reduces (non disability-adjusted) life expectancy by 11 minutes, and helpfully points out that this is enough time for "fairly frantic sexual intercourse". Let's move on.

**Vaping:** The following is entirely about *second-hand* vape smoke. (I advise against vaping unless you're doing it to quit smoking.)

It sometimes feels like the public health community is hellbent on destroying vaping, damn the evidence. Sure, I always thought, vaping isn't great, but surely the harm is small?

The vaping community often points to [this report](https://www.cdc.gov/niosh/hhe/reports/pdfs/2015-0107-3279.pdf) from the CDC, which didn't find any problems. However, *they didn't check for particles*. This proves nothing.

Lots of people have measured particles near vaping and found high levels. [Soule (2017)](http://dx.doi.org/10.1136/tobaccocontrol-2015-052772) found levels around 1000 at an e-cigarette conference. [Li (2021)](https://doi.org/10.1016/j.scitotenv.2020.143423) found an average level of 276 in six vape shops in Southern California. [Protano (2020)](https://doi.org/10.3390/ijerph17082947) found that a single person vaping could create levels as high as 1000-10,000. Lots of random people measure particles and report numbers like [600](https://old.reddit.com/r/electronic_cigarette/comments/hsiby6/vaping_and_pm_25_concentrations_toxic/) or [546](https://old.reddit.com/r/Vaping/comments/c4bq47/how_unhealthy_are_pm_25_emissions_from_vaping/) or [1000](https://old.reddit.com/r/electronic_cigarette/comments/k9wyvz/so_my_parents_and_i_ran_a_test_with/). Some report their parents made them do this (good job, parents.)

Vaping enthusiasts retort that the particles are almost all water and [glycerol](https://en.wikipedia.org/wiki/Glycerol) plus a tiny amount of nicotine. [This appears to be true](https://dx.doi.org/10.3390%2Fijerph111111177) -- unlike tobacco smoke, exhaled vape air doesn't contain significantly more phenols or carbonyls (like formaldehyde or [acetone](https://dynomight.net/2020/09/14/what-happens-if-you-drink-acetone/)) than regular exhaled air.

I'm tentatively calling this for Team Vape. In the mountains of papers measuring high particles from vape smoke, few even acknowledge the claim that it's all water and glycerol. Maybe I'm missing something? My idea of an anti-vaping conspiracy has not receded.

**Fireplaces and solid fuels:** Various papers have found that a typical day [living as an 18th century farmer](https://doi.org/10.1016/j.atmosenv.2009.11.045) or [being a Viking](https://doi.org/10.1111/ina.12147) or cooking over an open fire in Guatemala could all lead to average daily particle concentrations around 200. These studies always find insane particle levels near the fire (in the thousands), but these buildings have good ventilation don't spend *that* much time near the worst smoke. This would suggest a loss of around 6 DALYs, though real Vikings might have created less smoke after generations of practice at tending fires.

Still today, there are many people throughout the world who cook indoors with solid fuels (coal/wood). In India, including the harms from household air particulates nearly doubles the (already large) losses that ambient air pollution causes.

How much could it hurt you to have a fire in a fireplace? This depends on many factors: How big is the fire? Is it burning well? How well-ventilated is your home? Do you have a glass panel in front of the fire? How well does the flu for the fireplace draw air?

Let's be *really* pessimistic and imagine that you have a fire that produces a concentration of 25,000 and that this lasts for five hours. This would cost you around 25 disability adjusted life hours. Doing everything right can probably reduce this by 2-3 orders of magnitude. A modern wood stove with tight seals could do even better.

**Cooking:** What about other types of cooking? Again, it all depends. [Kang (2019)](https://doi.org/10.1016/j.scitotenv.2019.02.316) tried cooking various things in 30 different buildings in Korea. On average, soup produced a peak concentration of 65, frying 424, and broiling 1256. Both frying and broiling were hugely variable.

Opening a window reduced the peak concentration to around ⅓ as much. Using a range hood (with or without an open window) reduced it to around ⅐ as much.

And how long do the particles stick around? With no range hood or ventilation, they found a mean half-life of around an hour. (That's actually on the faster end of the ventilation half-lives we talked about above.) With a range hood, the half-life was around 20 minutes. With open windows, it was around 6-7 minutes (regardless of the range hood).

These numbers suggest broiling fish with the windows closed leads to a total loss of around 45 minutes.

**Candles:** Candles produce some particles while burning, but the vast majority of their particles happen in an instant [when the candle is extinguished](https://doi.org/10.4209/aaqr.2019.01.0046). (This is confirmed by [other research](https://doi.org/10.1021/es402429h).) Blowing out a candle causes a spike to around 50-200 with particles hang in the air for 3-5 hours.

<details>
<summary>
Assuming average values, blowing out a candle costs 10 minutes. Doing it every day of your life costs 0.5 years.
</summary>
Take a spike of 100 and assume that the particles hang in the air for 4 hours. Then the cost is 100 × 4 / 2500 = 0.16 hours or 9.6 minutes. 
</details>

The obvious solution is to avoid candles. If that's a nonstarter for you, candles probably aren't that bad, just *don't blow them out*. Instead, extinguish them by putting on an airtight lid.

**Incense:** [One paper](https://doi.org/10.1016/S0048-9697(02)00043-8) suggests that burning an incense stick could produce a peak concentration of around 800, while a [cone](https://en.wikipedia.org/wiki/Incense#Types) might produce a peak concentration of over 4000, with a half-life of around 1.6 hours. 

<details>
<summary>
This suggests burning a cone of incense costs 3.68 hours.
</summary>
Using our half-life formula, the total exposure is 4000 × 1.6 × 1.44 = 9216 particle hours. Thus, the total cost is 9216 / 2500 = 3.68 disability adjusted hours.
</details>

Don't use incense.

**Aerosols:** Some cleaning products create a ton of particles. [One paper](https://doi.org/10.4209/aaqr.2019.01.0046) found that using Febreze caused particles to spike by 50-75, They also found that hairspray could cause a spike of up to 200, with a half-life of 2 hours. These also seem to be exceptionally small particles that hang in the air for a very long time.

<details>
<summary>
This suggests that using hairspray (indoors) has a cost of around 14 minutes.
</summary>
Assume an increase of 200 and a half-life of 2 hours. Then, the total cost is 200 × 2 × 1.44 / 2500 = .23 hours.
</details>

Try to avoid spraying anything into the air. If you really love hairspray, you could use it outside, or in a well-ventilated room right before leaving.

**Humidifiers:** You're not going to like this, but ultrasonic humidifiers produce huge numbers of particles. They turn any minerals in the water become airborne particles. They do this almost by *design*! [Park (2020)](https://dx.doi.org/10.3390%2Fijerph17228638) tested different types of water in a small chamber with a carefully controlled air exchange rate and got the following steady-state increases over background levels.

* Mineral water: ~265
* Tap water (Seoul): ~260
* Purified water: ~50
* Distilled water: ~0

This appears to show that it's not just water particles being counted. Some real-world people report [even higher numbers](https://chemistry.stackexchange.com/questions/105154/why-does-humidifier-put-measurable-pm2-5-in-the-air). I've tested this myself and found the same thing.

<details>
<summary>
This suggests that using an ultrasonic humidifier with tap water at night for 8 hours costs 50 minutes. Doing it every night costs 2.6 years.
</summary>
(Since we're looking at steady-state concentrations rather than peak, we don't consider half-lives.) Your total exposure for one night is 260 × 8 = 2080, with a cost of 2080/2500 = 0.832 hours = 50 minutes. If you do this every night, it raises your mean daily exposure by 260 × 8 / 24 = 86.66 with a cost of 86.66 / 33.33 = 2.6 years.
</details>

Using a humidifier at night is almost as bad as smoking 5 cigarettes!? I was skeptical such large numbers could be real. I read the instruction manuals for a few ultrasonic humidifiers. There were a few passages suggesting they are not unaware of the issue:

* "Use only clean, cool tap water to fill the Water Tank (filtered or distilled water is recommended to avoid white dust if tap water is too hard.)"

* "The best way to minimize mineral build-up is to use distilled or de-mineralized water."

* "IMPORTANT: Using tap water with a high mineral content aka 'hard water' with any humidifier can cause a fine white dust to be emitted. To avoid this, use distilled or demineralized water."

As further evidence, the EPA has a [report](https://www.epa.gov/sites/production/files/2014-08/documents/humidifier_factsheet.pdf) that says, "Recent studies [...] have shown that ultrasonic and impeller (or 'cool mist') humidifiers can disperse materials, such as microorganisms and minerals, from their water tanks into indoor air." They recommend emptying and cleaning the tank *every day* as well as using distilled water.

The EPA emphasizes that there's no proof that these *particular* particles harm health. That's an... interesting... way of looking at things. It might be appropriate logic for a government contemplating a ban, but not for us.  These are huge effects, and you should assume ultrasonic humidifiers are dangerous until there's convincing evidence to the contrary.

In theory, you might try to solve the problem by using distilled water or humidifying a room during the way with the door closed. But don't. What if the humidifier gets dirty? What if particles leak out of the room? What if you have bacteria build up and pollute your water? Are you really going to unplug, clean, and dry the humidifier every time you use it?

Just use an evaporative or steam humidifier, which seem to create almost zero no particles.

**Other random things**

Vacuuming has been reported to cause particles to spike by [50](http://dx.doi.org/10.1080/15459620801901165). Cleaning [dryer lint](https://doi.org/10.1016/j.buildenv.2016.01.008) causes a spike in PM<sub>10</sub> but not PM<sub>2.5</sub>. You can get a small spike by *[making a bed](https://doi.org/10.4209/aaqr.2019.01.0046)*!

Overall, there's no way to avoid creating particles. Almost activity that involves molecules will create *some* particles. In reality, exposure for a small amount of time isn't a big deal. The solution is to avoid the biggest problems and make sure particles are removed from the air quickly enough not to do major harm. You can do this by purifying the air. Or, if you're a lucky person with clean and temperate air outside, you can just keep your windows open.

## What to do

### Try not to create particles indoors.

Above all, kill your ultrasonic air humidifier. Don't burn stuff while cooking. Don't use incense at all ever. Extinguish candles them with a lid. Avoid dangerous cleaning products. If you use hairspray, I guess you could do it outside?

### Monitor outdoor levels.

Most places in the world have real-time particle measurements. You should follow these along with the weather. Some weather websites/apps already include particle counts -- consider using these.

### Get a particle counter.

You can estimate the air exchange rate of your home and the rate your purifier removes particles. You can try to reduce activities that generate particles indoors. But the only way to be sure is to check.

You can get an OK-ish particle counter for $100. Carry it around with you sometimes to check for any nasty surprises. Share it with your friends. We really need better wearable particle counters. Ideally, these should be integrated into watches or phones.

### Use an air purifier inside.

An air purifier in your home has two purposes:

* To reduce the steady-state level of outdoor particles.
* To reduce the half-life of particles you generate indoors.

It turns out that an air purifier reduces both of these by exactly the same fraction. To be more precise, assume

* Your ventilation half-life is **t**, meaning that after this amount of time, half the air in your home has been replaced with outdoor air. (Typical times might be one to five hours.)
* Your purification half-life is **s**, meaning that after this amount of time, your purifier removes half the particles from the air (assuming no ventilation).

When you turn on the purifier, because of math, your total exposure from both indoor and outdoor sources gets multiplied by a factor of

<p style="text-align: center;" markdown="1">

**s / (s + t).** 

</p>

This is intuitive: You want purification to be faster than ventilation, i.e., you want **s < t**. In this case, your total exposure gets multiplied by a small number.

For example, suppose your home has an average ventilation half-life of 120 minutes and that you run a [cuboid air purifier](better-DIY-air-purifier.html) on low, meaning a purification half-life of 15 minutes in a 31 m³ room. Then that purifier reduces your exposure to a fraction of ⅑=15/(15+120) of what it would otherwise be.

While this works for both indoor and outdoor particles, remember that it always helps to open the windows if outdoor levels are currently lower than indoors  -- e.g., because you just burned dinner.

<details markdown="1">
<summary>Because this gets a little bit into the weeds, I'm suppressing the details of how to derive that formula here.</summary>

First let's talk about the steady state. In a fixed amount of time, purifiers remove a fixed fraction of particles from the air, while ventilation will replace a fixed fraction of indoor air with outdoor air. Thus, the more particles, the faster purification works and the less ventilation does. The steady state is when these are equal.

If outdoor levels are **L**, it turns out that the steady-state for indoor levels is **L × s / (s + t).**

For example, suppose outdoor levels are 100, your home has an average ventilation half-life of 120 minutes and that you run a [cuboid air purifier](better-DIY-air-purifier.html) on high, in a medium room, meaning a purification half-life of 7 minutes. Then the steady-state concentration will be 5.5 = 100 × 7 / (7 + 120).

Now let's talk about particles created indoors. Say you generate a bunch of smoke and get a peak concentration of **c**. If particles only go away because of ventilation, your total exposure ends up being **1.44 c t**. Now suppose you have an air filter that would have a half-life of **s** without ventilation. The combined half-life ends up being **st/(s+t)**, so your new exposure is **1.44 c s t / (s+t)**. The ratio of new and old exposure is again **s/(s+t)**.

</details>

### Put a HEPA cabin air filter in your car

One car company hypes the hell out of their air purification system. It's great to raise awareness but... well... most cars made any time in the last 10-20 have cabin air filters which the air goes through before being blown into your face.

These usually aren't HEPA, but you can buy a HEPA version for like $10-$20, and [easily install it yourself](https://howchoo.com/crosstrek/replace-subaru-xv-crosstrek-cabin-air-filter). For most cars you just pull out the glovebox and then slide the filter out. It takes around 5 minutes and requires absolutely no tools.

If you're like most people, you weren't even aware you had a cabin air filter, so it's probably time to replace it anyway. Pay the extra $5 to get one that removes small particles. (This might reduce the air velocity a little.)

### Masks are really tricky

In some parts of the world, it's common to wear masks to reduce the impact of particles. How much is this helping? I don't think anyone really knows. Still, we can make a few conclusive statements:

1. It is possible to use a mask to eliminate the majority of particle exposure (>90 % reduction).

2. Many widely sold masks simply don't perform as advertised, regardless of how they are used.

3. To use a mask successfully, it's paramount to have one that fits your face and to check the fit.

In laboratory tests, researchers buy a bunch of n95 masks, and then carefully attach them to either dummies or real human heads, and then check how well they work.  Optimistically, [Shakya (2016)](https://doi.org/10.1038/jes.2016.42) found two n95 masks both worked well, and even cloth masks did something. [Richard Saint Cyr](http://www.myhealthbeijing.com/children/my-personal-fit-testing-heres-the-best-pollution-mask-for-me/) tried a bunch of masks in China while being very careful about fit and got numbers between 56% and 99%. Some papers ([Cherrie, 2018](http://dx.doi.org/10.1136/oemed-2017-104765); [Pacitto, 2019](http://doi.org/10.1016/j.scitotenv.2018.09.109)) tested a bunch of different masks and found that one or two perform well but the majority achieve remove half of particles or less. Dismally, [Faridi 2020](doi.org/10.1038/s41370-020-0222-6) tried 50 different masks available in Iran and found that *none* did better than 40% and most were much worse.

My guess is that real-world conditions are closer to the bad cases than to the good ones.

What can you do? Two things:

* Refuse to buy any mask without an independent test to prove it works.

* Obsessively fit-test-- a low-quality check is to look at what happens when you inhale or exhale -- is it going around the sides of the mask? But really you want a formal fit test.

A common method for "real" fit-tests is to create an aerosol with saccharin (yes, the artificial sweetener) and check if the mask blocks the smell. [Provenzano (2020)](https://doi.org/10.1101/2020.04.06.20055368) gives some preliminary evidence that you can do this at a low cost.

There's no proven DIY recipe for this yet, but it seems possible. Maybe we can use those damn ultrasonic humidifiers to make the saccharin aerosol. Who knows, maybe some unrelated reason to be interested in masks might come up.

<!--
<details markdown="1">
<summary>Further reading.</summary>


[The NIH: Air Pollution and Your Health](https://www.niehs.nih.gov/health/topics/agents/air-pollution/index.cfm)

[The State of Global Air](https://www.stateofglobalair.org/)

[The Lancet - Estimates and 25-year trends of the global burden of disease attributable to ambient air pollution](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(17)30505-6/fulltext)

[The WHO - Ambient Air Pollution Attributable DALYs](https://www.who.int/data/gho/data/indicators/indicator-details/GHO/ambient-air-pollution-attributable-dalys-(per-100-000-population)) 

</details>
-->