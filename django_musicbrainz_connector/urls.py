from django.urls import include, path
from rest_framework import routers

from django_musicbrainz_connector.api.area import AreaViewSet
from django_musicbrainz_connector.api.area_type import AreaTypeViewSet
from django_musicbrainz_connector.api.artist import ArtistViewSet
from django_musicbrainz_connector.api.artist_credit import ArtistCreditViewSet
from django_musicbrainz_connector.api.artist_type import ArtistTypeViewSet
from django_musicbrainz_connector.api.gender import GenderViewSet
from django_musicbrainz_connector.api.language import LanguageViewSet
from django_musicbrainz_connector.api.link import LinkViewSet
from django_musicbrainz_connector.api.link_type import LinkTypeViewSet
from django_musicbrainz_connector.api.medium import MediumViewSet
from django_musicbrainz_connector.api.medium_format import MediumFormatViewSet
from django_musicbrainz_connector.api.recording import RecordingViewSet
from django_musicbrainz_connector.api.recording_work_link import RecordingWorkLinkViewSet
from django_musicbrainz_connector.api.release import ReleaseViewSet
from django_musicbrainz_connector.api.release_group import ReleaseGroupViewSet
from django_musicbrainz_connector.api.release_group_primary_type import ReleaseGroupPrimaryTypeViewSet
from django_musicbrainz_connector.api.release_packaging import ReleasePackagingViewSet
from django_musicbrainz_connector.api.release_status import ReleaseStatusViewSet
from django_musicbrainz_connector.api.script import ScriptViewSet
from django_musicbrainz_connector.api.track import TrackViewSet
from django_musicbrainz_connector.api.work import WorkViewSet
from django_musicbrainz_connector.api.work_type import WorkTypeViewSet

router = routers.DefaultRouter()
router.register(r"area-types", AreaTypeViewSet)
router.register(r"areas", AreaViewSet)
router.register(r"artist-credits", ArtistCreditViewSet)
router.register(r"artist-types", ArtistTypeViewSet)
router.register(r"artists", ArtistViewSet)
router.register(r"genders", GenderViewSet)
router.register(r"languages", LanguageViewSet)
router.register(r"links", LinkViewSet)
router.register(r"link-types", LinkTypeViewSet)
router.register(r"media", MediumViewSet)
router.register(r"medium-formats", MediumFormatViewSet)
router.register(r"recordings", RecordingViewSet)
router.register(r"recording-work-links", RecordingWorkLinkViewSet)
router.register(r"releases", ReleaseViewSet)
router.register(r"release-groups", ReleaseGroupViewSet)
router.register(r"release-group-primary-types", ReleaseGroupPrimaryTypeViewSet)
router.register(r"release-packaging", ReleasePackagingViewSet)
router.register(r"release-statuses", ReleaseStatusViewSet)
router.register(r"scripts", ScriptViewSet)
router.register(r"tracks", TrackViewSet)
router.register(r"works", WorkViewSet)
router.register(r"work-types", WorkTypeViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
