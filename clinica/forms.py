from django import forms
from .models import Consulta

class ConsultaForms(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'