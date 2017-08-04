from django.conf.urls import url
from django.contrib import admin

from website.views import HomeView
from usuarios.views import LoginView, LogoutView, RegistroView, CitaView, PerfilView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^login$', LoginView.as_view(), name='login'),
    url(r'^logout', LogoutView.as_view(), name='logout'),
    url(r'^registro', RegistroView.as_view(), name='registro'),
    url(r'^cita', CitaView.as_view(), name='cita'),
    url(r'^perfil', PerfilView.as_view(), name='perfil'),
    url(r'^admin/', admin.site.urls),

]
