from django.db import models

# Create your models here.

class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Libros(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    edicion = models.IntegerField()

    def __str__(self):
        return f"{self.titulo} ({self.autor})"

class Prestamo(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.titulo} {self.autor}"