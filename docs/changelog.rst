Changelog
=========

v0.0.10 (released 2025-08-13)
-----------------------------

*   Added models `AreaTag`, `ArtistTag`, `RecordingTag`, `ReleaseTag`, `ReleaseGroupTag`, and `WorkTag`.

v0.0.9 (released 2025-08-08)
---------------------------

*   Added model `ArtistCreditName`.
*   Dropped support for Python 3.9.
*   Bumped minimum Django version to 5.2.

v0.0.8 (released 2025-04-25)
----------------------------

*   Added ability in the API to GET an Artist using either the Artist's `id` (an integer), or `gid` (a UUID), or the
    Artist's name (as long as the name is unique).

v0.0.7 (released 2025-01-24)
----------------------------

*   Added models `LinkAttribute`, `LinkAttributeTextValue`, `LinkAttributeType`, and `LinkTextAttributeType`.
*   Added some missing `db_column` field attributes on model `LinkType`, and added a test so that these aren't missed.
*   Added completed or partial data dumps from the MusicBrainz database into the Sphinx documentation of models
    `AreaType`, `ArtistType`, `Gender`, `LinkAttributeType`, and `WorkType`.

v0.0.6 (released 2025-01-16)
----------------------------

This is a bug fix release. Changes:

*   Added missing `db_columb` attribute to the Link model.
*   Added missing `default` value to the Link Type model.
*   Removed the `priority` field from the Link Type model, per the same upstream change.
*   Dropped support for Django and require Django 5.1.
*   Updated versions of required dependencies.

v0.0.5 (released 2025-01-11)
----------------------------

This is a bug fix release. Changes:

*   This package requires a dependency on `psycopg` to be able to connect to the PostgreSQL database, but the dependency
    was not declared.
*   All URLs had the string `/api` hardcoded as a prefix. This was removed, so that the user can decide the URL
    structure.
*   Some fields on models Area, Area Type, and Artist are optional in their SQL definition, but they were not flagged as
    optional in the Django MusicBrainz Connector.
*   Some fields on models Area, Area Type and Artist were missing the `db_column` attribute, so they were not able to
    retrieve data from the database.

v0.0.4 (released 2024-12-29)
----------------------------

*   Added models `AreaType`, `Area`, `Gender`, `ArtistType`, and `Artist`.

v0.0.3 (released 2024-12-24)
----------------------------

*   Dropped support for end-of-life Python 3.8 and added support for Python 3.11 and 3.12.
*   Added models `Language`, `Medium Format`, `ReleaseGroupPrimaryType`, `ReleasePackaging`, `ReleaseStatus`, `Script`,
    and `Track`.

v0.0.2 (released 2023-11-12)
----------------------------

* Added models `ArtistCredit`, `LinkType`, `Link`, `Recording`, and `RecordingWorkLink`.

v0.0.1 (released 2023-11-11)
----------------------------

* First release, includes models `Work` and `WorkType`.
