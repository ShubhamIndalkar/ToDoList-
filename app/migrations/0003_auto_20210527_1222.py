# Generated by Django 3.2.2 on 2021-05-27 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_task_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='taskDesc',
            new_name='Description',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='taskTitle',
            new_name='Title',
        ),
    ]
