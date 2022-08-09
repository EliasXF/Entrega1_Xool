from django import forms

class formulario_vehicle(forms.Form):
    type = forms.CharField(max_length=20)
    brand = forms.CharField(max_length=20)
    model = forms.CharField(max_length=20)
    doors = forms.IntegerField()
    transmission = forms.CharField(max_length=12)