from django.contrib.auth import authenticate, login
from app_blog.forms.signinForm import SigninForm
from baseView import BaseView

class SigninHandler(BaseView):
    def get(self, request):
        return self.render_template(request, 'signin.html', {'form': SigninForm()})

    def post(self, request):
        userForm = SigninForm(request.POST.copy())
        # make sure fields are filled in
        if userForm.is_valid():
            # authenticate
            username = userForm.cleaned_data['username']
            password = userForm.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return self.redirect('/author/%(username)s' % {'username': user.username})
            else:
                return self.render_template(request, 'signin.html',
                                            {'form':userForm,
                                            'signin_error':'username or password wrong'
                                            })
        return self.write('no good')
