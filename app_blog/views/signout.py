from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views import View
from baseView import BaseView
class SignoutHandler(BaseView):
    def get(self, request):
        return self.write('homepage.html', {'title':'Blogzzz'})
