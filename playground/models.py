from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
class UserProfile(models.Model):
    profile_user=models.OnetoOneField(User,on_delete=models.CASCADE)
    profile_img=models.ImageField(default='images/default.png')
@receiver(post_save,sender=User)
def update_profile_signal(sender,instance,created,**kwarg):
    if created:
        UserProfile.objects.create(profile_user=instance)
    instance.userprofile.save()

