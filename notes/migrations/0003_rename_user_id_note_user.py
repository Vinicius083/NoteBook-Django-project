# Generated by Django 5.1.6 on 2025-02-22 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_rename_user_note_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='user_id',
            new_name='user',
        ),
    ]
