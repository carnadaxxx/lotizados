from django import forms

from .models import Lote, Manzana

class LoteForm(forms.ModelForm):
    class Meta:
        model = Lote
        fields = {
            "Manzana",
            "Numero",
            "Area",
            "Costo",
        }
