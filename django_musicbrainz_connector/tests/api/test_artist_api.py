import pytest
from rest_framework.test import APIClient

EXPECTED_API_RESPONSE = {
    "id": 205528,
    "gid": "482a86e0-4d49-4d26-8406-3d06f01f0285",
    "name": "Μάρκος Βαμβακάρης",
    "sort_name": "Vamvakaris, Markos",
    "begin_date_year": 1905,
    "begin_date_month": 5,
    "begin_date_day": 10,
    "end_date_year": 1972,
    "end_date_month": 2,
    "end_date_day": 8,
    "type": 1,
    "area": 84,
    "gender": 1,
    "comment": "",
    "edits_pending": 0,
    "last_updated": "2017-10-20T04:21:16.739978-05:00",
    "ended": True,
    "begin_area": 116512,
    "end_area": 12762,
}


@pytest.mark.django_db
def test_artist_api_get_by_id():
    api_client = APIClient()
    response = api_client.get("/artists/205528/")
    assert response.status_code == 200
    assert response.data == EXPECTED_API_RESPONSE


@pytest.mark.django_db
def test_artist_api_get_by_gid():
    api_client = APIClient()
    response = api_client.get("/artists/482a86e0-4d49-4d26-8406-3d06f01f0285/")
    assert response.status_code == 200
    assert response.data == EXPECTED_API_RESPONSE


@pytest.mark.django_db
def test_artist_api_get_by_name():
    api_client = APIClient()
    response = api_client.get("/artists/Μάρκος Βαμβακάρης/")
    assert response.status_code == 200
    assert response.data == EXPECTED_API_RESPONSE


@pytest.mark.django_db
def test_artist_api_get_not_found():
    api_client = APIClient()
    response = api_client.get("/artists/123/")
    assert response.status_code == 404
    assert response.data == {"detail": "Not found."}
