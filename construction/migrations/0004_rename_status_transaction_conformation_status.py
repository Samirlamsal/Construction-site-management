# Generated by Django 3.2 on 2021-04-19 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('construction', '0003_rename_status_construction_site_working_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='status',
            new_name='conformation_status',
        ),
    ]
