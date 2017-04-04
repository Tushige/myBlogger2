from baseView import BaseView

class WelcomeHandler(BaseView):
    def get(self, request, username):
        return self.render_template(request, 'welcome.html', {'user': self.request.user.is_authenticated()})
