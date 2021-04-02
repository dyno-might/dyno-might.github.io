---

layout: post
title: "Why sex?"
image: /img/writing/typewriter.jpg
tags: writing
hero_light: true
tags: science explainer

---

Life reproduces and evolves. We all know the story: During reproduction, mutations sometimes happen. If those mutations increase reproductive fitness, they tend to stick around. If they decrease reproductive fitness they don't.

That's all good. But why reproduce *sexually*? Why mix the genes of two parents?

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

<a href="/img/sex/single_iter_asexual.svg"><img src="/img/sex/single_iter_asexual.svg" alt="visualization of a single generation of asexual reproduction" width="320" style="display: block; margin: 0 auto;" /></a>

Simple enough, right? We started with a uniform distribution over good genes in the 45-55 interval. The probability of someone being a parent is proportional to their fitness. Thus, before mutations, the distribution for kids looks just like the fitness function on the 45-55 interval. Finally, mutations add a bit of "noise".

## Sexual reproduction

Now, what if we have sexual reproduction? In this case, we make two small changes:
* Each person has **two** parents. These are chosen in the same way. Any two people can be parents.
* Instead of just copying genes from one parent, each gene is randomly chosen from the same location in one of the two parents.

Obviously there's tons of complexity in real sexual reproduction that isn't present here. For one thing, there are no "males" and "females"--- anyone can mate with anyone, including themselves. Genes aren't binary, fitness is more complicated, there's geographical effects, blah, blah, blah. My defense is: That's the point of models, friend. We want the simplest possible system that shows the behavior we are looking for. If it's possible to exclude something, we should, so I did.

## One sexual generation

Here I run the same experiment as above but now with sexual reproduction instead of asexual.

<a href="/img/sex/single_iter_sexual.svg"><img src="/img/sex/single_iter_sexual.svg" alt="visualization of a single generation of sexual reproduction" width="320" style="display: block; margin: 0 auto;" /></a>

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

![](/img/sex/fitness0.png)

In each generation, we compute the percentage of good genes for each person. The lines show the mean over all people. The light shaded areas show the 5% - 95% quantiles. The darker shaded areas show the 25% - 75% quantiles.

What's going on here? Somehow the population that reproduces sexually reaches a much higher percentage of good genes.

We can also run a simulation where everyone starts with all good genes.

![](/img/sex/fitness1.png)

Think of it this way. Suppose every individual had 

# Code

Now, here's some Python code that will simulate the model. This version is slow, but is intended to be easy to understand.

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

Here's a version that plays tricks with NumPy to make things faster. While this is shorter, it's far more subtle due to all the array operations. So while this is what you'd want to actually run, I recommend the above code if you're trying to *understand* the model.


```python
import numpy as np
from numpy.random import choice, rand

def sim(N,G,num_generations,sexual=False):
    X = np.ones([N,G]) # initial population

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
