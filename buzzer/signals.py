
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile.objects.create(user=instance)
        user_profile.save()
        # Have the user follow themselves
        user_profile.follows.add(user_profile)
        user_profile.save()

post_save.connect(create_profile, sender=User)  # When a user is created, create a profile for them