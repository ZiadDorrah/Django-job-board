from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver  # add this
from django.db.models.signals import post_save
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.ForeignKey(
        'City', on_delete=models.CASCADE, null=True, blank=True)
    phone_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to='profile/')

    def __str__(self):
        return str(self.user)

    # def __str__(self):
    #     return self.user


@receiver(post_save, sender=User)  # add this
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


class City(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
