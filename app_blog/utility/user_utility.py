from django.contrib.auth.models import User


# determines if user exists with the specified username
def userExists(username):
    return User.objects.filter(username=username).exists()

def getUserByUsername(username):
    return User.objects.get(username=username)
