from django.db.models.signals import post_save
from django.contrib.auth.models import User #import the sender
from django.dispatch import receiver #import the receiver
from .models import Profile

@receiver(post_save, sender=User) #decorator: when user is saved send signal from user
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance) #create profile with the user instance

@receiver(post_save, sender=User) #decorator: when user is saved send signal from user
def save_profile(sender, instance, **kwargs): #kwargs takes additional arguments
    instance.profile.save()
