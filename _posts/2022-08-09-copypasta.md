---
layout: post
title: "A model for journalistic copypasta"
image: /img/copypasta/quixote.jpg
tags: 
description: ""
permalink: /copypasta/
background_color: rgb(100,136,90)
category: "uncategorizable"
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

Erik Hoel recently observed that high prestige outlets like *The Guardian* somehow get away with publishing low-effort and misleading "copypasta"---basically press releases disguised to look like real journalism. He also suggested that our culture might be better off if people paid more attention to independent writers, who couldn't get away with such things.

I agree, but I'm pessimistic. I think we need to give more consideration to *why* this happens. Because, unfortunately, I'd bet against any huge changes in the near future.

Why? Trust. Despite their mediocrity, people trust places like *The Guardian* and (I claim) this is *not a mistake*. Sadly, the world is full of outright lies, and it's hard to know who you can trust. *The Guardian* provides a consistent bare-minimum level of quality across a wide range of topics, which is harder than it looks. So I suspect the market is reasonably efficient: The fancy places provide real value, even when serving up journalistic mush, and people are making reasonable decisions when they read the fancy places.

Unless the distribution of writing changes somehow to upset that dynamic, I think the copypasta will continue.

## 1.

Let me summarize Hoel's post:

1. When fancy places publish an article based on a scientific paper, they use an egregious dark pattern: They deliberately make it hard to find the actual article. They don't link to it, or even provide the name.

   For example, did you notice how I didn't link to Hoel's article above? Wasn't that annoying? (It's [How prestige outlets like The Guardian get away with copypasta](https://erikhoel.substack.com/p/how-prestige-outlets-like-the-guardian).) Why is this considered acceptable?

2. Often, these places copy quotes from another article, or just a press release. Yet they make it look like they got the quote themselves.

3. If independent authors tried any of this nonsense, they'd be crucified.

4. So maybe everyone should follow more independent authors.

I'd even go a little further, and just say that for most complicated subjects, most prestigious outlets just aren't very good.

To pick an example close to my heart, take air purifiers. There are lots on the market, but we can't see indoor air pollution. To know if they are working, we need to test them.

The most well-known name in the air purifier game is the Wirecutter. Here is their testing regime:

* Generate some smoke in a room.
* Measure particles.
* Run a purifier for 30 minutes.
* Measure particles again.

Now, this isn't *terrible*, but it's not very good. You're only taking two measurements, so if there's noise in either, the final ratio will be off. This leads to them doing things like publishing two different tests of the same air purifier that imply a clean-air delivery rate that [vary by a factor of 2.4](/ikea-purifier/#on-tests).

Meanwhile, Internet People like [Smart Air](https://smartairfilters.com/en/blog/diy-purifier-tests/) or [Jeff Kaufman](https://www.jefftk.com/p/testing-air-purifiers) do tests that measure the entire trace of particles over time. Here's [from me](/better-DIY-air-purifier.html):

![box fan test](/img/copypasta/boxfan-performance-cropped.svg)

This is much more reliable, since it averages many measurements.

It's not like some kind of special brilliance is needed to come up with this test. Fankly, it's pretty obvious that this is a better way to test things, and I'm sure the Wirecutter is aware of it. They just don't do it.

## 2.

But why? *Why* do high-prestige places suck?

In one sense, it's explained the same way as everything else: 💵 💵 💵

This seems obvious, right? They don't link to journal articles that might make you leave their site, denying them the opportunity to stick more ads in front of your eyeballs. They give misleading quotes that make it look like they did more work because that allows them to churn out articles more quickly. The Wirecutter doesn't do more reliable tests of air purifiers because that would take more effort, and they don't think anyone cares.

But hold on. Sure, these places save money by cutting corners. But they could save even more by having their articles written by a team of pet monkeys. Why don't they put an unskippable video after each paragraph? Why does the market produce *this particular* level of quality and user-hostility? If people can get better information elsewhere now, why isn't everyone doing that?

One theory is that it's because *The Guardian* does "real" reporting, where they travel to places and talk to people and file freedom of information act requests and talk to their contacts in government off the record. This is clearly valuable, and perhaps some of that reputation spills over into their Quik-N-EZ journalism products. 

Probably. I think most people aren't aware how much they read is regurgitated press kits. But I don't think thats the full explanation.

Because---I'm pretty cynical about traditional journalism. I'm somewhere in the low tail of the population in terms of how much credibility I give it versus well-informed randos or the original scientific papers. Yet, *I still read traditional media*, sometimes including obvious copypasta. I even sometimes---please don't tell anyone---read the Wirecutter. 

As far as I can tell, so does everyone else. Why?

## 3.

Say you're driving down a lonely highway and you pull into a small town hungry and exhausted. You see three restaurants:

![3 restaurants](/img/copypasta/3-restaurants.svg)

Subway isn't good. At least, I don't know anyone who admits to liking it. (The Dynomight Biologist is aggrieved at having to inhabit a universe where it even exists.)

Of course, if you lived nearby, you'd try out each place and figure out which is best. But if you're just passing through and want to eat something quickly with a minimum risk of food poisoning, you might decide Subway is your best bet. It won't be great, but there are limits to how bad it can be.

That's because Subway has a very "broad" reputation. Say one person anywhere gets takeout from Subway but when they open the bag, a bat flies out and attacks them. That person could post their story online and cost the company tens of millions of sales. A single bad outcome can do more damage to Subway than to a Jimmy's. They both know this, and we know that they know it.

So some independent restaurants will specialize in making great food that will bring the locals back. Others will specialize in cutting costs and fleecing tourists. But if you *are* a tourist, it's hard to tell the difference.

## 4.

Say you're standing in a field with many holes of different depths and breadths. You'd like to find the deepest of these.

You'll soon notice that the depth of narrow holes is impossible to judge unless you're right above them. If you need to find a deep hole quickly, you'll probably end up picking one that's broad, even though you don't care about breadth.

So, imagine that in the restaurant scenario above, Jimmy's is good, Eat Pizza is terrible, and Subway is OK. You might picture it like this, with sightlines drawn:

![broad and narrow restaurants](/img/copypasta/broad-narrow1.svg)

Jimmy's might be amazing, but the creepy floating person can't see the difference from Eat Pizza.

Similarly, if you want information about air purifiers, I claim that <span style="font-family:monospace; font-size:80%;">dynomight.net</span> is good, while <span style="font-family:monospace; font-size:80%;">air-purifier-ratings.org</span> is godawful. (Please don't go there.) Meanwhile, the Wirecutter is not great, but it's not totally made up, either.

![broad and narrow websites](/img/copypasta/broad-narrow2.svg)

Having a bigger reputation gives an option more "breadth", which means lots of people will choose it, even when they only care about "depth".

## 5.

"Gell-Mann amnesia" is the idea that when any of us read newspaper articles in our area of expertise, we see that they're riddled with errors. But then we go on to the next article and assume it's fine.

This is usually presented as a kind of cognitive bias. We're presented with evidence that the newspaper isn't very good, but for some reason we refuse to update our judgements on the basis of that evidence.

I agree we trust the prestige media too much. But in another sense, Gell-Mann amnesia isn't wrong. For a random topic that you know nothing about, *The Guardian* may not be great, but they're unlikely to be *terrible*. Some independent writers are probably better, but there are lots that are worse, too, and it's hard to tell them apart.

For example: Sure, if an independent writer makes a mistake, commenters may tear them apart. But sometimes commenters will do that anyway, even when there is no mistake. And how do you know that negative comments aren't being removed? Unless you're familiar with the community, a comments section isn't very useful.

When can you trust independent writers? For me there are three cases:

1. I know enough about the topic to verify that the author seems to know what they're talking about.
2. I don't know the topic, but I've followed the author for a while and they've had many articles in category #1 so I trust them anyway.
3. There are extensive comments from a community that I know and trust.

See the problem? #1 is the only one that works for one-off articles on a random topic, and it only works when I'm already well-informed. #2 and #3 require me to spend lots of time in an advance forming an impression of an author or community. My guess is that most people don't follow *any* independent authors or communities closely enough for these to work. So they fall back to McJournalism. When it comes to writing, most people are "tourists".

## 6.

So here's the model. Let's assume four things:

1. There are four types of writing: Good independent writing, bad independent writing, SEO sludge, and copypasta from *The Guardian*.
2. It's hard to distinguish good independent writing from bad independent writing or SEO sludge, particularly if you aren't an expert on the subject or don't spend all your time on the internet.
3. But everyone recognizes *The Guardian*.
4. The same goes for algorithms.

If all these are true, what happens?

Some people are highly motivated. They will curate their information sources and follow whoever provides the most value. That will likely include some independent writers (maybe "good" ones or maybe "bad" ones).

But most people aren't all that motivated. They just want to get information quickly and go live their lives. So they get their information in three ways:

1. **Social media**. Most people aren't experts on most topics, so what trends on social media isn't very reliable. Some smaller places combat this with manual moderation. Others just let it run wild. Still other will try to reign it in using algorithms. But since their algorithms aren't very discriminating, that means they mostly promote *The Guardian* and un-promote everyone else.
2. **Search engines**. Because the algorithms can't tell good independent writers from bad, these will again mostly promote places like *The Guardian*. This is why it's basically impossible for an independent writer to get traffic from search for a health or finance related topic. Although, the SEO people are working day and night to stay ahead, so some of their sludge will get through, too.
3. **Big media outlets**. In this case: *The Guardian*.

Overall, only a small number of people are willing to make the effort that's needed to follow with independent writers without mediation from social signals or algorithms. But social signals don't convey reliability and all the algorithms can really do is just promote *The Guardian* even more.

## 7.

I think this shows why prestigious outlets will be so hard to displace: They provide somewhat-reliable information on a wide range of topics, which is difficult and valuable. For everyone to switch to reading independent authors would require a level of investment that only a minority of people will make for a minority of topics.

Now, I believe in independent writing. The idea of a population-wide cauldron of ideas fills me with hope. But unless we have a different way to *distribute* independent writing, it will remain a niche interest.

The fact is, *following* independent writers should not be a thing! (But, uh, don't let that stop you from following *me*. I have RSS and substack.) It's a tragedy that, today, someone who doesn't have an audience can't write a one-off article and have any confidence that anyone will read it. I'm sure that there's lots of great stuff published every day that goes unappreciated. But I'm more worried about the "invisible graveyard" of articles that never got written at all.

What we need, is a way to deliver independent writing that

* requires minimal effort from readers, and
* suggests stuff people are interest in, and
* gives reliable signals of trustworthiness.

I don't know how to do that or if it's even possible. But until that happens, I think that trying to make independent writing to overtake the McMedia is tilting at windmills.