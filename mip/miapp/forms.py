from django import forms
from django.forms import ModelForm
from .models import Curso

class FormularioCurso(ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'inscriptos']

    #nombre = forms.CharField(max_length=50, label="Nombre del Curso", help_text="Ingrese el nombre completo del curso")
    #inscriptos = forms.IntegerField(label="Cantidad de Inscriptos")
"""
    profesor = forms.CharField(max_length=100, label="Nombre del Profesor")
    solo_empresas= forms.BooleanField(required=False, label="Solo para Empresas?")
    TURNOS = (
        ('M', 'Mañana'), 
        ('T', 'Tarde'), 
        ('N', 'Noche')
    )
    turno = forms.ChoiceField(choices=TURNOS, label="Turno del Curso")
    fecha_inicio = forms.DateField(input_formats=["%d/%m/%Y"], label="Fecha de Inicio", widget=forms.DateInput(attrs={'type': 'date'}))
    fecha_fin = forms.DateField(input_formats=["%d/%m/%Y"], label="Fecha de Fin", widget=forms.DateInput(attrs={'type': 'date'}))
    email= forms.EmailField(label="Email de Contacto")
"""