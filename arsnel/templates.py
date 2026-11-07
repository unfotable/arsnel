"""Jinja2 page templates, kept as Python strings (no hand-written HTML files)."""

from __future__ import annotations

from jinja2 import DictLoader, Environment, select_autoescape

BASE = """\
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{ title }}</title>
<meta name="description" content="{{ tagline_plain }}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{{ fonts_url }}">
<link rel="stylesheet" href="{{ root }}static/arsnel.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="bar"><div class="wrap">
  <a class="brand" href="{{ root }}index.html">&gt; ARSNEL<span class="cursor">█</span></a>
  <nav aria-label="Primary">
    <a href="{{ root }}index.html#modules">modules</a>
    <a href="{{ root }}index.html#demo">demo</a>
    <a href="{{ root }}charts.html">charts</a>
    <a href="{{ repo_url }}">github</a>
    <button class="chip" id="theme-toggle" type="button">theme</button>
  </nav>
</div></header>
<main id="main" class="wrap page">
{% block body %}{% endblock %}
</main>
<footer><div class="wrap">
  <p>ARSNEL v{{ version }} · MIT · built {{ built }} · {{ tagline_plain }}</p>
  <p>$ exit 0 <span class="cursor">█</span></p>
</div></footer>
<script src="{{ root }}static/arsnel.js"></script>
</body>
</html>
"""

INDEX = """\
{% extends "base.html" %}
{% block body %}
<section class="hero">
  <pre class="ascii" aria-label="ARSNEL">{{ hero }}</pre>
  <p class="tagline">{{ tagline_html|safe }}</p>
  <div class="stats">
    <div class="tile"><b>{{ modules|length }}</b><small>modules</small></div>
    <div class="tile"><b>{{ exercises }}</b><small>exercises</small></div>
    <div class="tile"><b>{{ badges }}</b><small>badges</small></div>
    <div class="tile"><b>{{ python_percent }}%</b><small>Python</small></div>
    <div class="tile"><b>LVL {{ level }}</b><small>{{ rank }}</small></div>
  </div>
  <div class="xp" role="img" aria-label="XP {{ percent }} percent">
    {% for i in range(40) %}<i class="{{ 'on' if i < filled else '' }}"></i>{% endfor %}
  </div>
  <p>XP {{ xp }}/{{ max_xp }} - fork the repo, solve exercises, run <code>make progress</code>.</p>
  <a class="btn" href="#modules">start learning</a>
  <a class="btn" href="{{ repo_url }}">star on github</a>
</section>

<section id="demo" class="demo">
  <h2>interactive terminal</h2>
  <p>Real outputs, captured from the repo when this site was built. Try the chips.</p>
  <div class="chips">
    {% for c in demo_chips %}<button class="chip" type="button" data-cmd="{{ c }}">{{ c }}</button>{% endfor %}
  </div>
  <div class="term">
    <div class="titlebar"><i></i><i></i><i></i><span>arsnel@pixel: ~</span></div>
    <div class="screen" id="demo-screen" role="log" aria-live="polite"></div>
    <label class="row"><span>$</span>
      <input id="demo-input" autocomplete="off" spellcheck="false" aria-label="terminal command" placeholder="type help"></label>
  </div>
  <script type="application/json" id="demo-data">{{ demo_json|safe }}</script>
</section>

<section id="modules">
  <h2>module index</h2>
  <div class="search">
    <input id="q" type="search" placeholder="search modules: decorators, async, pytest...  (press /)" aria-label="Search modules">
  </div>
  <div class="grid">
  {% for m in modules %}
    <a class="mod" data-id="{{ m.mid }}" href="modules/{{ m.dirname }}.html">
      <span class="num">{{ m.prompt }}</span>
      <h3>{{ m.title }}</h3>
      <p>{{ m.tagline }}</p>
      <span class="tag">{{ m.level }} · ~{{ m.hours }}h</span>
    </a>
  {% endfor %}
  </div>
  <p id="empty" class="hidden">no modules match - try another keyword.</p>
  <script type="application/json" id="search-data">{{ search_json|safe }}</script>
</section>

<section>
  <h2>roadmap</h2>
  <p><img src="assets/charts/roadmap.png" alt="Learning path roadmap across all modules"></p>
  <p><a href="charts.html">see all six charts →</a></p>
</section>

<section>
  <h2>achievements</h2>
  <div class="term"><div class="titlebar"><i></i><i></i><i></i><span>badges</span></div>
  <pre class="compact"><code>{{ badges_art }}</code></pre></div>
</section>
{% endblock %}
"""

MODULE = """\
{% extends "base.html" %}
{% block body %}
<p class="crumbs"><a href="../index.html">ARSNEL</a> / curriculum / {{ m.prompt }}</p>
<p><span class="tag">{{ m.level }}</span> <span class="tag">~{{ m.hours }}h</span>
<span class="tag">{{ m.skill }}</span></p>
{{ body|safe }}
<nav class="pager" aria-label="Module navigation">
  {% if prev %}<a class="btn" href="{{ prev.dirname }}.html">&lt; {{ prev.prompt }}</a>{% else %}<span></span>{% endif %}
  {% if next %}<a class="btn" href="{{ next.dirname }}.html">{{ next.prompt }} &gt;</a>{% endif %}
</nav>
{% endblock %}
"""

CHARTS = """\
{% extends "base.html" %}
{% block body %}
<h1>charts</h1>
<p>Every chart is drawn by a script in <code>charts/</code> with matplotlib.</p>
{% for c in charts %}
<section>
  <h2>{{ c.title }}</h2>
  <p><img src="assets/charts/{{ c.name }}.png" alt="{{ c.title }}"></p>
  <p><a href="assets/charts/{{ c.name }}.svg">svg</a> · <a href="assets/charts/{{ c.name }}.png">png</a></p>
</section>
{% endfor %}
{% endblock %}
"""


def environment() -> Environment:
    """Return the Jinja2 environment that serves the templates above."""
    return Environment(
        loader=DictLoader(
            {
                "base.html": BASE,
                "index.html": INDEX,
                "module.html": MODULE,
                "charts.html": CHARTS,
            }
        ),
        autoescape=select_autoescape(default=True),
        trim_blocks=True,
        lstrip_blocks=True,
    )
