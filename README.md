# Django MusicBrainz Connector #

[![Django CI](https://github.com/mneia-gr/django-musicbrainz-connector/actions/workflows/django.yml/badge.svg)](https://github.com/mneia-gr/django-musicbrainz-connector/actions/workflows/django.yml)
[![Docs](https://readthedocs.org/projects/django-musicbrainz-connector/badge/?version=latest)](https://django-musicbrainz-connector.readthedocs.org/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/mneia-gr/django-musicbrainz-connector/graph/badge.svg?token=GUPRL0NELL)](https://codecov.io/gh/mneia-gr/django-musicbrainz-connector)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django-musicbrainz-connector)](https://pypi.python.org/pypi/django-musicbrainz-connector)
[![Supported Django versions](https://img.shields.io/pypi/djversions/django-musicbrainz-connector.svg)](https://pypi.python.org/pypi/django-musicbrainz-connector)

The **Django MusicBrainz Connector** is a Django app that connects to a replica of the MusicBrainz PostgreSQL database.

## Installation

1.  Using the Django MusicBrainz Connector requires that you have a replica of the MusicBrainz database. You can create
    one by following the installation steps in the [MusicBrainz Server](https://github.com/metabrainz/musicbrainz-server).

2.  Install this module from PyPI, for example:

    ```
    python3 -m pip install django-musicbrainz-connector
    ```

    Alternatively, install from code:

    ```
    git clone git@github.com:mneia-gr/django-musicbrainz-connector.git
    cd django-musicbrainz-connector
    python setup.py sdist
    python -m pip install dist/django-musicbrainz-connector-0.0.1.tar.gz
    ```

3.  Append the app to your Django project's `settings.py` list of `INSTALLED_APPS`, for example:

    ```python
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django_musicbrainz_connector',  # <-- like this
    ]
    ```

4.  Create a read-only user in the MusicBrainz Postgresql replica database. This step is not required, but it is highly
    recommended. Example commands:

    ```sql
    \c musicbrainz_db
    CREATE USER django_musicbrainz_connector WITH PASSWORD 'sUp3rSecr3t';
    GRANT CONNECT ON DATABASE musicbrainz_db TO django_musicbrainz_connector;
    GRANT USAGE ON SCHEMA musicbrainz TO django_musicbrainz_connector;
    GRANT SELECT ON ALL TABLES IN SCHEMA musicbrainz TO django_musicbrainz_connector;
    ALTER USER django_musicbrainz_connector SET SEARCH_PATH TO musicbrainz;
    ```

    You can confirm this with something like:

    ```sql
    SELECT grantee, privilege_type FROM information_schema.role_table_grants WHERE table_name='area_type';
    ```

    The output should include the user you just created:

    ```
              grantee            | privilege_type
    ------------------------------+----------------
    musicbrainz                  | INSERT
    musicbrainz                  | SELECT
    musicbrainz                  | UPDATE
    musicbrainz                  | DELETE
    musicbrainz                  | TRUNCATE
    musicbrainz                  | REFERENCES
    musicbrainz                  | TRIGGER
    django_musicbrainz_connector | SELECT
    ```

    You can also connect to the database with `psql`:

    ```
    psql -d musicbrainz_db -U django_musicbrainz_connector
    SELECT * FROM musicbrainz.area_type;
    ```

5.  Add the MusicBrainz database to your Django project's `settings.py` list of `DATABASES`. You shouldn't use the
    MusicBrainz database as the Django default database, because this app is only meant to have read access. For
    example:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        },
        'musicbrainz_db': {
            'NAME': "musicbrainz_db",
            "ENGINE": "django.db.backends.postgresql",
            "USER": "django_musicbrainz_connector",
            "PASSWORD": "sUp3rSecr3t",
        },
    }
    ```

6.  Add the database router to your Django project's `settings.py` list of `DATABASE_ROUTERS`, for example:

    ```python
    DATABASE_ROUTERS = [
        "django_musicbrainz_connector.routers.DjangoMusicBrainzConnectorDatabaseRouter",
    ]
    ```

7.  Apply the migrations. This doesn't make any changes to the MusicBrainz database:

    ```
    python manage.py migrate
    ```

8.  Include the URLs in your Django project's `urls.py`, for example:

    ```python
    urlpatterns = [
        path("admin/", admin.site.urls),
        path("mb/", include("django_musicbrainz_connector.urls")),  # <-- like this
        # other stuff here
    ]
    ```

## Notes on Read-Only Access

This app provides read-only connectivity to the database, because it assumes that you maintain a replica of the
MusicBrainz Postgresql database, and therefore it makes no sense to be able to write to it. This is done in several
ways:

1.  It is recommended that you create a read-only user in Postgresql, and use that user for this app. The installation
    documentation includes step-by-step instructions for this.

2.  All models have `Meta.managed` set to `False`.

3.  For models registered in the Django Admin, methods `has_add_permission`, `has_change_permission` and
    `has_delete_permission` are always set to `False`.

4.  All classes that inherit from Django REST Framework's `ViewSet` have `http_method_names` set to `["get"]` only.

## Development ##

### Testing ###

Install test dependencies with:

```
python -m pip install --requirement requirements-test.txt
```

Then, run tests with:

```
./test
```

### Documentation ###

To build the documentation locally:

```
python -m pip install --requirement docs/requirements.txt
sphinx-build -M html docs build/docs
```

### Release ###

1.  Bump the value of `version` in `setup.cfg`, and push to GitHub.

2.  Create a git tag same as the `version`, and push it, for example:

    ```
    git tag --annotate v0.0.2 --message "Release tag v0.0.2"
    git push origin v0.0.2
    ```

3.  Build:

    ```
    python setup.py sdist
    python setup.py bdist_wheel
    ```

4.  Upload to TestPyPI:

    ```
    python -m twine upload --repository testpypi dist/*
    ```

5.  If the output looks OK, upload to PyPI:

    ```
    python -m twine upload dist/*
    ```

6.  Create a new Release on GitHub, from the tag pushed earlier.
