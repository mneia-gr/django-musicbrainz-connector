from django.apps import apps
from django.db import models

from django_musicbrainz_connector.apps import DjangoMusicbrainzConnectorConfig


def test_all_model_fields_have_db_column():
    for model in apps.get_app_config(DjangoMusicbrainzConnectorConfig.name).get_models():
        for field in model._meta.fields:
            if field.primary_key and isinstance(field, models.CompositePrimaryKey):
                continue

            assert field.db_column is not None, f"Model '{model.__name__}' field '{field.name}' has no db_column"


def test_all_models_db_table():
    for model in apps.get_app_config(DjangoMusicbrainzConnectorConfig.name).get_models():
        assert not model._meta.db_table.startswith(DjangoMusicbrainzConnectorConfig.name)
