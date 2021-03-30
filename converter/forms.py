from django import forms

class ConvertForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Enter your text", "class": "textarea has-fixed-size head",}))
