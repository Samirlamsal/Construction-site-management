# Generated by Django 3.2.4 on 2021-10-04 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construction', '0019_transaction_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkerAttendence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('present', models.BooleanField(default=False)),
            ],
        ),
    ]
