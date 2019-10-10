# Generated by Django 2.2.5 on 2019-09-28 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='classes',
            name='subject',
            field=models.CharField(choices=[('CSIS', 'CSIS'), ('CSCI', 'CSCI'), ('INFO', 'INFO'), ('CIS', 'CIS')], max_length=20),
        ),
    ]