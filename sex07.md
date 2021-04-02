---

layout: post
title: "Why sex?"
image: /img/sex/stamen3.jpg
hero_light: true
tags: science explainer
usemathjax: true

---

Life reproduces and evolves. We all know the story: During reproduction, mutations sometimes happen. If those mutations increase reproductive fitness, they tend to stick around. If they decrease fitness they tend not to.

Fine, but why reproduce *sexually*? Why mix the genes of two parents? Life obviously goes to great lengths to make this happen, so what's the advantage?

The answer wasn't obvious to Darwin. He said, "...why new beings should be produced by the union of the two sexual elements. The whole subject is as yet hidden in darkness."

Today, we're given a justification in school as children. Something like: Combining genes from parents creates more individual differences and speeds up the pace of evolution. That's fine, but the details are fuzzy. *How* does it create more differences? *How* does it speed up evolution?

Let's start from first principles. We'll build a simple model of reproduction, and try to figure out the answer ourselves.

* auto-gen TOC:
{:toc}

# The model

Here's a simple model of asexual reproduction:

1. There are $$N$$ people. Each person's genes are a binary string of length $$G$$. Each gene is either *good* or *bad*.
2. Each person has a *fitness*. This starts at one and increases by 10% for each good gene. (Fitness with 5 good genes is 1.61=(1.1)⁵.)
3. At the end of each generation everyone dies and $$N$$ new people are born. These new people have one parent, chosen based on fitness--- the probability of being selected as a is fitness divided by total population fitness. (If three people have fitness 1, 2, and 5, their chances of being a parent are ⅛, ¼, and ⅝.)
4. The child's genes are copied from the parent. Then mutations happen: Each good gene has a 2% chance to become bad, while each bad gene has a 0.1% chance to become good.

That's it. That's the entire model. (You can read a formal specification as <a href="#mathematical-specification">math</a> or <a href="#code-for-reading">Python code</a> later in this page if you want.)

You could change most of the details without really changing our conclusions below. But there's one that's very important: We assume that bad mutations are more common than good ones.

## One asexual generation

To understand this better, let's visualize a single generation. Here I generate a large population where each person has between 45 and 55 good genes. We first choose the number of genes, then the genes.

<a href="/img/sex/single_iter_asexual.svg"><img src="/img/sex/single_iter_asexual.svg" alt="visualization of a single generation of asexual reproduction" width="480" style="display: block; margin: 0 auto;" /></a>

Simple enough, right? We started with a uniform distribution over good genes in the 45-55 interval. People reproduce with probability proportional to their fitness. So, before mutations, the distribution for kids looks just like the parent distribution times the fitness function. Finally, mutations add a bit of "noise".

## One sexual generation

Now, what if we have sexual reproduction? We will make two small changes:
* Each person has **two parents**. These are chosen in the same way based on their fitness. Any two people can be parents.
* Instead of just copying genes from one parent, each gene is **randomly chosen from the same location in one of the two parents**.

Let's do the same visualization of a single generation, but now with sexual reproduction.

<a href="/img/sex/single_iter_sexual.svg"><img src="/img/sex/single_iter_sexual.svg" alt="visualization of a single generation of sexual reproduction" width="480" style="display: block; margin: 0 auto;" /></a>

What's changed is the distribution of children pre mutation. Since kids are a mix of two parents, this is no longer looks like the parent distribution times the fitness function. Instead it's more of a bell curve.

# Results

OK, so what happens if we run the model? Here are the results with $$N=100000$$ people and $$G=100$$ genes using asexual reproduction, where the first generation starts with all bad genes:

<video width="480" height="320" autoplay loop style="display: block; margin: 0 auto;">
    <source src="/img/sex/asexual.mp4" type="video/mp4"/>
    <source src="/img/sex/asexual.webm" type="video/webm"/>
</video>

And here is what it looks like if we use sexual reproduction:

<video width="480" height="320" autoplay loop style="display: block; margin: 0 auto;">
    <source src="/img/sex/sexual.mp4" type="video/mp4"/>
    <source src="/img/sex/sexual.webm" type="video/webm"/>
</video>

The following plot summarizes what happens over time, with the means shown as lines and the standard deviations as shaded areas:

