from django import forms

from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = {
            "Nombres",
            "ApellidoPaterno",
            "ApellidoMaterno",
        }
