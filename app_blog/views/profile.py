'''
View Controller class for user profile page
handles views for:
    1. logged in user's profile
    2. other users' profile
'''

from baseView import BaseView
from django.contrib.auth.models import User
from app_blog.utility import utils

class ProfileHandler(BaseView):
    def get(self, request, username):
        # user visiting own profile
        if self.request.user.is_authenticated() and username == self.request.user.get_username():
            # get logged in user's last 10 blog submissions
            blogs = utils.getBlogsForUser(request.user, 10)
            return self.render_template(request, 'profile.html', {
                                        'user': request.user,
                                        'blogs': blogs
                                        })
        # user visiting another user's profile
        elif utils.userExists(username):
            # get the user
            user = utils.getUserByUsername(username)
            # get username's last blogs
            blogs = utils.getBlogsForUser(user, 10)
            if user:
                return self.render_template(request, 'author.html',
                                                {'author':user,
                                                 'blogs': blogs
                                                })
        # invalid request
        # can get here if requested 'username' is invalid
        else:
            return self.render_404(request)
