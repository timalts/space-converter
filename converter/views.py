from django.shortcuts import render
from .forms import ConvertForm


def index(request):
    submitbutton= request.POST.get("submit")
    content = ''
    form = ConvertForm(request.POST or None)
    result = ''
    if form.is_valid():
        content = form.cleaned_data.get("content")
        result = content.split(" ")
    context= {'form': form, 
            'content': content,
            'submitbutton': submitbutton,
            'result': result}
        
    return render(request, 'index/index.html', context)
