# Generated by Django 5.0.7 on 2024-08-07 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialGeek', '0003_gweek'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
