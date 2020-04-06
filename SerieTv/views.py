from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
from django.views.generic import CreateView, View
from .models import Serie, Stagione, Episodio
import os, shutil, string, random, datetime
from django.utils import timezone
from Film.models import FilmUploadForm
from django.views.decorators.csrf import csrf_exempt
import threading as th

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

# Create your views here.
def Series(request):
    #All Series
    series = Serie.objects.all()    
    return render(request, 'serie.html', {"series" : series})

# Create your views here.
def Stagioni(request, id_serie):
    #All Stagioni
    serie = Serie.objects.get(id = id_serie)
    stagioni = Stagione.objects.all().filter(serie = serie)    
    return render(request, 'stagioni.html', {"stagioni" : stagioni})

# Create your views here.
def Episodi(request, id_serie, id_stagione):
    #All Stagioni
    serie = Serie.objects.get(id = id_serie)
    stagione = Stagione.objects.get(id = id_stagione)  
    episodi = Episodio.objects.all().filter(stagione = stagione) 
    return render(request, 'episodi.html', {"episodi" : episodi, "episode" : episodi[0]})

def Watch(request, id_serie, id_stagione, id_episodio):

    episodio = Episodio.objects.get(id=id_episodio)
    if episodio.cachePath == "":
        link = f"./Static/tmp/{randomString()}.mp4"
        episodio.lastWatch = timezone.now()
        episodio.cachePath = link.replace('./Static/', '')
        episodio.save()
        shutil.copyfile(episodio.videoPath, link)
        
    link = episodio.cachePath
    
    return render(request, 'watchserie.html', {"episodio" : episodio, "link" : link})


def UpdateWatch(request, id):
    episodio = Episodio.objects.get(id=id)
    episodio.lastWatch = timezone.now()
    episodio.save()
    return HttpResponse("UPDATED")

def CheckCache(request):
    episodi = Episodio.objects.all()
    for episodio in episodi:
        if episodio.cachePath != "" and (timezone.now() - episodio.lastWatch).total_seconds() > 20:
            os.remove(f'./Static/{episodio.cachePath}')
            episodio.cachePath = ""
            episodio.save()
    return HttpResponse("")





def create_frame(path, e):
    print("Estrazione copertina...")
    cap = cv2.VideoCapture(path)
    e.imagePath = f'thumbnails/serietv/{e.pk}.jpg'
    for i in range(500):
        ret, frame = cap.read()
        
        if ret == False:
            break
        if i == 499:
            cv2.imwrite('Static/' + e.imagePath, frame)
    e.save()
    print("Fine")
    pass

def handle_episodio(id_serie, id_stagione, title, path, dest = "C:\\Users\\alema\\Desktop\\StreamPi\\DATA\\"):
    print("Creazione episodio...")
    serie = Serie.objects.get(pk = id_serie)
    stagione = Stagione.objects.get(pk = id_stagione)
    e = Episodio()
    e.save()
    e.title = f'{title}'
    e.videoPath = f'{dest}{e.pk}-{e.title}.mp4'
    shutil.copyfile(path, e.videoPath)
    os.remove(path)
    create_frame(e.videoPath, e)        
   

@csrf_exempt
def Upload(request, id_serie, id_stagione):

    if request.method == "GET":
        return render(request, 'uploadepisodio.html', {"form" : FileUploadForm()})
    else:
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            print("Salvataggio file...")
            title = form.data['numero']
            file = form.save().file.url
            th.Thread(target=handle_episodio, args=(id_serie, id_stagione, title, file, )).start()
            return HttpResponse("SAVED")

        return HttpResponse("ERROR")

