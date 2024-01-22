
from django.http import HttpResponse
from django.template import Template, Context


def saludo(request):
    return HttpResponse("Hola como estas???")


def saludo_personalizado(request, nombre):
    return HttpResponse(f"Hola {nombre}, como estas??")


def saludo3(request, nombre):
    respuesta = f"""
    <html>
    <h1>Bienvenido {nombre}!!!</h1>
    <h2>Todo bien?</h2>
    <h3>Que tengas un buen dia</h3>
    </html>
    """
    return HttpResponse(respuesta)


def bienvenido_template(request):
    mi_html = open("E:/Documentos/Desktop/Curso de PYTHON/Proyecto_1/Proyecto_1/Plantillas/bienvenido.html")
    plantilla = Template(mi_html.read())
    mi_html.close()
    mi_contexto = Context()
    respuesta = plantilla.render(mi_contexto)
    return HttpResponse(respuesta)