from django.db import models
from djmoney.models.fields import MoneyField

# Phan nay anh dang lam chua xong, 

class People(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    social_number = models.CharField(max_length=14, unique=True)
    phap_danh = models.CharField(max_length=20)
    nationality = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)

class Donation(models.Model):
    people = models.ForeignKey(People, on_delete=models.CASCADE)
    donate_date = models.DateTimeField('date donated')
    amount = models.IntegerField(default=0)

class Contact(models.Model):
    people = models.ForeignKey(People, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=50)

class Setting(models.Model):
    people = models.ForeignKey(People, on_delete=models.CASCADE)
    email_receive = models.BooleanField(default=False)
    phone_receive = models.BooleanField(default=False)
