# Generated by Django 4.2.3 on 2023-07-16 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_post_posted_by_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='posted_by_user',
        ),
    ]
