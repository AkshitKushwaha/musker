from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile

#unregister groups

admin.site.unregister(Group)

# mix profile info into user info

class ProfileInline(admin.StackedInline):
    model = Profile

#extend user model
class UserAdmin(admin.ModelAdmin):
    model = User
    # just display uername fields on admin page
    fields = ["username"]
    inlines = [ProfileInline]

#unregister initial user
admin.site.unregister(User)

#reregister user and profile
admin.site.register(User, UserAdmin)

admin.site.register(Profile)


