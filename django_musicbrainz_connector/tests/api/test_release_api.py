import pytest
from rest_framework.test import APIClient

RELEASE_RESPONSE = {
    "id": 2681644,
    "gid": "a026f47e-5ce7-4b6f-8469-cdf8c4bccb4b",
    "name": "Φάνταζες σαν πριγκηπέσα / Είσαι αριστοκράτισσα κι ωραία",
    "artist_credit": 205524,
    "release_group": 2369755,
    "status": 1,
    "packaging": None,
    "language": {
        "id": 159,
        "iso_code_2t": "ell",
        "iso_code_2b": "gre",
        "iso_code_1": "el",
        "name": "Greek",
        "frequency": 2,
        "iso_code_3": "ell",
    },
    "script": {
        "id": 22,
        "iso_code": "Grek",
        "iso_number": "200",
        "name": "Greek",
        "frequency": 4,
    },
    "barcode": None,
    "comment": "",
    "edits_pending": 0,
    "quality": -1,
    "last_updated": "2023-11-10T14:02:54.412000-06:00",
    "media": [
        {
            "id": 2912288,
            "position": 1,
            "name": "",
            "edits_pending": 0,
            "last_updated": "2020-04-19T12:53:28.789455-05:00",
            "track_count": 2,
            "release": 2681644,
            "format": 73,
            "tracks": [
                {
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
            ],
        }
    ],
}


@pytest.mark.django_db
def test_release_api_GET():
    api_client = APIClient()
    response = api_client.get("/releases/")
    assert response.status_code == 200
    assert response.data["count"] == 1
    assert response.data["next"] is None
    assert response.data["previous"] is None
    assert response.data["results"] == [RELEASE_RESPONSE]


@pytest.mark.django_db
def test_release_api_GET_by_id():
    api_client = APIClient()
    response = api_client.get("/releases/2681644/")
    assert response.status_code == 200
    assert response.data == RELEASE_RESPONSE


@pytest.mark.django_db
def test_release_api_GET_by_gid():
    api_client = APIClient()
    response = api_client.get("/releases/a026f47e-5ce7-4b6f-8469-cdf8c4bccb4b/")
    assert response.status_code == 200
    assert response.data == RELEASE_RESPONSE


@pytest.mark.django_db
def test_release_api_GET_not_found():
    api_client = APIClient()
    response = api_client.get("/releases/1/")
    assert response.status_code == 404
    assert response.data == {"detail": "Not found."}
