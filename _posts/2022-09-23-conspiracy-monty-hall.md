---
layout: post
title: "The conspiratorial Monty Hall problem"
image: /img/monty-hall/goat2.jpg
tags: explainer statistics math
description: "What if you and Monty decide to cheat?"
permalink: /conspiratorial-monty-hall/
background_color: rgb(97,97,97)
category: "math"
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
.eq {
  display:flex;
  justify-content: center;
  margin-bottom: 10px;
  font-family: Montserrat, sans-serif;
}
.eeq {
  font-family: Montserrat, sans-serif;
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

The Monty Hall problem has now been a pox on humanity for two generations, diverting perfectly good brains away from productive uses. Hoping to exacerbate this problem, some time ago I announced a new and more pernicious variant: What if you and Monty try to *cheat*?

Since then, many people have sent arguments. (Thank you!) Here, I'll review the problem and then go over all the arguments people sent in.

{:.no_toc}

<div style="font-size:90%; line-height:110%;" markdown="1">

* auto-gen TOC:
{:toc}

</div>

## Reminder

As a reminder, here's the standard Monty Hall problem:

1. There are 3 doors. A car is randomly placed behind one, and goats behind the other 2.
2. You pick one door.
3. Monty looks behind the other 2 doors. He chooses one of them with a goat behind it, and opens it.
4. You get two options:
  * Option A: You get whatever is behind the door you picked.
  * Option B: You get whatever is behind the other closed door.

<div class="myfigure">
 <img src="/img/monty-hall/game5.png">
</div>

The [well-known solution](/2020/09/17/making-the-monty-hall-problem-weirder-but-obvious/) is that you should always switch, which gets you the car ⅔ of the time.

## Variant

In our variant, Monty is corrupt. The night before the game, you show up at his house with a suitcase of cash. He agrees that he will follow whatever algorithm you want when choosing the door to open. (Of course, he still can't open a door with a car.)

What makes this challenging is:

1. Monty doesn't know where the car will be before the show starts.
2. After the show starts, Monty can't communicate with you other than by choosing what door to open.

The problem is: What is the best strategy for you and Monty to use?

The naive solution would be to play as if there was no conspiracy: Monty would just pick a random door, and you would always switch. This would get you the car ⅔ of the time. The question is: Can you do better?

## The answer

No.

Thanks to the dozens of people who sent in different arguments. (And my apologies for being so criminally slow in responding.) I read all of them in detail, tried to "cluster" similar proofs together, and then gave everything a consistent notation. (Because of this, many proofs are changed a fair bit from what folks originally sent in.)

---

## The "without loss of generality" argument

The position of the car is randomized, so it doesn't matter (on average) which door you choose at the start. To keep things simple, say you always choose door #1. Now, there are three cases:

1. If the car is behind door #1, then Monty can open either door #2 or door #3.
2. If the car is behind door #2, Monty must open door #3.
3. If the car is behind door #3, Monty must open door #2.

Monty only has freedom when the car is behind door #1. Suppose without loss of generality that he always chooses to open door #2 in this case. Now, what happens?

* In <span class="eeq">⅔</span> of cases, Monty will end up opening door #2, and in <span class="eeq">⅓</span> of cases, he will open door #3.
* If Monty opens door #2, there's a 50/50 chance the car is behind door #1 or door #3. It doesn't matter if you switch or stay. Either way, you have a ½ chance of winning.
* If Monty opens door #3, there is a 100% chance the car is behind door #3, so you should always switch.


If you always switch when Monty opens door #3, then your overall chances of winning are

<div class="eq" markdown="1">
&nbsp;&nbsp;&nbsp;&nbsp;ℙ[Win]  
&nbsp;&nbsp;&nbsp;&nbsp;= ℙ[Monty=2] ℙ[Win | Monty=2]  
&nbsp;&nbsp;&nbsp;&nbsp; + ℙ[Monty=3] ℙ[Win | Monty=3]  
&nbsp;&nbsp;&nbsp;&nbsp;= ⅔ × ½ + ⅓ × 1  
&nbsp;&nbsp;&nbsp;&nbsp;= ⅔.
</div>

Since this is the optimal strategy, <span class="eeq">⅔</span> is as good as you can do.

**Why you might not like this argument:** It assumes that Monty always does the same thing in the same situation. Maybe you could do better if he used a randomized strategy?

**Credit**: Unheamy, Alan, Matt, Dan Sisan, Steven, [ExistentAndUnique](https://old.reddit.com/r/math/comments/suqlz6/the_conspiratorial_monty_hall_problem/hxcj6ra/), [heelspider](https://old.reddit.com/r/math/comments/suqlz6/the_conspiratorial_monty_hall_problem/hxbha3s/).

---

## The information argument

If you had no information at all, your odds would be <span class="eeq">⅓</span>. But when Monty opens a door, he has only two options, so can convey at most one bit of information. But one bit of information can at most double your odds. So you can't do better than <span class="eeq">⅔</span>.

**Why you might not like this argument:** Why can one bit of information at most double your odds? And anyway, does Monty really convey a full bit of information, given that in <span class="eeq">⅔</span> of cases, he has no choice about which door he opens?

**Credit:** [KingLewi](https://old.reddit.com/r/math/comments/suqlz6/the_conspiratorial_monty_hall_problem/hxcjkea/)

---

## The decision points argument

Assume without loss of generality that the player picks door 1. Now, if the player picked the wrong door, Monty has no choice, there is only one other door with a goat, which he must open. So the only decision points are:

* If the car is behind door #1, should Monty open door #2 or door #3?
* If Monty opens door #2, should the player switch?
* If Monty opens door #3, should the player switch?

Suppose that when Monty has a choice, he opens door 2 with probability <span class="eeq">*p*</span> and door 3 with probability <span class="eeq">1-*p*</span>.

Note for reference that

<div class="eq" markdown="1">
&nbsp;&nbsp;&nbsp;&nbsp;ℙ[Monty=2]  
&nbsp;&nbsp;&nbsp;&nbsp;= ℙ[Car=1] × *p* + ℙ[Car=3]  
&nbsp;&nbsp;&nbsp;&nbsp;= ⅓ × *p* + ⅓  
&nbsp;&nbsp;&nbsp;&nbsp;= ⅓ × (*p*+1).
</div>

And similarly,

<div class="eq" markdown="1">
&nbsp;&nbsp;&nbsp;&nbsp;ℙ[Monty=3]  
&nbsp;&nbsp;&nbsp;&nbsp;= ℙ[Car=1] × (1-*p*) + ℙ[Car=2]  
&nbsp;&nbsp;&nbsp;&nbsp;= ⅓ × (1-*p*) + ⅓
&nbsp;&nbsp;&nbsp;&nbsp;= ⅓ × (2-*p*)
</div>

Now, suppose the player sees that door #2 is open. Then, the player knows that

<div class="eq" markdown="1">
&nbsp;&nbsp;&nbsp;&nbsp;ℙ[Car=3 | Monty=2]  
&nbsp;&nbsp;&nbsp;&nbsp;= ℙ[Car=3, Monty=2] / ℙ[Monty=2]  
&nbsp;&nbsp;&nbsp;&nbsp;= (⅓) / (⅓ × (1+*p*))  
&nbsp;&nbsp;&nbsp;&nbsp;= 1/(1+*p*)  
&nbsp;&nbsp;&nbsp;&nbsp;≥ ½
</div>

Similarly,

<div class="eq" markdown="1">
&nbsp;&nbsp;&nbsp;&nbsp;ℙ[Car=2 | Monty=3]  
&nbsp;&nbsp;&nbsp;&nbsp;= ℙ[Car=2, Monty=3] / ℙ[Monty=3]  
&nbsp;&nbsp;&nbsp;&nbsp;= (⅓) / (⅓ × (2-p))  
&nbsp;&nbsp;&nbsp;&nbsp;= 1/(2-p)  
&nbsp;&nbsp;&nbsp;&nbsp;≥ ½.
</div>

Thus it is optimal for the player to always switch. But if you always switch, then it's you get the car <span class="eeq">⅔</span> of the time regardless of what Monty does. So you can't do better than <span class="eeq">⅔</span>.

**Why you might not like this argument:** Maybe this feels too "Bayesian" for you? (Personally, I like this argument a lot.)

**Credit**: Joao, Beckett, Elvis Sikora, [Isaac Grosof](https://isaacg1.github.io/), Drake

---

## The analogy argument

Consider a game, which I'll call **GAME 1**:

1. There are 3 doors. A car is randomly placed behind one, and goats behind the other 2.
2. Monty looks behind all three doors. Then he can show you either a RED flag or a BLUE flag.
3. You pick one door.

It's "obvious" that you can win this game <span class="eeq">⅔</span> of the time and no more.

Now consider **GAME 2** (where I've highlighted the changes in bold).

1. There are 3 doors. A car is randomly placed behind one, and goats behind the other 2.
2. Monty looks behind all three doors. Then he can show you either a RED flag or a BLUE flag. **However,  if the car is behind door #2, he is not allowed to reveal the RED flag, and if the car is behind door #3, he is not allowed to reveal the BLUE flag**.
3. You pick one door.

Clearly, this is not *easier* than game 1, since the only difference is that Monty has less flexibility in choosing the flags. So you can win at most ⅔ of the time.

Now consider **GAME 3**:

1. There are 3 doors. A car is randomly placed behind one, and goats behind the other 2.
2. Monty looks behind all three doors. Then he can **open either door #2 or door #3. However, he cannot open a door that has a car behind it**.
3. You pick one door.

This is equivalent to game 2. Opening door #2 is equivalent to showing a RED flag, while the opening door #3 is equivalent to showing a BLUE flag.

Finally, consider **GAME 4**:

1. There are 3 doors. A car is randomly placed behind one, and goats behind the other 2.
2. **You pick one door.**
3. Monty looks behind all three doors. He then opens **some door you did not pick**. However, he cannot open a door that has a car behind it.
4. You pick one door.

This is equivalent to game 3. If you pick door #1 in the second step, they are the same. But since the car is placed randomly, you might as well pick door #1 --- choosing another door will not improve your odds.

Putting all of our logic above together, we get that

<div class="eq" markdown="1">
&nbsp;&nbsp;&nbsp;&nbsp;⅔  
&nbsp;&nbsp;&nbsp;&nbsp;= (Optimal play in game 1)  
&nbsp;&nbsp;&nbsp;&nbsp;≥ (Optimal play in game 2)  
&nbsp;&nbsp;&nbsp;&nbsp;= (Optimal play in game 3)  
&nbsp;&nbsp;&nbsp;&nbsp;= (Optimal play in game 4)  
&nbsp;&nbsp;&nbsp;&nbsp;≥ ⅔,
</div>

and thus

<div class="eq" markdown="1">
&nbsp;&nbsp;&nbsp;&nbsp;(Optimal play in game 4) = ⅔.
</div>

But of course, game 4 is exactly the conspiratorial Monty Hall problem.

**Why you might not like this argument:** Is it really "obvious" that it's not possible to win game 1 more often than <span class="eeq">⅔</span> of the time?

**Credit:** I did it. I did it all, [by myself](https://scsh.net/docu/html/man.html).

---

## The "more doors" argument

Suppose we had 100 doors rather than 3. Assume that Monty still opens a single door, and then are allowed to choose any door other than the one Monty opened (including your original door). What then?

An obvious strategy would be for Monty to open the door to the right of the true one whenever possible. For example, suppose there were ten doors (and you start by guessing door 1). Monty might use this table:

<div class="eq" markdown="1">

| Location of car | Monty opens |
| --------------- | ----------- |
| 1               | 2           |
| 2               | 3           |
| 3               | 4           |
| 4               | 5           |
| 5               | 6           |
| 6               | 7           |
| 7               | 8           |
| 8               | 9           |
| 9               | 10          |
| 10              | ???         |

</div>

Once Monty opens the door, you know where the car is---unless the car happens to be behind door #10. 

See the problem? There are 10 possible locations for the car, but in any given situation, Monty only has (at most) 9 signals he can send you. No matter what number you and Monty decide to put in the "???" square above, there are going to be two locations on the left that get mapped to the same location on the right. That means, there's always going to be one "unlucky" location, meaning your overall chances of getting the car are <span class="eeq">(*N*-1)/*N*</span>.

(Of course, there are many other equivalent strategies --- you can put any 9 of the numbers in {1, 2, ..., 10} anywhere in the right column so long as the two numbers in the same row are different.)

**Why you might like this argument:** It's very intuitive. And it shows an interesting difference: In the regular Monty Hall problem, your chances deteriorate when there are more doors, assuming Monty only opens one.  But in this version, they get better. So it's arguably a kind of coincidence that they coincide for <span class="eeq">*N*=3</span>.

**Why you might not like this argument**: It's not very formal. And what if Monty used some kind of randomized strategy?

**Credit:** [Dan](http://danomagnum.com/)

---

## The parameterization argument

Assume without loss of generality that you always start by picking door #1. Now, the only freedom Monty has is to choose which door to open. He can only exercise this freedom when you have in fact chosen the car. In this case, let <span class="eeq">*p*</span> be the probability that Monty chooses to open door #2, and let <span class="eeq">*(1-p)*</span> be the probability that Monty chooses to open door #3. This parameter completely encodes Monty's part of the strategy.

Now, what about your part of the strategy? Well, all that you can choose is:

1. Your probability of switching if Monty opens door #2. (Call this <span class="eeq">*x*</span>)
2. Your probability of switching if Monty opens door #3. (Call this <span class="eeq">*y*</span>)

If you work out the probabilities, it turns out that your final win probability with this setup is

<div class="eq" markdown="1">
&nbsp;&nbsp;&nbsp;&nbsp;ℙ[win] = ⅓ (1 + (1 - *p*)*x* + *py*).
</div>

But note here: <span class="eeq">(1-*p*)</span> is a positive number, and *p* is a positive number. (Technically these are "non-negative" since they could be zero.) Thus, your odds of winning are maximized by setting <span class="eeq">*x*=*y*=1</span>. Then, you get that

<div class="eq" markdown="1">
&nbsp;&nbsp;&nbsp;&nbsp;ℙ[win] = ⅓ (1 + (1 - *p*) + *p*) = ⅔.
</div>

So, regardless of what Monty does, you should always switch, and then you'll win <span class="eeq">⅔</span> of the time.

**Comment:** Say that <span class="eeq">*p*=0</span>, i.e. Monty always chooses door #2 when he has a choice. Then the probability of winning is <span class="eeq">ℙ[win] = ⅓ (1 + *x*)</span>. You can maximize this by choosing <span class="eeq">*x*=1</span>, and *any* value for <span class="eeq">*y*</span>. This means that if Monty always chooses door #2 when he can, it doesn't matter what you do when Monty opens door #3.

**Why you might not like this argument:** "It turns out"

**Credit:** amjr, Jae, Michael Lucy

---

## The parameterization argument, but actually doing the math

In general, your chances are

<div class="eq" markdown="1">
&nbsp;&nbsp;&nbsp;&nbsp;ℙ[Win]  
&nbsp;&nbsp;&nbsp;&nbsp;= ℙ[Car=1] ℙ[Stay | Car=1]  
&nbsp;&nbsp;&nbsp;&nbsp;+ ℙ[Car=2] ℙ[Switch | Car=2]  
&nbsp;&nbsp;&nbsp;&nbsp;+ ℙ[Car=3] ℙ[Switch | Car=3]  
&nbsp;&nbsp;&nbsp;&nbsp;= ⅓ ( ℙ[Stay | Car=1] + ℙ[Switch | Car=2] + ℙ[Switch | Car=3]),
</div>

where in the second line I use that the position of the car is randomized, so <span class="eeq">ℙ[Car=1] = ℙ[Car=2] = ℙ[Car=3] = ⅓</span>.

Now, when you and Monty devise your strategy, what options do you have? First, let's think about Monty's strategy. He only has a choice to make when the goat is behind door 1. (If it is behind door 2, he must always open door 3. If it is behind door 3, he must always open door 2.) Let <span class="eeq">*p*</span> be the probability that he opens door 2 in this case, and <span class="eeq">(1-*p*)</span> the probability that he opens door 3.

Thus, here is the table of <span class="eeq">ℙ[monty \| car]</span> for each possible value of monty and car:

<div class="eq" markdown="1">

|         | **Car=1** | **Car=2** | **Car=3** |
| **Monty=1** | 0     | 0     | 0     |
| **Monty=2** | *p*   | 0     | 1     |
| **Monty=3** | 1-*p* | 1     | 0     |

</div>

Now, let's think about your part of the strategy. All that you will observe is Monty opening door 2 or door 3, and you can either choose to switch or to stay. Let <span class="eeq">*x*</span> be the probability you switch if Monty opens door 2 and let <span class="eeq">*y*</span> be the probability you switch if Monty opens door 3. Then here is a table of <span class="eeq">ℙ[Stay \| monty]</span> and <span class="eeq">ℙ[Switch \| monty]</span>:

<div class="eq" markdown="1">

|        | **Monty=2** | **Monty=3** |
| **Stay**   | 1-*x*   | 1-*y*   |
| **Switch** | *x*     | *y*     |

</div>

Now we can calculate the three probabilities we need in our above formula for <span class="eeq">ℙ[Win]</span>:

<div class="eq" markdown="1">
&nbsp;&nbsp;&nbsp;&nbsp;ℙ[Stay | Car=1]  
&nbsp;&nbsp;&nbsp;&nbsp;= ℙ[Monty=2 | Car=1] ℙ[Stay | Monty=2]  
&nbsp;&nbsp;&nbsp;&nbsp;+ ℙ[Monty=3 | Car=1] ℙ[Stay | Monty=3]  
&nbsp;&nbsp;&nbsp;&nbsp;= *p* (1-*x*) + (1-*p*) (1-*y*)
</div>

<div class="eq" markdown="1">
&nbsp;&nbsp;&nbsp;&nbsp;ℙ[Switch | Car=2]  
&nbsp;&nbsp;&nbsp;&nbsp;= ℙ[Monty=2 | Car=2] ℙ[Switch | Monty=2]  
&nbsp;&nbsp;&nbsp;&nbsp;+ ℙ[Monty=3 | Car=2] ℙ[Switch | Monty=3]  
&nbsp;&nbsp;&nbsp;&nbsp;= 0 × *x* + 1 × *y*  
&nbsp;&nbsp;&nbsp;&nbsp;= *y*
</div>

<div class="eq" markdown="1">
&nbsp;&nbsp;&nbsp;&nbsp;ℙ[Switch | Car=3]  
&nbsp;&nbsp;&nbsp;&nbsp;= ℙ[Monty=2 | Car=3] ℙ[Switch | Monty=2]  
&nbsp;&nbsp;&nbsp;&nbsp;+ ℙ[Monty=3 | Car=3] ℙ[Switch | Monty=3]  
&nbsp;&nbsp;&nbsp;&nbsp;= 1 × *x* + 0 × *y*  
&nbsp;&nbsp;&nbsp;&nbsp;= *x*
</div>

If we put these numbers into our win probability formula, we get

<div class="eq" markdown="1">
&nbsp;&nbsp;&nbsp;&nbsp;ℙ[Win]  
&nbsp;&nbsp;&nbsp;&nbsp;= ⅓ ( ℙ[Stay | Car=1] + ℙ[Switch | Car=2] + ℙ[Switch | Car=3])  
&nbsp;&nbsp;&nbsp;&nbsp;= ⅓ ( *p* (1-*x*) + (1-*p*) (1-*y*) + *y* + *x*)  
&nbsp;&nbsp;&nbsp;&nbsp;= ⅓ (1 + (1 - *p*) *x* + *p* *y*)
</div>

Now, <span class="eeq">*p*</span> and <span class="eeq">(1-*p*)</span> are both positive (non-negative) numbers, meaning the best choice is <span class="eeq">*x*=*y*=1</span>, for which <span class="eeq">ℙ[win]=⅔</span>, regardless of the choice of <span class="eeq">*p*</span>. Thus, it doesn't matter what Monty does, you should always switch.

**Why you might not like this argument:** Lots of calculation.

**Credit:** Peter

---

## The parameterization argument, drawing a decision tree

Assume without loss of generality that you always start by picking door #1. Now, the only freedom Monty has is to choose which door to open. He can only exercise this freedom when you have in fact chosen the car. In this case, let <span class="eeq">*p*</span> be the probability that Monty chooses to open door #2, and let <span class="eeq">*(1-p)*</span> be the probability that Monty chooses to open door #3. This parameter completely encodes Monty's part of the strategy.

Now, what about your part of the strategy? Well, all that you can choose is:

1. Your probability of switching if Monty opens door #2. (Call this <span class="eeq">*x*</span>)
2. Your probability of switching if Monty opens door #3. (Call this <span class="eeq">*y*</span>)

Now, draw a graph of all the possible outcomes

![decision graph](/img/monty-hall/decision-graph.png)

If you add up all the winning paths, you get:

<div class="eq" markdown="1">
&nbsp;&nbsp;&nbsp;&nbsp;ℙ[win]  
&nbsp;&nbsp;&nbsp;&nbsp;= ⅓ ( *p* (1-*x*) + (1-*p*) (1-*y*) + *y* + *x* )  
&nbsp;&nbsp;&nbsp;&nbsp;= ⅓ (1 + (1- *p*) *x* + *p* *y* )
</div>

Since <span class="eeq">*p*</span> and <span class="eeq">*(1-p)*</span> are non-negative numbers, an optimal strategy is to use <span class="eeq">*x*=*y*=1</span>, for which the win probability becomes <span class="eeq">ℙ[win]=⅔</span>.

**Credit:** Marte (who also drew the above beautiful graph)

**Why you might not like this argument:** If you made it this far, I think that's impossible.

<div style="font-size:70%; text-align:right;" markdown="1">
(Comment on [reddit](https://old.reddit.com/r/dynomight/comments/xm1x2o/the_conspiratorial_monty_hall_problem_with_proofs/?) or [substack](https://dynomight.substack.com/p/conspiratorial-monty-hall).)
</div>