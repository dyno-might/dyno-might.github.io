---
layout: post
title: "The big alcohol study that didn't happen: My primal scream of rage"
image: /img/alcohol-trial/bottles.jpg
tags: alcohol science policy
hero_light: false
dark_title: false
background_color: black
description: "Why did a huge alcohol RCT get cancelled? A strange story of science, academia, bureaucratic maneuvering, ambition, politics, capitalism, the deep state, secret emails, and slippery ethical slopes."
excerpt: "What does drinking do to your health? We can say two things with confidence: 1.  Drinking is associated with lots of health problems. 2. Heavy drinking is bad for you. Here's a graph of some associations. Someone who averages 10 drinks per day is 50x more likely to get cirrhosis than someone who doesn't drink at all (controlling for age, sex, and drinking history). This looks bad, but there are two caveats. First, it doesn't establish causality. It could be—if all you had was this figure—that cirrhosis causes hormonal changes that in turn create the urge to drink more. But we do know that heavy drinking is bad. That's partly because we know *how* alcohol causes problems. It causes cirrhosis by destroying liver cells. It causes cancer by getting converted to acetaldehyde and then damaging DNA. There are also randomized controlled trials (RCTs) that take heavy drinkers and get them to drink less. These inevitably show improved health (either health outcomes or biomarkers like blood pressure).
"
permalink: /alcohol-trial/
background_color: rgb(182,182,182)
category: "obsessive investigation"
comment:
    hacker news: https://news.ycombinator.com/item?id=28748037
---

What does drinking do to your health? We can say two things with confidence:

1.  Drinking is associated with lots of health problems.
2. Heavy drinking is bad for you.

Here's a graph of some associations.

![associations between alcohol and health](/img/alcohol-trial/issues.svg)

Someone who averages 10 drinks per day is 50x more likely to get cirrhosis than someone who doesn't drink at all (controlling for age, sex, and drinking history). This looks bad, but there are two caveats.

First, it doesn't establish causality. It *could* be---if all you had was this figure---that cirrhosis causes hormonal changes that in turn create the urge to drink more.

But we *do* know that heavy drinking is bad. That's partly because we know *how* alcohol causes problems. It causes cirrhosis by destroying liver cells. It causes cancer by getting converted to acetaldehyde and then damaging DNA. There are also randomized controlled trials (RCTs) that take heavy drinkers and get them to drink less. These inevitably show improved health (either health outcomes or biomarkers like blood pressure).

