# Generated by Django 2.2.6 on 2019-11-21 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='course_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='classes',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]