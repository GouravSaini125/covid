# Generated by Django 3.0.3 on 2020-03-20 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidApp', '0003_helpline_hospital_testingcenter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='district',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='father_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='state',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]