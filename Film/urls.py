from django.contrib import admin
from django.urls import path, include
from Film.views import *

urlpatterns = [
    path('', HomePage),
    path('watch/<int:pk>/', Watch),
    path('update/<int:pk>/', UpdateWatch),
    path('checkCache/', CheckCache),
    path('upload/', Upload),
    
    
]