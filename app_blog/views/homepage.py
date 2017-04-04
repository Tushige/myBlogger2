'''
view handler for the home page
'''
from baseView import BaseView

class HomepageHandler(BaseView):
    def get(self, request):
        print '***************'
        print self.request.user.username
        print '***************'
        return self.render_template(request, 'homepage.html', {'user': self.request.user})
