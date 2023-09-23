from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserCreationFormulario, UserEditionFormulario
from django.contrib.auth.views import PasswordChangeView
from .forms import MyProfileForm
from .models import Profile, Blog
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView

# Create your views here.


def inicio_view(request):
    is_already_logged_in = request.user.is_authenticated
    return render(request, "Blog/inicio.html", {"is_already_logged_in": is_already_logged_in})


# REGISTRO
def registro_view(request):
    if request.method == "GET":
        return render(
            request,
            "Blog/signup.html",
            {"form": UserCreationFormulario()}
        )
    else:
        formulario = UserCreationFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario = informacion["username"]
            formulario.save()

            return render(
                request,
                "Blog/padre.html",
                {"mensaje": f"¡Tu usuario {usuario} fue creado con éxito!"}
            )
        else:
            return render(
                request,
                "Blog/signup.html",
                {"form": formulario}
            )


# EDITAR USUARIO
def editar_usuario_view(request):
    if not request.user.is_authenticated:
        return render(
            request,
            "Blog/login.html",
            {"form": AuthenticationForm()}
        )
    if request.method == "GET":
        return render(
            request,
            "Blog/editar_usuario.html",
            {"form": UserChangeForm()}
        )
    else:
        formulario = UserChangeForm(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            print(informacion)
            user = request.user
            user.email = informacion["email"]
            user.first_name = informacion["first_name"]
            user.last_name = informacion["last_name"]
            user.save()

            return render(
                request,
                "Blog/padre.html",
                {"mensaje": f"Usuario creado"}
            )
        else:
            return render(
                request,
                "Blog/editar-usuario.html",
                {"form": formulario}
            )

class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = "Blog/cambiar_contrasenia.html"
    success_url = reverse_lazy("editar-usuario")


# LOGIN

def login_view(request):
    if request.user.is_authenticated:
        return render(
            request,
            "Blog/login.html",
            {"form": AuthenticationForm(), "is_already_logged_in": True}
        )

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('inicio')
    
    form = AuthenticationForm()
    return render(
        request,
        "Blog/login.html",
        {"form": form, "is_already_logged_in": False}
    )



# LOGOUT
def logout_view(request):
    logout(request)
    return redirect('login')




#PERFIL
class ProfileCreateView(LoginRequiredMixin, CreateView):
    model = Profile
    template_name = "Blog/my_profile_create.html"
    success_url = reverse_lazy("profile-list")
    fields = ["imagen", "nombre", "descripcion", "link", "email"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_already_logged_in"] = self.request.user.is_authenticated
        return context
    
class ProfileListView(LoginRequiredMixin, ListView):
    model = Profile
    context_object_name = "profiles"
    template_name = "Blog/my_profile_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_already_logged_in"] = self.request.user.is_authenticated
        return context

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = "Blog/my_profile_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_already_logged_in"] = self.request.user.is_authenticated
        return context

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = "Blog/my_profile_edit.html"
    success_url = reverse_lazy("profile-list")
    fields = ["imagen", "nombre", "descripcion", "link", "email"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_already_logged_in"] = self.request.user.is_authenticated
        return context

class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = Profile
    template_name = "Blog/my_profile_delete.html"
    success_url = reverse_lazy("profile-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_already_logged_in"] = self.request.user.is_authenticated
        return context

# BLOG
class BlogCreateView(CreateView):
    model = Blog
    template_name = "Blog/blog_create.html"
    success_url = reverse_lazy("blog-list")
    fields = ["imagen", "titulo", "subtitulo", "cuerpo", "autor"]
    
    class Meta:
        model = Blog
        exclude = ['fecha']    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_already_logged_in"] = self.request.user.is_authenticated
        return context
    
class BlogListView(LoginRequiredMixin, ListView):
    model = Blog
    context_object_name = "blogs"
    template_name = "Blog/blog_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_already_logged_in"] = self.request.user.is_authenticated
        return context

class BlogDetailView(DetailView):
    model = Blog
    context_object_name = "blog"
    template_name = "Blog/blog_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_already_logged_in"] = self.request.user.is_authenticated
        return context