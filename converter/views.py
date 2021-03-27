from django.shortcuts import render
from .forms import ConvertForm


def index(request):
    submitbutton= request.POST.get("submit")
    content = ''
    form = ConvertForm(request.POST or None)

    if form.is_valid():
        content = form.cleaned_data.get("content")

    context= {'form': form, 
            'content': content,
            'submitbutton': submitbutton,}
        
    return render(request, 'index/index.html', context)
