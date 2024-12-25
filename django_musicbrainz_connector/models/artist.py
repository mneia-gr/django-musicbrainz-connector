from django.db import models


class Artist(models.Model):
    """
    PostgreSQL Definition
    ---------------------

    The :code:`artist` table is defined in the MusicBrainz Server as:

    .. code-block:: sql

        CREATE TABLE artist ( -- replicate (verbose)
            id                  SERIAL,
            gid                 UUID NOT NULL,
            name                VARCHAR NOT NULL,
            sort_name           VARCHAR NOT NULL,
            begin_date_year     SMALLINT,
            begin_date_month    SMALLINT,
            begin_date_day      SMALLINT,
            end_date_year       SMALLINT,
            end_date_month      SMALLINT,
            end_date_day        SMALLINT,
            type                INTEGER, -- references artist_type.id
            area                INTEGER, -- references area.id
            gender              INTEGER, -- references gender.id
            comment             VARCHAR(255) NOT NULL DEFAULT '',
            edits_pending       INTEGER NOT NULL DEFAULT 0 CHECK (edits_pending >= 0),
            last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
            ended               BOOLEAN NOT NULL DEFAULT FALSE
            CONSTRAINT artist_ended_check CHECK (
                (
                -- If any end date fields are not null, then ended must be true
                (end_date_year IS NOT NULL OR
                end_date_month IS NOT NULL OR
                end_date_day IS NOT NULL) AND
                ended = TRUE
                ) OR (
                -- Otherwise, all end date fields must be null
                (end_date_year IS NULL AND
                end_date_month IS NULL AND
                end_date_day IS NULL)
                )
            ),
            begin_area          INTEGER, -- references area.id
            end_area            INTEGER -- references area.id
        );
    """

    id = models.IntegerField("ID", primary_key=True, db_column="id")
    gid = models.UUIDField("GID", db_column="gid")
    name = models.CharField(max_length=255, db_column="name")
    sort_name = models.CharField("Sort Name", max_length=255, db_column="sort_name")
    begin_date_year = models.SmallIntegerField("Begin Date Year", null=True)
    begin_date_month = models.SmallIntegerField("Begin Date Month", null=True)
    begin_date_day = models.SmallIntegerField("Begin Date Day", null=True)
    end_date_year = models.SmallIntegerField("End Date Year", null=True)
    end_date_month = models.SmallIntegerField("End Date Month", null=True)
    end_date_day = models.SmallIntegerField("End Date Day", null=True)
    type = models.ForeignKey("ArtistType", db_column="type", on_delete=models.PROTECT)
    area = models.ForeignKey("Area", db_column="area", on_delete=models.PROTECT)
    gender = models.ForeignKey("Gender", db_column="gender", on_delete=models.PROTECT)
    comment = models.CharField(max_length=255, db_column="comment", default="")
    edits_pending = models.PositiveIntegerField("Edits Pending", db_column="edits_pending", default=0)
    last_updated = models.DateTimeField("Last Updated", db_column="last_updated")
    ended = models.BooleanField("Ended?", default=False)
    begin_area = models.ForeignKey(
        "Area",
        verbose_name="Begin Area",
        db_column="begin_area",
        on_delete=models.PROTECT,
        related_name="artists_begin_area",
    )
    end_area = models.ForeignKey(
        "Area",
        verbose_name="End Area",
        db_column="end_area",
        on_delete=models.PROTECT,
        related_name="artists_end_area",
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        managed = False
        db_table = "artist"
        verbose_name_plural = "Artist"
        ordering = ["name"]
