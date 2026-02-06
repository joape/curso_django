from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    inscriptos = models.IntegerField()
    profesor = models.CharField(max_length=50)
    adjunto= models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} ({self.inscriptos})"