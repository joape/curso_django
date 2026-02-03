from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("acerca/", views.acerca, name="acerca"),
    path("contacto/", views.contacto, name="contacto"),

    path("cursos/", views.cursos, name="cursos"),

    path("aero/", views.aero, name="aero"), 
    path("aero_api/", views.aero_api, name="aero_api"),  

    path("bienvenido/", views.bienvenido, name="bienvenido"),
    path("bienvenido2/", views.bienvenido2, name="bienvenido2"), 

    path("uncurso/<int:id>/", views.uncurso, name="uncurso"),
    path("allcursos/", views.allCursos, name="allcursos"),  
    path("nuevocurso/", views.nuevoCurso, name="nuevocurso"), 
]