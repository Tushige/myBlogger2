from __future__ import unicode_literals
from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# A blog post
class Blog(models.Model):
    blog_title = models.CharField(max_length=200)
    blog_abstract = models.TextField()
    blog_content = models.TextField()
    pub_date = models.DateTimeField('date published')
    submitter = models.ForeignKey('Profile', on_delete=models.CASCADE, null=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    biography = models.TextField(max_length=200)
    profile_name = models.CharField(max_length=64)
    occupation = models.CharField(max_length=64)
    employment = models.CharField(max_length=64)

    # Profile will be created/updated in accordance with the User it's related to
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
