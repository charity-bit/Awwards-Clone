# Generated by Django 4.0.5 on 2022-06-12 20:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('awwards', '0006_alter_vote_average_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='date_voted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
