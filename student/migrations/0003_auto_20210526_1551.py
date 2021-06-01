# Generated by Django 3.2.3 on 2021-05-26 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_rename_student_attendance_pupil'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='state',
            new_name='week1',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='week',
        ),
        migrations.AddField(
            model_name='attendance',
            name='week2',
            field=models.CharField(blank=True, choices=[('yet', 'yet'), ('attend', 'attend'), ('late', 'late'), ('absent', 'absent')], default='yet', max_length=100),
        ),
        migrations.AddField(
            model_name='attendance',
            name='week3',
            field=models.CharField(blank=True, choices=[('yet', 'yet'), ('attend', 'attend'), ('late', 'late'), ('absent', 'absent')], default='yet', max_length=100),
        ),
        migrations.AddField(
            model_name='attendance',
            name='week4',
            field=models.CharField(blank=True, choices=[('yet', 'yet'), ('attend', 'attend'), ('late', 'late'), ('absent', 'absent')], default='yet', max_length=100),
        ),
    ]