The second caveat is the little dip for diabetes and heart disease around 1-2 drinks. Some people think alcohol is causing this dip. Lots of mechanisms have been proposed: Maybe it reduces inflammation. Or maybe it impairs the cells that build up plaques in arteries. Or maybe it creates a hormonal imbalance that changes blood pressure regulation. Or maybe it increases HDL-cholesterol or insulin sensitivity or [adiponectin](https://en.wikipedia.org/wiki/Adiponectin) levels.

Or, maybe alcohol doesn't help diabetes and heart disease at all. [Mathews et al. (2015)](https://doi.org/10.1186/s12937-015-0011-6) try to model how alcohol affects the heart, ending up with this terrifying figure:


<img src="/img/alcohol-trial/pathways.png" alt="pathways between alcohol and heart disease" style="width:400pt" loading="lazy">

Alcohol does a *lot* of different things and interacts with a *lot* of other factors. It's great to try to unravel all this, but I don't trust anyone who says they understand everything with confidence.

If alcohol doesn't improve heart health, then why the dip? Well, it could just be that the same people who drink moderately also tend to exercise and eat well.

So we don't know if moderate drinking is bad for you. It almost certainly causes harms like cancer, but it might help heart disease enough to offset those harms. In the US, around 20% of adults drink 1-2 drinks per day. Even if the effects are modest, the collective impact is huge. Second perhaps to caffeine, alcohol is humanity's favorite drug. We need to know what it does.

This is the story of a trial that came close to answering this question and then exploded. At first, this looks like a simple story of corruption but when you look closely it's a *very complicated* story of corruption. {% comment %}Also, many of us have been shaken recently by the seemingly inexplicable things that happen when the government and scientific community interact. This is a peek behind the curtain---a case study of how things can go wrong despite so many people behaving rationally.{% endcomment %}

---

## We need an RCT

You might be thinking, "what we need to do is compare the health of people who drink different amounts, while controlling for income, diet, education, exercise, etc." The problem is that to a first approximation, "controlling" for things doesn't work. It requires tons of different assumptions, like what you control for, how you code stuff, and how you model everything. Reasonable people can disagree about those assumptions. For alcohol, reasonable people *do* disagree, and so they get estimates that are [all over the place](https://doi.org/10.1007/s11886-018-0962-2).

So what do we do? We take the long, slow, hard path:

1. Get a large group of people.
2. Tell some of them to drink moderately, tell the others not to drink at all.
3. Wait years, monitoring people to make sure they are actually drinking (or not) like they're supposed to.
4. Follow up and see which group is healthier.

Lots of things make this hard. Because the expected effects aren't huge, you need a *large* group of people. Because culture and [genetics](https://dynomight.net/alcohol/) vary, you need people from around the world. Because diseases take a long time to show up, you need to wait years. And imagine the challenge of telling people how much to drink and then making sure they follow your instructions.

An international effort monitoring thousands of people around the world for years---does that sound expensive?

## A solution

Back around 2013, the NIH's National Institute on Alcohol Abuse and Alcoholism ([NIAAA](https://en.wikipedia.org/wiki/National_Institute_on_Alcohol_Abuse_and_Alcoholism)) got interested in funding this. They figured it would cost on the order of \$100 million for the full trial. This doesn't seem crazy given the NIAAA's $500 million [annual budget](https://www.niaaa.nih.gov/about-niaaa/our-funding/congressional-budget-justification), but the NIAAA has lots of other priorities and didn't feel they had the money.

You know who has a lot of money, though? The alcohol industry. Worldwide, \$100 million of booze is sold every 30 minutes. In principle, the industry could directly fund a study, but who would trust it?

In 2016, it looked like the NIAAA had found an elegant solution:

* Five alcohol companies would donate money for a trial.
* The NIH would ask researchers to send proposals for how they'd run a trial.
* The NIH would choose the scientifically best proposal, just like they do with any government-funded grant. The donors would have no influence on the process.
* The make the results trustworthy, there would be a "firewall", with no communication between the industry and the research team.

Sounds promising. But if we go forward a couple of years, everything suddenly blows up.

**June 15, 2018**

[![headline: trial canceled as compromised](/img/alcohol-trial/image-20210901102128066.png)](https://www.washingtonpost.com/national/health-science/nih-cancels-100-million-study-of-moderate-drinking-as-irrevocably-compromised/2018/06/15/21f09fe2-7007-11e8-bf86-a2351b5ece99_story.html)

What happened? You might imagine banal corruption, with cocaine and overseas bank accounts, but it's nothing like that.

The real story is a much more interesting cocktail of science, academia, bureaucratic maneuvering, ambition, politics, capitalism, the "deep state", secret emails, and slippery ethical slopes. It's particularly interesting because it's a huge stroke of luck that we know about any of this. You have to ask how often similar things happen and *don't* blow up.

If you're brave, you can read the [165-page report](https://acd.od.nih.gov/documents/presentations/06152018Tabak-B.pdf) the NIH prepared before canceling the program. But I warn you: It's mostly out-of-order redacted emails written by people who wanted to conceal what was happening. There's an executive summary, but it's written in a frustratingly "government" style. There are also newspaper stories, but they don't try to give the full timeline.

After spending way too much time reconstructing things, here's the full story as best as I can tell.

## Timeline

(If you want an even-more-obsessive amount of information about the timeline, you can click on (more) after each of the sections.)

**2001 - 2013.** Kenneth Mukamal, a physician at [Beth Israel](https://en.wikipedia.org/wiki/Beth_Israel_Deaconess_Medical_Center) medical center and faculty member at Harvard Medical School, publishes many papers that argue that moderate alcohol consumption has health benefits, usually for heart disease or diabetes. During the same period, John Krystal, a psychiatrist and professor at Yale publishes many papers on alcohol, mostly focusing on addiction and mental health. (Many other researchers will be involved in this study, but these two are most prominent.)

<details markdown="1"><summary>(more)</summary>
Here's a small sample of Mukamal's papers:

> In summary, all of this evidence implicates alcohol consumption rather than lifestyle factors [...] as the primary factor in the  lower rates of cardiovascular disease found among moderate drinkers. [(2001)](https://pubmed.ncbi.nlm.nih.gov/11910702/)
>
> Compared with abstention, consumption of 1 to 6 drinks weekly is associated with a lower risk of incident dementia among older adults. [(2003)](https://doi.org/10.1001/jama.289.11.1405))
>
> In this large cohort study of older adults, there was a lower risk of congestive heart failure associated with moderate drinking compared with abstention. [(2006)](https://doi.org/10.1016/j.jacc.2006.02.066)
>
> There is convincing evidence that light-moderate, non-binge alcohol intake reduces the risk of coronary heart disease. [(2009)](https://doi.org/10.1111/j.1530-0277.2008.00828.x) 
>
> In a nationally representative samples of U.S. adults, light and moderate alcohol consumption were inversely associated with cardiovascular disease mortality, even when compared with lifetime abstainers [(2010)](https://doi.org/10.1016/j.jacc.2009.10.056) 
>
> Secondary analysis of mortality from all causes showed lower risk for drinkers compared with non-drinkers [(2011)](https://doi.org/10.1136/bmj.d671)
>
> Long-term moderate alcohol consumption is inversely associated with  all-cause and cardiovascular mortality among men who survived a first myocardial infarction. [(2012)](https://doi.org/10.1093/eurheartj/ehs047)

I'm not joking about this being a small sample. [His list of publications](https://scholar.google.com/citations?user=cROjkDcAAAAJ&hl=en) (up to the present day) has **185** hits for "alcohol". I didn't read all them, but after randomly sampling 20 or so, I found that almost all have a positive spin on the health effects of alcohol. The only exception I found was [this paper from 2010](https://doi.org/10.1161/STROKEAHA.110.580092) that suggests stroke risk goes up while alcohol is in your system. On that paper, Mukamal was the 4th author out of 6. (In academic publications, the people with the most influence on the paper are typically either first (actually did the work) or last (most senior/famous muckety-muck).)

During a similar period, John Krystal also published [many papers on alcohol](https://scholar.google.com/citations?user=Bu-gRtYAAAAJ). These mostly focus on various technical issues related to addition, e.g. if the [GAD2 gene might contribute to alcoholism](https://doi.org/10.1002/ajmg.b.30377). Some have a clearly negative view of alcohol, e.g. one that explores how alcohol dependence has effects that are [similar to accelerated aging](https://doi.org/10.1017/S1041610200006621).


</details>

**Early 2013.** Some NIAAA staff are convinced that moderate drinking is good for you, and an RCT could prove it conclusively enough that doctors might recommend it to patients like they do with aspirin now. (We don't know who these staff were, but Margaret Murray was probably among them.) They have the idea of getting the alcohol industry to fund the study but face two problems. First, the alcohol industry wants lots of details before forking over any cash. Second, the NIAAA isn't allowed to solicit from industry. They try to get around these problems by having outside researchers (including Mukamal and Krystal) meet with industry to give details on how such a trial might work. This creates a dynamic where everyone (the NIAAA, the alcohol industry, Mukamal) wants to coordinate with each other, but maintain a pretense of being isolated. There's lots of scheming about how information should flow to maintain this pretense.

<details markdown="1"><summary>(more)</summary>

You can read the full business case the NIAAA put together [here](/img/alcohol-trial/business-case.pdf). Here's an excerpt:

> Consistent evidence [...] has demonstrated that moderate drinking [...] lowers one's cardiovascular, metabolic [...], and neurodegenerative [...] disease risk. [...] the benefit is not negated by the potential increases in risk for specific cancers or other illnesses
>
> [...]
>
> no government public health entity or scientific/medical professional society has been willing to recommend that patients be advised to consider using alcohol as a risk-reduction intervention. [...] there remains a hesitance to be more proactive in the recommendation without a large-scale fully randomized clinical trial

Discussion around that time shows that they didn't want to spend the money that would be required for such a trial.

![image-20210901165722968](/img/alcohol-trial/image-20210901165722968.png)

Other discussion shows that they thought they might be able to get the alcohol industry to pay for it. However, they had two concerns. First, they knew the alcohol industry wouldn't be willing to fund a study without some idea of what it would look like.

![image-20210901171157354](/img/alcohol-trial/image-20210901171157354.png)

Second, they knew that they weren't allowed to "solicit" funding from the industry, and they were worried that they might be crossing a line.

![image-20210901165948433](/img/alcohol-trial/image-20210901165948433.png)

They settled on the strategy of having the industry make a "gift" to [FNIH](https://en.wikipedia.org/wiki/Foundation_for_the_National_Institutes_of_Health), the arm of the NIH that was set up to take industry money and then do NIH-stuff with it.

![image-20210901171527061](/img/alcohol-trial/image-20210901171527061.png)

At the same time, they decided that they could get rid of the appearance of soliciting by getting an external researcher to make the case. They settled on... Kenneth Mukamal. (Here BI appears to refer to Beth Israel, a medical center affiliated with Harvard where Mukamal holds an appointment.)

The record is silent on exactly *why* they chose Mukamal. My guess is that it's partly because of Mukamal's pro-alcohol research record, and partly because it helped to overcome some weird inscrutable issues regarding collaborations between Harvard and Beth Israel.

![image-20210901172140639](/img/alcohol-trial/image-20210901172140639.png)

I think you can see the seeds of destruction in the above email. You have these three entities (the NIAAA, the alcohol industry, and outsider researchers) who all want to pretend that they are isolated from each other whilst not actually being isolated.  The NIAAA wants someone else to make the approach to overcome their prohibition of solicitation, even though they've obviously set this whole thing in motion. The alcohol industry is excited about what they hear directly from the researcher, but then they want the plan to come "from the NIAAA".

Who were these NIAAA staff? Thanks to all the redaction, for the most part we don't know. We only have two hints. First, we can look at who ended up quoted in news reports. This is George Koob (who wasn't at the NIAAA in 2013) and Margaret Murray. Murray also ended up in the [final report](https://dx.doi.org/10.1177/2047487320912376) written by the researchers on the design of the study, where it's stated that Murray helped develop the initial proposal to the NIAAA.

</details>

**July 12, 2013.** After getting some positive feedback from the industry, NIAAA staff decide to create a "planning grant". This was supposed to be open to anyone, but the staff conspire to steer the money to Mukamal by having a super-short deadline (overruled by NIH-central) requiring pre-approval (also overruled, sort of), and asking for a very specific clinical trial. Two staff go as far as to take fake "personal vacations" to travel to Boston and help Mukamal write the grant. When the window to apply for the grant closes on November 1, Mukamal is the only applicant.

<details markdown="1"><summary>(more)</summary>

On July 12, 2013, the NIAAA published a [NOT-AA-13-004](https://grants.nih.gov/grants/guide/notice-files/NOT-AA-13-004.html). By NIH rules, this was a public opportunity, meaning any researcher could submit and win the grant if they had the best science. Yet they obviously wanted "their" PI to win:

>  I would be fine with a one-year term; I think the PI can easily meet that, given that we have gone over in a lot of detail what the ultimate RCT should look like; plus that tight a timeframe would discourage other applicants who have not even begun to think about this idea yet !

They stacked the deck in three ways. First, they asked for an extra-short deadline, and said that applications would need to get pre-approval before submitting a grant. Both of these tricks were overruled by NIH central, though "prior consultation" was still "strongly encouraged". Second, rather than a typical open-ended call for research, they asked for a specific trial to be done---coincidentally exactly the trial Mukamal wanted to do. Third, NIAAA staff decided to physically travel to Boston to help Mukamal write the grant. Since this was totally forbidden, they went another way.

> I am going to Boston for a brief "vacation". It would be entirely coincidental if I happened to spend a day with some friends who might be in the process of writing a U34 grant application, and if we also just happened to have some "hypothetical" discussions about details of such a study. This is a purely personal, i.e., NOT NIAAA-funded or authorized, trip.

All the scheming from the NIAAA worked. Ultimately, they received exactly one application: from Mukamal. There's a complex subplot regarding the review of this grant: There were serious concerns from someone on the NIAAA advisory council, but staff in the NIAAA rebutted them, and then were able to exclude them from voting on procedural grounds. In email, they reassured Mukamal "Do not worry" and that "They are inappropriate comments". In response, Mukamal simply said "here's a draft for the U34. I tried to be discrete (sic) about the industry stuff."

</details>

**November 21, 2013**. There is a meeting at the [Distilled Spirits Council](https://en.wikipedia.org/wiki/Distilled_Spirits_Council_of_the_United_States) in Washington, DC between the alcohol industry, the NIAAA, and three researchers, including Mukamal and Krystal. Someone from industry later reported to NIAAA staff that "he was tremendously enthused about the project" and that they would need similar meetings with other companies. He specifically wanted to hear more from Mukamal and Krystal. There was another meeting at the same location on Jan 28, 2014.

<details markdown="1"><summary>(more)</summary>

This meeting took place  [Distilled Spirits Council](https://en.wikipedia.org/wiki/Distilled_Spirits_Council_of_the_United_States)'s headquarters in Washington DC

Here's an email between NIAAA staff following this meeting. Clearly, the industry liked what they heard. They wanted to hear more from the NIAAA, and specifically said that they wanted two of the same researchers.

Here's a key to help you understand the following email:

* DISCUSS is the [Distilled Spirits Council of the United States](https://www.distilledspirits.org/) (an industry group)
* [Diago](https://en.wikipedia.org/wiki/Diageo) was then the world's largest distiller. They make vodka, rum, gin, beer, and whiskeys that you've heard of.
* The "guy from Harvard" is Mukamal.
* The "guy from Yale" is (almost certainly) [John Krystal](https://medicine.yale.edu/profile/john_krystal/).

![image-20210901173336026](/img/alcohol-trial/image-20210901173336026.png)

According to the [New York Times](https://www.nytimes.com/2018/03/17/health/nih-alcohol-study-liquor-industry.html), representatives of Anheuser-Busch InBev, Heineken and Diageo later confirmed that these meetings were important for their decision to go ahead and fund the trial:

> “When Heineken was invited by the N.I.H. to partially fund the  N.I.A.A.A. trial for a duration of ten years, as part of our decision  making process, the scientists presented the research project to us so we would have a sound understanding of the trial,” Michael Fuchs, a  company spokesman, said in an email.

</details>

**January 2014.** The preliminary planning grant is reviewed. One reviewer was concerned about the alcohol industry, but NIAAA staff were able to exclude the reviewer from voting on procedural grounds. When responding to reviewer comments, Mukamal states that he "tried to be discrete [sic] about the industry stuff." The grant is formally awarded on March 20, 2014.

<details markdown="1"><summary>(more)</summary>

There's a whole complex subplot about the review process for this grant: There was a secondary review from the NIAAA advisory council, who raised concerns about the alcohol industry. Staff in the NIAAA provided a rebuttal to these concerns, and were able to exclude that person's vote on procedural grounds. In an email, they reassured Mukamal.

![image-20210909161317342](/img/alcohol-trial/image-20210909161317342.png)

 Mukamal responded as follows

![image-20210903182255896](/img/alcohol-trial/image-20210903182255896.png)

There was a parallel conference grant that was awarded at the same time, also successfully steered to Mukamal.

</details>

**February 26, 2014.** There is a meeting in Palm Beach, Florida, including the alcohol industry, at least one NIAAA staffer, and outside researchers. Mukamal's slides stated, "A definitive clinical trial represents a unique opportunity to show that moderate alcohol consumption is safe and lowers risk of common diseases."

<details markdown="1"><summary>(more)</summary>

Little seems to be known about this meeting other than that it took place at [The Breakers](https://en.wikipedia.org/wiki/The_Breakers_(hotel)) hotel in Palm Beach Florida. The [New York Times](https://www.nytimes.com/2018/03/17/health/nih-alcohol-study-liquor-industry.html) appears to have slides from this meeting and gives the following quotes:

> “A definitive clinical trial represents a unique opportunity to show that moderate alcohol consumption is safe  and lowers risk of common diseases,” said one slide in the scientists’  presentation at The Breakers. “That level of evidence is necessary if  alcohol is to be recommended as part of a healthy diet.”
>
> “We have strong reason to suspect so,” said another slide, referring to the large number of studies suggesting that moderate alcohol may be linked  to reduced risk of cardiovascular disease.

Since I have no other relevant information, here's a picture of the hotel instead:

![the breakers hotel](/img/alcohol-trial/breakers.jpg)

</details>

**February 28, 2014.** Wine Industry Insights publishes ["US Govt Asking Industry To Fund Most Of $50 Million Alcohol/Health Study"](https://wineindustryinsight.com/?p=52139), causing a ton of concern inside the NIAAA from people who didn't know what was going on. The people involved openly discuss how to best conceal information.

<details markdown="1"><summary>(more)</summary>

In early 2014, Wine Industry Insight published an [article](https://wineindustryinsight.com/?p=52139) that said:

> The federal government, along with scientists from Yale and Harvard, are asking wine, beer and spirits organizations to fund a landmark clinical study on the health effects of moderate alcohol consumption estimated  to cost \$36 million to \$54 million.
>
> [...]
>
> “While there are risks in every new endeavor, this study will be a landmark piece of research that should legitimize moderate consumption,” said a member of the DISCUS board of directors, speaking off the record to Wine Industry Insight.
>
> The source added that the only risk involved is that some new negative information might be uncovered. “The evidence is overwhelming that moderate consumers live longer,” the source said. “The risk of discovering negative information is very small given the decades and billions that the government has spent trying to prove the French Paradox wrong.”
>
> [...]
>
> The prime movers from the university research sector are [John Krystal] of the Yale University School of Medicine and [Kenneth Mukamal] of the Harvard University Medical School.

This caused a lot of concern within the NIAAA.

![image-20210901174401529](/img/alcohol-trial/image-20210901174401529.png)

Clearly, information was not being shared very well within the NIAAA. Some people asked what was going on.

![image-20210901174424500](/img/alcohol-trial/image-20210901174424500.png)

Someone at the [Division of Metabolism and Health Effects](https://www.niaaa.nih.gov/research/extramural-research/division-metabolism-and-health-effects) naively suggested that it was an FNIH initiative, so it made sense that they had no idea what was going. (Remember, the NIAAA led this from the beginning, and only later decided the FNIH was the easiest way to structure funding.)

![image-20210903142713840](/img/alcohol-trial/image-20210903142713840.png)

Here's an email later the same day that is identified as part of the NIAAA communications office. They are clearly annoyed and/or worried. I think this is the same person as in the previous email (comparing the widths of redacted email addresses and phone numbers and such.)

![image-20210901175415984](/img/alcohol-trial/image-20210901175415984.png)

Here's an email from one NIAAA senior staff member to another saying that they should basically conceal as much information as possible. The person they are talking about concealing information from is an NIAAA division director.

![image-20210901175537712](/img/alcohol-trial/image-20210901175537712.png)

Eventually the furor about the article all seems to die down, though it's unclear when or if the people wondering what was going on become informed.


</details>

**June 21, 2014.** There's a meeting in Seattle, led by Mukamal, and including NIAAA staff and the alcohol industry. Afterward, representatives from industry send Mukamal a list of technical concerns about the design of the RCT, including what outcomes to measure, the treatment population, adherence, dropouts, monitoring, using beer vs. spirits, and incentives to participate. Mukamal sends back a [detailed response](/img/alcohol-trial/mukamal-response.pdf), sort of saying "well, this is what *I* would do *if* I happened to win the grant..." and then giving some reasonable answers.

<details markdown="1"><summary>(more)</summary>

This meeting took place at the Hyatt Regency in Bellevue, Washington.

Following this meeting in July, representatives from the [ICAP](https://en.wikipedia.org/wiki/International_Alliance_for_Responsible_Drinking) and [DISCUS](https://www.distilledspirits.org/) (industry groups, ICAP is now IARD), [Diago](https://en.wikipedia.org/wiki/Diageo) (the world's largest distiller), and [AB InBev](https://en.wikipedia.org/wiki/AB_InBev) (the world's largest brewer) sent Mukamal a detailed list of concerns about the design of an RCT. In August, Mukamal gives a [7-page](/img/mukamal-response.pdf) response responding to all concerns in detail.

I can't emphasize enough: In this exchange, industry concerns and Mukamal's response look almost completely non-scandalous. They seem like reasonable concerns from people that are paying a lot of money and want to make sure the trial is well-designed: What outcomes will be measured, who will be eligible to enroll in the trial, would it be better to have fewer sample sites with larger populations, what if patents don't comply with their instructions to (not) drink, what if patents quit the study, what biomarkers will you measure to be sure if people are drinking or not.

The one bit that does seem a little suspicious is this from the beginning of Mukamal's response:

![image-20210915113753690](/img/alcohol-trial/image-20210915113753690.png)

It's not clear how to judge this. Did industry really believe that any investigator could win? Or had the NIAAA winked at them enough that they could be confident who would win?

</details>

**November-December, 2014.** A large joint conference call is coordinated between the alcohol industry, NIAAA staff, and researchers including Mukamal. Here are three topics that industry asks about:

1. Will the data be shared with other researchers? Mukamal states that they would make "controlled data sets" available one year after the study ends.
2. Might industry funding call the study into doubt? Mukamal reassures that it's fine because there will be a "firewall" between research and industry.
3. Will results will be published even if they are negative? Mukamal says yes, but they will "most certainly" see a positive impact at least for diabetes. 

<details markdown="1"><summary>(more)</summary>

The purpose of this call is "an opportunity to understand more about the protocol that is currently under development". This call takes place on December 8, 2014. Here's some quotes from the minutes of this meeting:

Regarding the overall trial:

> * **What would a trial look like?** - It would be a randomized, multicenter, trial. Individuals interested in the trail will come the field centers and sign a consent form. They will be at high cardiovascular risk (so we can conduct this in a 5yr period). They would fall in an intermediate category of drinking a little, but less than daily. They would be randomized to not drink at all or to drink daily for 5 years.
>

Regarding data sharing:

> * <u>ABI, [redacted]</u> Can you describe the data availability to be shared with other researchers? What happens to the blinded data after the study? And will there be any differentiation btwn wine, beer, and spirits?
>
> [redacted] -  We will need to make data available a year after the study concludes, and we can do so in the form of controlled data sets.

Regarding funding:

> * <u>Suntory, ?</u> – Is the funding source going to impact the interpretation of the results by external agencies?
>
>   [redacted] – We will be running the study in conjunction with NIH/NIAAA who is the biggest source of data for the WHO. As long as that firewall is established between industry, and the design/ management of the trial, it should remove doubt.
>

Regarding possible negative results.

> * <u>Suntory, ?</u> – Is the intention to publish results even if they are less desirable eg. negative or mixed?
> * [redacted] – Yes, however the peer review comments from the initial analysis of our study design were that we will most certainly see an impact for DM and we are not enrolling people of high risk for breast cancer.

Here "DM" is diabetes mellitus. You can read the full minutes for this meeting [here](/img/alcohol-trial/ICAP-minutes.pdf). (For fun, try to find where "Ken" slipped through redaction.)


</details>

**February 26, 2015.** Murkamal and NIAAA senior staffers coordinate edits to an email that will be sent to someone in industry. This email states that yes, they really need $100 million, and "one of the important findings will be showing that moderate drinking is safe."

<details markdown="1"><summary>(more)</summary>

They are coordinating an email to send to some [redacted person, probably part of [ICAP](https://en.wikipedia.org/wiki/International_Alliance_for_Responsible_Drinking)]. Here's the full quote to show that it isn't taken out of context:

> One of the important findings will be showing that moderate drinking is safe. Small studies pose a serious risk of spurious results, including showing harm simply because of bad luck. As we discussed, this will be the first RCT (i.e. “gold standard”) evidence of this and it is important to answer statements made by WHO and others that “no level of alcohol is safe” with certainty.

The rest of the message is mostly devoted to explaining that yes, they really need the entire 100 million dollars.

![image-20210909174958306](/img/alcohol-trial/image-20210909174958306.png)

![image-20210909175010038](/img/alcohol-trial/image-20210909175010038.png)


</details>

**Oct 5, 2015.** The NIAAA publishes the funding opportunity for the big RCT. The published document implies that only someone who won the earlier planning grant---meaning only Mukamal---should apply. In December, Mukamal applies, and in January the opportunity closes without receiving any other applications.

<details markdown="1"><summary>(more)</summary>

The funding opportunity is ["Multi-Site Randomized Controlled Clinical Trial Research Center on Alcohol's Health Effects"](https://grants.nih.gov/grants/guide/pa-files/PAR-16-363.html), published on October 5, 2015.

Apparently the NIAAA originally requested that this funding opportunity be a limited competition where only people who had won the preliminary planning grant could apply, Mukamal would be eligible. NIH central rejected this, however, the funding opportunity still "encouraged" this with language like the following:

> Applicants for the U10 Clinical Trial Implementation Cooperative Agreement must be able to begin the trial without further planning activities when the U10 is awarded. Therefore, investigators who have already completed planning activities through an NIAAA-funded U34 clinical trial planning grant are expected to apply.

On December 18, Mukamal submits his application. You can read it in its entirety [here](https://clinicaltrials.gov/ProvidedDocs/30/NCT03169530/Prot_SAP_004.pdf). It begins like so:

> The health effects of alcohol consumption have been key public health concerns for millennia. Alcohol consumption is highly prevalent, with remarkably little change in prevalence over the last century, and excessive use is a risk factor for innumerable adverse health outcomes, including cognitive impairment, cancer, cardiomyopathy, cirrhosis, gastrointestinal bleeding, trauma, and social devastation. Although the benefit of avoiding alcohol misuse is well-accepted and uncontroversial, the risks and potential benefits of alcohol consumption when consumed within moderation remain unproven. Observational studies document a lower risk of coronary heart disease and diabetes among moderate consumers relative to abstainers, but they also suggest a higher risk of breast and gastrointestinal cancers, and the possibility of residual confounding of these associations by other characteristics cannot be excluded. No clinical trial has been conducted to test the hypothesis that moderate alcohol consumption lowers risk of cardiovascular disease or diabetes compared to abstention, yet public policy continues to be made regarding safe limits of drinking. A definitive yet feasible clinical trial investigating whether moderate alcohol consumption lowers cardiovascular and diabetes risk is needed; indeed, it was the foremost recommendation of the NIAAA Expert Panel on Alcohol and Chronic Disease Epidemiology.

On January 12, 2016, the funding opportunity closed. There were no other applications.


</details>

**March-September 2016.** The proposal is reviewed by the NIH, and eventually awarded to Mukamal. The project begins on September 30.

<details markdown="1"><summary>(more)</summary>

The panel peer review happened on March 29, 2016, while the advisory council teleconference review happened on April 19, 2016. Little information seems to be publicly available about these reviews. The "memorandum of understanding" was signed on September 16, 2016 and the "cooperative agreement" made on September 30, 2016. The grant was to run from September 30, 2016 to July 31, 2021.

</details>

**July 3, 2017.** The New York Times publishes ["Is Alcohol Good for You? An Industry-Backed Study Seeks Answers"](https://www.nytimes.com/2017/07/03/well/eat/alcohol-national-institutes-of-health-clinical-trial.html). This quotes Margaret Murray of the NIAAA as saying that five companies had pledged $67.7 million, and has a lot of general skepticism of the reliability of industry-sponsored research. There's this quote from George Koob, then director of the NIAAA:

> “This study could completely backfire on the alcoholic beverage  industry, and they’re going to have to live with it,” Dr. Koob said.  “The money from the Foundation for the N.I.H. has no strings attached.  Whoever donates to that fund has no leverage whatsoever — no  contribution to the study, no input to the study, no say whatsoever.” 

There's also this:

> Dr. Mukamal [...] said he was not aware that alcohol companies were supporting the trial financially. “This isn’t anything other than a good old-fashioned N.I.H. trial,” he said. “We have had literally no contact with anyone in the alcohol industry in the planning of this.”


**October 26, 2017.** Wired publishes ["A Massive Health Study on Booze, Brought to You by Big Alcohol"](https://www.wired.com/story/a-massive-health-study-on-booze-brought-to-you-by-big-alcohol/). Aside from more general skepticism of industry funding research, it also points out that Murray and Koob at the NIAAA seem to have a cozy relationship with the industry. It's got some quotes from a researcher in South Africa that sort of make Mukamal look like a jerk, and finally this:

> Yet when I spoke to Mukamal in February 2017, he said he didn’t know about the Foundation’s  negotiation for industry contributions “until relatively recently.” [...]  "We have no contact with funders other than NIAAA itself whatsoever," he wrote.


**Feb 5, 2018.** The trial begins enrolling patients.

**March 17, 2018.** The New York Times publishes ["Federal Agency Courted Alcohol Industry to Fund Study on Benefits of Moderate Drinking"](https://www.nytimes.com/2018/03/17/health/nih-alcohol-study-liquor-industry.html). They interviewed former federal officials and used Freedom of Information Act requests to get emails and travel vouchers related to the grant. This story reveals that, contrary to Mukamal's claims, there were various meetings in 2013 and 2014. This includes a "working lunch" at the Beer Institute convention in Philadelphia that's not in my timeline above because I can't figure out when it happened.

**March 20, 2018.** Based on the previous above article, NIH director Francis Collins [orders an investigation](https://www.nytimes.com/2018/03/20/health/mukamal-alcohol-nih-funding.html) into the trial.


**April 11, 2018.** Collins appears before the House Appropriations Subcommittee on Labor, Health and Human Services to discuss the NIH's budget. When asked about the trial, Collins responds that he is very concerned and is investigating the issue as a matter of priority. (You can watch the video [here](https://www.youtube.com/watch?v=ahKnVXzVb3o&t=51m38s).)


**May 10, 2018.** The NIH [suspends enrollment](https://www.scientificamerican.com/article/after-controversy-over-industry-funding-nih-halts-enrollment-in-moderate-drinking-study/) in the trial.

**June 8, 2018.** Anheuser-Busch [pulls its funding](https://www.nytimes.com/2018/06/08/well/anheuser-busch-to-pull-funding-from-major-alcohol-study.html).

**June 15, 2018.** Based on a [recommendation](https://acd.od.nih.gov/documents/presentations/06152018Tabak.pdf) from an NIH working group, Collins [terminates](https://acd.od.nih.gov/documents/presentations/06152018Tabak.pdf) the study.

## Skepticism

You might think I'm out of my mind, but it's hard for me to celebrate this trial being canceled. Obviously, lots of inappropriate stuff happened. But when you think about *why* you'd cancel the trial, the arguments aren't as strong as you might think. Here are the arguments I've seen:

**The NIAAA and Mukamal lied to the public.**

True. They claimed this was just like any other NIH grant, where any researcher could propose a study design, and the NIH would choose the best entirely based on scientific merit. In reality, the NIAAA intentionally steered the money to one pro-alcohol researcher who coordinated the plan with the alcohol industry.

That was bad. But this doesn't *necessarily* imply cancelation, if the study would have been useful. If the point is to punish people, let's not hurt ourselves in the process, right?

**If the study were done, no one would trust the results.**

Possibly true, but let's be careful. Are we claiming that no one *should* believe the results, or just that no one *would*? If it's the latter, isn't that kind of a weird reason to cancel a trial? Let's break this down. Why might you not trust the results?

**I don't trust the research team.**

Clearly, Mukamal *thought* the trial would show a benefit, but that doesn't mean he was right. Anyone who's worked in science knows what it's like to confidently run an experiment, only to get smacked in the face by reality's indifference to your pet theories and career goals.

But OK, say you don't trust the research team. What do you think they are going to do, fabricate data? The study was a collaboration of a large team around the world. The data would be stored at a Data Management Center (whatever that is) at a different university and inspected every six months by a monitoring board. Here's the [organizational structure](https://doi.org/10.1177/2047487320912376) for the study:

![organization of MACH15 study](/img/alcohol-trial/org.svg)

This isn't some excel spreadsheet stored on one grad student's laptop. You'd need a big conspiracy.

Or maybe you don't think they'd falsify data, but that for publication they would use some tortured data analysis to spin the results. The thing is, it's not unusual to have researchers who want to find a given result---that's every researcher everywhere! We have a system for this, which is that studies pre-register their statistical analysis. This study did that, and the plan seems fine (although, see below). There just aren't many places to hide the bodies.

<details markdown="1"><summary>If the full data would have been public, that would be another major safeguard against selective data analysis, and made it even harder for anyone to fake things. I can't tell exactly what would have been public. Mukamal mentions making it public when planning the grant with industry. But then the actual grant proposal says nothing about it.
</summary>

 [NIH guidelines](https://grants.nih.gov/grants/policy/data_sharing/data_sharing_guidance.htm) say that any research costing $1/2 million or more are expected to include a plan for sharing final research data for research purposes, or state why data sharing is not possible. Yet, in the actual grant proposal, here's the entirety of that plan:

![image-20210916185241830](/img/alcohol-trial/image-20210916185241830.png)

That's it. It's the entire thing. As far as I can tell, there's no mention of making the data public. This is odd, since when he planned the trial with the alcohol industry earlier, he said he'd *have* to make the data public, at least in "controlled" form. Why did this disappear from the final grant? If you had any intention to publish the data, you'd make *absolutely sure* it was in the proposal. That way, if anyone tries to stop you, you can point out that you're committed to it.

I'm not sure what's going on here. Maybe the sharing details were in another document that isn't publicly available? One hint is that at least some of the data would be made public is that for the small amount that was actually collected, some data *is* public today, and can be viewed [here on clinicaltrials.gov](https://clinicaltrials.gov/ct2/show/results/NCT03169530). It basically says that 32 people were randomized into alcohol or abstention groups and nobody had any adverse events whatsoever.

However, my [ever-patient biologist friends](https://dynomight.net/2020/12/22/what-i-learned-about-covid-19-from-pestering-a-bunch-of-biologists/) point out that there is no obligation to actually put data on clinicaltrials.gov. You can easily confirm this by looking at random studies that most don't seem to bother. I really have no idea if the researchers for the alcohol study were planning to put their data on the site, or just did it after the study blew up since it shows nothing and makes them look (marginally) better.
</details>

**The study seems designed to deliver a pro-alcohol result.**

Two concerns have been made about the study design. For one, it's plausible that the biggest harms of alcohol (e.g. cancer) appear later, while cardiovascular and diabetes benefits (if they exist) happen quickly. So a five-year study might find alcohol reduces mortality while a ten-year study could show the opposite.

Fine, but what's the principle here? Should we cancel all studies where there's a much more expensive and difficult variant that would be more conclusive? We know this is an issue now, and we'd still know it when interpreting results after the study is done.

Another concern is that the study population maximizes the chances for alcohol to look good: It would only enroll people who are either ≥75 years old or at elevated risk for cardiovascular disease while excluding anyone with liver disease, a personal history of colon/liver/breast cancer, a family history of breast cancer, suicidal ideation, or dementia. If I wanted to maximize the chance that alcohol could be beneficial while minimizing the chance that alcohol could be harmful, this is the population I would choose.

If you want a final verdict on if moderate drinking is safe, I agree this seems like stacking the deck. I'd prefer a random sample of all adults. You can call this a "bias". But you can also call it "refusing to take the sampling scheme into account when interpreting results". There's still value in knowing how alcohol affects a restricted population. And we can extrapolate---a neutral result in this study population would suggest alcohol is harmful to the average person.

You might also argue that it's ethically *required* to exclude people who are at higher risk for being harmed by alcohol. I don't really agree, but I'd imagine many people would.

**The premise of the study is flawed: Recent evidence says alcohol is harmful to cardiovascular health.**

This was brought up by the extra reviewers brought in to check the scientific merit of the study for the big NSF investigation. Some recent research suggests that alcohol could be *bad* for cardiovascular health. One strategy is "Mendelian randomization": The ADH1B gene (which [we've talked about before](https://dynomight.net/alcohol/#some-east-asians-struggle-with-alcohol)) makes it hard to metabolize alcohol. People who have it drink less. If you assume that gene is random in the population and that it's *causing* reduced drinking, then you can treat it like a random assignment to drink less. [Holmes et al. (2014)](https://dx.doi.org/10.1136%2Fbmj.g4164) did this and found that carriers of ADH1B had better cardiovascular health by every measure. This suggests alcohol makes cardiovascular disease worse, not better. There's also a recent meta-analysis of observational studies by [Wood et al. (2018)](https://doi.org/10.1016/S0140-6736(18)30134-X) that suggests that even small amounts of alcohol hurt cardiovascular health.

I don't get this. Is the point that alcohol is *definitely* harmful? That's wrong, the research in the previous paragraph is great, but it isn't conclusive. Or is the point just that an RCT could fail to prove alcohol was helpful? Then... umm... isn't that the entire point of doing the RCT?

**The study would be misrepresented.**

Imagine that the trial was done and that it showed little overall effect on health. Sure, you might say, *you'll* remember that it used a special population and maybe didn't run long enough to catch cancer. Clever people *like you* will interpret this as meaning that alcohol is probably harmful to the average person.

But do you trust journalists to understand these subtleties and convey them to the general public? Or would we just end up with headlines like "Gold-standard trial shows that moderate alcohol consumption is safe"?

This worries me, but less than you might think. For one thing, don't most people *already* think moderate drinking is safe? The [CDC](https://www.cdc.gov/alcohol/fact-sheets/moderate-drinking.htm) just says not to drink more than 1-2 drinks a day. [Tyler Cowen](https://marginalrevolution.com/marginalrevolution/author/tyler-cowen)---the Internet's greatest teetotaler---often points out the massive harms of alcohol. Yet he's stated that he believes that by refusing to drink at all, he's sacrificing a small amount of health.

Put that aside, though. Let's make the logic more explicit: This is suggesting that because journalists might do something dumb, we should *not run a trial* that could give knowledge humanity has needed for generations.

Sure, I agree journalists might oversimplify things and confuse people. (Can anyone disagree given recent history?) I just don't think that we can live in fear. We have to believe that once the scientific community has found the truth, it will eventually make its way into public consciousness. The solution to bad journalism is better journalism, not scientists refusing to do research on anything that could be misinterpreted.

**It just looks bad.**

The final NIH report notes that the researchers do not have "equipoise". You could interpret this two ways. One, you might say the whole thing seems rotten and damn the logic of it. The other is that it looks bad *for the NIH*---that even if useful, it needs to be canceled to preserve trust in the institution. I understand this. But if that's the reason to cancel, it makes me sad.

## A defense of the main characters

When I first read about this trial blowing up, I was stupefied---how could everyone have been so shameless? What were they thinking?

Before criticizing people, it's good to try to imagine the strongest defense of their actions. So let me try to do that.

**The alcohol industry**

I mean, OK, this is an industry entirely devoted to selling an addictive substance that kills, by [WHO estimates](https://www.who.int/publications/i/item/9789241565639), three million people per year. Something like [75% of alcohol is sold to raging alcoholics](https://www.washingtonpost.com/news/wonk/wp/2014/09/25/think-you-drink-a-lot-this-chart-will-tell-you/). This isn't a nonprofit organic vegetable farm. But we live in a capitalist system. We expect companies to try to make money, and selling alcohol is *legal*. Let's not conflate this particular trial with general objections to the alcohol industry's existence.

Think about their perspective. The NIAAA *came to them* and said, "We think moderate alcohol consumption is good for you! You should fund a trial to prove this. Win-win for everyone!" The NIAAA sent fancy researchers from fancy places to present to them. Those researchers told them, "I, fancy person, am sure moderate drinking is good! Give me money to prove it!"

The alcohol industry was straightforward they wouldn't fund anything without knowing what would happen in the trial. The NIAAA could have given up at that point, but they bent the rules instead. The industry was worried, "Won't it look bad that we're funding this?" Again, they were told, "Nah, it's fine! There will be a firewall!"

They were told by well-credentialed people that they could make money and do good at the same time. Is it so terrible that they believed them?

**NIAAA staff**

You might criticize NIAAA staff for becoming convinced that moderate drinking was healthy, even though the science is inconclusive. That's bad, but if you criticize everyone who's wrong about stuff, you're not going to get much sleep.

You can also criticize them for stretching the rules and misleading the public. This is a more clear failing. But imagine you *knew* a study would be valuable, but there's some bureaucratic rule that prevents you from doing it. Wouldn't you be tempted to stretch the rules?

Think about the NIAAA staff who took "personal vacations" to visit Mukamal to help him write the original planning grant. When they did this, I bet they saw themselves as heroes. This is what you see in movies: There's a big problem in the world. People in power *know* there's a problem, but for institutional reasons, it's hard to fix. Most of the people in power are [blankfaces](https://www.scottaaronson.com/blog/?p=5675), more concerned with covering their asses than helping people. The heroes are the ones who are willing to bend the rules to solve the problem---even if that means taking on personal risks.

If you think that no one in government should bend any rules, then I bet you haven't interacted with the government much. Often, the rules were made by people so removed from what's actually happening that the abstractions in the rules don't even make sense.

Here's an example. Say you're a scientist and you want to send a grant to the National Science Foundation (NSF). According to The Rules, you will propose a detailed plan of *future* work. In some (more theoretical) fields this is absurd: You have to do half the work in order to write that plan! And in other (less theoretical) fields, your grant will be reviewed by other scientists who will expect to see "preliminary work" to show your idea has promise. This leads to a funny situation where people do much of the research and then "propose" it afterward.

Everyone involved knows that this is happening! The grant reviewers aren't fooled. The people at NSF aren't fooled. (Though if they've been around for a while, they might not notice the doublethink anymore.) When Congress set up the NSF, they had a mental model of how research works. When that model doesn't fit, people do the best thing they can: They collectively follow a parallel set of slightly different rules while simultaneously going through the motions of the rules as written. Congress didn't *mean* to set up a system like this. Bending the rules allows their spirit to be followed as closely as possible.

At the NIAAA, The Rules say that you can't solicit grants from industry. But what exactly is "soliciting"? You might imagine there's some oracle somewhere ready to lend definitive answers, but I doubt it. Instead, what you probably see is some people doing things that are a *little* like soliciting, and it's fine. Other people do things that look slightly more like soliciting, and again it's fine. Eventually, someone pushes things slightly too far (or is just unlucky) and gets into trouble. The rules get clarified a bit then, but without acknowledging the institutional incentives that made everyone bend the rules in the first place. The person who got in trouble probably feels like a duck shot out of a flock.

So that's what I guess happened at the NIAAA. The staffers are used to bending the rules because that's what everyone does all the time because it's the only way to do anything. They think that the alcohol study would be beneficial, and go for it, and over time things sort of spiral out of control.

**Mukamal**

There are lots of quotes from Mukamal where he appears to be promising to deliver a positive result. At first glance, these might look like red flags, but I don't think they're as bad as they seem.

For one thing, Mukamal didn't start claiming alcohol was safe as a cynical ploy to get his hands on grant money. He had been publishing on the health effects of alcohol for years. There is no reason to doubt that he sincerely believed that moderate drinking had cardiovascular and diabetes benefits. (And he may well be correct!)

Can Mukamal be trusted? We can look at his track record. In 2007, he was first author on a [paper](https://doi.org/10.1016/j.ahj.2007.07.008) that randomly assigned patients to consume black tea or not. They looked at tons of different biomarkers and found that the tea did... basically nothing. This is the kind of case where it would be easy to p-hack your way to force some conclusion, but they straightforwardly state they found no evidence.

So I don't think these quotes represent a promise to falsify data but rather his confidence for what the study really would show when honestly performed.

Then there's the lying. Mukamal said there was *no communication* with industry and that he had *no idea* industry funding was even involved. Lying is bad, but still: When Mukamal was describing a "firewall" between industry and research, he was probably thinking of a firewall that started existing sometime after industry committed to funding the study. As far as we know, such a firewall *did actually exist*: Mukamal wrote the final study plan without (further) interference from industry, and the trial would have run without any industry contact.

Would this "late firewall" have meant anything? Maybe so! The biggest question is if industry would have had an opportunity to bury the results if they didn't look good. Maybe the firewall really would have stopped that.

So why did he hide the earlier meetings? Likely, Mukamal felt the public couldn't handle it. Take a look at the first [New York Times](https://www.nytimes.com/2017/07/03/well/eat/alcohol-national-institutes-of-health-clinical-trial.html) story on the subject. It is dripping with implications that the study is totally compromised when the only thing known (at the time) was that industry had funded things. It's understandable that Mukamal might have felt that the media was out to get him.

So my guess is that Mukamal was basically a well-intentioned researcher who happened to have pro-alcohol views. He took an opportunity to try to prove his pet theory, and then kind of fell down a slippery slope where he was making gradually larger and larger ethical compromises in pursuit of a goal that he thought was worthy.

## Rage

Having written that defense, I'd now like to explain why it's wrong and I'm furious about every aspect of this story.

First, we can only compensate for biases if we know about them. I'm open to industry-funded research. I don't *necessarily* mind a lead researcher who was chosen because they believe what industry likes. I can even live with industry having influence on the study design. I stubbornly hold all this even when the study has a goal of proving it's safe to use humanity's [most harmful drug](https://www.economist.com/graphic-detail/2019/06/25/what-is-the-most-dangerous-drug).

But my (possibly delusional) open-mindedness is based on the idea that it's possible to compensate for the biases these issues create. That's not possible if we don't know about them. If you think research still has value despite these issues, fine, but you need to make that argument openly, not pretend the issues don't exist.

Second, the firewall was fake. Say you're OK with a "late firewall" where there's tons of contact with industry early on, but no influence after the trial starts. This didn't happen. How do I know? Well, did you notice the part where Anheuser-Busch pulled its funding? Having the power to shut down the entire trial whenever you want qualifies as *influence*.

Third, slippery slopes aren't much of an excuse. Yes, we all face them, but that's why it's important to have principles---lines you won't cross. If you haven't run into one of those lines before you start lying to the New York Times, something is wrong.

Fourth, many people are complicit in silence. Maybe the alcohol industry really didn't think anything underhanded was happening. Well, they knew on July 7, 2017, when the first New York Times [story](https://www.nytimes.com/2017/07/03/well/eat/alcohol-national-institutes-of-health-clinical-trial.html) came out, including untrue or misleading statements from Mukamal and the NIAAA. They had months to correct the record, but they did nothing. The same is true for many of the other researchers involved.

Fifth, the general idea of industry funding with a firewall could be tremendously valuable but was tarnished by everyone here. Take nutritional supplements. Every time someone actually checks, we find out what's in them bears little resemblance to what's on the label (e.g. [melatonin off by a factor of 10](https://dx.doi.org/10.5664%2Fjcsm.6434), or ["ginkgo biloba extract" containing *zero* ginko biloba](https://dx.doi.org/10.5664%2Fjcsm.6434) or [tons of supplements containing heavy metals](https://doi.org/10.1371/journal.pone.0049676).) Some rare companies publish lab tests, but these always seem to be a test of some batch from two years ago by an unknown lab with no reputation who only tests three things and labels them "within spec".

In principle, firewalled research could be the solution. Supplement companies could pay to have tests done by independent researchers. Consumers would have a quality signal for what products to trust, and the companies that make good stuff would make more money. Everyone would win (except the people selling crap products). 

This trial has discredited this idea. Obviously, I blame the main characters, but the media is also part of this. Take the first [New York Times article](https://www.nytimes.com/2017/07/03/well/eat/alcohol-national-institutes-of-health-clinical-trial.html) again. Remember that when this was written, the firewall was valid, as far as anyone knew. But the article is almost an editorial disguised as journalism. Besides mentioning that the study exists and is funded by industry (which is totally legit) it's largely a collection of whatever random suspicious connections they could dig up between anyone even vaguely connected to the study and the alcohol industry. There are also quotes about how industry funding skews research, but it doesn't address that *that's why* there was supposed to be a firewall.

Obviously, I'm glad the New York Times followed up on this story and revealed holes in the firewall. I just wish there was a more nuanced tone that engaged with the premise that the problems with industry funding are possible to overcome, at least in principle.

Sixth, in the final review, the NIH made no attempt at cost/benefit analysis. Their final report is a fair summary of the problems with the trial. But it doesn't consider the information that was lost by cancellation, or the fact that there was little cost to taxpayers. (Though Collins' [letter to Senator Grassley](/img/alcohol-trial/grassley-response.pdf) reveals the NIH did pay around $4 million out of pocket.) Could a different principal investigator be put in charge? Could the study design be modified to address the concerns? Could the monitoring bodies have been strengthened so people could trust the results? Maybe the trial was unsalvageable, but it's telling that the NIH didn't bother to make that argument.

Finally, why have there been so few consequences? [Collins says](grassley-response.pdf) that "three individuals are no longer employed" at the NIH, and they made process changes to avoid similar problems in the future.

That's something, but what about the researchers? To their credit, Harvard and Beth Israel did do an investigation of Mukamal, which led to him formally apologizing and them creating safeguards to make sure no future employees would do anything similar.

Hahahaha, no. Here's what actually happened:

1. Mukamal stated, "We stand fully and forcefully behind the scientific integrity” and “Every design consideration was carefully and deliberately vetted with no input or direction whatsoever from private sponsors.” (Yes, these are real quotes from [*after* the study was canceled](https://doi.org/10.1136/bmj.k2689).)
2. As far as we know, there were no investigations by Harvard, Beth Israel, or any of the other researchers' institutions. No one faced any penalty of any kind.
3. In 2020, in what might be the most brazen display of academic shamelessness in history, the researchers published a [paper on how awesome the study would have been](https://doi.org/10.1177/2047487320912376). Here's a quote from that paper's "sponsorship" section:

> The Foundation for the National Institutes of Health (FNIH) supported the trial financially and managed contact between public and private organizations on behalf of NIH. The funds provided by FNIH for this project were contributed to FNIH by the brewing and distilling industries following contract negotiations that established an intellectual and financial firewall between MACH15 investigators and private contributors. The corporations providing support agreed to have, and had, no contact with trial investigators about any aspect of the study **after their commitment of funding**, and they agreed to receive no data or updates until they became publicly available. Ultimately, however, the most important safeguard for impartiality lies in the execution of a rigorous, transparent protocol following independent, expert peer review, and in the conduct of the statistical analyses as described in the protocol.

Emphasis mine. You can't make this stuff up.
