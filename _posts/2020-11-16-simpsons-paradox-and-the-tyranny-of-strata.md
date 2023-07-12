---
layout: post
title: "Simpson's paradox all the way down"
image: /img/simpson/statue.jpg
description: Visualizes Simpson's paradox, and shows how it's a deeper problem than many people realize.
tags: statistics math
background_color: black
permalink: /simpsons-paradox/
category: "math"
seo:
  date_modified: 2022-12-11
last_modified_at: 2022-12-11
excerpt: "It's hard to get into Oxford. Is it easier if your parents are rich? In 2013, The Guardian showed noticed something disturbing: Students from (expensive) independent schools were accepted more often that students from state schools (28% vs 20%). Of course, a natural question to ask is, did students from independent schools have stronger applications? To check this, you can limit things to just students with strong grades (three A* grades at A-level). If you do that, the difference shrinks but doesn't disappear."
---
It's hard to get into Oxford. Is it easier if your parents are rich? In 2013, [The Guardian](https://www.theguardian.com/education/2013/aug/14/oxford-university-private-a-level) showed noticed something disturbing: Students from (expensive) independent schools were accepted more often that students from state schools.

| Population | Acceptance rate | 
| - | - |
| Independent | 28% |
| State | 20% |

Of course, a natural question to ask is, did students from independent schools have stronger applications? To check this, you can limit things to just students with strong grades (three A* grades at A-level). If you do that, the difference shrinks but doesn't disappear.

| Population | Acceptance rate | 
| - | - |
| Independent + great grades | 50.5% |
| State + great grades | 46.1% |

What's the deal? Do privileged kids get to go Brighton and *also* get lower admissions standards?

