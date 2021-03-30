from django.shortcuts import render
from .forms import ConvertForm


def index(request):
    submitbutton= request.POST.get("submit")
    content = ''
    form = ConvertForm(request.POST or None)
    result = ''
    if form.is_valid():
        content = form.cleaned_data.get("content")
        result = content.split("\r")
        final_result = ''
        for line in result:
            final_result += f"{line.strip()}\n"
        result = repr(final_result)

    context= {'form': form, 
            'content': content,
            'submitbutton': submitbutton,
            'result': result}
        
    return render(request, 'index/index.html', context)
