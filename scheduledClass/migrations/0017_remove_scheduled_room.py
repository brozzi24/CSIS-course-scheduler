# Generated by Django 2.2.5 on 2019-10-01 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduledClass', '0016_remove_scheduled_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheduled',
            name='room',
        ),
    ]