# Generated by Django 2.2.6 on 2019-10-18 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classes', '0001_initial'),
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(max_length=20, unique=True)),
                ('default', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Scheduled',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.IntegerField(blank=True)),
                ('end_time', models.IntegerField(blank=True)),
                ('flex', models.IntegerField(default=1)),
                ('crn', models.IntegerField()),
                ('offering', models.IntegerField()),
                ('name', models.CharField(blank=True, max_length=100)),
                ('banner_id', models.CharField(blank=True, max_length=100)),
                ('primary', models.CharField(blank=True, max_length=100)),
                ('monday', models.CharField(blank=True, max_length=1)),
                ('tuesday', models.CharField(blank=True, max_length=1)),
                ('wednesday', models.CharField(blank=True, max_length=1)),
                ('thursday', models.CharField(blank=True, max_length=1)),
                ('friday', models.CharField(blank=True, max_length=1)),
                ('saturday', models.CharField(blank=True, max_length=1)),
                ('sunday', models.CharField(blank=True, max_length=1)),
                ('building', models.CharField(default='8', max_length=5)),
                ('campus', models.CharField(default='M', max_length=5)),
                ('delivery', models.CharField(default='TR', max_length=2)),
                ('notes', models.CharField(blank=True, max_length=200)),
                ('capacity', models.IntegerField(blank=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.Classes')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.Rooms')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduledClass.Semester')),
            ],
        ),
    ]
