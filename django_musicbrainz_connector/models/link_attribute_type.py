from django.db import models


class LinkAttributeType(models.Model):
    """
    PostgreSQL Definition
    ---------------------

    The :code:`link_attribute_type` table is defined in the MusicBrainz Server as:

    .. code-block:: sql


        CREATE TABLE link_attribute_type ( -- replicate
            id                  SERIAL,
            parent              INTEGER, -- references link_attribute_type.id
            root                INTEGER NOT NULL, -- references link_attribute_type.id
            child_order         INTEGER NOT NULL DEFAULT 0,
            gid                 UUID NOT NULL,
            name                VARCHAR(255) NOT NULL,
            description         TEXT,
            last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW()
        );
    """

    id = models.IntegerField("ID", primary_key=True, db_column="id")
    parent = models.ForeignKey(
        "self",
        null=True,
        on_delete=models.PROTECT,
        related_name="child_link_attribute_types",
        db_column="parent",
    )
    root = models.ForeignKey(
        "self",
        on_delete=models.PROTECT,
        related_name="leaf_child_attribute_types",
        db_column="root",
    )
    child_order = models.IntegerField("Child Order", default=0, db_column="child_order")
    gid = models.UUIDField("GID", db_column="gid")
    name = models.CharField(max_length=255, db_column="name")
    description = models.TextField(db_column="description", null=True)
    last_updated = models.DateTimeField("Last Updated", db_column="last_updated", auto_now=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        managed = False
        db_table = "link_attribute_type"
        verbose_name_plural = "Link Attribute Types"
