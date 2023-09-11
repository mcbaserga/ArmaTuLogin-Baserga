from django.shortcuts import render
from .models import Curso


from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy

# from AppCoder.models import *

def inicio(request):
    return render(request, "AppCoder/inicio.html")


def exito(request):
    return render(request, "AppCoder/exito.html")


class CursoListView(ListView):
    model = Curso
    context_object_name = "cursos"
    template_name = "AppCoder/cbv_curso_list.html"


class CursoDetail(DetailView):
    model = Curso
    template_name = "AppCoder/cbv_curso_detail.html"


class CursoCreateView(CreateView):
    model = Curso
    template_name = "AppCoder/cbv_curso_create.html"
    success_url = reverse_lazy("curso-list")
    fields = ["curso", "camada"]


class CursoUpdateView(UpdateView):
    model = Curso
    template_name = "AppCoder/cbv_curso_update.html"
    success_url = reverse_lazy("curso-list")
    fields = ["curso"]


class CursoDeleteView(DeleteView):
    model = Curso
    template_name = "AppCoder/cbv_curso_delete.html"
    success_url = reverse_lazy("curso-list")