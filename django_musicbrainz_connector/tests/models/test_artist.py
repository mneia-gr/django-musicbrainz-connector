import pytest

from django_musicbrainz_connector.models import Artist


@pytest.mark.django_db
def test_artist_str():
    artist = Artist.objects.get(id=205528)
    assert str(artist) == "Μάρκος Βαμβακάρης"
