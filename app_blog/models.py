from __future__ import unicode_literals

from django.db import models

# A blog post
class Blog(models.Model):
    blog_title = models.CharField(max_length=200)
    blog_abstract = models.TextField()
    blog_content = models.TextField()
    pub_date = models.DateTimeField('date published')
    submitter = models.ForeignKey('User', on_delete=models.CASCADE)

# A user model that describes a 'user'
class User(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    email = models.EmailField(max_length=32)
    created = models.DateTimeField('date published')
    #
    profile_name = models.CharField(max_length=32)
    occupation = models.CharField(max_length=32)
    employment = models.CharField(max_length=32)
    biography = models.TextField()
