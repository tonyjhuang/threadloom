from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.
class Topic(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    owner = models.ForeignKey('auth.User', related_name='topics')

    class Meta:
        ordering = ('created',)

class Thread(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='threads')

    class Meta:
        ordering = ('created',)

class Reply(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='replies')

    class Meta:
        ordering = ('created',)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
