from django.shortcuts import render


def inicio_view(request):
    return render(request, "AppCoder/inicio.html")

def cursos_view(request):
    return render(request, "AppCoder/cursos.html")