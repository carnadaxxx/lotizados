from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import Contrato

class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = {
            "lote",
            "titular",
            "cuotas",
        }

    def clean(self):
        cleaned_data = super(ContratoForm, self).clean()
        loteObj = cleaned_data['lote']
        q1 = Contrato.objects.filter(lote__id=loteObj.id).count()
        if q1 > 0:
            raise ValidationError(
            _('El lote ya esta vendido')
        )
        print(q1)
