'''
BaseView is the base view handler: all view classes subclass this
'''
from django.http import HttpResponse
from django.template import loader
from django.views import View

class BaseView(View):
    def write(self, content):
        return HttpResponse(content)

    def render_template(self, request, template_name, temp_context):
        template = loader.get_template('app_blog/%s'%template_name)
        return HttpResponse(template.render(temp_context, request))
