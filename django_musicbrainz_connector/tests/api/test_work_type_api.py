import pytest
from rest_framework.test import APIClient

from django_musicbrainz_connector.api.work_type import WorkTypeSerializer
from django_musicbrainz_connector.models.work_type import WorkType

WORK_TYPE_API_RESPONSE = {
    "id": 17,
    "name": "Song",
    "child_order": 1,
    "description": "A song is in its origin (and still in most cases) a composition for voice...",
    "gid": "f061270a-2fd6-32f1-a641-f0f8676d14e6",
    "parent": None,
}


@pytest.mark.django_db
def test_work_type_serializer():
    instance = WorkType.objects.get(id=17)
    serializer = WorkTypeSerializer(instance=instance)

    assert serializer.data["name"] == "Song"


@pytest.mark.django_db
def test_work_type_api_GET():
    api_client = APIClient()
    response = api_client.get("/work-types/")
    assert response.status_code == 200
    assert response.data["count"] == 1
    assert response.data["next"] is None
    assert response.data["previous"] is None
    assert response.data["results"] == [WORK_TYPE_API_RESPONSE]


@pytest.mark.django_db
def test_work_type_api_GET_by_id():
    api_client = APIClient()
    response = api_client.get("/work-types/17/")
    assert response.status_code == 200
    assert response.data == WORK_TYPE_API_RESPONSE


@pytest.mark.django_db
def test_work_type_api_GET_by_gid():
    api_client = APIClient()
    response = api_client.get("/work-types/f061270a-2fd6-32f1-a641-f0f8676d14e6/")
    assert response.status_code == 200
    assert response.data == WORK_TYPE_API_RESPONSE


@pytest.mark.django_db
def test_work_type_api_GET_by_name():
    api_client = APIClient()
    response = api_client.get("/work-types/Song/")
    assert response.status_code == 200
    assert response.data == WORK_TYPE_API_RESPONSE


@pytest.mark.django_db
def test_work_type_api_GET_not_found():
    api_client = APIClient()
    response = api_client.get("/work-types/1/")
    assert response.status_code == 404
    assert response.data == {"detail": "Not found."}
