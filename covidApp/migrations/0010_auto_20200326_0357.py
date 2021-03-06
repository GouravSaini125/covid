# Generated by Django 3.0.3 on 2020-03-26 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidApp', '0009_helpline_lang'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('father_name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=7)),
                ('aadhar', models.BigIntegerField()),
                ('is_infected', models.BooleanField()),
                ('diabetes', models.BooleanField()),
                ('symptoms', models.BooleanField()),
                ('cured', models.BooleanField()),
                ('travelled', models.BooleanField()),
                ('from_date', models.DateField(blank=True, null=True)),
                ('to_date', models.DateField(blank=True, null=True)),
                ('latitude', models.DecimalField(decimal_places=10, max_digits=15)),
                ('longitude', models.DecimalField(decimal_places=10, max_digits=15)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='family_infected',
        ),
    ]
