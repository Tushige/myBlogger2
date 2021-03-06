'''
View Controller class for the sign up page
'''
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from baseView import BaseView
from app_blog.forms.signupForm import SignupForm

class SignupHandler(BaseView):
    def get(self, request):
        # redirect to homepage if user already logged in
        if request.user.is_authenticated():
            return self.redirect('/')
        # show signup page
        return self.render_template(request, 'signup.html', {'form':SignupForm()})

    def post(self, request):
        # create a form instance and populate it with data from request
        userForm = SignupForm(request.POST.copy())
        if userForm.is_valid():
            # create a user if valid submission
            newUser = self.saveUser(userForm)
            if newUser:
                login(request, newUser)
                return self.redirect('/author/%(username)s'% {'username': newUser.username})
            else:
                self.render_404("login failed")
        # if form is invalid, show errors
        else:
            return self.render_template(request, 'signup.html', {'form':userForm})

    # saves user to the DB
    def saveUser(self, userForm):
        username = userForm.cleaned_data['username']
        password = userForm.cleaned_data['password']
        email = userForm.cleaned_data['email']
        
        newUser = User.objects.create_user(username, email, password)
        newUser.profile.profile_name = username
        newUser.save()
        user = authenticate(username=username, password=password)
        return user
