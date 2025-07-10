---
layout: default
title: Home
---
# Welcome to My Data Science Portfolio

## Featured Projects
{% for project in site.projects %}
<div class="project-card">
  <h3>{{ project.title }}</h3>
  {{ project.excerpt }}
  <a href="{{ project.url | relative_url }}">Read more</a>
</div>
{% endfor %}

trigger rebuild
