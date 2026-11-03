# Saint Lucia ministry website

Django application for the Ministry of Infrastructure, Port Services and Energy, preserving the navy, teal and gold homepage design and Castries harbour imagery.

## Run locally

Python 3.10+ is required.

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r app/requirements.txt
cd app
../.venv/bin/python manage.py migrate
DEBUG=1 ../.venv/bin/python manage.py runserver
```

Open http://127.0.0.1:8000/. The homepage works without database content. Migrations initialise Django’s built-in admin/auth tables.

## Architecture

- **Django 5.2:** full-page rendering, curated content, search and resource filtering.
- **Alpine.js 3.14.9:** mobile menu, search panel, focus handling, Escape dismissal and request error messages.
- **HTMX 2.0.11:** submits search and filters resource cards using server-rendered HTML fragments, without reloading the page.

Both JavaScript libraries are pinned and served locally from `app/static/vendor/`; no Node build is required. Their upstream projects are [Alpine.js](https://alpinejs.dev/) (MIT) and [HTMX](https://htmx.org/) (BSD 2-Clause). Google Fonts remains optional, with system-font fallbacks.

Routes:

| URL | Behaviour |
| --- | --- |
| `/` | Homepage; accepts `?category=notice` or `?category=publication` |
| `/search/?q=roads` | Search fragment for HTMX, full page for a normal request |
| `/updates/?category=notice` | Resource fragment for HTMX, full page for a normal request |
| `/admin/` | Built-in Django administration |

Search covers the homepage sections. Services and resource documents link to the existing official websites. Navigation, search and resource filters have normal-page fallbacks when JavaScript is disabled. This version has no CMS or live news feed.

Edit `app/pages/content.py` for searchable sections and resource cards, `app/templates/` for markup, and `app/static/` for styling and scripts. The old static-export workflow has been retired; run Django to use the server-backed interactions.

## Checks

```sh
.venv/bin/python app/manage.py check
.venv/bin/python app/manage.py test pages
node --check app/static/js/site.js
```

`DEBUG` defaults to false and accepts `1`, `true` or `yes`. Use `DEBUG=1` for local development and Django’s static-file serving. Deployment configuration is separate from this local migration.

## Content and imagery

- Ministry branding uses “Ministry of Infrastructure, Port Services and Energy”, as supplied. Existing official service and resource URLs are retained.
- Resources link to official sources. The January 2025 SLASPA notice is explicitly marked as archived; no current tender availability is implied.
- Castries harbour photograph: [Unsplash image source](https://images.unsplash.com/photo-1622896900858-99ad8da7b8d9), found through the [Castries photo collection](https://unsplash.com/s/photos/castries).
- Coat of arms: [Government of Saint Lucia ministry portal](https://infrastructure.govt.lc/Images/logo-41.png). The source is a small raster image and should be replaced with an official high-resolution asset before launch.
- Roadwork photographs were already present in the repository. They are illustrative; verify usage rights and replace them with ministry project photography before production use.
- DM Sans and Manrope load from Google Fonts, with local system-font fallbacks.
