import pytest
from rest_framework.test import APIClient

API_RESPONSE = {
    "id": 1,
    "name": "Person",
    "child_order": 1,
    "description": (
        'This indicates an individual person, be it under its legal name ("John Lennon"), '
        'or a performance name ("Sting").'
    ),
    "gid": "b6e035f4-3ce9-331c-97df-83397230b0df",
    "parent": None,
}


@pytest.mark.django_db
def test_artist_type_api_GET_by_id():
    api_client = APIClient()
    response = api_client.get("/api/artist-types/1/")
    assert response.status_code == 200
    assert response.data == API_RESPONSE


@pytest.mark.django_db
def test_artist_type_api_GET_by_gid():
    api_client = APIClient()
    response = api_client.get("/api/artist-types/b6e035f4-3ce9-331c-97df-83397230b0df/")
    assert response.status_code == 200
    assert response.data == API_RESPONSE


@pytest.mark.django_db
def test_artist_type_api_GET_by_name():
    api_client = APIClient()
    response = api_client.get("/api/artist-types/Person/")
    assert response.status_code == 200
    assert response.data == API_RESPONSE


@pytest.mark.django_db
def test_artist_type_api_GET_not_found():
    api_client = APIClient()
    response = api_client.get("/api/artist-types/123/")
    assert response.status_code == 404
    assert response.data == {"detail": "Not found."}
