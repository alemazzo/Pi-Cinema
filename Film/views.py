from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.views.generic import CreateView, View
from django.core import serializers
from .models import Film, FilmUploadForm
import os, shutil, string, random, datetime
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
import threading as th    
import subprocess

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

# Create your views here.
def HomePage(request):

    films = Film.objects.all()    
    films = serializers.serialize('json', films)
    return JsonResponse(films, safe = False)

def Watch(request, id):

    film = Film.objects.get(id=id)
    if film.cachePath == "":
        link = f"./Static/tmp/{randomString()}.mp4"
        film.lastWatch = timezone.now()
        film.cachePath = link.replace('./Static/', '')
        film.save()
        shutil.copyfile(film.videoPath, link)
        
    return redirect(f'/api/film/{film.pk}')


def UpdateWatch(request, id):
    film = Film.objects.get(id=id)
    film.lastWatch = timezone.now()
    film.save()
    return HttpResponse("UPDATED")

def CheckCache(request):
    films = Film.objects.all()
    for film in films:
        if film.cachePath != "" and (timezone.now() - film.lastWatch).total_seconds() > 20:
            os.remove(f'./Static/{film.cachePath}')
            film.cachePath = ""
            film.save()
    return HttpResponse("")





def create_frame(path, f):
    print("Estrazione copertina...")
    #cap = cv2.VideoCapture(path)
    f.imagePath = f'thumbnails/films/{f.pk}.jpg'
    #i=0
    #for i in range(500):
    #    ret, frame = cap.read()
    #    
    #    if ret == False:
    #        break
    #    if i == 499:
    #        cv2.imwrite('Static/' + f.imagePath, frame)
    subprocess.call(['ffmpeg', '-i', f.videoPath, '-ss', '00:00:03.000', '-vframes', '1', './Static/' + f.imagePath])
    f.save()
    print("Fine")
    pass

def get_duration(file):
    print("")
    #clip = VideoFileClip(file)
    #dur = int(clip.duration)
    #hrs, mins, secs = dur//60//60, dur//60%60, dur%60
    #hrs = "0"+str(hrs) if(hrs<10) else str(hrs)
    #mins = "0"+str(mins) if(mins<10) else str(mins)
    #secs = "0"+str(secs) if(secs<10) else str(secs)
    #return hrs +":"+ mins +":"+ secs

def handle_film(pk, path, dest = "/home/pi/Pi-Cinema/DATA/"):
    print("Creazione film...")
    f = Film.objects.get(pk = pk)
    f.videoPath = f'{dest}{f.pk}-{f.title}.mp4'
    f.save()
    os.rename(path, f.videoPath)
    #f.duration = get_duration(f.videoPath)
    f.save()
    create_frame(f.videoPath, f)    
    
   

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
            th.Thread(target=handle_film, args=(pk, file )).start()
            return HttpResponse("SAVED")

        return HttpResponse("ERROR")

    


