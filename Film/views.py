from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.views.generic import CreateView, View
from django.core import serializers
from .models import Film, FilmUploadForm
import os, shutil, string, random, datetime
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from multiprocessing import Process
from threading import Thread
import subprocess
from django.conf import settings
import time


def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

# Create your views here.
def HomePage(request):

    films = Film.objects.all()    
    films = serializers.serialize('json', films)
    return JsonResponse(films, safe = False)


def cacheFile(src, dst, pk):
    print("Start caching file")
    shutil.copy2(src, dst)
    print("File Cached")
    film = Film.objects.get(id=pk)
    film.caching = False
    film.save()


def Watch(request, pk):

    film = Film.objects.get(id=pk)
    if film.cachePath == "":
        link = f"./media/tmp/{randomString()}.mp4"
        film.lastWatch = timezone.now()
        film.cachePath = link.replace('./media/', '')
        film.caching = True
        film.save()
        Thread(target = cacheFile, args = (film.videoPath, link, pk, ), daemon = True).start()
        return HttpResponse("None")
    else:
        if film.caching == True:
            return HttpResponse("None")
        else:
            return redirect(f'/api/film/{film.pk}')


def UpdateWatch(request, pk):
    film = Film.objects.get(id=pk)
    film.lastWatch = timezone.now()
    film.save()
    return HttpResponse("UPDATED")

def CheckCache(request):
    films = Film.objects.all()
    for film in films:
        if film.cachePath != "" and (timezone.now() - film.lastWatch).total_seconds() > 20:
            os.remove(f'./media/{film.cachePath}')
            film.cachePath = ""
            film.save()
    return HttpResponse("")





def create_frame(path, f):
    print("Estrazione copertina...")
    #cap = cv2.VideoCapture(path)
    f.imagePath = f'thumbnails/films/{f.pk}.jpg'
    subprocess.call(['ffmpeg', '-i', f.videoPath, '-ss', '00:00:03.000', '-vframes', '1', './media/' + f.imagePath])

def get_duration(file):
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", file],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    return time.strftime('%H:%M:%S', time.gmtime(int(result.stdout)))

def handle_film(pk, path):
    print("Creazione film...")
    dest = settings.DATA_BASE_PATH + 'film/'
    path = '.' + path
    f = Film.objects.get(pk = pk)
    f.videoPath = f'{dest}{f.pk}-{f.title}.mp4'
    os.rename(path, f.videoPath)
    f.duration = get_duration(f.videoPath)
    create_frame(f.videoPath, f)    
    f.creating = False
    f.save()
    print("Fine")
    

@csrf_exempt
def Upload(request):

    if request.method == "GET":
        return render(request, 'uploadfilmform.html', {"form" : FilmUploadForm()})
    else:
        form = FilmUploadForm(request.POST, request.FILES)
        if form.is_valid():
            print("Salvataggio file...")
            file = form.save().file.url
            pk = form.instance.pk
            Thread(target = handle_film, args = (pk, file,), daemon = True).start()
            return HttpResponse("SAVED")

        return HttpResponse("ERROR")

    


