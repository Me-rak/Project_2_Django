from django import forms
from .models import Professeur

class formprof(forms.ModelForm):
    class Meta:
        model= Professeur
        fields = '__all__'
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'example@ept.sn'}),
            'contact_prof': forms.TextInput(attrs={'placeholder': '+221 xx xxx xx xx'}),
            'date_d_adhesion': forms.DateInput(attrs={'placeholder': 'yyyy-mm-dd'}),
        }