# Generated by Django 2.2.5 on 2019-10-16 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduledClass', '0034_auto_20191011_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduled',
            name='capacity',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
