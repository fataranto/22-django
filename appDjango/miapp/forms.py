from django import forms
from django.core import validators

class FormArticle(forms.Form):

    title = forms.CharField(
        label = "Título",
        max_length=40,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Inserte el título',
                'class': 'title_form_arrticle'
            }
        ),
        validators=[
            validators.MinLengthValidator(4, "El título es demasiado corto"),
            validators.RegexValidator('^[\w\sáéíóúÁÉÍÓÚüÜñÑ]*$', 'El texto es incorrecto', 'invalid_title')
        ]
    )

    content = forms.CharField(
        label = "Contenido",
        widget= forms.Textarea(
            attrs={
                'placeholder': 'Inserte el contenido',
                'class': 'desc_form_arrticle'
            }
        ),
        validators=[
            validators.MaxLengthValidator(50, "El texto es demasiado largo"),
            validators.RegexValidator('^[\w\sáéíóúÁÉÍÓÚüÜñÑ]*$', 'El texto es incorrecto', 'invalid_title')
        ]
    )

    public_options = [
        (1, 'Si'),
        (0, 'No')
    ]

    public = forms.TypedChoiceField(
        label = "Publicar",
        choices = public_options
    )