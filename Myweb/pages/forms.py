from django import forms
from .models import *
class CoursForm(forms.ModelForm):
    class  Meta:
       model =  Etud_Cours
       fields = '__all__'
       widgets ={ 
            'Dep':forms.TextInput(attrs={'class': 'form-control'}),
            'Modul':forms.TextInput(attrs={'class': 'form-control'}),
            'description':forms.TextInput(attrs={'class': 'form-control'}),
            'title':forms.TextInput(attrs={'class': 'form-control'}),
            
            
            } 