# Generated by Django 4.0.5 on 2022-06-17 00:59

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awwards', '0019_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/dvhid4k2j/image/upload/v1655420766/annie-spratt-0ZPSX_mQ3xI-unsplash_s1pxcj.jpg', max_length=255, verbose_name='profile_image'),
        ),
    ]