# Generated by Django 2.0.3 on 2018-03-13 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_account_atype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='atype',
            new_name='account_type',
        ),
    ]