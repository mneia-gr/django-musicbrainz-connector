"""
CREATE TABLE link_type ( -- replicate
    id                  SERIAL,
    parent              INTEGER, -- references link_type.id
    child_order         INTEGER NOT NULL DEFAULT 0,
    gid                 UUID NOT NULL,
    entity_type0        VARCHAR(50) NOT NULL,
    entity_type1        VARCHAR(50) NOT NULL,
    name                VARCHAR(255) NOT NULL,
    description         TEXT,
    link_phrase         VARCHAR(255) NOT NULL,
    reverse_link_phrase VARCHAR(255) NOT NULL,
    long_link_phrase    VARCHAR(255) NOT NULL,
    last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    is_deprecated       BOOLEAN NOT NULL DEFAULT false,
    has_dates           BOOLEAN NOT NULL DEFAULT true,
    entity0_cardinality SMALLINT NOT NULL DEFAULT 0,
    entity1_cardinality SMALLINT NOT NULL DEFAULT 0
);
"""

from django.db import models


class LinkType(models.Model):
    id = models.IntegerField("ID", primary_key=True, db_column="id")
    parent = models.ForeignKey("self", db_column="parent", null=True, on_delete=models.PROTECT)
    child_order = models.IntegerField("Child Order", db_column="child_order", default=0)
    gid = models.UUIDField("GID", db_column="gid")
    entity_type0 = models.CharField("Entity Type 0", max_length=50, db_column="entity_type0")
    entity_type1 = models.CharField("Entity Type 1", max_length=50, db_column="entity_type1")
    name = models.CharField(max_length=255, db_column="name")
    description = models.TextField(db_column="description")
    link_phrase = models.CharField("Link Phrase", max_length=255, db_column="link_phrase")
    reverse_link_phrase = models.CharField("Reverse Link Phrase", max_length=255, db_column="reverse_link_phrase")
    long_link_phrase = models.CharField("Long Link Phrase", max_length=255, db_column="long_link_phrase")
    last_updated = models.DateTimeField("Last Updated", db_column="last_updated", auto_now=True)
    is_deprecated = models.BooleanField("Is Deprecated?", default=False, db_column="is_deprecated")
    has_dates = models.BooleanField("Has Dates?", default=True, db_column="has_dates")
    entity0_cardinality = models.SmallIntegerField("Entity 0 Cardinality", default=0, db_column="entity0_cardinality")
    entity1_cardinality = models.SmallIntegerField("Entity 1 Cardinality", default=0, db_column="entity1_cardinality")

    def __str__(self) -> str:
        return f"{self.name}: {self.entity_type0} -> {self.entity_type1}"

    class Meta:
        managed = False
        db_table = "link_type"
        verbose_name_plural = "Link Types"
