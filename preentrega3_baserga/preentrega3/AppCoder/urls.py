from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

from .views import (
    inicio,
    exito,
    CursoCreateView,
    CursoDetail,
    CursoDeleteView,
    CursoListView,
    CursoUpdateView
)

urlpatterns = [
    path('inicio/', inicio),
    path('exito/', exito),
    path("curso/list", CursoListView.as_view(), name="curso-list"),
    path("curso/new", CursoCreateView.as_view(), name="curso-create"),
    path("curso/<pk>", CursoDetail.as_view(), name="curso-detail"),
    path("curso/<pk>/update", CursoUpdateView.as_view(), name="curso-update"),
    path("curso/<pk>/delete", CursoDeleteView.as_view(), name="curso-delete"),
]
