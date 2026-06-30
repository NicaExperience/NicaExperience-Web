from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = [
            'nombre',
            'correo',
            'fecha',
            'personas',
            'mensaje'
        ]
        widgets = {
         'fecha': 
   forms.DateInput(attrs={'type': 'date'}),
         }