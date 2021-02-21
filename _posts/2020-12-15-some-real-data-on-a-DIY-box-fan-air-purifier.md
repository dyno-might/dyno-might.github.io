---

layout: post
title: "Experiments on a $50 DIY air purifier you can make in 30s"
image: /img/purifier/smoke.jpg
description: You can make a DIY air purifier in 30s. To test if it works, I generated smoke, and measured how well it removes tiny particles.
tags: science

---

<head>
<style>
.figure {
  display: block;
  margin-left: auto;
  margin-right: auto;
  max-width: 70%
}
</style>
</head>

Bad air is bad for you. The air purifier market, though, is a mess. Every purifier uses incompatible proprietary filters, presumably to lock you into buying replacements. How do we know these actually work? Few seem to publish lab tests. And why does it cost $100-$300 for a big plastic box with a fan and a filter inside?

It's common to build DIY air purifiers by basically strapping a filter to a fan. I like the idea of these, but again, it's hard to be confident they really work. There's a few experiments out there, but not enough to make me comfortable. So I decided to do some experimenting of my own. I made a purifier, generated smoke, and measured how well it removes tiny particles.

# TL;DR: YES IT WORKS

If you're in a hurry, this post says that if you strap two HEPA filters to a box fan, it will clear the air of basically all the particles we can measure, and it will do it faster than a commercial filter that costs twice as much.

![in a large room the DIY filter does slightly better than the commercial filter](/img/purifier/smallroom_log.jpg)

# The experiment

### DIY purifier

