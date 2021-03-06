# Generated by Django 3.0.3 on 2020-04-17 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0012_dailybasis'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('aadhar', models.BigIntegerField()),
                ('image', models.ImageField(upload_to='home/')),
                ('address', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('from_district', models.CharField(max_length=100)),
                ('to_district', models.CharField(max_length=100)),
                ('from_state', models.CharField(max_length=100)),
                ('to_state', models.CharField(max_length=100)),
                ('date_of_journey', models.DateField()),
                ('reason', models.CharField(max_length=100)),
                ('have_tested', models.BooleanField()),
                ('have_infected', models.BooleanField()),
                ('mobile_number', models.BigIntegerField()),
                ('is_approved', models.BooleanField(default=False)),
                ('approval_date', models.DateField(null=True)),
            ],
        ),
    ]
