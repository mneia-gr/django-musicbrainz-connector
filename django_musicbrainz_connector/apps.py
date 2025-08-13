from django.apps import AppConfig
from django.db import models

from django_musicbrainz_connector.utils import clone_field


class DjangoMusicbrainzConnectorConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "django_musicbrainz_connector"

    def ready(self):

        # Also available, but not in django_musicbrainz_connector yet: Event, Instrument, Label, Place, Series
        import django_musicbrainz_connector.models
        from django_musicbrainz_connector.models import Area, Artist, Recording, Release, ReleaseGroup, Tag, Work
        from django_musicbrainz_connector.models.base_tag_model import TagModel

        for model_class in [Area, Artist, Recording, Release, ReleaseGroup, Work]:
            # Creation of the <Model>Tag model, based on the list
            class_name = f"{model_class.__qualname__}Tag"
            class_relation_name = model_class._meta.db_table

            # Create the Meta class (not metaclass) for the <Model>Tag class
            meta_class = type(
                "Meta",
                (),
                {
                    "managed": False,
                    "db_table": f"{class_relation_name}_tag",
                    "verbose_name_plural": f"{model_class.__qualname__} Tags",
                    "ordering": ["pk"],
                },
            )

            tag_field = TagModel._meta.get_field("tag")

            model_tag_class = type(
                class_name,
                (TagModel,),
                {
                    "__module__": "django_musicbrainz_connector.models",
                    # All `M_tag` table have composite primary key with the `M` table and the tag one
                    "pk": models.CompositePrimaryKey(class_relation_name, "tag"),
                    class_relation_name: models.ForeignKey(
                        model_class,
                        on_delete=models.PROTECT,
                        db_column=class_relation_name,
                        # Access through `M.m_tag_m2m.all()`
                        related_name=f"{class_relation_name}_tag_m2m",
                    ),
                    # Access through `tag.m_tag_m2m.all()`
                    "tag": clone_field(tag_field, related_name=f"{class_relation_name}_tag_m2m"),
                    "Meta": meta_class,
                },
            )
            # Set into the module so it can be auto imported
            # with `from django_musicbrainz_connector.models import ModelTag`
            setattr(django_musicbrainz_connector.models, class_name, model_tag_class)

            # Add the m2m relation between Model <> Tag, so we can use:
            # - the convenient `tag.models.all()`
            # - and `model.tags.all()`
            # Without the necessity of manually navigating the through-table,
            # those options remain accessible through:
            # - `model.model_tag_m2m.all()`
            # - and the reverse: `tag.model_tag_m2m.all()`
            Tag.add_to_class(
                f"{class_relation_name}s",
                models.ManyToManyField(model_class, through=model_tag_class, related_name="tags"),
            )
