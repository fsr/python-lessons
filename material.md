---
layout: post
title: Materials
permalink: /materials/
---

The slides for the lessons can be found here:  

{% for slide in site.data.materials.slides %}
[{{ slide.number }}. {{ slide.name }}]({{slide.url}}){:target="_blank"}
{% endfor %}
