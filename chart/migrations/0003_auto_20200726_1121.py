# Generated by Django 2.2.5 on 2020-07-26 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0002_auto_20200726_1108'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Temp_controll_env',
            new_name='Temp_controller_env',
        ),
        migrations.AlterModelOptions(
            name='temp_controller_env',
            options={'verbose_name_plural': 'Temp_controller_env'},
        ),
    ]
