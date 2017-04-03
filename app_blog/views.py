from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def homepage(request):
    template = loader.get_template('app_blog/home.html')
    context = {
        'title': 'Blogzzz'
    }
    return HttpResponse(template.render(context, request))
