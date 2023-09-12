from django.contrib import admin
from .models import Alumno, Libros, Prestamo


# Register your models here.



@admin.register(Alumno, Libros, Prestamo)
class Admin(admin.ModelAdmin):
    pass