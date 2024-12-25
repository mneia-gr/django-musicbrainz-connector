import pytest

from django_musicbrainz_connector.models import Gender


@pytest.mark.django_db
def test_gender_str():
    gender = Gender.objects.get(id=1)
    assert str(gender) == "Male"
