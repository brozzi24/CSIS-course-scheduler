# Generated by Django 2.2.5 on 2019-10-17 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduledClass', '0036_auto_20191017_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduled',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduledClass.Semester'),
        ),
    ]
