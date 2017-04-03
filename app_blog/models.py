from __future__ import unicode_literals

from django.db import models

# A blog post
class Blog(models.Model):
    blog_title = models.CharField(max_length=200)
    blog_abstract = models.TextField()
    blog_content = models.TextField()
    pub_date = models.DateTimeField('date published')

# A user
class User(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
