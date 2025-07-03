---
layout: post
title: "Do blue-blocking glasses improve sleep?"
image: /img/blue-light/beach_at_trouville.jpg
tags: 
description: "(are they worth looking like a huge dork?)"
excerpt: ""
permalink: /blue-light/
background_color: rgb(127,167,167)
category: "obsessive investigation"
#seo:
#  date_modified: 2025-06-20
#  last_modified_at: 2025-06-20
comment:
  lemmy: "https://old.lemmy.world/post/32419596"
  substack: "https://dynomight.substack.com/p/blue-light"
head: ""

---

Back in 2017, everyone went crazy about these things:

![goggles](/img/blue-light/goggles.png)

The theory was that perhaps the pineal gland isn't the [principal seat of the soul](https://plato.stanford.edu/entries/pineal-gland/) after all. Maybe what it does is spit out melatonin to make you sleepy. But it only does that when it's dark, and you spend your nights in artificial lighting and/or staring at your favorite glowing rectangles.

You could sit in darkness for three hours before bed, but that would be boring. But—supposedly—the pineal gland is only shut down by *blue* light. So if you selectively block the blue light, maybe you can sleep well and also participate in modernity.

Then, by around 2019, blue-blocking glasses seemed to disappear. And during that brief moment in the sun, I never got a clear picture of if they actually work.

So, do they? To find out, I read all the papers.

## Light and eyes

