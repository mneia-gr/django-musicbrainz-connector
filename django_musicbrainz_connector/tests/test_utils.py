import pytest

from django_musicbrainz_connector.utils import get_musicbrainz_identifier_type


@pytest.mark.parametrize(
    "identifier, expected_type",
    [
        (123, "id"),
        ("123", "id"),
        ("49daefeb-3cc5-4f8b-aa0d-26d7c83be1f8", "gid"),
        ("foo", "name"),
        ("956d1ec2-33b2-4cd6-8832-1bbcd0d42661+2745d711-1ca1-4647-9971-5e208682fdcb", "name"),  # something weird :D
    ],
)
def test_get_musicbrainz_identifier_type(identifier, expected_type):
    assert get_musicbrainz_identifier_type(identifier) == expected_type
