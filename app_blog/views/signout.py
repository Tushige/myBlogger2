'''
View Controller class for the sign out page
'''
from django.contrib.auth import logout
from baseView import BaseView

class SignoutHandler(BaseView):
    def get(self, request):
        # deletes session, cookies
        logout(request)
        # redirect to home page
        return self.redirect('/')
