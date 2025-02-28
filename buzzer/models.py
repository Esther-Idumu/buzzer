from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver

# Create buzz model


class Buzz(models.Model):
    user = models.ForeignKey(
        User, related_name="buzzes",
        on_delete=models.DO_NOTHING
        )
    body = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return(
                f"{self.user}"
                f"({self.created_at:%Y-%m-%d %H:%M}):"
                f"{self.body}..."
                )

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)   # OneToOneField is a relationship where a user has only one profile, on_delete=models.CASCADE means if a user is deleted, the profile is also deleted
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False, blank=True)  # ManyToManyField is a relationship where a user can follow many profiles and a profile can be followed by many users

    date_modified = models.DateTimeField(User, auto_now=True)


    def __str__(self):
        return self.user.username

    def follower_count(self):
        return self.followers.count()

    def following_count(self):
        return self.following.count()

# Create a profile for each user


#post_save.connect(create_profile, sender=User)  # When a user is created, create a profile for them

