# Generated by Django 2.2.5 on 2019-09-29 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.IntegerField(unique=True)),
                ('room_type', models.CharField(max_length=20)),
                ('capcity', models.IntegerField()),
            ],
        ),
    ]
