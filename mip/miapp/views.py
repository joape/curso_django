from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import sqlite3

# Create your views here.
def index(request):
    return HttpResponse("Hola, bienvenidos al curso de Django")

def acerca(request):
    return HttpResponse(
        """
        <html>
            <h1>Acerca de nosotros</h1>
            <h2>Profesor Norman Beltran</h2>
            <h3>ACurso de Desarrollo Web con Python & Django</h3>
        </html>
        """)

def contacto(request):   
    html = """
          <html>
            <h1>Contactos </h1>
            <h2>Telefono / Celular</h2>
            <h3>Whatsapp</h3>
          </html>
           """
    return HttpResponse(html)

def cursos(request):
    conn = sqlite3.connect('curso.db')
    cursor = conn.cursor()
    html =   """
        <html>
        <title>Lista de Cursos</title>
        <table style='border:1px solid'>
        <thead>
            <tr>
                <th>Id</th>
                <th>Nombre</th>
                <th>Inscriptos</th>
            </tr>
        </thead>
        """
    # Leer los registros de la BD
    cursor.execute("SELECT id, nombre, inscriptos FROM cursos;")
    for (id, nombre, inscriptos) in cursor.fetchall():
        html += "<tr>"
        html += "<td>" + str(id) + "</td>"
        html += "<td>" + nombre + "</td>"
        html += "<td>" + str(inscriptos) + "</td>"
        html += "</tr>"

    html += """
        </table>
        </html>
    """
    conn.close()
    return HttpResponse(html)

def aero(request):
   
    html =   """
        <html>
        <title>Lista de Aeropuertos</title>
        <table style='border:1px solid'>
        <thead>
            <tr>
                <th>Aeropuerto</th>
                <th>Ciudad</th>
                <th>Pais</th>
                <th>Codigo</th>
            </tr>
        </thead>
        """
    # Leer los registros del csv
    with open("aeropuertos.csv", "r", encoding="utf8") as file:
        for linea in file:
            datos = linea.split(",")
            html += "<tr>"           
            html += "<td>" + datos[1].replace('"', '') + "</td>"
            html += "<td>" + datos[2].replace('"', '') + "</td>"
            html += "<td>" + datos[3].replace('"', '') + "</td>"
            html += "<td>" + datos[4].replace('"', '') + "</td>"
            html += "</tr>"

    html += """
        </table>
        </html>
    """ 
    return HttpResponse(html)

def aero_api(request):
    aeropuertos = []
    # Leer los registros del csv
    with open("aeropuertos.csv", "r", encoding="utf8") as file:
        for linea in file:
            datos = linea.split(",")
    
            nombre = datos[1].replace('"', '') 
            ciudad = datos[2].replace('"', '') 
            pais = datos[3].replace('"', '') 
            codigo = datos[4].replace('"', '') 
            aeropuerto = {
                "nombre": nombre,
                "ciudad": ciudad,
                "pais": pais,
                "codigo": codigo,
            }
            aeropuertos.append(aeropuerto)
    return JsonResponse(aeropuertos, safe=False)