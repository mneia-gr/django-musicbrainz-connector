import pytest
from rest_framework.test import APIClient

from django_musicbrainz_connector.api.work import WorkSerializer
from django_musicbrainz_connector.models.work import Work

WORK_11432290_API_RESPONSE = {
    "id": 11432290,
    "gid": "fe4f5295-4d0f-32bd-8029-743f740d31f1",
    "name": "Η αχάριστη",
    "edits_pending": 0,
    "last_updated": "2023-11-10T14:02:54.412000-06:00",
    "type": 17,
    "recordings": ["fdb9d6f4-73f2-41f2-ba57-a8dbb65433a2"],
}

WORK_12431814_API_RESPONSE = {
    "id": 12431814,
    "gid": "864c45d9-8450-4b6f-9570-744980fba21e",
    "name": "Φραγκοσυριανή",
    "edits_pending": 0,
    "last_updated": "2020-04-30T11:00:28.854191-05:00",
    "type": 17,
    "recordings": ["0e065830-aa1d-42d7-94f5-9513b5bed21d"],
}


@pytest.mark.django_db
def test_work_serializer():
    instance = Work.objects.get(id=11432290)
    serializer = WorkSerializer(instance=instance)

    assert serializer.data["name"] == "Η αχάριστη"


@pytest.mark.django_db
def test_work_api_GET():
    api_client = APIClient()
    response = api_client.get("/works/")
    assert response.status_code == 200
    assert response.data["count"] == 2
    assert response.data["next"] is None
    assert response.data["previous"] is None
    assert response.data["results"] == [WORK_11432290_API_RESPONSE, WORK_12431814_API_RESPONSE]


@pytest.mark.django_db
def test_work_api_GET_by_id():
    api_client = APIClient()
    response = api_client.get("/works/11432290/")
    assert response.status_code == 200
    assert response.data == WORK_11432290_API_RESPONSE


@pytest.mark.django_db
def test_work_api_GET_by_gid():
    api_client = APIClient()
    response = api_client.get("/works/fe4f5295-4d0f-32bd-8029-743f740d31f1/")
    assert response.status_code == 200
    assert response.data == WORK_11432290_API_RESPONSE


@pytest.mark.django_db
def test_work_api_GET_instance_not_found():
    api_client = APIClient()
    response = api_client.get("/works/1/")
    assert response.status_code == 404
    assert response.data == {"detail": "Not found."}
