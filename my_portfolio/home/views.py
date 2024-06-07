from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import About

def home(request):
    aboutme = About.objects.values().all()
    template = loader.get_template('home.html')
    context = {
        'aboutme' : aboutme
    }
    return HttpResponse(template.render(context, request))

