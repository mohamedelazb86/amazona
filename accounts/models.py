from django.db import models
from django.contrib.auth.models import User
from utils.generate_code import generate_code
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user=models.OneToOneField(User,related_name='profile_user',on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images')
    code=models.CharField(max_length=75,default=generate_code)

    def __str__(self):
        return str(self.user)
    

# create new profile if create new user by signals

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(
            user=instance
        )
    