Before getting to the papers, please humor me while I give three excessively-detailed reminders about how light works. First, it comes in [different wavelengths](https://en.wikipedia.org/wiki/Visible_spectrum).

| Color  | Wavelength (nm) |
| ------ | ------------------ |
| violet | 380–450            |
| blue   | 450–485            |
| cyan   | 485–500            |
| green  | 500–565            |
| yellow | 565–590            |
| orange | 590–625            |
| red    | 625–750            |


![](/img/blue-light/Linear_visible_spectrum.svg)

Outside the visible spectrum, infrared light and microwaves and radio waves have even longer wavelengths, while ultraviolet light and x-rays and gamma rays have even shorter wavelengths. Shorter wavelengths have more energy. Do not play around with gamma rays.

Other colors are hallucinations made up by your brain. When you get a mixture of all wavelengths, you see "white". When you get a lot of yellow-red wavelengths, some green, and a little violet-blue, you see "brown". Similar things are true for pink/purple/beige/olive/etc. (Technically, the original spectral colors and everything else you experience are also hallucinations made up by your brain, but never mind.)

Second, the [ruleset of our universe](https://en.wikipedia.org/wiki/Black-body_radiation) says that all matter gives off light, with a mixture of wavelengths that depends on the temperature. Hotter stuff has atoms that are jostling around faster, so it gives off more total light, and shifts towards shorter (higher-energy) wavelengths. Colder stuff gives off less total light and shifts towards longer wavelengths. The "color temperature" of a lightbulb is the temperature some chunk of rock would have to be to produce the same visible spectrum. Here's a [figure](https://commons.wikimedia.org/wiki/File:Color_temperature_black_body_800-12200K.svg), with the x-axis in kelvins.

![](/img/blue-light/color_temperature.svg)

The sun is around 5800 K. That's both the physical temperature on the surface and the color temperature of its light. Annoyingly, the orange light that comes from cooler matter is often called "warm", while the blueish light that comes from hotter matter is called "cool". Don't blame me.

Anyway, different light sources produce widely [different spectra](https://www.comsol.com/blogs/calculating-the-emission-spectra-from-common-light-sources/).

![A graph of the combined plots of the emission spectra for different light sources.](/img/blue-light/Combined-plot-of-emission-spectra.png)

You can't sense most of those differences because you only have three types of [cone cells](https://en.wikipedia.org/wiki/Cone_cell). Rated color temperatures just reflect how much those cells are stimulated. 

Your eyes probably see the frequencies they do because that's where the sun's spectrum is concentrated. In dim light, cones are inactive, so you rely on [rod cells](https://en.wikipedia.org/wiki/Rod_cell) instead. You've only got one kind of rod, which is why you can't see color in dim light. (Though you might not have noticed.)

Finally, *amounts* of light are typically measured in **lux**. Your eyes are amazing and can deal with [upwards of 10 orders of magnitude](https://en.wikipedia.org/wiki/Lux).

| Situation                     | lux    |
| ----------------------------- | ------ |
| Moonless overcast night       | 0.0001 |
| Full moon                     | 0.2    |
| Very dark overcast day        | 100    |
| Sunrise or sunset             | 400    |
| Overcast day                  | 1,000  |
| Full daylight                 | 20,000 |
| Direct sunlight               | 50,000 |

In summary, you get *widely* varying amounts of different wavelengths of light in different situations, and the sun is *very* powerful. It's reasonable to imagine your body might regulate its sleep schedule based that input.

## Experiments

OK, but do blue-blocking glasses actually work? Let's read some papers.

### Kayumov

[Kayumov et al. (2005)](https://doi.org/10.1210/jc.2004-2062) had 19 young healthy adults stay awake overnight for three nights, first with dim light (<5 lux) and then with bright light (800 lux), both with and without blue-blocking goggles. They measured melatonin in saliva each hour. 

The goggles seemed to help a lot. With bright light, subjects only had around 25% as much melatonin as with dim light. Blue-blocking goggles restored that to around 85%.

![](/img/blue-light/kayumov.png)

I rate this as *good* evidence for a *strong* increase in melatonin. Sometimes good science is pretty simple.

### Burkhart

[Burkhart and Phelps (2009)](https://doi.org/10.3109/07420520903523719) first had 20 adults rate their sleep quality at home for a week as a baseline. Then, they were randomly given either blue-blocking glasses or yellow-tinted "placebo" glasses and told to wear them for 3 hours before sleep for two weeks.

Oddly, the group with blue-blocking glasses had much lower sleep quality during the baseline week, but this improved a lot over time.

![](/img/blue-light/burkhart.png)

I rate this as *decent* evidence for a *strong* improvement in sleep quality. I'd also like to thank the authors for writing this paper in something resembling normal human English.

### Van der Lely

[Van der Lely et al. (2014)](https://doi.org/10.1016/j.jadohealth.2014.08.002) had 13 teenage boys wear either blue-blocking glasses or clear glasses from 6pm to bedtime for one week, followed by the other glasses for a second week. Then they went to a lab, spent 2 hours in dim light, 30 minutes in darkness, and then 3 hours in front of an LED computer, all while wearing the glasses from the second week. Then they were asked to sleep, and their sleep quality was measured in various ways.

The boys had more melatonin and reported feeling sleepier with the blue-blocking glasses.

![](/img/blue-light/van_der_lely1.jpg)

<details markdown="1">
<summary>
However, the sleep quality measurements show no real effect. They are all pretty close in the two groups, sometimes slightly better with the blue-blocking glasses and sometimes slightly worse.
</summary>

![](/img/blue-light/van_der_lely2.jpg)

![](/img/blue-light/van_der_lely3.png)

</details>

I rate this as *decent* evidence for a *moderate* increase in melatonin, and *weak* evidence for *near-zero* effect on sleep quality.

### Gabel

[Gabel et al. (2017)](https://doi.org/10.1038/s41598-017-07060-8) took 38 adults and first put them through 40 hours of sleep deprivation under white light, then allowed them to sleep for 8 hours. Then they were subjected to 40 *more* hours of sleep deprivation under either white light (250 lux at 2800K), blue light (250 lux at 9000K), or very dim light (8 lux, color temperature unknown).

Their results are weird. In younger people, dim light led to more melatonin that white light, which led to more melatonin that blue light. That carried over to a tiny difference in sleepiness. But in older people, both those effects disappeared, and blue light even seemed to cause more sleepiness than white light. The cortisol and wrist activity measurements basically make no sense at all.

![](/img/blue-light/gabel.svg)

I rate this as *decent* evidence for a *moderate* effect on melatonin, and *very weak* evidence for a *near-zero* effect on sleep quality. (I think its decent evidence for a near-zero effect on sleepiness, but they didn't actually measure sleep quality.)

### Esaki

[Esaki et al. (2017)](http://dx.doi.org/10.1080/07420528.2017.1318893) gathered 20 depressed patients with insomnia. They first recorded their sleep quality for a week as a baseline, then were given either blue-blocking glasses or placebo glasses and told to wear them for another week starting at 8pm.

The changes in the blue-blocking group were a bit better for some measures, but a bit worse for others. Nothing was close to significant. Apparently 40% of patients complained that the glasses were painful, so I wonder if they all wore them as instructed.

![](/img/blue-light/esaki.svg)

I rate this was *weak* evidence for *near-zero* effect on sleep quality.

### Shechter

[Shechter et al. (2018)](https://doi.org/10.1016/j.jpsychires.2017.10.015.) gave 14 adults with insomnia either blue-blocking or clear glasses and had them wear them for 2 hours before bedtime for one week. Then they waited four weeks and had them wear the other glasses for a second week. They measured sleep quality through diaries and wrist monitors.

The blue-blocking glasses seemed to help with everything. People fell asleep 5 to 12 minutes faster, and slept 30 to 50 minutes longer, depending on how you measure. (SOL is sleep onset latency, TST is total sleep time).

![](/img/blue-light/shechter.svg)

I rate this as *good* evidence for a *strong* improvement in sleep quality.

### Knufinke

[Knufinke et al. (2019)](https://doi.org/10.1080/17461391.2018.1544278) had 15 young adult athletes either wear blue-blocking glasses or transparent glasses for four nights.

The blue-blocking group did a little better on most measures (longer sleep time, higher sleep quality) but nothing was statistically significant.

![](/img/blue-light/knufinke.svg)

I rate this as *weak* evidence for a *small* improvement in sleep quality.

### Janků

[Janků et al. (2019)](https://doi.org/10.1080/07420528.2019.1692859) took 30 patients with insomnia and had them all go to therapy. They randomly gave them either blue-blocking glasses or placebo glasses and asked the patients to wear them for 90 minutes before bed.

The results are pretty tangled. According to sleep diaries, total sleep time went up by 37 minutes in the blue-blocking group, but slightly decreased in the placebo group. The wrist monitors show total sleep time *decreasing* in both groups, but it did decrease less with the blue-blocking glasses. There's no obvious improvement in sleep onset latency or the various questionnaires they used to measure insomnia.

![](/img/blue-light/janků.svg)

I rate this as *weak* evidence for a *moderate* improvement in sleep quality.

### Esaki (again)

[Esaki et al. (2020)](https://doi.org/10.1111/bdi.12912) followed up on their 2017 experiment from above. This time, they gathered 43 depressed patients with insomnia. Again, they first recorded their sleep quality for a week as a baseline, then were given either blue-blocking glasses or placebo glasses and told to wear them for another week starting at 8pm.

The results were that subjective sleep quality seemed to improve more in the blue-blocking group. Total sleep time went down by 12.6 minutes in the placebo group, but increased by 1.1 minutes in the blue-blocking group. None of this was statistically significant, and all the other measurements are confusing. Here are the main results. I've added little arrows to show the "good" direction, if there is one.

![](/img/blue-light/esaki-again.svg)

These confidence intervals don't make any sense to me. Are they blue-blocking minus placebo or the reverse? When the blue-blocking number is higher than placebo, sometimes the confidence interval in centered above zero (VAS), and sometimes it's centered below zero (TST). What the hell?

Anyway, they also had a doctor estimate the [clinical global impression](https://en.wikipedia.org/wiki/Clinical_global_impression) for each patient, and this looked a bit better for the blue-blocking group. The doctor seemingly *was* blinded to the type of glasses the patients were wearing.

![](/img/blue-light/esaki-again2.svg)

This is a tough one to rate. I guess I'll call it *weak* evidence for a *small* improvement in sleep quality.

### Guarana

[Guarana et al. (2020)](https://gwern.net/doc/zeo/2020-guarana.pdf) sent either blue-blocking glasses or sham glasses to 240 people, and asked them to wear them for at least two hours before bed. They then had them fill out some surveys about how much and how well they slept.

Wearing the blue-blocking glasses was positively correlated with both sleep quality and quantity with a correlation coefficient of around 0.20.

![](/img/blue-light/guarana.svg)

This paper makes me nervous. They never show the raw data, there seem to be huge dropout rates, and lots of details are murky. I can't tell if the correlations they talk about weight all people equally, all surveys equally, or something else. That would make a huge difference if people dropped out more when they weren't seeing improvements.

I rate this as *weak* evidence for a *moderate* effect on sleep. There's a large sample, but I discount the results because of the above issues and/or my general paranoid nature.

### Domagalik

[Domagalik et al. (2020)](https://doi.org/10.3389/fnins.2020.00654) had 48 young people wear either blue-blocking contact lenses or regular contact lenses for 4 weeks. They found no effect on sleepiness. 

![](/img/blue-light/domagalik.svg)

<details markdown="1">
<summary>
They also found that blocking blue light was <em>harmful</em> for attention and working memory.
</summary>

![](/img/blue-light/domagalik2.svg)

</details>

I rate this as *very weak* evidence for *near-zero* effect on sleep. The experiment seems well-done, but it's testing the effects of blocking blue light all the time, not just at night. Given the effects on attention and working memory, don't do that.

### Bigalke

[Bigalke et al. (2021)](https://doi.org/10.1016/j.sleh.2021.02.004) had 20 healthy adults wear either blue-blocking glasses or clear glasses for a week from 6pm until bedtime, then switch to the other glasses for a second week. They measured sleep quality both through diaries ("Subjective") and wrist monitors ("Objective").

The differences were all small and basically don't make any sense.

![](/img/blue-light/bigalke.svg)

I rate this *weak* evidence for *near-zero* effect on sleep quality. Also, see how in the bottom pair of bar-charts, the y-axis on the left goes from 0 to 5, while on the right it goes from 30 to 50? Don't do that, either.

### See also

I also found a couple papers that are related, but don't directly test what we're interested in:

* [Appleman et al. (2013)](https://doi.org/10.1016/j.sleep.2012.12.011) either exposed people to different amounts of blue light at different times of day. Their results suggest that early-morning exposure to blue light might shift your circadian rhythm earlier.

* [Sasseville et al. (2015)](https://doi.org/10.1016/j.physbeh.2015.06.028) had people stay awake from 11pm to 4am on two consecutive nights, while either wearing blue-blocking glasses or not. With the blue-blocking glasses there was more overall light to equalizing the total incoming energy. I can't access this paper, but apparently they found no difference.

## Drumroll

For a synthesis, I scored each of the measured effects according to this rubric:

| Rating | Meaning |
| --- | ----------------- |
| ↑↑↑ | large increase    |
| ↑↑  | moderate increase |
| ↔   | small increase    |
| ↔   | no effect         |
| ↓   | small decrease    |
| ↓↓  | moderate decrease |
| ↓↓↓ | large decrease    |

And I scored the quality of evidence according to this one:

| Rating | Meaning |
| --- | -------------------- |
| ★☆☆☆☆ | very weak evidence |
| ★★☆☆☆ | weak evidence      |
| ★★★☆☆ | decent evidence    |
| ★★★★☆ | good evidence      |
| ★★★★★ | great evidence     |

Here are the results for the three papers that measured melatonin:

| Study                      | Effect on melatonin | Quality of evidence |
| -------------------------- | ------------------- | ------------------- |
| Kayumov                    | ↑↑↑                 | ★★★★☆               |
| Van der Lely               | ↑↑                  | ★★★☆☆               |
| Gabel                      | ↑↑                  | ★★★☆☆               |

And here are the results for the papers that measured sleep quality:

| Study                      | Effect on sleep | Quality of evidence |
| -------------------------- | --------------- | ------------------- |
| Burkhart                   | ↑↑↑             | ★★★☆☆               |
| Van der Lely               | ↔               | ★★☆☆☆               |
| Gabel                      | ↔               | ★☆☆☆☆               |
| Esaki                      | ↔               | ★★☆☆☆               |
| Shechter                   | ↑↑↑             | ★★★☆☆               |
| Knufinke                   | ↑               | ★★☆☆☆               |
| Janků                      | ↑↑              | ★★☆☆☆               |
| Esaki (again)              | ↑               | ★★☆☆☆               |
| Guarana                    | ↑↑              | ★★☆☆☆               |
| Domagalik                  | ↔               | ★☆☆☆☆               |
| Bigalke                    | ↔               | ★★☆☆☆               |

We should adjust all that a bit because of publication bias and so on. But still, here are my final conclusions after staring at those tables:

1. There is **good** evidence that blue-blocking glasses cause a **moderate** increase in melatonin. It could be large, or it could be small, but I'd say there's an ~85% chance it's not zero.

2. There is **decent** evidence that blue-blocking glasses cause a **small** improvement in sleep quality. This could be moderate (or even large) or it could be zero. It might be inconsistent and hard to measure. But I'd say there's an ~75% chance there is *some* positive effect.

I'll be honest—I'm surprised.

## So....

If those effects are real, do they warrant wearing stupid-looking glasses at night for the rest of your life? I guess that's personal.

But surely the sane thing is not to *block* blue light with headgear, but to not create blue light in the first place. You can tell your glowing rectangles to block blue light at night, but lights are harder. Modern LED lightbulbs typically range in color temperature from 2700K for "warm" lighting to 5000 K for "daylight" bulbs. Judging from [this animation](https://commons.wikimedia.org/wiki/File:Black_body_visible_spectrum.gif) that should reduce blue frequencies to around 1/3 as much.

![](/img/blue-light/Black_body_visible_spectrum.gif)

Old-school incandescent bulbs are 2400 K. But to really kill blue, you probably want 2000K or even less. There are obscure LED bulbs out there as low as 1800K. They look *extremely* orange, but candles are apparently 1850K, so probably you'd get used to it?

So what do we do then? Get two sets of lamps with different bulbs? Get fancy bulbs that change color temperature automatically? Whatever it is, I don't feel very optimistic that we're going to see a lot of RCTs where researchers have subjects install an entire new lighting setup in their homes.