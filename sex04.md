---

layout: post
title: "Why sex?"
image: /img/writing/typewriter.jpg
tags: writing
hero_light: true
tags: science explainer

---

Life reproduces and evolves. We all know the story: During reproduction, mutations sometimes happen. If those mutations increase reproductive fitness, they tend to stick around. If they decrease reproductive fitness they don't.

Fine! But why reproduce *sexually*? Why mix the genes of two parents? The earliest forms of life didn't 

This question has a simple but surprising answer. We can actually find that answer ourselves by doing some simple simulations.

* auto-gen TOC:
{:toc}

# The model

Let's make a very simple mathematical model of asexual reproduction:

1. There are $N$ people. Each person's genes are a binary string of length $G$. Each gene is either *good* or *bad*.
2. Each person has a *fitness*. This starts at zero and increases by 10% for each good gene. (Fitness with 5 good genes is $1.61051=(1.1)^5$.)
3. At the end of each generation everyone dies and $N$ new people are born. These new people have one parent, chosen based on fitness--- the probability of an individual being selected as a parent is their fitness divided by total population fitness. (If $3$ people have fitness $1,2,5$, their chances of being a parent are $1/8$, $2/8$, and $5/8$.)
4. The child's genes are copied from the parent. Then mutations happen: Each good gene has a 2% chance to become bad, while each bad gene has a 0.1% chance to become good.

