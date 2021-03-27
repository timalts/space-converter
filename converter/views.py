from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    var = "a"
    template = loader.get_template('index/index.html')
    context = {
        'var': var,
    }
    return HttpResponse(template.render(context, request))