from django.conf.urls import url
from views import homepage
from .views.homepage import HomepageHandler
from .views.newpost import NewpostHandler
from .views.blogEntry import BlogEntryHandler
from .views.signup import SignupHandler
from .views.signin import SigninHandler
from .views.signout import SignoutHandler
from .views.profile import ProfileHandler
from .views.editProfile import EditProfileHandler

# namespace for our blog app
app_name = 'app_blog'

# map urls to their view handlers
urlpatterns = [
    url(r'^$', HomepageHandler.as_view(), name='homepage'),
    url(r'^newpost$',NewpostHandler.as_view(), name='newpost'),
    url(r'^blog_entry/(?P<blog_id>[0-9]{1,100})$', BlogEntryHandler.as_view(), name='blog_entry'),
    url(r'^signup$', SignupHandler.as_view(), name='signup'),
    url(r'^signin$', SigninHandler.as_view(), name='signin'),
    url(r'^signout$', SignoutHandler.as_view(), name='signout'),
    url(r'^author/(?P<username>[a-zA-Z0-9_-]{3,20})/$', ProfileHandler.as_view(), name='profile'),
    url(r'^author/(?P<username>[a-zA-Z0-9_-]{3,20})/edit_profile/$', EditProfileHandler.as_view(), name='edit_profile'),
]
