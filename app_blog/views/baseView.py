'''
BaseView is the base view handler: all view classes subclass this
'''
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.views import View

class BaseView(View):
    # writes plain text to page
    # @content: plain text to write to page
    def write(self, content):
        return HttpResponse(content)

    # renders a template to page
    # @template_name: name of the template file
    # @temp_context: template variable-value mapping
    def render_template(self, request, template_name, temp_context):
        template = loader.get_template('app_blog/%(template_name)s'%{'template_name':template_name})
        return HttpResponse(template.render(temp_context, request))

    # redirect to the specified url
    # @rurl: the url to redirect
    def redirect(self, rurl):
        return HttpResponseRedirect(rurl)

    # renders a 404 error page
    def render_404(self, request, error_msg="The page you're looking for doesn't exist!"):
        return self.render_template(request, 'error404.html', {'error_msg':error_msg})
