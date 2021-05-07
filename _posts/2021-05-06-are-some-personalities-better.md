---
layout: post
title: "A review of correlations between personality traits and life outcomes"
image: /img/personalities/shadows.jpg
tags: personality statistics
hero_light: false
dark_title: false
background_color: black
description: "A review of correlations between personality traits and various life outcomes"
permalink: /better-personalities/
background_color: rgb(10, 10, 10)
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
</style>"
---

I don't know if you like parties. I don't know if you're organized or punctual. But I bet you don't like rotting smells or long swims in freezing water.

That is to say: People are different, but only in certain ways. What's the difference? Hypothermia enthusiasts have few kids, so their genes tend to disappear. If introverts were worse at breeding than extraverts, then the same thing would have happened. Since extraversion varies widely, we can infer that we're at an equilibrium point with no real advantage either way. (Personality traits are around [40% genetic](https://emilkirkegaard.dk/en/wp-content/uploads/Heritability-of-Personality-A-Meta-Analysis-of-Behavior-Genetic-Studies.pdf).) 

So, no personality is *better* than any other. Instead, there must be intricate tradeoffs, with each personality occupying a different kind of niche.

That's what I thought, anyway. Then I read a few dozen papers and made this table:

![correlations of various things with the big five](/img/personalities/vals.svg)

This shows correlations between the [Big Five](https://en.wikipedia.org/wiki/Big_Five_personality_traits) personality traits and various personal characteristics. To make this easier to understand, I reversed some "bad" traits (r). I also used  *Emotional Stability*, which is the opposite of *Neuroticism*.

So, uhh, where are the tradeoffs? People who are extroverted, agreeable, conscientious, emotionally stable and open seem to do better at basically everything. Let's call these people **all-blues**. Broadly speaking, they are more happy, successful, intelligent, creative, and popular. They have fewer addictions and less of every mental disorder. The one real tradeoffs are agreeableness against income/intelligence and extraversion/conscientiousness against math scores.

I'd like to give a list of famous all-blues as examples, but this doesn't seem to exist. As a proxy, we can look to [Myers-Briggs](https://dynomight.net/in-defense-of-myers-briggs.html), where all-blues are similar to emotionally stable ENFJs. The internet claims that examples of ENFJs are Michael Jordan, Oprah, Pope John Paul II, Martin Luther King Jr., Pericles, and Barack Obama. For the opposite type, famous ISTPs supposedly include the Dalai Lama, Ernest Hemingway, Snoop Dogg, Melania Trump, and Vladimir Putin. (Personally, I assume the Dalai Lama has high emotional stability, but judge for thyself.)

Anyway, what's the deal here? Why don't we see more tradeoffs? Is the idea of a population equilibrium mistaken?

## Evolution don't care

Evolution doesn't care if you're happy. Evolution only wants you to pass on your genes. [Berg et al. (2014)](https://doi.org/10.1016/j.evolhumbehav.2014.07.006) took data from 10.7k representative Americans born between 1900 and 1947 and did a regression to predict the number of grandchildren someone has from their personality traits. Here are the regression coefficients:

![regression of number of grandkids on personality traits](/img/personalities/model1.svg)

The personality characteristics are standardized so Extraversion = 0 for someone who is average, and Extraversion = -2 for someone 2 standard deviations below average, etc. They focus on grandchildren to reflect the influence of a parent's personality on a child's survival, but just using children gives similar results.

If you're wondering, this suggests the ESFP as the most fecund [MBTI](https://dynomight.net/in-defense-of-myers-briggs.html) type (Ronald Reagan, Bill Clinton, Hugh Hefner).

On the one hand, this would explain why everyone isn't an all-blue: If you want to dominate the personality landscape, you need to reproduce more. On the other hand, it creates a bigger puzzle: If we were in population equilibrium, all the coefficients would be zero! Instead, there are huge effects like extroverted men having 0.8 more grandchildren than introverted men. If that's true, then we are *way* out of equilibrium, and future generations will look different from us.

It's tempting to make up post-hoc stories for those coefficients. ("High openness people spend too much time on rationalist-adjacent blogs," har-har, yes, very good.) But it's not that simple. You've got to do one of two things.

* You might reject the idea of a population equilibrium. If so, you should explain why the rules of natural selection don't apply here.
* You might claim that humans *used* to be in equilibrium, but there's been some recent change to reproductive fitness that evolution hasn't caught up to yet. If so, what's the change?

What changes could have thrown us out of equilibrium? It can't be the dawn of agriculture -- there's been too many generations for effects this strong to persist. It would need to be more recent like the industrial revolution or the invention of birth control. Intelligence isn't exactly a personality trait, but [Udry (1978)](http://dx.doi.org/10.1080/19485565.1978.9988313) surveyed 225 women on birth control. After three years, the percentage of low, medium, and high-IQ women who accidentally had a baby was 11.1%, 8.2%, and 3.4%, respectively. This paper is old and I couldn't find any replications, so I wouldn't put too much faith in it. Still, it's plausible that conscientiousness could have a similar role.

<details markdown="1">
<summary>Aside: Personality traits are correlated. For example, extraversion is correlated with openness. If we account for this, there's still tons of variability in how many grandkids different personalities should expect.
</summary>

Lieu [pointed out](https://twitter.com/lieuZhengHong/status/1389972790334435337) that there are correlations between personality traits. [Vukasović and Bratko (2015)](https://dx.doi.org/10.1037/bul0000017) do a meta-analysis, arriving at the following correlations.

|      | E    | A    | C    | ES   | O    |
| ---- | ---- | ---- | ---- | ---- | ---- |
| E    | 1    | .051 | .122 | .231 | .413 |
| A    | .051 | 1    | .413 | .438 | .114 |
| C    | .122 | .413 | 1    | .442 | .208 |
| ES   | .231 | .438 | .442 | 1    | .188 |
| O    | .413 | .114 | .208 | .188 | 1    |

Fortunately for us, correlations alone are enough to generate the normalized variables (z-scores) that we need to plug into the above regression. I generated a bunch of "random people" either sampling from either an independent multivariate Normal distribution, or a multivariate Normal distribution with the above table as a covariance matrix. I then plugged those people into the regression model and computed a histogram for each.

<img src="/img/personalities/hist.svg">

Sure enough, the standard deviation is less if we account for the correlations. But it's only a *bit* less. In any case, the grandkids model is a *regression*. Correlations among with inputs don't change the fact that certain people (high openness introverts) have fewer grandkids than others (low openness extraverts).

<br>
</details>

I suspect we really are out of equilibrium. Modern lives are very different than even 5-10 generations ago, and it would be strange if this didn't impact how much different people reproduce. But there's no reason to think we're evolving in an all-blue direction.

## A look at presidents

Forget about evolution for a second. Do successful people still tend to be all-blue?

[Rubenzer et al. (2000)](https://doi.org/10.1177%2F107319110000700408) had multiple expert historians profile American presidents. Here are their results, presented as a percentage of the population:

![big five personality traits for American presidents](/img/personalities/prez.svg)

 Washington is a 98.6% on Conscientiousness. Nixon is a 0.02% on Agreeableness.

It's *very* hard to become president. If an all-blue personality was better, we'd see that here. Instead, among recent presidents, we see high extraversion, low agreeableness, and no clear trend otherwise. (Most US households gained radios around 1930 before the election of Franklin Roosevelt.)

If being all-blue doesn't help you *become* president, does it make you a good one? It happens that the closest there's been to an all-blue president was Lincoln, often considered the best of all. (He scores low on emotional stability due to his lifelong struggles with depression.) To be more data-driven, the paper finds correlations between personality factors and how *great* a president is rated to be.

![correlations between big five personality traits and presidential greatness](/img/personalities/model2.svg)

This is similar to the profile of an all-blue, except that agreeableness is bad, and emotional stability doesn't matter. Teddy Roosevelt probably fits this profile best.

There's also value in looking at sub-traits. In particular, *Agreeableness* has different facets: *Tender-mindedness* is correlated with greatness, while *compliance* and *straightforwardness* are anti-correlated.

## The darkness hypothesis

Why are recent presidents usually extraverted and low agreeableness, but otherwise so mixed? Here's my guess:

![relationships of the big five with darker traits](/img/personalities/badvals.svg)

This isn't to say that presidents are all narcissists or psychopaths. (Though who are we kidding, some are.) It's widely agreed now that "narcissism" and "psychopathy" aren't discrete categories. Rather, they are "spectrum traits" that we all have to some degree.

How do we arrive at a spectrum of psychopathy? It's the same equilibrium process. If there were no psychopaths, the first one to show up would probably manipulate everyone and have a thousand kids. As we get more psychopaths, everyone's defenses go up, and the strategy becomes less useful. It's not shocking that these traits might be useful in politics.

## Summary

All-blues might really be happier and healthier. If so, it could a result of late modernity, or it might have always been true. Still, that doesn't mean that evolution will favor all-blues, or that all-blues are "more successful".

What about the rest of us, who aren't all-blue? (Market research suggests my median reader is high openness and conscientiousness, but low extraversion and agreeableness.)

Well, it's all just correlations. It's not that low agreeableness *causes* people to have gambling disorders. I'm not even sure that statement makes sense! Rather, other factors (genes, environment) cause both. If you aren't a psychopath, then correlations aren't something to worry about. If you *are* a psychopath, then... probably you're not worried about my advice?

<details markdown="1">
<summary>
Data Sources
</summary>

Life Satisfaction - [Anglim et al, 2020](https://doi.org/10.1037/bul0000226) (Many other measures of happiness are similar)

Job satisfaction - [Judge et al., 2002](https://doi.org/10.1037/0021-9010.87.3.530)

Income, Intelligence - [Judge et al., 1999](http://timothy-judge.com/Judge,%20Higgins,%20Thoresen,%20&%20Barrick%20PPsych.pdf)

ADHD  - [Nigg et al., 2002](https://doi.org/10.1037/0022-3514.83.2.451) (Table 8 Grand M)

Schizophrenia - [Ohi et al., 2016](https://doi.org/10.1016/j.psychres.2016.04.004)

Autism - [Lodi-Smith et al. 2018](https://doi.org/10.1177/1362361318766571)

Depression, Panic disorder, OCD, Substance Abuse - [Kotov et al., 2010](https://doi.org/10.1037/a0020327)

Loneliness - [Buecker et al., 2020](https://doi.org/10.1002%2Fper.2229)

Popularity, Likability - [D. van der Linden et al., 2010](https://doi.org/10.1016/j.jrp.2010.08.007)

Gambling Disorder - [Dash et al., 2019](https://doi.org/10.1037/adb0000468) (Table 2, 2+ symptoms, average men + women)

College Performance - [Vedel, 2014](https://doi.org/10.1016/j.paid.2014.07.011)

SAT Verbal, SAT Math - [Noftle and Robins, 2014](https://doi.org/10.1037/0022-3514.93.1.116)

Creativity - [Zare and Flinchbaugh, 2018](https://doi.org/10.1080/08959285.2018.1550782)

Average restaurant tip - [Lynn, 2021](https://doi.org/10.1016/j.ijhm.2020.102722)

Accidents - [Beus et al., 2015](http://dx.doi.org/10.1037/a0037916)

Pro-environment - [Soutter et al, 2020](https://doi.org/10.1177%2F1745691620903019) (traits as attitudes)

Politically Conservative - [Sibley et al, 2012](https://doi.org/10.1016/j.jrp.2012.08.002)

Body Mass Index - [Sutin et al., 2015](https://dx.doi.org/10.1016/j.jrp.2015.07.006)

Infidelity, Promiscuity - [Schmitt, 2004](https://doi.org/10.1002/per.520)

Narcissism, Machiavellianism, Psychopathy - [Muris et al, 2017](https://doi.org/10.1177%2F1745691616666070)

The Presidential Big Five data is from *Personality, Character, and Leadership In The White House: Psychologists Assess the Presidents* by Rubenzer and Faschingbauer, 2004. It was quite an effort to extract these numbers from the book and get them into a useable form. Since they might be useful to others, I've uploaded the raw CSV data here: [presidents.csv](/assets/data/presidents.csv) [names.csv](/assets/data/names.csv)

</details>