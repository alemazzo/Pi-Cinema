from django.db import models
from django import forms

# Create your models here.
class Film(models.Model):

    title = models.CharField(max_length=200)
    year = models.CharField(max_length=4, null=True)
    duration = models.TextField(null=True)
    videoPath = models.TextField()
    imagePath = models.TextField(null=True)
    cachePath = models.TextField(blank=True)
    lastWatch = models.DateTimeField(null=True)
    file = models.FileField(upload_to="upload", null=True)

    class Meta:
        verbose_name = ("Film")
        verbose_name_plural = ("Films")

    def __str__(self):
        return self.title


class FilmUploadForm(forms.ModelForm):

        class Meta:
                model = Film
                fields = ['title', 'year','file']