from django.db import models


class Link(models.Model):
    """
    PostgreSQL Definition
    ---------------------

    The :code:`link` table is defined in the MusicBrainz Server as:

    .. code-block:: sql

        CREATE TABLE link ( -- replicate
            id                  SERIAL,
            link_type           INTEGER NOT NULL, -- references link_type.id
            begin_date_year     SMALLINT,
            begin_date_month    SMALLINT,
            begin_date_day      SMALLINT,
            end_date_year       SMALLINT,
            end_date_month      SMALLINT,
            end_date_day        SMALLINT,
            attribute_count     INTEGER NOT NULL DEFAULT 0,
            created             TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
            ended               BOOLEAN NOT NULL DEFAULT FALSE
            CONSTRAINT link_ended_check CHECK (
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
            )
        );
    """

    id = models.IntegerField("ID", primary_key=True, db_column="id")
    link_type = models.ForeignKey(
        "LinkType",
        verbose_name="Type",
        related_name="links",
        on_delete=models.PROTECT,
        db_column="link_type",
    )
    begin_date_year = models.SmallIntegerField("Begin Date Year", null=True, db_column="begin_date_year")
    begin_date_month = models.SmallIntegerField("Begin Date Month", null=True, db_column="begin_date_month")
    begin_date_day = models.SmallIntegerField("Begin Date Day", null=True, db_column="begin_date_day")
    end_date_year = models.SmallIntegerField("End Date Year", null=True, db_column="end_date_year")
    end_date_month = models.SmallIntegerField("End Date Month", null=True, db_column="end_date_month")
    end_date_day = models.SmallIntegerField("End Date Day", null=True, db_column="end_date_day")
    attribute_count = models.IntegerField("Attribute Count", db_column="attribute_count", default=0)
    created = models.DateTimeField("Created", db_column="created")
    ended = models.BooleanField("Ended?", db_column="ended", default=False)

    class Meta:
        managed = False
        db_table = "link"
        verbose_name_plural = "Links"
