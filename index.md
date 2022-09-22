---
layout: home
title: 🏠 Home
nav_exclude: false
nav_order: 1
---

# {{ site.tagline }}
{: .mb-2 }
{{ site.description }}
{: .fs-6 .fw-300 }

{{ site.staffersnobio }}

**Welcome to DSC 10! 👋** Get started by reading the [syllabus](syllabus).

{% for module in site.modules %}
{{ module }}
{% endfor %}
