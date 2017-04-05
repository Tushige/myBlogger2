'''
View Controller class for the home page
'''
from baseView import BaseView
from app_blog.utility import utils

class HomepageHandler(BaseView):
    def get(self, request):
        # get the last 10 blogs
        blogs = utils.getBlogs(10)
        return self.render_template(request, 'homepage.html', {
                                    'user': request.user,
                                    'blogs':blogs
                                    })
