# Generated by Django 4.0.7 on 2022-11-30 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin_calcu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('petrol', models.IntegerField(null=True)),
                ('diesel', models.IntegerField(null=True)),
                ('gas', models.IntegerField(null=True)),
                ('taxi', models.IntegerField(null=True)),
                ('localbus', models.IntegerField(null=True)),
                ('train', models.IntegerField(null=True)),
                ('lpg_cyclinder', models.IntegerField(null=True)),
                ('electricity', models.IntegerField(null=True)),
                ('Total_emission', models.IntegerField(null=True)),
                ('emission_calculate', models.BooleanField(default=False)),
            ],
        ),
    ]
