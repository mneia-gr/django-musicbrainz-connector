from django.db import models


class Tag(models.Model):
    """
    PostgreSQL Definition
    ---------------------

    The :code:`tag` table is defined in the MusicBrainz Server as:

    .. code-block:: sql

        CREATE TABLE tag ( -- replicate (verbose)
            id                  SERIAL,
            name                VARCHAR(255) NOT NULL,
            ref_count           INTEGER NOT NULL DEFAULT 0
        );

    """

    id = models.IntegerField("ID", primary_key=True, db_column="id")
    name = models.CharField(max_length=255, db_column="name")
    ref_count = models.IntegerField("Ref Count", db_column="ref_count")

    def __str__(self) -> str:
        return self.name

    class Meta:
        managed = False
        db_table = "tag"
        verbose_name_plural = "Tags"
        ordering = ["name"]
