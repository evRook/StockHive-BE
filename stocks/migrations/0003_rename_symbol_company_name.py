# Generated by Django 4.2.1 on 2023-05-06 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0002_rename_ticker_company_symbol_remove_company_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='symbol',
            new_name='Name',
        ),
    ]