My DIY purifier was *very* simple. (I don't want to promote any particular brands here. Contact me if you want the exact products.)

* A standard box fan. (Cost: $19)
* Two HEPA air filters, each approximately 32 cm x 22 cm and 5cm thick. (Cost: $35 for both)
* A bungie cord. (Cost: Free)

Assembly takes about 30s. You put the filters on the intake side of the fan and strap them on with the bungie cord. Here's a picture:

<div class="figure"><img src="/img/purifier/filter_notape.jpg" alt="DIY purifier" max-width="60%" min-width="35%" /></div>

Timeless elegance and grace, it is not. I get the shakes just looking at that bit of crinkled filter.

### Commercial purifier

As a comparison, I got a $100 air purifier from a well-known brand that's intended for small rooms. It uses uses a single HEPA filter that's about 25cm x 12cm and 4cm thick. Replacement filters currently cost around $25.

### Smoke

It's surprisingly hard to repeatedly generate a consistent amount of smoke. I tried burning various things (paper, cardboard) and found that the number of particles generated can vary by an order of magnitude, depending on the burn pattern. This is difficult to control and effectively random.

Ideally, I'd have liked to burn some food product like oil, since the kitchen is usually the biggest source of indoor air pollution. I couldn't figure out a good way of doing this, either: You'd need to have the same amount of oil distributed in the same way and heated to the same temperature.

I finally settled on using incense. I cut sticks to the length of a standard credit card and then attached the ends horizontal to the ground. This seemed to be pretty consistent. In retrospect, I bet that burning toast in a toaster would work well. (I didn't have one on hand.)

### Measurements

I borrowed a cheap-ish ($100) air quality monitor from a friend. I think it's made by some company in China and then re-sold by various white-label brands. I can't figure out who the original manufacturer is. Based on data I've seen for the reliability of other air quality monitors, I wouldn't trust the absolute numbers, but the I think the *relative* measurements should still be OK.

The typical measurement for particulate pollution is "PM 2.5" which is in units of μg/m³. This is intended to measure what you'd get if you did the following:
* Take a cubic meter of air.
* Filter all the solid particles out of the air.
* Keep only the solid particles that are are 2.5 micrometers (μm) or smaller.
* Weigh all the particles you kept in micrograms (μg).

Here are some ways to interpret these numbers:
* The EPA says yearly averages should be below 12 and daily averages below 35.
* The average outdoor level ranges from 6 in Finland to almost 100 in Nepal. Rich countries are typically under 15. The highest levels are typically found in Asia and Africa.
* Cooking can easily cause PM 2.5 measurements to spike into the hundreds. I've observed myself that this can happen with only a small amount of visible smoke.

### Logging

Since the air quality monitor doesn't log data, I used an ultra-hacky alternative: I set the monitor next to a laptop running a stopwatch. I then aimed a tabet at both of those screens and took a timelapse video. Finally, I manually transcribed the data by going to each minute marker in the data. (This was even more tedious than it sounds.)

# Results in a Tiny Room

I ran a first experiment in a tiny room of around 8 ㎥. Due to worries that wind from the purifiers might change the speed the incense burned, I placed it on the opposite side of a wall, with a gap of around 20 cm near the ceiling.

<div class="figure"><img src="/img/purifier/setup_tinyroom.jpg" alt="tiny room setup" /></div>

I repeated the experiment once with no filter, once with a commercial filter, and once with the DIY filter. Here are the results:

![smallroom measurements in linear space](/img/purifier/smallroom_linear.jpg)

Things are a bit random around the beginning, probably due to the drifting of the smoke before it's equalized in the room. With no filter at all, this spikes all the way to 1000 μg/m³, the maximum the instrument can show.

If we make the y-axis logarithmic, it becomes quite clear that the DIY filter is cleaning the air at a better rate. (This is the picture from the top of this page.)

![smallroom measurements in log space](https://dyno-might.github.io/img/purifier/smallroom_log.jpg)

If we take the EPA's threshold of 12 μg/m³, the DIY filter gets there in around 15 minutes, while the commercial filter take around 25 minutes.

# Results in a Large Room

Thankfully, I don't spend most of my time in an 8 ㎥ room. Thus, I repeated the experiment in a large room of around 100 ㎥. Here there was no wall between incense and purifier. Instead I left around a meter of distance between the incense and purifier and the purifier and the monitor.

<div class="figure"><img src="/img/purifier/setup_largeroom.jpg" alt="large room setup" /></div>

Here are the results:

![large room measurements in linear space](/img/purifier/largeroom_linear.jpg)

There's even more randomness around the beginning, probably just due to how the smoke drifts around. Based on the room volume we'd expect a peak concentration with no filter of around 80 μg/m³ = 1000 μg/m³ * (8/100). Reassuringly, this is pretty close to what we see.

The DIY purifier looks a bit better. If we plot in log space, it's more clear that it is indeed filtering at a better rate:

![large room measurements in log space](https://dyno-might.github.io/img/purifier/largeroom_log.jpg)

# Taping

It's common advice for DIY purifiers like this to seal around the edges of the filter so that all air must pass through it.  I share the intuition that this would help, but it's hard to be sure: If you block airflow, you slow down the fan. This could be counterproductive.

In this case at least, experiment is easier than theory. I took packing tape and carefully sealed around the intake side.

<div class="figure"><img src="/img/purifier/filter_tape.jpg" alt="DIY purifier with tape" max-width="60%" min-width="35%" /></div>

And the results are...

![taping around the filter has no effect](/img/purifier/taping.jpg)

...nothing!?

This was unexpected. I thought the tape would help, but I wouldn't have been surprised if it hurt instead. Instead, there's basically no difference at all. I don't know enough about fluid dynamics to even speculate about what's happening here, so I won't try.

There could be some weird quirk in how I ran this experiment. This doesn't necessarily mean that all the advice to tape around the filter is *wrong*. However, I've never seen any experriments that show taping helps either.

# Thoughts

**Cost.** The DIY purifier isn't dramatically cheaper than the commercial one, but I expect the filters would need to be replaced much less often. The commercial purifier uses a single filter with an area of 300 cm², whereas the DIY purifier uses two filters with a total area of around 1400 cm², and also slightly thicker. It's reasonable to assume the DIY filters could remove ~4 times as many particles before replacement.

**Durability.** One concern is that box fans aren't meant to be used with filters attached and could wear out. This is reasonable. However, box fans are much cheaper than commercial purifiers, and I've been using this particular fan with various filters attached for several years now without issue.

**Electricity.** The cost of electricity is another factor. Typical box fans seem to use around 55W, whereas commercial purifiers typically use 30-45W. If electricity costs $0.13 / kWh, the box fan would cost around $62 to operate 24 hours a day for a year, while a 30-watt purifier would cost around $34. Obviously, these numbers decrease if you run the purifier less. Some (more expensive) commercial purifiers have air quality sensors built in and automatically turn on only when needed.

**MERV or HEPA?** Most people who build box-fan purifiers use [MERV](https://en.wikipedia.org/wiki/Minimum_efficiency_reporting_value)-rated filters intended for furnaces. Commercial air purifiers use [HEPA](https://en.wikipedia.org/wiki/HEPA)-rated filters. Roughly speaking, HEPA filters are "better" in that they are rated to remove a higher percentage of particles in one pass. It's not clear that HEPA filter will actual perform better when attached to a fan, though: A filter that catches fewer particles in one pass might still be better if it allows for faster airflow.

**That one video.** If you're reading this article after it was linked from some forum, I'd bet you that someone in the comments links to [this video](https://www.youtube.com/watch?v=kH5APw_SLUU) from the Michigan Sinus Center. I found this inspirational, but note a couple of things: First, while the description says they use HEPA filter, the video clearly indicates a MERV filter. Again, that's not necessarily bad! They claim that around 90% of particles sized 0.3 microns are larger are eliminated in a single pass. That's good, but not totally reassuring. The question is, does it remove 99% in two passes? If 90% of the particles in the ambient air were large and the filter only catches large particles, then additional passes would never get rid of the most dangerous small particles. This is why I trust HEPA filters a bit more: since they remove almost all particles in one pass, I'm confident they should remove almost all particles eventually. This is also why I strongly prefer experiments that actually measure particles removed from the air in a room, rather than just the air coming out of the purifier.

**Further questions.** There's a lot of things that further experiments could look at:

1. Does the fan speed make a huge difference?
2. How does the purifier compare to larger commercial purifiers?
3. How do MERV-rated furnace-type filters compare under the same conditions?
4. How can it not matter if there's tape around the filters!?
5. Does fan speed matter? (I always ran the box fan at maximum speed.)
6. Is it better to put the filters on the intake or outtake side of the fan? Intuition suggests the intake side, but as we've seen, surprises happen.

**On purifiers and health.** If the outside air is clean where you live, your first priority probably shouldn't be to get an air purifier. Instead, I'd recommend you *be careful when cooking*. Having an air quality monitor around really drives home how even small amounts of cooking smoke can cause gigantic spikes in particulate levels. For most people, *not creating* these particles in the first place is the best strategy. Try not to create any smoke at all. If you have a range hood that vents outside, use it! If you do create smoke, open windows immediately. One difficulty is that it's actually quite hard to guess how many particulates you've created. There's a reasonable case that you should spend your money on an air-quality monitor before a purifier.

**Incense.** It's probably bad for you. I'd avoid it.
