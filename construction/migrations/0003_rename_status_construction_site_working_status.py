# Generated by Django 3.2 on 2021-04-19 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('construction', '0002_construction_site_transaction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='construction_site',
            old_name='status',
            new_name='working_status',
        ),
    ]
