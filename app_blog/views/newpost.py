from baseView import BaseView
from app_blog.forms.newpostForm import NewpostForm
from django.utils import timezone

class NewpostHandler(BaseView):
    def get(self, request):
        userForm = NewpostForm()
        return self.render_template(request, 'newpost.html', {'form':userForm})

    def post(self, request):
        userForm = NewpostForm(request.POST.copy())
        if userForm.is_valid():
            blog_entry = self.saveForm(userForm)
            # redirect to blog permalink page
            return self.redirect('/blog_entry/%(blog_id)s'%{'blog_id': str(blog_entry.id)})
        else:
            return self.render_template(request, 'newpost.html', {'form':userForm})

    def saveForm(self, userForm):
        title = userForm.cleaned_data['blog_title']
        abstract = userForm.cleaned_data['blog_abstract']
        content = userForm.cleaned_data['blog_content']
        blog_entry = self.request.user.profile.blog_set.create(blog_title=title,
                                     blog_abstract=abstract,
                                     blog_content=content,
                                     pub_date=timezone.now())
        return blog_entry
        # do I need to save user?
