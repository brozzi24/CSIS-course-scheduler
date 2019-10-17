# Generated by Django 2.2.5 on 2019-10-10 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduledClass', '0031_remove_scheduled_attribute'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduled',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.Classes'),
        ),
        migrations.AlterField(
            model_name='scheduled',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.Rooms'),
        ),
    ]