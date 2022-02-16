---
layout: post
title: "The conspiratorial Monty Hall problem"
image: /img/monty-hall/monty.jpg
tags: explainer statistics math
description: "Meanwhile, in the multiverse..."
permalink: /conspiratorial-monty-hall/
background_color: rgb(97,97,97)
head: "<style>
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
img{
    display:block;
    margin-left: auto;
    margin-right: auto;
    max-width:min(100%,500pt);
}
details{
    margin-bottom: 10pt;
    background: #eeeeee;
    }
details > summary{
  padding-bottom: 0pt;
  cursor: pointer;
  background: #ffffff;
  padding-bottom: 5pt;
}
details > *:not(summary){
  margin-top: 0pt;
  margin-left: 5pt;
}
table tr{
    border-style: hidden;
    text-align:left;
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
  font-size: 2.4vw;
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
</style>
"
---

The Monty Hall problem has now been a pox on humanity for two generations, diverting perfectly good brains away from productive uses.

So it is with great trepidation that I'd like to announce a new and more pernicious variant.

## Reminder

As a reminder, here's the standard problem:

1. There are 3 doors. A car is randomly placed behind one, and goats behind the other 2.
2. You pick one door.
3. Monty looks behind the other 2 doors. He chooses one of them with a goat behind it, and opens it.
4. You get two options:
  * Option A: You get whatever is behind the door you picked.
  * Option B: You get whatever is behind the other closed door.

<div class="myfigure">
 <img src="/img/monty-hall/game5.png">
</div>

The [well-known solution](2020/09/17/making-the-monty-hall-problem-weirder-but-obvious/) is that you should always switch, which gets you the car 2/3 of the time.

## Variant

In our variant, Monty is corrupt. The night before the game, you show up at his house with a suitcase of cash. He agrees that he will follow whatever algorithm you want when choosing the door to open. 

What makes this challenging is:

1. Monty doesn't know where the car will be before the show starts.
2. After the show starts, Monty can't communicate with you other than by choosing what door to open.

The problem is: What is the best strategy for you and Monty to use? And if you use that strategy, how likely are you to get the car?

## Thoughts

The naive solution would be to play as if there was no conspiracy: If Monty picks a random door to open and you always switch, then you get the car 2/3 of the time. The question is: Can you do better?

I'm pretty sure I have the answer, but <strike>people always yell at me when I talk about this stuff</strike> I don't yet have an elegant proof.

Do you have one? If so, please [send it to me](/about). When/if I get some nice solutions, I'll post an update.
