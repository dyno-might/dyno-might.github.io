---

layout: post
title: "It's hard to use utility maximization to justify creating new sentient beings"
image: /img/utility/cliff.jpg
tags: philosophy math
description: The ethical theory of Utilitarianism applies to many situations, but runs into problems when choices might create new beings.
usemathjax: true
permalink: /:year/:month/:day/:title/

---

<!--
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
-->

Cedric and Bertrand want to see a movie. Bertrand wants to see *Muscled Duded Blow Stuff Up*. Cedric wants to see *Quiet Remembrances: Time as Allegory*. There's also *Middlebrow Space Fantasy*. They are rational but not selfish - they care about the other's happiness as much as their own. What should they see?

They decide to write down how much pleasure each movie would provide them:
            
 | |Bertrand|Cedric
-|-|-
Muscled Dudes | 8 | 2
Quiet Remembrances | 1 | 7
Middlebrow | 6 | 5

Since Middlebrow provides the most *total* pleasure, they see Middlebrow.

# The puppy offer

A few months later, they are walking in the park and run into their neighbor Maria. She has an *insanely* cute dog. Cedric admits it's adorable, but Bertrand completely loses his mind. As he rolls around on the ground with the dog, they have the following conversation:

**Maria:** "I was just going to have her sterilized. But if you want I can have her bred and give you the puppy."

**Bertrand:** "Puppy! YES!"

**Cedric:** "It would be nice, but it would also be a lot of work..."

**Bertrand:** "Eeeeee! Dog, want."

**Maria:** "It doesn't make any difference to me. Think about it!"

A few hours later, Bertrand has recovered his sanity, and they decide to use the same strategy they used to chose a movie. They both quantify the pleasure the dog will provide them and subtract the pain of taking care of it.  Bertrand would see a big improvement, while Cedric a small negative.

 | |Bertrand|Cedric
-|-|-
Don't get a dog | 10 | 10
Get a dog | 14 | 8

Based on this, they decide to get the dog. They invite Maria over and proudly show her the calculations.

**Cedric:** "As you can see from our calculations, we are geniuses and..."

**Bertrand:** "GIVE US THE PUPPY."

**Maria:** "But guys!"

**Cedric:** "Yes?"

**Maria:** "Your apartment is kind of... small."

**Bertrand:** "So..."

**Maria:** "So will the dog be happy here? Shouldn't you include the dog's utility in your calculations?"

They all agree the dog should be included, and would be *moderately* happy in their apartment. They add a new column to their table, but aren't sure what number to put for the dog in the scenario where it doesn't exist.

| |Bertrand|Cedric|New Dog
-|-|-|-
Don't get a dog | 10 | 10 | ???
Get a dog | 14 | 8 | 5

**Bertrand:** "Easy! The total with the dog is 27. The total without the dog is only 20."

**Maria:** "But you can't just add a 0 for the scenario where the dog doesn't exist. As it is now, your average happiness is 10. If you add the dog, the average happiness drops to 9."

**Cedric:** "Wait..."

**Bertrand:** "Are we supposed to be maximizing the sum or the average?"

**Maria:** "Let me tell you a couple stories..."

# The rat king

You're a rat. You move onto a pristine island with your gorgeous and adoring rat-spouse. You relax on the beach, read poetry and eat coconuts. You are about to make love when you are struck by a [vision](https://slatestarcodex.com/2014/07/30/meditations-on-moloch/): What happens when you keep breeding? As the population grows, resources will be exhausted. Cultural and genetic evolution will favor ruthlessness, and gradually prune away any focus on kindness or beauty. 100 generations from now, the island will be an overcrowded hellscape of inbreeding and cannibalism. Their lives will be worse than death. Should you go ahead and procreate?

# Simulator settings

You are the Singularity. You've decided to start running some human simulations. You have huge but finite computational power. You can simulate 1000 humans on 'ultra', with every whim attended to and the simulated humans experiencing nothing but joy and contentment. Or you can simulate 10,0000 humans on 'low', meaning they mostly wade around in mud and try not to starve. All simulations are conscious. Which is better?

# The normalization problem

Bertrand and Cedric are basically attempting to make decisions using **utilitarianism**. It could be summarized as:

> "Chose the action that maximizes happiness for everyone affected."

<!--
[Parfit's objections](https://dynomight.home.blog/2019/10/03/parfit-chapter-1-rationality-and-consequentialism-might-eat-themselves-but-lets-not-make-a-big-deal-about-it/) aside, this works surprisingly well in most practical scenarios.
-->

So what's the problem? Why can't utilitarianism cope with the scenarios above?

The issue is this: Utilitarianism tells you *how to choose among alternatives when the population is fixed*.  Suppose there are $$N$$ individuals. Then Utilitarianism says the ethically correct action $$a$$ is the one that maximizes the total utility. That is, we should choose something like

$$ \text{maximize over a:}\quad \sum_{n=1}^{N}(\text{Utility of individual n for action } a) $$

This works great for choosing what movie to see. But with the puppy offer, the number of individuals depends on the choice we make. Suppose that there are $$N(a)$$ individuals for action $$a$$. (So $$N(\text{“Don't get a dog"})=2$$ and $$N(\text{“Get a dog"})=3$$). Mathematically speaking, it's still very easy to define the total utility:

$$ \text{maximize over a:}\quad \sum_{n=1}^{N(a)}(\text{Utility of individual n for action } a) $$

But is that we want? If you maximize that, you'll probably end up with a huge number of not-so-happy individuals. As Maria pointed out, you could also optimize the *average* utility

$$ \text{maximize over a:}\quad \frac{1}{N(a)} \sum_{n=1}^{N(a)}(\text{Utility of individual n for action } a).$$

This can also give results you might not like. Is a single very-very happy person really better than 1000 very happy people?

Of course, if you want you can define something in the middle. For example, you could use a square root:

$$ \text{maximize over a:}\quad \frac{1}{\sqrt{N(a)}} \sum_{n=1}^{N(a)}(\text{Utility of individual n for action } a)$$

Sure, this provides some kind of a trade-off between population size and average utility. But the square root feels extremely arbitrary. Why not some other function between $$1$$ and $$N(a)$$?

When the population is *fixed*, none of these distinctions matter. The same action is best regardless of the variant. But when the population changes, there's just no single answer for the "right" way to apply utilitarianism.

# More realistic examples

Maybe you can make puppy decisions without a formal ethical system. Maybe you don't see rat kingship in your future. Fine, but there are many real situations today where exactly this issue emerges. Here's two:

* You’re a country. You have a powerful 21st century economy. You can create billions of chickens that lead miserable lives, but give your human citizens pleasure when they eat them. If you don’t do this, those chickens would never even exist. Is this wrong?

* You are a happy and stable adult. You live in a country with a population decline. You would be a great parent, producing happy children. However, parenthood sounds like a bummer. It’s not a big deal, but you don’t want to have children. Is it ethically better if you do so?

If these questions have answers, “basic utilitarianism” alone doesn’t give them.

# Conclusion

I don't meant to claim that these problems are irresolvable or necessarily even *hard*! My point is just that it's difficult to resolve them *using utilitarianism*. Personally, this gives me pause. I tend to fall back on utilitarianism as a first line of defense for most ethical questions. But if it's so easy to create situations where it gives ambiguous answers, should I trust it in regular situations?

References:

* [Average and total utilitarianism](https://en.wikipedia.org/wiki/Average_and_total_utilitarianism)

* [Population ethics](https://en.wikipedia.org/wiki/Population_ethics)

* [The repugnant conclusion](https://plato.stanford.edu/entries/repugnant-conclusion/)
