# Generated by Django 3.0.3 on 2020-03-29 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0004_neighbour_requirement'),
    ]

    operations = [
        migrations.AddField(
            model_name='govtdata',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='govtdata',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True),
        ),
    ]
