# Generated by Django 3.0.3 on 2020-04-03 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0005_auto_20200329_0723'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighbour',
            name='gender',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='requirement',
            name='feedback',
            field=models.TextField(blank=True, null=True),
        ),
    ]
