# Generated by Django 3.0.3 on 2020-04-06 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidApp', '0017_auto_20200406_0352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='decl_date',
        ),
        migrations.AddField(
            model_name='member',
            name='decl_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
