from django.db import models


class AreaType(models.Model):
    """
    PostgreSQL Definition
    ---------------------

    The :code:`area_type` table is defined in the MusicBrainz Server as:

    .. code-block:: sql

        CREATE TABLE area_type ( -- replicate
            id                  SERIAL, -- PK
            name                VARCHAR(255) NOT NULL,
            parent              INTEGER, -- references area_type.id
            child_order         INTEGER NOT NULL DEFAULT 0,
            description         TEXT,
            gid                 uuid NOT NULL
        );

    """

    id = models.IntegerField("ID", primary_key=True, db_column="id")
    name = models.CharField(max_length=255, db_column="name")
    parent = models.ForeignKey("self", db_column="parent", null=True, on_delete=models.PROTECT)
    child_order = models.IntegerField("Child Order", db_column="child_order")
    description = models.TextField(db_column="description", null=True)
    gid = models.UUIDField("GID", db_column="gid")

    def __str__(self) -> str:
        return self.name

    class Meta:
        managed = False
        db_table = "area_type"
        verbose_name_plural = "Area Types"
        ordering = ["name"]