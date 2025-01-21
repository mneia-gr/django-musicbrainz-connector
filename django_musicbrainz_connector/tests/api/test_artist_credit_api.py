import pytest
from rest_framework.test import APIClient

from django_musicbrainz_connector.api.artist_credit import ArtistCreditSerializer
from django_musicbrainz_connector.models.artist_credit import ArtistCredit


@pytest.mark.django_db
def test_artist_credit_serializer():
    instance = ArtistCredit.objects.get(id=1002760)
    serializer = ArtistCreditSerializer(instance=instance)

    assert serializer.data["name"] == "Ιωάννα Γεωργακοπούλου, Στελλάκης Περπινιάδης & Βασίλης Τσιτσάνης"


@pytest.mark.django_db
def test_artist_credit_GET():
    api_client = APIClient()
    response = api_client.get("/artist-credits/")
    assert response.status_code == 200
    assert response.data["count"] == 4
    assert response.data["next"] is None
    assert response.data["previous"] is None
    assert response.data["results"] == [
        {
            "id": 1002781,
            "name": "Απόστολος Χατζηχρήστος, Μάρκος Βαμβακάρης & Βασίλης Τσιτσάνης",
            "artist_count": 3,
            "ref_count": 4,
            "created": "2012-06-19T16:39:39.479103-05:00",
            "edits_pending": 0,
            "gid": "1227e205-bf71-3bb0-ad47-8ed6c6e3be0f",
        },
        {
            "id": 205524,
            "name": "Βασίλης Τσιτσάνης",
            "artist_count": 1,
            "ref_count": 336,
            "created": "2023-11-10T14:02:54.412000-06:00",
            "edits_pending": 0,
            "gid": "0e83e00a-a28c-3e80-9c00-5fa3d92cb2b1",
        },
        {
            "id": 290582,
            "name": "Γρηγόρης Μπιθικώτσης",
            "artist_count": 1,
            "ref_count": 1179,
            "created": "2011-05-16T11:32:11.963929-05:00",
            "edits_pending": 0,
            "gid": "125d928a-67e3-33e1-9884-cb1fee89cf08",
        },
        {
            "id": 1002760,
            "name": "Ιωάννα Γεωργακοπούλου, Στελλάκης Περπινιάδης & Βασίλης Τσιτσάνης",
            "artist_count": 3,
            "ref_count": 2,
            "created": "2023-11-10T14:02:54.412000-06:00",
            "edits_pending": 0,
            "gid": "8c9bafac-0df4-33c0-a7e2-61b4d5774936",
        },
    ]
