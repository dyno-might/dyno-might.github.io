---
layout: post
title: "Does the gender-equality paradox actually exist?"
image: /img/gender-equality-paradox/sign3.jpg
tags: policy statistics personality
hero_light: false
dark_title: false
background_color: black
description: "Some claim that more feminist countries have fewer women in STEM. Others say this is nonsense. Who is right?"
permalink: /gender-equality-paradox/
background_color: rgb(189, 161, 154)
seo:
  date_modified: 2021-12-06
category: "psychology"
head: "<style>
details{
    }
details summary{
  padding-bottom: 12pt;
}
img{
    display:block;
    margin-left: auto;
    margin-right: auto;
}
table tr{
    border-style: hidden;
    text-align:center;
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

The gender-equality paradox is the (disputed) idea that countries with more gender equality have fewer women in STEM careers. While there's lots of debate in the scientific literature about the *causal implications* of this paradox, there's no agreement about a more basic question: Does the paradox even *exist*, or is it just an illusion caused by a contrived data analysis?

{% comment %}
To answer that, let's check how robust the paradox is. Does it stand up if we change how we measure *gender equality* or *women in STEM careers*?
{% endcomment %}

{% comment %}
## Contents
{:.no_toc}
{% endcomment %}

<div style="font-size:90%; line-height:110%;" markdown="1">

* auto-gen TOC:
{:toc}

</div>


## The debate so far

### Act I

In 2018, [Stoet and Geary](https://doi.org/10.1177%2F0956797617741719) had one of the most surprising results in social science in a decade. They took the [Global Gender Gap Index](https://en.wikipedia.org/wiki/Global_Gender_Gap_Report) (GGGI), which measures gender equality, and plotted it against the percentage of women among STEM graduates.

![GGGI against fraction of women in STEM](/img/gender-equality-paradox/stoet-geary-original-graph-wide.jpg)

Finland has high equality but few women in STEM, while Algeria is the opposite. That's the trend.

*Why* this would be true is unclear, but the result seems hard to dispute. It's obvious that GGGI is measuring *something*, just look at the countries that are high or low on the graph. And you don't need to trust any fancy statistics, you can see the trend in the data.

This was picked up by [The Atlantic](https://www.theatlantic.com/science/archive/2018/02/the-more-gender-equality-the-fewer-women-in-stem/553592/), [The American Enterprise Institute](https://www.aei.org/carpe-diem/the-global-educational-gender-equality-paradox-the-more-gender-equality-in-a-country-the-fewer-women-in-stem/), [Ars Technica](https://arstechnica.com/science/2018/02/globally-women-tend-to-avoid-science-careers-even-when-theyre-good-at-it/), [MacLean's](https://www.macleans.ca/society/could-helping-boys-be-the-key-to-closing-the-stem-gap/), and [Jordan Peterson](https://www.jordanbpeterson.com/political-correctness/the-gender-scandal-part-one-scandinavia-and-part-two-canada/). Stoet and Geary themselves published an article at [Quillette](https://quillette.com/2018/02/15/sex-stem-stubborn-facts-stubborn-ideologies/), where they suggest their graph is partly due to different levels of interest in STEM and partly to [comparative advantage](https://dynomight.net/2020/09/11/comparative-advantage-and-when-to-blow-up-your-island/)—in places like Finland, girls perform similarly to boys in science but much better in reading.

Wait, did I just say this was hard to dispute? {% comment %} Hahaha, no. {% endcomment %}

### Act II

Suspicious of these results, Richardson and colleagues took the same data, calculated the percentage of women among STEM graduates, and got... completely different numbers. They—I think—contacted the journal, which led to a [corrigendum](https://doi.org/10.1177%2F0956797619892892) from Stoet and Geary in late 2019. This clarified what's on the x-axis in the above graph:

> The propensity of women to graduate with STEM degrees was *a*/(*a + b*), where *a* is the percentage of women who graduate with STEM degrees (relative to all women graduating) and *b* is the percentage of men who graduate with STEM degrees (relative to all men graduating). 

Get that? Take a country with the following graduates each year:

{% comment %}
‎‎‏‏‎ ‎|men|women|
-|-|-
**STEM degrees**|100|5
**All degrees**|1000|50
{% endcomment %}

‎‎‏‏‎ ‎|STEM degrees|All degrees|
-|-|-
**Men**|100|1000
**Women**|5|50

Women make up 4.8% (5/105) of STEM graduates.  However, their formula gives 50%, since the fraction of women who do STEM is the same as the fraction of men who do STEM. That is, *a*=5/50 is equal to *b*=100/1000.

There's a good argument for this. The most salient fact about the above country isn't anything STEM-specific, it's just that few women get degrees. Stoet and Geary's formula is invariant to this kind of imbalance.

There's also a good argument against this formula. Maybe you think that imbalances in the total number of degrees are important, and you don't *want* to be invariant to them.

What there's *not* a good argument for is calling this quantity "Women Among STEM Graduates (%)" like the above graph does. In their corrigendum, Stoet and Geary don't really explain how this happened. In fact, they don't change much about their paper at all, other than adding above quote and inserting "propensity" everywhere.

### Act III

Simultaneously with Stoet and Geary's corrigendum in 2019, Richardson and colleagues published a [commentary](https://doi.org/10.1177%2F0956797619872762) on the corrected paper. They argue:

1. Propensities are bad.
2. It's not cool to use GGGI because it "measures achieved outcomes, not propensities" and "is not intended to be used to causally explain outcomes".
3. Better than GGGI is the ultra-simple [Basic Indicator of Gender Inequality](https://bigi.genderequality.info/) (BIGI). Stoet and Geary shouldn't object to this, since it was proposed by... [Stoet and Geary](https://doi.org/10.1371/journal.pone.0205349).
5. If they compute the *actual* percentage of STEM degrees earned by women and plot it against BIGI, they get this graph, along with a non-significant regression coefficient.

<img src="/img/gender-equality-paradox/richardson-reply-graph.svg" alt="richardson reply graph" loading="lazy">

They also published articles in [Slate](https://slate.com/technology/2020/02/women-stem-innate-disinterest-debunked.html) and on [their blog](https://www.buzzfeednews.com/article/stephaniemlee/women-stem-gender-equality-paradox-correction). This was picked up by [Buzzfeed](https://www.buzzfeednews.com/article/stephaniemlee/women-stem-gender-equality-paradox-correction) and [The Scientist](https://www.the-scientist.com/news-opinion/scholars-debate-causes-of-womens-underrepresentation-in-stem-67117).

### Act IV

In 2020, Breda and colleagues published a [paper](https://doi.org/10.1073/pnas.2008704117), part of this uses the same propensities as Stoet and Geary. They argue this is worthwhile both because the original result is well-known and because it's nice to be invariant to imbalances in the overall number of degrees.

Their first observation is that the propensities aren't just correlated with GGGI. They are also correlated with:
* GDP per capita.
* The [human development index](https://en.wikipedia.org/wiki/Human_Development_Index).
* Income inequality, measured via the [Gini index](https://en.wikipedia.org/wiki/Gini_coefficient).
* The [Coefficient of Human Inequality](http://hdr.undp.org/en/content/inequality-adjusted-human-development-index-ihdi).

They do a regression to predict propensities from each of these variables (one variable at a time) and get these coefficients (from [Table S5](https://www.pnas.org/lookup/suppl/doi:10.1073/pnas.2008704117/-/DCSupplemental)):

<a href="/img/gender-equality-paradox/breda_model.pdf" alt="regression of STEM propensities on different country variables">
<img src="/img/gender-equality-paradox/breda_model.svg" alt="regression of STEM propensities on different country variables" loading="lazy">
</a>

Everything "good" is associated with lower propensities, be it more GDP, more development, less income/human inequality, or more gender equality.

Their goal was to test how all this relates to gender stereotypes. They took the [PISA 2012](https://www.oecd.org/pisa/pisaproducts/pisa2012database-downloadabledata.htm) data, and looked at how boys and girls felt about these two statements. These were chosen because they don't directly mention gender, reducing the risk of social desirability bias.

> "Whether or not I do well in mathematics is completely up to me."
>
> "My parents believe it’s important for me to study mathematics."

Their *stereotype score* for each country reflects how much boys vs. girls agree with the above statements. If a boy of equal math ability is more likely to agree than a girl, the stereotype score is positive. If a girl is more likely to agree, the stereotype score is negative.

Their main result is a second regression to predict STEM propensities, now controlling for the stereotype scores in each country:

<a href="/img/gender-equality-paradox/breda_model_GMS.pdf" alt="regression of STEM propensities controlling for stereotypes">
<img src="/img/gender-equality-paradox/breda_model_GMS.svg" alt="regression of STEM propensities controlling for stereotypes" loading="lazy">
</a>

Knowing stereotypes makes the other variables less predictive, dramatically so in some cases (Human Inequality) less so for others (GGGI).

This paper is often summarized (e.g. on [Wikipedia](https://en.wikipedia.org/wiki/Gender-equality_paradox#Breda,_Jouini,_Napp_and_Thebault_(2020)_study_on_economic_development_and_gendered_study_choices)) with quotes like this (emphasis mine):

> The stereotype associating math to men is stronger in more egalitarian and developed countries. It is also strongly associated with various measures of female underrepresentation in math-intensive fields and can therefore *entirely explain* the gender-equality paradox.

## New Analysis

### Paradox dissolved?

After first reading these follow-up papers, I had the impression the original study was debunked. But notice three things:

First, **causality isn't everything.** Richardson et al. think that BIGI is better than GGGI for establishing causality. I don't understand their reasoning in the slightest, but it doesn't matter. *None* of these analyses prove causality.

Still, does the paradox actually exist? It can't simultaneously be *false* (as Richardson et al. seem to claim) and *true but explained by gender stereotypes* (as Breda et al. claim.) Which is it?

Second, **stereotypes don't solve the paradox.** How could they, when the reduction for the GGGI coefficient above is so modest? I think the Wikipedia quote is misleading: Most of Breda et al.'s paper is about predicting other things, e.g. the *intention* to study STEM, where controlling for stereotypes has a stronger effect.

But OK, suppose that the paradox was entirely explained by gender stereotypes. That would just mean we've traded the mystery of why more gender-equal countries have fewer women in STEM for the mystery of why more gender-equal countries would have stronger stereotypes. That is still very paradoxical!

{% comment %}

* It could be cultural. Maybe in rich, gender-equal countries, The Patriarchy has more spare resources to spend indoctrinating everyone.
* It could be intrinsic interest. Maybe women are less likely to have STEM as their #1 choice, but in *un*equal countries they have few other options and so they conclude math is important for them.
* It could be some impossible-to-disentangle combination. Maybe parents in gender-unequal countries know that their daughters have fewer opportunities, and so they constantly tell them how amazing math is, resulting in those girls liking math.
{% endcomment %}

Third, **it's unclear how fragile the result is.** Richardson et al. say that the paradox only appears because of "contrived measures and selective data". Of course, if the paradox only appears after torturing the data in one particular way, then we shouldn't trust it. But their evidence is what happened when they tortured the data in one *other* particular way.

Shouldn't we try a *bunch* of analyses, and just check how robust things are?

### A bunch of analyses

Let's start with the original analysis, relating GGGI to propensities. (Click to zoom in and look at the country names.)

<a href="/img/gender-equality-paradox/gggi_vs_female_propensity.pdf" alt="gggi vs female propensity" markdown="1">
![gggi vs female propensity](/img/gender-equality-paradox/gggi_vs_female_propensity.svg)
</a>

This is the same as the [original Stoet and Geary figure](/img/gender-equality-paradox/stoet-geary-original-graph-wide.jpg), with three small changes:

<!-- really only 1 million or greater? -->

1. Switch the axes.
3. Color countries according to their continent.
4. Show a [LOWESS](https://en.wikipedia.org/wiki/Local_regression) smoothing (linearity is for wimps) along with a 95% confidence interval, computed using [bootstrapping](https://en.wikipedia.org/wiki/Bootstrapping_%28statistics%29).

### A different calculation for STEM-participation

The above figure uses propensities, which is a major point of contention. Personally, I think this debate is silly. Propensities give one view of the data, while the raw fraction of women in STEM gives another. They both have value.

So, what if Stoet and Geary had just switched to using the *actual* percentage of women among people who earn STEM degrees, as Richardson et al. suggest they should have? They'd have gotten the following curves. (I added non-STEM degrees for context.)

<a href="/img/gender-equality-paradox/gggi_vs_female_share_nonstem_and_female_share.pdf">
![gggi vs female STEM and non-STEM fractions](/img/gender-equality-paradox/gggi_vs_female_share_nonstem_and_female_share.svg)
</a>

In more-equal countries, women earn a larger share of non-STEM degrees, but a smaller share of STEM degrees. The paradox is still there.

### Other measures of equality

Maybe this all depends on some weirdness with how GGGI measures equality? A newer alternative is the [Gender Inequality Index](https://en.wikipedia.org/wiki/Gender_Inequality_Index) (GII). I took the 2019 rankings and used them instead of GGGI.

Be careful interpreting this graph: While more equality meant *more* GGGI, it means *less* GII.

<a href="/img/gender-equality-paradox/gii_vs_female_share_nonstem_and_female_share.pdf" alt="gii vs female STEM and non-STEM fractions">
<img src="/img/gender-equality-paradox/gii_vs_female_share_nonstem_and_female_share.svg" alt="gii vs female STEM and non-STEM fractions" loading="lazy">
</a>

Again, the most gender-equal countries have a smaller fraction of women in STEM, but not non-STEM. If you use propensities instead of the female share of degrees, the effect is <a href="/img/gender-equality-paradox/gii_vs_female_propensity.pdf">even stronger</a>.

A third alternative is BIGI, as suggested by Richardson et al. Be very careful here: BIGI is negative when women are favored and positive when men are favored. Equality occurs around zero.

<a href="/img/gender-equality-paradox/bigi_vs_female_share_nonstem_and_female_share.pdf" alt="bigi vs female STEM and non-STEM fractions">
<img src="/img/gender-equality-paradox/bigi_vs_female_share_nonstem_and_female_share.svg" alt="bigi vs female STEM and non-STEM fractions" loading="lazy">
</a>

For non-STEM degrees, the trend is simple---the more women are favored, the more degrees they earn. But for STEM degrees, there's a U-shaped curve where women earn the smallest share around BIGI ≈ -.02, where women are *just slightly* favored. Comparing BIGI to propensities gives a <a href="/img/gender-equality-paradox/bigi_vs_female_propensity.pdf">stronger, but less symmetric, effect</a>.

While we're on the subject... The red dots in the above graph show the same data as in Richardson et al.'s commentary [above](#act-iii), which they used to claim that there was no gender-equality-paradox. (You can also see them [by themselves with country labels](https://dynomight.net/img/gender-equality-paradox/bigi_vs_female_share.pdf).) What's going on?

<details>
<summary>
Well, for one thing, I made the graph <strike>better</strike> differently, switching the axes and using smaller markers so you can see the density of countries.
</summary>
Don't believe me? Here's what you get if you take their graph, rotate right by 90 degrees, flip the vertical axis, and change the aspect ratio:

<img src="/img/gender-equality-paradox/richardson_transformed.jpg" alt="transformed version of richardson's data" loading="lazy">

If you look carefully, you can see that these dots are the same as the red dots above.

</details>

For another thing, they did a *linear regression* and found no significant result. That's not too surprising, given that the effect above is nonlinear and symmetric.

### Against BIGI

I think BIGI is a terrible measure of gender-equality and we shouldn't be using it. For context here's a plot comparing the other two measures we've looked at, GGGI and GII:

<a href="/img/gender-equality-paradox/gggi_vs_gii.pdf" alt="gggi vs gii graph">
<img src="/img/gender-equality-paradox/gggi_vs_gii.svg" alt="gggi vs gii" loading="lazy">
</a>

Are the Philippines more gender-equal than Japan (as GGGI implies) or the opposite (as GII implies)? I don't know, but I'll accept that it depends on different, reasonable definitions of *gender-equal*.

On the other hand, here's a plot of GGGI against BIGI:

<a href="/img/gender-equality-paradox/gggi_vs_bigi.pdf">
<img src="/img/gender-equality-paradox/gggi_vs_bigi.svg" alt="gggi vs bigi" loading="lazy">
</a>

According to BIGI, Saudi Arabia—where women can only show their [hands and eyes in public](https://en.wikipedia.org/wiki/Women%27s_rights_in_Saudi_Arabia#Hijab_and_dress_code) and must have a [legal male guardian](https://en.wikipedia.org/wiki/Women%27s_rights_in_Saudi_Arabia#Male_guardians)—is basically the same as Switzerland. And Lesotho—the tiny country inside South Africa—is by far the most women-favored place in the entire world. Ooohkaaay.

This isn't to say that BIGI is *bad* exactly. They [specifically discuss Saudi Arabia](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0205349#sec011) in their paper. My point is that it doesn't capture what we have in mind in this context. At all. So while we *do* seem to get a paradox with BIGI, I think it's meaningless and we should forget about it.

### Other measures of women in STEM

While the result seems robust to different measures of gender equality, everything above uses the same data from UNESCO on the number of STEM graduates. We've analyzed it both in terms of propensities and raw fractions, and the result is still robust. Still, what if we use a different data source entirely to measure STEM participation?

For variety, I looked at the [female share of researchers in engineering and technology](https://en.unesco.org/sites/default/files/usr15_is_the_gender_gap_narrowing_in_science_and_engineering.pdf). If you compare this to GGGI, there's really no paradox at all. At most, there's a bit of a "leveling off".

<a href="/img/gender-equality-paradox/gggi_vs_researchers.pdf">
<img src="/img/gender-equality-paradox/gggi_vs_researchers.svg" alt="GGGI vs. female share of engineering researchers">
</a>

If you look at <a href="/img/gender-equality-paradox/gggi_vs_natsci_researchers.pdf">natural science</a> researchers instead of engineering, you again see no paradox.

On the other hand, if you use GII instead of GGGI, you do see a small effect in the most gender-equal countries:

<a href="/img/gender-equality-paradox/gii_vs_researchers.pdf">
![GII vs. female share of engineering researchers](/img/gender-equality-paradox/gii_vs_researchers.svg)
</a>

Comparing GII to the <a href="/img/gender-equality-paradox/gii_vs_natsci_researchers.pdf">natural sciences</a> shows more of a leveling off than a full reversal.

I'm not sure if all these observations constitute a "paradox" exactly, but they aren't something I would have predicted.

## Takeaways

So, is there a gender-equality paradox? Three points.

First, Stoet and Geary's original paradox is **robust.** It doesn't matter how you measure gender inequality and or if you use propensities or raw fractions to measure women's fraction of STEM degrees. It's not fair to imply that they cherry-picked the details of their analysis to support some pre-determined conclusion.

Second, the paradox is **somewhat limited.** It appears with STEM degrees no matter how you define "equality", or how you torture the data. For STEM researchers, the effect is more modest and only appears for certain definitions of gender equality. This is weird, and I don't understand it other than that it suggests we need more nuance than "more gender equality → fewer women in STEM".

Third, **resist simplistic causal explanations!** People choose degrees for lots of reasons: Economics,  working conditions, family influences, cultural/media influences, intrinsic interest, and simply what degree programs are accessible. Most of these operate in feedback loops with each other. My love for scatterplots is vaster than the seas, but they're at most *vaguely suggestive* of any single cause.

### Plot all the plots
{:.no_toc}

Lest I be accused of cherry-picking, here's *all* the different ways of measuring gender inequality against *all* the ways of measuring women's participation in STEM. I also threw in per-capita GDP and Breda et al.'s stereotype measurements. (For GDP I removed Qatar and the [top 10 tax havens](https://en.wikipedia.org/wiki/Tax_haven#Top_10_tax_havens) where [GDP is meaningless](https://www.washingtonpost.com/news/monkey-cage/wp/2016/07/15/did-irelands-economy-really-grow-by-26-3-percent-only-on-paper-heres-the-real-story/).)

<table>
<th>
<td>GGGI</td>
<td>GII</td>
<td>BIGI</td>
<td>GDP</td>
<td>stereotypes</td>
</th>
<tr><td>STEM propensity</td>
<td><a href="/img/gender-equality-paradox/gggi_vs_female_propensity.pdf">x</a></td>
<td><a href="/img/gender-equality-paradox/gii_vs_female_propensity.pdf">x</a></td>
<td><a href="/img/gender-equality-paradox/bigi_vs_female_propensity.pdf">x</a></td>
<td><a href="/img/gender-equality-paradox/gdp_vs_female_propensity.pdf">x</a></td>
<td><a href="/img/gender-equality-paradox/stereotypes_vs_female_propensity.pdf">x</a></td>
</tr>
<tr><td>STEM degrees</td>
<td><a href="/img/gender-equality-paradox/gggi_vs_female_share.pdf">x</a></td>
<td><a href="/img/gender-equality-paradox/gii_vs_female_share.pdf">x</a></td>
<td><a href="/img/gender-equality-paradox/bigi_vs_female_share.pdf">x</a></td>
<td><a href="/img/gender-equality-paradox/gdp_vs_female_share.pdf">x</a></td>
<td><a href="/img/gender-equality-paradox/stereotypes_vs_female_share.pdf">x</a></td>
</tr>
<tr><td>non-STEM degrees</td>
<td><a href="/img/gender-equality-paradox/gggi_vs_female_share_nonstem.pdf">x</a></td>
<td><a href="/img/gender-equality-paradox/gii_vs_female_share_nonstem.pdf">x</a></td>
<td><a href="/img/gender-equality-paradox/bigi_vs_female_share_nonstem.pdf">x</a></td>
<td><a href="/img/gender-equality-paradox/gdp_vs_female_share_nonstem.pdf">x</a></td>
<td><a href="/img/gender-equality-paradox/stereotypes_vs_female_share_nonstem.pdf">x</a></td>
</tr>
<tr><td>Engineering researchers</td>
<td><a href="/img/gender-equality-paradox/gggi_vs_researchers.pdf">x</a></td>
<td><a href="/img/gender-equality-paradox/gii_vs_researchers.pdf">x</a></td>
<td><a href="/img/gender-equality-paradox/bigi_vs_researchers.pdf">x</a></td>
<td><a href="/img/gender-equality-paradox/gdp_vs_researchers.pdf">x</a></td>
<td><a href="/img/gender-equality-paradox/stereotypes_vs_researchers.pdf">x</a></td>
</tr>
<tr><td>Natural science researchers</td>
<td><a href="/img/gender-equality-paradox/gggi_vs_natsci_researchers.pdf">x</a></td>
<td><a href="/img/gender-equality-paradox/gii_vs_natsci_researchers.pdf">x</a></td>
<td><a href="/img/gender-equality-paradox/bigi_vs_natsci_researchers.pdf">x</a></td>
<td><a href="/img/gender-equality-paradox/gdp_vs_natsci_researchers.pdf">x</a></td>
<td><a href="/img/gender-equality-paradox/stereotypes_vs_natsci_researchers.pdf">x</a></td>
</tr>
</table>

Choose the column you want on the x-axis, the row you want on the y-axis, and let the beautiful dots wash over you.

<details markdown="1">
<summary>
<b>Data sources</b>
</summary>

* GGGI: [Wikipedia](https://en.wikipedia.org/wiki/Global_Gender_Gap_Report#WEF_Global_Gender_Gap_Index_rankings) (2015 rankings)
* GII: [Wikipedia](https://en.wikipedia.org/wiki/Gender_Inequality_Index#Rankings) (2019 rankings)
* BIGI: [genderinequality.info](https://bigi.genderequality.info/#_data)
* Women's share of STEM / non-STEM: The actual UNESCO data used for the share of STEM degrees going to women appears to no longer be on their website.  With much gnashing of teeth, I was able to find an [older version](https://web.archive.org/web/*/http://data.uis.unesco.org/index.aspx?queryid=163) on archive.org.
* Propensities: Due to the same problem, I couldn't find the raw data for propensities. Instead, I took these from Stoet and Geary's [supplementary material](https://journals.sagepub.com/doi/suppl/10.1177/0956797617741719).
* Women's share of engineering / natural science researchers: [UNESCO report](https://en.unesco.org/sites/default/files/usr15_is_the_gender_gap_narrowing_in_science_and_engineering.pdf)
* GDP: The IMF's 2021 estimates in purchasing power parity, via [Wikipedia](https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28PPP%29_per_capita).
* Stereotypes: Breda et al.'s [supplementary material](https://www.pnas.org/lookup/suppl/doi:10.1073/pnas.2008704117/-/DCSupplemental).

</details>