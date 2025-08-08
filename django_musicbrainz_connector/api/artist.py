from rest_framework import serializers, viewsets
from rest_framework.exceptions import NotFound

from django_musicbrainz_connector.api import DjangoMusicBrainzConnectorPagination
from django_musicbrainz_connector.models import Artist
from django_musicbrainz_connector.utils import get_musicbrainz_identifier_type


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        # Dont serialize m2m fields
        exclude = ["credits"]


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    http_method_names = ["get"]
    pagination_class = DjangoMusicBrainzConnectorPagination

    def get_object(self):
        """
        Overriding the default `get_object` method of `ModelViewSet` to allow GET by any unique identifier for an
        Artist, either the MusicBrainz ID (an integer), or the GID (a UUID), or the name (a string). Either of these
        calls should return the same result:

            GET /api/artists/738375/
            GET /api/artists/f61458a1-412e-46c0-ad76-d2e0c39a14ff/
            GET /api/artists/Κώστας Ουράνης/
        """
        pk = self.kwargs["pk"]
        pk_type = get_musicbrainz_identifier_type(pk)
        params = {pk_type: pk}
        try:
            return Artist.objects.get(**params)
        except Artist.DoesNotExist:
            raise NotFound
