from django.shortcuts import render
from .models import Alumno, Libros, Prestamo


from django.views.generic import ListView,CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy



def inicio(request):
    return render(request, "Final/inicio.html")


def exito(request):
    return render(request, "Final/exito.html")



# ALUMNO

class AlumnoListView(ListView):
    model = Alumno
    context_object_name = "alumnos"
    template_name = "Final/alumno_list.html"


class AlumnoDetail(DetailView):
    model = Alumno
    template_name = "Final/alumno_list.html"


class AlumnoCreateView(CreateView):
    model = Alumno
    template_name = "Final/alumno_create.html"
    success_url = reverse_lazy("alumno-list")
    fields = ["nombre", "apellido", "email"]


class AlumnoUpdateView(UpdateView):
    model = Alumno
    template_name = "Final/alumno_update.html"
    success_url = reverse_lazy("alumno-list")
    fields = ["nombre", "apellido", "email"]


class AlumnoDeleteView(DeleteView):
    model = Alumno
    template_name = "Final/alumno_delete.html"
    success_url = reverse_lazy("alumno-list")


# LIBROS

class LibrosListView(ListView):
    model = Libros
    context_object_name = "libros"
    template_name = "Final/libros_list.html"


class LibrosDetail(DetailView):
    model = Libros
    template_name = "Final/libros_detail.html"


class LibrosCreateView(CreateView):
    model = Libros
    template_name = "Final/libros_create.html"
    success_url = reverse_lazy("libros-list")
    fields = ["titulo", "autor", "edicion"]


class LibrosUpdateView(UpdateView):
    model = Libros
    template_name = "Final/libros_update.html"
    success_url = reverse_lazy("libros-list")
    fields = ["titulo", "autor", "edicion"]


class LibrosDeleteView(DeleteView):
    model = Libros
    template_name = "Final/libros_delete.html"
    success_url = reverse_lazy("libros-list")


# PRESTAMO

class PrestamoListView(ListView):
    model = Prestamo
    context_object_name = "prestamos"
    template_name = "Final/prestamo_list.html"


class PrestamoDetail(DetailView):
    model = Prestamo
    template_name = "Final/prestamo_detail.html"


class PrestamoCreateView(CreateView):
    model = Prestamo
    template_name = "Final/prestamo_create.html"
    success_url = reverse_lazy("prestamo-list")
    fields = ["nombre", "apellido", "titulo", "autor"]


class PrestamoUpdateView(UpdateView):
    model = Prestamo
    template_name = "Final/prestamo_update.html"
    success_url = reverse_lazy("prestamo-list")
    fields = ["nombre", "apellido", "titulo", "autor"]


class PrestamoDeleteView(DeleteView):
    model = Prestamo
    template_name = "Final/prestamo_delete.html"
    success_url = reverse_lazy("prestamo-list")