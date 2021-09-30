from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user    = models.OneToOneField(User,primary_key = True,on_delete = models.CASCADE)
    status  = models.TextField(max_length = 100, blank = True)
    location= models.TextField(max_length = 50, blank = True)
    image   = models.ImageField(upload_to = 'pics',default = 'pics/download.jpg')

    def __str__(self):
        return self.user.username           #for show user name in database

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.TextField(max_length=300,blank=False)
    date_posted = models.DateField(auto_now=True)

    def __str__(self):
        return self.user.username 

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()