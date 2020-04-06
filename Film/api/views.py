from Film.models import Film
from rest_framework import serializers, viewsets
from .serializers import FilmSerializer


# ViewSets define the view behavior.
class AllFilm(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
