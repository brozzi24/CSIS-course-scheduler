# Generated by Django 2.2.5 on 2019-10-01 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduledClass', '0017_remove_scheduled_room'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheduled',
            name='name',
        ),
    ]