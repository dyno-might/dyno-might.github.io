---
layout: post
title: "Prediction market does not imply causation"
image: /img/prediction-market-causation/arrows1.jpg
tags: forecasting math
description: "Unless you're careful, conditional prediction markets have all the same problems as observational studies."
excerpt: "We all want to make good decisions. But it’s hard because we aren’t sure what’s going to happen. Like, say you want to know if CO₂ emissions will go up in 10 years. One of our best ideas is to have people bet. For example, I might wager my $4 that emissions will go up against your $1 that they will go down. If lots of people bet in a market, the final prices combine everyone’s wisdom and information. If bets were to stabilize at a 4:1 ratio, that suggests that the odds of emissions going up are 4 times larger than the odds of emissions going down"
permalink: /prediction-market-causation/
background_color: rgb(92,42,40)
category: "math"
head: "<style>
var{
  font-family:Montserrat;
  font-style: normal;
  font-size: 80%;
}
.eq {
  display:flex;
  justify-content: center;
  text-align: center;
  padding-top: 0;
  margin-top: 0px;
  margin-bottom: 20px;
  font-family: Montserrat, sans-serif;
  font-size: 90%;
}

</style>
"
comment:
  substack: https://dynomight.substack.com/p/prediction-market-causation
  EA forum: https://forum.effectivealtruism.org/posts/gDsppmv8TzrH2zKJc/prediction-market-does-not-imply-causation
---

