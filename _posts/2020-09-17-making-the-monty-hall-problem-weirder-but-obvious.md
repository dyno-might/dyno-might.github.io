---
layout: post
title: "Making the Monty Hall problem weirder but obvious"
image: /img/monty-hall/monty.jpg
description: Would you like what's behind one door or what's behind the other nine?
tags: explainer statistics math
last_updated: 2021-12-11
permalink: /:year/:month/:day/:title/
---

<head>
<style>
.myfigure {
/*border: dashed blue 1px; */
}
.myfigure img {
max-width: 385px;
width: 90%;
height: auto;
display: block;
margin-left: auto;
margin-right: auto;
}
</style>
</head>

Here's an **Obvious problem**:

1. There are 10 doors. A car is behind a random door, goats behind the others.
2. Do you want what's behind door 1, or what's behind all the other doors?

That's obvious, right? Well, how about the **Monty Hall problem**?

1. There are three doors. A car is behind one random door, goats behind the others.
2. You pick one door.
3. The host picks another door that contains a goat, and opens it.
4. Should you keep your original door, or switch to the other closed door?

Many people guess it doesn't matter if you switch. But in reality, switching gets you the car 2/3 of the time.

This post claims that these problems are really just disguised versions of each other. We'll start with the Obvious problem, apply a series of small changes that clearly don't change the solution, and end up at the Monty Hall problem.

{% comment %}
<div align="right" style="font-size:70%">(Also available in <a href="https://www.youtube.com/watch?v=LCBTUtApvU8">video form</a>.)</div>

