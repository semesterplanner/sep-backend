# Generated by Django 3.0.3 on 2020-02-22 23:28

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('semesterplaner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday', models.IntegerField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday')], default=0)),
                ('time', models.TimeField(choices=[(datetime.time(9, 0), '9:00'), (datetime.time(9, 15), '9:15'), (datetime.time(11, 0), '11:00'), (datetime.time(13, 30), '13:30'), (datetime.time(15, 15), '15:15'), (datetime.time(17, 0), '17:00')], verbose_name='Starting time')),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='semesterplaner.Lecture')),
            ],
        ),
    ]