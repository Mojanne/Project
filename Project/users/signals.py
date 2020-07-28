from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


# User model is our sender, which means it is gonna send the signal. **kwargs allows you to handle named arguments
# that you have not defined in advance.In a function call, keyword arguments must follow positional arguments.All the
# keyword arguments passed must match one of the arguments accepted by the function
# for profile creation
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# for saving profile
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
