'''
Contains helper functions to retrieve objects from the database
'''
from django.contrib.auth.models import User
from app_blog.models import Blog

# determines if user exists with the specified 'username'
def userExists(username):
    return User.objects.filter(username=username).exists()

# returns a 'user' model object with the specified 'username'
def getUserByUsername(username):
    return User.objects.get(username=username)

# returns the last 'count' blogs by 'user'
def getBlogsForUser(user, count):
    return user.profile.blog_set.all().order_by('-pub_date')[:count]

# returns the latest 'count' blogs
def getBlogs(count):
    return Blog.objects.all().order_by('-pub_date')[:count]
