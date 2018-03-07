from django.db import models

class People(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    social_number = models.CharField(max_length=14)

class Donation(models.Model):
    people = models.ForeignKey(People, on_delete=models.CASCADE)
    donate_date = models.DateTimeField('date donated')
    amount = models.IntegerField(default=0)
