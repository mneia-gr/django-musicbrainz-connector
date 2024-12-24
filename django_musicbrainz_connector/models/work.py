from django.db import models

from django_musicbrainz_connector.models.link_type import LinkType
from django_musicbrainz_connector.models.recording_work_link import RecordingWorkLink


class Work(models.Model):
    """
    Model of a Work. In addition to the attributes that come from the MusicBrainz server, this model has a
    `musicbrainz_url` property that returns a link to open the work on the MusicBrainz website.

    PostgreSQL Definition
    ---------------------

    The :code:`work` table is defined in the MusicBrainz Server as:

    .. code-block:: sql

        CREATE TABLE work ( -- replicate (verbose)
            id                  SERIAL,
            gid                 UUID NOT NULL,
            name                VARCHAR NOT NULL,
            type                INTEGER, -- references work_type.id
            comment             VARCHAR(255) NOT NULL DEFAULT '',
            edits_pending       INTEGER NOT NULL DEFAULT 0 CHECK (edits_pending >= 0),
            last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
        );

    """

    id = models.IntegerField("ID", primary_key=True, db_column="id")
    gid = models.UUIDField(db_column="gid")
    name = models.CharField(max_length=255, db_column="name")
    type = models.ForeignKey("WorkType", db_column="type", on_delete=models.PROTECT)
    edits_pending = models.PositiveIntegerField("Edits Pending", db_column="edits_pending", default=0)
    last_updated = models.DateTimeField("Last Updated", db_column="last_updated")

    def __str__(self) -> str:
        return self.name

    @property
    def musicbrainz_url(self) -> str:
        """Returns a URL to open the work on the MusicBrainz website."""
        return f"https://musicbrainz.org/work/{self.gid}"

    @property
    def recordings(self):
        """Returns the recordings of this work."""
        performance = LinkType.objects.get(name="performance", entity_type0="recording", entity_type1="work")
        recording_work_links = RecordingWorkLink.objects.filter(work=self, link__link_type=performance)
        return [link.recording for link in recording_work_links]

    class Meta:
        managed = False
        db_table = "work"
        verbose_name_plural = "Works"
