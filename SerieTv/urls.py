from django.contrib import admin
from django.urls import path, include
from SerieTv.views import *

urlpatterns = [
    path('', Series),
    path('<int:id_serie>/', Stagioni),
    path('<int:id_serie>/<int:id_stagione>/', Episodi),
    path('<int:id_serie>/<int:id_stagione>/<int:id_episodio>/', Watch),
    path('upload/<int:id_serie>/<int:id_stagione>/', Upload),
    path('update/<int:id>/', UpdateWatch),
    path('checkCache/', CheckCache),
    
    
]