<a href="/img/sex/fitness0.svg"><img src="/img/sex/fitness0.svg" alt="time course of evolution under sexual and asexual reproduction starting at 0" width="480" style="display: block; margin: 0 auto;" /></a>

Why does evolution stall out before reaching all good genes? The answer is *genetic load*. The more good genes there are, the more opportunities for bad mutations to make things worse. Meanwhile, selection pressure is trying to increase the number of good genes. Eventually these two reach an equilibrium and things stall.

If you like, we can run the same experiment, but starting everyone with all good genes, rather than all bad. Now there's a slow process of decay, but it ends up at pretty much the same point.

<a href="/img/sex/fitness1.svg"><img src="/img/sex/fitness1.svg" alt="time course of evolution under sexual and asexual reproduction starting at 0" width="480" style="display: block; margin: 0 auto;" /></a>

# What is happening?

So far, all we've done is invent a very simple model of (a)sexual reproduction, and we've observed that sexual reproduction works better.

OK, but why? *Why does it work better*?

## Recall single generations

Look back at the visualizations of a single generation of <a href="#one-asexual-generation">asexual</a> and <a href="#one-sexual-generation">sexual</a> reproduction. For your convenience, here is the distribution for the next generation under asexual reproduction (top) and sexual (bottom):

<div style="overflow:hidden; width:480px; display: block; margin: 0 auto;">
   <img src="/img/sex/single_iter_asexual.svg" alt="" style="margin:-93% 0px 0% 0px;" />
</div>
<div style="overflow:hidden; width:480px; display: block; margin: 0 auto;">
   <img src="/img/sex/single_iter_sexual.svg" alt="" style="margin:-93% 0px 0% 0px;" />
</div>

This is puzzling. The mean under sexual reproduction *isn't higher*. Yet we already saw it reaches a much better equilibrium. So what the hell is going on here?

While avoiding math, this has a two-part answer:

1. Sexual reproduction *increases variance*.
2. Variance improves *future* generations.

Let's look at these one at a time.

## Sexual reproduction increases variance

The difference is variance. The new generation has, on average, very nearly the same number of good genes as under asexual reproduction. But there is much more variance. You can see this from comparing the lines plotting the standard deviation. You can also observe that under asexual reproduction, *no child* had more than 56 good genes. With sexual reproduction, there can be as many as 60.

Why does sexual reproduction increase variance? Take a simple situation where $$G=10$$, $$N$$ is huge, and everyone in the previous generation has exactly 5 good genes. Write 0 for bad genes and 1 for good. If we generate children by asexual reproduction, they look like this:

```
  genes       # good genes
0100011011      5
0101001101      5
0110110010      5
0011011000      4
1000111100      5
0000111110      5
1101100000      4
0011011001      5
0110101010      5
1101001101      6
```

The average number of good genes is 4.905. Most children (about 90%) have 5. A few have 4. It's rare to have 6, and *really* rare to have more than 6.

<!--
4.905 = .98*5 + .002*5
-->

<!--
Around 90% of children have 5 good genes, around 9.5% will have 4 or fewer , around 0.45% will have 6. It's *really* rare to have more than 6.
-->

Meanwhile if we generate children by sexual reproduction, they look like this:

```
  genes       # good genes
0101011011      6
1011000011      5
0010000101      3
1000111010      5
1000100001      3
0111001100      5
1011010101      6
0001010110      4
0000101101      4
0110111111      8
```

The mean is the same: 4.905. But there's much more variability. Only around 35% of children have exactly 5 good genes, and kids varying by 2 are more are reasonably common.

It's easy to see why. Suppose you have two parents:

```
parent A: 1110011000
parent B: 1000011110
```

If the child's genes are chosen according to the pattern `AAAAABBBBB`, before mutation they would have a string of `1110011110` with 7 good genes. If the child's genes are chosen according to the pattern of `BBBBBAAAAA` they would have `1000011000` with only 3 good genes.

## Variance leads to better genes in future generations

What's going on here? Somehow the population that reproduces sexually reaches a much higher percentage of good genes.

<a href="/img/sex/second_iter_asexual_asexual.svg"><img src="/img/sex/second_iter_asexual_asexual.svg" alt="visualization of a second generation of asexual reproduction" width="50%"  /></a><a href="/img/sex/second_iter_sexual_sexual.svg"><img src="/img/sex/second_iter_sexual_sexual.svg" alt="visualization of a second generation of sexual reproduction" width="50%" /></a>

