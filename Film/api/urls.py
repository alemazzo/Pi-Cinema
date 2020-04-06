from django.urls import include, path
from django.contrib.auth.models import User
from .views import *

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', AllFilm.as_view({'get': 'list'})),
    path('<int:pk>', AllFilm.as_view({'get': 'retrieve'})),
]