"""
.. module:: artist_credit

PostgreSQL Definition
---------------------

The :code:`artist_credit` table is defined in the MusicBrainz server as:

.. code-block:: sql

    CREATE TABLE artist_credit ( -- replicate
        id                  SERIAL,
        name                VARCHAR NOT NULL,
        artist_count        SMALLINT NOT NULL,
        ref_count           INTEGER DEFAULT 0,
        created             TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
        edits_pending       INTEGER NOT NULL DEFAULT 0 CHECK (edits_pending >= 0),
        gid                 UUID NOT NULL
    );

"""

from django.db import models


class ArtistCredit(models.Model):
    id = models.IntegerField("ID", primary_key=True, db_column="id")
    name = models.CharField("Name", max_length=255, db_column="name")
    artist_count = models.SmallIntegerField("Artist Count", db_column="artist_count")
    ref_count = models.IntegerField("Ref Count", db_column="ref_count")
    created = models.DateTimeField("Created", db_column="created")
    edits_pending = models.PositiveIntegerField("Edits Pending", db_column="edits_pending", default=0)
    gid = models.UUIDField("GID", db_column="gid")

    def __str__(self) -> str:
        return self.name

    class Meta:
        managed = False
        db_table = "artist_credit"
        verbose_name_plural = "Artist Credits"
