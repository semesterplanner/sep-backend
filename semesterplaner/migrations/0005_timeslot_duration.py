# Generated by Django 3.0.3 on 2020-02-28 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semesterplaner', '0004_timeslot_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeslot',
            name='duration',
            field=models.IntegerField(choices=[(45, 45), (90, 90), (135, 135), (180, 180), (225, 225), (270, 270), (315, 315), (360, 360)], default=90),
        ),
    ]
