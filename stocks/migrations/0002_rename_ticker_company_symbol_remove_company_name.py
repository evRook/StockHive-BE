# Generated by Django 4.2.1 on 2023-05-06 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='ticker',
            new_name='symbol',
        ),
        migrations.RemoveField(
            model_name='company',
            name='name',
        ),
    ]