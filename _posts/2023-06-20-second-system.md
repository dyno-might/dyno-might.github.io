---
layout: post
title: The second system problem
image: /img/second-system/sponge.jpg
tags:
  - AI
description: Building a safe AI ≠ preventing all unsafe AI
excerpt: In The Vulnerable World Hypothesis, Nick Bostrom imagines we found a technological "black ball"—say a way to make a nuclear weapon with just some glass, some metal, and a battery. He concludes that society in our current "semi-archic default condition"—could not survive such a discovery. We'd have to build a panopticon to watch everything everyone does, along with a world government to rigidly enforce "no messing around with glass and metal" in every corner of the planet everywhere forever.
permalink: /second-system/
background_color: rgb(232,220,206)
category: science
---

{% comment %}
<span style="font-size:80%">
[<em>Epistemic status</em>: Attempted exploit of Cunningham's law]
</span>
{% endcomment %}

## 1.

In [*The Vulnerable World Hypothesis*](https://nickbostrom.com/papers/vulnerable.pdf), Nick Bostrom imagines we found a technological "black ball"—say a way to make a nuclear weapon with just some glass, some metal, and a battery. He concludes that society in our current "semi-archic default condition" could not survive such a discovery. We'd have to build a panopticon to watch everything everyone does, along with a world government to rigidly enforce "*no messing around with glass and metal*" in every corner of the planet everywhere forever.

## 2.

So here's a common argument:

1. Superhuman AI would be *dangerous by default*. It's hard to predict what something vastly smarter than us would do, and the example of how *we* treat sentient beings less intelligent than *us* is not encouraging.
  
2. But if we're careful, we can figure out how to build *safe AI* that will be nice to us.
  
3. So let's figure that out, now, immediately, so we can be safe.

Let's just assume the first two points are true. Because... am I missing something here?

## 3.

Assume AI is dangerous by default, but safe AI is possible. Then here's a little daydream:

1. Since AIs are cool, you decide to build one.
  
2. Fortunately, you are smart and careful, so you solve the insanely difficult problem of how to make an AI that would never hurt anyone (nor build a 2nd AI that could hurt anyone, ad infinitum), then build your AI and it works and is totally harmless, good job!
  
3. I see how cool your AI is and decide to make my own.
  
4. Unfortunately, I am dumb and sloppy and don't correctly make my AI safe so after I turn it on it makes a nanovirus cobalt bomb and everyone dies. :(
  

## 4.

If AI is dangerous by default then figuring out how to build a safe AI is not enough. Don't you also need to make sure no one builds an *unsafe* AI, anywhere, forever?

![building a safe AI is easier than stopping anyone from building an unsafe AI anywhere ever for the rest of time](/img/second-system/hardness2.svg)

## 5.

Say we already knew how to build safe AI. How could we block unsafe AIs?

There are some obvious directions. We might regulate building AIs, try to keep AI research secret, restrict access to AI hardware, and/or build that lovely worldwide total surveillance state.

Maybe those can work. But they seem *orthogonal* to the technical problem of alignment. And also perhaps *harder* than the technical problem of alignment?

(See also: [Tamsin Leake](https://www.lesswrong.com/posts/bG7yKSRWBaMou7t93/my-current-outlook-on-ai-risk-mitigation#sponge_coordination) and [Eliezer Yudkowsky](https://www.lesswrong.com/posts/uMQ3cqWDPHhjtiesc/agi-ruin-a-list-of-lethalities/#:~:text=Building,actor) on "sponge coordination".)

## 6.

Imagine we lived in the "*metal+glass+battery=nuke*" universe. In parallel with trying to stop people from making nukes, we'd surely try to minimize the damage that any one nuke could do. The obvious way to do this would be to eliminate large cities so that the blast radius of any one bomb wouldn't contain too many people or too much critical infrastructure.

In principle, this could work OK. According to [NUKEMAP](https://nuclearsecrecy.com/nukemap/), the most powerful nuclear warhead in the US stockpile detonated in an airburst would have a heavy damage blast radius of 3km. If people were distributed at the continental US average population density of 42.9 people/km², that would mean 1213 people. Not good, but not the end of civilization.

Of course, the problem is that the population density of Manhattan is not 42.9 people/km², but around 670 times higher. Spacing everyone out equally would mean the end of civilization "as we know it".

Incidentally, Einstein discussed this [in 1947](https://www.theatlantic.com/magazine/archive/1947/11/atomic-war-or-peace/305443/):

> A danger that cannot be averted had perhaps better be forgotten; or a danger against which every possible precaution has been taken also had probably better be forgotten. That is, if the United States had dispersed its industries and decentralized its cities, it might be reasonable for people to forget the peril they face.

He was still against dismantling all the cities for complicated second-order game theory reasons. But also, back in 1934 he was [in favor of dismantling cities](https://cooperative-individualism.org/einstein-albert_the-world-as-i-see-it.pdf#page=53) for socialism-type reasons, so who knows.

## 7.

Analogously, could we reorganize society so that it's impossible for any one AI to do too much damage?

This seems even harder than for nukes because we're assuming our adversary is much smarter than us. Maybe we're worried about superviruses so we—at enormous cost—split the population up into "cells" of 5 million people. But then the AI just makes the AI transmittable by birds. Or releases chemicals to kill the ozone layer and eliminate all food. Or whatever.

Maybe this is possible. But it also seems mostly orthogonal to alignment research.

## 8.

There's one clear way in which "*how to build safe AI*" could have implications for "*how to stop anyone from making unsafe AI*". We could try to build an **AI guardian**—an AI that is *so* safe that not only will it not hurt anyone, it will also *protect* us from any dangerous AIs that might come later.

Maybe... but notice that many existing alignment strategies are in conflict with the goal of having the guardian protect us:

- Say your guardian is a [**bounded AI**](https://www.lesswrong.com/posts/ngEvKav9w57XrGQnb/cognitive-emulation-a-naive-ai-safety-proposal) with limited capabilities. Then it will be outsmarted by my dangerous unbounded AI.
  
- Say your guardian is a [**genie AI**](https://astralcodexten.substack.com/p/janus-simulators) that can only follow orders but not pursue goals independently. Then it will lose to my dangerous **agent AI** without those restrictions.
  
- Say your guardian is an [**oracle AI**](https://astralcodexten.substack.com/p/janus-simulators) that can only answer questions but never *do* anything. Then it couldn't even beat my agent AI at Starcraft.
  
- Say you put your guardian in a **box** with restricted access to the world. Then it's not going to be able to stop my dangerous AI from stealing the nuclear launch codes.
  

## 9.

So OK. You give your guardian AI full control of all the weapons systems, to make sure they aren't used for evil. And you give it the ability to monitor the world biosphere and autonomously release viruses, so that if my AI makes super-plauge, the guardian can quickly release anti-super-plague. And you use a different alignment strategy—perhaps you make it **supervised** by a less powerful AI or you make it **interpretable** so you can supervise it yourself.

That's not super comforting, but say it works. Then notice a further problem: If whatever you did to align the guardian makes it less *effective*, (slower, less smart, less informed, smaller action space) then it will still lose if someone else builds an AI without those restrictions.

So after you build a godlike guardian AI+panopticon and give it control of everything, you either:

1. Tell the guardian to stop anyone else from building new AIs, by whatever means necessary, or
  
2. Hope that the guardian, by virtue of being first, will have such a lead that no other AI can ever catch up, or
  
3. Hope that, for some reason, safety doesn't decrease effectiveness. That is, if you find the most effective AI in the set of all AIs, and then find the most effective AI in the subset of *safe* AIs, the two happen to be equally capable.
  

![max effective safe AI = max effective all AI](/img/second-system/whew2.svg)

Is this the outcome we're hoping for? Because if not, then it seems like technical alignment is only the beginning of our problems.