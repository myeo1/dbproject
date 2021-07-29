# Generated by Django 3.2.5 on 2021-07-24 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='DriverRecords',
            fields=[
                ('points', models.IntegerField()),
                ('valid_driving_licence', models.BooleanField()),
                ('number_of_accidents', models.IntegerField()),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='dbapp.owner')),
            ],
        ),
        migrations.CreateModel(
            name='Offenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=1000)),
                ('penalty', models.CharField(max_length=20)),
                ('points', models.IntegerField(default=0)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbapp.owner')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=20)),
                ('fuel_type', models.CharField(max_length=20)),
                ('registration', models.CharField(max_length=20)),
                ('power', models.IntegerField()),
                ('transmission', models.CharField(max_length=20)),
                ('make', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=20)),
                ('number_of_seats', models.CharField(max_length=20)),
                ('engine_cubic_capacity', models.CharField(max_length=20)),
                ('emission_class', models.CharField(max_length=5)),
                ('fuel_consumption', models.IntegerField()),
                ('production_date', models.DateField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbapp.owner')),
            ],
        ),
    ]
