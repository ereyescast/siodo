from django.contrib.auth import views as auth_views, login
from django.shortcuts import redirect
from django.views.generic import FormView, UpdateView, TemplateView

from usuarios.forms import RegistroForm, PerfilForm, CitaForm
from usuarios.models import Perfil, Cita


class LoginView(auth_views.LoginView):
    template_name = 'login.html'


# class LogoutView(auth_views.LogoutView):
#     pass

LogoutView = auth_views.LogoutView


class RegistroView(FormView):
    template_name = 'registro.html'
    form_class = RegistroForm

    def form_valid(self, form):
        usuario = form.save()
        perfil = Perfil()
        perfil.usuario = usuario
        perfil.direccion = form.cleaned_data.get('direccion')
        perfil.documento_identidad = form.cleaned_data.get('documento_identidad')
        perfil.telefono = form.cleaned_data.get('telefono')

        perfil.fecha_nac = form.cleaned_data.get('fecha_nac')
        perfil.save()

        login(self.request, usuario, 'django.contrib.auth.backends.ModelBackend')

        return redirect('home')


class PerfilView(UpdateView):
    template_name = 'perfil.html'
    model = Perfil
    form_class = PerfilForm
    success_url = '/'

    def get_object(self, queryset=None):
        return self.request.user.perfil

class CitaView(TemplateView):
    template_name = 'reserva.html'
    model = Cita
    form_class = CitaForm