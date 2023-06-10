# Generated by Django 4.0.7 on 2022-11-21 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data_analyst_register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254, null=True, unique=True)),
                ('Phone_number', models.PositiveBigIntegerField(null=True, unique=True)),
                ('Password', models.CharField(max_length=50)),
                ('Address', models.CharField(max_length=50)),
            ],
        ),
    ]
