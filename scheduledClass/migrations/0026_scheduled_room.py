# Generated by Django 2.2.5 on 2019-10-01 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0006_remove_rooms_monday'),
        ('scheduledClass', '0025_auto_20191001_0523'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduled',
            name='room',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.DO_NOTHING, to='rooms.Rooms'),
            preserve_default=False,
        ),
    ]