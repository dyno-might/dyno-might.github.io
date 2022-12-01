---
layout: post
title: "Valid arguments with invalid conclusions"
image: /img/valid-invalid/blueberries.jpg
tags: policy
description: "subterfuge, berries, Bayes, billboards, stop signs"
excerpt: "Some time ago, I was driving somewhere with a friend and I claimed that someone was operating with subterfuge. There was an odd silence, after which my friend quietly asked, 'What was that?' Something was wrong. Was she offended? I said, '...subterfuge?' She gave me a brief and somewhat pitying glance, but said nothing."
permalink: /valid-invalid/
background_color: rgb(139,152,158)
category: "rants"
comment:
  substack: https://dynomight.substack.com/p/valid-invalid/
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
---

*Note:* This is a short list of stories I put together on the theory that some lesson would reveal itself in the telling. Having written them, this lesson did not eventuate.

## 1.

Some time ago, I was driving somewhere with a friend and I claimed that someone was operating with *subterfuge*. There was an odd silence, after which my friend quietly asked, "What was that?"

Something was wrong. Was she offended? I said, "...*subterfuge*?"

She gave me a brief and somewhat pitying glance, but said nothing. Eventually, I asked, "What's happening?"

She said, kindly, "It's not *sub*-*ter*-*fyuge*, it's *suh*-*ter*-*fyuge*."

I tightened my neck. "Are you... it..."

She took a breath. Clearly trying to be gentle, she explained, "Something that's hard to detect isn't *sub-tuhl*, is it? It's *suh-tuhl*. Same root."

I blinked. If I missed this, what *else* was I missing? What was I doing just going around and talking, like I owned the place?

**Problem:** It's *sub-ter-fyuge*. But probably the bigger mistake was either of us imagining that any of this mattered?

## 2.

Botanically speaking, a "berry" is a fruit that develops from the ovary of a single flower, where the outer layer of the ovary forms the flesh of the fruit.

So, umm:

![berries Venn diagram](/img/valid-invalid/berries2.svg)

Similarly, a "nut" is a fruit with a single seed and a tough shell that has no built-in line of weakness and does not open at maturity. Thus:

![nuts Venn diagram](/img/valid-invalid/nuts2.svg)

**Problem:** Lots of fields borrow existing words to create technical jargon. But when your roommate complains that you ate all the berries, you shouldn't counter that raspberries are the fusion of multiple ovaries—because your roommate wasn't speaking Botanist.

Similarly, let's spare a thought for the Supreme court in their legendary [1893 ruling that tomatoes are vegetables](https://en.wikipedia.org/wiki/Nix_v._Hedden). Of course they knew this wasn't technically true, but it's not crazy to think that this was Congress' intent when they wrote the Tariff Act of 1883.

![Nix v. Hedden judgment](/img/valid-invalid/nix.svg)

At least, *always* adopting technical jargon would be absurd. If the next farm bill banned the export of "kernels", should it be illegal for mathematicians to publish new [inverse images of zero](https://en.wikipedia.org/wiki/Kernel_(algebra))?

## 3.

Here's how you do Bayesian statistics:

1. You define a prior distribution <var>P[A]</var>.
2. You define a likelihood <var>P[B|A]</var>.
3. You use math to calculate the posterior <var>P[A|B]</var>.

Here <var>A</var> is the unobserved variable you want to estimate, e.g. "number of squirrels living in the attic". Meanwhile, <var>B</var> is your data, e.g. "the kids have complained about being awoken by muk-muk sounds on 12 of the last 14 nights". Then, the posterior would try to answer how many squirrels there were, given all the muk-muk sounds.

Here are the most common criticisms of Bayesian statistics:

1. Where does the prior come from?
2. You just make up the prior?
3. The prior comes out of your brain?
4. What if there's a mistake in the prior?
5. "Nice post! Here are 8000 words on why subjective probabilities are a moral abomination."
6. The prior.

**Problem:** I think these criticisms of the prior are misguided, not because they're invalid, but because there's an even stronger argument: Every concern about the prior *also applies to the likelihood*. It also comes out of your brain. You can also get it wrong. Yet likelihoods are (often) more complex, and so easier to screw up. And—unlike with the prior—collecting enough data won't make mistakes in the likelihood disappear.

If you want to criticize a Bayesian model, I suggest one of these templates:

1. In this situation, the prior is bad because of [*reasons*].
2. In this situation, the likelihood is bad because of [*reasons*].

These are rare. I think that's because despite being logically stronger, they are *rhetorically* weaker. You have to actually engage with the situation. And if you discuss possible flaws in the likelihood, it becomes obvious that *other* forms of statistics *also* involve assumptions akin to those in the likelihood, and those assumptions are similarly tenuous. Safer to stick to fully-general philosophical quibbling.

## 4.

When I was young, my dad asked me what I thought of a ballot initiative that would have restricted new billboards. I was just at the age of a dawning political consciousness, so I thought about it for a couple of days, then said something like this:

> I hate billboards. But it's bad for the government to tell people what they can put on their own land. It's close to violating freedom of speech. Are we going to have a board that decides what is "advertising" and what is "valid" speech?

As I talked, my dad nodded and stroked his chin. But when I asked what he thought, he said he was still going to vote against the billboards. When I asked why, he paused and then gave this argument:

> Fuck the billboards.

**Problem:** It's rare to have your position on an issue reversed by three words. I wasn't sure *what* was wrong with my argument, but I knew something was.

Over the next few years, I ran into the standard libertarian ideas: You don't need to compromise rights to restrict billboards. Private companies could build tollways and advertise that they were billboard-free. We could treat billboards as an externality and pay people not to have them. A corporation could buy the land for a city and sell restricted rights for sub-plots!

But when I read stuff like this, I always had "fuck the billboards" looming in the back of my mind. Slowly, it took on a meaning like this:

> Alternative governance patterns are cool. But until they're proven viable, shouldn't we try to effectively use the patterns that exist now?

**Deeper problem:** This story worries me: If my dad had given this more explicit argument, would it have convinced me? If I had heard the Libertarian Reveries *before* "fuck the billboards", would I still think what I think now? Are all beliefs fake, the consequences of randomly hearing the right words at the right age to trigger an emotional reaction that will ferment for years and slowly transform us?

## 5.

The purpose of a stop sign is to prevent vehicles from running into each other when roads intersect. Often there are stop signs for both roads (4-way stops). But sometimes one road has higher traffic than the other, so there are only stop signs for the lower-traffic road (2-way stops).

Now, what happens if you confuse these? If you're at a 4-way stop but you think it's a 2-way stop, you might hesitate and waste some time. If you're at a 2-way stop but you think it's a 4-way stop you might proceed into the intersection and then get hit by oncoming traffic.

| True | Perception | Worst-case result |
|-|-|
| 4-way | 4-way | 👍 |
| 2-way | 2-way | 👍 |
| 4-way | 2-way | Minor inconvenience |
| 2-way | 4-way | ☠️ |

So what do we do? Logically, we'd label every sign as 2-way or 4-way. The poles are already there, so this couldn't be too expensive.

But if we didn't do that, we'd mark the *2-way* signs, right?

Surely we wouldn't leave most signs ambiguous but label a random subset of *4-way* signs, leaving everyone to squint looking for the back of other signs that are distant, perpendicular, and possibly blocked by foliage—and not even bother to paint the backs of the signs in some high-visibility color?

**Problem**: Hahaha.

{% comment %}
(I know there's a conspiracy theory that this forces everyone to look carefully and thereby increases safety. But if that's true, why stop there? Why not disable a random subset of the bulbs in traffic lights? Why not remove some signs altogether?)
{% endcomment %}