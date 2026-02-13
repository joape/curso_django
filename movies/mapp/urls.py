from django.urls import path, include
from .views import *

urlpatterns = [
    path("", HomeView.as_view(), name="home"),    

    path("companias/", CompanyList.as_view(), name="companias"),    
    path("generos/", GenderList.as_view(), name="generos"),   

    path("peliculas/", MovieList.as_view(), name="peliculas"),    
    path("pelicula_create/", MovieCreate.as_view(), name="pelicula_create"),    
    path("pelicula_update/<int:pk>/", MovieUpdate.as_view(), name="pelicula_update"),    
    path("pelicula_delete/<int:pk>/", MovieDelete.as_view(), name="pelicula_delete"),    
]

