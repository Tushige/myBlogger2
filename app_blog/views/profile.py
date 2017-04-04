from baseView import BaseView
from django.contrib.auth.models import User
from app_blog.utility import user_utility

class ProfileHandler(BaseView):
    def get(self, request, username):
        if self.request.user.is_authenticated() and username == self.request.user.get_username():
            return self.render_template(request, 'profile.html', {'user': request.user})
        # user visiting another user's profile
        elif user_utility.userExists(username):
            # get username's blogs
            # get the user
            user = user_utility.getUserByUsername(username)
            if user:
                return self.render_template(request, 'author.html',
                                                {'author':user,
                                                 'blogs': None
                                                })
        # invalid request
        else:
            self.render_404("The page you're looking for doesn't exist!")
