# Django for Beginners – Projects

Hands-on implementation of Projects from “Django for Beginners” by William S. Vincent.

## Overview

This repository contains a basic Django project adapted from the book. It focuses on learning the Django project/app structure, URL routing, views, templates, and static file handling.

## Key Dependencies

(Exact versions from requirements.txt)

- Django 4.0.10
- django-crispy-forms 1.13.0
- crispy-bootstrap5 0.6
- whitenoise 5.3.0 (static files in production)
- gunicorn 23.0.0 (production WSGI server)
- asgiref 3.9.1
- sqlparse 0.5.3
- djlint 1.36.4 (template/style linting)

Full list is in `requirements.txt`.

## Setup

```bash
# (Optional) create and activate a virtual environment
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows
.venv\Scripts\activate

pip install --upgrade pip
pip install -r requirements.txt
```

## Running the Development Server

```bash
python manage.py migrate
python manage.py runserver
```

Visit: http://127.0.0.1:8000/

Create a superuser (if admin access is needed):

```bash
python manage.py createsuperuser
```

## Static Files (Production Hint)

`whitenoise` and `gunicorn` are included. A typical production flow (after configuring settings) would involve:

```bash
python manage.py collectstatic
gunicorn <your_project>.wsgi
```

(Adjust `<your_project>` to the actual Django project package name.)

## Linting / Formatting

`djlint` is available for template and HTML/CSS/JS formatting:

```bash
djlint .
```

## Environment Variables

If using a `.env` file (not shown here), ensure you configure at least:

- SECRET_KEY
- DEBUG
- ALLOWED_HOSTS

## License

Add a LICENSE file if distribution is intended.

## Reference

Book: Django for Beginners – William S. Vincent

---

Minimal README focused strictly on information present in the repository (description + dependencies). Extend as the codebase grows.
