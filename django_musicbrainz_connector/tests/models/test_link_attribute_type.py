import pytest

from django_musicbrainz_connector.models.link_attribute_type import LinkAttributeType


@pytest.mark.django_db
def test_link_attribute_type_str():
    link_attribute_type = LinkAttributeType.objects.get(id=567)  # from fixture
    assert str(link_attribute_type) == "cover"
