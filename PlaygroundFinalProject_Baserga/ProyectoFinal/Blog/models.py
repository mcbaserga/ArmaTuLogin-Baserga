from django.db import models

class Profile(models.Model):
    imagen = models.ImageField(null=True, blank=True, upload_to='media/profile_images/')
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    link = models.URLField()
    email = models.EmailField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.descripcion}"

class Blog(models.Model):
    imagen = models.ImageField(null=True, blank=True, upload_to='media/blog_images/')  
    titulo = models.CharField('Titulo', max_length=24)
    subtitulo = models.CharField(max_length=50)
    cuerpo = models.CharField(max_length=300)
    autor = models.CharField(max_length=50)
    fecha = models.DateField(auto_now_add=True)
