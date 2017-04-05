'''
View controller class for the 'edit profile' page
'''
from baseView import BaseView
from app_blog.forms.profileForm import ProfileForm

class EditProfileHandler(BaseView):
    def get(self, request, username):
        # create the submission form and render it
        form = ProfileForm()
        return self.render_template(request, 'edit_profile.html', {
                                    'user': request.user,
                                    'form': form
                                    })

    def post(self, request, username):
        # get user form submission
        userForm = ProfileForm(request.POST.copy())
        # save changes if valid submission
        if userForm.is_valid():
            self.updateUserProfile(userForm)
        # if invalid, show errors
        return self.redirect('/author/%(username)s' % {'username': username})

    # helper function to update user profile fields
    def updateUserProfile(self, userForm):
        # retrieve submission data
        name = userForm.cleaned_data['name']
        occupation = userForm.cleaned_data['occupation']
        employment = userForm.cleaned_data['employment']
        biography = userForm.cleaned_data['biography']
        modified = False
        # update user profile fields
        if name:
            self.request.user.profile.profile_name = name
            modified = True
        if occupation:
            self.request.user.profile.occupation = occupation
            modified = True
        if employment:
            self.request.user.profile.employment = employment
            modified = True
        if biography:
            self.request.user.profile.biography = biography
            modified = True

        # save to DB only if 1 or more fields were changed
        if modified:
            self.request.user.save()
