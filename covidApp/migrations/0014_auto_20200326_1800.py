# Generated by Django 3.0.3 on 2020-03-26 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidApp', '0013_auto_20200326_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='testingcenter',
            name='is_operational',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='testingcenter',
            name='type',
            field=models.CharField(default='rt', max_length=50),
            preserve_default=False,
        ),
    ]
