---
layout: post
title: "Blocked persons and letters of marque"
image: /img/blocked-persons/flag1.jpg
tags: 
description: "What are letters of marque and reprisal, and who is on the US's list of Block Persons?"
permalink: /blocked-persons/
background_color: rgb(188,193,203)
category: "obsessive investigation"
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

Article I, Section 8, Clause 11 of the US Constitution reads:

> The Congress shall have Power to declare War, grant Letters of Marque and Reprisal, and make Rules concerning Captures on Land and Water;

What are these *Letters of Marque and Reprisal*?

They were essentially permission for private citizens or "privateers" to carry out acts of war against specific targets. If you could convince the government to write one for you, then you got to go searching the seas for plunder.

The last time these letters were used was during the War of 1812 wherein president Madison authorized the [Prince de Neufchatel](https://en.wikipedia.org/wiki/Prince_de_Neufchatel)---that's an American Ship, not a French vampire---to hunt British vessels. The last time they were *considered* was during Andrew Jackson's administration of 1829-1837.

Surprisingly enough, this practice led to abuses, like people getting letters from the governments on both sides in a war, or bribing corrupt governments to give their piracy a veneer of legitimacy. As a result, the practice was mostly banned by the [Paris Declaration of 1856](https://en.wikipedia.org/wiki/Paris_Declaration_Respecting_Maritime_Law).

The US refused to sign that declaration on the grounds that it had a puny navy and so needed to enlist private citizens for defense. This turned out to cause some difficulty during the American Civil War (1861-1865). Although the Union only had around 42 warships at the time, the Confederacy has almost none, and so turned to letters of marque, which disrupted Union shipping in the Caribbean.

This put Lincoln in a difficult position: He could have issued his own letters, but this would have angered Britain, which Lincoln hoped to get help from. He tried to belatedly sign the treaty, but Europe refused on the grounds that this was tantamount to taking a side in the conflict. In the end, the Union had to abstain from using letters of marque while the confederacy used them.

Legally, the Union did not regard the Confederacy as a legitimate party in a war, and so tried captured privateers as pirates, which would carry the death penalty. After Confederate President Jefferson Davis promised to execute captured Union officers in response, the Union backtracked.

To this day, the US has not formally agreed to the declaration, though it announced after the war that it would abide by it. So though it could *in theory* bring letters of marque back and this would *in theory* not violate any treaties, it would in practice be a big break with tradition and some people claim it would violate international law (if you believe international law exists). Anyway, [with](https://en.wikipedia.org/wiki/List_of_current_ships_of_the_United_States_Navy#Fleet_totals) 11 aircraft carriers, 72 destroyers, 22 cruisers, 22 littoral combat ships, 49 attack submarines, 14 ballistic missile submarines, etc., I'm thinking that the original motivation for using privateers doesn't apply these days.

That being said, Rep. Gooden has proposed [a bill](https://www.congress.gov/bill/117th-congress/house-bill/6869/) that would allow the president to issue letters of marque to people who could then go and seize the yachts, planes, or other assets of any Russian citizen on the List of Specially Designated Nationals and Blocked Persons. That would be exciting.

---

Speaking of which---there's a List of Specially Designated Nationals and Blocked Persons?

Yes, it's maintained by the Department of Treasury's Office of Foreign Assets Control. As I write this, it is [1,495,887 words long](https://home.treasury.gov/policy-issues/financial-sanctions/specially-designated-nationals-and-blocked-persons-list-sdn-human-readable-lists).

I wondered what was on this list, so I decided to check how often some different strings occur.

### Countries

First, I checked how often the names of the most populous countries in the world occur, normalized by population size.

![blocked-countries-perpop](/img/blocked-persons/blocked-countries-perpop.svg)

Apparently, USA ❤️ Phillipines which at 0.044 easily beats Japan (0.47) and India (0.55) for the fewest mentions per capita.

### Digital currencies

Next, I searched for `Digital Currency Address - X` for various values of `X`:

| `XBT`  | bitcoin      | 349  |
| `ETH`  | etherium     | 61   |
| `USDT` | tether       | 10   |
| `LTC`  | litecoin     | 9    |
| `BCH`  | bitcoin cash | 8    |
| `DOGE` | DOGE         | 0    |

### Genders

Here are the counts of `gender X` for different values of `X` (I checked for non-binary, etc. but there were no mentions.):

| `male`   | 4854 |
| `female` | 466  |


### Year of birth

I first got the counts for `DOB year;` for different values of `year`, but then realized that doesn't work. To see why, here's an entry from line 138357:

<div style='font-family:monospace; font-size:75%;' markdown="1">

> PUTIN, Vladimir (a.k.a. PUTIN, Vladimir Vladimirovich), Kremlin, Moscow, Russia; Novo-Ogaryevo, Moscow Region, Russia; Bocharov Ruchey, Sochi, Russia; Valdai, Novgorod Region, Russia; **DOB 07 Oct 1952**; POB Leningrad, Russia; nationality Russia; citizen Russia; Gender Male; President of the Russian Federation (individual) [RUSSIA-EO14024].

</div>
<br>

And here's one from line 83844:

<div style='font-family:monospace; font-size:75%;' markdown="1">

> IZZ-AL-DIN, Hasan (a.k.a. SALWWAN, Samir; a.k.a. "GARBAYA, AHMED"; a.k.a. "SA-ID"), Lebanon; **DOB 1963**; POB Lebanon; citizen Lebanon; Additional Sanctions Information - Subject to Secondary Sanctions Pursuant to the Hizballah Financial Sanctions Regulations (individual) [SDGT].

</div>
<br>

Sometimes it's the exact date and sometimes it's just the year. How to get the counts for years in both of these formats? After a lot of trepidation, I remembered hearing about these things called *regular expression* and *bash scripts* and after a lot of terror and shrieking it's "actually really easy":

```bash
for i in {1910..2010}
do
    c=($(grep "DOB .*$i;" sdnlist.txt |  wc -l))
    echo $i, $c
done
```

Plotting those numbers, we get this graph:

![blocked](/img/blocked-persons/blocked.svg)

Get to it, zoomers.