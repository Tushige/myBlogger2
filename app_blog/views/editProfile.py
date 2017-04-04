from baseView import BaseView

class EditProfileHandler(BaseView):
    def get(self, request, username):
        return self.render_template(request, 'edit_profile.html', {'user': request.user})

    def post(self, request):
        return self.write('thank you')
