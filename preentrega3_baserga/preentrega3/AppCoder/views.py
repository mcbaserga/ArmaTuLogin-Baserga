from django.shortcuts import render
from .models import Alumno, Libros, Prestamo


from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy



def inicio(request):
    return render(request, "AppCoder/inicio.html")


def exito(request):
    return render(request, "AppCoder/exito.html")



# ALUMNO

class AlumnoListView(ListView):
    model = Alumno
    context_object_name = "alumnos"
    template_name = "AppCoder/cbv_alumno_list.html"


class AlumnoDetail(DetailView):
    model = Alumno
    template_name = "AppCoder/cbv_alumno_list.html"


class AlumnoreateView(CreateView):
    model = Alumno
    template_name = "AppCoder/cbv_alumno_create.html"
    success_url = reverse_lazy("alumno-list")
    fields = ["nombre", "apellido"]


class AlumnoUpdateView(UpdateView):
    model = Alumno
    template_name = "AppCoder/cbv_alumno_update.html"
    success_url = reverse_lazy("curso-list")
    fields = ["nombre", "apellido", "email"]


class AlumnoDeleteView(DeleteView):
    model = Alumno
    template_name = "AppCoder/cbv_alumno_delete.html"
    success_url = reverse_lazy("alumno-list")


# LIBROS

class LibrosListView(ListView):
    model = Libros
    context_object_name = "libros"
    template_name = "AppCoder/cbv_libros_list.html"


class LibrosDetail(DetailView):
    model = Libros
    template_name = "AppCoder/cbv_libros_detail.html"


class LibrosCreateView(CreateView):
    model = Libros
    template_name = "AppCoder/cbv_libros_create.html"
    success_url = reverse_lazy("libros-list")
    fields = ["titulo", "edicion"]


class LibrosUpdateView(UpdateView):
    model = Libros
    template_name = "AppCoder/cbv_libros_update.html"
    success_url = reverse_lazy("libros-list")
    fields = ["edicion"]


class LibrosDeleteView(DeleteView):
    model = Libros
    template_name = "AppCoder/cbv_libros_delete.html"
    success_url = reverse_lazy("libros-list")


# PRESTAMO

class PrestamoListView(ListView):
    model = Prestamo
    context_object_name = "prestamos"
    template_name = "AppCoder/cbv_prestamo_list.html"


class PrestamoDetail(DetailView):
    model = Prestamo
    template_name = "AppCoder/cbv_prestamo_detail.html"


class PrestamoCreateView(CreateView):
    model = Prestamo
    template_name = "AppCoder/cbv_prestamo_create.html"
    success_url = reverse_lazy("prestamo-list")
    fields = ["nombre", "apellido", "titulo", "autor"]


class PrestamoUpdateView(UpdateView):
    model = Prestamo
    template_name = "AppCoder/cbv_prestamo_update.html"
    success_url = reverse_lazy("prestamo-list")
    fields = ["nombre", "apellido", "titulo", "autor"]


class PrestamoDeleteView(DeleteView):
    model = Prestamo
    template_name = "AppCoder/cbv_prestamo_delete.html"
    success_url = reverse_lazy("prestamo-list")