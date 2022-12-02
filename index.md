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

<span style='color:red'><b>Note: As of 1:30AM on Friday, we're at 67% completion of [CAPEs](https://cape.ucsd.edu) and 51% completion of the [End of Quarter Survey](https://docs.google.com/forms/d/e/1FAIpQLSeiZodx0wMHVxC-PfSGXu0mrI2R8XgS1RUzI-VZhZc9TbT3lA/viewform). If 80% of the class fills out both by 8AM on Saturday, everyone will have 0.5% of extra credit added to their overall grade!</b></span>

Lecture and discussion recordings can be found at [podcast.ucsd.edu](https://podcast.ucsd.edu).

{% for module in site.modules %}
{{ module }}
{% endfor %}
