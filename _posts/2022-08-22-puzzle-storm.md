---
layout: post
title: "358 games of puzzle storm"
image: /img/puzzle-storm/storm2.jpg
tags: 
description: "Tracking my cognitive performance for a year"
permalink: /puzzle-storm/
background_color: rgb(189,196,220)
category: "self improvement"
head: "<style>
img{
    display:block;
    margin-left: auto;
    margin-right: auto;
    max-width:min(100%,450pt);
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
.highlighter-rouge{
  color:black;
}
table{
    font-family:Montserrat;
}
table tr{
    border-style: hidden;
    text-align:left;
}
@media (min-width:501px){
table{
  max-width:100;
  max-width:100%;
  font-size:90%;
}
}
@media (max-width:500px) and (min-width:301px) {
table{
  max-width:100;
  max-width:100%;
  font-size: 2.8vw;
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

A year ago, I started playing [puzzle storm](https://lichess.org/storm). This is a short game where you try to rapidly solve as many chess puzzles as you can in a few minutes.

![puzzle-storm-small](/img/puzzle-storm/puzzle-storm-small.png)

Now, I don't play---or even really like---real chess. It feels too much like mortal combat, and I get a similar feeling of reward by doing math and (hypothetically) contributing something to the universe.

But I found puzzle storm to be an ideal distraction when I need a break at work: It's fun, but it's also short and sort of frustrating, so I'm rarely tempted to play more than a few games.

I got very low scores when I started, but improved rapidly. After a couple of weeks---inspired by Scott Alexander's [experiment with WordTwist](https://astralcodexten.substack.com/p/eight-hundred-slightly-poisoned-word)---I thought there might be something to learn about skill acquisition or fluctuations in cognitive performance over time, so I started recording all the scores in a big file that looks like this:

```
oct 2
930 10
933 13
1521 13
1525 10
oct 5
1620 11
1624 8
1933 12
...
```

That was a year ago. Since then I've played 358 games, for a total time-wastage of around 18 hours. 

Just to get this out of the way: I'm not good at puzzle storm. Even after a year, my top score ever is a somewhat-embarrassing 19. Someone who is actually good looks like [this](https://www.youtube.com/watch?v=ZlZ3cIWNHj4&t=37s).

## Hypothesis #1: I got better over time

Here are my scores on all the games, with a small jitter added. To make the trend easier to see, I added a moving average of 15 games.

![scores-ordered](/img/puzzle-storm/scores-ordered.svg)

This hypothesis is not supported.

## Hypothesis #2: I got better when I played more often

My play was extremely irregular. What if we use the date and time for each game? Because moving averages are weird when you have irregular sampling, here I used a smoothed ([loess](https://en.wikipedia.org/wiki/Local_regression)) curve.

![scores-days](/img/puzzle-storm/scores-loess.svg)

It looks like I did improve at first, but I regressed horribly when I stopped playing for 5 months and regressed a bit when I stopped for one month later on. So I think this hypothesis is true.

## Hypothesis #3: My brain is OK

There's something else I should maybe mention about the above chart:

![scores-days](/img/puzzle-storm/scores-covid.svg)

Physically, Covid wasn't too bad for me, but I just *couldn't think*---I'd have conversations and be astonished by the gibberish coming out of my mouth. (Looking back, this is when I decided that the world urgently needed to know everything about [ethylene](/ethylene/).)

So that was a lesson on the fragility of the human condition. After I recovered, I seemed to slowly regain my ability to think. But I was a little neurotic: If I *wasn't* back to full capacity, would I notice? My desire to measure this is what led me to start playing puzzle storm again.

I'm pretty sure I'm fine, but this data isn't very conclusive either way. Did I get worse during the gap because of Covid, or just because my skill atrophied? Did I plateau later on because of a skill ceiling, because I played less often, or because Covid cooked my brain? It's hard to be sure. I really wish I had continued playing at a steady pace the whole time.

## Hypothesis #4: I'm smarter in the morning.

We can also look at averages at different times of day. Here's how many games I played for each one hour period during the day: (The 8am bin shows the number of games between 8am and 9am.)

![num-played-by-hour](/img/puzzle-storm/num-played-by-hour.svg)

And here's my average performance for each time.

![by-hour](/img/puzzle-storm/by-hour.svg)

The orange lines show 90% confidence intervals, just to stick it to the 95% interval mafia.

So: Zero evidence that I'm any smarter or dumber at any different time of day.

There are, however, two major caveats:

1. I played puzzle storm whenever I felt like it and had time. This is not random. Subjectively, I don't like to play when I'm tired, and when I'm at my best, I don't get distracted as much. It's possible I am smarter/dumber at different times of day, but this selection effect killed off the signal.
2. I'm not sure how much this game measures intelligence. This is probably obvious to people who play chess, but I was surprised that almost all my improvement seemed to come from unconscious pattern recognition, not "thinking". After playing a while, you mostly start to "feel" the promising moves. Still, there's some conscious processing to filter the moves the unconscious mind suggests.

## Hypothesis #5: I'm smarter on certain days of the week.

Here's the total number of games I played on each day:

![num-played-by-day](/img/puzzle-storm/num-played-by-day.svg)

And here's my average performance on each:

![by-day](/img/puzzle-storm/by-day.svg)

I *miiigghhtt* be slightly better during the middle of the week. But there's no conclusive evidence.

Even if this were true, it could be a "recent practice effect": Since I played more during the middle of the week, on those days I had more recent practice.

## Discussion

To summarize:

* I'm not good at puzzle storm.
* I improved a lot in the first couple of weeks before I started tracking, but not much in the following year.
* Practice seems to help, but skill decays quickly with time off.
* There's no evidence I'm smarter at any time or on any day of the week, though it's hard to be sure with this kind of data.

In retrospect, I'm not sure puzzle storm is ideal for this purpose. There's a ton of luck: Some puzzles are easier than others, and this effect is compounded by the way the game gives you extra time for streaks of correct answers. I also had a lot of trouble with misclicks. All this variance makes it hard to detect the true signal.

If I were to do this again, I'd choose a less random game. There are lots of cognitive tests out there, but they *aren't fun*, which is a non-starter for me. 

What's really needed is to play a game on a regular schedule. The ideal would be a game that is:

* Short
* Fun (this disqualifies WordTwist)
* But not *too* fun (not addictive)
* Gives a high-resolution output (not just won/lost)
* Has a skill component
* Has a general cognitive performance component
* Is low variance

Does such a game exist?

{% comment %}
<div style="font-size:70%; text-align:right;" markdown="1">
(Comment on [reddit](https://old.reddit.com/r/dynomight/comments/wp3vw1/rules_for_weird_ideas/) or [substack](https://dynomight.substack.com/p/weird-ideas).)
</div>
{% endcomment %}
