# Generated by Django 5.0.6 on 2024-05-19 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manage_institute', '0002_rename_clubs_club'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='books',
            new_name='Book',
        ),
    ]