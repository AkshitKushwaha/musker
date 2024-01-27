from django.db import models

from django.contrib.auth.models import User

from django.db.models.signals import post_save

#create a meep model
class Meep(models.Model):
    user = models.ForeignKey(User, related_name="meeps", on_delete=models.DO_NOTHING)
    body = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="meep_like", blank=True)

    #Keep count of likes
    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return(
            f"{self.user}"
            f"({self.created_at:%Y-%m-%d %H:%M}): "
            f"{self.body}..."
        )

#create a user profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False, blank=True)

    date_modified = models.DateTimeField(User, auto_now=True)

    profile_image = models.ImageField(null = True, blank = True, upload_to='images/')

    def __str__(self):
        return self.user.username
    

# create a user profile model when New User Signs Up
    
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        #Have he user follow themselves
        user_profile.follows.set([instance.profile.id])
        user_profile.save()


post_save.connect(create_profile, sender=User)