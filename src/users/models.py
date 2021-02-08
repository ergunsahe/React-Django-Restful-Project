
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def user_profile_path(instance, filename):
    return 'user/{0}/{1}'.format(instance.user.id, filename)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(blank= True, max_length=200)
    last_name = models.CharField(blank= True, max_length=200)
    country = models.CharField(blank= True, max_length=200)
    address = models.CharField(blank= True, max_length=200)
    phone = models.CharField(blank= True, max_length=200)
    image = models.URLField(max_length=5000, default="avatar.png")
    bio = models.TextField(blank=True)
    
    def __str__(self):
        return "{} {}".format(self.user.username, "Profile")