# Generated by Django 3.0.3 on 2020-04-12 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0011_auto_20200405_0646'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyBasis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=150)),
                ('district', models.CharField(max_length=150)),
                ('area', models.CharField(max_length=150)),
                ('ward', models.CharField(max_length=150)),
                ('date', models.CharField(max_length=150)),
                ('authority', models.CharField(max_length=150)),
                ('contact', models.CharField(max_length=150)),
                ('post', models.CharField(max_length=150)),
                ('food', models.CharField(max_length=150)),
                ('vegetable', models.CharField(max_length=150)),
                ('ration', models.CharField(max_length=150)),
                ('farmer', models.CharField(max_length=150)),
                ('milk', models.CharField(max_length=150)),
                ('other', models.CharField(max_length=150)),
                ('announcement', models.TextField()),
                ('remarks', models.TextField()),
            ],
        ),
    ]