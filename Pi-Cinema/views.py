from django.shortcuts import render, HttpResponse
from django.views.generic import CreateView, View

def HomePage(request):

    return render(request, 'index.html')
