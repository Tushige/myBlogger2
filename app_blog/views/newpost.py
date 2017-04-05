'''
View Controller class for the new blog submission page
'''
from baseView import BaseView
from app_blog.forms.newpostForm import NewpostForm
from django.utils import timezone

class NewpostHandler(BaseView):
    def get(self, request):
        # 'post submission' only allowed for logged in user
        if request.user.is_authenticated():
            userForm = NewpostForm()
            return self.render_template(request, 'newpost.html', {'form':userForm})
        # if not logged in, redirect to homepage
        else:
            return self.redirect('/')

    def post(self, request):
        # retrieve user submission
        userForm = NewpostForm(request.POST.copy())
        # save form if valid
        if userForm.is_valid():
            blog_entry = self.saveForm(userForm)
            # redirect to blog permalink page
            return self.redirect('/blog_entry/%(blog_id)s'%{'blog_id': str(blog_entry.id)})
        # else user will be shown errors
        else:
            return self.render_template(request, 'newpost.html', {'form':userForm})

    # creates a blog entry for the user and returns the new 'blog' model object
    def saveForm(self, userForm):
        # retrieve submission data
        title = userForm.cleaned_data['blog_title']
        abstract = userForm.cleaned_data['blog_abstract']
        content = userForm.cleaned_data['blog_content']
        # create a 'blog entry' for the logged in user
        blog_entry = self.request.user.profile.blog_set.create(blog_title=title,
                                     blog_abstract=abstract,
                                     blog_content=content,
                                     pub_date=timezone.now())
        return blog_entry