[The Conversation](https://theconversation.com/hard-evidence-is-oxford-biased-against-state-students-18979) later noticed two important facts: First, it's [much easier](https://www.ox.ac.uk/sites/files/oxford/Annual%20Admissions%20Statistical%20Report%202020.pdf) to get into Oxford if you apply to classics (45% accepted) rather than medicine (21%). Second, students from independent schools are much more likely to apply to classics. Even if all department admitted students at equal rates, you'd still get an appearance of *overall* bias if state students apply more often to more competitive majors like medicine.

---

This kind of situation—where the data seems to tell a different story depending on how it's analyzed—is typically known as "Simpson's paradox". Typically these situations are seen as odd little curiosities, or perhaps cautionary tales about the "correct" way to interpret data.

But I think this underrates Simpson's paradox. It's not a little quirk. Really, it's just the first layer of a deeper issue that may not *have* a solution. It's better to think of it as a limit on what questions data can answer. So here's a little parable about that.

{% comment %}
Of course, there's still lots to argue about the above situation. (Is it fair that Classics is easier to get into when when less privileged students will have more of a need to make money?) But forget all that.


It's less about the “right” way to analyze data and more about the limits to what questions data can answer.

How does Simpson's paradox work? What is this deeper issue? You don't need to be a data scientist to understand all this. In this post, I'll illustrate both Simpson's paradox and the issues beneath it using a little cartoon about lighting bolts and farm animals. This will use no statistics and (basically) no math.
{% endcomment %}

## Zeus

You're a mortal shepherd living near Olympus with a flock of sheep and goats. Your neighbor Zeus has grown weary of transforming into animals to [seduce love interests](https://en.wikipedia.org/wiki/Zeus#Transformation_of_Zeus) and, in his boredom, has taken to shooting lighting bolts at your flock.

![zeus](/img/simpson/goats9a.svg)

You wonder: Is He biased in terms of shooting goats or sheep more often? You keep records for a year.

![sheep v goats 1](/img/simpson/goats9b.svg)

At the end of the year, Zeus shot 12 of your 25 sheep and 13 of your 25 goats, suggesting a bias against goats. (If you're worried about having a small sample, multiply all the numbers by a million.)

## Colors

Except, maybe Zeus doesn't care about species, and he's biased in terms of the color of fur that the animals have. You go back and update your records to break things down that way.

![sheep v goats 2](/img/simpson/goats9c.svg)

You re-do the analysis, splitting the animals into dark and light groups.

![sheep v goats 3](/img/simpson/goats9d.svg)

Overall, sheep are zapped less often than goats (¹²⁄₂₅ < ¹³⁄₂₅). But dark sheep are zapped more often than dark goats (⁷⁄₁₁ > ¹⁰⁄₁₆) *and* light sheep are zapped more often than light goats (⁵⁄₁₄ > ³⁄₉).

Why do things reverse? Ultimately it's pretty simple: Dark animals get zapped more often, and there are more dark goats than dark sheep. So when you ignore color, that changes the conclusion.

This is the "normal" version of Simpson's paradox as it's usually presented. Group-level differences can be the opposite of subgroup differences when the ratio of subgroups varies.

Seems like a weird little edge case so far, right? Let's continue.

## Stripes

Thinking more, you notice that many of your animals have stripes. So you prepare the data again, marking them according to stripes rather than color.

![sheep v goats 4](/img/simpson/goats9e.svg)

You wonder, naturally, what happens if you analyze these groups.

![sheep v goats 5](/img/simpson/goats9f.svg)

The results are similar to those with color. Though sheep are zapped less often than goats overall (¹²⁄₂₅ < ¹³⁄₂₅), plain sheep are zapped more often than plain goats (⁵⁄₁₄ > ³⁄₉), and striped sheep are zapped more often than striped goats (⁷⁄₁₁ > ¹⁰⁄₁₆).

## Colors and stripes

But of course, you could also consider both color and stripes at the same time.

![sheep v goats 6](/img/simpson/goats9g.svg)

So you analyze all four subgroups separately

![sheep v goats 7](/img/simpson/goats9h.svg)

Now, sheep are zapped *less* often in each subgroup. Dark plain sheep are zapped less than dark plain goats (¼ < ²⁄₇), dark striped sheep are zapped less than dark striped goats (⁶⁄₇ < ⁸⁄₉), and so on.

So, to review:

Subgroups|Zapped more often
-|-
All| Goats
Light | Sheep
Dark | Sheep
Plain | Sheep
Striped | Sheep
Dark Plain | Goats
Dark Striped | Goats
Light Plain | Goats
Light Striped | Goats

Overall, there's a bias against goats. That reverses to a bias against sheep if you break things down by color, or if you break things down by stripes. Yet if you break things down by color *and* stripes, it reverses again.

How can this happen? That has two answers, though I warn you that you might not like them.

The first answer is that it happened in this particular case because I wrote a mixed-integer linear program (MILP) that encoded "conjure me a magical double-reversing dataset into math" and then called a [MILP solver](https://gekko.readthedocs.io/) that output the data above.

The second answer is that asking how this can happen is the wrong question. Instead, you should ask if there is anything to *stop* it from happening. The world is complex and full of wonders. There are a lot of datasets, and unless there is some special structure forcing things to be orderly, arbitrary stuff can happen. There is no special structure here. *Any* pattern of biases could happen for the 9 different subgroups in the above table.

## Individuals

In some cases, thinking about Simpson's paradox can help you find the right way to analyze things. Say that Prestige Airways has more delays than GreatValue Skybus, but Prestige flies mostly between snowy cities whereas Skybus mostly flies between warm dry cities. Prestige might have a better track record for all routes but a worse record overall, simply because they fly difficult routes more often. Then, maybe it's right to say that Prestige is more reliable.

But in other cases, the lesson should be just the opposite: There *is* no "right" way to analyze data. Often the real world looks like this:

![sheep v goats 8](/img/simpson/goats9i.svg)

There's no clear dividing line between "dark" and "light" animals. Stripes can be dense or sparse, thick or thin, light or dark. There can be many dark spots or few light spots. This list can go on forever so every case is unique.

In these cases, you don't beat the paradox. To get answers, you have to make arbitrary choices, even though the answers will depend on the choices you make.

Arguably this is a *philosophical* problem as much as a statistical one. We think about bias in terms of "groups". If prospects vary for two "otherwise identical" individuals in two groups, there is a bias. But in a world of *individuals*, this definition of bias breaks down.

Say Prestige mostly flies in the middle of the day on weekends in winter, while Skybus mostly flies at night during the week in summer. They vary from these patterns, but never enough that they are flying the same route on the same day at the same time in the same season. If you want to compare the two, you can group flights by cities, or day, or time, or season, but not all of them. Different groupings (and sub-groupings) can give different results. There simply is no right answer.

This is the endpoint of Simpson's paradox: Analyzing all the data together can be misleading, but often you can't create subgroups without making arbitrary choices, and those choices might change the result.

All this is similar to how correlation ≠ causation and how [controlling for variables](/control/) often fails to reveal causal effects. Except, with Simpson's paradox, we often don't have the alternative of running a randomized trial even in *principle*—there's no way to *assign* an animal to be a sheep or a goat. Fundamentally, it's not clear what bias *means* when every individual is unique.
