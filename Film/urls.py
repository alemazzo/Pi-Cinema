from django.contrib import admin
from django.urls import path, include
from Film.views import *

urlpatterns = [
    path('', HomePage),
    path('watch/<int:id>/', Watch),
    path('update/<int:id>/', UpdateWatch),
    path('checkCache/', CheckCache),
    path('upload/', Upload),
    
    
]