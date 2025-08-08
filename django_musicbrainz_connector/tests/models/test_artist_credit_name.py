import pytest

from django_musicbrainz_connector.models.artist_credit_name import ArtistCreditName


@pytest.mark.django_db
def test_artist_credit_name_pk():
    credit_name = ArtistCreditName.objects.get(artist_credit=1002781, artist=205528)

    assert credit_name.pk == (1002781, 1)


@pytest.mark.django_db
def test_artist_credit_name_str():
    credit_name = ArtistCreditName.objects.get(artist_credit=1002781, artist=205528)

    assert str(credit_name) == "Μάρκος Βαμβακάρης"
