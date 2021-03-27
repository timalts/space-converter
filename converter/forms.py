from django import forms

class ConvertForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20})
