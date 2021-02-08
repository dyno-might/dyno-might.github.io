---

layout: post
title: "Writing is hard: Branching, rulesets, stress, and value"
image: /img/writing/typewriter.jpg
tags: writing
hero_light: true
last_updated: 2021-02-07

---

[Standard advice](https://archive.org/stream/pdfy-2_qp8jQ61OI6NHwa/Strunk+&+White+-+The+Elements+of+Style,+4th+Edition_djvu.txt) on writing is to use the active voice, be clear, minimize extra words. That's all fine, but isn't it a bit... superficial? No one reads a book because it's *clear*.

Hoping for deeper advice, I read the experts. Here's some of what I learned: Have a consistent ruleset. Titles are a black art. Have empathy for the brain's parsing heuristics.  It's impossible to follow all the conventions. Write a thesis statement. Value value.

# Stephen King

(*On Writing: A Memoir of the Craft, 2000*) Here's how Stephen King writes a novel:

- He has a vague story idea.
- He creates some characters.
- He places those characters in a situation.
- He writes the novel from beginning to end.

Here's how he writes *well*: He lets the characters do what they want. He warns against plot. If a rigid set of events must happen, characters become unreal and robotic. Let them breathe and accept things may stray from your original vision.

There's an analogy to science fiction, where the cardinal sin is unclear rulesets. Good science fiction states the rules of the game and then follows them. It's OK to have faster-than-light travel or telepathic aliens, but explain what's possible and stick with it. There's no stakes if the characters are always rescued by their robot butler revealing some previously unknown superpower.

Both King's formula and good science fiction are based on the same principle: Set up a system with a ruleset and then let it go.  The fun is in watching how things evolve from the initial conditions.


# Stein Sol

(*Stein on Writing, 1995*) Sol liked to spy on people at bookstores. He gives a brutal picture:

* For 99% of books, they scan the title and move on.
* If they pick up a book, they usually just skim the cover or first page.
* No one gets past the third page before either buying it or putting it back.

He stresses: Unless you're famous, the title and introduction are what determine if anyone reads you. <!-- (He's talking about books in physical stores, but I'm sure it's even more true for articles on the internet today.) -->

For introductions he says to give a surprising personality or action so the reader will hunger for more. Here's some great first sentences.

* "You must not tell anyone", my mother said, "what I am about to tell you."
* At exactly 10:19 A.M. yesterday, a grandmother's purse on a conveyor belt at Orange County airport set off an alarm that caused two security guards to rush to the scene.
* I have long been an admirer of the octopus.

For titles, he gives examples of what the author wanted versus what was published.

