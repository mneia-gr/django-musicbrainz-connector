import pytest
from rest_framework.test import APIClient

from django_musicbrainz_connector.api.recording import RecordingSerializer
from django_musicbrainz_connector.models import Recording

RECORDING_13679939_API_RESPONSE = {
    "id": 13679939,
    "recording_of": ["fe4f5295-4d0f-32bd-8029-743f740d31f1"],
    "gid": "fdb9d6f4-73f2-41f2-ba57-a8dbb65433a2",
    "name": "Αχάριστη",
    "length": 195000,
    "comment": "",
    "edits_pending": 0,
    "last_updated": "2023-11-10T14:02:54.412000-06:00",
    "video": False,
    "artist_credit": 1002760,
}

RECORDING_13679972_API_RESPONSE = {
    "id": 13679972,
    "recording_of": [],
    "gid": "cd726d65-7f36-415f-b539-9dc4527b8580",
    "name": "Φάνταζες σαν πριγκιπέσα",
    "length": 190000,
    "comment": "",
    "edits_pending": 0,
    "last_updated": "2012-06-19T16:39:39.479103-05:00",
    "video": False,
    "artist_credit": 1002781,
}

RECORDING_10911771_API_RESPONSE = {
    "id": 10911771,
    "recording_of": ["864c45d9-8450-4b6f-9570-744980fba21e"],
    "gid": "0e065830-aa1d-42d7-94f5-9513b5bed21d",
    "name": "Φραγκοσυριανή",
    "length": 185000,
    "artist_credit": 290582,
    "comment": "",
    "edits_pending": 0,
    "last_updated": "2022-12-02T04:40:23.765950-06:00",
    "video": False,
}

RECORDING_LIST_API_RESPONSE = [
    RECORDING_13679939_API_RESPONSE,
    RECORDING_13679972_API_RESPONSE,
    RECORDING_10911771_API_RESPONSE,
]


@pytest.mark.django_db
def test_recording_serializer():
    instance = Recording.objects.get(id=13679939)
    serializer = RecordingSerializer(instance=instance)

    assert serializer.data["name"] == "Αχάριστη"


@pytest.mark.django_db
def test_recording_api_GET():
    api_client = APIClient()
    response = api_client.get("/recordings/")
    assert response.status_code == 200
    assert response.data["count"] == 3
    assert response.data["next"] is None
    assert response.data["previous"] is None
    assert response.data["results"] == RECORDING_LIST_API_RESPONSE


@pytest.mark.django_db
def test_recording_api_GET_by_id():
    api_client = APIClient()
    response = api_client.get("/recordings/13679939/")
    assert response.status_code == 200
    assert response.data == RECORDING_13679939_API_RESPONSE


@pytest.mark.django_db
def test_recording_api_GET_by_gid():
    api_client = APIClient()
    response = api_client.get("/recordings/fdb9d6f4-73f2-41f2-ba57-a8dbb65433a2/")
    assert response.status_code == 200
    assert response.data == RECORDING_13679939_API_RESPONSE


@pytest.mark.django_db
def test_recording_api_GET_not_found():
    api_client = APIClient()
    response = api_client.get("/recordings/1/")
    assert response.status_code == 404
    assert response.data == {"detail": "Not found."}
