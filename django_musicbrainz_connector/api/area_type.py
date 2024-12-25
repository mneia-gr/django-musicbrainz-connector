from rest_framework import serializers, viewsets
from rest_framework.exceptions import NotFound

from django_musicbrainz_connector.api import DjangoMusicBrainzConnectorPagination
from django_musicbrainz_connector.models import AreaType
from django_musicbrainz_connector.utils import get_musicbrainz_identifier_type


class AreaTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaType
        fields = "__all__"


class AreaTypeViewSet(viewsets.ModelViewSet):
    queryset = AreaType.objects.all()
    serializer_class = AreaTypeSerializer
    http_method_names = ["get"]
    pagination_class = DjangoMusicBrainzConnectorPagination

    def get_object(self):
        """
        Overriding the default `get_object` method of `ModelViewSet` to allow GET by any unique identifier for an Area
        Type, either the MusicBrainz ID (an integer), or the GID (a UUID), or the name (a string). Call with something
        like:

            GET /api/area-types/Country/
        """
        pk = self.kwargs["pk"]
        pk_type = get_musicbrainz_identifier_type(pk)
        params = {pk_type: pk}
        try:
            return AreaType.objects.get(**params)
        except AreaType.DoesNotExist:
            raise NotFound
