import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_link_attribute_type_api():
    api_client = APIClient()
    response = api_client.get("/link-attribute-types/567/")  # from fixture
    assert response.status_code == 200
