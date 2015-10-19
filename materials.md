---
layout: post
title: Materials
---

The slides for the lessons can be found here:  

{% for slide in site.data.materials.slides %}
{% if slide.published %}
   [{{ slide.number }}. {{ slide.name }}]({{ slide.url }}){:target="_blank"}
{% endif %}
{% endfor %}
