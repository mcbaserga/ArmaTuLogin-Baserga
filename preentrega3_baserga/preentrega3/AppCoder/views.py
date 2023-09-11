from django.shortcuts import render
# from .models import PersonalInfo, Course, ContactInfo
from .models import Curso
from .forms import CursoFormulario

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def welcome(request):
    return render(request, "AppCoder/welcome.html")

# def create_user(request):
#     if request.method == "GET":
#         print("+" * 90) #  Imprimimos esto para ver por consola
#         print("+" * 90) #  Imprimimos esto para ver por consola
#         return render(
#             request,
#             "AppCoder/curso_formulario_basico.html",
#         )
#     else:
#         print("*" * 90)     #  Imprimimos esto para ver por consola
#         print(request.POST) #  Imprimimos esto para ver por consola
#         print("*" * 90)     #  Imprimimos esto para ver por consola
#         return render(
#             request,
#             "AppCoder/curso_formulario_basico.html",
#         )

def cursos_view(request):
    if request.method == "GET":
        print("+" * 90) 
        print("+" * 90) 
        return render(
            request,
            "AppCoder/curso_formulario.html",
            {"form": CursoFormulario()}
        )
    else:
        print("*" * 90)     
        print(request.POST) 
        print("*" * 90)     
        
        modelo = Curso(curso=request.POST["curso"], camada=request.POST["camada"])
        modelo.save()

        return render(
            request,
            "AppCoder/curso_formulario.html",
            {"form": CursoFormulario()}
        )