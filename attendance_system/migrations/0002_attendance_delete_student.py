# Generated by Django 4.2.3 on 2023-07-09 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_system', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_number', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('entrance_time', models.TimeField()),
            ],
            options={
                'unique_together': {('seat_number', 'date')},
            },
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
