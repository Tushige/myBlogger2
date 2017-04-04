from baseView import BaseView
from app_blog.models import Blog

class BlogEntryHandler(BaseView):
    def get(self, request, blog_id):
        # retrieve blog and show if exists
        try:
            blog = Blog.objects.get(id=blog_id)
        except DoesNotExist:
            return self.render_404("Nothing here")
        # blog exists => show it
        return self.render_template(request, 'blogEntry.html', {'blog':blog})
