# Generated by Django 4.0.5 on 2022-06-12 13:21

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awwards', '0004_alter_project_date_submited_alter_project_rank'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image'),
        ),
    ]