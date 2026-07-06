---
layout: post
title: "Life with hazard ratios"
image: /img/hazard-ratios/shooting-the-rapids.jpg
tags: [science, health, math]
description: "Or human-ish"
excerpt: ""
permalink: /hazard-ratios/
#seo:
# date_modified: 2025-11-21
# last_modified_at: 2025-11-21
#comment:
#  substack: "https://dynomight.substack.com/p/blink"
#  lemmy: "https://lemmy.world/post/48678173"
# head: ""

---

If you read anything about health or longevity, you'll soon find yourself in a world of hazard ratios. Some study might say that eating more fiber might change your risk of dying by a factor of HR = 0.90. Another might say that occasional smoking might change it by HR = 1.30.

But how much should you care about that? Is HR = 0.90 or HR = 1.30 a lot? What if you don't *want* to eat more fiber? What if you *like* smoking? Is it worth it?

Instead of a hazard ratio, a better number to look at would be life expectancy.[^1] [^2] But can you convert a hazard ratio to a change in life expectancy? You might reason as follows: Baseline life expectancy is around [75 years](https://en.wikipedia.org/wiki/List_of_countries_by_life_expectancy). And HR = 0.90 corresponds to a 10% decrease in mortality. So perhaps that hazard ratio corresponds to something like 7.5 extra years of life expectancy?

Unfortunately, that's completely wrong.

To see why, imagine that humans only die by playing Russian roulette. They start doing this once per day at the age of 75, with a revolver containing two bullets and six chambers. If you were to remove one of those two bullets, that would drop the person's risk of death by HR = 0.5. (One bullet versus two.) But life expectancy would barely change, because even with just one bullet, almost nobody would survive for any significant amount of time past 75.

For contrast, imagine again that humans only die via Russian roulette, but now they do this once per day from birth with a revolver with 2 bullets and 54,786 chambers. (Newborns emerge and instinctively reach for this gigantic gun.) You can show that these people also live 75 years on average. But now, if you remove one of the bullets (HR = 0.5), life expectancy doubles, because when someone is spared, it takes a long time before they get unlucky again.[^3]

Neither of those is a good model for humans. We're somewhere between the two, with heart disease et al. instead of revolvers and risks slowly rising over time as we get older instead of suddenly turning on at 75 or staying constant throughout life.

But you get the point: If you want to convert a hazard ratio for some intervention to a change in life expectancy, the impact depends on how "spread out" baseline mortality risk is over time. Baseline life expectancy is simply not enough information.

That's one problem. Here's another: What even is a hazard ratio? The technical definition is something like:

> The hazard ratio *at a given time* is the rate of an event in the treatment group divided by the rate of that event in the control group.

Hazard ratios are often confused with their more beloved siblings, relative risks. Say you run a trial for 10 years and at the end, 10% of the control group died, and 8% of the treatment group. Then the relative risk is RR = 0.8. That's nice and simple. But relative risks have problems, most notably that if you run a *long enough* trial, no matter what the intervention is, no one will be alive at the end, and you'll get RR = 1.0, which isn't helpful. Intuitively, you can think of the hazard ratio at age 40 as sort of like the relative risk for people between the ages of 39.99 and 40.01.

In real life, interventions have different hazard ratios at different ages. Chemotherapy tends to have better results in younger patients who are more able to endure the side-effects. Having a slightly higher BMI (25-30 rather than 20-25) is associated with an increased risk of mortality in young people, but a decreased risk in the elderly. You may remember from 2020 that COVID's mortality risk had a different age curve than baseline mortality, meaning the hazard ratio of getting COVID was different at different ages.

This is important, because hazard ratios at different ages have different impacts on life expectancy. A hazard ratio of 0.9 at age 80 prevents more deaths than at age 20, because baseline mortality is higher at 80. But at the same time, if you save the life of a 20 year-old, they have more years in front of them. Beyond that, the hazard ratios at different ages interact: If some intervention decreases mortality at young ages, then that allows more people to reach older ages, increasing the importance of hazard ratios at older ages.

If we knew the hazard ratio at all ages, we could account for those dynamics. But we don't. When estimating hazard ratios, people almost always [assume](https://en.wikipedia.org/wiki/Proportional_hazards_model) that the hazard ratio is constant. We're quasi-forced to do this because there's not enough data to estimate a whole time-series of ratios. That's why papers contain single numbers like HR = 0.90.[^4]

So even though Intervention A (say, more fiber) and Intervention B (say, light jogging) might have the same hazard ratio in a paper, those numbers could be the product of different underlying age-dependent effects, meaning those interventions could conceivably lead to vastly different changes in life expectancy.

So is this all hopeless? Are single hazard ratio numbers just too far removed from what we care about to tell us anything meaningful?

Surprisingly, it's mostly OK. If we were a different species, it might be hopeless. But for modern humans in rich countries, mortality happens to be distributed in a way that produces a kind of lucky coincidence: When people compute scalar hazard ratios for papers, they implicitly aggregate hazard ratios for different ages that approximately reflect their impact on life expectancy.

So, I will argue, even if the hazard ratio isn't constant, it's sorta-mostly OK to take a hazard ratio from a paper, and convert it to a change in life expectancy using this curve.

![dl_vs_hr_log](/img/hazard-ratios/dl_vs_hr_log.svg)

For example, if a paper contains a hazard ratio number HR = 0.75, that corresponds to an increase of around 3.7 years. If a paper contains a hazard ratio of HR = 1.25, that corresponds to a decrease of around 2.9 years.

If the intervention is more helpful for older people (meaning the hazard ratio is lower in older people) then this will tend to overestimate the change in life expectancy. If the intervention is more helpful in younger people, it will tend to underestimate the change in life expectancy. But as long as the hazard ratio doesn't vary *too* much, it's probably not off by more than around 30% in either direction.

## The easy case

Say there's some intervention (eating more fiber or whatever) that multiplies your risk of dying at age *t* by a factor of *HR(t)*. Then it can be shown that this changes life expectancy by approximately

  *ΔL ≈ ∑ₜ ΔHR(t) × P(t) × L(t)*.

Here, *P(t)* is the baseline probability of dying at age *t*. For males in the United States, it looks like this:

![](/img/hazard-ratios/P.png)

Meanwhile, *L(t)* is conditional life expectancy at age *t*. That's the average number of additional years left for someone who reaches age *t*. For males in the United States, it looks like this:

![](/img/hazard-ratios/L.png)

Finally, *ΔHR(t)* is the decrease in hazard at age *t*. You can think of that as just *ΔHR(t) = 1 - HR(t)*. If you're OK with logarithms, there's a somewhat better approximation that uses logarithms, which I've quarantined in a footnote.[^5]

Let's start with the easy case. What if your intervention has the same effect on mortality at all ages, so *HR(t)=HR* is just a constant? Then, the above equation simplifies into

  *ΔL ≈ ΔHR × L̄*, 

where

  *L̄ = ∑ₜ P(t) × L(t).* 

Since *P(t)* (the baseline probability of dying at age *t*) and *L(t)* (conditional life expectancy at age *t*) are constant, *L̄* is just a number. For males in the United States, it happens to be 12.93 years. This quantity has a specific meaning: The average remaining life expectancy for US males when they die. That sounds a bit odd, but think of picking a random death and asking how many additional years people who reach that age live on average. That number is 12.93 years.

So, if an intervention has a constant hazard ratio, the mean change in life expectancy for US males is just

  *ΔL ≈ ΔHR × 12.93* years.

Now we're getting somewhere. If you prevent a fraction *ΔHR* of deaths, then you increase life expectancy by *ΔHR* times 12.93 years.

Now remember the naive calculation we started with: Life expectancy for US males is 75.8 years. You might hope that if eating more fiber drops your risk of death by 10%, that would save 7.58 years. Sadly, the above equation says that a 10% drop in risk only increases life expectancy by around 1.293 years—only 0.17 times as much.

This is essentially the observation Keyfitz made in his 1977 paper, ["What Difference Would It Make if Cancer Were Eradicated?"](https://doi.org/10.2307/2060587) Cancer is responsible for 18 percent of deaths, so does that mean eradicating it would increase lifespan by 18 percent, or around 13.6 years? Nope, Keyfitz says, it's only 2.3 years.

> If a cure for cancer were discovered and made available today, 350,000 cancer deaths would be avoided in the next year. The overall death rate would be lower by nearly 18 percent. If the cure were quick and inexpensive, a large fraction of the country's hospital beds and medical personnel would be released for treatment of other ailments. Patients would be spared untold suffering. Such an implicit analysis underlies government proposals for eradication of cancer. The argument is sound for first effects on mortality but wholly misleading for the long term.
> 
> The first effects would soon be offset by more mortality from diseases other than cancer. As a result of the cancer cures, the population would include a higher proportion of people subject to other causes of death. […]
>
>At the extreme, it might be said that everyone dies of something sooner or later, so that, when the effects of the eradication of cancer had shaken down, the same number of deaths would occur as before, and the only benefit would be the substitution of heart and other diseases for cancer. A cure for cancer would only have the effect of giving people the opportunity to die of heart disease.

Cheerful stuff! We could also write our approximation in terms of baseline life expectancy as

  *ΔL ≈ ΔHR × 0.17 × 75.8* years,

which makes explicit that the change in life expectancy is only 0.17 times as large as a naive estimate. The discount factor of 0.17 is sometimes called the "Keyfitz entropy". You can think of it as measuring how close some population is to playing Russian roulette with 2 bullets in 6 chambers starting at age 75 (a discount factor of just above 0) and playing Russian roulette from birth with 2 bullets and 54,786 chambers (a discount factor of 1.0). It's typically around 0.15 in rich countries today, though it was historically [much higher](https://doi.org/10.1007/s11698-019-00185-y).

Keyfitz entropy is also much higher in other species like mice (perhaps 0.45). You could argue that this explains why nothing that increases lifespan in mice ever seems to translate to humans. Say caloric restriction or whatever produced the same constant hazard ratio in mice and humans. Then it's mathematically guaranteed that the percentage increase in life expectancy will be three times smaller in humans, because Keyfitz entropy is three times smaller in humans. It's harder to increase life expectancy when the baseline mortality distribution is more compressed.[^6]

But that's all assuming the hazard ratio is the same at all ages. Which it surely isn't.

## The interesting case

Here again is our equation for the change in life expectancy in response to taking some action that changes the risk of mortality at age *t* by a factor of *HR(t)*:

  *ΔL ≈ ∑ₜ ΔHR(t) × P(t) × L(t)*,

Basically, for each age *t*, we multiply three numbers together:

1.  *ΔHR(t)* is the decrease in the chance of dying at age *t* as a result of whatever intervention you've made (e.g. eating more fiber). This reflects that larger decreases in risk lead to larger increases in life expectancy.
2. *P(t)* is the baseline probability of dying at age *t*. This reflects that the hazard ratio is a *ratio*, so you prevent more deaths when you apply a ratio to ages where the baseline rate is higher.
3. *L(t)* is conditional life expectancy at age *t*. This reflects that you miss out on more years of life if you die when you're young.

Now notice: The impact of a change *ΔHR(t)* at age *t* is the product of the baseline risk of death *P(t)* and remaining life expectancy *L(t)*. So what really matters is their product, *P(t) × L(t)*:

![](/img/hazard-ratios/L_times_P.png)

This shows how sensitive life expectancy is to changes in hazard ratios at different ages. It would be nice if this were constant. Then, the shape of *HR(t)* wouldn't matter at all, only the average value. That's not quite true, but it's not terribly far from being true.

An equivalent way of writing our equation for the change in life expectancy is

  *ΔL ≈ avg(ΔHR) × L̄*, 

where *L̄* is still mean life expectancy at death (*L̄ = 12.93* years for US males) and *avg(ΔHR)* is the average change in hazard, weighted by the *P(t) × L(t)* sensitivity curve at different ages.[^7] While that sensitivity curve isn't constant, it's not too curvy, either. Intuitively, it gives a lot of weight to ages between 50 and 90, somewhat less weight to ages between 20 and 50, and little weight to other ages.[^8]

So that's not too bad. But let's remember our original problem: You see some number like HR = 0.90 in a paper, and you want to convert it to a change in life expectancy. If the true underlying hazard ratio were constant, that would be fine. But if it's not constant, then what does that HR = 0.90 number even mean?

## Numbers in papers

Unfortunately, you almost never get to see the underlying time-dependent *HR(t)*, because there's almost never enough data to estimate it. And you almost never get to see the weighted average *avg(ΔHR)*. What you get is some number in a paper. Let's call that number *est(HR)*. The obvious thing to do would be to plug the change into the above equation in place of *avg(ΔHR)* and approximate the change in life expectancy as

&nbsp;&nbsp;*ΔL ≈ est(ΔHR) × L̄*.

Again, you can just think of *est(ΔHR) = 1-est(HR)* as being the estimated reduction in hazard, although it's better to use logarithms if you're willing to use logarithms.[^9] So the question is: Will that be accurate? How close are *est(ΔHR)* and *avg(ΔHR)*?

Well, how do people actually estimate those hazard ratio numbers in papers? *Somehow* they're aggregating information about hazards at different ages into a single number. But how? It's quite [complicated](https://en.wikipedia.org/wiki/Proportional_hazards_model). But if there's a lot of data, you can show that the estimated scalar hazard ratio is approximately[^10]

&nbsp;&nbsp;*est(HR) ≈ Πₜ HR(t)ᵖ⁽ᵗ⁾.*

That is, the estimated hazard ratio is the geometric average of age-dependent hazard ratios, weighted by the probability of dying at each age. It follows[^11] that the estimated *change* in hazard is approximately

&nbsp;&nbsp;*est(ΔHR) ≈ ∑ₜ P(t) ΔHR(t)*.

So now we see the key difference. Ideally, we'd compute *avg(ΔHR)*, which averages the changes *ΔHR(t)* based on the weights *P(t) × L(t)*. But we can't do that, because we don't have access to the *ΔHR(t)* numbers. What you can do is read a hazard ratio number in a paper, and compute *est(ΔHR)*. The above equation says that if you do that, you are *implicitly* (and approximately) averaging the changes *ΔHR(t)* based on the weights *P(t)* alone.

The weights used by *avg(ΔHR)* and the weights implicitly used by *est(ΔHR)* aren't the same. But they're not *that* different. Here's *P(t) × L(t)*, the weights that we'd like to use to compute *avg(ΔHR)* and estimate changes in life expectancy accurately:

![](/img/hazard-ratios/L_times_P.png)

And here's *P(t)*, the weights we are implicitly using if we take a hazard ratio from a paper and compute *est(ΔHR)*.

![](/img/hazard-ratios/P.png)

They're different. In particular, *P(t)* gives more weight to people aged 80-100 and less weight to people aged 20-50. But they're not terribly different.

## Enough math, let's try it

To start, imagine some intervention that decreases risk by *HR(t)=0.9* for all ages.

![](/img/hazard-ratios/hr_curve_0.9.svg)

Here are the results:

| Thing                    | Formula              | Years   |
| ------------------------ | -------------------- | ------- |
| Original life expectancy | *L*                  | 75.7769 |
| New life expectancy      | *L'*                 | 76.4127 |
| Exact ΔL                 | *ΔL = L - L'*        | 0.6358  |
| Ideal approximation      | *ΔL ≈ avg(ΔHR) × L̄* | 0.6409  |
| Use number from paper    | *ΔL ≈ est(ΔHR) × L̄* | 0.6409  |

Let me explain what's happening here. I made a [simulator](/img/hazard-ratios/simulator.html) that takes [actuarial data](https://www.ssa.gov/oact/STATS/table4c6.html) for how likely US males are to die at various ages. From this, it's easy to estimate life expectancy *L*.[^12] Then I applied a hazard ratio to change the probability of dying at each age, and re-ran the simulator to compute a new life expectancy *L'* and the exact difference *ΔL*. Then I'm showing two approximations: The first is the "ideal approximation" using *avg(ΔHR)*. I'm including this to show that it's close to *ΔL* and thus that my math is good. Finally, I'm showing an approximation based on actually fitting a Cox proportional hazards model and plugging in the number to get *est(ΔHR)*. This corresponds to what you'd get if you plug in a number from a paper.

With the above constant ratio, you can see that the approximation is extremely good. That remains true if you use some other constant instead of HR = 0.90.

What if the hazard ratio varies? You might think that something like this would be problematic:

![](/img/hazard-ratios/hr_curve_sin.svg)

But it's basically fine:

| Thing                    | Formula              | Years   |
| ------------------------ | -------------------- | ------- |
| Original life expectancy | *L*                  | 75.7769 |
| New life expectancy      | *L'*                 | 77.4373 |
| Exact ΔL                 | *ΔL = L - L'*        | 1.6604  |
| Ideal approximation      | *ΔL ≈ avg(ΔHR) × L̄* | 1.7451  |
| Use number from paper    | *ΔL ≈ est(ΔHR) × L̄* | 1.7121  |

The reason this is fine is that the changes in the hazard ratio are "high frequency", meaning they sort of locally average out. To demonstrate that, suppose the hazard ratio is chosen randomly for each 1-year bin:

![](/img/hazard-ratios/hr_curve_random.svg)

| Thing                    | Formula              | Years   |
| ------------------------ | -------------------- | ------- |
| Original life expectancy | *L*                  | 75.7769 |
| New life expectancy      | *L'*                 | 77.4218 |
| Exact ΔL                 | *ΔL = L - L'*        | 1.6449  |
| Ideal approximation      | *ΔL ≈ avg(ΔHR) × L̄* | 1.7059  |
| Use number from paper    | *ΔL ≈ est(ΔHR) × L̄* | 1.7123  |

What really causes trouble is when the hazard ratio systematically varies between young and old people. For example, suppose the intervention does nothing for people who are young but is gradually more helpful as you get older:

![](/img/hazard-ratios/hr_curve_random.svg)

Now, my ideal approximation would still be pretty accurate (if you could compute it) but plugging in a number from a paper leads to an overestimate.

| Thing                    | Formula              | Number        |
| ------------------------ | -------------------- | ------------- |
| Original life expectancy | *L*                  | 75.7769 years |
| New life expectancy      | *L'*                 | 77.9031 years |
| Exact ΔL                 | *ΔL = L - L'*        | 2.1261 years  |
| Ideal approximation      | *ΔL ≈ avg(ΔHR) × L̄* | 2.0962 years  |
| Use number from paper    | *ΔL ≈ est(ΔHR) × L̄* | 2.7645 years  |

This happens because *est(ΔHR)* is implicitly weighted by *P(t)* which is heavily biased towards older people, whereas we'd like to use something more like *avg(ΔHR)* which is less biased towards older people. But even so, the error isn't terrible.

It *is* possible that plugging in a hazard ratio from a paper could give wildly inaccurate estimates of life expectancy. One case would be an intervention which is amazing for people aged 85-95, but does very little for anyone else:

![](/img/hazard-ratios/hr_curve_worst.svg)

Now, the hazard ratio looks good exactly at the point where *est(ΔHR)* has the most weight, leading it to greatly overestimate the impact on life expectancy:

| Thing                    | Formula              | Number        |
| ------------------------ | -------------------- | ------------- |
| Original life expectancy | *L*                  | 75.7769 years |
| New life expectancy      | *L'*                 | 76.1741 years |
| Exact ΔL                 | *ΔL = L - L'*        | 0.3972 years  |
| Ideal approximation      | *ΔL ≈ avg(ΔHR) × L̄* | 0.3840 years  |
| Use number from paper    | *ΔL ≈ est(ΔHR) × L̄* | 1.0989 years  |

Another nightmare case is an intervention that starts out harmful, but then switches to being helpful at older ages:

![](/img/hazard-ratios/hr_curve_switch.svg)

In this case, using a number from a paper doesn't even give the right sign.

| Thing                    | Formula              | Number        |
| ------------------------ | -------------------- | ------------- |
| Original life expectancy | *L*                  | 75.7769 years |
| New life expectancy      | *L'*                 | 75.5006 years |
| Exact ΔL                 | *ΔL = L - L'*        | -0.2764 years |
| Ideal approximation      | *ΔL ≈ avg(ΔHR) × L̄* | -0.2348 years |
| Use number from paper    | *ΔL ≈ est(ΔHR) × L̄* | +0.2709 years |

That is bad. But I think most interventions probably aren't like that? My guess is that most real interventions vary *somewhat* with age, but they do so gradually and without switching sign. In those cases, it's quite difficult to find cases where plugging in the number from a paper is off by more than 30% or so.

## TLDR

If we were another species, it might be very hard to convert from hazard ratios to changes in life expectancy. But for modern people in rich countries, there are three lucky coincidences:

1. Mortality risk happens to be distributed so that you can approximate changes in life expectancy through a simple weighted sum of hazard ratios at different ages, ignoring interactions.
2. The statistical method that people use to estimate scalar hazard ratios can also be approximated as a weighted sum of hazard ratios at different ages, ignoring interactions.
3. The weights that you need to estimate life expectancy (from #1) and the weights that are implicitly used to compute hazard ratio numbers (from #2) aren't the same. But they're fairly close.

These facts justify taking an estimated hazard ratio number from a paper and approximating the change in life expectancy as *ΔL ≈ ln(1/HR) × 12.93* years or, if the hazard ratio is close to one and you hate logarithms, as *ΔL ≈ (1-HR) × 12.93* years.

![dl_vs_hr_both](/img/hazard-ratios/dl_vs_hr_both.svg)

The number 12.93 years is for US males. It's the product of Keyfitz entropy (0.17) and baseline life expectancy (75.8 years). It will vary a bit in other populations.

If the true underlying hazard ratio:

* …is constant across ages, then the above approximation will be extremely good.
* …decreases as people get older, that approximation will overestimate *ΔL*. That is, it will make helpful interventions look better than they actually are, and it will make harmful interventions look less bad than they actually are.
* …increases as people get older, that approximation will underestimate *ΔL*. It will make helpful interventions look less good than they actually are, and it will make harmful interventions look worse than they actually are.

But as long as the true underlying hazard ratio isn't *too* wacky, there's probably not more than ~30% error in either direction.

Finally, two major caveats: First, the above calculation assumes that the hazard ratio was estimated by running a trial on people of all ages. In general, *est(ΔHR)* implicitly gives weight to different ages proportional to how many deaths occur at those ages in the baseline population in the trial. If there's a minimum age of, say 50 years old, that won't change much because almost all the mass of *P(t)* is above the age of 50. But if there's a minimum age of 70, or a *maximum* age of 50, that could make a huge difference.

Second, these are estimates for life expectancy *for a population*. But you are not a population. In some sense, your genetics and lifestyle mean you have your own individual Keyfitz entropy, reflecting how spread out mortality would be for you if you led a million random lives. If you drive safely and use an air purifier and eat well and get exercise and don't smoke, that likely means your personal life expectancy is higher than average, but also that your personal Keyfitz entropy is lower than average. So, even if eating more fiber or whatever produced the same hazard ratio for you as everyone else, it would likely lead to smaller changes in life expectancy, for the same reason the same hazard ratio produces smaller changes in lifespan in humans compared to mice. What we really need is some interventions strong enough to get down into the nonlinearity of the logarithm and break the math.

---

[^1]: ![](/img/hazard-ratios/house.png)  

[^2]: I know, I know, you care about quality of life, not just years of life. I agree, some number that measures health and vitality, maybe disability-adjusted life years or quality-adjusted life years, would be better. But these are hard to estimate and so are rarely reported. Anyway, in practice most interventions that make you more vital tend to make you live longer and vice versa, so focusing on life expectancy isn't too bad.

[^3]: In this model, the number of days of life follows a geometric distribution with *p* = (number of bullets) / (number of chambers). So the mean life expectancy is *1/p* days or (number of chambers) / (number of bullets) days. With 54,786 chambers and 2 bullets, that works out to 75 years. And if you drop down to one bullet, then it increases to 150 years.

[^4]: If some intervention would have reduce mortality among people aged ≥ 60 in prehistorical tribal bands, that wouldn't have increased life expectancy very much, because most people didn't make it to 60. But compared to prehistorical tribal bands, we *have* in fact vastly reduced mortality at younger ages. And so, today, reducing mortality for people aged ≥ 60 will increase life expectancy a lot.

[^5]: You might think this is stupid. Why change a relative risk into a hazard ratio if you're just going to assume it's constant? Isn't that pointless? Well, no. Remember how relative risks always go to 1.0 for long enough trials as everyone in both the treatment and control groups departs our coil? That doesn't happen with constant hazard ratios.

[^6]: It's usually (though not always) better to use ΔHR(t) = ln(1/HR(t)). This correctly reflects, for example, that if all hazard ratios go to zero, then life expectancy goes to infinity, yay. These two approximations are almost identical for hazard ratios that are close to one because *ln(1/r) ≈ (1-r)* when *r* is close to one. So if you *are* terrified of logarithms but you've made it to the end of this footnote anyway, you're not missing out on too much.

[^7]: There's a degree of circularity to this argument. It assumes that hazard ratios transfer better between species than changes in life expectancy. That might be true, but it would be an empirical / biological fact, not something that's guaranteed by logic.

[^8]: To see this, note that *ΔL ≈ ∑ₜ ΔHR(t) × P(t) × L(t) = L̄ × ∑ₜ ΔHR(t) × (P(t) × L(t) / L̄) = L̄ × avg(ΔHR)*.

[^9]:  A pretty decent approximation turns out to be
	
	*avg(ΔHR) ≈ 0.27 × avg₂₀₋₅₀(ΔHR) + 0.73 × avg₅₀₋₉₀(ΔHR)*,

	where *avg₂₀₋₅₀(ΔHR)* represents a flat average of the change over the ages 20 to 50 and avg₅₀₋₉₀(ΔHR) represents a flat average over the ages 50 to 90.

[^10]: That is, it's better to use *est(ΔHR) = ln(1/est(HR))*. This is close to *1-est(HR)* when *est(HR)* is close to one.

[^11]: If there is an infinite amount of data, the typical method reduces to solving
	
	*∑ₜ (P(t) + P'(t)) × π(t, HR) = ∑ₜ P'(t)*,

	for *HR*. Here,  *P'(t)* is the chance of dying at age *t* after the hazard ratio has been applied, and *π(t, HR)* is the probability that, if a death occurred at time *t*, it was in the treatment group. Of course, the *true* probability that a death is in the treatment group is

	*P'(t) / (P(t) + P'(t))*.

	The standard "proportional Cox" model assumes that the hazard ratio is constant and so replaces this raw fraction with a model-based one, namely

	*π(t, HR) = S'(t) × HR / (S(t) + S'(t) × HR)*.

	This reflects the fact that at age *t*, a fraction *S(t)* of controls are alive and each of these have some chance *μ(t)* of dying, so *P(t)=S(t) × μ(t)*. Meanwhile, a fraction *S'(t)* of the treatment group is alive, and these each have a chance *HR × μ(t)* of dying, meaning that *P'(t) = S'(t) × HR × μ(t)*. If you substitute these equations for *P(t)* and *P'(t)* into the second equation above, the factor of μ(t) conveniently cancels and you get π(t, HR) as written. 

	In effect, the hazard ratio's job is to attribute deaths to the treatment versus the control group. Now, if the *true* time-varying *HR(t)* is close to one, then it [can be shown](https://baselbiometrics.github.io/home/docs/talks/20160428/7_Stone.pdf) that the estimated hazard ratio *est(HR)* approximately satisfies

	*ln(est(HR)) ≈  ∑ₜ P(t) ln(HR(t))*.

[^12]: The geometric average is equivalent to the condition that
	
	*ln(est(HR)) ≈ ∑ₜ P(t) ln(HR(t))*  

	Using the "better" approximation that *ΔHR(t) = ln(1/HR(t))* and *est(ΔHR)=ln(1/est(HR)), it follows that 

	*est(ΔHR) ≈  ∑ₜ P(t) ΔHR(t)*.

	You can justify interpreting that same equation using *est(ΔHR) = 1-est(HR)* and *ΔHR(t)=1-HR(t)* from the fact that these are almost the same when *HR(t)* is close to one.

[^13]: This simulator pretends that people live for integer numbers of years. That's not true in reality, of course, but it makes the simulator easier to implement and understand and makes little difference in practice.

[^14]: In the simulation, "true ΔL" is what I called "exact ΔL" above, while "approximation (log)" is what I called "ideal approximation" and "Cox fitted" is what I called "Use number from paper".

[^15]: The way modern human mortality is distributed, even if your healthy lifestyle were to reduce mortality by a constant factor at all ages, that still has the effect of decreasing Keyfitz entropy.