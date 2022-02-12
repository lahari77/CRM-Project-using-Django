# Generated by Django 3.2 on 2021-10-12 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=60, unique=True)),
                ('lastname', models.CharField(max_length=60)),
                ('mobilenumber', models.IntegerField(unique=True)),
                ('email', models.EmailField(max_length=60, unique=True)),
                ('dob', models.DateField(null=True)),
                ('address', models.CharField(max_length=60)),
                ('gender', models.CharField(max_length=6)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=60)),
                ('lastname', models.CharField(max_length=60)),
                ('mobile', models.IntegerField(unique=True)),
                ('address', models.TextField(null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('gender', models.CharField(max_length=6)),
                ('dob', models.DateField(null=True)),
                ('city', models.CharField(max_length=60, null=True)),
                ('state', models.CharField(max_length=60, null=True)),
                ('occupation', models.CharField(max_length=60, null=True)),
                ('source', models.CharField(max_length=60, null=True)),
                ('agent', models.CharField(max_length=60, null=True)),
                ('follow_up_date', models.DateField(null=True)),
                ('remarks', models.TextField(blank=True, max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_name', models.CharField(max_length=120, unique=True)),
                ('property_type', models.CharField(max_length=60)),
                ('area', models.CharField(max_length=60)),
                ('price', models.FloatField()),
                ('no_of_bedrooms', models.PositiveIntegerField()),
                ('no_of_bathrooms', models.PositiveIntegerField()),
                ('location', models.CharField(max_length=50)),
            ],
        ),
    ]