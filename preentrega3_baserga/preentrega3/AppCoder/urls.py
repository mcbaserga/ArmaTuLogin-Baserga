from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

from .views import (
    inicio,
    exito,
    AlumnoCreateView,
    AlumnoDetail,
    AlumnoDeleteView,
    AlumnoListView,
    AlumnoUpdateView,

    LibrosCreateView,
    LibrosDetail,
    LibrosDeleteView,
    LibrosListView,
    LibrosUpdateView,

    PrestamoCreateView,
    PrestamoDetail,
    PrestamoDeleteView,
    PrestamoListView,
    PrestamoUpdateView
)

urlpatterns = [
    path('inicio/', inicio),
    path('exito/', exito),

    # ALUMNOS
    path("alumno/list", AlumnoListView.as_view(), name="alumno-list"),
    path("alumno/new", AlumnoCreateView.as_view(), name="alumno-create"),
    path("alumno/<pk>", AlumnoDetail.as_view(), name="alumno-detail"),
    path("alumno/<pk>/update", AlumnoUpdateView.as_view(), name="alumno-update"),
    path("alumno/<pk>/delete", AlumnoDeleteView.as_view(), name="alumno-delete"),

    # LIBROS
    path("libros/list", LibrosListView.as_view(), name="libros-list"),
    path("libros/new", LibrosCreateView.as_view(), name="libros-create"),
    path("libros/<pk>", LibrosDetail.as_view(), name="libros-detail"),
    path("libros/<pk>/update", LibrosUpdateView.as_view(), name="libros-update"),
    path("libros/<pk>/delete", LibrosDeleteView.as_view(), name="libros-delete"),

    # PRESTAMO
    path("prestamo/list", PrestamoListView.as_view(), name="prestamo-list"),
    path("prestamo/new", PrestamoCreateView.as_view(), name="prestamo-create"),
    path("prestamo/<pk>", PrestamoDetail.as_view(), name="prestamo-detail"),
    path("prestamo/<pk>/update", PrestamoUpdateView.as_view(), name="prestamo-update"),
    path("prestamo/<pk>/delete", PrestamoDeleteView.as_view(), name="prestamo-delete"),
]
