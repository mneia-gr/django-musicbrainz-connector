from django.db import models


class Area(models.Model):
    """
    PostgreSQL Definition
    ---------------------

    The :code:`area` table is defined in the MusicBrainz Server as:

    .. code-block:: sql

        CREATE TABLE area ( -- replicate (verbose)
            id                  SERIAL, -- PK
            gid                 uuid NOT NULL,
            name                VARCHAR NOT NULL,
            type                INTEGER, -- references area_type.id
            edits_pending       INTEGER NOT NULL DEFAULT 0 CHECK (edits_pending >=0),
            last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
            begin_date_year     SMALLINT,
            begin_date_month    SMALLINT,
            begin_date_day      SMALLINT,
            end_date_year       SMALLINT,
            end_date_month      SMALLINT,
            end_date_day        SMALLINT,
            ended               BOOLEAN NOT NULL DEFAULT FALSE
            CHECK (
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
            comment             VARCHAR(255) NOT NULL DEFAULT ''
        );

    """

    id = models.IntegerField("ID", primary_key=True, db_column="id")
    gid = models.UUIDField("GID", db_column="gid")
    name = models.CharField(max_length=255, db_column="name")
    type = models.ForeignKey("AreaType", db_column="type", on_delete=models.PROTECT)
    edits_pending = models.PositiveIntegerField("Edits Pending", db_column="edits_pending", default=0)
    last_updated = models.DateTimeField("Last Updated", db_column="last_updated")
    begin_date_year = models.SmallIntegerField("Begin Date Year", null=True)
    begin_date_month = models.SmallIntegerField("Begin Date Month", null=True)
    begin_date_day = models.SmallIntegerField("Begin Date Day", null=True)
    end_date_year = models.SmallIntegerField("End Date Year", null=True)
    end_date_month = models.SmallIntegerField("End Date Month", null=True)
    end_date_day = models.SmallIntegerField("End Date Day", null=True)
    ended = models.BooleanField("Ended?", default=False)
    comment = models.CharField(max_length=255, db_column="comment", default="")

    def __str__(self) -> str:
        return self.name

    class Meta:
        managed = False
        db_table = "area"
        verbose_name_plural = "Areas"
        ordering = ["name"]
