'''
view handler for the home page
'''
from baseView import BaseView
from app_blog.models import Blog

class HomepageHandler(BaseView):
    def get(self, request):
        try:
            blogs = Blog.objects.all()[:10]
        except Blog.DoesNotExist:
            blogs = None
        return self.render_template(request, 'homepage.html', {
                                    'user': request.user,
                                    'blogs':blogs
                                    })
