"""
.. module:: Language

PostgreSQL Definition
---------------------

The :code:`language` table is defined in the MusicBrainz Server as:

.. code-block:: sql

    CREATE TABLE language ( -- replicate
        id                  SERIAL,
        iso_code_2t         CHAR(3), -- ISO 639-2 (T)
        iso_code_2b         CHAR(3), -- ISO 639-2 (B)
        iso_code_1          CHAR(2), -- ISO 639
        name                VARCHAR(100) NOT NULL,
        frequency           SMALLINT NOT NULL DEFAULT 0,
        iso_code_3          CHAR(3)  -- ISO 639-3
    );

"""

from django.db import models


class Language(models.Model):
    id = models.IntegerField("ID", primary_key=True, db_column="id")
    iso_code_2t = models.CharField("ISO Code 2T", max_length=3, null=True, blank=True, db_column="iso_code_2t")
    iso_code_2b = models.CharField("ISO Code 2B", max_length=3, null=True, blank=True, db_column="iso_code_2b")
    iso_code_1 = models.CharField("ISO Code 1", max_length=2, null=True, blank=True, db_column="iso_code_1")
    name = models.CharField("Name", max_length=100, db_column="name")
    frequency = models.SmallIntegerField("Frequency", default=0, db_column="frequency")
    iso_code_3 = models.CharField("ISO Code 3", max_length=3, null=True, blank=True, db_column="iso_code_3")

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = "language"
        verbose_name_plural = "Languages"
        ordering = ["name"]
