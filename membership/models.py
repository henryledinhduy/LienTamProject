from djmoney.models.fields import MoneyField
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profession = models.CharField(max_length=50, default="", blank=True)
    social_number = models.CharField(max_length=14, default="", blank=True)
    phap_danh = models.CharField(max_length=20, blank=True, null=True)
    nationality = models.CharField(max_length=20, default="")
    gender = models.CharField(max_length=10, default="")
    address = models.CharField(max_length=100, default="")
    postal_code = models.IntegerField(default=0)
    city = models.CharField(max_length=10, default="")
    phone = models.IntegerField(default=0)
    phone_following = models.BooleanField(default=False)


    def __str__(self):
        return str(self.user)

class Donation(models.Model):
    person = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    donate_date = models.DateTimeField('date donated')
    amount = MoneyField(max_digits=10, decimal_places=2, default_currency='EUR')

    def __str__(self):
        return str(self.amount)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    """
    This function create the UserProfile table automatically whenever
    the new User object is created.
    """
    if created:
        UserProfile.objects.create(user=instance)
        instance.userprofile.save()
