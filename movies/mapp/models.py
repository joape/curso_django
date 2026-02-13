from django.db import models
from django.contrib import admin
from django.utils.html import format_html

# Create your models here.
class Gender(models.Model):
    name = models.CharField(max_length=50, verbose_name="Género")
    created = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name_plural = "Géneros"
        verbose_name = "Género"
        ordering = ["name"]

class Company(models.Model):
    name = models.CharField(max_length=50, verbose_name="Compañía")
    created = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Compañías"
        verbose_name = "Compañía"
        ordering = ["name"]

class Movie(models.Model):
    name = models.CharField(max_length=50, verbose_name="Película")
    description = models.TextField(verbose_name="Sinopsis")
    RATING = [
        (1, "Mala"),
        (2, "Mediocre"),
        (3, "Buena"),
        (4, "Muy Buena"),
        (5, "Excelente"),        
    ]
    rating = models.PositiveSmallIntegerField(choices=RATING)
    premiere = models.PositiveSmallIntegerField(verbose_name="Año de Estreno", null=False, blank=False)
    company = models.ForeignKey(Company, verbose_name="Compañía", on_delete=models.CASCADE)
    genders = models.ManyToManyField(Gender, verbose_name="Géneros")
    image = models.ImageField(verbose_name="Cover", upload_to="covers", null=True, blank=True)
    created = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now_add=True)    

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Películas"
        verbose_name = "Película"
        ordering = ["name"]

    @admin.display(ordering="name")
    def pelicula(self):
        return format_html(f"<span style='color:green';>{self.name.upper()}</span>")
    
    @admin.display(ordering="description")
    def sinopsis(self):
        return format_html(f"<span style='color:blue';>{self.description[:20]+"..."}</span>")
    
    @admin.display(ordering="rating")
    def estrellas(self):
        st = self.rating  * "✭"
        return format_html(f"<span style='color:red';>{st}</span>")

