---
layout: post
title: "Comparative advantage and when to blow up your island"
image: /img/comparative-advantage/island.jpg
tags: explainer economics gameTheory
permalink: /:year/:month/:day/:title/
---

<head>
<style>

.figure {
  display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 70%
}

</style>
</head>

Economists say free trade is good because of "comparative advantage". But what is comparative advantage? Why is it good? 

This is sometimes considered an arcane part of economics. ([Wikipedia](https://en.wikipedia.org/wiki/Comparative_advantage#Ricardo's_example) defines it using "autarky".) But it's really a very simple idea. Anyone can use it to understand the world and make decisions.

# I Islands

<div class="figure"><img src="/img/comparative-advantage/you.png" alt="you on an island" max-width="75%" min-width="50%" /></div>

Say you live alone on an island. 


Each week you gather and eat 10  coconuts and 10 bananas. It takes you five minutes to gather a coconut, and 10 minutes for a banana. Thus, you work 150 minutes per week.


|        |You Need|Time to gather one|Time You Spend|
|--------|--------|------------------|--------------|
|Coconuts|10      |	5 minutes	       |50 minutes    |
|Bananas |10      |	10 minutes	     |100 minutes   |
|			   |        |                  |Total: 150 minutes|

I live on a nearby island.

<div class="figure"><img src="/img/comparative-advantage/me.png" alt="both of us on islands" width="65%"/></div>

Just like you I eat 10 coconuts and 10 bananas per day. But *unlike* you, I'm terrible at everything.

|        |I Need|Time to gather one|Time I Spend|
|--------|--------|------------------|------------------|
|Coconuts|10      | 60 minutes       |600 minutes       |
|Bananas |10      | 30 minutes       |300 minutes       |
|        |        |                  |Total: 900 minutes|


Since I'm so incompetent, I need to work a lot more than you -- six times as much.

# II The Bridge

Thus, we live our lives until one day a bridge appears between the islands.

<div class="figure"><img src="/img/comparative-advantage/bridge.png" alt="a bridge appears" max-width="75%" min-width="50%"/></div>

We are both peaceful. We will not coerce each other, but are otherwise completely selfish. What will happen?

Intuitively, you value bananas more, while I value coconuts more. So it's natural to trade my bananas for your coconuts. We agree as follows: Each week, you gather 20 coconuts, and I gather 20 bananas. Then, I trade 10 of my bananas for 10 your coconuts. It’s easy to check that this will make *both* of us better off.


|        |You Gather|Time to gather one|Time You Spend|
|--------|--------|------------------|--------------|
|Coconuts|20      | 5 minutes        |100 minutes    |
|Bananas |0       | 10 minutes       |0 minutes   |
|        |        |                  |Total: 100 minutes|


|        |I Gather|Time to gather one|Time I Spend|
|--------|--------|------------------|------------------|
|Coconuts|0       | 60 minutes       |0 minutes       |
|Bananas |20      | 30 minutes       |600 minutes       |
|        |        |                  |Total: 600 minutes|

In one sense, it's obvious that trade makes us both better off. If it didn't we wouldn't both agree to it! But comparative advantage explains how. You have an *advantage* at everything. But I have a *comparative advantage* at bananas, because my ratio (banana time) / (coconut time) is lower than yours. And if we both concentrate our efforts on the thing we have a comparative advantage at, we are both better off.

This is why economists like free trade. If different producers have different relative abilities, everyone can benefit from specializing. This is true even if one producer is better at everything.

Beyond trade, this is an important lesson for life. Choosing your career path? Dividing up chores with your partner? Think about comparative advantage!

# III Complexities

The real world, of course, is more complex. For example:

* There might be transportations costs.
* It might get harder to find coconuts as you gather more of them.
* There might be more goods to trade.

More sophisticated models can deal with these complications. The math gets more complex, but more or less the same conclusion arises. There is one complication that's a bit special: 

* There might be more than two people.

In this case, introducing trade can make *individual people* worse off: Suppose you live with me on an island, but you're incapable of gathering bananas. Since you need them to live, I can demand a huge number of coconuts for one banana. When a bridge opens up to another island, you might get a better trade. This will help you, but actually *hurt* me. Still, introducing free trade still makes people better off "on the whole".

In this subtlety, Politics emerges. In principle, one can always use free trade plus a set of wealth transfers to make every individual better off. But that's a nightmare in practice: It would require a central authority to predict what set of trades the market will decide on. So we're left with a mess.

# IV ZOPA

But even in this toy model of two people on two islands, I skipped an important step. How did we decide to trade 10 coconuts for 10 bananas? I might say: “I’ll trade 7 bananas for 10 of coconuts. Take it or leave it!”

Of course, this would be great for me, and worse for you than our original trade. But it’s easy to check that this is better for you than no trade at all.



|        |You Gather|Time to gather one|Time You Spend|
|--------|--------|------------------|--------------|
|Coconuts|20      | 5 minutes        |100 minutes    |
|Bananas |3       | 10 minutes       |30 minutes   |
|        |        |                  |Total: 130 minutes|


|        |I Gather|Time to gather one|Time I Spend|
|--------|--------|------------------|------------------|
|Coconuts|0       | 60 minutes       |0 minutes       |
|Bananas |17      | 30 minutes       |510 minutes       |
|        |        |                  |Total: 510 minutes|

Now, what possible banana/coconut exchange rates could we arrive at?  I’d be happiest paying you nearly zero bananas for each coconut. On the other hand, I'd never agree to pay you three bananas per coconut -- it would be "cheaper" for me to just make the coconuts myself. I'd never agree to trade more than two.

<div class="figure"><img src="/img/comparative-advantage/im_happy.png" alt="bananas per coconut" width="65%"/></div>

Thus, I benefit from any trade where I pay you between 0 and 2 bananas for one coconut. These are the only trades I'd ever agree to.

<div class="figure"><img src="/img/comparative-advantage/my_range.png" alt="my range" width="65%"/></div>


Of course, I’d prefer to pay you fewer bananas! So I’d prefer a rate to the left end of this range.

Conversely, it takes you twice as long to make banana as a coconut. You’d be thrilled if I paid you 4 bananas per coconut, but you’d never accept less than 1/2 a banana for one coconut.

<div class="figure"><img src="/img/comparative-advantage/youre_happy.png" alt="bananas per coconut for you" width="65%"/></div>

Thus, you benefit from any trade where I give you more than 1/2 a banana for a coconut.

<div class="figure"><img src="/img/comparative-advantage/your_range.png" alt="your range" width="65%"/></div>

You’d like me to pay you as many bananas as possible. So you’d prefer a rate as far to the right as possible.

Now, the big question is: What rate do we agree on? Simple economics does not tell us the answer! In principle, our negotiations could arrive at an “exchange rate” of anywhere between .5 and 2 of your coconuts for 1 of my bananas.

This range of (.5 to 2) is the [Zone of Possible Agreement](https://en.wikipedia.org/wiki/Zone_of_possible_agreement) (ZOPA) in negotiation theory.

<div class="figure"><img src="/img/comparative-advantage/zopa4.png" alt="zone of potential agreement" width="65%"/></div>


# V Perverse Behavior

There's no simple simple math to decide what point in the ZOPA we settle on. This can lead to strange and perverse behaviors.

**Walking away.** Since we are nonviolent, the only “threat” is to refuse to trade.  If you know I am “rational” and won’t refuse a beneficial deal, you can be “irrational” and refuse to trade unless we do so at the end of the range that’s favorable to you. Thus, your “irrational” behavior gives you a better outcome than my “rational” behavior.

**Gaining information.** Before our first meeting, I build a telescope and spy on you. When we meet, I say “I noticed it takes you 2x as long to make a banana as a coconut. It takes me 1.95x as long. Bananas sure are hard, aren't they? Because I like you, I’m willing to trade at a rate of .512 bananas per coconut (.512=1/1.95). This does nothing for me, but you have a kind face, and I want to help you." If you believe me, I get a very favorable rate.

**Concealing information.** You are smart. After the bridge appears, you quality realize I might spy on you, and this would harm your negotiation position. Before doing any gathering, you construct a privacy wall around your island.

**Faking skills.** You’re a hard-ass. You will walk away unless I agree to an exchange on your end. I’ve tried walking away, but you don't care. I always blink before you, and we both know it. What can I do? For a weeks, I secretly gather coconuts in the night. The next time we meet, I bring a huge pile of coconuts. I say “I’ve been practicing, and now it only takes me 1.5x as long to make a coconut as a banana. I know you’re a hard-ass and you want the sweet end of the ZOPA. I admit I can’t beat you, but the ZOPA has shifted. You need to offer me a better deal.”

**Blowing up my island.** You’re a hard-ass. I only get .501 coconuts for 1 banana. I’ve tried walking away, but we both know you will out-wait me. I've tried fakings skills, but you won't bite. Because we are non-violent, I can’t coerce you. But there’s nothing wrong with hurting *myself*, is there? I build a machine that monitors inter-island commerce. If there is ever a trade that is not 1 coconut for 1 banana, the machine activates a bomb, my island sinks into the ocean forever, and I die. If I try to disable the machine, the bomb activates. When we next meet I say “OK. I can’t out bad-ass you. However, because of this machine, it will forever be against my interests to agree to a non-even trade. There’s no point in you waiting. Even if I *did* agree to an uneven trade, I'd sink into the ocean, and you'd have to gather your own coconuts!"

**Blowing up your island if I threaten to blow up my island.** You are smart. You are also a hard-ass.  As soon as the bridge appears, you know you can out-wait me to get a good rate. You immediately realize that my only option is to build the island destroying machine described above. Before we meet, you construct a machine that monitors my island for the presence of machines. Your machine is connected to a bomb on your island. If at any point, a bomb-activating machine is constructed on my island, your bomb activates, your island sinks into the ocean, and you die. When we meet, you explain that you’re a hard-ass, and that no island-destroying machines can help me. My best bet is to accept terms that barely improve my situation at all. You win.
