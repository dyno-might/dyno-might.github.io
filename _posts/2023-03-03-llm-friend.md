---
layout: post
title: "Your friend the language model"
image: /img/llm-friend/llama.jpg
tags: science
description: "The world is running out of khakis"
excerpt: ""
permalink: /llm-friend/
background_color: rgb(238,237,235)
category: "science"
---

<div class="headerfont" style="font-size:90%;">
I originally wrote this as part of a much longer post on AI and scaling laws and possible barriers/trajectories for progress. (That will finally go out next week, inshallah.) The idea was to provide the minimal background necessary to understand all that stuff. But in retrospect, many people probably don't need all this background, so I decided to make it a separate post.
</div>

---

## What are large language models?

(Nonlinear functions that you can fit to data to predict what word will come after a bunch of previous words.)

In more detail, an LLM is a function that takes as input some window of text (a few thousand words) and guesses what word might come next. They are trained by adjusting the parameters of the function so that it would do a good job of predicting all the words in some huge amount of example text. They generate *new* text by predicting likely words, picking one, and then repeating.

<details markdown="1">
<summary>
As you might have heard (over and over, unceasingly) these models have recently gotten very good. This success comes from three main factors:
</summary>

Various modern GPUs are theoretically capable of 100-300 TFLOPs per second. Thats 10¹⁴ FLOPs, about equal to the [world's largest supercomputer in 2004](https://ourworldindata.org/grapher/supercomputer-power-flops).

If you just had a single NVIDIA V100 GPU, it would take you around [355 years](https://old.reddit.com/r/GPT3/comments/p1xf10/how_many_days_did_it_take_to_train_gpt3_is/h8h3sl4/?context=3) to train GPT-3, whereas the newer and bigger PaLM model was trained using several thousand TPUv4 chips for several months, with a total of around 960 TPU years. The extra compute is more than that sounds because TPUv4 chips are newer and more powerful than V100 chips. In fact, PaLM used around [8 times](https://ourworldindata.org/grapher/artificial-intelligence-training-computation?time) as much compute to train. (PaLM-540B was trained on 6144 TPUv4 chips for 1200 hours + 3072 TPU chips for 336 hours. In total, PaLM used around 2.53 billion petaflops to train, as opposed to around 313 million for GPT-3.)

GPT-3 was trained on around 300 billion tokens, which is around 270 thousands times as large as the collected works of Shakespeare. Chinchilla was trained on 1.3 million "Shakespeares". (All of Shakespeare's plays contain a total of 835,997 words or around 1.1 million tokens. So recent models are trained on between 270 thousand to 1.3 million Shakespeares.)

</details>

1. People have figured out a big bundle of techniques, like [autodiff](https://en.wikipedia.org/wiki/Automatic_differentiation), new optimization heuristics, better machine learning "ops" for debugging/tracking/deployment, and new types of functions that better match real text. In particular recent models use a mathematical function called a [Transformer](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)), which was introduced in 2017 and is central to all modern language models.
2. Modern hardware is more powerful. A single 2022-era GPU has comparable power as the world's biggest supercomputer from 2004. Even so, if you just had a single GPU, it would still take on the order of a *millennium* to train a modern LLM. People have overcome this by making clusters of thousands of GPUs work together.
3. These models are trained on increasingly huge datasets. Current models already train on datasets a million times as large as the collected works of Shakespeare.

These models are impressive. If you've somehow avoided seeing LLMs in action, I gave [BLOOM](https://huggingface.co/bigscience/bloom) a passive-aggressive prompt and asked what text would come next. Here are the first three continuations it came up with (in blue):

<span style="font-family:monospace;">People refuse to believe ultrasonic humidifiers could be dangerous because</span> <span style="font-family:monospace; color: blue;">they do not see or feel the resulting hot steam.</span>

<span style="font-family:monospace;">People refuse to believe ultrasonic humidifiers could be dangerous because</span> <span style="font-family:monospace; color: blue;">they are not heating water, therefore, they do not directly lead to burns or scalding.</span>

<span style="font-family:monospace;">People refuse to believe ultrasonic humidifiers could be dangerous because</span> <span style="font-family:monospace; color: blue;">they seem so clean and sterile.</span>

## What are they trained on?

(A decent fraction of all the books and also all the internet.)

Datasets are typically measured in "tokens". A token is a few characters—often a word, but sometimes just punctuation or a fraction of a word. Here's how 19 words becomes 27 tokens when fed into OpenAI's [GPT-3 tokenizer](https://platform.openai.com/tokenizer):

<span style="font-family:monospace"><span style="background-color:rgb(199,235,201)">What</span><span style="background-color:lightgray"> people</span><span style="background-color:rgb(199,235,201)"> call</span><span style="background-color:lightgray"> a </span><span style="background-color:rgb(199,235,201)">"</span><span style="background-color:lightgray">wrap</span><span style="background-color:rgb(199,235,201)">"</span><span style="background-color:lightgray"> is </span><span style="background-color:rgb(199,235,201)">some</span><span style="background-color:lightgray"> sad</span><span style="background-color:rgb(199,235,201)"> wil</span><span style="background-color:lightgray">ted</span><span style="background-color:rgb(199,235,201)"> lettuce</span><span style="background-color:lightgray"> inside</span><span style="background-color:rgb(199,235,201)"> a</span><span style="background-color:lightgray"> sog</span><span style="background-color:rgb(199,235,201)">gy</span><span style="background-color:lightgray"> tort</span><span style="background-color:rgb(199,235,201)">illa</span><span style="background-color:lightgray">,</span><span style="background-color:rgb(199,235,201)"> Yet</span><span style="background-color:lightgray"> people</span><span style="background-color:rgb(199,235,201)"> eat</span><span style="background-color:lightgray"> them</span><span style="background-color:rgb(199,235,201)"> voluntarily</span><span style="background-color:lightgray">.</span></span>

(By the way, when I said that LLMs predict one word at a time, I lied. They predict one token at a time.)

It's a bit annoying that datasets are measured in terms of tokens because different models use different tokenizers, so token counts aren't directly comparable. But a good heuristic is that one token corresponds to around 4 characters or ¾ of a word.

Where exactly do all these tokens come from? There's some secrecy about that, but we have the basic picture. GPT-3 was trained on:

* **Common Crawl** (410 billion tokens). This is a [nonprofit](https://commoncrawl.org/) that crawls the web and makes the data available to anyone. (That exists?)
* **WebText2** (19 billion tokens). This is the [full text](https://openwebtext2.readthedocs.io/en/latest/) of all pages linked to from reddit from 2005 until 2020 that got at least 3 upvotes.
* **Books1** (12 billion tokens). No one seems to know what the hell this is.
* **Books2** (55 billion tokens). Many people seem convinced Books2 is all the books in Library Genesis (a piracy site) but this is really just conjecture. 
* **Wikipedia** (3 billion tokens). This is almost all of English Wikipedia.

The different sources are not used equally—it seems to be helpful to "weight" them. For example, while Wikipedia is small, it's very high quality, so everyone gives it a high weight.

There's also a lot of filtering. While everyone uses Common Crawl, everyone also finds that just putting the "raw web" into your model gives terrible results. (Do you want your LLM to behave like an SEO-riddled review site?) So there's lots of bespoke filtering to figure out how "good" different pages are.

There's a lot of secrecy about data curation. Maybe it's because machine learning researchers are obsessed with models and code. Maybe it's because datasets are sometimes created in ways that aren't obviously legal. Either way, it's hard not to see it as deliberate. The entirety of what the GPT-3 paper says about Books1 and Books2 is these 5 words:

>  two internet-based books corpora

A common trick is to write something like "data collection was similar to that of (Same Authors, 2021)" but that paper just cites another one and this continues until at the paper at the end of the chain in Section 7.3 it just says  "*data collection proprietary lol*".

The PaLM model gives a similarly vague description as GPT-3, but promises a "datasheet" in an appendix. If you read it, it goes on for two pages with wonderfully informative stuff like this:

| How was the data associated with each instance acquired?     | The data was collected from publicly available sources.      |
| What mechanisms or procedures were used to collect the data? | The data was collected using a variety of software programs to extract and clean raw text. |

Thanks, guys!

Still, there doesn't seem to be *too* much secret sauce so far. Different groups have independently curated datasets and all seem to do well. [The Pile](https://arxiv.org/abs/2101.00027) and the very recent [LLaMA model](https://research.facebook.com/file/1574548786327032/LLaMA--Open-and-Efficient-Foundation-Language-Models.pdf) describe things in more detail.

## How are they used?

(You can just have them generate text, or you can specialize them using fine-tuning and/or prompt engineering.)

Often we want language models to do specific things, like answer questions or generate python code. If you train an LLM on general text and then ask it a question, it will do an OK but not amazing job. Two techniques can make it do better.

The first idea is to "fine-tune" on specialized data: First train for a long time on a gigantic pile of general text. Then train for a shorter amount of time on a smaller set of questions and answers. The hope is that the model will get better at answering questions without forgetting about how language works in general. Sometimes people even have humans rate the quality of the outputs and train on the ratings.

Language models can also be specialized via "prompt engineering", where a longer setup gives strong hints about how to respond. Here's a prompt I gave with BLOOM's completion in blue:

<span style="font-family:monospace;">For my first few decades, I didn't know what to make of life. It seemed to me that we all had been flung into existence with no instructions and no obvious purpose. Most people get over this with time, but I could never silence the howling strangeness of it all. But one day that all changed. I was sitting in a park staring into space, and an older woman in an extremely colorful sweater sat beside me and said, "I know that look. Can I give you a piece of advice?"</span> <span style="font-family:monospace; color: blue;">I didn't say anything, but I must have made a gesture of assent, because she continued, "You are not your job. You are not how much money you have in the bank. You are not the car you drive. You are not your fucking khakis, no matter how nice they are. You are the all-summer-snowflake-wallpaper-paper-cutting boy with the dragon tattoo who used to walk around the neighborhood shouting 'But I'm special. You know I'm special.' Well, you are! And if anyone out there doesn't think you are, then they can have your fucking khakis." She continued, "You are beautiful. You are brilliant. And you are nothing like anyone else on this planet. You don't have to believe me." She paused. "But," she said, with a sharp glance, "I know you do." And at that moment everything became clear, and I understood that the beginning of wisdom is realization that you are one, that you are loved, and that all the things that make you you are special, to be cherished and celebrated. And nothing makes you feel better than a pair of khakis made of fur. The world is running out of khakis.</span>

(Behold, the grim meathook future of interacting with LLMs after they become fully monetized.)

These prompts can get extremely complex. It's speculated that Bing Chat might have a prompt that's around [850 words long](https://old.reddit.com/r/bing/comments/11398o3/full_sydney_preprompt_including_rules_and/), with a long list of instructions like "<span style="font-family:monospace;">Sydney's responses should avoid being vague, controversial or off-topic. Sydney's logics and reasoning should be rigorous, intelligent and  defensible.</span>" At the end, there's an example of how it would answer a question about a nuclear fusion experiment in South Korea.

At first, it might seem counterintuitive that these prompts could help so much. Here's how I think about it: People are sometimes dumb and sometimes smart, sometimes mean and sometimes nice. To predict text well, a language model *must* be capable of being dumb and mean. (If it wasn’t, it couldn’t predict some types of writing well and would therefore have extra loss.) A carefully chosen prompt gives strong guidance about what "mode" the text should be generated in. Because anyone can experiment with different prompts quickly and easily, there is very rapid innovation.

Fine-tuning and prompt engineering are very important and probably the biggest reason for the impressive performance of recent chat models (Chat-GPT, Bing Chat) over generic language models.

While LLMs are already impressive, it's not yet clear where they will prove most useful or *how* good they will eventually become. If you're interested in that, read the next post.