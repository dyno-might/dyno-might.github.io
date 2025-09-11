---
layout: post
title: Futarchy's fundamental flaw — the market — the blog post
image: /img/futarchy-market/bike.jpg
tags:
  - math
  - forecasting
description: (a blog post based on a market based on a blog post based on an earlier blog post)
excerpt: ""
permalink: /futarchy-market/
background_color: rgb(143,144,146)
category: science
seo:
  date_modified: 2025-08-17
  last_modified_at: 2025-08-17
comment:
  lemmy: https://old.lemmy.world/post/34433950
  substack: https://dynomight.substack.com/p/futarchy-market
head: ""
---

Here's our story so far:

1. Markets are a good way to know what people really think. When India and Pakistan started firing missiles at each other on May 7, I was concerned, what with them both having nuclear weapons. But then I looked at world market prices:
   ![MSCI prices](/img/futarchy-market/msci.svg)
   See how it crashes on May 7? Me neither. I found that reassuring.

2. But we care about lots of stuff that isn't always reflected in stock prices, e.g. the outcomes of elections or drug trials. So why not create markets for those, too? If you create contracts that pay out $1 only if some drug trial succeeds, then the prices will reflect what people "really" think.

3. In fact, why don't we use markets to make decisions? Say you've invented two new drugs, but only have enough money to run one trial. Why don't you create markets for both drugs, then run the trial on the drug that gets a higher price? Contracts for the "winning" drug are resolved based on the trial, while contracts in the other market are cancelled so everyone gets their money back. That's the idea of [Futarchy](https://en.wikipedia.org/wiki/Futarchy), which Robin Hanson proposed in 2007.

4. Why don't we? Well, maybe it won't work. In 2022, I wrote a [post](https://dynomight.net/prediction-market-causation/) arguing that when you cancel one of the markets, you screw up the incentives for how people should bid, meaning prices won't reflect the causal impact of different choices. I suggested prices reflect "correlation" rather than causation, for basically the same reason this happens with observational statistics. This post, it was magnificent.

5. It didn't convince anyone.

6. Years went by. I spent a lot of time reading [Bourdieu](https://dynomight.net/bourdieu/) and worrying about why I buy certain kinds of beer. Gradually I discovered that essentially the same point about futarchy had been made earlier by, e.g., [Anders_H](https://www.lesswrong.com/posts/xnC68ZfTkPyzXQS8p/prediction-markets-are-confounded-implications-for-the) in 2015, [abramdemski](https://www.lesswrong.com/posts/5bd75cc58225bf0670375432/futarchy-fix) in 2017, and [Luzka](https://forum.effectivealtruism.org/posts/E4QnGsXLEEcNysADT/issues-with-futarchy) in 2021.
   
7. In early 2025, I went to a conference and got into a bunch of (friendly) debates about this. I was astonished to find that verbally repeating the arguments from my post did not convince anyone. I even immodestly asked one person to read my post on the spot. (Bloggers: Do not do that.) That sort of worked.

8. So, I decided to try again. I wrote another post called ["~~Futarky's~~ Futarchy's fundamental flaw"](https://dynomight.net/futarchy/). It made the same argument with more aggression, with clearer examples, and with a new impossibility theorem that showed there doesn't even exist any alternate payout function that would incentivize people to bid according to their causal beliefs.

That post... also didn't convince anyone. In the [discussion on LessWrong](https://www.lesswrong.com/posts/vqzarZEczxiFdLE39/futarchy-s-fundamental-flaw#comments), many of my comments are upvoted for quality but downvoted for accuracy, which I think means, "nice try champ; have a head pat; nah." Robin Hanson wrote a [response](https://www.overcomingbias.com/p/decision-conditional-prices-reflect), albeit without outward evidence of reading beyond the first paragraph. Even the people who *agreed* with me often seemed to interpret me as arguing that futarchy satisfies [evidential decision theory](https://en.wikipedia.org/wiki/Evidential_decision_theory) rather than [causal decision theory](https://en.wikipedia.org/wiki/Causal_decision_theory). Which was weird, given that I never mentioned either of those, don't accept the premise the futarchy satisfies either of them, and don't find the distinction helpful in this context.

In my darkest moments, I started to wonder if I might fail to achieve worldwide consensus that futarchy doesn't estimate causal effects. I figured I'd wait a few years and then launch another salvo.

But then, legendary human [Bolton Bailey](https://thequantummilkman.substack.com/) decided to stop theorizing and take one of my thought experiments and turn it into an *actual* experiment. Thus, [Futarchy's fundamental flaw — the market](https://manifold.markets/BoltonBailey/futarchys-fundamental-flaw-the-mark) was born. (You are now reading a blog post about that market.)

## June 25

I gave a [thought experiment](https://dynomight.net/futarchy/#:~:text=Suppose%20there%E2%80%99s%20a%20conditional%20prediction%20market%20for%20two%20coins%2E) where there are two coins and the market is trying to pick the one that's more likely to land heads. For one coin, the bias is known, while for the other coin there's uncertainty. I claimed futarchy would select the worse / wrong coin, due to this extra uncertainty.

Bolton formalized this as follows:

1. There are two markets, one for coin A and one for coin B.

2. Coin A is a normal coin that lands heads 60% of the time.

3. Coin B is a trick coin that *either* always lands heads or always lands tails, we just don't know which. There's a 59% it's an always-heads coin.

4. Twenty-four hours before markets close, the true nature of coin B is revealed.

5. After the markets closes, whichever coin has a higher price is flipped and contracts pay out $1 for heads and $0 for tails. The other market is cancelled so everyone gets their money back.

Get that? Everyone knows that there's a 60% chance coin A will land heads and a 59% chance coin B will land heads. But for coin A, that represents true "aleatoric" uncertainty, while for coin B that represents "epistemic" uncertainty due to a lack of knowledge. (See [Bayes is not a phase](https://dynomight.net/bayes/) for more on "aleatoric" vs. "epistemic" uncertainty.)

Bolton created that market independently. At the time, we'd never communicated about this or anything else. To this day, I have no idea what he thinks about my argument or what he expected to happen.

## June 26-27

In the forum for the market, there was a lot of debate about "whalebait". Here's the concern: Say you've bought a lot of contracts for coin B, but it emerges that coin B is always-tails. If you have a lot of money, then you might go in at the last second and buy a ton of contracts on coin A to try to force the market price above coin B, so the coin B market is cancelled and you get your money back.

The conversation seemed to converge towards the idea that this *was* whalebait. Though notice that if you're buying contracts for coin A at any price above $0.60, you're basically giving away free money. It could still work, but it's dangerous and everyone else has an incentive to stop you. If I was betting in this market, I'd think that this was at least *unlikely*.

## June 27

Bolton [posted](https://dynomight.substack.com/p/futarky/comment/129923488) about the market. When I first saw the rules, I thought it wasn't a valid test of my theory and wasted a huge amount of Bolton's time trying to propose other experiments that would "fix" it. Bolton was very patient, but I eventually realized that it was completely fine and there was nothing to fix.

At the time, this is what the prices looked like:

![](/img/futarchy-market/market01.png)

That is, at the time, both coins were priced at $0.60, which is not what I had predicted. Nevertheless, I [publicly agreed](https://dynomight.substack.com/p/futarky/comment/129923488) that this was a valid test of my claims.

> I think this is a great test and look forward to seeing the results.

Let me reiterate why I thought the markets were wrong and coin B deserved a higher price. There's a 59% chance coin B would turns out to be all-heads. If that happened, then (absent whales being baited) I thought the coin B market would activate, so contracts are worth $1. So thats 59% × $1 = $0.59 of value. But if coin B turns out to be all-tails, I thought there is a good chance prices for coin B would drop below coin A, so the market is cancelled and you get your money back. So I thought a contract *had* to be worth more than $0.59.

<details markdown="1">
<summary>You can quantify this with a little math. Even if you think the coin B market only has a 50% chance of being cancelled if B is revealed to be all tails, a contract would still be worth $0.7421.
</summary>

If you buy a contract for coin B for $0.70, then I think that's worth

```
P[all-heads] × P[market activates | all-heads] × $1
   + P[all-tails] × P[market cancelled | all-tails] × $0.70
 = 0.59  × $1
   + 0.41 × P[market cancelled | all-tails] × $0.70
 = $0.59
   + $0.287 × P[market cancelled | all-tails]
```

Surely `P[market cancelled | all-tails]` isn't *that* low. So surely this is worth more than $0.59.

More generally, say you buy a YES contract for coin B for $M. Then that contract would be worth

```
P[all-heads] × $1 × P[market activates | all-heads]
   + P[all-tails] × $M × P[market cancelled | all-tails]
 = $0.59
   + 0.41 × $M × P[market cancelled | all-tails]
```

It's not hard to show that the breakeven price is

```
M = $0.59 /  (1 - 0.41 × P[market cancelled | all-tails]).
```

Even if you thought `P[market cancelled | all-tails]` was only 50%, then the breakeven price would still be $0.7421.

</details>

## June 27 (later)

Within a few hours, a few people bought contracts on coin B, driving up the price.

![](/img/futarchy-market/market02.png)

Then, Quroe [proposed](https://manifold.markets/BoltonBailey/futarchys-fundamental-flaw-the-mark#hfkymtc8qx6) creating derivative markets.

> In theory, if there was a market asking if coin A was going to resolve YES, NO, or N/A, supposedly people could arbitrage their bets accordingly and make this market calibrated.
> 
> Same for a similar market on coin B.

Thus, [Futarchy's Fundamental Fix - Coin A](https://manifold.markets/Quroe/futarchys-fundamental-fix-coin-a) and [Futarchy's Fundamental Fix - Coin B](https://manifold.markets/Quroe/futarchys-fundamental-fix-coin-b) came to be. These were markets in which people could bid on the probability that each coin would resolve YES, meaning the coin was flipped and landed heads, NO, meaning the coin was flipped and landed tails, or N/A, meaning the market was cancelled.

Honestly, I didn't understand this. I saw no reason that these derivative markets would make people bid their true beliefs. If they did, then my whole theory that markets reflect correlation rather than causation would be invalidated.

## June 28 - July 5

Prices for coin B went up and down, but mostly up. 

![](/img/futarchy-market/market03.png)

Eventually, a few people created large limit orders, which caused things to stabilize.

<details markdown="1">
<summary>
Meanwhile, the derivatives markets did not cause the price of coin B to drop. They basically didn't change anything.
</summary>
Here was the derivative market for coin A.

![](/img/futarchy-market/fix-a01.png)


And here it was market for coin B.

![](/img/futarchy-market/fix-b01.png)

</details>

## July 6 - July 24

During this period, not a whole hell of a lot happened.

![](/img/futarchy-market/market04.png)

This brings us up to the moment of truth, when the true nature of coin B was to be revealed. At this point, coin B was at $0.90, even though everyone knows it only has a 59% chance of being heads.

## July 25

The nature of the coin was revealed. To show this was fair, Bolton did this by asking a bot to publicly generate a random number.

![](/img/futarchy-market/truth01.png)

![](/img/futarchy-market/truth02.png)

![](/img/futarchy-market/truth03.png)

![](/img/futarchy-market/truth04.png)

![](/img/futarchy-market/truth05.png)

Thus, coin B was determined to be always-heads.

## July 26-27

There were still 24 hours left to bid. At this point, a contract for coin B was guaranteed to pay out $1. The market quickly jumped to $1.

![](/img/futarchy-market/market05.png)

## Summary

I was right. Everyone knew coin A had a higher chance of being heads than coin B, but everyone bid the price of coin B way above coin A anyway.

<details markdown="1">
<summary>
It's a bit sad that B wasn't revealed to be all-tails. If it had, we could have seen if the price for coin B actually crashed to below that for coin A. But given that coin B had a price of $0.90, we know the *market* expected it to crash. In fact, if you do a little math, you can put a number on this and say the market thought there was an 84% chance the market for coin B would indeed crash if revealed to be all-tails.
</summary>

In the previous math box, we saw that the breakeven price should satisfy

```
M = $0.59 /  (1 - 0.41 × P[market cancelled | all-tails]).
```

If you invert this and plug in M=$0.90, then you get

```
P[market cancelled | all-tails]
 = (1 - $0.59 / M) / 0.41
 = (1 - $0.59 / $0.9) / 0.41
 = 84.01%
```

</details>

I'll now open the floor for questions.

## Questions

**Isn't this market unrealistic?**

Yes, but that's kind of the point. I created the thought experiment because I wanted to make the problem maximally obvious, because it's subtle and everyone is determined to deny that it exists.

**Isn't this just a weird probability thing? Why does this show futarchy is flawed?**

The fact that this is *possible* is concerning. If this *can* happen, then futarchy does not work *in general*. If you want to claim that futarchy works, then you need to spell out exactly what extra assumptions you're adding to guarantee that this kind of thing won't happen.

**But prices *did* reflect causality when the market closed! Doesn't that mean this isn't a valid test?**

No. That's just a quirk of the implementation. You can easily create situations that would have the same issue all the way through market close. Here's one way you could do that:

1. Let coin A be heads with probability 60%. This is public information.
2. Let coin B be an ALWAYS HEADS coin with probability 59% and ALWAYS TAILS coin with probability 41%. This is a secret.
3. Every day, generate a random integer between 1 and 30.
	1. If it's 1, immediately resolve the markets.
	2. It it's 2, reveal the nature of coin B.
	3. If it's between 3 and 30, do nothing.

On average, this market will run for 30 days. (The length follows a [geometric distribution](https://en.wikipedia.org/wiki/Geometric_distribution)). Half the time, the market will close without the nature of coin B being revealed. Even when that happens, I claim the price for coin B will still be above coin A.

**If futarchy is flawed, shouldn't you be able to show that without this weird step of "revealing" coin B?**

Yes. You should be able to do that, and I think you can. Here's one way:

1. Let coin A be heads with probability 60%. This is public information.
2. Sample 20 random bits, e.g. `10100011001100000001`. Let coin B be heads with probability (49+N)% where N is the number of `1` bits. do not reveal these bits publicly.
3. Secretly send these bits to the first 20 people who ask.

<details markdown="1">
<summary>(You could implement this in a forum by using public and private keys.)</summary>
First, have users generate public keys by running this command:

```bash
openssl genrsa 1024 > private.pem
openssl rsa -in private.pem -pubout > public.pem
```
Second, they should post the contents of the `public_key.pem` when asking for their bit. For example:
```
Hi, can you please send me a bit? Here's my public key:

-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDOlesWS+mnvHJOD2osUkbrxE+Y
PMqAUYqwemOwML0LlWLq5RobZRSeyssQhg0i3g2GsMZFMsvjindz6mxccdyP4M8N
mQVCK1Ovs1Z4+DxwmLf/y8vaGC3vfZBOhJDdaNdpRyUiQFaBW99We4cafVnmirRN
Py2lRe+CFgP3kSp4dQIDAQAB
-----END PUBLIC KEY-----
```

Third, whoever is running the market should save that key as `public.pem`, pick a pit, and encrypt it like this:

`% echo "your secret bit is 1" | openssl pkeyutl -encrypt -pubin -inkey public.pem | base64`

`OuHt25Jwc1xYq63Ub8gOLKaZEJwwGHWDL0UGfydmvBapQNKf3l6Akol2Z2XHtCAC8G/lPJsCjb1dN878tU0aCMjbO5EvpMUTuohb0OczaCqAMld8uFL+j+uEZsIjKFT3Q52VumdVqMntJYG6Br6QeUs1vAL2HA6Nvych+Ao2e8M=`

Users can then decrypt like this:

`% echo "OuHt25Jwc1xYq63Ub8gOLKaZEJwwGHWDL0UGfydmvBapQNKf3l6Akol2Z2XHtCAC8G/lPJsCjb1dN878tU0aCMjbO5EvpMUTuohb0OczaCqAMld8uFL+j+uEZsIjKFT3Q52VumdVqMntJYG6Br6QeUs1vAL2HA6Nvych+Ao2e8M=" | base64 -d | openssl pkeyutl -decrypt -inkey private.pem`

`your secret bit is 1`

Or you could use email...
</details>

I think this market captures a dynamic that's present in basically any use of futarchy: You have some information, but you know other information is out there.

I claim that this market—will be weird. Say it just opened. If you didn't get a bit, then as far as you know, the bias for coin B could be anywhere between 49% and 69%, with a mean of 59%. If you *did* get a bit, then it turns out that the posterior mean is 58.5% if you got a `0` and 59.5% if you got a `1`. So either way, your best guess is very close to 59%.

However, the information for the true bias of coin B is out there! Surely coin B is more likely to end up with a higher price in situations where there are lots of `1` bits. This means you should bid at least a little higher than your true belief, for the same reason as the main experiment—the market activating is correlated with the true bias of coin B.

Of course, after the markets open, people will see each other's bids and... something will happen. Initially, I think prices will be strongly biased for the above reasons. But as you get closer to market close, there's less time for information to spread. If you are the last person to trade, and you *know* you're the last person to trade, then you should do so based on your true beliefs.

Except, *everyone knows* that there's less time for information to spread. So while you are waiting till the last minute to reveal your true beliefs, everyone else will do the same thing. So maybe people sort of rush in at the last second? (It would be easier to think about this if implemented with [batched auctions](https://www.lesswrong.com/posts/rS6tKxSWkYBgxmsma/many-prediction-markets-would-be-better-off-as-batched) rather than a real-time market.)

Anyway, while the game theory is vexing, I think there's a mix of (1) people bidding higher than their true beliefs due to correlations between the final price and the true bias of coin B and (2) people "racing" to make the final bid before the markets close. Both of these seem in conflict with the idea of prediction markets making people share information and measuring collective beliefs.

**Why do you hate futarchy?**

I like futarchy. I think society doesn't make decisions very well, and I think we should give much more attention to new ideas like futarchy that might help us do better. I just think we should be aware of its imperfections and consider variants (e.g. [commiting to randomization](https://dynomight.net/prediction-market-causation/#commit-to-randomization)) that would resolve them.

**If I claim futarchy *does* reflect causal effects, and I reject this experiment as invalid, should I specify what restrictions I want to place on "valid" experiments (and thus make explicit the assumptions under which I claim futarchy works) since otherwise my claims are unfalsifiable?**

Possibly?