[*Note*: If you’re already familiar with prediction markets, you might want to skip to [section 3](#3) or maybe even [section 6](#6).]

## 1.

We all want to make good decisions. But it’s hard because we aren’t sure what’s going to happen.

Like, say you want to know if CO₂ emissions will go up in 10 years. One of our best ideas is to have people bet. For example, I might wager my \$4 that emissions will go up against your \$1 that they will go down. If lots of people bet in a market, the final prices combine everyone’s wisdom and information. If bets stabilize at a 4:1 ratio, that suggests that emissions are 4 times more likely to go up than to go down, i.e.

<var class="eq">P[emissions up] ≈ 0.80</var>

<var class="eq">P[emissions down] ≈ 0.20.</var>

But when you want to make *decisions*, you often need more information. Say someone suggests a treaty to reduce CO₂ emissions. If you want to know if the treaty will work, you can have people make *conditional* bets. For example, I might bet my \$9 against your \$1 with these rules:

1. In 10 years, we check if (a) the treaty became law, and (b) emissions went up.
2. If the treaty became law and emissions went up, you pay me \$1.
3. If the treaty became law and emissions went down, I pay you \$9.
4. If the treaty didn’t become law, we both get our bets back.

If lots of people bet in a market and prices settle at a 9:1 ratio, that suggests that emissions go up in 90% of the worlds where the treaty gets signed, i.e.

<div class="eq">P[emissions up | treaty] ≈ 0.90.</div>

You can run a second market to get the odds of emissions going up, conditional on there *not* being a treaty.

So here’s our question: Say you do that and the market thinks that emissions are more likely to go up with the treaty than without, i.e. <var>P[emissions up | treaty] > P[emissions up | no treaty]</var>. Does that mean that the market thinks that signing the treaty will cause emissions to go up?

## 2.

People worry about prediction markets for lots of reasons. Maybe someone will manipulate prices for political reasons. Maybe fees will distort prices. Maybe you’ll go Dr. Evil and bet that emissions will go up and then go emit a gazillion tons of CO₂ to ensure that you win. Valid concerns, but let's ignore them and assume markets output “true” probabilities.

Now, why would emissions be more likely to go up with the treaty? The obvious explanation is that the market thinks the treaty will cause emissions to go up:

<div class="eq" markdown="1">
Treaty becomes law  
↓  
Emissions go up  
</div>

Totally plausible. But maybe the market thinks something else. Maybe the treaty does nothing but voters *believe* it does something, so emissions going up would cause the treaty to be signed:

<div class="eq" markdown="1">
Emissions go up  
 ↓  
 Climate does scary things  
 ↓  
 People freak out  
 ↓  
 People demand treaty  
 ↓  
 Treaty becomes law
</div>

In this chain of events, the treaty acts as a kind of “emissions have gone up” award. Even though signing the treaty has no effect on emissions, the fact that it became law means it's more likely that emissions have increased. You could still get the same probabilities as in a world where the treaty *caused* increased emissions.

## 3.

Here's a market that [actually exists](https://manifold.markets/LucaPetrolati/conditional-on-nato-declaring-a-nof) (albeit with internet points instead of money): "Conditional on NATO declaring a No-Fly Zone anywhere in Ukraine, will a nuclear weapon be launched in combat in 2022?" This market currently says:

<div class="eq" markdown="1">
P[launch | declare] = 18%,
</div><div class="eq" markdown="1">
P[launch | don’t declare] = 5.4%.  
</div>

<details markdown="1">
<summary>
Technically there's no market for <var>P[launch | don’t declare]</var> but you can find an implied price using (1) the market for <var><a href="https://manifold.markets/EricJang/will-a-nuclear-weapon-be-launched-i">P[launch]</a></var> (2) the market for <var><a href="https://manifold.markets/MetaculusBot/will-nato-declare-a-nofly-zone-anyw">P[declare]</a></var> and (3) <small>THE POWER OF MATH</small>.
</summary>
<!-- Currently the markets give <var>P[launch]=0.06</var> and <var>P[declare]=0.05</var>. We know that -->

Currently the markets give <var>P[declare]=0.05</var>. Thus, we know that

<div class="eq" markdown="1">
P[launch, declare]  
= P[declare] × P[launch | declare]  
= .05 × .18  
= 0.009.   
</div>

So we have this table of probabilities with known row and column sums (the row sums come from the fact that <var>P[launch]=0.06</var>, while the column sums come from the fact that <var>P[declare]=0.05</var>):

|                  | declare | don't declare |      |
| -----------------| -----   | ------------- | ---- |
| <b>launch</b>    | 0.009   | ???           | 0.06 |
| <b>no launch</b> | ???     | ???           | 0.94 |
|                  | 0.05    | 0.95          |      |

Using the known row/column sums we can fill in the missing entries:

|                  | declare | don't declare |      |
| -----------------| -----   | ------------- | ---- |
| <b>launch</b>    | 0.009   | .051          | 0.06 |
| <b>no launch</b> | 0.041   | 0.899         | 0.94 |
|                  | 0.05    | 0.95          |      |

So, finally, we get that

<div class="eq" markdown="1">
P[launch | don't declare]  
= P[launch, don't declare] / P[don't declare]  
= 0.051 / 0.95  
= 0.0537.
</div>

</details>

So launch is 3.3x more likely given <var>declare</var> than given <var>don’t declare</var>. The obvious way of looking at this would be that NATO declaring a no-fly zone would increase the odds of a nuclear launch:

<div class="eq" markdown="1">
NATO declares no-fly zone  
 ↓  
 NATO and Russian planes clash over Ukraine  
 ↓  
 Conflict escalates  
 ↓  
 Nuclear weapon launched  
</div>

That’s probably the right interpretation. But not *necessarily*. For example, do we really know the mettle of NATO leaders? It could be that declaring a no-fly zone has no direct impact on the odds of a launch, but the fact that NATO declares one reveals that NATO leaders have aggressive temperaments and are thus more likely to take *other* aggressive actions (note the first arrow points up):

<div class="eq" markdown="1">
 NATO declares no-fly zone  
 ↑  
NATO leaders are aggressive  
 ↓  
 NATO sends NATO tanks to Ukraine  
 ↓  
 NATO and Russian tanks clash in Ukraine  
 ↓  
 Nuclear weapon launched  
</div>

This could also explain the current probabilities.

## 4.

Is this starting to sound familiar? If we had a market, I’m confident investors would assign a vastly higher price for <var>is charming & good-looking</var> when you condition on <var>reads dynomight</var> than when you condition on <var>doesn’t read dynomight</var>.

Is that because reading dynomight makes you more charming and good-looking? Sadly, no—it’s because such people are more likely to value prime-grade autodidactism.

Does this remind you of another issue in probability and statistics? Like, say, the *issue über alles*?

The problem is:

- Correlation does not imply causation.
- Conditional probabilities don’t imply causation either.
- All conditional prediction markets give you is conditional probabilities.

## 5.

Scott Alexander has [suggested](https://astralcodexten.substack.com/p/open-thread-212) using prediction markets to predict if banned commenters should be reinstated. The idea is that if you get banned, you can write an argument that you will be good and then investors would bet on the odds that Scott would reinstate you if he read your justification, i.e.

<div class="eq" markdown="1">
P[reinstated | justification read].
</div>

This might not work. Suppose that Scott currently pays an assistant to pre-screen the justifications. If the assistant thinks there’s at least an 80% chance someone will be reinstated, they forward their justification to be read, while the rest are ignored. (The assistant gives "ideal" predictions, in the sense that it's impossible to be more accurate given the available information.)

This distorts the market. Assuming people know about the assistant, the market will give at least an 80% probability of reinstatement to *everything*, regardless of how bad it is. (You are guaranteed to make money over time by blindly taking any bet with odds lower than 80%.)

What went wrong? The problem is that the quality of the justification influences if it gets read:

<div class="eq" markdown="1">
Justification good  
 ↓ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ↘ &nbsp;  
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reinstated ← Justification read  
</div>

This same distortion of probabilities happens with almost any selection based on the quality of the justifications. I can't figure out how to make the general case without some grungy calculations, but here's one example: Suppose that Scott looks at only those cases where the prediction market is above 25%.

This will also distort the probabilities upward. Imagine that the market is currently at 30%, but you think the true probability is 20%. What will happen if you short the market? There are two possibilities:

* You are wrong that the market is too high. Then the market is likely to stay above 25%, meaning the bet will activate.
* You are right that the market is too high. Then the market is likely to eventually move down closer to 20% and then the bet won't activate.

That doesn't seem fair, does it? In the situation where you're right, the bet is likely to be canceled, while in situations where you're wrong, the bet goes ahead. The people who think the probabilities are low will accordingly drop out of the market, which distorts the probabilities upwards.

A solution is to read justifications chosen *at random*, without looking at the market prices. This breaks the link from the justification to the event of being read:

<div class="eq" markdown="1">
Justification good  
 ↓ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp; &nbsp;  
 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reinstated ← Justification read  
</div>


Look at that---to make things work, all we needed to do was promise to our conditional prediction market that we will do the conditioning *randomly*.

## 6.

Where are we? Let’s review. Here’s the typical *correlation does not imply causation* story:

1. You can use observational studies to get the correlation between action <var>A</var> and outcome <var>B</var>.
2. But just because <var>A</var> is correlated with <var>B</var> doesn’t mean that *doing* <var>A</var> will make <var>B</var> more likely.
3. For that to be true, you need a particular causal structure for the variables being studied. (No causal path from <var>B</var> to <var>A</var>, no variable <var>C</var> with a causal path to both <var>A</var> and <var>B</var>)
4. You can guarantee the right causal structure by randomizing the choice of <var>A</var>. If you do that, then correlation *does* imply causation.

So far, this article has made this argument:

1. You can use conditional prediction markets to get the probability of outcome <var>B</var> given different actions <var>A</var>.
2. But just because changing the value of A changes the conditional probability of <var>B</var> doesn’t mean that *doing* <var>A</var> changes the probability of <var>B</var>.
3. For that to be true, you need a particular causal structure for the variables being studied. (No causal path from <var>B</var> to <var>A</var>, no variable <var>C</var> with a causal path to both <var>A</var> and <var>B</var>)
4. You can guarantee the right causal structure by randomizing the choice of <var>A</var>. If you do that, then conditional prediction market prices *do* imply causation.

Basically: If you run a prediction market to predict correlations, you get correlations. If you run a prediction market to predict the outcome of a randomized trial, you get causality. But to incentivize people to predict the outcomes of a randomized trial you have to actually *run* a randomized trial, and this is costly.

## 7.

So that’s the problem. What can we do about it? There are several options.

### Get the arrows right

One option is to think carefully about the system you’re studying. If the causal structure is OK (no reverse causality, no confounders), then you’re OK, and a conditional prediction market will give you what you want. But do be careful, because if you’re wrong you’ll silently get meaningless results.

There’s an possible wrinkle here in that perhaps all you *truly* need is that people betting in the market *think* the causal structure is OK. But it seems dangerous to try to exploit this.

### Commit to randomization

We solved the problem with banned commenters by committing to choosing actions randomly. This option always works, but there’s a cruel irony: The whole point of prediction markets is to make good decisions. If you have to behave *randomly* to get good predictions, then what are we even doing here?

Fortunately, there’s a good (and well-known) alternative, which is to randomize decisions *sometimes,* at *random*. You tell people: “I will roll a 20-sided die. If it comes up 1-19, everyone gets their money back and I do what I want. If it comes up 20, the bets activate and I decide what to do using a coinflip.”

What’s nice about this is that you can do whatever you want when 1-19 come up, including making your decisions using the market prices. But you must make decisions randomly *sometimes*, because if bets never activate, no one will waste their time betting in your market.

This is elegant. Oh, and by the way are you THE NSF or DARPA or THE NIH or A BILLIONAIRE WHO WANTS TO SPEND LOTS OF MONEY AND BRAG ABOUT HOW YOU ADVANCED THE STATE OF HUMAN KNOWLEDGE MORE THAN ALL THOSE OTHER LAME BILLIONAIRES WHO WOULDN’T KNOW A HIGH ROI IF IT HIT THEM IN THE FACE? Well how about this:

1. Gather proposals for a hundred RCTs that would each be really expensive but also really awesome. (E.g. you could investigate <var>SALT → MORTALITY</var> or <var>ALCOHOL → MORTALITY</var> or <var>UBI → HUMAN FLOURISHING</var>.)

2. Fund highly liquid markets to predict the outcome of each of these RCTs, conditional on them being funded.  
  * If you have hangups about prison, you might want to chat with the [CFTC](https://en.wikipedia.org/wiki/Commodity_Futures_Trading_Commission) before doing this.
3. Randomly pick 5% of the proposed projects, fund them as written, and pay off the investors who correctly predicted what would happen.

4. Take the other 95% of the proposed projects, give the investors their money back, and use the SWEET PREDICTIVE KNOWLEDGE to pick another 10% of the RCTs to fund for STAGGERING SCIENTIFIC PROGRESS and MAXIMAL STATUS ENHANCEMENT.

Still, I really hope that NATO doesn’t randomize the decision about a no-fly zone.

### Bet re-weighting

Consider again the case where people could bet on the odds of a commenter being reinstated. It would be nice to use a market to do filtering, i.e. only read the justifications that have a probability above 25%. But we saw that would distort the market.

You could also solve this problem using an alternative betting structure. The basic idea is that if the final market probability is above a threshold you always read the justification. If the final market probability is below a threshold, you only read the justification a fraction of the time, but you make the stakes correspondingly larger. For example, we might agree to a bet like this:

1. If the market ends up above 25%, the justification is read. If the person was reinstated you pay me \$1. If the person is not reinstated, I pay you \$4.
2. If the market ends up below 25%, roll a 10-sided die. If the die doesn't come out ten, bets are cancelled and the justification is ignored. If the die *does* comes out 10, the justification is read, and you pay me **\$10** if the person is reinstated, while I pay you **\$40** if the person is not reinstated.

Regardless of the final market price, *in expectation*, I will win \$1 if I'm right that the person will be reinstated and you win \$4 if you're right that they won't. So this market will still incentivize people to bet their true beliefs.

### Natural experiments

Imagine a prediction market for the odds of a war conditional on who wins a presidential election. You couldn’t interpret this causally---maybe candidate X is less likely to cause a war, but if it already looks like war is looming, then people might vote for candidate Y.

But we can’t randomly pick presidents. (That would interfere with our elections which are *really good* and totally *not* as bad as choosing a winner at random, or something.)

Robin Hanson [suggests](https://www.overcomingbias.com/2011/11/conditional-close-election-markets.html) a market that only activates if the votes are very close to even, so that the outcome is *effectively* random.

This isn’t perfect, because an election being close might influence other variables: Imagine that candidate Y likes to undermine the legitimacy of elections. If there’s a clear result it won’t matter, but if X wins narrowly, riots would start and global adversaries might take advantage of the chaos to start wars. In a case like this, a “close call” prediction market might make it look like X is more likely to cause a war even though X is better under most circumstances.

Still, this is a good idea—it’s not that far-fetched to just assume that things like that don’t happen. You can probably invent other markets with the same principle of “bet that activates if a natural experiment happens to occur”.

### The arrow of time

Robin Hanson has also suggested “fire the CEO” prediction markets where people bet on the future price of a company, conditional on a CEO being fired (or not). Of course, if such a market says the price is more likely to go down if the CEO is fired, that doesn’t necessarily mean the CEO is good. The market might be predicting something like this:

<div class="eq" markdown="1">
Recession  
 ↓  
 Company loses money  
 ↓  
 Stock price goes down  
 ↓  
 Company fires CEO  
</div>

An obvious way to deal with this is to use time: Bet on the stock price 2 years from now, conditional on the CEO being fired in the next month.

This eliminates reverse causality. However, it still doesn't guarantee that the market probabilities are causal, because it doesn't eliminate hidden confounders. Maybe everyone knows the CEO is terrible, but hard to fire. But the company was just bought by some billionaire and there are weird rumors that the billionaire hates the CEO and wants to fire them and then drive the company into the ground out of spite:

<div class="eq" markdown="1">
Company fires CEO  
↑  
Billionaire hates CEO  
↓  
Billionaire destroys company  
↓  
Stock price goes down
</div>

If you learned that the CEO gets fired soon, you'd start to suspect that the billionaire really does hate them and plans to destroy the company. So even though the CEO is terrible, you’ll have conditional probabilities that make it look like the CEO is good. Time is no magic bullet.

### Controlled conditional prediction markets

Finally, one could add control variables to the prediction market. Say you want to know if you should fire the CEO, but you’re worried about things being confounded by a recession. Then you could run four prediction markets for the odds of the stock going up conditioned on each combination of the CEO being fired (or not) and there being a recession (or not). If the CEO truly is crap, you’d expect that

<div class="eq" markdown="1">
P[stock up | CEO fired, recession]
</div>

would be larger than

<div class="eq" markdown="1">
P[stock up | no CEO fired, recession],
</div>

and that

<div class="eq" markdown="1">
P[stock up | CEO fired, no recession]
</div>

would be larger than

<div class="eq" markdown="1">
P[stock up | no CEO fired, no recession].
</div>

I don’t like this idea, but that’s mostly because of [general objections to the idea of controlling for variables in observational studies](/control/): It all depends on how you code “recession” and you need to control for *all* the variables that are upstream of both the stock going up and the CEO being fired, but none of the variables that are downstream, etc. That’s usually hard and sometimes literally impossible.

Still, most of social science is built on recklessly controlling for stuff and people seem to believe in it. So don’t do this but if you do please name it after me.