from baseView import BaseView

class NewpostHandler(BaseView):
    def get(self, request):
        return self.render_template(request, 'newpost.html', {})
