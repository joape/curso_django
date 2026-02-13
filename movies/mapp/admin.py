from django.contrib import admin
from .models import *

class GenderAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')

class CompanyAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')

class MovieAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')
    list_display = ('id', 'pelicula', 'company', 'premiere', 'sinopsis', 'estrellas')
    list_filter = ('genders', 'company')

# Register your models here.
admin.site.register(Gender, GenderAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Movie, MovieAdmin)