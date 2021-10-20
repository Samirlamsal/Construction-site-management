# Generated by Django 3.2.4 on 2021-10-11 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('construction', '0028_worker_site'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worker',
            name='site',
        ),
        migrations.AddField(
            model_name='on_duty',
            name='site',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='construction.construction_site'),
        ),
    ]
