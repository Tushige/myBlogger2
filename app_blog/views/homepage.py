'''
view handler for the home page
'''
from baseView import BaseView

class HomepageHandler(BaseView):
    def get(self, request):
        return self.render_template(request, 'homepage.html', {'user': request.user})