The [Monty Hall problem](https://en.wikipedia.org/wiki/Monty_Hall_problem) is famously unintuitive. This post starts with an extreme version where the solution is blindingly obvious. We then go through a series of small changes. It will be clear that these don't affect the solution. At the end, we arrive at the classic Monty Hall problem.

For reference, the [classic formulation](https://en.wikipedia.org/wiki/Monty_Hall_problem) goes:

> Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?

Intuitively, many people guess it doesn't matter if you switch. But it does. You get the car 2/3 of the time if you switch, and 1/3 of the time if you don't. Why?
{% endcomment %}

## Game 1 {% comment %}(Dynomight™ Monty Hall){% endcomment %}

Here's our first game.

1. There are 10 doors. A car is randomly placed behind one, and goats behind the other 9.
2. You pick one door.
3. You get two options:
  * Option A: You get whatever is behind the door you picked.
  * Option B: You get whatever is behind all of the other 9 doors.

<div class="myfigure">
 <img src="/img/monty-hall/game1.png">
</div>

There's nothing mysterious here. You should choose option B. There’s only a 10% chance you picked the right door, so there’s a 90% chance the car is behind one of the others.

## Game 2

Now, we slightly update the game (new part in bold).

1. There are 10 doors. A car is randomly placed behind one, and goats behind the other 9.
2. You pick one door.
3. **Monty says “Hey! I promise you that there is a goat behind at least 8 of the other 9 doors!”**
4. You get two options:
  * Option A: You get whatever is behind the door you picked.
  * Option B: You get whatever is behind all of the other 9 doors.

<div class="myfigure">
 <img src="/img/monty-hall/game2.png">
</div>

Monty’s statement changes nothing. You don’t need to rely on his [trustworthy looks](https://en.wikipedia.org/wiki/Monty_Hall#/media/File:Monty_hall_abc_tv.JPG). You already *knew* there were at least 8 goats! Option B still gets you the car 90% of the time.

# Game 3

Let's update the game again (new part in bold).

1. There are 10 doors. A car is randomly placed behind one, and goats behind the other 9.
2. You pick one door.
3. **Monty looks behind the other 9 doors. He chooses 8 with goats behind them, and opens them.**
4. You get two options:
  * Option A: You get whatever is behind the door you picked.
  * Option B: You get whatever is behind all of the other 9 doors.

<div class="myfigure">
 <img src="/img/monty-hall/game3.png">
</div>

The key insight is this: When Monty shows you that 8 of the 9 other doors contain goats, you haven't learned anything relevant to your decision. You *already knew there were at least 8 goats behind the other doors*! So this is just like game 2. Option B still gets you the car 90% of the time.

Want more intuition? Suppose you picked door 3. Imagne Monty walking past the doors, opening doors 1, 2, 4, 5, 6, **skipping 7**, then opening 8, 9, and 10. Doesn't door 7 seem special?

## Game 4

Let's make another change. Finally, we arrive at a game very similar to Monty Hall.

1. There are 10 doors. A car is randomly placed behind one, and goats behind the other 9.
2. You pick one door.
3. Monty looks behind the other 9 doors. He chooses 8 of them with goats behind them, and opens them.
4. You get two options:
  * Option A: You get whatever is behind the door you picked.
  * Option B: You get whatever is behind **the other closed door**.

<div class="myfigure">
 <img src="/img/monty-hall/game4.png">
</div>

The only difference with Game 3 is that option B doesn’t get you the 8 visible goats. Since you don’t care about goats, this makes no difference. This is still just like the game 3. You get the car 90% of the time by switching.

## Game 5 (Classic Monty Hall)

Here is the last game. We just change the number of doors from 10 to 3.

1. There are **3** doors. A car is randomly placed behind one, and goats behind the other **2**.
2. You pick one door.
3. Monty looks behind the other **2** doors. He chooses one **1** of them with a goat behind it, and opens it.
4. You get two options:
  * Option A: You get whatever is behind the door you picked.
  * Option B: You get whatever is behind the other closed door.
  
<div class="myfigure">
 <img src="/img/monty-hall/game5.png">
</div>
  
Of course, you still want to choose option B. The chance of success is now 2/3 instead of 9/10. This game is exactly Monty Hall, so we're done.

## Side Notes

  * It’s important that Monty looked behind the doors before choosing which to open. This is where people’s intuition usually fails. If he had chosen a door at random — *in a way that he risked possibly exposing a car*, then the situation would be different. (In that case, there's no advantage or harm in switching.) But he doesn’t choose the door at random. He deliberately chooses to show you goats. Since this is always possible, it tells you nothing. I think this is the crux of what makes this problem unintuitive: If the host had picked a random door, the intuition that it doesn't matter if you switch would be correct!

  * It might be helpful to draw a diagram of the relationship of the different games, starting with classic Monty Hall and ending with the Obvious version.

<div style="text-align:center; text-size:70%; margin-left:15%; margin-right:15%;" markdown="1">

**Game 5 (Classic Monty Hall)**<br>
 ↓  
 Use 10 doors instead of 3.<br>
 ↓   
**Game 4**<br>
 ↓  
If you switch, you get the contents of *all* other doors, not just the other closed door.<br>
 ↓  
**Game 3**<br>
 ↓  
Monty promises 8 goats behind the other doors instead of showing you.<br>
 ↓  
**Game 2**<br>
 ↓  
 Monty doesn't bother promising.<br>
 ↓  
**Game 1 (Obvious Monty Hall)** {% comment %}(Dynomight™ Monty Hall) {% endcomment %}

</div>

  * There are [some](https://marginalrevolution.com/marginalrevolution/2019/09/the-intuitive-monty-hall-problem.html) [other](https://twitter.com/jben0/status/1174180200072011776) [attempts](https://statmodeling.stat.columbia.edu/2019/09/19/alternative-more-intuitive-formulation-of-monte-hall-problem/) at [variants](https://math.stackexchange.com/questions/96826/the-monty-hall-problem/3360686#3360686) of the Monty Hall problem, also intended to be more intuitive. These involve switching the doors for "boxers".

  * Monty Hall was actually named “Monte” at birth! Given that [Monte Carlo simulations](https://en.wikipedia.org/wiki/Monte_Carlo_method) are often used for exploring the Monty Hall problem, that's either a miracle for confused students or a tragedy for puns.
