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

<!-- <details>
<summary>🎥 Lecture Recordings</summary>
<ul>
    <li>A00, 10am with Janine Tiefenbruck</li>
    <li>B00, 11am with Janine Tiefenbruck</li>
    <li>C00, 1pm with Suraj Rampure</li>
    <li>D00, 12pm with Puoya Tabaghi</li>
</ul>
</details> -->

Lecture and discussion recordings can be found at [podcast.ucsd.edu](https://podcast.ucsd.edu).

{% for module in site.modules %}
{{ module }}
{% endfor %}
