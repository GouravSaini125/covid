# Generated by Django 3.0.3 on 2020-04-05 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0010_auto_20200405_0645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='govtdata',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='govtdata',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True),
        ),
    ]
