from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

from .views import inicio, welcome, cursos_view

urlpatterns = [
    path('inicio/', inicio),
    path('welcome/', welcome),
    path('cursos/', cursos_view)
    # path('user_form/', create_user)
]