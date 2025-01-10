from django import template

register = template.Library()

@register.filter(name='saludo')
def saludo(value):
    largo = ''
    if len(value) > 5:
        largo = '<p>El nombre es muy largo</p>'                
    
    return f"<h1 style='background:green;color:white;'>Hola, {value}</h1>"+largo
