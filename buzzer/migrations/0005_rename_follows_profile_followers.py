# Generated by Django 5.1.6 on 2025-02-26 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buzzer', '0004_profile_date_modified'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='follows',
            new_name='followers',
        ),
    ]
