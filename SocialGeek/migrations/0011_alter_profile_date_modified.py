# Generated by Django 5.0.7 on 2024-08-08 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialGeek', '0010_remove_gweek_facebook_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
