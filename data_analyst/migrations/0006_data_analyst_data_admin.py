# Generated by Django 4.0.7 on 2022-12-03 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_analyst', '0005_alter_data_analyst_data_output'),
    ]

    operations = [
        migrations.AddField(
            model_name='data_analyst_data',
            name='admin',
            field=models.BooleanField(default=False),
        ),
    ]
