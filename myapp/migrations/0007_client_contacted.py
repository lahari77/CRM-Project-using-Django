# Generated by Django 3.2 on 2021-10-16 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_myuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='contacted',
            field=models.CharField(default='No', max_length=10),
        ),
    ]
