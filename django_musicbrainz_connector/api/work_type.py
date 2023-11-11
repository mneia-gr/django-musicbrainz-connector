from rest_framework import serializers, viewsets

from django_musicbrainz_connector.models import WorkType


class WorkTypeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = WorkType
        fields = "__all__"


class WorkTypeViewSet(viewsets.ModelViewSet):
    queryset = WorkType.objects.all()
    serializer_class = WorkTypeSerializer
    http_method_names = ["get"]