---
layout: post
title: "Simpson's paradox and the tyranny of strata"
image: /img/simpson/statue.jpg
tags: statistics math
permalink: /:year/:month/:day/:title/
---
It's hard to get into Oxford. Is it easier if your parents are rich?

| Population          | State Students Accepted | Independent Students Accepted |
| -------------------- | ------------------------- | ------------------------------- |
| Everyone  | 20%                       | 28%                             |
| Great grades | 46.1%                       | 50.5%  |

In 2013, [The Guardian](https://www.theguardian.com/education/2013/aug/14/oxford-university-private-a-level) showed that students from expensive independent schools were accepted more often than students from state schools. If you limit things to just students with strong grades (3 A* at A-level) the bias reduces, but doesn't disappear.

[The Conversation](https://theconversation.com/hard-evidence-is-oxford-biased-against-state-students-18979) later checked noticed something important: It's [much easier](https://www.ox.ac.uk/sites/files/oxford/Annual%20Admissions%20Statistical%20Report%202020.pdf) to get into Oxford if you apply to Classics (45% accepted) rather than Medicine (21%). If *each department* admits at equal rates, you'll still have the appearance of an *overall* bias, if state students are more likely to apply to Medicine.

---

Simpson's paradox is the name for situations like this, where the same data can seem to tell entirely different stories. Most people think of the paradox as an odd little curiosity, or perhaps just a cautionary tale about interpreting data correctly.

But you shouldn't see Simpson's paradox like that. Rather than a little quirk, it's actually a manifestation of a deeper and much stranger issue. It's less about the “right” way to analyze data and more about the limits to what questions data can answer.

How does Simpson's paradox work? What is this deeper issue? You don't need to be a data scientist to understand all this. In this post, I'll illustrate both Simpson's paradox and the issues beneath it using a little cartoon about lighting bolts and farm animals. This will use no statistics and (basically) no math.

# I Zeus

Imagine that you are a mortal shephard living near Olympus with a flock of sheep and [goats](https://dyno-might.github.io/2020/09/17/making-the-monty-hall-problem-weirder-but-obvious/).  Your neighbor, the thunder god Zeus, is a jerk. He has started zapping your animals with lightning bolts.

![zeus](/img/simpson/zeus.png)

He's not trying to kill them; He's just bored. (Transforming into animals to [seduce love interests](https://en.wikipedia.org/wiki/Zeus#Transformation_of_Zeus) gets old eventually.)

Anyway, you wonder: Does Zeus have a preference for shooting sheep or goats? You decide to keep records for a year. You have 25 sheep and 25 goats, so you use a 5x5 grid with one cell for each animal.

![sheep v goats 1](/img/simpson/sheep_v_goats1.png)

At first glance, it seems like Zeus dislikes goats more than He dislikes sheep. (If you're worried about the difference being due to random chance, feel free to multiply the number of animals by a million.)

# II Colors

Thinking about it, it occurs to you that some animals have darker fur than others. You go back to your records and mark each animal accordingly.

![sheep v goats 2](/img/simpson/sheep_v_goats2.png)

You re-do the analysis, splitting the animals into dark and light groups.

![sheep v goats 3](/img/simpson/sheep_v_goats3.png)

Overall, sheep are zapped less often than goats. But dark sheep are zapped *more* often than dark goats (7⁄11 > 10⁄16) *and* light sheep are zapped more often than light goats (5⁄14 > 3⁄9). This is the usual *paradox*: The conclusion changes when you switch from analyzing everyone to analyzing subgroups.

How does that reversal happen? It's simple: For both sheep and goats, dark animals get zapped more often, and there are more dark goats than dark sheep. Dark sheep are zapped slightly more than dark goats, and light sheep are capped more than light goats. But dumping all the animals together changes the conclusion because there are so many *more* dark goats. This is an example of Simpson's paradox. Group-level differences can be totally different than subgroup differences when the ratio of subgroups varies.

If you just want to understand Simpson's paradox you're done! This probably seems like a weird little edge case so far. But let's continue.

# III Stripes

Thinking even more, you notice that many of your (apparently mutant) animals have stripes. You prepare the data again, marking each animal according to stripes, rather than color.

![sheep v goats 4](/img/simpson/sheep_v_goats4.png)

You wonder, naturally, what happens if you analyze these groups.

![sheep v goats 5](/img/simpson/sheep_v_goats5.png)

The results are similar to those with color. Though sheep are zapped less often than goats overall (12⁄25 < 13⁄25), plain sheep are zapped more often than plain goats (5⁄14 > 3⁄9), and striped sheep are zapped more often than striped goats (7⁄11 > 10⁄16).

# IV Colors and stripes

Of course, instead of just considering either color or stripes, nothing stops you from considering both.

![sheep v goats 6](/img/simpson/sheep_v_goats6.png)

You decide to consider all four subgroups separately.

![sheep v goats 7](/img/simpson/sheep_v_goats7.png)

Now sheep are zapped *less* often in each subgroup. (1⁄4 < 2⁄7, 6⁄7 < 8⁄9, etc.)

When you compare everyone, there's a bias against goats. When you compare by color, there's a bias against sheep. When you compare by stripes, there's also a bias against sheep. Yet when you compare by both color *and* stripes, there's a bias against goats again.

Type of animals compared|Who gets zapped more often?
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

The same data gives lots of different results! How can this happen?

To answer that, it's important to realize that *anything can happen*. When you split data into subgroups, it's possible to find any biases. These could reverse (or not) when you split those subgroups again. In the table above, *any* sequence of goats / sheep is possible in the right-hand column.

But *how*, you ask? *How* can this happen? I think this is the wrong question. Instead we should ask if there is anything to *prevent* this from happening. There are a huge variety of possible datasets, with all sorts of different group averages. Unless there is some special structure forcing things to be "orderly", essentially arbitrary stuff can happen. There is no special force here.

# V Individuals

So far, this all seems like a lesson about finding the right way to analyze data. In some cases, that's probably true. Suppose read that Prestige Airways is more often delayed than GreatValue Skybus. Looking closer, you notice that Prestige flies mostly between snowy cities while Skybus mostly flies between warm dry cities. Prestige may have a better track record for *all* individual routes, but a worse track record overall, simply because they fly difficult routes more often. In this case, it's probably correct to say because Prestige is better for any flight you might take, Prestige is more reliable. 

But in other cases, the lesson should be just the opposite: There *is* no "right" way to analyze data. Often the real world looks like this:

![sheep v goats 8](/img/simpson/sheep_v_goats8.png)

There's no clear dividing line between "dark" and "light" animals. Stripes can be dense or sparse, thick or thin, light or dark. There can be many dark spots or few light spots. This list can go on forever. In the real world, individuals often vary in so many ways that there's no obvious definition of subgroups. In these cases, you can't beat the paradox. To get answers, you have to make arbitrary choices, even though the answers will depend on the choices you make.

Arguably this is a *philosophical* problem as much as a statistical one. We usually think about bias in terms of "groups". If prospects vary for two "otherwise identical" individuals in two groups, we say there is a bias. This made sense for the airlines above: If Prestige was more often on time than GreatValue for each route, it's fair to say Prestige is more reliable.

In a world of *individuals*, this definition of bias breaks down. Suppose Prestige mostly flies in the middle of the day on weekends in winter, while Skybus mostly flies at night during the week in summer. They vary from these patterns, but never enough that they are flying the same route on the same day at the same time at the same time of year. If you want to compare the two, you can group flights by cities or day or time or season, but not all of them. Different groupings (and sub-groupings) can give different result. There simply is no right answer.

This is the endpoint of Simpson's paradox: Group level differences often really *are* misleading. You can try to solve that by accounting for variability within groups, and there are lots of complex ways to try to do that I haven't talked about. However, none of them solve the fundamental problem that it's not clear what bias means when every individual is unique.

So by all means, beware of Simpson's paradox. Try splitting your data and see what happens. But keep in mind that you might be trying to estimate a quantity that's not defined. No data will solve that problem for you.
