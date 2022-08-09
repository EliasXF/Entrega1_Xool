from django import forms

class formulario_pet(forms.Form):
    name = forms.CharField(max_length=20)
    type = forms.CharField(max_length=30)
    age = forms.IntegerField()
    powertype = forms.CharField(max_length=20) 
    wings = forms.CharField(max_length=3)
    description = forms.CharField(max_length=100)