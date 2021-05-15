# Generated by Django 3.2 on 2021-05-12 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construction', '0013_auto_20210512_1826'),
    ]

    operations = [
        migrations.RenameField(
            model_name='site_user',
            old_name='name',
            new_name='username',
        ),
        migrations.AddField(
            model_name='site_user',
            name='fullname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
