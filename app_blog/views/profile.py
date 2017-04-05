from baseView import BaseView
from django.contrib.auth.models import User
from app_blog.models import Blog
from app_blog.utility import user_utility

class ProfileHandler(BaseView):
    def get(self, request, username):
        if self.request.user.is_authenticated() and username == self.request.user.get_username():
            #try:
            blogs = request.user.profile.blog_set.all()[:10]
            return self.render_template(request, 'profile.html', {
                                        'user': request.user,
                                        'blogs': blogs
                                        })
        # user visiting another user's profile
        elif user_utility.userExists(username):
            # get the user
            user = user_utility.getUserByUsername(username)
            # get username's blogs
            blogs = user.profile.blog_set.all()[:10]
            if user:
                return self.render_template(request, 'author.html',
                                                {'author':user,
                                                 'blogs': blogs
                                                })
        # invalid request
        else:
            print '1111111111111111111'
            print '1111111111111111111'
            self.render_404(request)
