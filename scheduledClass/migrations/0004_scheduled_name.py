# Generated by Django 2.2.5 on 2019-09-30 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduledClass', '0003_auto_20190930_0114'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduled',
            name='name',
            field=models.CharField(default='programming', max_length=100),
            preserve_default=False,
        ),
    ]
