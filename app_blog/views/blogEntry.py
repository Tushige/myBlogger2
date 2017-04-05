'''
View Controller class for the blog permalink page
'''
from baseView import BaseView
from app_blog.models import Blog

class BlogEntryHandler(BaseView):
    def get(self, request, blog_id):
        # retrieve blog and show if exists
        try:
            blog = Blog.objects.get(id=blog_id)
        except Blog.DoesNotExist:
            return self.render_404(request)
        # blog exists => show it
        return self.render_template(request, 'blogEntry.html', {'blog':blog})
