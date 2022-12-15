---
layout: page
title: DYNOMIGHT CATEGORIES
subtitle: 
image: /img/deathvalley/small.jpg
hero_image: /img/deathvalley/small.jpg
hero_height: is-large
hide_hero: True
permalink: /categories/
---

{%- for post in site.pages -%}
    {%- if post.is_category_page -%}
        <br>
        <a href="{{post.url}}" class="headerfont">{{post.title}}</a>
    {%- endif -%}
{%- endfor -%}