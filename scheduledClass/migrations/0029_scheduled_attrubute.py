# Generated by Django 2.2.5 on 2019-10-02 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduledClass', '0028_auto_20191002_0030'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduled',
            name='attrubute',
            field=models.CharField(default='UNGR', max_length=4),
        ),
    ]