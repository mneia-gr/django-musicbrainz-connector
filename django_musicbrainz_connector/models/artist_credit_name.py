from django.db import models


class ArtistCreditName(models.Model):
    """
    PostgreSQL Definition
    ---------------------

    The :code:`artist_credit_name` table is defined in the MusicBrainz Server as:

    .. code-block:: sql

        CREATE TABLE artist_credit_name ( -- replicate (verbose)
            artist_credit       INTEGER NOT NULL, -- PK, references artist_credit.id CASCADE
            position            SMALLINT NOT NULL, -- PK
            artist              INTEGER NOT NULL, -- references artist.id CASCADE
            name                VARCHAR NOT NULL,
            join_phrase         TEXT NOT NULL DEFAULT ''
        );
    """

    pk = models.CompositePrimaryKey("artist_credit", "position")
    artist_credit = models.ForeignKey(
        "ArtistCredit",
        verbose_name="Artist Credit",
        related_name="artist_credit_names",
        on_delete=models.PROTECT,
        db_column="artist_credit",
    )
    position = models.IntegerField("Position", db_column="position")
    artist = models.ForeignKey(
        "Artist",
        verbose_name="Artist",
        related_name="artist_credit_names",
        on_delete=models.PROTECT,
        db_column="artist",
    )
    name = models.CharField("Name", max_length=255, db_column="name")
    join_phrase = models.TextField("Join phrase", db_column="join_phrase")

    def __str__(self) -> str:
        return self.name

    class Meta:
        managed = False
        db_table = "artist_credit_name"
        verbose_name_plural = "Artist Credit Names"
        ordering = ["name"]
