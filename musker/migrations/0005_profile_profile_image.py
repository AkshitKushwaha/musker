# Generated by Django 3.0.5 on 2024-01-12 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musker', '0004_auto_20231219_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]