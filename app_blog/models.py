'''
All DB model classes are defined here
'''
from __future__ import unicode_literals
from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django import forms

# A blog post
class Blog(models.Model):
    blog_title = models.CharField(max_length=200)
    blog_abstract = models.TextField()
    blog_content = models.TextField()
    pub_date = models.DateTimeField('date published')
    # create Many-to-One relationship with a Profile model
    submitter = models.ForeignKey('Profile', on_delete=models.CASCADE, null=True)

# Profile model associated with Django's 'User' model object
class Profile(models.Model):
    # Create relationship with 'User' model
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    biography = models.TextField(max_length=200)
    profile_name = models.CharField(max_length=48)
    occupation = models.CharField(max_length=48)
    employment = models.CharField(max_length=48)

    # Profile will be created/updated in accordance with the User it's related to
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
