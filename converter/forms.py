from django import forms

class ConvertForm(forms.Form):
    content = forms.CharField(max_length=1000000)
