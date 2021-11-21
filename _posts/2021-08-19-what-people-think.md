---
layout: post
title: "Political polarization is partly a sample bias illusion"
image: /img/what-people-think/demand.jpg
tags: statistics policy
hero_light: false
dark_title: false
background_color: black
description: "How polarized are we? An overview of what people of different political parties, education levels, races, and political engagement think about politics."
permalink: /polarization-sample-bias/
background_color: rgb(143,177,189)
head: "<style>
video{
  display: block;
  margin: 0 auto;
}
details{
    padding-left: 10pt;
    margin-bottom: 10pt;
    border-left: solid 1px gray;
    }
details > summary{
  padding-bottom: 0pt;
  padding: 5pt;
  padding-left: 5pt;
  cursor: pointer;
}
img{
    display:block;
    margin-left: auto;
    margin-right: auto;
    max-width:min(100%,350pt);
}
table{
  display:block;
  }
table tr{
    border-style: hidden;
    text-align:left;
}
@media (min-width:501px){
table{
  margin-left: 15pt;
  max-width:100%;
  font-size: 90%;
}
}
@media (max-width:500px) and (min-width:301px) {
table{
  max-width:100%;
  font-size: 3.2vw;
}
}
@media (max-width:300px) {
table{
  max-width:100%;
  font-size: 0.5em;
}
.fixed{
    max-width:100%;
    overflow:scroll;
}
}
</style>
"
---

We're here on Earth for such a short time. So, I often wonder---what do people spend their days thinking about? Judging from the ever-increasing amount of screaming everywhere, the answer would seem to be politics. But is that right? What opinions do normal people really have?

Asking my friends won't help. They're a biased subpopulation---otherwise, we'd have, like, universal pet insurance funded by a land-value tax. (Or at least lower [particle levels in subways](https://dynomight.net/air/#particles-while-commuting).)

The solution is to find lots of random people, and ask them all a battery of questions. That is, polling.

## Polling