<!--
Explain rest in words, move rest to supplement
-->

<a href="/img/sex/second_iter_asexual_asexual.svg"><img src="/img/sex/second_iter_asexual_asexual.svg" alt="visualization of a second generation of asexual reproduction" width="50%"  /></a><a href="/img/sex/second_iter_asexual_sexual.svg"><img src="/img/sex/second_iter_asexual_sexual.svg" alt="visualization of a second generation of sexual reproduction" width="50%" /></a>

<a href="/img/sex/second_iter_sexual_asexual.svg"><img src="/img/sex/second_iter_sexual_asexual.svg" alt="visualization of a second generation of asexual reproduction" width="50%"  /></a><a href="/img/sex/second_iter_sexual_sexual.svg"><img src="/img/sex/second_iter_sexual_sexual.svg" alt="visualization of a second generation of sexual reproduction" width="50%" /></a>



# Discussion

<!--
Cut this?
-->
## Complaints about this model

Obviously there's tons of complexity in real sexual reproduction that isn't present here. For one thing, there are no males and females--- anyone can reproduce with anyone, including themselves. You might also complain about genes being binary or non-diploid, the simplistic fitness function, or that there's no notion of geography. My defense is: That's the point of a model, friend! We want the simplest system that displays the behavior we are trying to understand. If it's possible to simply something, we should, so I did.

## What this explanation is missing

(Correlations between genes.)


## horizontal gene transfer

# Formal specification of the model

Not satisfied with an English-language description of the model? Here you can read it as Python code, as faster-but-more-confusing Python code, or specified mathematically.

## Code for reading

Now, here's some Python code that will simulate the model. This version is slow, but is intended to be easy to understand. Think of this as a formal specification, similar to the mathematical model above.

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

## Code for running

Here's a version that plays tricks with NumPy to make things faster. Use this if you actually want to run the model.  While this is shorter, it's far more subtle due to all the array operations. So I recommend the above code if your goal is just to *understand* the model.


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
## Mathematical specification

* There are $$N$$ people.

* The generations are numbered by $$k=1, 2, \cdots, K$$.

* At generation $$k$$, the people are $$x^{k1}, \cdots, x^{kN}$$. 

* Each person's genes are a binary string of length $$G$$. That is, $$x^{kn} = (x^{kn}_1, \cdots, x^{kn}_G)$$, where $$x^{kn}_g \in \{0,1\}$$.

* The fitness of a person is $$f(x) = \prod_{g=1}^G (1.1)^{x_g}$$.

* The probability that person $$n$$ is selected as a parent in generation $$k$$ is $$\theta^k_{n} = f(x^{nk}) / \sum_{m=1}^N f(x^{mk})$$.

* If doing asexual reproduction:
    
    * For each new person $$n$$ at timestep $$k>1$$, their parents $$p^k_n$$ are chosen as $$p^k_n \sim \mathrm{Categorical}(\theta^{k-1})$$.

    * The pre-mutation genes for the next generation are a copy of the parent, i.e. $$y^{kn} = x^{(k-1) p^k_n}$$.

* If doing sexual reproduction

    * For each person $$n$$ at generation $$k>1$$ there are two parents $$p^k_n$$ and $$q^k_n$$. These are chosen as $$p^k_n \sim \mathrm{Categorical}(\theta^{k-1})$$ and $$q^k_n \sim \mathrm{Categorical}(\theta^{k-1})$$.

    * For each person $$n$$ and gene $$g$$ at generation $$k>1$$, the pre-mutation gene is chosen randomly from one of the two parents

    $$ y^{kn}_g = C x^{(k-1) p^k_n}_g + (1-C) x^{(k-1) q^k_n}_g, C \sim \mathrm{Bernoulli}\left(\frac{1}{2}\right).$$
    
* Finally, mutations are applied. For each $$k>1$$, $$n$$, and $$g$$,

$$x^{kn_g} \sim \begin{cases} \mathrm{Bernoulli}(.001) & \text{ if } y^{kn}_g=0 \\ \mathrm{Bernoulli}(.98) & \text{ if } y^{kn}_g=1
    \end{cases}.$$
