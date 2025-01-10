from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name = "Título")
    content = models.TextField(verbose_name = "Detalle")
    image = models.ImageField(default='null', verbose_name = "Imagen", upload_to="articlles")
    public = models.BooleanField(verbose_name = "Publicado")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = "Creado")
    updated_at = models.DateTimeField(auto_now=True, verbose_name = "Modificado")

    class Meta:
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"
        ordering = [ '-created_at' ]

    def __str__(self):
        if self.public:
            publicado = "(Publicado)"
        else:
            publicado = "(Privado)"
        return f"{self.title} {publicado}"
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return f"{self.name}"