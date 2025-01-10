from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article
from django.db.models import Q #esto es para hacer consultas con or
from miapp.forms import FormArticle
from django.contrib import messages

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
    return render(request, 'index.html', {
        'titulo': 'Inicio desde la vista',
        'nombre': 'Neiro'
    })


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

def crear_articulo(request, title="título", content="contenido", public=True):
    articulo = Article(
        title = title,
        content = content,
        public = public
    )

    articulo.save()


    return HttpResponse(f"Articulo: {articulo.title} {articulo.content}")

def save_article(request):

    if request.method == 'POST':

        title = request.POST['title']
        content = request.POST['content']
        public = request.POST['public']

        articulo = Article(
            title = title,
            content = content,
            public = public
        )

        articulo.save()

        return HttpResponse(f"Articulo: {articulo.title} {articulo.content}")
    
    else:
        return HttpResponse(f"<h2>No se ha podido crear el artículo</h2>")


def create_article(request):
    return render(request, 'create_article.html')

def create_full_article(request):
    if request.method == 'POST':
        formulario = FormArticle(request.POST)

        if formulario.is_valid():
            data_form = formulario.cleaned_data

            title = data_form.get('title')
            content = data_form['content']
            public = data_form['public']

            articulo = Article(
                title = title,
                content = content,
                public = public
            )

            articulo.save()

            messages.success(request, f'Has creado correctamente el artículo {articulo.id} "{articulo.title}"')

            return redirect('articulos')
            #return HttpResponse(articulo.title + ' ' + articulo.content + ' ' + str(articulo.public) )

    else:

        formulario = FormArticle()

    return render(request, 'create_full_article.html', {
        'form': formulario
    })


def articulo(request):

    articulo = Article.objects.get(id=1)

    return HttpResponse(f"Articulo: ")

def editar_articulo(request, id):
    articulo = Article.objects.get(pk=id)

    articulo.title = "Batman"
    articulo.content = "Pelicula del 2022"
    articulo.public = True

    articulo.save()

    return HttpResponse(f"Articulo: {articulo.title} {articulo.content}")

def articulos(request):
    #articulos = Article.objects.all()
    articulos = Article.objects.filter(public=True).order_by('title')

    return render(request, 'articulos.html', {
        'articulos': articulos
    })

def borrar_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.delete()

    return redirect('articulos')