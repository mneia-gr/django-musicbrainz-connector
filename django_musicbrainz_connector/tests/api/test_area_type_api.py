import pytest
from rest_framework.test import APIClient

API_RESPONSE = {
    "id": 1,
    "name": "Country",
    "child_order": 1,
    "description": "Country is used for areas included (or previously included) in ISO 3166-1, e.g. United States.",
    "gid": "06dd0ae4-8c74-30bb-b43d-95dcedf961de",
    "parent": None,
}


@pytest.mark.django_db
def test_area_type_api_GET_by_id():
    api_client = APIClient()
    response = api_client.get("/api/area-types/1/")
    assert response.status_code == 200
    assert response.data == API_RESPONSE


@pytest.mark.django_db
def test_area_type_api_GET_by_gid():
    api_client = APIClient()
    response = api_client.get("/api/area-types/06dd0ae4-8c74-30bb-b43d-95dcedf961de/")
    assert response.status_code == 200
    assert response.data == API_RESPONSE


@pytest.mark.django_db
def test_area_type_api_GET_by_name():
    api_client = APIClient()
    response = api_client.get("/api/area-types/Country/")
    assert response.status_code == 200
    assert response.data == API_RESPONSE


@pytest.mark.django_db
def test_area_type_api_GET_not_found():
    api_client = APIClient()
    response = api_client.get("/api/area-types/123/")
    assert response.status_code == 404
    assert response.data == {"detail": "Not found."}
