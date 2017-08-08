from django import forms
from django.contrib.auth.forms import UserCreationForm

from usuarios.models import Perfil
from datetime import datetime

class RegistroForm(UserCreationForm):

    direccion = forms.CharField(
        required=True
    )

    documento_identidad = forms.CharField(
        max_length=10,
        required=True
       )

    telefono = forms.CharField(
        max_length=9,
        required=True
    )

    fecha_nac = forms.DateField(widget=forms.SelectDateWidget(
        years=range(1980, datetime.now().year + 1)
    ))

    class Meta(UserCreationForm.Meta):
        fields = ('username', 'first_name', 'last_name',)


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ('direccion', 'telefono', 'fecha_nac', 'avatar','documento_identidad',)

