---
layout: post
title: "The simplest possible way to convert Celsius and Fahrenheit"
image: /img/convert/thermometer.jpg
description: If you can switch the order of two numbers, you can convert temperatures.
tags: science math
permalink: /:year/:month/:day/:title/
seo:
  date_modified: 2022-02-18
category: "math"
head: "<style>
img{
    display:block;
    margin-left: auto;
    margin-right: auto;
    max-width:min(100%,400pt);
    max-height:400px;
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
  font-size: 2.8vw;
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

This is a new way to convert temperatures between Celsius and Fahrenheit. It's not the most accurate method, but it's surely the easiest.

If you want a puzzle, here is the system as a cartoon:

![conversion as lines](/img/convert/convert.svg)

Did you figure it out? Here's the system in words:

<span style="font-size:110%; font-weight:bold;">For the numbers 4, 16, and 28, transposing digits switches from Celsius from Fahrenheit.</span>

If you want even more explanation, here's the system as a diagram:

![conversion as transposition](/img/convert/transpose.svg)

It's a coincidence that these conversion points exist---I found them by writing a program and searching for all the cases where this happen. It's an very fortunate coincidence that they divide the range of temperatures in a convenient way.

Range in C | Range in F | Description
-|-|-
< 4°C | < 40°F | Cold
4°C - 16°C | 40°F - 61°F | Cool
16°C - 28°C | 61°F - 82°F | Warm
> 28°C | > 82°F | Hot

As an example, suppose you are familiar with Celsius and don't know how to interpret 71°F. Since this is around halfway between 61°F and 82°F you know it is also about halfway between 16°C and 28°C.

# Questions

**Question:** Did you lie a little bit about the numbers?

**Answer:** Yes, but by less than 1°F.

**Question:** Don't I have to remember "4, 16, 28"?

**Answer:** Yes. But it's not that hard! You have 4, then 4 + 12, and 4 + 12 + 12.

**Question:** Isn't this a bad system for me, smart person who can easily calculate F=(9/5)C + 32 and C=(5/9)(F - 32) in my head?

**Answer:** Probably yes.

**Question:** How do I use this system to convert other temperatures?

**Answer:** You can mentally interpolate: For example, 7°C is ¼ of the way from 4°C to 16°C, so it converts to around 45°F, ¼ of the way from 40°F and 61°F.
