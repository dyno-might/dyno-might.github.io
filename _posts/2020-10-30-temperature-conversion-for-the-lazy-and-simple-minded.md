---
layout: post
title: "Temperature conversion for the lazy and simple-minded"
image: /img/convert/thermometer.jpg
tags: science math
---

This is a new way to convert temperatures between Celsius and Fahrenheit. It's *bad*. You shouldn't use it if you have any other option.

If you want a little bit of a puzzle, here is the system as a plot:

![conversion as lines](/img/convert/convert.png)

Did you figure it out? Here's the system in words:

> For the numbers 4, 16, and 28, transposing digits switches from Celsius from Fahrenheit.

If you want even more explanation, here's the system as a diagram:

![conversion as transposition](/img/convert/transpose.png)

It's a coincidence that these conversion points exist. It's an even greater coincidence that they divide the range of temperatures in a convenient way.

Range in C | Range in F | Description
-|-|-
Less than 4°C | Less Than 40°F | Cold
Between 4°C and 16°C | Between 40°F and 61°F | Cool
Between 16°C and 28°C | Between 61°F and 82°F | Warm
More than 28°C | More than 82°F | Hot

As an example, suppose you are familiar with Celsius and don't know how to interpret 71°F. Since this is around halfway between 61°F and 82°F you know it is also about halfway between 16°C and 28°C.

# Questions

**Question:** Did you lie a little bit about the numbers?

**Answer:** Yes, but by less than 1°F.

**Question:** Don't I have to remember "4, 16, 28"?

**Answer:** Yes. But it's not that hard! You have 4, then 4 + 12, and 4 + 12 + 12.

**Question:** Isn't this a bad system for me, smart person who can easily calculate F=(9/5)C + 32 and C=(5/9)(F - 32) in my head?

**Answer:** Yes.

**Question:** How do I use this system to convert other temperatures?

**Answer:** You don't.



