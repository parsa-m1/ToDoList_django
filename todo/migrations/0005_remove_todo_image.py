# Generated by Django 5.1.1 on 2024-10-07 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_alter_todo_managers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='image',
        ),
    ]
