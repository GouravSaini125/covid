# Generated by Django 3.0.3 on 2020-04-17 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0013_home'),
    ]

    operations = [
        migrations.AddField(
            model_name='precaution',
            name='is_lockdown',
            field=models.BooleanField(default=False),
        ),
    ]