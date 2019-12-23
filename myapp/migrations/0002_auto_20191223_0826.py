# Generated by Django 2.2.5 on 2019-12-23 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieSearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search', models.CharField(max_length=500)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Moive Searches',
            },
        ),
        migrations.RenameModel(
            old_name='Search',
            new_name='BookSearch',
        ),
        migrations.AlterModelOptions(
            name='booksearch',
            options={'verbose_name_plural': 'Book Searches'},
        ),
    ]
