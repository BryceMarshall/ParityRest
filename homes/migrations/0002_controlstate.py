# Generated by Django 2.1.15 on 2020-02-11 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ControlState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('controlType', models.TextField(choices=[('Thermostat', 'Thermostat'), ('Light', 'Light')])),
                ('state', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
