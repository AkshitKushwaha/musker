# Generated by Django 3.0.5 on 2023-12-19 13:45

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('musker', '0003_meap'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Meap',
            new_name='Meep',
        ),
    ]