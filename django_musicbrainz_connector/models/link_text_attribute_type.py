from django.db import models


class LinkTextAttributeType(models.Model):
    """
    PostgreSQL Definition
    ---------------------

    The :code:`link_text_attribute_type` table is defined in the MusicBrainz Server as:

    .. code-block:: sql

        CREATE TABLE link_text_attribute_type ( -- replicate
            attribute_type      INT NOT NULL -- PK, references link_attribute_type.id CASCADE
        );
    """

    attribute_type = models.OneToOneField(
        "LinkAttributeType", primary_key=True, on_delete=models.PROTECT, db_column="attribute_type"
    )

    class Meta:
        managed = False
        verbose_name_plural = "Link Text Attribute Types"
        db_table = "link_text_attribute_type"
