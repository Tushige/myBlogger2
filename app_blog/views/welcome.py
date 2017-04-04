from baseView import BaseView
from django.contrib.auth.models import User
from app_blog.utility import user_utility

class WelcomeHandler(BaseView):
    def get(self, request, username):
        if not self.request.user.is_authenticated():
            print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
            print 'NOT authenticated'
            print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
        if self.request.user.is_authenticated() and \
            username == self.request.user.get_username():
                return self.render_template(request, 'welcome.html', {'user': self.request.user.is_authenticated()})
        # user visiting another user's profile
        elif user_utility.userExists(username):
            # get username's blogs
            # get the user
            user = user_utility.getUserByUsername(username)
            print '*********************'
            print user.profile.profile_name
            print '*********************'
            if user:
                return self.render_template(request, 'author.html',
                                                {'author':user,
                                                 'blogs': None
                                                })
        # invalid request
        else:
            self.render_404("The page you're looking for doesn't exist!")
