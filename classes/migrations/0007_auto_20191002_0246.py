# Generated by Django 2.2.5 on 2019-10-02 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0006_classes_fixed_hours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='fixed_hours',
            field=models.IntegerField(default=0),
        ),
    ]