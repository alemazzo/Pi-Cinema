from django.db import models

# Create your models here.
class Serie(models.Model):

    title = models.TextField(null=True)
    imagePath = models.TextField(null=True)

    def __str__(self):
        return self.title

class Stagione(models.Model):

    serie = models.ForeignKey(Serie, on_delete = models.CASCADE)
    numero = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.numero}'

class Episodio(models.Model):

    serie = models.ForeignKey(Serie, on_delete = models.CASCADE)
    stagione = models.ForeignKey(Stagione, on_delete = models.CASCADE)
    titolo = models.TextField(null=True)
    videoPath = models.TextField(null=True)
    imagePath = models.TextField(null=True)
    cachePath = models.TextField(blank=True)
    lastWatch = models.DateTimeField(null = True)

    def __str__(self):
        return f"{self.serie} - {self.stagione} - {self.numero}"




