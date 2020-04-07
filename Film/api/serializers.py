from rest_framework import serializers, viewsets
from Film.models import Film

# Serializers define the API representation.
class FilmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Film
        fields = ['pk','title', 'year', 'videoPath', 'imagePath', 'cachePath', 'lastWatch', 'duration', 'caching']
