# Generated by Django 5.0.3 on 2024-03-29 07:00

import expenses_tracker.my_validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_alter_userprofile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images/', validators=[expenses_tracker.my_validators.MaxImageSizeValidator(5.0)]),
        ),
    ]
