# Generated by Django 4.2.3 on 2023-07-16 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_system', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(null=True, upload_to='students_data/images'),
        ),
    ]
