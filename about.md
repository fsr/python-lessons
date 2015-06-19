---
layout: page
title: About
permalink: /about/
---

This site hosts the exercises for the fsr python lessons. Sources can be found on [GitHub](https://github.com/fsr/python-lessons/tree/gh-pages)


Modules and concepts this course wants to teach:
{% for target in site.data.overview.targets %}
- {{ target }}
{% endfor %}
