import pytest

from django_musicbrainz_connector.models import ArtistType


@pytest.mark.django_db
def test_artist_type_str():
    artist_type = ArtistType.objects.get(id=1)
    assert str(artist_type) == "Person"
