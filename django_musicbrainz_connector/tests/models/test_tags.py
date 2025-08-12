import pytest

from django_musicbrainz_connector.models import Tag


@pytest.mark.django_db
def test_tag_str():
    tag = Tag.objects.get(pk=479)
    assert str(tag) == "greek"
