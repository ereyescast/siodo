from django.conf.urls import url
from django.contrib import admin

from website.views import HomeView
from usuarios.views import LoginView, LogoutView, RegistroView, PerfilView, ReservaView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^login$', LoginView.as_view(), name='login'),
    url(r'^logout', LogoutView.as_view(), name='logout'),
    url(r'^registro', RegistroView.as_view(), name='registro'),
    url(r'^perfil', PerfilView.as_view(), name='perfil'),

    url(r'^reserva', ReservaView.as_view(), name='reserva'),
    url(r'^admin/', admin.site.urls),

]
