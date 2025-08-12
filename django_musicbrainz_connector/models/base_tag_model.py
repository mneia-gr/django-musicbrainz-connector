from django.db import models


class TagModel(models.Model):
    """
    PostgreSQL Definition
    ---------------------

    The :code:`M_tag` table is defined in the MusicBrainz Server as:

    .. code-block:: sql

        CREATE TABLE M_tag ( -- replicate (verbose)
            M                   INTEGER NOT NULL, -- PK, references M.id
            tag                 INTEGER NOT NULL, -- PK, references tag.id
            count               INTEGER NOT NULL,
            last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW()
        );

    """

    tag = models.ForeignKey("Tag", db_column="tag", on_delete=models.PROTECT)
    count = models.IntegerField("Count", db_column="count")
    last_updated = models.DateTimeField(db_column="last_updated")

    class Meta:
        abstract = True
