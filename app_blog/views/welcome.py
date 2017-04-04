from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views import View
from baseView import BaseView

class WelcomeHandler(BaseView):
    def get(self, request, username):
        return self.render_template(request, 'homepage.html', {})
