from django import forms
from products.models import Contactos


class ContactosForm(forms.ModelForm):
    class Meta:
        model = Contactos
        fields = [
            'Nombre',
            'Apellido',
            'Empresa',
            'Correo',
            'Mensaje'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'empresa': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'subject': forms.TextInput(attrs={'class':'form-control'}),
            'message ': forms.Textarea(attrs={'class':'form-control'}),
        }