* Diego Rivera → The Fabulous Life of Diego Rivera
* The Battle of Schmidt → Follow Me and Die
* The Anatolian Smile → [America America](https://en.wikipedia.org/wiki/America_America)
* The Eye and the Ear → [A Moveable Feast](https://en.wikipedia.org/wiki/A_Moveable_Feast)
* Twilight → [The Sound and the Fury](https://en.wikipedia.org/wiki/The_Sound_and_the_Fury)

There's no formula. The takeaway is that these choices are important, some people are good at making them, Stein Sol is one of those people, and all the authors who refused to listen to him did so at their peril.

# Stephen Pinker

(*The Sense of Style: The Thinking Person's Guide to Writing in the 21st Century, 2014*)

> The view that beating a third-rate Serbian military that for the third time in a decade is brutally targeting civilians is hardly worth the effort is not based on a lack of understanding of what is occurring on the ground.

> It's not a lack of understanding of what is occurring on the ground that creates the view that it's hardly worth the effort to beat a third-rate Serbian military that is brutally targeting civilians for the third time in a decade.

The first quote above is a monstrosity, the second merely bad. Why?

You may suspect a simple trick. But look look at the transformation. We've basically permuted chunks <font color="blue">A</font><font color="purple">B</font><font color="red">C</font><font color="#996600">D</font><font color="#669933">E</font> into <font color="#669933">E</font><font color="#996600">D</font><font color="blue">A</font><font color="purple">B</font><font color="red">C</font>.

> The view that <font color="blue">beating a third-rate Serbian military</font> that <font color="purple">for the third time in a decade</font> is <font color="red">brutally targeting civilians</font> is <font color="#996600">hardly worth the effort</font> is not based on <font color="#669933">a lack of understanding of what is occurring on the ground</font>.

> It's not <font color="#669933">a lack of understanding of what is occurring on the ground</font> that creates the view that it's <font color="#996600">hardly worth the effort</font> to <font color="blue">beat a third-rate Serbian military</font> that is <font color="red">brutally targeting civilians</font> <font color="purple">for the third time in a decade</font>.

According to Pinker, the second is better because of *the algorithm your brain uses to parse English text*. I guess that's a tautology, but it's helpful once you get specific about the heuristics our brains use.

**Principle 1: Avoid left-branching.**

![left branching parse](/img/writing/left_branching_cropped.jpg)

![right branching parse](/img/writing/right_branching_cropped.jpg)

These [syntax trees](http://nlpviz.bpodgursky.com/) show the problem. The first sentence has lots of **left-branching**. This is harder to parse since there's less context. Picture your brain partway through the first sentence. It will be deep in left part of the first tree above, with no idea what's on all the right branches. While parsing the second sentence, you never have more than a few "open branches".

**Principle 2: Avoid Garden Paths.**

> I enthusiastically recommend this candidate with no qualifications whatsoever. 

Even worse than left-branching is multiple valid parses. (Who lacks qualifications, the candidate or the recommendation?) 

> The man who hunts ducks out on weekends. 

More common than ambiguous sentences are **garden paths**. These have *local* ambiguities so reader starts to build one tree, then has to backtrack when later information arrives. This sentence only has one parse, yet it's confusing because your brain knows that "hunts ducks" usually bind together and it's expecting something like "...out on the lake."

>  The man who hunts goes out on weekends. 

This is much easier to understand because "hunts goes" doesn't mean anything.

Garden paths are easy to write, yet are rare in spoken language. Speakers naturally use tone and rhythm to clarify meaning. Be careful not to imagine these clues when writing, since readers only get bare words.

While classic style guides call to *omit needless words*, this is not always good advice. Sometimes extra words can improve clarity by making it more obvious what a word means. Compare these:

> Light cranes lead us right to bass.

> Light-colored cranes then lead us to the right, to some bass.

If the first sentence is read in context, a reader might be able to figure out what which meaning of *light*, *crane*, *lead*, *right* and *bass* are intended. But why make them do that?

Sometimes longer text is faster to read.

**Principle 3: Context first**

> A discussion on turbulent airflow added to the concerns about pressure in the air purifier post in this site.

This is hard to read because it starts out with details, and only gives you the context later. If we put the old information first, it becomes much easier to read.

> In this site's post on air purifiers, the concerns about pressure barriers led to a discussion about turbulent airflow.

When style guides tell you not to use the passive voice, this is why. Usually the passive voice puts the wrong information at the wrong part of the sentence. But not always:

> Whole wheat pasta frightens me.

> I am frightened by whole wheat pasta.

*I* am old news. The pasta is new. Pasta is better at the end.

For related issues, I recommend *The Science of Scientific Writing*, an article by Gopen and Swan from 1990 now [freely available online](https://www.americanscientist.org/blog/the-long-view/the-science-of-scientific-writing).


# Benjamin Dreyer: We Got Some Rules

(*Dreyer's English: An Utterly Correct Guide to Clarity and Style, 2019*) This explains punctuation, commonly misspelled words, when to write out a number, how long dashes should be, and how to (not) borrow words from other languages. He disparages some common advice, such as to avoid sentence fragments or that you can't start a sentence with *but*. On the other hand, he *insists* on other rules such as that terminal periods "are always set inside." It's hard to tell the difference between the arbitrary illogical rules that we should happily ignore and the arbitrary illogical rules that only a simpleton would ever break.

All the same, I'd like to do as he says, but there are a *lot* of rules. My unavoidable takeaway is that I'll never remember or obey half of them. Unless you're an aspiring editor, I'm not sure I'd recommend this book. The fact that I still enjoyed all three hundred pages is a testament to Dreyer's outlandishly compelling style.

# Matthew Yglesias: Write a Damn Thesis 

This was just a tweet, not a book.

> *THE* professional journalist habit that could easily improve 90% of writing by smart, knowledgeable amateurs is making sure to check that you've written a strong lede with a clear thesis statement.

This might be bad advice for the New Yorker. Still, if you're unsure if it applies to you, it probably does. It's easy to fantasize about readers savoring each subtle turn of your masterpiece. In reality, it's *very* hard to make even your highest-level message clear.

# Bonus: Larry McEnerney

This isn't even a piece of writing. It's a [lecture](https://www.youtube.com/watch?v=vtIzMaLkCaM). Still, it changed how I look at writing, and to some degree life. He asks the audience what makes good non-fiction writing. They give answers like:

1. Persuasive
2. Organized
3. Clear

Sure, he says, these are kind of interesting, but the real answer is:

1. Valuable

The only thing that matters is if the reader gets something they want. Why have a thesis statement? Because life is short, and people shouldn't waste time reading something they don't care about. Do arcane stye guidelines matter? Only if it matters to your readers. Is beauty or clarity more important? It depends on if people are reading for aesthetics or information.

He also stresses to avoid perfection. Very, *very* little non-fiction from 100 years is still read today. Writing is less ephemeral than talking, but it's still a conversation. It will be forgotten. It won't make you immortal– nothing will. Once you've said what you want to say, move on.

<!--
emphasize value
don't worry about things that don't interfere with value
-->