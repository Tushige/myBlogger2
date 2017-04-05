'''
Controller for the signin page
'''
from django.contrib.auth import authenticate, login
from app_blog.forms.signinForm import SigninForm
from baseView import BaseView

class SigninHandler(BaseView):
    def get(self, request):
        # redirect to homepage if user already logged in
        if request.user.is_authenticated():
            return self.redirect('/')
        # show signin page if no logged in user
        return self.render_template(request, 'signin.html', {'form': SigninForm()})

    def post(self, request):
        # retrieve user input
        userForm = SigninForm(request.POST.copy())

        # make sure fields are filled in
        if userForm.is_valid():
            username = userForm.cleaned_data['username']
            password = userForm.cleaned_data['password']
            # authenticate user credentials
            user = authenticate(username=username, password=password)
            # login user if authentication is successful
            if user:
                login(request, user)
                return self.redirect('/author/%(username)s' % {'username': user.username})
            # show error message
            else:
                return self.render_template(request, 'signin.html',
                                            {'form':userForm,
                                            'signin_error':'username or password wrong'
                                            })
        # shouldn't get here since submission is not allowed if fields are empty
        else:
            return self.render_template(request, 'signin.html',
                                        {'form':userForm,
                                        'signin_error':'username or password wrong'
                                        })
