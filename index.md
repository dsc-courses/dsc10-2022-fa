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

Below, you can access lecture material in two ways:
- By clicking the title of the lecture, which will open the lecture on DataHub, where we will run our code in this course. (More on this on Wednesday.)
- By clicking ✏️, which will open the lecture as a static HTML page, which you can download as a PDF and annotate on your tablet.

{% for module in site.modules %}
{{ module }}
{% endfor %}
