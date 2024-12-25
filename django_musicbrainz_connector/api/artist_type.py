from rest_framework import serializers, viewsets
from rest_framework.exceptions import NotFound

from django_musicbrainz_connector.api import DjangoMusicBrainzConnectorPagination
from django_musicbrainz_connector.models import ArtistType
from django_musicbrainz_connector.utils import get_musicbrainz_identifier_type


class ArtistTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistType
        fields = "__all__"


class ArtistTypeViewSet(viewsets.ModelViewSet):
    queryset = ArtistType.objects.all()
    serializer_class = ArtistTypeSerializer
    http_method_names = ["get"]
    pagination_class = DjangoMusicBrainzConnectorPagination

    def get_object(self):
        """
        Overriding the default `get_object` method of `ModelViewSet` to allow GET by any unique identifier for an Artist
        Type, either the MusicBrainz ID (an integer), or the GID (a UUID), or the name (a string). Call with something
        like:

            GET /api/artist-types/Person/
        """
        pk = self.kwargs["pk"]
        pk_type = get_musicbrainz_identifier_type(pk)
        params = {pk_type: pk}
        try:
            return ArtistType.objects.get(**params)
        except ArtistType.DoesNotExist:
            raise NotFound
