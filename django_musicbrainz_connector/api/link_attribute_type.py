from rest_framework import serializers, viewsets

from django_musicbrainz_connector.api import DjangoMusicBrainzConnectorPagination
from django_musicbrainz_connector.models import LinkAttributeType


class LinkAttributeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkAttributeType
        fields = "__all__"


class LinkAttributeTypeViewSet(viewsets.ModelViewSet):
    queryset = LinkAttributeType.objects.all()
    serializer_class = LinkAttributeTypeSerializer
    http_method_names = ["get"]
    pagination_class = DjangoMusicBrainzConnectorPagination
