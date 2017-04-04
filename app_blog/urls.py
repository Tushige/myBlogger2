from django.conf.urls import url
from views import homepage
from .views.homepage import HomepageHandler
from .views.newpost import NewpostHandler
from .views.signup import SignupHandler
from .views.signin import SigninHandler
from .views.signout import SignoutHandler
from .views.welcome import WelcomeHandler
from .views.profile import ProfileHandler

urlpatterns = [
    url(r'^$', HomepageHandler.as_view(), name='homepage'),
    url(r'^newpost$',NewpostHandler.as_view(), name='newpost'),
    url(r'^signup$', SignupHandler.as_view(), name='signup'),
    url(r'^signin$', SigninHandler.as_view(), name='signin'),
    url(r'^signout$', SignoutHandler.as_view(), name='signout'),
    url(r'^author/(?P<username>[a-zA-Z0-9_-]{3,20})$', WelcomeHandler.as_view(), name='welcome'),
    url(r'^author/(?P<username>[a-zA-Z0-9_-]{3,20})/profile$', ProfileHandler.as_view(), name='profile'),
]
