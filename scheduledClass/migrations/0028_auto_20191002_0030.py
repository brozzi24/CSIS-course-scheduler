# Generated by Django 2.2.5 on 2019-10-02 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduledClass', '0027_auto_20191001_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduled',
            name='friday',
            field=models.CharField(blank=True, max_length=1),
        ),
        migrations.AlterField(
            model_name='scheduled',
            name='monday',
            field=models.CharField(blank=True, max_length=1),
        ),
        migrations.AlterField(
            model_name='scheduled',
            name='saturday',
            field=models.CharField(blank=True, max_length=1),
        ),
        migrations.AlterField(
            model_name='scheduled',
            name='sunday',
            field=models.CharField(blank=True, max_length=1),
        ),
        migrations.AlterField(
            model_name='scheduled',
            name='thursday',
            field=models.CharField(blank=True, max_length=1),
        ),
        migrations.AlterField(
            model_name='scheduled',
            name='tuesday',
            field=models.CharField(blank=True, max_length=1),
        ),
        migrations.AlterField(
            model_name='scheduled',
            name='wednesday',
            field=models.CharField(blank=True, max_length=1),
        ),
    ]