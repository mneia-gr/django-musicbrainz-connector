import pytest

from django_musicbrainz_connector.models import AreaType


@pytest.mark.django_db
def test_area_type_str():
    area_type = AreaType.objects.get(id=1)
    assert str(area_type) == "Country"
