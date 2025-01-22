from django.db import models


class LinkAttribute(models.Model):
    """
    PostgreSQL Definition
    ---------------------

    The :code:`link_attribute` table is defined in the MusicBrainz Server as:

    .. code-block:: sql

        CREATE TABLE link_attribute ( -- replicate
            link                INTEGER NOT NULL, -- PK, references link.id
            attribute_type      INTEGER NOT NULL, -- PK, references link_attribute_type.id
            created             TIMESTAMP WITH TIME ZONE DEFAULT NOW()
        );

    :param link: References :class:`Link`. This is both a Foreign Key to the :class:`Link` model, as well as a Primary
        Key for :class:`LinkAttribute`. In Django, this is best implemented as a :code:`OneToOneField`.
    :param attribute_type: References :class:`LinkAttributeType`.
    """

    link = models.OneToOneField("Link", primary_key=True, on_delete=models.PROTECT, db_column="link")
    attribute_type = models.OneToOneField("LinkAttributeType", on_delete=models.PROTECT, db_column="attribute_type")
    created = models.DateTimeField(auto_now_add=True, db_column="created")

    class Meta:
        managed = False
        verbose_name_plural = "Link Attributes"
        db_table = "link_attribute"
