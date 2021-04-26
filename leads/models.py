from django.db import models

# Create your models here.
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_organizer = models.BooleanField(default= True)
    is_agent = models.BooleanField(default= False)

class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.user.username

class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
# while allowing agents to be null, we arent keeping track of what orgainization nthey fall under 
#  adding field allows tracking of everyone under the same organization
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    agent = models.ForeignKey("Agent", null= True, blank= True, on_delete=models.SET_NULL)

    def __str__(self):
      return f"{self.first_name} {self.last_name}"

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
# object ORM to see string instead of object 
    def __str__(self):
      return self.user.username

def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

# sender is the exact model that is sending the event
post_save.connect(post_user_created_signal, sender=User, weak=True, dispatch_uid=None, apps=None)