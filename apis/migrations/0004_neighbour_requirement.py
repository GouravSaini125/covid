# Generated by Django 3.0.3 on 2020-03-27 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0003_auto_20200326_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='Neighbour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rel', models.CharField(choices=[('N', 'Neighbour'), ('F', 'Friend')], max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('colony', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('house', models.CharField(blank=True, max_length=50, null=True)),
                ('mobile', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rashan', models.CharField(blank=True, max_length=50, null=True)),
                ('gas', models.CharField(blank=True, max_length=50, null=True)),
                ('medical', models.CharField(blank=True, max_length=50, null=True)),
                ('remarks', models.CharField(blank=True, max_length=100, null=True)),
                ('emergency', models.CharField(blank=True, max_length=50, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('colony', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('house', models.CharField(blank=True, max_length=50, null=True)),
                ('mobile', models.IntegerField()),
            ],
        ),
    ]