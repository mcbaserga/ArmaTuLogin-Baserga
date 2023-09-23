from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

from .views import (
    inicio_view,
    about,
    
    # Perfil
    ProfileCreateView,
    ProfileListView,
    ProfileDetailView,
    ProfileUpdateView,
    ProfileDeleteView,
    
    # Blog 
    BlogCreateView,
    BlogDetailView,
    BlogListView,

    
    # Login
    login_view,
    editar_usuario_view,
    registro_view,
    CambiarContrasenia,
)


urlpatterns = [
    path('inicio/', views.inicio_view, name='inicio'),
    path('about/', views.about, name='about'),
    
    # Perfil
    path("my_profile/new", ProfileCreateView.as_view(), name="profile-create"),
    path("my_profile/<int:pk>", ProfileDetailView.as_view(), name= "profile-detail"),
    path("my_profile/list", ProfileListView.as_view(), name= "profile-list"),
    path("my_profile/<pk>/update", ProfileUpdateView.as_view(), name="profile-update"),
    path("my_profile/<pk>/delete", ProfileDeleteView.as_view(), name="profile-delete"),


    # Blog
    path("blog/", BlogCreateView.as_view(), name="blog-create"),
    path("blog/<int:pk>", BlogDetailView.as_view(), name= "blog-detail"),
    path("blog/list", BlogListView.as_view(), name= "blog-list"),


    # Login / Logout
    path("signup/", registro_view, name="signup"),
    path("login/", login_view, name="login"),
    path("logout/", LogoutView.as_view(template_name="Blog/logout.html"), name="logout"),


    # Edicion de usuario
    path("editar-usuario/", editar_usuario_view, name="editar-usuario"),
    path("cambiar-contrasenia/", CambiarContrasenia.as_view(), name="cambiar-contrasenia")

]