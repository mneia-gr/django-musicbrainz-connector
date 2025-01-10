import pytest
from rest_framework.test import APIClient

EXPECTED_TRACK_API_RESPONSE = {
    "id": 31083305,
    "gid": "6744f21c-5112-49d9-bf59-81c25c4d9dd0",
    "position": 1,
    "number": "A",
    "name": "Φάνταζες σαν πριγκηπέσα",
    "length": None,
    "edits_pending": 0,
    "last_updated": "2020-04-19T12:53:28.789455-05:00",
    "is_data_track": False,
    "medium": 2912288,
    "artist_credit": 205524,
    "recording": {
        "id": 13679972,
        "gid": "cd726d65-7f36-415f-b539-9dc4527b8580",
        "name": "Φάνταζες σαν πριγκιπέσα",
        "length": 190000,
        "comment": "",
        "edits_pending": 0,
        "last_updated": "2012-06-19T16:39:39.479103-05:00",
        "video": False,
        "artist_credit": 1002781,
        "recording_of": [],
    },
}


@pytest.mark.django_db
def test_track_api_GET():
    api_client = APIClient()
    response = api_client.get("/tracks/")
    assert response.status_code == 200
    assert response.data["next"] is None
    assert response.data["previous"] is None
    assert response.data["results"] == [EXPECTED_TRACK_API_RESPONSE]


@pytest.mark.django_db
def test_track_api_GET_by_medium():
    api_client = APIClient()
    response = api_client.get("/tracks/?medium-id=2912288")
    assert response.status_code == 200
    assert response.data["next"] is None
    assert response.data["previous"] is None
    assert response.data["results"] == [EXPECTED_TRACK_API_RESPONSE]
