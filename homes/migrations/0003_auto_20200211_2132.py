# Generated by Django 2.1.15 on 2020-02-11 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0002_controlstate'),
    ]

    operations = [
        migrations.CreateModel(
            name='LightState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_created=True, auto_now=True)),
                ('name', models.CharField(help_text='Name', max_length=200)),
                ('state', models.CharField(choices=[('on', 'On'), ('off', 'Off')], default='off', help_text='Current state of the light.', max_length=3)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RoomState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_created=True, auto_now=True)),
                ('name', models.CharField(help_text='Name', max_length=200)),
                ('current_temperature', models.DecimalField(decimal_places=2, help_text='Current temperature at the thermostat.', max_digits=5)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ThermostatState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_created=True, auto_now=True)),
                ('name', models.CharField(help_text='Name', max_length=200)),
                ('mode', models.CharField(choices=[('off', 'Off'), ('fan', 'Fan'), ('auto', 'Auto'), ('cool', 'Cool'), ('heat', 'Heat')], default='off', help_text='Current mode of the thermostat.', max_length=5)),
                ('current_temperature', models.DecimalField(decimal_places=2, help_text='Current temperature at the thermostat.', max_digits=5)),
                ('temperature_set_point', models.DecimalField(decimal_places=2, help_text='Temperature set point.', max_digits=5)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='ControlState',
        ),
    ]
