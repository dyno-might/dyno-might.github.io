---
layout: post
title: Your ratios don't prove what you think they prove
image: /img/police/court_light_cropped.jpg
description: Why trying to measure police violence though ratios is totally and utterly meaningless.
tags:
  - policy
  - math
usemathjax: true
permalink: /:year/:month/:day/:title/
category: politics/policy
---

Watching people discuss police bias statistics, I despair. Some claim simple calculations prove police bias, some claim the opposite. Who is right?

No one. Frankly, nobody has any clue what they are talking about. It's not that the statistics are *wrong* exactly. They just don’t prove what they’re being used to prove. In this post, I want to explain why, and give you the tools to dissect these kinds of claims.

I've made every effort to avoid politics, due to my [naive dream](https://dynomight.net/2020/09/29/doing-discourse-better-stuff-i-wish-i-knew/) where well-meaning people can agree on facts even if they don't agree on policy.

## Population size

The obvious place to start is to look at the number of people killed by police. This is easy to find.

| |Black|White|Hispanic|
|-|-|-|-|
|# in US (million)| 41.3 | 185.5 | 57.1 |
|# killed by police per year| 219 | 440 | 169 |
|# killed by police per million people | 5.3 | 2.3  | 2.9 |

Does this prove the police are racist? Before you answer, consider a different division of the population.

| |Male|Female|
|-|-|-|
|# in US (million) | 151.9 | 156.9 |
|# killed by police per year| 944 | 46 |
|# killed by police per million people | 6.2 | 0.29 |

And here's a third one.

| |<18 y/o|18-29|30-44|45+|
|-|-|-|-|-|
|# in US (million) | 72.9  | 53.6 | 63.2 | 137.3|
|# killed by police per year| 19  |  283 | 273 |  263 |
|# killed by police per million people | 0.26  | 5.2  | 4.3  | 1.9 |

The first table above is often presented as an obvious "smoking gun" that proves police racism with no further discussion needed. But if that were true, then the second would be a smoking gun for police *sexism* and the third for police *ageism*. So let's keep discussing.

Of course, the second and third tables have obvious explanations: Men are different from women. The young are different from the old. Because of this, they interact with the police in different ways. Very true! But the following is also true:

| |Black|White|Hispanic|
|-|-|-|-|
|average height (men) | 175.5cm (5'9") | 177.4cm (5'10)  | 169.5cm (5'7") |
|life expectancy | 74.9 yrs | 78.5 yrs | 81.8 yrs |
|mean annual income | $41.5k | $65.9k | $51.4k |
|median age | 33 yrs | 43 yrs | 28 yrs |
|go to church regularly | 65% | 53% | 45%|
|children in single-parent homes | 65% | 24% | 41% |
|identify as LGBT | 4.6% | 3.6% | 5.4% |
|live in a large urban area | 82% | 61% | 82% |
|poverty | 21% | 8.1% | 17%|
|men obese  | 41% | 44% | 45% |
|women obese  | 56% | 39% | 43% |
|completed high school | 87% | 93% | 66% |
|completed bachelor's | 22% | 36% | 15% |
|heavy drinkers | 4.5% | 7.1% | 5.1% |

Maybe it's uncomfortable, but it's a fact: In the US today, there are few traits where there *aren't* major statistical differences between races. (Of course this doesn't mean these differences are *caused* by race! This is a good example of why correlation does not imply causation.)

## A thought experiment

Suppose police were required wear augmented reality goggles. On those goggles, real-time image processing changes faces so that race is invisible. Would doing this cause police statistics to equalize with respect to race?

No. Even if race is *literally invisible*, young urban alcoholics will have different experiences with police than old teetotalers on farms. The fraction of these kinds of people varies between races. Thus, racial averages will still look different because of things that are *associated with race* but aren't *race as such*.

So despite the thousands of claims to the contrary, just looking at killings as a function of population size doesn't prove bias. Not does it prove a lack of bias. It really doesn't prove anything.

## Arrests

Why do police kill more men than women? We can't rule out police bias. But surely it's relevant that men and women behave differently? So, it might seem like we should normalize not by population size, but by *behavior*.

One popular suggestion is to consider the number of arrests:

| |Black|White|Hispanic|
|-|-|-|-|
|# killed by police per year| 219 | 440 | 169 |
|# arrests for violent crimes per year (thousands) | 146 | 230 | 83 |
|# killed by police per thousand violent crime arrests | 1.4 | 1.9 | 1.9 |

Some claim this proves the police *aren't* biased, or even that there is bias in favor of blacks. But that's nearly circular logic: If police are biased, that would manifest in arrests as much as killings. So what we are really calculating above is

$$ \frac{\text{“Normal” killings + killings due to bias}}{\text{“Normal” arrests + arrests due to bias}}.$$

The ratio doesn't tell you much about how large the bias terms are. So, unfortunately this also doesn't prove anything.

