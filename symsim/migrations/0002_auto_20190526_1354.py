# Generated by Django 2.2.1 on 2019-05-26 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symsim', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data_generator',
            name='data_value',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='data_generator',
            name='dg_name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='data_generator',
            name='freq_data',
            field=models.IntegerField(),
        ),
        migrations.AlterModelTable(
            name='computing_node',
            table='computing_node',
        ),
    ]