To better understand what people think, I found the [2020 Cooperative Election Study Common Content](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/E9N6PH) survey, which is a representative sample of 61,000 American adults. (They've helpfully made it impossible to link directly, but you can get a description by going [here](https://dataverse.harvard.edu/file.xhtml?fileId=4950256&version=2.0) and clicking on "Access File").

It asks boring questions like if people approve of Trump or Congress or whatever. But it also asks if people approve of a ton of different policies. I picked seven that I thought were representative. Here they are, along with their exact wording:

|**Immigration amnesty** | "Grant legal status to all illegal immigrants who have held jobs and paid taxes for at least 3 years, and not been convicted of any felony crimes."|
| **EPA CO2 regulation** | "Give the Environmental Protection Agency power to regulate Carbon Dioxide emissions." |
| **Medicare for all** | "Expand Medicare to a single comprehensive public health care coverage program that would cover all Americans." |
| **Ban assault rifles** | "Ban assault rifles" |
| **Abortion on demand** | "Always allow a woman to obtain an abortion as a matter of choice" |
| **10% more police** | "Increase the number of police on the street by 10 percent, even if it means fewer funds for other public services." |
| **Border security & wall** | "Increase spending on border security by $25 billion, including building a wall between the U.S. and Mexico." |

We have every answer from each person, along with their political party, education level, race, income, and so on.

## What people think

Here's a first visualization. This shows the percentage of people that support each policy, broken down into various groups.

[![support for all policies by group](/img/what-people-think/all-nonboring.svg)](/img/what-people-think/all-nonboring.pdf)

Here's what I conclude from this:

* **First two panels**: For most issues, a majority of people support the leftist / Democratic position.
* **Third panel**: Registered voters are more right-leaning than non-registered voters. However, this pattern reverses for assault weapons, where registered voters favor a ban.
* **Fourth panel**: More educated people lean left, though there's little effect on medicare for all.
* **Fifth panel**: Blacks, asians, and hispanics are more left-leaning than whites and native Americans.

Here's a chart that breaks people up in other ways that turn out to be less impactful: If they are an immigrant, their family income, where they live in the US, and if they used social media in the last 24 hours:

[![support for all policies by group](/img/what-people-think/all-boring.svg)](/img/what-people-think/all-boring.svg)

What does this mean?

* **These people lean more to the right**: Non-immigrants, richer people, those in the south and midwest, and social media users.
* **These people lean more to the left**: Immigrants, poorer people, those in the northeast and west, and social-media abstainers.

There are a few subtleties: The pattern reverses for the rich on abortion and the police. There's no pattern between if someone uses social media and how they feel about assault weapons or abortion. Naturalized citizens (but not non-citizens) favor increasing the number of police.

Some other ways you can break things up that seem interesting, but turn out to be kind of dumb. For example, here's what you get if you break things down by how people think the economy changed over the last year.

[![support for all policies by group](/img/what-people-think/all-economy.svg)](/img/what-people-think/all-economy.svg)

This looks interesting at first, but I think it just shows the power of motivated reasoning. Remember, this survey was done in the run-up to the 2020 presidential election, where Republican Donald Trump was running for a second term. Democrats convinced themselves the economy was terrible, while Republicans did the opposite. That's all this is showing.

## Heterodoxy

The above graphs are organized around *questions* rather than *people*.

Remember that, for each of the policies, around 55% of social media users were in support. How how does that 55% come about? Is it 55% supporting all the policies, and 45% opposing them all? Does everyone support some random subset? These situations would represent very different degrees of polarization, but we can't tell them apart from the above graphs.

We need to look at interactions between how individual people answered different questions. To do this, I calculated how many "Democratic answers" they gave, i.e. supporting the first five policies or opposing the last two. Here is a histogram of the full population:

[![histogram of full population support for policies](/img/what-people-think/hists-basic.svg)](/img/what-people-think/hists-basic.svg)

Around 10% of people give "all Republican" answers, while around 20% give "all Democratic" answers. Between the two it's a gradual change. This first glimpse doesn't look very polarized at all.

Things get more informative if we calculate histograms for different groups of people.

[![histogram of support for policies from different groups](/img/what-people-think/hists-nonboring.svg)](/img/what-people-think/hists-nonboring.svg)

This contains a ton of information.

* **First panel**: There's lots of overlap between the distribution of Republicans and Democrats. And independents aren't necessarily moderates! Their distribution looks much like the overall population. Plenty of them hold all Democratic or all Republican positions.
* **Second panel**: People who aren't registered to vote tend to support a mix of Democratic and Republican positions. People who are registered are more polarized.
* **Third panel**: People with more education are more likely to have all-Democratic opinions, and less likely to have heterodox positions.
* **Fourth panel**: Blacks mostly have mostly-Democratic opinions, whites are more variable, and hispanics are in the middle.

We can do the same thing for the other groups. Like above, these groupings don't tend to show particularly strong results. But remember, the lack of a result, is a result in and of itself.

[![histogram of support for policies from even more different groups](/img/what-people-think/hists-boring.svg)](/img/what-people-think/hists-boring.svg)

## On Caring

People aren't as polarized as I would have expected. Only around 30% of people hold "all-Democratic" or "all-Republican" positions. And there are reasonable numbers of people who identify as Democrats yet support nearly all Republican positions, or vice-versa.

However, *registered voters* are a lot more polarized than those not registered. This seems important! There are two possible explanations:

1. Maybe people decide not to vote if their opinions don't align well with a party. Why bother if you dislike all the options?
2. Maybe people who care more tend to have more extreme positions.

My instinct was that the second hypothesis was more correct. To test this, I looked for other questions that measure how "engaged" people are---did they read/forward/comment about politics on social media in the last 24 hours? (The "didn't" groups include people who didn't use social media at all.)

If you look at individual issues, you don't see much difference between these groups: 

[![support for policies by engagement](/img/what-people-think/all-caring.svg)](/img/what-people-think/all-caring.pdf)

Yet, if you look at *polarization*, the effect is clear:

[![histogram of support for policies from groups with different levels of engagement](/img/what-people-think/hists-caring.svg)](/img/what-people-think/hists-caring.pdf)

If we could separate people who read *multiple* stories, and made *multiple* comments, the trend would surely continue. People who engage with politics online are like everyone else, except more so. This is probably worth keeping in mind when you read about politics online. You can't hear everyone who isn't yelling.
