from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile, Buzz

#Unregister Groups
admin.site.unregister(Group)

# Mix profile info into user info
class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    # Just display username fields
    fields = ['username']
    inlines = [ProfileInline]

# Unregister initial User
admin.site.unregister(User)

# Register User
admin.site.register(User, UserAdmin)
#admin.site.register(Profile)

# Register Buzzes
admin.site.register(Buzz)
