# Generated by Django 4.2.3 on 2023-07-10 21:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trips', '0002_rename_visitedplace_visited'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Visited',
            new_name='VisitedPlace',
        ),
    ]