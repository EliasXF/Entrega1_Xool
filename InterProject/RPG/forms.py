from django import forms

class formulario_character(forms.Form):
    name = forms.CharField(max_length=20)
    level = forms.IntegerField()
    race = forms.CharField(max_length=30)
    attackPower = forms.IntegerField()
    defense = forms.IntegerField()
    magic = forms.IntegerField()