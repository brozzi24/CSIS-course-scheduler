# Generated by Django 2.2.5 on 2019-09-28 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0004_auto_20190928_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='grad_type',
            field=models.CharField(choices=[('UNGR', 'Undergraduate'), ('GRAD', 'Graduate')], max_length=20),
        ),
    ]