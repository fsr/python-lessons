---
layout: post
title: Materials
---

The slides for the lessons can be found here:  

{% for slide in site.data.materials.slides %}
{% if slide.published %}
[{{ slide.number }}. {{ slide.name }}]({{ slide.url }}){:target="_blank"}
{% else %}
<del>{{ slide.number }}. {{ slide.name }}</del>
{% endif %}
{% endfor %}

**The solutions of the exercises can be found at [GitHub](https://github.com/Feliix42/python-solutions)**
