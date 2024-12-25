import pytest
from rest_framework.test import APIClient

API_RESPONSE = {
    "id": 1,
    "name": "Male",
    "child_order": 1,
    "description": None,
    "gid": "36d3d30a-839d-3eda-8cb3-29be4384e4a9",
    "parent": None,
}


@pytest.mark.django_db
def test_gender_api_GET_by_id():
    api_client = APIClient()
    response = api_client.get("/api/genders/1/")
    assert response.status_code == 200
    assert response.data == API_RESPONSE


@pytest.mark.django_db
def test_gender_api_GET_by_gid():
    api_client = APIClient()
    response = api_client.get("/api/genders/36d3d30a-839d-3eda-8cb3-29be4384e4a9/")
    assert response.status_code == 200
    assert response.data == API_RESPONSE


@pytest.mark.django_db
def test_gender_api_GET_by_name():
    api_client = APIClient()
    response = api_client.get("/api/genders/Male/")
    assert response.status_code == 200
    assert response.data == API_RESPONSE


@pytest.mark.django_db
def test_gender_api_GET_not_found():
    api_client = APIClient()
    response = api_client.get("/api/genders/123/")
    assert response.status_code == 404
    assert response.data == {"detail": "Not found."}
