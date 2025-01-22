from django.db import models


class LinkAttributeTextValue(models.Model):
    """
    PostgreSQL Definition
    ---------------------

    The :code:`link_attribute_text_value` table is defined in the MusicBrainz Server as:

    .. code-block:: sql

        CREATE TABLE link_attribute_text_value ( -- replicate
            link                INT NOT NULL, -- PK, references link.id
            attribute_type      INT NOT NULL, -- PK, references link_text_attribute_type.attribute_type
            text_value          TEXT NOT NULL
        );
    """

    link = models.OneToOneField("Link", primary_key=True, on_delete=models.PROTECT)
    attribute_type = models.OneToOneField("LinkAttributeType", on_delete=models.PROTECT)
    text_value = models.TextField()

    class Meta:
        managed = False
        verbose_name_plural = "Link Attribute Text Value"
        db_table = "link_attribute_text_value"
