import pytest
from django.apps import apps
from django.core.management import call_command

from django_musicbrainz_connector.apps import DjangoMusicbrainzConnectorConfig


@pytest.mark.django_db
def pytest_sessionstart():
    """Convert unmanaged models to managed models during testing, so we can create objects in a test database."""
    unmanaged_models = [
        model
        for model in apps.get_app_config(DjangoMusicbrainzConnectorConfig.name).get_models()
        if model._meta.managed is False
    ]
    for model in unmanaged_models:
        model._meta.managed = True


@pytest.fixture(scope="session")
def django_db_setup(django_db_setup, django_db_blocker):
    """Load all JSON fixtures."""
    fixtures = [
        "link-type",
        "link",
        "work-type",
        "work",
        "artist-credit",
        "recording",
        "recording-work-link",
        "script",
        "language",
        "release-packaging",
        "release-status",
        "release-group-primary-type",
        "release-group",
        "release",
        "medium-format",
        "medium",
        "track",
        "area-type",
        "area",
        "artist-type",
        "gender",
        "artist",
    ]
    with django_db_blocker.unblock():
        for fixture in fixtures:
            call_command("loaddata", f"django_musicbrainz_connector/tests/fixtures/{fixture}.json")
