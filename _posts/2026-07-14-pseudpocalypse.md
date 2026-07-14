---
layout: post
title: "Pseudpocalypse"
image: /img/pseudpocalypse/the_beach_at_villerville.jpg
tags: [math, writing, effort]
description: "Here’s a conjecture: If you put any significant amount of text on the internet under different names, those identities can be linked using only the text itself."
excerpt: ""
permalink: /pseudpocalypse/
#seo:
# date_modified: 2025-11-21
# last_modified_at: 2025-11-21
comment:
substack: "https://dynomight.substack.com/p/pseudpocalypse"
lemmy: "https://lemmy.world/post/49440260"
# head: ""

---

Here's a conjecture: If you put any significant amount of text on the internet under different names, those identities can be linked using only the text itself. This is possible (I conject) because of the statistical "fingerprint" you leave in everything you write.

Imagine a website where you can paste in some brand-new text someone just wrote. In return, the website provides links to all the text that writer has ever published under any name. It's not perfect, but it's pretty good. As far as I know, no such website exists—at least not on the public internet. But I suspect it's possible and will soon become easy. This will pose some difficulty for pseudonymous blogging.

*Note*: I wrote most of this essay in mid-2025, after which I idiotically sat on it for a year tinkering with theorem statements that none of you will read.[^1] In the meantime, LLMs have gotten much better at guessing authors from text. (Given the first 1000 words of a draft of this post, Claude 4.8 knows it's me.) Still, I think we're just getting started. I expect to see increasingly obscure writers identified from increasingly small bits of text. I expect that this work even when people are writing in a different register or about unrelated subjects. And I expect that everything I've ever written under any pseudonym will soon be linked to my genuine-nym.[^2]

A stronger conjecture is that we're heading towards a sort of generalized pseudpocalypse. Perhaps, in the future, if you interact with the world through essentially *any* high-bandwidth channel, then you identify yourself. Say you wear a mask in public and only speak by sub-vocalizing into a voice changer. That's fine, you'll still be identified using your body shape, gait, or chemical signature. Or say you don't like your car being tracked everywhere, so you stop carrying a phone and you somehow convince lawmakers to ban license plates. No problem, your car will still be tracked using tiny scratches or unique pinging sounds from the engine. Or say you don't like being tracked on the internet, so you lock down your browser profile, buy stuff only with Monero, and connect through a chain of three VPNs. That's OK. You'll still be identified through how you wiggle your finger as you scroll down the page. We're all just too unique, and the information theoretic limit is coming for us.

## Starting bits

Let's start from first principles. Imagine that at birth, everyone is assigned a random binary string. Whenever you post anything on the internet, you're required to sign it with that string. If the strings are very short, like `0110`, then lots of other people will have the same one as you. But if the strings are very long, then yours would almost certainly be unique and it would be trivial to link all your pseudonyms.

Where's the transition point? If you only know that the author is currently alive and living somewhere in the Anglosphere, it's around 29 bits. That's because if there are K digits, then there are 2ᴷ possible binary strings, and if K = 28.86, then 2ᴷ ≈ 490,000,000 is the number of currently-alive Anglosphere-dwellers. If the strings have fewer than 29 bits, then someone else will probably share your string. If they have more than 29 bits, then your string is probably unique.

We don't (yet?) have to sign the things we write with immutable government-issued strings. But the way you write still provides lots of clues about you by way of your tone, personality, word choice, and so on.

Theoretically speaking, I think it *has* to be possible to link the identities of anyone who writes enough. Imagine again that everyone is assigned a random binary string at birth, but instead of you needing to sign the stuff you write with your string, each time you write a word, there's some chance that a random bit from your string is revealed and added as a signature to your message. For example, maybe a signature of `bit[129]=1` is added, indicating that your string at position 129 has value 1.

Think of your string as representing all your writing style quirks, and a bit being revealed as representing when you write something that reveals a preference. For example, maybe bit 18 indicates if you prefer to write your em-dashes with hideous spaces — like this — or without spaces—like this. If you use an em-dash, that bit is revealed.

So imagine you've written a lot under Pseudonym A, enough that the full bit-string has been revealed. Maybe it's this:

```
Pseudonym A: 
110000001111001101110000100001
010100100101011110111001101000
100111110010101001101010111010
```

Now say you start writing under Pseudonym B. Initially, none of the bits will be known:

```
Pseudonym B: 
??????????????????????????????
??????????????????????????????
??????????????????????????????
```

But slowly, you'll start to leak a few bits:

```
Pseudonym B:
?????00???1????1????????1??0??
?????01??1?????????11????01???
???1??????1???10??????????????
```

And eventually you'll leak a lot of bits:

```
Pseudonym B:
???0?00?1?11??110??1????10?0??
?10?001?0101?11???11100?101???
???11?1??010??10?1?01??011????
```

Now think about this from the perspective of an "attacker" who wants to know if A and B are the same person. Let's assume they've *only* seen the above bits, and have no information about anyone else. Then here's what the attacker knows:

1. A and B have revealed K overlapping bits, which all match.
2. Different people have a 50% chance of matching on any given revealed bit.
3. Non-different people have a 100% chance of matching on any given revealed bit.
4. There are 490,000,000 people.

Intuitively, if K was 5, then the fact that all bits match wouldn't prove much, since with 490 million people, lots of people would match on those bits by chance. But if K was 70, it's extremely unlikely that two different people would share all of them, even with such a gigantic pool to start with. It turns out that if there are N other people with random bits, and you pick K of your bits, the probability that *someone* exists who matches all of them is 1 - (1-2⁻ᴷ)ᴺ. When N is 490 million, that looks like this:

![](/img/pseudpocalypse/one_sided_thought_experiment.svg)

Look at that, 29 appears again. (Isn't math wonderful?) In general, the transition happens around whatever number of bits K makes 2ᴷ ≈ N, namely K = log₂(N).

If you reveal significantly fewer than 29 bits under pseudonym B, then it's almost guaranteed that there's someone else out there who matches all of them. But if you reveal significantly more than 29 bits, then there's almost no chance that anyone else exists who matches all of them. So the attacker essentially knows that A and B are the same person. And I stress again: They know that without needing to see anything from the other 490 million people.

Of course, we don't literally leak bits of immutable feature strings as we write. But you can make the model more realistic, and the same issue persists. If you want to reflect that text only provides noisy information about the writer, then you can add noise to the bits before they're revealed. If you want to reflect that some writing styles are more common than others, then you can make the distribution over bit strings non-uniform. If you want to reflect that certain quirks are more obvious than others, you can give different bits different probabilities of being revealed. All these make the math more complicated.  But they don't change the basic conclusion: If your writing style contains at least 29 bits of information, and you do enough writing, you're done.

That's my argument that pseudpocalypse is possible. But I don't just want to claim that it *could* happen, eventually. I think it is *likely* to happen, soon, and that the amount of text you need to reveal isn't very large. To make that argument, we need to get specific: What features do people have that are reflected in their writing? How many bits of information do those features contain? How accurately can those bits be guessed from written text?

*Note*: To avoid this turning into a giant information theory lecture, I'll mostly use words like "bit" and "information" without being 100% fully precise about what they mean. I'm doing that because I expect that most people reading this aren't definition-of-bit fetishists, and anyway being hyper-technical would obscure the big picture. If you're an information theory enthusiast and/or skeptical that I know what I'm doing, I refer you to the Section For Skeptical Information Theory Enthusiasts, below. Until then, use your intuition and have faith.

## Feature space

Say you knew nothing about me other than that I wrote the above words. And say you had to guess my age or religion or occupation. You could *guess*, right? It wouldn't be perfect, but you'd do much better than you would *without* being able to read those words. Thus, somehow, those words contain information about my demographic characteristics. So I tried to make a list of similar things that you could plausibly guess from text at least somewhat better then chance. Here's what I came up with:

* Age
* Education
* Ethnicity
* Family status
* Income
* Marital status
* Mental health
* Native language
* Occupation
* Physical health
* Political leanings
* Region
* Religious affiliation
* Sex

In the same spirit, if you only read the above words, could you guess how extroverted or conscientious I am? Again, not perfectly. (When I meet people who read this blog, they usually seem surprised I can survive direct sunlight.) But still, I'm sure you'd do OK. So, again, these words contain information about my personality.

What features does personality have? The [HEXACO model](https://en.wikipedia.org/wiki/HEXACO_model_of_personality_structure) lists six, namely honesty-humility, emotionality, extraversion, agreeableness, conscientiousness, and openness to experience. I suspect those can all be guessed with reasonable accuracy from a long-enough writing sample. But could you guess more? For each of those six factors, the HEXACO model lists four "facets". In the abstract, trying to guess 6 × 4 = 24 different personality features from text sounds ludicrous, but just look at them:

* Honesty-humility
	* Sincerity
	* Fairness
	* Greed avoidance
	* Modesty
* Emotionality
	* Fearfulness
	* Anxiety
	* Dependence
	* Sentimentality
* Extraversion
	* Social self-esteem
	* Social boldness
	* Sociability
	* Liveliness
* Agreeableness
	* Forgivingness
	* Gentleness
	* Flexibility
	* Patience
* Conscientiousness
	* Organization
	* Diligence
	* Perfectionism
	* Prudence
* Openness to experience
	* Aesthetic appreciation
	* Inquisitiveness
	* Creativity
	* Unconventionality

If you think about specific people, I think you can convince yourself that these 24 represent real things, and that it's plausible to guess them from text. (Your favorite existential angst + science blogger, for example, might score lower on "modesty" than the other honesty-humility facets.) The different sub-factors are surely correlated, but not perfectly correlated.

Of course, the biggest thing you learn from people's writing is *how they write*. Do they pointlessly split infinitives? Do they use hyphen-connected words? Do they, incorrectly, position their adverbial clauses?

The idea of attributing authorship using writing style features goes back to at least 1440, when Lorenzo Valla demonstrated that the [Donation of Constantine](https://en.wikipedia.org/wiki/Donation_of_Constantine)—in which Emperor Constantine supposedly donated the Roman Empire to the Catholic Church—used a vernacular that came from 400 years after Constantine's death and was therefore a forgery. In 1851, Augustus De Morgan observed that average word length tends to be stable for the same author. The first "modern" attempt seemingly came in 1964, when Mosteller and Wallace published [*Inference in an Authorship Problem*](https://doi.org/10.2307/2283270):

> This study [attempts] to solve the authorship question of *The Federalist* papers; […]
>
> Word counts are the variables used for discrimination. Since the topic written about heavily influences the rate with which a word is used, care in selection of words is necessary. The filler words of the language such as *an*, *of*, and *upon*, and, more generally, articles, preposition, and conjunctions provide fairly stable rates, whereas more meaningful words like *war*, *executive*, and *legislature* do not.
> 
> After an investigation of the distribution of these counts, the authors execute an analysis […] based on Bayesian methods. The conclusions about the authorship problem are that Madison rather than Hamilton wrote all 12 of the disputed papers.

Get that? The idea is that your usage of the word *war* depends mostly on if you happen to be talking about war. But your usage of *upon* mostly depends mostly on how much you like the word *upon*. To demonstrate this, they took 48 papers written by Hamilton and 50 by Madison and made this table of how many times they used *by*, *from*, and *to*:

![](/img/pseudpocalypse/mosteller.png)

Madison liked *by*. Hamilton was more a *to* man. Using these kinds of statistics, they concluded that the disputed Federalist papers must have been written by Madison.

So I did some research looking for other writing style features that are believed to be stable when people write about different subjects. I found that there are a lot. There were so many that I struggle to even organize them into meaningful groups:

**Low-level frequencies:**

* Word lengths
* Sentence lengths
* Paragraph lengths
* Punctuation frequencies (commas, colons, dashes, parentheses)
* Function word frequencies (*the*, *of*, *and*, *to*)
* Adverb frequencies
	* Intensifiers (*very*, *really*, *quite*, *pretty*, *so*)
	* Evidential markers (*apparently*, *evidently*, *obviously*)
	* Downtoners (*somewhat*, *fairly*, *rather*)
* Pronoun usage
	* Overall preferences (*I*/*we* vs. *you* vs. *he*/*she*/*they*)
	* Third-person singular preferences (*he*, *she*, *he or she*, *they*, *one*)
* Modal verbs (*can*, *could*, *might*, *must*, *should*, *will*, *would*) 
* Hedges (*perhaps*, *maybe*, *possibly*, *probably*)
* Conjunctions (*and*,  *but*,  *yet*, *so*)
* Known stable ratios (*the*/*a*, *this*/*that*, *these*/*those*, *I*/*me*/*my*)
* Character N-grams (3-grams and 4-grams)
* Word N-grams (often 3-grams)

**Lexical features:**

* Vocabulary size
* Lexical diversity / type-token ratio (Number of distinct words divided by number of words.)
* Frequencies of rare words
* Semantic density
* Discourse marker positions, combinations (*So*, *anyway*, *so anyway*)
* Use of abbreviations and acronyms
* Preference for latinate vs. germanic words (*The* *majestic* *creature* *traversed* *the* *terrain* vs. *the* *mighty* *beast* *strode* *across* *the* *land*.)

**Syntactic features:**

* Syntactic complexity
	* Subordination index
	* Average parse tree depth
* Use of passive voice.
* Nominalization (*She was shocked I ate the pizza* vs. *My pizza consumption shocked her*)
* Verb tense and aspect (*I walk* vs *I walked* vs *I was walking* vs *I have walked*)
* Sentence structure preferences:
	* Branching preferences (Cursed *everyone had a good time when Alice taught some cool dogs I met and brought to dinner to juggle* vs. clumsy-but-readable *I met some dogs and they were cool and I took them to dinner and Alice taught them to juggle and and everyone had a good time*.)
	* Adverbial clause positioning (*Suddenly I was hungry* vs. *I was, suddenly, hungry* vs. *I was hungry, suddenly*)
	* Sentence-final weight (*Your plan won't work because of the dyslexic bears* vs. *Dyslexic bears mean your plan won't work.*)
* Polysyndeton (*I like dogs, cats, and ferrets* vs. *I like dogs and cats and ferrets*.)
* Repetition / breaking of syntactic structures.

**Style features:**

* Register / formality.
* Patterns in sentence length (long/short/long/short vs. long/long/short/short)
* Stressed syllable interval preferences (e.g. iambic vs. trochaic)

**Rule preference features:**

* Minor punctuation (*I laughed—you cried* vs. *I laughed — you cried*, "…" (three periods) vs. "…" an actual ellipsis)
* Capitalization. (Job titles, seasons, after a colon, mistakes)
* Apostrophes (*Steve Jobs' car* vs *Steve Jobs's car*, *1990's* vs *1990s*)
* Hyphenation (*a highly-stable feature* vs *a highly stable feature*)
* Oxford commas.
* Article omissions (*Local dog was petted.* vs. *A local dog was petted.*)
* Relative pronoun omissions (*the dog you petted* vs. *the dog that you petted*)
* *Who* vs. *whom*.
* Split infinitives (*To obsessively blog* vs. *to blog obsessively*)

**Idiosyncratic features:**

* Whitespace habits.
* Spelling errors (*loose* instead of *lose*)
* Grammar errors. (*Between you and I*)
* Consistent, unique typos
* Other consistent errors (repeated words, un-closed parentheses)

That's a lot. There are surely more. And these are all "shallow" features that humans came up with using our tiny little brains. I strongly suspect that there are many more "deep" features that could be found by looking for statistical patterns in a sufficiently large dataset. Many of those features might not even have a coherent English-language description. But they're still there, providing bits for those who seek them.

So we leak information about lots of different stuff when we write. But how much information? Is it possible to say how many words are needed to uniquely fingerprint someone?

No. To a first approximation, the answer is no. But to a second approximation, maybe? Within an order of magnitude? I'll try, but it's going to be hard.

## Demographic bits

How many bits of identifying information does text provide by way of demographic features like age and sex and so on?

At first glance, this seems a perilous question, as it depends on the number of categories you consider those things to have. Take sex. For pseudpocalypse purposes, your opinion about how sex should be defined or how many sexes exist is irrelevant. Finer categorizations always provide more information, and our de-pseudonymizing attacker friends will use that information if they can. However, going beyond two categories for sex makes little difference, because the additional categories will be hard to guess and even if you could, categories with low prevalence don't contribute much extra information.[^3] So, for us, two categories is the right answer.

And what about age? At first glance, converting age into a set of categories seems meaningless. If you code age by the millisecond, then there are 3.156 trillion categories for people born in the last 100 years. If you code age by the decade, there are only 10. Here, the thing to notice is that while you might be able to guess my decade of birth from how I write, you don't have a snowball's chance in hell of guessing the millisecond. (See what I did there? People born in certain decades are more likely to use expressions like *snowball's chance in hell*?[^4]) If we took age to have some crazy number of categories, we'd have to discount later to reflect the difficulty of guessing. My intuition is that it would be hard to guess age more accurately than around five years, so 20 categories seems reasonable.

Following this kind of logic, I chose a number of categories for each of the demographic variables, trying to hit the upper end of what could be guessed from text. (I'll provide the actual categories below.)

| Feature               | Number of categories |
| --------------------- | -------------------- |
| Age                   | 20                   |
| Education level       | 6                    |
| Ethnicity             | 6                    |
| Family status         | 2                    |
| Income                | 11                   |
| Marital status        | 3                    |
| Mental health         | 3                    |
| Native language       | 2                    |
| Occupation            | 23                   |
| Physical health       | 3                    |
| Political leanings    | 3                    |
| Region                | 23                   |
| Religious affiliation | 3                    |
| Sex                   | 2                    |

If each of the age bins were equally likely, then knowing what bin someone fell into would provide 4.32 bits of information, because 2ᴷ ≈ 20 when K = 4.32. Doing that same calculation for each feature gives the maximum amount of information they could contain.

| Feature               | Number of categories | Maximum bits |
| --------------------- | -------------------- | ------------ |
| Age                   | 20                   | 4.32         |
| Education level       | 6                    | 2.58         |
| Ethnicity             | 6                    | 2.58         |
| Family status         | 2                    | 1            |
| Income                | 11                   | 3.46         |
| Marital status        | 3                    | 1.58         |
| Mental health         | 3                    | 1.58         |
| Native language       | 2                    | 1            |
| Occupation            | 23                   | 4.52         |
| Physical health       | 3                    | 1.58         |
| Political leanings    | 3                    | 1.58         |
| Region                | 23                   | 4.52         |
| Religious affiliation | 3                    | 1.58         |
| Sex                   | 2                    | 1            |
| **Total**             |                      | 32.88        |

But there's a problem. There are more people aged 30-35 than there are people aged 90-95. So, even if you could guess those age bins perfectly, they'd provide less than 4.32 bits of information on average. However, it turns out that categories need to get pretty damned uneven before information content drops very much. A perfectly balanced 50/50 distribution provides 1 bit of information, but if you switch to a 60/40 distribution, you still get 0.971 bits, and you need to go almost to 90/10 before information content drops to 0.5 bits.[^5] The same basic thing is true when there are more than two categories.[^6]

So I went through all those features, rated them by how unevenly people are distributed, and tried to discount the bits accordingly. I've put the full details of what the original categories are and how I discounted them in a footnote.[^7]

| Feature               | Number of categories | Maximum bits | Estimated bits |
| --------------------- | -------------------- | ------------ | -------------- |
| Age                   | 20                   | 4.32         | 3.9            |
| Education level       | 6                    | 2.58         | 2.1            |
| Ethnicity             | 6                    | 2.58         | 1.7            |
| Family status         | 2                    | 1            | 0.8            |
| Income                | 11                   | 3.46         | 2.5            |
| Marital status        | 3                    | 1.58         | 1.2            |
| Mental health         | 3                    | 1.58         | 0.9            |
| Native language       | 2                    | 1            | 0.6            |
| Occupation            | 23                   | 4.52         | 4.0            |
| Physical health       | 3                    | 1.58         | 1.3            |
| Political leanings    | 3                    | 1.58         | 1.5            |
| Region                | 23                   | 4.52         | 3.5            |
| Religious affiliation | 3                    | 1.58         | 1.5            |
| Sex                   | 2                    | 1            | 1              |
| **Total**             |                      | 32.88        | 26.5           |

But there's another problem. Female 65 to 70 year-old Asians living in Scotland tend to have different {occupations, family statuses, religious affiliations} than 15 to 20 year-old Latinos living in Southeast Australia. That is, the above features are correlated. So as you look at more of them, they gradually become less surprising and thus contribute less information.

How much less? Answering that the right way would require us to estimate how likely someone is to fall into each of the 20 × 6 × 6 × 2 × 11  × 3 × 3 × 2 × 23 × 3 × 3 × 23 × 3 × 2 = 8,144,737,920 joint categories. That seems hard. But a not-completely-ridiculous approximation is that if a group of variables are all pairwise correlated at a level of ρ>0, then the total information might be reduced by a fraction of ρ.[^8]

So how correlated are those features? In the social sciences, a correlation of 0.5 is considered quite high. That's plausible for some pairs of variables, e.g. age vs. health or political leaning vs. religious affiliation. But many of those correlations are are probably quite weak, e.g. age vs. native language or region vs. sex vs. marital status.[^9]

Overall, my guess is that correlations reduce the total information by at least 10% but I doubt they reduce it by more than 60%. So I'd think the total information in the above features (if you could guess the categories perfectly) is somewhere between 10.6 and 23.9 bits. Let's take the average and call it 17.2 bits.

## Personality bits

What about personality features? Let's use the same same recipe we used for demographic features, but faster: To start, let's give each of the 24 personality features five bins, in deference to [dynomight personality notation](https://dynomight.net/in-defense-of-myers-briggs.html#:~:text=Behold). That would correspond to 24 × 2.32 = 55.68 bits total, because 2ᴷ ≈ 5 when K = 2.32.

Then we need to discount for correlations. The six main HEXACO personality factors are designed to be uncorrelated, but the different "facets" inside each factor are correlated (usually with a coefficient between 0.3 and 0.6). It seems reasonable to use an overall discount factor of 0.3 to reflect strong intra-factor correlations but weak inter-factor correlations. That suggests 39.0 bits overall.

## Style bits

And what about writing style features? How much information do they contain?

This seems hard. Some of the features, like character n-grams are actually themselves long lists of features. (Frequency of typing `aaa`, frequency of typing `aab`, etc.) However, many of those features contain little information, since almost everyone types `zqx`  around 0% of the time. And, of course, writing style features are correlated, since people who write `realise` instead of `realize` are less likely to put spaces around their em-dashes.

In absence of a better idea, I'm going to give one bit for each leaf node in the above list of style features. I think of this as giving each feature two bins, and then assuming that uneven distributions of features and correlations (which reduce information) are canceled out by the fact that many features deserve more than one bin and that there are probably more "deep" features that aren't listed (which increase information). This gives us the suspiciously round number of 50.0 bits.

## Guessing bits

If you believe the above numbers, then we have at least 17.2 + 39.0 + 50.0 = 106.2 bits of identifying information that we leave clues about when we write. That's a lot. If you could see all those features, it would be enough to identify people even on a planet with 93 million trillion trillion people.

But to argue that the pseudpocalypse is nigh, it's not enough to argue that those bits exist. We need to argue that they *can* and *will* be guessed from a *relatively small* amount of text.

So obviously we need to talk about nuclear weapons. In a nuclear detonation, many unstable atoms are created. These spontaneously decay into more-stable atoms, in the process emitting radiation. Some types of atoms are very eager to decay, meaning they release a lot of radiation but stop existing within a few weeks (iodine-131). Others are reluctant to decay, meaning they don't release as much radiation but they stick around for decades (strontium-90). Others stick around for millions of years, but they produce so little radiation that they're not a big problem (cesium-135).[^10] So, the residual radiation produced after a nuclear detonation is the sum of many different exponential curves, one for each isotope created during the detonation.

I suspect that identifying bits in text are sort of like that. Your level of formality and your average sentence length are revealed almost immediately. Your preference for latinate vs. germanic words takes a while to come through. And your social boldness and the fact that you live in Queensland rather than Southeast Australia are revealed very slowly, perhaps so slowly that it's effectively not revealed at all.

Right. So if you start with 106.2 bits, how many of those do you reveal after writing a given number of words?

I will answer that question through the noble method of making up numbers. But first, let's calibrate. You just read 4500 words written by me. How well could you guess my demographic and personality features? As a sanity check, I gave the above words to an LLM and asked it to guess. It did unnervingly well. It wasn't always right, but it usually was, and it did a great job of rating the confidence of the individual predictions.

I don't think there's any magical explanation for this. The fact is, if you look at the individual personality and demographic features, guessing them just isn't that hard. So I'm sure you could do just as well. And given enough time, I'm pretty sure you'd do even better for writing style features.

Even so, you're probably bad at it. Take the example of [GeoGuessr](https://en.wikipedia.org/wiki/GeoGuessr), where people guess a location in the world from a random photo. Random people are sort of OK, but if you pick the top natural talents and have them practice obsessively, they're *really* good. I don't think LLMs are particularly good at guessing features from text, either. They weren't trained for it. It's just an emergent property of their general intelligence. The information-theoretic limit is surely much higher.

So here's a very rough cut: After 4500 words, I'd think it's possible to guess around:

* 60% of the demographic features
* 70% of the personality features
* 80% writing style features

If we model each of those with a separate exponential, and start them at 17.2 / 39.0 / 50.0 bits, then the total number of identifying bits that remain hidden after writing a given number of words is as plotted here:[^11]

![](/img/pseudpocalypse/decay_plot_10k.svg)

*Et voilà*, pseudonymity is compromised when you leak 29 bits, which happens after 1071 words.

## Seriously?

Of course not. The above figure stands on a creaking tower of tenuous assumptions. I've gone through the details of deriving that curve not because you should trust it, but because I think seeing the calculations makes the following points hard to argue with:

* You have far more than 29 bits of identifying information that you leak into your writing.
* Some of those bits take a long time to get revealed, but others are revealed pretty quickly.
* There are enough "fast leaking bits" that you can be identified from a writing sample that's "pretty small".

I've made lots of debatable choices in terms of choosing features, assigning numbers of categories, estimating distributions across those categories, discounting for correlations, and guessing how many bins can be guessed. Those choices are all individually suspect. But the above points are supported by a pretty wide margin of error. You can make different choices, but it seems very hard to avoid concluding that the above three points are true.[^12]

## How would this work?

You might be wondering why I'm using so many made-up numbers. After all, there's a whole field devoted to identifying authors from text, usually called ["stylometry"](https://en.wikipedia.org/wiki/Stylometry) or "authorship attribution". They have research papers and [competitions](https://pan.webis.de/) and all that. However, as best I can tell, state of the art [published results](https://doi.org/10.1109/ACCESS.2024.3407673) look something like this:

1. Take 50 people.
2. Get a few hundred writing samples from each author, each 1000-2000 words long.
3. Now, take a new writing sample from one of those authors.
4. Do some standard machine learning stuff.
5. Hey look, the author can be identified with ~95% accuracy!

That sounds OK, but that's only identifying people against a pool of ~50 authors. For my claim to be true, similar accuracy would have to be possible with 490 million people. That's seven orders of magnitude more.

The thing is, the methods those papers are using are extremely weak. All the above math assumes that you're operating at the "information-theoretic limit", making perfect use of *all* available information. If you want to get close to that, we now have some idea how to do it: You apply the "modern" machine learning recipe of gigantic dataset + gigantic neural network + gigantic fortune spent on GPUs. My guess is that for us, that would require something on the order of "all the words ever written" + "tens of billions of parameters" + "tens of millions of dollars". I couldn't find a single paper that came remotely close to attempting that.

So I don't think those papers tell us much, for the same reason that a 3rd-order Markov model trained on a few books doesn't tell us much about how good computers could be at writing text. LLMs have shown that if you use the above recipe, then computers can get close to the information-theoretic limit for generating text.[^13] So, I suspect that an LLM-level effort could achieve the same thing for identifying authors.

You might also wonder: Why am I talking about this as some possible future technology? Isn't that technology just LLMs?

I suspect the technology will be quite LLM-like in how it models human language. But current general-purpose LLMs aren't trained for this task. They're good at it "by accident". So, just like specialized chess AIs can crush LLMs at chess, I suspect specialized stylometry methods could crush general-purpose LLMs at stylometry. It's just that those specialized stylometry methods don't seem to exist yet, or at least aren't public.[^14] So we shouldn't imagine that current LLMs are anything close to what's possible, even if you assume that generic LLM progress stopped today.[^15]

## Countermeasures

If this is all true, what could be done about it?

The most obvious "countermeasure" would be to get used to it. I mean, imagine that we *did* live in a world in which everyone literally had to sign everything they wrote with a unique immutable string. What would happen? I'd expect a mixture of:

1. People become more comfortable with their "full selves" being public, with less compartmentalization.
2. People pull back from communicating in public channels, relying more on group chats and the like.
3. People self-censor.

There are strong historical analogies here, since over the past 20 years many governments and tech companies have in fact decreed that people must sign the things they write with their real names.

The effects seem to vary quite a lot based on the ambient culture and political system. Overall, my impression is that people are already much more comfortable with the idea that their work colleagues might read their dating profile or learn that they go to furry conventions. I'm optimistic that culture will continue to adapt to respect the fact that we all encompass multitudes. This seems healthy.

Some effects seem clearly positive. Self-censoring is not necessarily bad. For example, on the margin, real-names surely stop some teenagers from engaging in cyber-bullying. On the other hand, were you ever a teenager? I'm pretty sure that for anyone who is "different", having those differences broadcast to the world creates a much larger "bullying surface area". So the effects are mixed. And adults aren't as different from teenagers as we might like to think.

Twenty years ago, I might have predicted that real names would discourage people from expressing controversial political ideas online. Superficially, that seems completely wrong. At least in the West, lots of people are *very* happy to express minority political views, and if you disagree at all, then you can go to hell. But I also tend to think this hides a lot of self-censorship, where most people don't want engage in political mortal combat and so are cowed by a feisty minority. And, obviously, people in certain countries know that it's unwise to criticize the Party. So, getting used to it seems like an imperfect solution at best.

Another countermeasure would be to not build this technology, or not make it widely available. In the short term, this seems plausible. As far as I can tell, it's been possible for years for a modestly-funded group to build a phone app that would identify most people on the street from a photo. And yet, almost no one reading this has access to such an app. If general-purpose LLMs continue to get better at stylometry, it seems entirely possible that AI companies might decide it's a safety issue and train their AIs to refuse to do it.[^16] This could work for a while.

But if the technology is possible, it seems certain that governments will build it and use it. They might try to keep it out of the hands of normal people. Certain governments might restrict their own use. My privacy-minded allies always seem very jaded, but it wouldn't surprise me at all if the Supreme Court declared that a warrant was needed before the FBI could de-pseudonymize a U.S. citizen. But when/if that technology becomes sufficiently cheap, it seems like it would be very difficult to keep it out of the hands of normal people and/or bad actors. My guess is that it's possible to create a program that's a few hundred gigabytes large and can run (slowly) on most modern laptops. If that program is made public, it would be hard to put the genie back in the bottle.

There are also technological countermeasures. Most obviously, you could run your writing through a "filter" to try to remove identifying bits, e.g. by asking an LLM to rewrite it. It's hard to be sure how well this would work, since we don't have accurate estimates of how many bits you're starting with or how many bits this would remove. But I'd guess this would be pretty effective if done carefully. The reason is that the number of identifying bits you leave in writing probably isn't *that* large, relative to the number needed to identify you. If you "homogenize" your writing to remove all style and personality, you should be able to remove most of those bits. Theoretically, you'll still leak some information. But I'd think this would substantially increase the amount you could write while remaining pseudonymous.[^17]

But after thinking about it, this makes me sad. Effectively, this countermeasure would preserve pseudonymity by taking writing and destroying all traces of humanity. It seems like this would work well for the "bad" uses of pseudonymity, like cyber-bullying or coordinated violence, but it wouldn't work at all for the "good" uses, like for example someone who likes to write pseudonymously because they feel like it allows them to be more honest and vulnerable and more fully themselves, damn it.

## Generalized pseudpocalypse

Maybe this isn't just true for writing. Maybe it's just a feature of our universe that if you interact with the world in any significant way, then you leave traces that make it possible to identify you.

* If you walk around in public, then you can likely be identified by your face, your gait, your voice, your DNA, your retinas, or your literal fingerprints.

* Or say you use the internet. Even if you lock down your browser fingerprint and hide your IP address using a VPN or Tor, a sufficiently powerful adversary could still identify you by analyzing global packet flow.

* Or say you use *any* phone or computer. You might be identified through keystroke dynamics or the way you jiggle your finger or mouse.

* Say you buy food at the grocery store, but you pay with cash and somehow shop at a grocery store with no cameras. If you buy more than a handful of items, I'd bet you can still be identified through the patterns in the stuff you buy.

* (Incidentally, did you ever notice that cash has serial numbers on it? And did you know that more and more ATMs are starting to track those numbers?)

* Or say you don't like your car being tracked, so you stop carrying a phone and somehow get lawmakers to outlaw license plates. Still, your car surely has a few small unique scratches, and the engine probably doesn't sound exactly the same as other cars, even from the same model and year. So if there's any high-resolution video or audio, that's still enough to track you.

* Say you plug your headphones into a charging station at the airport. Your headphones have eccentricities in their analog charging circuits. If someone really wanted to, they could track that.

* Or say you use electricity. Given high-resolution power-usage data, what can be said about how many people live with you? And what devices you're using? Probably a lot?

* Or say you use a toilet. Many places already test sewage and know, at a population level, what drugs people are using and how prevalent various diseases are. Imagine this was upgraded to test many places in the system, with high temporal resolution, possibly correlated with flow measurements from individual houses. That would be exciting.

* Or say you are a country and you have submarines. Can they be detected by adversaries using distributed acoustic sensing? What about satellite-based synthetic aperture radar? Gravity Gradiometers? Quantum magnetometry? 

As far as I can tell, the general trend is that without countermeasures, almost everything can be identified. Countermeasures can make it harder, but they're costly, and on the whole, the arms race seems to favor the identifier, not the person who doesn't want to be identified.

I stress: This is not all bad. The goodness / badness of a generalized pseudpocalypse depends on how society is structured. After all, the foundation of civilization is finding ways for people to make deals, and arguably less privacy makes that easier. The degree that we live in a [vulnerable world](https://en.wikipedia.org/wiki/Vulnerable_world_hypothesis) where it's easy to create civilization-destroying technologies, perhaps we're very lucky to find ourselves in a non-private world. Still, I do worry that privacy has long provided a kind of "slack" from laws and norms. Historically, that slack has limited the power of institutions to enforce their rules. If privacy is going away, we need to think about how to preserve slack, particularly when institutions don't want to.

## Appendix: Section for skeptical information theory enthusiasts

Above, I tried to estimate the number of bits of identifying information in writing. But what is a "bit"? In general, if **x** is a discrete random variable, then the [Shannon entropy](https://en.wikipedia.org/wiki/Entropy_(information_theory)) of **x** in bits is **H(x) = ∑ₓ p(x) log₂(1/p(x))**, where the sum is over all the values **x** can take. This is always bounded between zero and the logarithm of the number of values **x** can take. 

That's fine, but "writing style" is not a discrete variable with a discrete number of categories. So how can I estimate the entropy of writing style? The short answer is that I can't. What I've actually estimated above is the *mutual information* between writing and writing style.

Let **s** be a random variable representing writing style. Think of this as some sort of high dimensional continuous vector representing all the quirks of how different people write. And let **x** be a writing sample of some length. This is discrete because we can represent writing on digital computers. Then what I've estimated above is the mutual information **I(x;s) = H(x) - H(x\|s)**, where **H(x\|s)** is the conditional entropy of **x** given **s**. This can be measured in bits because both **H(x)** and **H(x\|s)** can be measured in bits. So that's what my estimate above really says: **I(x;s) ≈ 106.2 bits**.

Now, you still might be skeptical. Above, I've implicitly assumed something like the following was true:

> It's possible to identify one person out of N possibilities with low accuracy if and only if the mutual information between identifying features and writing is at least **log₂(N)** bits.

That's how I justified pseudonymity being compromised around 29 bits. But is it really true? Strictly speaking, no. Actually, even more strictly speaking, it's "not even untrue" because it's not precise enough to be true or false. But as far as I can tell, basically any precise version of that statement is false. However, it's possible to find versions of that statement that *are* true, provided you add some extra not-too-crazy assumptions.

To start, let's consider an extremely simple model of information leakage.

**Theorem.** Suppose the world consists of you plus **N** other people, and suppose each person has a binary identity string, drawn at uniform from the distribution over **M**-bit binary strings. All these strings are known to the attacker. Suppose you pick some subset of **K** bits and reveal them. Then the probability that this identifies you is

&nbsp;&nbsp;**(1-2⁻ᴷ)ᴺ**.

Furthermore, in order to hold the probability of being identified below

&nbsp;&nbsp;**(1-1/N)ᴺ ≈ exp(-1) ≈ 36.7%**,

it is necessary that **K ≤ log₂(N)**.

**Proof.** The probability that all **K** observed features collide with any random person in the crowd is **2⁻ᴷ**. Thus, the probability of no collisions after checking the crowd of **N** people (meaning you are the only one matching the observed features) is **(1-2⁻ᴷ)ᴺ**. □

That's simple. But it's not realistic at all, since it assumes that people have immutable binary strings that they leak into their writing. Can we make it more realistic?

Well, there is a simple *lower* bound. That is, we can say in general that if the mutual information is significantly *less* than **log₂(N)**, then it's not possible to reliably identify someone.

**Theorem.** Suppose N random people are selected and their full writing style features are made public. One person from that group is chosen and produces a writing sample. Then, the attacker must guess who produced it. The average success rate of the attacker (averaged over the random pool, the random choice of author, and the random writing sample) is at most **(I(x;s)+1)/log₂(N)**.

**Proof.** Let **S=(s₁, s₂, s₃, …)** be the pool of **N** styles and let **n** be a random variable indicating which person was chosen. [Fano's inequality](https://en.wikipedia.org/wiki/Fano%27s_inequality) says that the highest possible success rate is bounded by the conditional mutual information between the writing sample **x** and the identity **n**, conditioning on the pool of writing styles, i.e. the probability of success is at most

&nbsp;&nbsp;**(I(x;n\|S)+1)/log₂(N)**.

However, we can bound that conditional mutual information as

&nbsp;&nbsp;**I(x;n\|S) ≤ I(x;n,S) = I(x;n,sₙ) = I(x;sₙ) = I(x;s).**

The first inequality is standard. The second step uses the fact that given **n**, the writing **x** is conditionally independent of all styles except the chosen writer. The third step uses the fact that **n** is conditionally independent of **x** given **sₙ**. The last step uses that **(x,sₙ)** is distributed as **(x,s)**. Substituting this bound gives the claimed result. □

So, if mutual information is much less than **log₂(N)**, reliable identification is impossible, even if the attacker knows all the style vectors perfectly. So, provided you don't leak that many bits, you're definitely safe.

But is the converse true? Does leaking more than **log₂(N)** bits always identify you? The general answer is *no*. The basic problem is that **I(x;s)** is the *average* information that an *average* person leaks in an *average* writing sample. Without further assumptions, you can construct scenarios where *some* rare people and writing samples contain gigantic amounts of information, but most people usually leak nothing. That would mean that the attacker is *very* certain in some cases but usually learns nothing.

So, to get a guarantee that identification is actually possible, you need to make some kind of additional assumption that the information leakage rate doesn't vary too much between different writers or between different things they write.

Suppose that **p(x,s)** is the joint distribution over writing styles **s** and writing samples **x**. Let's suppose that the attacker knows the true style vector **ŝ** for some person. Then, they will be given a writing sample **x** that either came from that person or came from a randomly chosen person, and must decide which. Formally, the attacker's goal is to guess if **x** was sampled from the writing distribution for that person, **p(x\|ŝ)** or from the population marginal **p(x)**. Intuition suggests that the attacker's best strategy will be to look at the ratio

&nbsp;&nbsp;**p(x\|ŝ)/p(x),**

and "accept" **x** as coming from **ŝ** if above some threshold, and reject it otherwise. In fact, the [Neyman-Pearson lemma](https://en.wikipedia.org/wiki/Neyman%E2%80%93Pearson_lemma) guarantees that this is the optimal strategy, in a very strong sense: That ratio contains *all* the information that's useful for making that decision.

Now here's something interesting: Instead of looking at the ratio, the attacker could look at the logarithm of the ratio. It makes no difference since it's monotonic. But if you take the logarithm of that ratio, and take the expectation over people and over texts, what do you get? Well:

&nbsp;&nbsp;**𝔼 ln (p(x\|s)/p(x)) = 𝔼 ln (p(x,s)/(p(x) p(s))) = I(x;s)** 

It's the mutual information! So, intuitively, the mutual information is how much an attacker learns about the style of the writer "on average", where that average is over both writers and text.

The following theorem will look at the average information in text for a writer with a particular style. I'll define this as

&nbsp;&nbsp;**D(s) = KL(p(X\|s) \|\| p(X))**.

Intuitively, this is how different the writing of someone with style **s** is from the population average. That's because if you take the average of this value over different styles, you get the mutual information. That is, **I(x;s) = 𝔼[D(s)]**.[^18]

**Theorem (informal).** Suppose that the attacker will observe some text and wishes to classify it as either coming from a writer with specific known style **ŝ**, or coming from someone with a random style. Suppose that the attacker is only willing to tolerate some small risk **ε** of a false positive. Provided that **D(ŝ)** is significantly larger than **-ln(ε)**, the attacker can achieve that, while also keeping the risk of false negatives very low, provided that the variance of how much information is revealed in a random writing sample is bounded.

**Theorem.** Let **D(ŝ) = KL(p(X\|ŝ) \|\| p(X))** to be the divergence between the target's writing distribution and the marginal distribution. Also, define **qₜ(x) ∝ p(x\|ŝ)ᵗ p(x)¹⁻ᵗ** to be the family that interpolates between those two distributions. To formalize the idea that "information leakage" for **ŝ** doesn't vary that much, we assume that some constant **V** exists such that for **0 < t < 1**, the variance of **log(p(x\|ŝ)/p(x))** under **qₜ** is bounded by **V**.

Then for any **ε** satisfying **exp(-D) < ε < exp(-D + ½ V)**, it is possible for the attacker to simultaneously achieve a false positive rate of **FPR ≤ ε** and a false negative rate of **FNR ≤ exp( - ½ (D+ ln ε)² / V).** This false positive rate reflects the mistake rate provided the writing sample **x** came from a randomly chosen other person, while the false negative rate reflects the mistake rate provided the writing sample **x** actually came from the person with style **ŝ**.

**Proof sketch.** Let **f** be the distribution of **l(x) = log(p(x\|ŝ)/p(x))** with respect to **p(x\|ŝ)** and let **g** be the distribution of **l(x)** with respect to **p(x)**. The stated variance assumption implies a quadratic bound **K(u) ≤ D u +½ V u^2** for **-1 < u < 0**, where **K** is the cumulant generating function of **f**. Observe that **g** is an exponential tilting of **f**. The attacker's strategy must be to "accept" **x** as coming from **ŝ** if **l** is above some threshold **c** and "reject" it otherwise. Use **K** in a Chernoff bound on the probability **l** is less than **c** under **f** to upper-bound **FNR ≤ exp( - ½ (D-c)²/V)**. Now, using that **g(l) = exp(-l) f(l)**, again use **K** in a Chernoff bound on the probability **l** exceeds **c** under **g** to upper-bound **FPR ≤ exp( -c - ½ (D-c)²/V)**. Both of these bounds are simultaneously valid when **D-V < c < D**. Setting **c** to make the false-positive bound equal to **ε** gives **FPR ≤ ε** and **FNR ≤ exp( -½ (V - √(V² - 2V(D + ln ε)))²/V).** The latter can be relaxed into the stated result using that **√(1-x) ≤1-x/2** for **0 ≤ x ≤ 1**. □

Now, if we suppose that the attacker wants to find a particular person, with a particular known style **s**. And suppose that the attacker has a pool of **N** people and will see one writing sample from each, but wants to limit the total probability of a false positive to **δ** after seeing one sample from each person. Then, they will need that

&nbsp;&nbsp;**(1-ε)ᴺ ≈ exp(-εN) = (1-δ),**

which is satisfied by **ε ≈ δ/N**. Substituting this into the previous result says that the attacker can hold the *total* risk of a false positive to **δ** while achieving a false-negative risk of

&nbsp;&nbsp;**FNR ≤ exp( - ½ (D(s) + ln δ - ln N)² / V).**

These results use natural logarithms because the math is easier if you measure information in nats. If you measure information in bits then you would get **log₂ δ** and **log₂ N**. (Rescaling **D** and **V** appropriately.)

So, again, as long as the average information for user **s** is significantly larger than **log₂ N**, the attacker can identify that user with minimal risk of false positives.

Some writers might leak more information (higher **D(s)**) and some writers might leak less information (lower **D(s)**). But remember, **I(x;s)=𝔼 D(s)**. So as long as information leakage doesn't vary too much between people, and assuming that **I(x;s)** is much larger than **log₂ N** (and assuming that variance condition), almost everyone can be identified.

[^1]: Editor's note: After this sentence was written, many additional hours were devoted to further idiotic tinkering.

[^2]: It's fine.

[^3]: A standard binary variable that is 0 or 1 with 50% probability conveys 1 bit of information, while a variable that is 0 / 1 / 2 with probability 49.8% / 49.8% / 0.4% conveys 1.0336 bits.

[^4]: People born in certain decades are also presumably more likely to employ *see what I did there* gambits.

[^5]: For example, here is the information content for seven different "bent coins":
	

	| Probability of landing heads | Information |
	| ---------------------------- | ----------- |
	| 0.50 (fair coin)             | 1.000       |
	| 0.60                         | 0.971       |
	| 0.70                         | 0.881       |
	| 0.80                         | 0.722       |
	| 0.90                         | 0.469       |
	| 0.95                         | 0.286       |
	| 0.99                         | 0.081       |

	
	

[^6]: Here's a more formal looking version of the table from the previous footnote:
	

	| p(A) | p(B) | Information |
	| ---- | ---- | ----------- |
	| 0.50 | 0.50 | 1.000       |
	| 0.60 | 0.40 | 0.971       |
	| 0.70 | 0.30 | 0.881       |
	| 0.80 | 0.20 | 0.722       |
	| 0.90 | 0.10 | 0.469       |
	| 0.95 | 0.05 | 0.286       |
	| 0.99 | 0.01 | 0.081       |
	

	You can generate that table by running this code:

	
	```python
	from scipy.stats import entropy
	 
	dists = ([0.5, 0.5], [0.6, 0.4], [0.7, 0.3], [0.8, 0.2], [0.9, 0.1], [0.95, 0.05], [0.99, 0.01])
	entropies = [entropy(p, base=2) for p in dists]
	
	print("| p(A) | p(B) | Entropy |")
	print("|------|------|---------|")
	for i in range(len(dists)):
	    print(f"| {dists[i][0]:<4.3f} | {dists[i][1]:<4.3f} | {entropies[i]:<7.3f} |")
	```
	 

	With three categories, the story is much the same. Things need to get quite uneven before information drops too much:

	| p(A)  | p(B)  | p(C)  | Entropy |
	| ----- | ----- | ----- | ------- |
	| 0.333 | 0.333 | 0.333 | 1.585   |
	| 0.400 | 0.300 | 0.300 | 1.571   |
	| 0.500 | 0.250 | 0.250 | 1.500   |
	| 0.600 | 0.200 | 0.200 | 1.371   |
	| 0.700 | 0.150 | 0.150 | 1.181   |
	| 0.800 | 0.100 | 0.100 | 0.922   |
	| 0.900 | 0.050 | 0.050 | 0.569   |
	| 0.950 | 0.025 | 0.025 | 0.336   |
	| 0.990 | 0.005 | 0.005 | 0.091   |
	
	You can generate that with this code:
	
	```python
	from scipy.stats import entropy
	
	dists = (
	    [1/3, 1/3, 1/3],
	    [.4, .3, .3],
	    [.5, .25, .25],
	    [.6, .2, .2],
	    [.7, .15, .15],
	    [.8, .1, .1],
	    [.9, .05, .05],
	    [.95, .025, .025],
	    [.99, .005, .005]
	)
	entropies = [entropy(p, base=2) for p in dists]
	
	print("| p(A) | p(B) | p(C) | Entropy |")
	print("|------|------|------|---------|")
	for i in range(len(dists)):
	    print(f"| {dists[i][0]:<4.3f} | {dists[i][1]:<4.3f} | {dists[i][2]:<4.3f} | {entropies[i]:<7.3f} |")
	```
	
	

[^7]: Roughly speaking, we we should discount those maximum bits as follows:
	
	* Near even: No discount.
	* "Mildly uneven" (E.g. 70/30 with two categories) Discount by 10%.
	* "Quite uneven" (E.g. 90/10 with two categories) Discount by 50%.
	* "Extremely uneven" (E.g. 99/1 with two categories) Discount by 90%.

	The Shannon entropy of a categorical distribution is - Σᵢ pᵢ log₂ pᵢ. Or, in python:
	
	```python
	import math
	def entropy(probs):
		return sum(-p * math.log2(p) for p in probs)
	```

	Age: It's hard for me to imagine you could guess age from text with accuracy higher than 5 years. If you assume an age between 0 and 100, that would be 20 categories and log2(20)=4.32 bits. These are [mildly non-uniform](https://en.wikipedia.org/wiki/Demographics_of_the_United_States) so I'll reduce to 3.9. 

	Education: I'm assuming 6 categories: less than high school, high school, some college, finished college, master's degree, doctorate. That would be log2(6)=2.58 bits, but fairly uneven, so I'll reduce by 20% to 

	Ethnicity: Assuming 62% white, 11% black, 16% latino, 6% asian, 1.5% indigenous, 3.5% mixed/other, and actually using the entropy formula.

	Family status: I'm using two categories: Children / no children, on the logic that guessing the number of children would be very hard. These are mildly non-uniform, so I'll drop to 0.8 bits. You could have a third category for having children that are grown and that had left home, but this would be heavily redundant with age.

	Income: The US census gives 11 income brackets. That seems as good a way of discretizing as anything. That would be log2(11) = 3.459 bits, but  these are again moderately non-uniform, so I'll reduce to 2.5.

	Marital status: I'm taking 3 categories (single, married, divorced / widowed / etc). That would be log2(3)=1.58 bits at maximum, but again these are somewhat non-uniform, so I dropped that to 1.2.

	Mental health: I'm using 3 categories: "Healthy", "chronic condition", and "severe issues". Assuming 73% healthy 25% chronic condition, 2% "severe issues", and using the entropy formula gives 0.9 bits.

	Native language: I'm using 2 categories, namely "English native", and "non-English native". These are pretty uneven inside the Anglosphere, so I'll drop from 1 bit to 0.6 bits.

	Occupation. The BLS classification gives 23 major groups. That would be log2(23)=4.523 bits, but it's moderately non-uniform, so I'll reduce to 4 bits.

	Physical health: Assuming 60% "healthy" 30% "chronic condition" 10% "severe issues" and using the entropy formula.

	Political leanings:  I'm using three categories (left, center, right). These are fairly uniform so I'm using 1.58 bits.

	Region: I asked an LLM to divide the Anglosphere up into a number of regions with reasonable granularity. With some tinkering, it gave 23 regions: South East England, South West England, Midlands, Northern England, Scotland, Wales, Republic of Ireland, Northern Ireland, Quebec, Ontario, Western Canada, Atlantic Canada, Northeast US, Southern US, Midwest US, Western US, Alaska, Hawaii, Southeast Australia, Western Australia, Queensland, Central & Southern Australia, New Zealand. With LLM-generated population estimates (which looked reasonable) and plugging into the entropy formula, this gave 3.5481 bits.


	| #   | Region                       | Pop (M) | pi (Pop/Total) | log2⁡(pi) | pilog2⁡(pi) |
	| --- | ---------------------------- | ------- | -------------- | --------- | ----------- |
	| 1   | South East England           | 20.0    | 0.04062        | -4.617    | -0.1875     |
	| 2   | South West England           | 6.0     | 0.01219        | -6.353    | -0.0774     |
	| 3   | Midlands                     | 11.0    | 0.02234        | -5.485    | -0.1225     |
	| 4   | Northern England             | 20.0    | 0.04062        | -4.617    | -0.1875     |
	| 5   | Scotland                     | 5.5     | 0.01117        | -6.484    | -0.0724     |
	| 6   | Wales                        | 3.0     | 0.00609        | -7.359    | -0.0448     |
	| 7   | Republic of Ireland          | 5.0     | 0.01015        | -6.626    | -0.0673     |
	| 8   | Northern Ireland             | 2.0     | 0.00406        | -7.949    | -0.0323     |
	| 9   | Quebec                       | 9.0     | 0.01828        | -5.774    | -0.1055     |
	| 10  | Ontario                      | 16.0    | 0.03250        | -4.943    | -0.1606     |
	| 11  | Western Canada               | 13.0    | 0.02640        | -5.247    | -0.1385     |
	| 12  | Atlantic Canada              | 2.5     | 0.00508        | -7.625    | -0.0387     |
	| 13  | Northeast US                 | 56.0    | 0.11373        | -3.136    | -0.3568     |
	| 14  | Southern US                  | 130.0   | 0.26401        | -1.922    | -0.5074     |
	| 15  | Midwest US                   | 69.0    | 0.14013        | -2.836    | -0.3973     |
	| 16  | Western US                   | 80.0    | 0.16247        | -2.624    | -0.4264     |
	| 17  | Alaska                       | 0.7     | 0.00142        | -9.467    | -0.0134     |
	| 18  | Hawaii                       | 1.4     | 0.00284        | -8.790    | -0.0249     |
	| 19  | Southeast Australia          | 16.0    | 0.03250        | -4.943    | -0.1606     |
	| 20  | Western Australia            | 3.0     | 0.00609        | -7.359    | -0.0448     |
	| 21  | Queensland                   | 5.5     | 0.01117        | -6.484    | -0.0724     |
	| 22  | Central & Southern Australia | 2.5     | 0.00508        | -7.625    | -0.0387     |
	| 23  | New Zealand                  | 5.3     | 0.01076        | -6.539    | -0.0703     |
	|     | **Sum of pilog2⁡(pi)**       |         |                |           | **-3.5481** |

	Religious affiliation: 3 categories (christian, other religion, atheist / agnostic). These are uniform-ish.

	Sex: 2 categories, near-even

[^8]: Consider a set of binary random variables, each of which is equally likely to be 0 and 1, yet all are correlated with a pairwise correlation coefficient of ρ. There are many distributions that satisfy this condition, but a natural choice is an Ising model. If there are many variables, then the entropy per-variable in an Ising model with pairwise correlations of ρ tends to h((1+√ρ)/2), where h is the [binary entropy function](https://en.wikipedia.org/wiki/Binary_entropy_function). We can print out those numbers:
	

	|      ρ | h((1+√ρ)/2) |
	| -----: | ----------: |
	| 0.0000 |  1.00000000 |
	| 0.1000 |  0.92661216 |
	| 0.2000 |  0.85048963 |
	| 0.3000 |  0.77121926 |
	| 0.4000 |  0.68826012 |
	| 0.5000 |  0.60087604 |
	| 0.6000 |  0.50801160 |
	| 0.7000 |  0.40803633 |
	| 0.8000 |  0.29811751 |
	| 0.9000 |  0.17212786 |
	| 1.0000 |  0.00000000 |

	As you can see, the entropy per-variable is always a bit more than 1-ρ. But the Ising model is optimistic, in the sense that it has the highest entropy of all distributions meeting the given conditions. So, screw it, let's estimate the entropy per-variable to just be 1-ρ.

[^9]: If it means anything to you, I asked Kimi 2.6 to hallucinate some numbers:
	
	||**Age**|**Edu**|**Eth**|**Fam**|**Inc**|**Mar**|**Mhe**|**Nlg**|**Occ**|**Phe**|**Pol**|**Reg**|**Rel**|**Sex**|
	|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
	|**Age**|1.0|-0.2|0.0|0.6|0.1|0.5|-0.1|0.0|0.2|-0.5|0.1|0.0|0.2|-0.1|
	|**Edu**|-0.2|1.0|0.3|0.2|0.6|0.2|0.1|0.1|0.7|0.3|0.3|0.2|-0.2|-0.1|
	|**Eth**|0.0|0.3|1.0|0.2|0.3|0.1|-0.1|0.7|0.3|-0.3|0.2|0.4|0.4|0.0|
	|**Fam**|0.6|0.2|0.2|1.0|0.2|0.7|-0.1|0.0|0.1|0.0|0.1|0.0|0.2|0.1|
	|**Inc**|0.1|0.6|0.3|0.2|1.0|0.3|-0.2|0.1|0.7|0.3|0.1|0.2|0.0|-0.1|
	|**Mar**|0.5|0.2|0.1|0.7|0.3|1.0|0.2|0.0|0.1|0.2|0.1|0.0|0.2|0.0|
	|**Mhe**|-0.1|0.1|-0.1|-0.1|-0.2|0.2|1.0|0.0|-0.2|0.4|0.0|0.0|-0.1|0.1|
	|**Nlg**|0.0|0.1|0.7|0.0|0.1|0.0|0.0|1.0|0.1|0.0|0.1|0.5|0.3|0.0|
	|**Occ**|0.2|0.7|0.3|0.1|0.7|0.1|-0.2|0.1|1.0|0.1|0.2|0.2|0.0|0.3|
	|**Phe**|-0.5|0.3|-0.3|0.0|0.3|0.2|0.4|0.0|0.1|1.0|0.0|0.1|0.0|0.1|
	|**Pol**|0.1|0.3|0.2|0.1|0.1|0.1|0.0|0.1|0.2|0.0|1.0|0.5|0.4|0.1|
	|**Reg**|0.0|0.2|0.4|0.0|0.2|0.0|0.0|0.5|0.2|0.1|0.5|1.0|0.2|0.0|
	|**Rel**|0.2|-0.2|0.4|0.2|0.0|0.2|-0.1|0.3|0.0|0.0|0.4|0.2|1.0|0.1|
	|**Sex**|-0.1|-0.1|0.0|0.1|-0.1|0.0|0.1|0.0|0.3|0.1|0.1|0.0|0.1|1.0|	

	Personally, this doesn't mean very much to me…

[^10]: It's more complicated than this, because some atoms (e.g. strontium-90) emit more energy per decay than others. And some types of radiation are more harmful to human life than others.

[^11]: In general, if you want an exponential curve f(n) that starts at 1 for n=0 and decays to 1-X for n=N, you should choose f(n) = exp(n × ln(1-X) / N). So for demographic features we're using X=0.6 and N = 4500, meaning f(n) = exp(-0.00020362 × n). For personality features, we're using X=0.7, meaning f(n) = exp(-0.00026755 × n), and for writing style features, we're using X = 0.8, meaning f(n) = exp(-0.000357653 × n). So the total number of bits remaining hidden is 17.2 × exp(-0.00020362 × n) + 39.0 × exp(-0.00026755 × n) + 50.0 × exp(-0.000357653 × n).

[^12]: OK, what's the most likely reason I might be wrong? Above, I used math to estimate the information in features, and then I basically made up numbers for how much of that information can be guessed from text. Even so, my greatest concern is that the first part. I'm a bit worried that I might be overestimating the amount of information in the features themselves due to inadequately discounting for correlations. For one thing, there are probably correlations between feature groups. (For example, I'd bet that people who are high in perfectionism are less likely to use *lose* and *loose* interchangeably, and that people who live in Northern England are more likely to use the character string `colour` than people who live in Hawaii.) Also, my crude method of discounting information by ρ due to pairwise correlations of ρ might not discount enough: I used an estimate based on an Ising model, which is the maximum-entropy (highest information) distribution given the correlation constraints. I haven't been able to figure out how much lower the information could be in the worst-case.

[^13]: People debate if this is true for "intelligence", but it's definitely true in terms of bit-rate.

[^14]: Also, arguably, stylometry is about language. This means that large *language* models probably have much of what they need baked in. That might explain why they're pretty good at it just "by accident". But to do this optimally I think they'd need self-reflection (e.g. access to probabilities of text given different contexts) that current LLMs aren't typically capable of, and wouldn't know how to manipulate correctly without task-specific training.

[^15]: You could conjecture that near-optimal stylometry abilities are some kind of "emergent property". But the general lesson so far is that LLMs mostly don't have emergent properties but are just good at what they're trained at.

[^16]: (Meta-joke about you—person who works at an AI company—thinking, "maybe we should do that", coming to this footnote, and seeing this meta-joke.)

[^17]: Instead of "homogenizing" writing by imposing a generic style, perhaps it would be better to "camouflage" it by enforcing a very strong but random style.

[^18]: Be a little careful here: Typically, the KL-divergence is understood to be measured in nats. But in this article, I've measured mutual information in bits. That's fine, but you need to convert. For example, 106.2 bits = 73.60 nats.