Incidentally: There are some [popular but different](https://twitter.com/leonydusjohnson/status/1267466345844740098) numbers out there for this same ratio. These have tens of thousands of re-tweets with no one questioning the math. But I've checked the source data carefully, and I'm pretty sure my numbers are right. (They reach the same basic conclusion anyway.)

## Murders

The police have discretion when deciding to make an arrest. But a dead body either exists or doesn't. So why not normalize by the number of murders committed?

This turns out to be basically impossible:
* Something like 40% of murders go unsolved, so the race of the murderer is unknown.
* The only real source of murder statistics is the [FBI](https://ucr.fbi.gov/crime-in-the-u.s/2018/crime-in-the-u.s.-2018/tables/expanded-homicide-data-table-6.xls). They treat hispanic/non-hispanic ethnicity as *independent* of race. Why not just ignore hispanics then? Well, you can't. Hispanics are still counted as white or black in an unknown way. It's impossible to compare to police shooting statistics where hispanic is an alternative race.
* In around 31% of cases, the FBI has [no information](https://ucr.fbi.gov/crime-in-the-u.s/2017/crime-in-the-u.s.-2017/tables/expanded-homicide-data-table-3.xls) about race, and in 40% of cases, no information about ethnicity. 

I've seen tons of articles use [this version](https://ucr.fbi.gov/crime-in-the-u.s/2018/crime-in-the-u.s.-2018/tables/expanded-homicide-data-table-6.xls) of the FBI's murder data that simply drops all the cases where data are unknown. None of these articles even acknowledge the issue of missing data or different treatment of hispanics.

Instead, let's look at murder *victims*. This is counterintuitive, but it's [relatively rare](https://ucr.fbi.gov/crime-in-the-u.s/2018/crime-in-the-u.s.-2018/tables/expanded-homicide-data-table-6.xls) for murders to cross racial boundaries (<20%). So this is a non-terrible proxy for the number of murders committed. Data from the CDC separates out black, white, and hispanics in a similar way as police shooting statistics.

| | Black | White | Hispanic|
|-|-|-|-|
|# killed by police per year| 219 | 440 | 169 |
|# murder victims per year | 9,908 | 5,747 | 3,186 |
|# killed by police per murder victim | 0.022 | 0.076 | 0.053 |

So what does this prove? Again, not much. The simple fact is that most police killings are **not in the context of a murder or a murder investigation**. Though there are [exceptions](https://medcraveonline.com/FRCIJ/FRCIJ-06-00237.pdf), the precise *context* of police killings hasn't had enough study, and definitely not enough to get reliable statistics.

## Ratios are hopeless

Really, though, it's not an issue of lacking data. Philosophically, consider the any possible ratio like

$$ \frac{\text{# of people of a race killed by police}}{\text{# of times act } X \text{ committed by a member of a race}}.$$

For what act $$X$$ does this really measure police bias? I think it's pretty clear that **no such act exists**, even if we could measure it. Races vary along too many dimensions. There are too many scenarios for police use of force. Bias interacts with the world in too many ways. You just can't learn anything meaningful with these sort of simplistic high-level statistics.

This doesn't mean we need to give up. It just means you need to get closer and try harder. In the next part of this series I'll look at some valiant attempts to do that. They will disappoint us too, but for different reasons.

**Data Used:**
* [Police shootings](https://www.washingtonpost.com/graphics/investigations/police-shootings-database/) (average 2017-2019)
* [Number of people of each race / sex](https://www.census.gov/quickfacts/fact/table/US/PST045219)
* [Number of people by age](https://data.census.gov/cedsci/table?q=S01&d=ACS%201-Year%20Estimates%20Subject%20Tables&tid=ACSST1Y2019.S0101)
* Data by race: [Life expectancy](https://www.cdc.gov/nchs/data/nvsr/nvsr68/nvsr68_07-508.pdf) / [Income](https://en.wikipedia.org/wiki/List_of_ethnic_groups_in_the_United_States_by_household_income) / [Height](https://www.medicinenet.com/height_men/article.htm) / [Church](https://news.gallup.com/poll/248837/church-membership-down-sharply-past-two-decades.aspx) / [Single-parent homes](https://datacenter.kidscount.org/data/tables/107-children-in-single-parent-families-by-race#detailed/1/any/false/37,871,870,573,869,36,868,867,133,38/10,11,9,12,1,185,13/432,431) / [Identifying LGBT](https://news.gallup.com/poll/201731/lgbt-identification-rises.aspx) / [Median age](https://www.pewresearch.org/hispanic/2016/04/20/the-nations-latino-population-is-defined-by-its-youth/) / [School](https://www.census.gov/content/dam/Census/library/publications/2016/demo/p20-578.pdf) / [Drinking](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5205547/) / [Poverty](https://fas.org/sgp/crs/misc/R46294.pdf) / [Urbanity](https://onlinelibrary.wiley.com/doi/pdf/10.1111/1475-6773.13106) / [Obesity](https://www.cdc.gov/nchs/data/databriefs/db360_tables-508.pdf#page=2)
* [Arrests for violent crime](https://ucr.fbi.gov/crime-in-the-u.s/2018/crime-in-the-u.s.-2018/tables/table-43)
* [Murder victims](https://www.cdc.gov/nchs/data/nvsr/nvsr68/nvsr68_09-508.pdf) (p. 43)

---

This post is part of a series on bias in policing with several posts still to come.


* Part 1: **Your ratios don't prove what you think they prove (This post)**
* Part 2: [The veil of darkness](https://dynomight.net/2020/10/12/police-violence-the-veil-of-darkness/)
* Part 3: [Policy proposals and what we don't know about them](https://dynomight.net/2020/11/21/police-violence-policy-proposals-and-what-we-dont-know-about-them/)
* Part 4: [Why fairness is basically unobservable](https://dynomight.net/2020/11/23/police-violence-why-fairness-is-basically-unobservable/)
