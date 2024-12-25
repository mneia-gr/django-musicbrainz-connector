import pytest

from django_musicbrainz_connector.models import Area


@pytest.mark.django_db
def test_area_str():
    area_type = Area.objects.get(id=84)
    assert str(area_type) == "Greece"