That's it. That's the entire model. (If you're a programmer, you might like to look at <a href="#code">the code</a> later in this page.)

You could change most of the details without really changing our conclusions below. But there's one that's very important: We assume that bad mutations are more common than good ones.

## One asexual generation

To understand this better, let's visualize a single generation. Here I generate a large population where each person has between 45 and 55 good genes. We first choose the number of genes, then the genes.

<a href="/img/sex/single_iter_asexual.svg"><img src="/img/sex/single_iter_asexual.svg" alt="visualization of a single generation of asexual reproduction" width="480" style="display: block; margin: 0 auto;" /></a>

Simple enough, right? We started with a uniform distribution over good genes in the 45-55 interval. People reproduce with probability proportional to their fitness. So, before mutations, the distribution for kids looks just like the parent distribution times the fitness function. Finally, mutations add a bit of "noise".

## Sexual reproduction

Now, what if we have sexual reproduction? We will make two small changes:
* Each person has **two parents**. These are chosen in the same way based on their fitness. Any two people can be parents.
* Instead of just copying genes from one parent, each gene is **randomly chosen from the same location in one of the two parents**.

Obviously there's tons of complexity in real sexual reproduction that isn't present here. For one thing, there are no males and females--- anyone can reproduce with anyone, including themselves. The real world has much more complex genes, fitness, geographical effects, etc. My defense is: That's the point of a model, friend! We want the simplest system that displays the behavior we are trying to understand. If it's possible to simply something, we should, so I did.

## One sexual generation

Let's do the same visualization of a single generation, but now with sexual reproduction.

<a href="/img/sex/single_iter_sexual.svg"><img src="/img/sex/single_iter_sexual.svg" alt="visualization of a single generation of sexual reproduction" width="480" style="display: block; margin: 0 auto;" /></a>

# Results

OK, so what happens if we run the model? Here are the results with $N=100000$ people and $G=100$ genes, using asexual reproduction:

<video width="480" height="320" autoplay loop style="display: block; margin: 0 auto;">
    <source src="/img/sex/asexual.mp4" type="video/mp4"/>
    <source src="/img/sex/asexual.webm" type="video/webm"/>
</video>

And here is what it looks like if we use sexual reproduction:

<video width="480" height="320" autoplay loop style="display: block; margin: 0 auto;">
    <source src="/img/sex/sexual.mp4" type="video/mp4"/>
    <source src="/img/sex/sexual.webm" type="video/webm"/>
</video>

The following plot summarizes what happens over time. In each generation, we compute the mean number of good genes in the population. This is plotted as a line. The light shaded areas show one standard deviation.

<a href="/img/sex/fitness0.svg"><img src="/img/sex/fitness0.svg" alt="time course of evolution under sexual and asexual reproduction starting at 0" width="480" style="display: block; margin: 0 auto;" /></a>

Why does evolution stall out with less than all good genes? The answer is that the more good genes there are, the more opportunities for bad mutations to make things worse. Meanwhile, selection pressure is trying to increase the number of good genes. Eventually these two reach a balance, and things "stall".

If you like, we can run the same experiment, but starting everyone with all good genes, rather than all bad. Now there's a slow process of decay, but it ends up at pretty much the same point.

<a href="/img/sex/fitness1.svg"><img src="/img/sex/fitness1.svg" alt="time course of evolution under sexual and asexual reproduction starting at 0" width="480" style="display: block; margin: 0 auto;" /></a>

# What the hell is happening?

So far, all we've done is invent a very simple model of (a)sexual reproduction, and we've observed that sexual reproduction works better.

OK, but why? *Why does it work better*?

It really isn't very obvious. Even the simple model I have is surprisingly tricky to study mathematically. (I think )

 While avoiding too much math, I think has a two-part answer:

1. Sexual reproduction *increases variance*.
2. Variance improves *future* generations.

Let's look at these one at a time.

## Recall single generations

Look back at the visualizations of a single generation of <a href="#one-asexual-generation">asexual</a> and <a href="#one-sexual-generation">sexual</a> reproduction. For your convenience, here is the distribution for the next generation under asexual reproduction (top) and sexual (bottom):

<div style="overflow:hidden; width:480px; display: block; margin: 0 auto;">
   <img src="/img/sex/single_iter_asexual.svg" alt="" style="margin:-93% 0px 0% 0px;" />
</div>
<div style="overflow:hidden; width:480px; display: block; margin: 0 auto;">
   <img src="/img/sex/single_iter_sexual.svg" alt="" style="margin:-93% 0px 0% 0px;" />
</div>

This is puzzling. The mean under sexual reproduction *isn't higher*. 

At first, this is puzzling. The mean for the children under sexual reproduction is nearly the same as under asexual. If the mean isn't better, why should sexual reproduction work better?

This has a two-part answer:

## Sexual reproduction increases variance

That has a two part answer:
* Sexual reproduction creates more variance.
* Variance leads to a higher mean in future generations.

The difference is variance. The new generation has, on average, very nearly the same number of good genes as under asexual reproduction. But there is much more variance. You can see this from comparing the lines plotting the standard deviation. You can also observe that under asexual reproduction, *no child* had more than 56 good genes. With sexual reproduction, there can be as many as 60.

Why does sexual reproduction increase variance? Take a simple situation where $N=2$ and $G=10$ Suppose the previous generation has these gene strings:

> 0000011111
> 1111100000

Suppose we generate 

## Variance leads to better genes in future generations

What's going on here? Somehow the population that reproduces sexually reaches a much higher percentage of good genes.



# horizontal gene transfer



# Code

## For understanding

Now, here's some Python code that will simulate the model. This version is slow, but is intended to be easy to understand. Think of this as a formal specification of the model, if you will.

```python
import numpy as np
from numpy.random import choice, rand, randint

def mutate(x):
    x_old = x.copy()
    x[(x_old==0) * (rand(G)<.001)] = 1      # good mutation
    x[(x_old==1) * (rand(G)<.020)] = 0      # bad mutation
    return x

def sexual_mix(x,y):
    choice = np.random.randint(0,2,len(x))
    return choice*x + (1-choice)*y

def sim_slow(N,G,num_generations,sexual=False):
    X = [np.zeros(G) for n in range(N)]    # initial population

    for gen in range(num_generations):
        fit = [np.prod(1.10**x) for x in X
        prob = np.array(fit) / np.sum(fit) # prob of being parent

        if sexual:
            parents1 = [choice(N,p=prob) for n in range(N)] 
            parents2 = [choice(N,p=prob) for n in range(N)]
            X = [sexual_mix(X[par1],X[par2]) for \
                (par1, par2) in zip(parents1,parents2)]
        else:                              # asexual
            parents = [choice(N,p=prob) for n in range(N)]
            X = np.array(X)[parents]

        X = [mutate(x) for x in X]
```

## For efficiency

Here's a version that plays tricks with NumPy to make things faster. Use this if you actually want to run the model.  While this is shorter, it's *far* more subtle due to all the array operations. So I recommend the above code if you're trying to *understand* the model.


```python
import numpy as np
from numpy.random import choice, rand

def sim(N,G,num_generations,sexual=False):
    X = np.zeros([N,G]) # initial population

    for gen in range(num_generations):
        fitness = np.prod(1.10**X,axis=1)

        # probability of being a parent
        prob = np.array(fitness)
        prob /= np.sum(prob)
        
        if sexual:
            parent1 = choice(N,N,p=prob)
            parent2 = choice(N,N,p=prob)
            choice = np.random.randint(0,2,X1.shape)
            X = choice*X[parent1] + (1-choice)*X[parent2]
        else:
            parent = choice(N,N,p=prob)
            X = X[parent]
        
        X_old = X # save temp copy
        X[(X_old==0) * (rand(N,G)<.001)] = 1
        X[(X_old==1) * (rand(N,G)<.020)] = 0
```
