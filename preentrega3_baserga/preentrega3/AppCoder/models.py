from django.db import models

# Create your models here.
# class PersonalInfo(models.Model):
#     usuario = models.CharField(max_length=100, default='SOME STRING')
#     nombre = models.CharField(max_length=100)
#     apellido = models.CharField(max_length=100)

# class Course(models.Model):
#     curso = models.CharField(max_length=100)
#     camada = models.IntegerField()

# class ContactInfo(models.Model):
#     telefono = models.IntegerField()
#     email = models.EmailField()

class Curso(models.Model):
    curso = models.CharField(max_length=100)
    camada = models.IntegerField()