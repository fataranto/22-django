from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
layaut = """
    <h1>Web con Django</h1>
    <ul>
        <li><a href="/">Inicio</a></li>
        <li><a href="/hola-mundo">Hola Mundo</a></li>
        <li><a href="/pagina">Pagina</a></li>
        <li><a href="/contacto">Contacto/</a></li>
    </ul>
    <hr>
"""


def index(request):
    return render(request, 'index.html')


def hola_mundo(request):
    return render(request, 'hola-mundo.html')

def pagina(request, redirigir=0):
    if redirigir == 1:
        return redirect("contacto", nombre="Neiro")

    html = """ 
        <h1>Pagina de mi web</h1>
        <h2>Desarrollo Web con Django</h2>
    """
    return HttpResponse(layaut + html)

def contacto(request, nombre=""):
    html = "<h2>Contacto</h2>"

    if nombre:
        html += f"<h2>El nombre es: {nombre}</h2>"

    return HttpResponse(layaut + html)