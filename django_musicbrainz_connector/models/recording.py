"""
CREATE TABLE recording ( -- replicate (verbose)
    id                  SERIAL,
    gid                 UUID NOT NULL,
    name                VARCHAR NOT NULL,
    artist_credit       INTEGER NOT NULL, -- references artist_credit.id
    length              INTEGER CHECK (length IS NULL OR length > 0),
    comment             VARCHAR(255) NOT NULL DEFAULT '',
    edits_pending       INTEGER NOT NULL DEFAULT 0 CHECK (edits_pending >= 0),
    last_updated        TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    video               BOOLEAN NOT NULL DEFAULT FALSE
);
"""

from django.db import models

from django_musicbrainz_connector.models.link_type import LinkType
from django_musicbrainz_connector.models.recording_work_link import RecordingWorkLink


class Recording(models.Model):
    id = models.IntegerField("ID", primary_key=True, db_column="id")
    gid = models.UUIDField("GID", db_column="gid")
    name = models.CharField(max_length=255, db_column="name")
    artist_credit = models.ForeignKey(
        "ArtistCredit",
        verbose_name="Artist Credit",
        related_name="recordings",
        on_delete=models.PROTECT,
        db_column="artist_credit",
    )
    length = models.PositiveIntegerField(null=True, db_column="length")
    comment = models.CharField("Comment", max_length=255, default="", db_column="comment")
    edits_pending = models.PositiveIntegerField("Edits Pending", db_column="edits_pending", default=0)
    last_updated = models.DateTimeField("Last Updated", db_column="last_updated")
    video = models.BooleanField(default=False, db_column="video")

    def __str__(self) -> str:
        return self.name

    @property
    def musicbrainz_url(self) -> str:
        """Returns a URL to open the recording on the MusicBrainz website."""
        return f"https://musicbrainz.org/recording/{self.gid}"

    @property
    def recording_of(self):
        """Return the works that this recording is a recording of."""
        performance = LinkType.objects.get(name="performance", entity_type0="recording", entity_type1="work")
        recording_work_links = RecordingWorkLink.objects.filter(recording=self, link__link_type=performance)
        return [link.work for link in recording_work_links]

    class Meta:
        managed = False
        db_table = "recording"
        verbose_name_plural = "Recordings"
