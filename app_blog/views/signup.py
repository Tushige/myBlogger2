from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from baseView import BaseView
from app_blog.forms.signupForm import SignupForm

class SignupHandler(BaseView):
    def get(self, request):
        return self.render_template(request, 'signup.html', {'form':SignupForm()})

    def post(self, request):
        # create a form instance and populate it with data from request
        userForm = SignupForm(request.POST.copy())
        if userForm.is_valid():
            # store user data
            newUser = self.saveUser(userForm)
            return self.redirect('/author/%(username)s'% {'username': newUser.username})
        else:
            return self.render_template(request, 'signup.html', {'form':userForm})

    # saves user to the DB, automatically logs user in
    def saveUser(self, userForm):
        username = userForm.cleaned_data['username']
        password = userForm.cleaned_data['password']
        email = userForm.cleaned_data['email']
        newUser = User.objects.create_user(username, email, password)
        newUser.save()
        return newUser
