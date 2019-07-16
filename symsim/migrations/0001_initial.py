# Generated by Django 2.2.1 on 2019-05-05 13:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Simulation_report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('simulation_id', models.BigIntegerField(default=0)),
                ('system_time', models.BigIntegerField(default=0)),
                ('record_id', models.BigIntegerField(default=0)),
                ('event', models.BigIntegerField(default=0)),
                ('object', models.BigIntegerField(default=0)),
                ('operation', models.BigIntegerField(default=0)),
                ('int1', models.BigIntegerField(default=0)),
                ('int2', models.BigIntegerField(default=0)),
                ('double1', models.FloatField(default=0, max_length=1000)),
                ('double2', models.FloatField(default=0, max_length=1000)),
                ('comment', models.TextField(default='', max_length=150)),
            ],
            options={
                'db_table': 'simulation_report',
            },
        ),
        migrations.CreateModel(
            name='User_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_model',
            },
        ),
        migrations.CreateModel(
            name='Switch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('switch_name', models.TextField()),
                ('sw_capacity', models.FloatField()),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='symsim.User_model')),
            ],
            options={
                'db_table': 'switch',
            },
        ),
        migrations.CreateModel(
            name='Disk_server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disk_server_name', models.TextField(max_length=20)),
                ('disk_pool_size', models.FloatField(max_length=50)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='symsim.User_model')),
            ],
            options={
                'db_table': 'disk_server',
            },
        ),
        migrations.CreateModel(
            name='Data_generator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dg_name', models.TextField(max_length=20)),
                ('freq_data', models.IntegerField(max_length=50)),
                ('data_value', models.IntegerField(max_length=20)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='symsim.User_model')),
            ],
            options={
                'db_table': 'data_generator',
            },
        ),
        migrations.CreateModel(
            name='Computing_node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cn_name', models.TextField()),
                ('ncpu', models.IntegerField()),
                ('cpu_speed', models.IntegerField()),
                ('avr_data_value', models.IntegerField()),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='symsim.User_model')),
            ],
            options={
                'db_table': 'computing_mode',
            },
        ),
    ]