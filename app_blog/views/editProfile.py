from baseView import BaseView

class EditProfileHandler(BaseView):
    def get(self, request):
        return self.redner_template(request, 'edit_profile.html', {})
