from django.shortcuts import render
from .forms import UserForm


def index(request):
    submitbutton= request.POST.get("submit")
    content = ''
    form = UserForm(request.POST or None)

    if form.is_valid():
        content = form.cleaned_data.get("content")

    context= {'form': form, 
            'content': content,
            'submitbutton': submitbutton,}
        
    return render(request, 'index/index.html', context)
