import pytest
from rest_framework.test import APIClient

from django_musicbrainz_connector.api.language import LanguageSerializer
from django_musicbrainz_connector.models.language import Language

EXPECTED_API_RESPONSE = {
    "id": 159,
    "name": "Greek",
    "iso_code_2t": "ell",
    "iso_code_2b": "gre",
    "iso_code_1": "el",
    "frequency": 2,
    "iso_code_3": "ell",
}


@pytest.mark.django_db
def test_language_serializer():
    instance = Language.objects.get(id=159)
    serializer = LanguageSerializer(instance=instance)

    assert serializer.data["name"] == "Greek"


@pytest.mark.django_db
def test_language_api_GET():
    api_client = APIClient()
    response = api_client.get("/languages/")
    assert response.status_code == 200
    assert response.data["count"] == 1
    assert response.data["next"] is None
    assert response.data["previous"] is None
    assert response.data["results"] == [EXPECTED_API_RESPONSE]


@pytest.mark.django_db
def test_language_api_GET_by_id():
    api_client = APIClient()
    response = api_client.get("/languages/159/")
    assert response.status_code == 200
    assert response.data == EXPECTED_API_RESPONSE


@pytest.mark.django_db
def test_language_api_GET_by_name():
    api_client = APIClient()
    response = api_client.get("/languages/Greek/")
    assert response.status_code == 200
    assert response.data == EXPECTED_API_RESPONSE


@pytest.mark.django_db
def test_language_api_GET_not_found():
    api_client = APIClient()
    response = api_client.get("/languages/1/")
    assert response.status_code == 404
    assert response.data == {"detail": "Not found."}
