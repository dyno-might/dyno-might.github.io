---
layout: post
title: Are language models good at making predictions?
image: /img/predictions/time.jpg
tags: AI data forecasting
description: politics more than science
excerpt: ""
permalink: /predictions/
background_color: rgb(215,216,218)
category: science
head: "<style>table {border-spacing: 10px;}</style>"
---

To get a crude answer to this question, we took 5000 questions from Manifold markets that were resolved after GPT-4's current knowledge cutoff of Jan 1, 2022. We gave the text of each of them to GPT-4, along with these instructions:
   > You are an expert superforecaster, familiar with the work of Tetlock and others. For each question in the following json block, make a prediction of the probability that the question will be resolved as true.
   > 
   > Also you must determine category of the question. Some examples include: Sports, American politics, Science etc. Use make_predictions function to record your decisions. You MUST give a probability estimate between 0 and 1 UNDER ALL CIRCUMSTANCES. If for some reason you can't answer, pick the base rate, but return a number between 0 and 1.

This produced a big table:

|question|prediction P(YES)|category|actually happened?|
|---|---|---|---|
|Will the #6 Golden State Warriors win Game 2 of the West Semifinals against the #7 LA Lakers in the 2023 NBA Playoffs?|0.5|Sports|YES|
|Will Destiny's main YouTube channel be banned before February 1st, 2023?|0.4|Social Media|NO|
|Will Qualy show up to EAG DC in full Quostume?|0.3|Entertainment|NO|
|Will I make it to a NYC airport by 2pm on Saturday, the 24th?|0.5|Travel|YES|
|Will this market have more Yes Trades then No Trades|0.5|Investment|CANCEL|
|Will Litecoin (LTC/USD) Close Higher July 22nd Than July 21st?|0.5|Finance|NO|
|Will at least 20 people come to a New Year’s Resolutions live event on the Manifold Discord?|0.4|Social Event|YES|
|hmmmm {i}|0.5|Uncategorized|YES|
|Will there be multiple Masters brackets in Leagues season 4?|0.4|Gaming|NO|
|Will the FDA approve OTC birth control by the end of February 2023?|0.5|Health|NO|
|Will Max Verstappen win the 2023 Formula 1 Austrian Grand Prix?|0.5|Sports|YES|
|Will SBF make a tweet before Dec 31, 2022 11:59pm ET?|0.9|Social Media|YES|
|Will Balaji Srinivasan actually bet $1m to 1 BTC, BEFORE 90 days pass? (June 15st, 2023)|0.3|Finance|YES|
|Will a majority of the Bangalore LessWrong/ACX meet-up attendees on 8th Jan 2023 find the discussion useful that day?|0.7|Community Event|YES|
|Will Jessica-Rose Clark beat Tainara Lisboa?|0.6|Sports|NO|
|Will X (formerly twitter) censor any registered U.S presidential candidates before the 2024 election?|0.4|American Politics|CANCEL|
|test question|0.5|Test|YES|
|stonk|0.5|Test|YES|
|Will I create at least 100 additional self-described high-quality Manifold markets before June 1st 2023?|0.8|Personal Goal|YES|
|Will @Gabrielle promote to ???|0.5|Career Advancement|NO|
|Will the Mpox (monkeypox) outbreak in the US end in February 2023?|0.45|Health|YES|
|Will I have taken the GWWC pledge by Jul 1st?|0.3|Personal|NO|
|FIFA U-20 World Cup - Will Uruguay win their semi-final against Israel?|0.5|Sports|YES|
|Will Manifold display the amount a market has been tipped by end of September?|0.6|Technology|NO|

In retrospect maybe we have filtered these. Many questions are a bit silly for our purposes, though they're typically classified as "Test", "Uncategorized", or "Personal".

## Is this good?

One way to measure if you're good at predicting stuff is to check your calibration: When you say something has a 30% probability, does it actually happen 30% of the time?

To check this, you need to make a lot of predictions. Then you dump all your 30% predictions together, and see how many of them happened.

GPT-4 is not well-calibrated.
![](/img/predictions/calibration_histogram_overall.svg)
Here, the x-axis is the range of probabilities GPT-4 gave, broken down into bins of size 5%. For each bin, the green line shows how often those things actually happened. Ideally, this would match the dotted black line. For reference, the bars show how many predictions GPT-4 gave that fell into each of the bins. (The lines are labeled on the y-axis on the left, while the bars are labeled on the y-axis on the right.)

At a high level, this means that GPT-4 is over-confident. When it says something has only a 20% chance of happening, actually happens around 35-40% of the time. When it says something has an 80% chance of happening, it only happens around 60-75% of the time.

## Does it depend on the area?

We can make the same plot for each of the 16 categories. (Remember, these categories were decided by GPT-4, though from a spot-check, they look accurate.) For unclear reasons, GPT-4 is well-calibrated for questions on sports, but horrendously calibrated for "personal" questions:

![](/img/predictions/calibration_histograms_4x4.svg)

All the lines look a bit noisy since there are 20 × 4 × 4 = 320 total bins and only 5000 total observations.
## Is there more to life than calibration?

Say you and I are predicting the outcome that a fair coin comes up heads when flipped. I always predict 50%, while you always predict either 0% or 100% and you're always right. Then we are both perfectly calibrated. But clearly your predictions are better, because you predicted with more confidence.

The typical way to deal with this is squared errors, or "Brier scores". To calculate this, let the actual outcome be 1 if the thing happened, and 0 if it didn't. Then take the average squared difference between your probability and the actual outcome. For example:

* GPT-4 gave "Will SBF make a tweet before Dec 31, 2022 11:59pm ET?" a YES probability of 0.9. Since this actually happened, this corresponds to a score of (0.9-1)² = 0.01.
* GPT-4 gave "Will Manifold display the amount a market has been tipped by end of September?" a YES probability of 0.6. Since this didn't happen, this corresponds to a score of (0.6-0)² = 0.36.

Here are the average scores for each category (lower is better):

![](/img/predictions/brier.svg)

Or, if you want, you can decompose the Brier score. There are various ways to do this, but my favorite is <var>Brier = Calibration + Refinement</var>. Informally, <var>Calibration</var> is how close the green lines above are to the dotted black lines, while <var>Refinement</var> is how confident you were. (Both are better when smaller.)

![](/img/predictions/decomp.svg)

You can also visualize this as a scatterplot:

![](/img/predictions/decomp-scatter.svg)

## Is there more to life than refinement?

Brier scores are better for politics questions than for science questions. But is that because it's bad at science, or just because science questions are hard?

There's a way to further decompose the Brier score. You can break up the resolution as <var>Refinement = Uncertainty - Resolution</var>. Roughly speaking,  <var>Uncertainty</var> is "how hard questions are", while <var>Resolution</var> is "how confident you were, once calibration and uncertainty are accounted for".

Here's the uncertainty for different categories:

![](/img/predictions/uncertainty.svg)

And here's a scatterplot of the calibration and resolution for each category: (Since more resolution is better, it's now the upper-left that contains better predictions.)

![](/img/predictions/decomp-scatter-resolution.svg)

Overall, this further decomposition doesn't change much. This suggests GPT-4 really is better at making predictions for politics than for science or technology, even once the hardness of the questions are accounted for.

P.S. The relative merits of different [Brier score decompositions](https://en.wikipedia.org/wiki/Brier_score#3-component_decomposition) caused an amazing amount of internal strife during the making of this post. I had no idea I could feel so strongly about mundane technical choices. I guess I now have an exciting new category of enemies.
