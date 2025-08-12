import pytest
from django.db.models import Model

from django_musicbrainz_connector.models import Area, Artist, Recording, Release, ReleaseGroup, Tag, Work


@pytest.mark.parametrize(
    "tag_id,klass,instance_id",
    [
        (479, Artist, 205528),
        (1616, Area, 84),
        (1616, Recording, 13679939),
        (1616, Release, 2681644),
        (1616, ReleaseGroup, 2369755),
        (1616, Work, 11432290),
    ],
)
@pytest.mark.django_db
def test_tag_class_m2m(tag_id: int, klass: Model, instance_id: int):
    tag = Tag.objects.get(id=tag_id)
    instance = klass.objects.get(id=instance_id)

    relation_name = klass._meta.db_table
    plural_class_name = f"{relation_name}s"

    # Test the tag <> through table relations
    assert getattr(tag, f"{relation_name}_tag_m2m").first().pk == (instance.pk, tag.pk)
    assert getattr(instance, f"{relation_name}_tag_m2m").first().pk == (instance.pk, tag.pk)

    # Test the tag <> instance relations
    assert tag in instance.tags.all()
    assert instance in getattr(tag, plural_class_name).all()
