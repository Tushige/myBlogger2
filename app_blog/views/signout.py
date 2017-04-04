from django.contrib.auth import logout
from baseView import BaseView

class SignoutHandler(BaseView):
    def get(self, request):
        logout(request)
        return self.redirect('/')
