# Generated by Django 2.0.3 on 2018-03-11 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0005_auto_20180310_2129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email_following',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profession',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='social_number',
            field=models.CharField(blank=True, default='', max_length=14),
        ),
    ]
