# Generated by Django 3.1.7 on 2021-04-21 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CIVILjobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=70)),
                ('year_of_experience', models.IntegerField()),
                ('job_description', models.TextField()),
                ('job_role', models.CharField(max_length=80)),
                ('location', models.CharField(max_length=80)),
                ('package', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ITjobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=70)),
                ('year_of_experience', models.IntegerField()),
                ('job_description', models.TextField()),
                ('job_role', models.CharField(max_length=80)),
                ('location', models.CharField(max_length=80)),
                ('package', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='MECHjobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=70)),
                ('year_of_experience', models.IntegerField()),
                ('job_description', models.TextField()),
                ('job_role', models.CharField(max_length=80)),
                ('location', models.CharField(max_length=80)),
                ('package', models.FloatField()),
            ],
        ),
    ]
